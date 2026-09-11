# Smoke Validation — ACE-EG01-MEMORY-001

**Adjudication:** PASS WITH CAUTION
**Scope:** Implementation validation only
**Evidence Gate 1:** NOT YET PASSED
**Full-run authorization:** PENDING RECORD VALIDATION

## Verified facts

- The benchmark completed successfully.
- It produced all 36 expected rows.
- No checksum failures occurred.
- Process affinity was restricted to logical CPU 0.
- The recorded implementation commit was `d3e037b727e3d4956549dd0ed0549689216b8fff`.
- All four preregistered access conditions executed.

## Observed smoke results

| Working set | Comparison | Ratio | Interpretation |
|---:|---|---:|---|
| 16 KiB | D/C | 3.17x | Dependency serialization is visible even in the small-set regime. |
| 1 MiB | C/B | 1.04x | No stable locality effect is claimed because B showed high variability. |
| 64 MiB | C/B | 4.55x | Independent random indexing was substantially slower than sequential indexed traversal. |
| 64 MiB | D/C | 26.75x | Dependent pointer chasing exposed latency that independent misses could partially overlap. |

## Mechanistic interpretation

At the smallest nominal working-set size, A, B and C converged because expensive lower-level misses were not persistent enough to dominate execution. D remained slower because each next address depended on the preceding load, restricting out-of-order overlap and memory-level parallelism.

At 64 MiB, B benefited from sequential cache-line use, predictable access and hardware prefetching. C lost most of that regularity and useful cache-line consumption, although its independent addresses still permitted multiple misses to overlap.

D was slower than C because D serialized address discovery. C primarily measures random-access throughput with independent misses; D more directly exposes dependent-load latency.

## Reliability caution

The 1 MiB B condition ranged from 0.6657 to 1.3657 ns/access. This warns that trial duration, frequency state, background activity, cache/TLB state, trial order or another uncontrolled factor materially affected the intermediate regime.

The full run must preserve raw trial-level results and use the preregistered nine trials per condition. Averaging must not conceal multimodal or high-variance behaviour.

## Explicit non-claims

- The smoke run does not confirm the preregistered hypotheses.
- The three smoke sizes do not locate L1, L2 or LLC boundaries.
- The nominal data size is not necessarily the total effective footprint of each condition.
- Logical CPU 0 has not been verified as a P-core or E-core.
- No single mechanism has been proven to explain the observed ratios.
- Exact ratios are not treated as portable architectural constants.

## Authorization decision

The implementation is suitable for a preregistered full run after this record and its associated smoke artifacts pass repository validation.

## Artifact integrity

- CSV: `smoke-20260911-150509.csv`
- CSV SHA256: `2E74A57010B267AFCB072F4E67D37963C728B93212E9964BBEA49F1C62405582`
- Metadata: `smoke-20260911-150509.metadata.json`
- Metadata SHA256: `D283EFA4BB2496B452F1850992777714EEC7493D1A9DEF6656321F6D563FD9C7`
