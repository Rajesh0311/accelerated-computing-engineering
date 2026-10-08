# Accelerated Computing Engineer (ACE)

**Foundation Sprint 0 (replanned):** 7 October–30 November 2026  
**Formal ACE core start:** 1 December 2026  
**Target completion:** 31 October 2027

This directory is the control centre for the Accelerated Computing Engineer programme.

The schedule was revised on 23 September 2026 due to unforeseen circumstances. The [locked baseline](./00-programme/ACE_LOCKED_BASELINE.md#schedule-lock) records the date reconciliation: the full core now runs December 2026–October 2027, with capstone integration and evidence closure in September–October 2027. The locked curriculum, hours, prerequisites and evidence gates remain unchanged. Earlier study and completed evidence retain their actual dates and credit.

The objective is to develop demonstrable competence across:

- Computer architecture
- Parallel computing
- High-performance computing
- CUDA
- GPU performance engineering
- NVIDIA accelerated computing
- AMD ROCm / HIP
- TPU / JAX
- Compiler systems
- Distributed accelerators
- ML systems
- AI infrastructure performance economics

---

# Programme Control Files

## Master Atlas
[00-programme/ACE_ATLAS.md](./00-programme/ACE_ATLAS.md)

**Start here.** Single-view programme atlas covering courses, links, sequence, hours, target dates, evidence gates and current status.

## Roadmap
[ACE_ROADMAP.md](./ACE_ROADMAP.md)

Defines:
- programme phases
- sequence
- expected effort
- technical focus
- evidence gates
- final capstone

## Progress Dashboard
[ACE_PROGRESS.md](./ACE_PROGRESS.md)

Tracks:
- current phase
- hours completed
- target windows
- evidence-gate status
- overall programme progress
- October 2027 completion target

## Competency Matrix
[ACE_COMPETENCY_MATRIX.md](./ACE_COMPETENCY_MATRIX.md)

Defines:
- Level 0 — Unfamiliar
- Level 1 — Foundational
- Level 2 — Working
- Level 3 — Strong
- Level 4 — Engineer-Level

Used to distinguish course completion from actual engineering competence.

## Daily Execution
[TODAY.md](./TODAY.md)

Daily operating loop:

**LEARN → BUILD → MEASURE → EXPLAIN → COMMIT**

---

# Programme Phases

1. Computer Architecture
2. Parallel Computing
3. High-Performance Computing
4. CUDA Core
5. GPU Performance Engineering
6. Advanced HPC
7. AMD ROCm / HIP
8. TPU / JAX
9. Compiler Systems
10. Distributed Accelerators
11. AI Workload Internals
12. Cross-Accelerator Capstone

---

# Directory Structure

```text
ace/
│
├── README.md
├── ACE_ROADMAP.md
├── ACE_PROGRESS.md
├── ACE_COMPETENCY_MATRIX.md
├── TODAY.md
│
├── 01-computer-architecture/
├── 02-parallel-computing/
├── 03-cuda/
├── 04-profiling/
├── 05-hpc/
├── 06-amd-rocm/
├── 07-tpu-jax/
├── 08-compilers/
├── 09-distributed/
├── 10-ml-systems/
└── 11-capstone/
Completion Standard

The programme is not complete because courses are marked DONE.

Completion requires:

all 12 evidence gates passed
reproducible labs committed
benchmark evidence recorded
profiling evidence recorded
CUDA competence demonstrated
AMD portability demonstrated
TPU/JAX competence demonstrated
compiler/Triton competence demonstrated
distributed accelerator competence demonstrated
transformer workload performance analysed
final cross-accelerator capstone completed
North Star

The long-term engineering chain is:

ALGORITHM
→ MODEL
→ COMPILER
→ KERNEL
→ ACCELERATOR
→ MEMORY
→ INTERCONNECT
→ CLUSTER
→ ENERGY
→ COST

The goal is to understand and optimize the complete chain.

Target Professional Identity
Accelerated Computing & AI Infrastructure Efficiency Engineer

The programme is complete when this title is defensible through reproducible engineering evidence rather than course completion alone.

## Scientific programme and public evidence

- [Scientific scope and experiment method](00-programme/ACE_SCIENTIFIC_PROGRAMME.md)
- [Weekly evidence calendar through October 2027](00-programme/ACE_WEEKLY_EVIDENCE_CALENDAR.md)
- [Reusable release template](00-programme/templates/WEEKLY_EVIDENCE_RELEASE.md)

GitHub holds technical proof, the NSDM website holds the dossier, and The NeuroAlchemist provides authored interpretation. Weekly publication preserves null findings, unsupported configurations and claim boundaries; it does not expand the locked curriculum.

## Public publication boundary

This is the public scientific portfolio. Released experiment code, data, methods and learning plans remain inspectable. Commercial implementation, proposals, customer data, daily operations and unapproved editorial drafts belong in the private development repository. See [the publication boundary](PUBLICATION_BOUNDARY.md).

Before pushing a public release, run `python scripts/check_public_release.py`. Existing operational/draft pointers are frozen; update the private records instead. This is a current-tree publication check, not a full history/secret audit.

