# Full Analysis — ACE-EG01-MEMORY-001

**Experiment status:** PASS
**H1 threshold result:** SUPPORTED
**H3 threshold result:** SUPPORTED
**Evidence Gate 1:** PASS
**Execution commit:** `7421ee7f1c9e02acf09577d52e20f588936e9b45`
**Run timestamp:** `20260911T145240Z`
**CPU affinity:** Logical CPU 0
**Trials:** Nine per condition and size
**Recorded rows:** 468
**Checksum failures:** 0

## Experimental question

How do access order, locality and address dependency affect memory-access performance as the working set grows?

## Conditions

- A_DIRECT: direct sequential traversal.
- B_SEQ_INDEX: independent indexed traversal in sequential order.
- C_RANDOM_INDEX: independent indexed traversal through a random permutation.
- D_POINTER_CHASE: dependent traversal in which each loaded value determines the next address.

B and C form the primary controlled comparison. They use the same indexed-loop structure, equal data and index sizes, and equal combined working-set footprints. Their principal difference is index order: sequential versus randomly permuted.

D introduces address dependency and therefore tests exposed load latency when out-of-order execution cannot generate multiple future addresses.

A provides useful sequential context, but it is not the primary causal control because its index footprint and generated work differ from B and C.

## Results

| Nominal size | A ns/access | B ns/access | C ns/access | D ns/access | C/B | D/C |
|---:|---:|---:|---:|---:|---:|---:|
| 16 KiB | 0.3896 | 0.3916 | 0.3906 | 1.2285 | 0.997 | 3.145 |
| 32 KiB | 0.3884 | 0.3831 | 0.3902 | 1.6573 | 1.019 | 4.247 |
| 64 KiB | 0.3895 | 0.3940 | 0.3951 | 2.3814 | 1.003 | 6.028 |
| 256 KiB | 0.3923 | 0.4436 | 0.4186 | 3.5832 | 0.944 | 8.560 |
| 1 MiB | 0.3978 | 0.4453 | 0.4887 | 6.0769 | 1.097 | 12.435 |
| 2 MiB | 0.4242 | 0.5035 | 0.6132 | 10.6584 | 1.218 | 17.383 |
| 4 MiB | 0.4025 | 0.5799 | 0.9553 | 17.0292 | 1.647 | 17.826 |
| 8 MiB | 0.4359 | 0.8619 | 1.4174 | 24.6417 | 1.645 | 17.385 |
| 16 MiB | 0.4811 | 0.8743 | 2.2302 | 50.3350 | 2.551 | 22.570 |
| 32 MiB | 0.5411 | 0.8498 | 3.2069 | 103.2635 | 3.774 | 32.200 |
| 64 MiB | 0.5300 | 0.8358 | 4.3521 | 121.8745 | 5.207 | 28.003 |
| 128 MiB | 0.5304 | 0.9013 | 5.6539 | 130.7469 | 6.273 | 23.125 |
| 256 MiB | 0.4783 | 0.8156 | 6.6127 | 133.3845 | 8.107 | 20.171 |

The size column is the nominal data size. B, C and D also use an equally sized index structure, so their combined footprints are twice the nominal values.

## Registered threshold adjudication

H1 requires C/B to exceed 1.10 at each of the three largest registered sizes.

| Nominal size | Combined B/C footprint | C/B | Decision |
|---:|---:|---:|---|
| 64 MiB | 128 MiB | 5.207 | PASS |
| 128 MiB | 256 MiB | 6.273 | PASS |
| 256 MiB | 512 MiB | 8.107 | PASS |

**H1 result:** SUPPORTED under the preregistered threshold rule.

H3 requires D/C to exceed 1.25 at each of the three largest registered sizes.

| Nominal size | D/C | Decision |
|---:|---:|---|
| 64 MiB | 28.003 | PASS |
| 128 MiB | 23.125 | PASS |
| 256 MiB | 20.171 | PASS |

**H3 result:** SUPPORTED under the preregistered threshold rule.

The 256 KiB C/B reversal does not affect H1 because it lies outside the predefined adjudication set. It does reject an overly broad claim that random indexing must be slower at every working-set size.

## Mechanistic interpretation

C/B remains near unity through 1 MiB, reaches 1.218 at 2 MiB and remains above 1.64 from 4 MiB onward. This is consistent with the random permutation progressively losing the cache-line utilization and prefetchability available to sequential indexed traversal.

Both B and C preserve independent loads. The processor can therefore use out-of-order execution and memory-level parallelism to overlap work. C becomes slower as unpredictable accesses create more costly misses, waste more transferred cache-line data and eventually pressure the finite structures that track outstanding memory operations.

D is different. Each next address depends on the preceding load result. The processor cannot discover and issue later requests early enough to overlap their latency. D therefore shifts the experiment from independent-miss throughput toward serialized load-to-use latency.

At large sizes, D approaches approximately 103–133 ns/access while C remains approximately 3.21–6.61 ns/access. This is consistent with D exposing much more of the underlying memory latency and C amortizing latency across multiple concurrent misses.

## Dispersion and caution

Elevated within-run dispersion appears in the intermediate regime:

- B IQR: 15.2% at 2 MiB.
- C IQR: 15.9% at 2 MiB.
- B IQR: 13.4% at 8 MiB.
- B IQR: 14.1% at 16 MiB.
- D IQR: 10.1% at 4 MiB.

These measurements support a transition-region interpretation but not a precise cache-boundary claim. Frequency state, interrupts, background activity, cache and TLB state, page placement, trial history and hybrid-core topology remain possible contributors.

## Non-claims

This experiment does not:

- locate exact L1, L2 or last-level-cache boundaries;
- prove that one unique mechanism caused every observed transition;
- identify D's plateau as a universal DRAM-latency constant;
- verify P-core versus E-core placement for logical CPU 0;
- provide hardware-counter confirmation of cache misses, TLB misses or stalled cycles;
- establish portability beyond the recorded machine and software environment.

## Engineering conclusion

For this machine and implementation, sequential indexed traversal substantially outperformed random indexed traversal at the three largest registered sizes. Dependent pointer chasing was slower still because it prevented effective overlap of future loads.

The results demonstrate the practical distinction between:

- locality and poor locality;
- predictable and unpredictable address order;
- independent miss throughput and dependent-load latency;
- mathematical work and the hardware cost of feeding that work with data.

The experiment supports H1 and H3. Evidence Gate 1 remains pending until the CPU-to-GPU transfer explanation and sprint synthesis are completed.

## Artifact integrity

- Full CSV: `full-20260911-165240.csv`
- CSV SHA256: `2D2D28EA5BF03970718C65C0E102954B15D2212E18E2DD3A3AD2D08AB0052861`
- Full metadata: `full-20260911-165240.metadata.json`
- Metadata SHA256: `4EBF8B58C577C2F25CCB8507D1EF07D1707B06610D86FE075373EE473BEA84B7`
