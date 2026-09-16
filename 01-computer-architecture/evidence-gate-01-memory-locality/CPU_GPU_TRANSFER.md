# Evidence Gate 1 — CPU-to-GPU Transfer

**Transfer assessment:** PASS
**GPU experiment executed:** NO — deferred to the CUDA phase
**Evidence Gate 1:** PASS

## Transfer objective

The CPU memory-locality experiment established that identical or closely comparable mathematical work can produce substantially different execution times because of:

- address order;
- spatial locality;
- working-set size;
- cache and translation behaviour;
- memory-level parallelism;
- load dependency;
- the hardware's ability to overlap memory operations.

These mechanisms transfer conceptually to GPU engineering. The CPU measurements do not directly prove GPU performance and their numerical ratios must not be projected onto a GPU.

## CPU-to-GPU mechanism map

| CPU experiment mechanism | GPU analogue | Expected performance consequence |
| --- | --- | --- |
| Direct sequential traversal | Contiguous and aligned lane accesses | Efficient memory transactions and high useful bandwidth |
| Sequential indexed traversal | Predictable indexed access | Some additional instruction and index-traffic cost |
| Independent randomized indexing | Uncoalesced or scattered global-memory access | Additional memory transactions and reduced useful bandwidth |
| Dependent pointer chasing | Result-dependent address generation | Serialized access and exposed load-to-use latency |
| Independent cache misses | Independent requests from lanes and warps | Memory latency can be overlapped |
| Increasing working-set size | Data exceeding useful GPU cache capacity | Greater dependence on lower cache levels and device memory |
| CPU cache locality | GPU cache-line and transaction locality | Data layout materially affects achieved performance |

## Coalescing

A GPU executes threads in groups called warps. When adjacent lanes access adjacent, suitably aligned words, the hardware can combine those lane requests into a small number of memory transactions.

When lanes access widely scattered addresses, substantially more memory transactions may be required to retrieve the same amount of useful data.

The operation count can remain unchanged while the memory-system cost increases.

The CPU experiment therefore supports this falsifiable GPU prediction:

> For sufficiently large working sets, a coalesced CUDA kernel should achieve greater useful memory throughput than a semantically equivalent randomized-gather kernel.

This is a mechanism-level prediction, not a claim that the CPU and GPU slowdown ratios will match.

## Latency hiding and occupancy

Condition C contained independent accesses. This allowed the processor to overlap multiple memory operations.

Condition D used a dependency chain. The address of the next load was unavailable until the preceding load completed. This prevented effective memory-level parallelism and exposed substantially more latency.

A GPU uses a related latency-hiding strategy. When one warp is waiting for memory, a streaming multiprocessor can issue instructions from another eligible warp.

The ability to hide latency depends on:

- the number of eligible warps;
- block configuration;
- register consumption;
- shared-memory consumption;
- instruction dependencies;
- memory-system capacity;
- occupancy constraints.

Occupancy is an enabling condition, not an independent performance objective. High occupancy cannot repair inefficient transactions or remove a true pointer-chasing dependency.

## Pointer-chasing transfer

A CUDA pointer-chasing kernel should expose more memory latency than an independent randomized-gather kernel because each next address depends on the preceding result.

Additional active warps may hide some latency across warps, but they cannot remove the dependency inside each individual chain.

This makes pointer chasing a useful future diagnostic for distinguishing:

- throughput from latency;
- independent misses from serialized misses;
- occupancy from genuinely eligible work;
- cache-resident behaviour from large-footprint memory behaviour.

## Why sequential access is not sufficient

Sequential access alone does not guarantee strong GPU performance.

Performance also depends on:

- alignment;
- access width;
- lane-to-address mapping;
- transaction utilization;
- register pressure;
- shared-memory pressure;
- instruction dependencies;
- active and eligible warps;
- cache behaviour;
- memory bandwidth;
- compiler-generated instructions.

The transferable engineering principle is:

> Arrange memory accesses so the hardware can retrieve useful data with efficient transactions while maintaining enough independent work to hide unavoidable latency.

## Proposed CUDA experiment

### Research question

How do coalescing, address randomness and dependency chaining affect GPU memory performance across working-set sizes?

### Conditions

1. `A_COALESCED` — consecutive lanes access consecutive aligned elements.
2. `B_STRIDED` — lanes access elements using controlled increasing strides.
3. `C_RANDOM_GATHER` — lanes perform independent randomized gathers.
4. `D_POINTER_CHASE` — each next address depends on the preceding load.

### Controlled variables

- same GPU;
- same driver and CUDA runtime;
- same data type;
- same useful-access count;
- same correctness checksum;
- same compiler configuration;
- same clock and power policy where controllable;
- same block-size policy unless block size is the tested variable;
- warm-up before measurement;
- randomized condition order;
- repeated trials.

### Required measurements

- kernel elapsed time;
- nanoseconds per useful access;
- useful GiB/s;
- achieved memory bandwidth;
- global-memory transaction efficiency;
- cache-hit measurements where supported;
- active and eligible warps;
- achieved occupancy;
- memory-pipeline utilization;
- correctness checksum.

### Predictions

For working sets exceeding useful cache capacity:

1. coalesced access will provide the highest useful throughput;
2. strided access will degrade as lane requests require more transactions;
3. randomized gathering will reduce useful transaction efficiency;
4. pointer chasing will expose the strongest dependency and latency penalty.

### Correctness rule

Every implementation must produce the preregistered expected result.

A faster kernel with an incorrect checksum is a failed experiment.

### Falsification conditions

The transfer hypothesis must be revised if controlled measurements show that:

- randomized gathering consistently matches coalesced useful bandwidth;
- transaction measurements do not differ as predicted;
- pointer chasing shows no dependency penalty after compiler elimination and cache residency are controlled;
- the measured ordering disappears across repeated runs;
- profiler evidence contradicts the proposed mechanism.

## Evidence boundary

The completed experiment demonstrates CPU memory-hierarchy and dependency effects on this machine and implementation.

It does not yet demonstrate:

- GPU coalescing performance;
- GPU cache capacities;
- GPU device-memory latency;
- GPU occupancy effects;
- CUDA pointer-chasing behaviour.

Those remain testable predictions for the CUDA phase.

## Sources

- NVIDIA CUDA Programming Guide — Writing SIMT Kernels: https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html
- NVIDIA CUDA C++ Best Practices Guide: https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html

## Transfer conclusion

The completed CPU experiment supports the following reusable performance chain:

**address pattern → transaction behaviour → available parallelism → latency hiding → observed performance**

The CPU-to-GPU transfer assessment passes because the observed mechanisms have been translated into technically bounded, falsifiable CUDA predictions without claiming that CPU evidence directly proves GPU behaviour.
