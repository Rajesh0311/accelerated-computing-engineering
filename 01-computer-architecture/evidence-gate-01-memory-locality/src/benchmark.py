from __future__ import annotations

import argparse
import csv
import gc
import json
import math
import os
import platform
import random
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import numba
import numpy as np
import psutil
from numba import njit


EXPERIMENT_ID = "ACE-EG01-MEMORY-001"
CONDITIONS = ("A_DIRECT", "B_SEQ_INDEX", "C_RANDOM_INDEX", "D_POINTER_CHASE")

SMOKE_SIZES_BYTES = (
    16 * 1024,
    1 * 1024 * 1024,
    64 * 1024 * 1024,
)

FULL_SIZES_BYTES = (
    16 * 1024,
    32 * 1024,
    64 * 1024,
    256 * 1024,
    1 * 1024 * 1024,
    2 * 1024 * 1024,
    4 * 1024 * 1024,
    8 * 1024 * 1024,
    16 * 1024 * 1024,
    32 * 1024 * 1024,
    64 * 1024 * 1024,
    128 * 1024 * 1024,
    256 * 1024 * 1024,
)


@njit(cache=True)
def direct_sum(data: np.ndarray, repeats: int) -> float:
    total = 0.0
    for _ in range(repeats):
        for i in range(data.size):
            total += data[i]
    return total


@njit(cache=True)
def indexed_sum(
    data: np.ndarray,
    indices: np.ndarray,
    repeats: int,
) -> float:
    total = 0.0
    for _ in range(repeats):
        for i in range(indices.size):
            total += data[indices[i]]
    return total


@njit(cache=True)
def pointer_chase_sum(
    data: np.ndarray,
    next_indices: np.ndarray,
    start_index: int,
    repeats: int,
) -> tuple[float, int]:
    total = 0.0
    current = start_index

    for _ in range(repeats):
        for _ in range(next_indices.size):
            total += data[current]
            current = next_indices[current]

    return total, current


@njit(cache=True)
def touch_eviction_buffer(buffer: np.ndarray) -> float:
    total = 0.0
    elements_per_cache_line = 8

    for i in range(0, buffer.size, elements_per_cache_line):
        total += buffer[i]

    return total


def make_data(element_count: int) -> np.ndarray:
    return np.arange(element_count, dtype=np.float64) % 1024.0


def make_sequential_indices(element_count: int) -> np.ndarray:
    return np.arange(element_count, dtype=np.int64)


def make_random_permutation(
    element_count: int,
    rng: np.random.Generator,
) -> np.ndarray:
    indices = np.arange(element_count, dtype=np.int64)
    rng.shuffle(indices)
    return indices


def make_single_cycle(
    permutation: np.ndarray,
) -> tuple[np.ndarray, int]:
    if permutation.ndim != 1:
        raise ValueError("Permutation must be one-dimensional.")

    if permutation.size == 0:
        raise ValueError("Permutation must not be empty.")

    next_indices = np.empty_like(permutation)
    next_indices[permutation[:-1]] = permutation[1:]
    next_indices[permutation[-1]] = permutation[0]

    return next_indices, int(permutation[0])


def validate_permutation(indices: np.ndarray) -> None:
    expected = np.arange(indices.size, dtype=np.int64)

    if not np.array_equal(np.sort(indices), expected):
        raise ValueError("Index array is not a complete permutation.")


def validate_single_cycle(
    next_indices: np.ndarray,
    start_index: int,
) -> None:
    visited = np.zeros(next_indices.size, dtype=np.bool_)
    current = start_index

    for _ in range(next_indices.size):
        if current < 0 or current >= next_indices.size:
            raise ValueError("Pointer chain contains an invalid index.")

        if visited[current]:
            raise ValueError("Pointer chain repeated before visiting every element.")

        visited[current] = True
        current = int(next_indices[current])

    if current != start_index:
        raise ValueError("Pointer chain did not return to its start.")

    if not bool(np.all(visited)):
        raise ValueError("Pointer chain did not visit every element.")


def expected_sum(data: np.ndarray, repeats: int) -> float:
    return float(np.sum(data, dtype=np.float64)) * repeats


def checksum_matches(observed: float, expected: float) -> bool:
    return math.isclose(
        observed,
        expected,
        rel_tol=1e-12,
        abs_tol=1e-9,
    )


