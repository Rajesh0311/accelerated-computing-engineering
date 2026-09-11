# Evidence Gate 1 — Memory Locality

Experiment: `ACE-EG01-MEMORY-001`

Read in this order:

1. `QUESTION.md`
2. `PREREGISTRATION.md`
3. `THREAT_MODEL.md`
4. `environment.json`
5. `src/benchmark.py`
6. `tests/test_benchmark.py`

## Execution stages

### Tests

Run correctness and structural tests before producing results.

### Smoke benchmark

Uses three working-set sizes and three trials per condition. Its purpose is implementation validation, not hypothesis adjudication.

### Full benchmark

Uses the preregistered size sweep and nine trials per condition.

Do not run the full benchmark until:

- tests pass;
- smoke results pass correctness checks;
- smoke output has been inspected;
- the implementation commit has been published.

## Evidence boundary

The Numba implementation produces native machine code through LLVM but does not replace the required later C/C++ reproduction.

No result should be generalized beyond the recorded machine, operating system, runtime, affinity and power configuration.
