# Evidence Gate 1 — Final Synthesis

**Experiment:** ACE-EG01-MEMORY-001
**Gate:** CPU / Cache / Memory Behaviour
**Gate adjudication:** PASS
**Adjudication date:** 16 September 2026
**Computer Architecture sprint:** REMAINS ACTIVE

## Engineering conclusion

Programs performing the same or closely comparable mathematical work can have substantially different execution times because operation count does not capture the cost of supplying instructions and data to the execution units.

Observed performance depends on:

- address order and locality;
- working-set size;
- cache and translation behaviour;
- prefetch effectiveness;
- instruction dependencies;
- out-of-order execution;
- memory-level parallelism;
- latency and bandwidth.

## Experimental evidence

The full experiment recorded:

- 13 working-set sizes;
- 4 access conditions;
- 9 trials per condition;
- 468 observations;
- zero checksum failures;
- randomized execution order;
- fixed logical-CPU affinity;
- preregistered hypotheses and thresholds.

At the three largest preregistered sizes:

| Size | Random/Sequential | Pointer chase/Random |
| ---: | ---: | ---: |
| 64 MiB | 5.207× | 28.003× |
| 128 MiB | 6.273× | 23.125× |
| 256 MiB | 8.107× | 20.171× |

H1 and H3 were supported at every preregistered decision size.

## Locality

Sequential indexed access and randomized indexed access both use independent indexed loads. Their comparison therefore isolates address order and locality more effectively than a comparison involving pointer chasing.

At large working sets, randomized access was substantially slower. The evidence supports the conclusion that locality-friendly access uses the memory hierarchy and memory subsystem more efficiently.

The transition between approximately 2 MiB and 16 MiB must not be described as an exact cache boundary. Cache residency, associativity, translation, prefetching, memory-level parallelism and runtime noise may all contribute.

The 256 KiB reversal does not alter H1 because it lies outside the preregistered largest-three decision set.

## Latency and throughput

Random independent access can sustain multiple outstanding memory operations. The processor can overlap some of their latency.

Pointer chasing creates a dependency chain. Each next address becomes known only after the preceding load completes.

This explains why large-working-set randomized access measured approximately 4–7 ns per completed access while pointer chasing reached approximately 103–133 ns per access.

The randomized measurement represents amortized throughput under concurrency. The pointer-chasing measurement exposes substantially more serialized load-to-use latency.

The pointer-chasing values are consistent with large-footprint memory latency but are not a pure universal measurement of DRAM latency.

## Out-of-order execution

Out-of-order execution allows a processor to issue ready independent instructions while earlier instructions wait.

It cannot bypass a true dependency. A pointer-chasing load must resolve before its successor address is available.

## Why faster arithmetic is insufficient

Faster arithmetic cannot accelerate a program whose dominant bottleneck is data movement, cache misses, memory latency, bandwidth, branching, dependency or synchronization.

Execution units cannot produce useful work when the required operands are unavailable.

## CPU-to-GPU transfer

The reusable performance chain is:

**address pattern → transaction behaviour → available parallelism → latency hiding → observed performance**

The corresponding GPU hypotheses are:

- contiguous lane access should encourage coalesced memory transactions;
- scattered access should reduce transaction efficiency;
- independent requests may allow latency hiding across eligible warps;
- pointer chasing should expose dependent-load latency;
- occupancy can enable latency hiding but cannot remove true dependencies.

These are falsifiable CUDA predictions. The CPU ratios do not directly predict GPU ratios.

## Limitations

The experiment did not directly record:

- processor frequency per trial;
- hardware performance counters;
- physical cache residency;
- NUMA or physical-page placement;
- whether logical processor 0 was a performance or efficiency core.

These limitations constrain the scope of the conclusions but do not invalidate the preregistered within-machine comparisons.

## Evidence integrity

- Full CSV: `results/full-20260911-165240.csv`
- CSV SHA256: `2D2D28EA5BF03970718C65C0E102954B15D2212E18E2DD3A3AD2D08AB0052861`
- Metadata: `results/full-20260911-165240.metadata.json`
- Metadata SHA256: `4EBF8B58C577C2F25CCB8507D1EF07D1707B06610D86FE075373EE473BEA84B7`
- Analysis: `FULL_ANALYSIS.md`
- Transfer record: `CPU_GPU_TRANSFER.md`
- Preregistration: `PREREGISTRATION.md`
- Threat model: `THREAT_MODEL.md`

## Adjudication

Evidence Gate 1 passes because the evidence demonstrates the ability to:

- design and preregister a controlled experiment;
- execute it reproducibly;
- validate computational correctness;
- distinguish locality from dependency;
- distinguish latency from throughput;
- explain observed performance through architecture;
- identify threats to validity;
- translate CPU mechanisms into bounded GPU hypotheses.

This decision closes Evidence Gate 1 only.

The overall Computer Architecture sprint remains active until all remaining learning, notes, diagnostic assessment, progress updates and sprint exit requirements are completed.
