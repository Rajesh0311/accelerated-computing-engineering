# Threat Model — Benchmark Validity

## Critical threats

| Threat | Potential distortion | Control |
|---|---|---|
| JIT compilation | Inflated first trial | Compile and validate before timing |
| Dead-code elimination | Missing memory work | Consume and verify checksums |
| Unequal index work | False locality attribution | Use B versus C as primary comparison |
| Invalid random sampling | Repeated accesses and accidental hits | Use verified permutations |
| CPU migration | Different cache and core behaviour | Fix and record process affinity |
| Hybrid core topology | P-core/E-core performance mixture | Use one fixed logical processor; do not assume its type |
| Thermal or boost drift | Time-order bias | AC power, warm-up and interleaved trial order |
| Background applications | Outliers and contention | Record environment and retain trial distribution |
| Cache contamination | Condition-order bias | Deterministically randomize condition order |
| Page faults | Inflated cold measurements | Allocate and pre-touch outside timing |
| Compiler/vectorization differences | Confounded mechanism | Inspect Numba signatures and later generated code |
| Floating-point reassociation | Incorrect equivalence conclusion | Fixed tolerance and checksum checks |
| Working-set misclassification | False cache-boundary claim | Report nominal sizes without asserting exact boundaries |
| Power-plan behaviour | Frequency variability | Record active plan; do not silently change it |

## Interpretation boundary

This experiment characterizes the tested laptop, operating system, runtime, power configuration and implementation.

It does not establish universal cache latencies or general performance for all Intel processors.
