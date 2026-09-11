# Preregistration — Evidence Gate 1 Memory Locality

**Experiment ID:** ACE-EG01-MEMORY-001
**Preregistration date:** 11 September 2026
**Status:** PREREGISTERED — NOT YET EXECUTED
**Evidence target:** E3 controlled comparison
**Current implementation:** Python 3.11 with Numba/LLVM native compilation
**Required later reproduction:** C or C++

## Research objective

Determine how access order, working-set size and dependency structure affect measured CPU memory-access performance.

## Conditions

### A — Direct sequential

Read `data[i]` in increasing index order.

Purpose: practical best-case baseline.

### B — Sequential indirect

Read `data[sequential_indices[i]]`.

Purpose: control for index-array loading and indirect addressing.

### C — Random independent

Read `data[random_permutation[i]]`.

Purpose: measure the effect of randomized data access while retaining independent loads.

### D — Dependent pointer chase

Use the current loaded index to determine the next address.

Purpose: expose latency when memory-level parallelism is restricted by a dependency chain.

## Primary comparison

**B versus C**

Both conditions use a precomputed index array and perform equal numbers of indexed data accesses.

## Secondary comparisons

- A versus B: cost of indirect indexing
- C versus D: independent misses versus serialized dependent misses

## Working-set sweep

Data-array sizes:

- 16 KiB
- 32 KiB
- 64 KiB
- 256 KiB
- 1 MiB
- 2 MiB
- 4 MiB
- 8 MiB
- 16 MiB
- 32 MiB
- 64 MiB
- 128 MiB
- 256 MiB

Report both:

- data-array bytes;
- combined data-plus-index bytes for indirect conditions.

Do not equate nominal cache capacity with an exact transition boundary.

## Fixed parameters

- Data type: float64
- Index type: int64
- Random seed: fixed and recorded
- Every indexed condition uses a permutation with exactly one visit per element
- Allocation, initialization, permutation generation and JIT compilation occur outside timed regions
- Process affinity is fixed for measured trials
- Selected logical processor is recorded; performance/efficiency core type is not assumed unless independently verified
- Laptop remains connected to AC power
- Active Windows power plan is recorded
- Conditions are interleaved using a deterministic randomized trial order
- At least nine measured trials per condition and size
- A checksum is consumed and validated after every trial

## Metrics

Primary:

- median nanoseconds per access

Secondary:

- elapsed time
- useful accesses per second
- useful-data GiB/s
- trial distribution
- p95 trial time
- ratio C/B
- ratio D/C
- checksum correctness
- coefficient of variation
- CPU affinity
- active power plan

## Hypotheses

### H1 — Sequential locality

For working sets exceeding the effective private-cache regime, condition B will have lower median nanoseconds per access than condition C.

### H2 — Size-dependent divergence

The C/B ratio will tend to increase as the combined working set moves beyond private caches and the last-level cache.

The transition may be gradual and is not required to coincide exactly with reported cache capacity.

### H3 — Dependency penalty

For large working sets, condition D will be slower than condition C because pointer chasing restricts memory-level parallelism.

### H4 — Mechanism consistency

Observed timing changes should be consistent with cache-line utilization, prefetchability, memory-level parallelism and address-translation effects.

Hardware-counter attribution is deferred until suitable tooling is available.

## Hypothesis-support thresholds

H1 is supported if C/B exceeds 1.10 for each of the three largest completed working-set sizes.

H3 is supported if D/C exceeds 1.25 for each of the three largest completed working-set sizes.

These thresholds determine hypothesis support, not whether Evidence Gate 1 passes.

A correct, reproducible null result remains valid evidence.

## Correctness criteria

- A, B and C must produce equivalent sums within a preregistered floating-point tolerance.
- D must visit every element exactly once.
- Generated permutations must contain every valid index exactly once.
- No timed result is accepted if its checksum fails.
- JIT compilation time must never enter a measured trial.
- Results must identify the exact environment and package versions.

## Falsification and null-result conditions

The locality hypothesis is weakened if B and C remain reproducibly equivalent beyond the last-level-cache regime after controlling indexing work, affinity, warm-up and trial order.

The dependency hypothesis is weakened if C and D remain reproducibly equivalent for the largest working sets.

Any failure of permutation validity, checksum validity, timing integrity or repeatability invalidates the affected run.

## Scope exclusions

The first experiment does not claim to isolate:

- huge-page effects;
- precise TLB event counts;
- NUMA effects;
- DRAM row-buffer behaviour;
- branch-prediction behaviour;
- multithread scaling;
- operating-system-independent behaviour;
- cross-machine generality.

These require later experiments.

## Evidence-gate pass criteria

Evidence Gate 1 requires:

1. reproducible implementation;
2. passing correctness tests;
3. completed working-set sweep;
4. raw results preserved;
5. summary results generated from raw data;
6. observed mechanisms interpreted without overclaiming;
7. nulls and failures retained;
8. limitations documented;
9. later C/C++ reproduction recorded as outstanding or completed.

Hypothesis confirmation is not required for the evidence gate to pass.
