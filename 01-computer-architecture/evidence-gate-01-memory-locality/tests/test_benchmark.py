from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

import benchmark


def test_random_indices_are_complete_permutation() -> None:
    rng = np.random.default_rng(123)
    indices = benchmark.make_random_permutation(1024, rng)

    benchmark.validate_permutation(indices)

    assert np.array_equal(
        np.sort(indices),
        np.arange(1024, dtype=np.int64),
    )


def test_single_cycle_visits_every_element_once() -> None:
    rng = np.random.default_rng(456)
    permutation = benchmark.make_random_permutation(2048, rng)
    next_indices, start = benchmark.make_single_cycle(permutation)

    benchmark.validate_single_cycle(next_indices, start)

    visited = set()
    current = start

    for _ in range(next_indices.size):
        visited.add(current)
        current = int(next_indices[current])

    assert len(visited) == next_indices.size
    assert current == start


def test_all_conditions_produce_correct_checksum() -> None:
    element_count = 4096
    repeats = 3
    data = benchmark.make_data(element_count)
    sequential = benchmark.make_sequential_indices(element_count)

    rng = np.random.default_rng(789)
    permutation = benchmark.make_random_permutation(element_count, rng)
    next_indices, start = benchmark.make_single_cycle(permutation)

    expected = benchmark.expected_sum(data, repeats)

    observed_a = benchmark.direct_sum(data, repeats)
    observed_b = benchmark.indexed_sum(data, sequential, repeats)
    observed_c = benchmark.indexed_sum(data, permutation, repeats)
    observed_d, final_index = benchmark.pointer_chase_sum(
        data,
        next_indices,
        start,
        repeats,
    )

    assert benchmark.checksum_matches(observed_a, expected)
    assert benchmark.checksum_matches(observed_b, expected)
    assert benchmark.checksum_matches(observed_c, expected)
    assert benchmark.checksum_matches(observed_d, expected)
    assert final_index == start


def test_condition_order_is_balanced_and_reproducible() -> None:
    first = benchmark.condition_order(trials=9, seed=42)
    second = benchmark.condition_order(trials=9, seed=42)

    assert first == second

    for condition in benchmark.CONDITIONS:
        assert first.count(condition) == 9


def test_smoke_and_full_size_sets_are_ordered() -> None:
    assert tuple(sorted(benchmark.SMOKE_SIZES_BYTES)) == (
        benchmark.SMOKE_SIZES_BYTES
    )
    assert tuple(sorted(benchmark.FULL_SIZES_BYTES)) == (
        benchmark.FULL_SIZES_BYTES
    )
    assert benchmark.FULL_SIZES_BYTES[-1] == 256 * 1024 * 1024