def git_head(repo_root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


@dataclass(frozen=True)
class TrialResult:
    experiment_id: str
    timestamp_utc: str
    git_head: str
    mode: str
    seed: int
    cpu_affinity: int
    size_bytes: int
    element_count: int
    index_bytes: int
    combined_working_set_bytes: int
    condition: str
    trial: int
    execution_order: int
    repeats: int
    accesses: int
    elapsed_ns: int
    ns_per_access: float
    useful_gib_per_second: float
    checksum_observed: float
    checksum_expected: float
    checksum_pass: bool


def condition_order(trials: int, seed: int) -> list[str]:
    order = list(CONDITIONS) * trials
    chooser = random.Random(seed)
    chooser.shuffle(order)
    return order


def run_trial(
    condition: str,
    data: np.ndarray,
    sequential_indices: np.ndarray,
    random_indices: np.ndarray,
    next_indices: np.ndarray,
    pointer_start: int,
    repeats: int,
) -> tuple[float, int | None, int]:
    start_ns = time.perf_counter_ns()

    if condition == "A_DIRECT":
        checksum = direct_sum(data, repeats)
        final_index = None
    elif condition == "B_SEQ_INDEX":
        checksum = indexed_sum(data, sequential_indices, repeats)
        final_index = None
    elif condition == "C_RANDOM_INDEX":
        checksum = indexed_sum(data, random_indices, repeats)
        final_index = None
    elif condition == "D_POINTER_CHASE":
        checksum, final_index = pointer_chase_sum(
            data,
            next_indices,
            pointer_start,
            repeats,
        )
    else:
        raise ValueError(f"Unknown condition: {condition}")

    elapsed_ns = time.perf_counter_ns() - start_ns
    return float(checksum), final_index, elapsed_ns


def warm_up_jit() -> None:
    data = make_data(64)
    sequential = make_sequential_indices(64)
    rng = np.random.default_rng(1)
    permutation = make_random_permutation(64, rng)
    next_indices, start = make_single_cycle(permutation)
    eviction = np.ones(1024, dtype=np.float64)

    direct_sum(data, 1)
    indexed_sum(data, sequential, 1)
    indexed_sum(data, permutation, 1)
    pointer_chase_sum(data, next_indices, start, 1)
    touch_eviction_buffer(eviction)


def write_csv(path: Path, rows: list[TrialResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(asdict(rows[0]).keys()),
        )
        writer.writeheader()

        for row in rows:
            writer.writerow(asdict(row))


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="ACE Evidence Gate 1 memory-locality benchmark."
    )
    parser.add_argument(
        "--mode",
        choices=("smoke", "full"),
        default="smoke",
    )
    parser.add_argument(
        "--cpu",
        type=int,
        default=0,
        help="Logical processor used for process affinity.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=20260911,
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()

    process = psutil.Process()
    available_cpus = process.cpu_affinity()

    if args.cpu not in available_cpus:
        raise SystemExit(
            f"Requested CPU {args.cpu} is not available. "
            f"Available CPUs: {available_cpus}"
        )

    process.cpu_affinity([args.cpu])

    if process.cpu_affinity() != [args.cpu]:
        raise SystemExit("Failed to apply the requested CPU affinity.")

    mode_config = {
        "smoke": {
            "sizes": SMOKE_SIZES_BYTES,
            "trials": 3,
            "target_accesses": 250_000,
            "eviction_bytes": 64 * 1024 * 1024,
        },
        "full": {
            "sizes": FULL_SIZES_BYTES,
            "trials": 9,
            "target_accesses": 2_000_000,
            "eviction_bytes": 128 * 1024 * 1024,
        },
    }[args.mode]

    repo_root = Path(__file__).resolve().parents[3]
    current_git_head = git_head(repo_root)

    print(f"Experiment: {EXPERIMENT_ID}")
    print(f"Mode: {args.mode}")
    print(f"Git HEAD: {current_git_head}")
    print(f"Python: {sys.version.split()[0]}")
    print(f"NumPy: {np.__version__}")
    print(f"Numba: {numba.__version__}")
    print(f"Platform: {platform.platform()}")
    print(f"CPU affinity: {process.cpu_affinity()}")
    print(f"Output: {args.output}")

    warm_up_jit()

    eviction_count = mode_config["eviction_bytes"] // 8
    eviction = np.ones(eviction_count, dtype=np.float64)
    eviction_guard = touch_eviction_buffer(eviction)

    rows: list[TrialResult] = []
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    gc.disable()

    try:
        for size_bytes in mode_config["sizes"]:
            element_count = size_bytes // 8
            repeats = max(
                1,
                math.ceil(mode_config["target_accesses"] / element_count),
            )

            data = make_data(element_count)
            sequential_indices = make_sequential_indices(element_count)

            rng = np.random.default_rng(args.seed + size_bytes)
            random_indices = make_random_permutation(element_count, rng)
            validate_permutation(random_indices)

            next_indices, pointer_start = make_single_cycle(random_indices)
            validate_single_cycle(next_indices, pointer_start)

            expected = expected_sum(data, repeats)
            trial_counts = {condition: 0 for condition in CONDITIONS}
            order = condition_order(
                mode_config["trials"],
                args.seed + size_bytes,
            )

            print(
                f"Size={size_bytes} bytes; "
                f"elements={element_count}; repeats={repeats}"
            )

            for execution_order, condition in enumerate(order, start=1):
                trial_counts[condition] += 1

                eviction_guard += touch_eviction_buffer(eviction)

                checksum, final_index, elapsed_ns = run_trial(
                    condition=condition,
                    data=data,
                    sequential_indices=sequential_indices,
                    random_indices=random_indices,
                    next_indices=next_indices,
                    pointer_start=pointer_start,
                    repeats=repeats,
                )

                checksum_pass = checksum_matches(checksum, expected)

                if (
                    condition == "D_POINTER_CHASE"
                    and final_index != pointer_start
                ):
                    checksum_pass = False

                if not checksum_pass:
                    raise RuntimeError(
                        f"Correctness failure: size={size_bytes}, "
                        f"condition={condition}, "
                        f"observed={checksum}, expected={expected}, "
                        f"final_index={final_index}"
                    )

                accesses = element_count * repeats
                ns_per_access = elapsed_ns / accesses
                seconds = elapsed_ns / 1_000_000_000
                useful_gib_per_second = (
                    accesses * data.itemsize / seconds / (1024**3)
                )

                index_bytes = (
                    0 if condition == "A_DIRECT"
                    else sequential_indices.nbytes
                )

                rows.append(
                    TrialResult(
                        experiment_id=EXPERIMENT_ID,
                        timestamp_utc=timestamp,
                        git_head=current_git_head,
                        mode=args.mode,
                        seed=args.seed,
                        cpu_affinity=args.cpu,
                        size_bytes=size_bytes,
                        element_count=element_count,
                        index_bytes=index_bytes,
                        combined_working_set_bytes=size_bytes + index_bytes,
                        condition=condition,
                        trial=trial_counts[condition],
                        execution_order=execution_order,
                        repeats=repeats,
                        accesses=accesses,
                        elapsed_ns=elapsed_ns,
                        ns_per_access=ns_per_access,
                        useful_gib_per_second=useful_gib_per_second,
                        checksum_observed=checksum,
                        checksum_expected=expected,
                        checksum_pass=checksum_pass,
                    )
                )

            del data
            del sequential_indices
            del random_indices
            del next_indices

    finally:
        gc.enable()

    if not rows:
        raise RuntimeError("No benchmark rows were produced.")

    write_csv(args.output, rows)

    metadata_path = args.output.with_suffix(".metadata.json")
    metadata = {
        "experiment_id": EXPERIMENT_ID,
        "timestamp_utc": timestamp,
        "git_head": current_git_head,
        "mode": args.mode,
        "seed": args.seed,
        "cpu_affinity": args.cpu,
        "sizes_bytes": list(mode_config["sizes"]),
        "trials_per_condition": mode_config["trials"],
        "target_accesses": mode_config["target_accesses"],
        "eviction_bytes": mode_config["eviction_bytes"],
        "conditions": list(CONDITIONS),
        "rows": len(rows),
        "eviction_guard": eviction_guard,
    }

    metadata_path.write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Rows written: {len(rows)}")
    print(f"CSV: {args.output}")
    print(f"Metadata: {metadata_path}")
    print("Benchmark status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
