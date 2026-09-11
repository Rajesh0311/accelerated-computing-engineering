# Research Question

Can working-set size, access order and load dependency explain measurable differences in CPU memory-access performance on the tested Intel Core Ultra 9 275HX system?

## Primary causal comparison

Compare sequential-indirect access with random-independent access.

Both conditions read:

1. one precomputed index;
2. one indexed data element;
3. every data element exactly once.

This reduces the unequal-instruction-work problem present in a direct-sequential versus indirect-random comparison.

## Secondary comparisons

- Direct sequential versus sequential indirect
- Random independent versus dependent pointer chasing

## Prediction

Expected fastest-to-slowest order for working sets larger than the last-level cache:

**direct sequential → sequential indirect → random independent → dependent pointer chase**

Random-independent access may outperform pointer chasing because independent misses can overlap through out-of-order execution and memory-level parallelism. Pointer chasing makes each next address depend on the previous load and therefore exposes more of the memory latency.
