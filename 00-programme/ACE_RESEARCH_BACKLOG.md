# ACE Research Backlog

**Status:** ACTIVE
**Created:** 11 September 2026
**Purpose:** Maintain intelligence-derived, falsifiable research opportunities without creating syllabus sprawl.

---

# Operating Rules

1. The locked baseline and ACE Atlas remain authoritative.
2. A backlog item is not automatically part of the active learning sequence.
3. No experiment begins before its prerequisite competence exists.
4. Every experiment requires a stable reference, preregistered metrics and correctness validation.
5. Null results, unsupported configurations and failed experiments are preserved.
6. No portfolio claim becomes defensible below Evidence Level E3.
7. Vendor benchmark results never become ACE evidence without independent reproduction.

Evidence levels:

- **E0:** reading, course or source review
- **E1:** guided reproduction
- **E2:** independent implementation with tests
- **E3:** controlled comparison
- **E4:** external reproduction or review
- **E5:** peer-reviewed, adopted or upstream contribution

---

# ACE-RB-001 — Governed Shared-Accelerator Resource Isolation

**Status:** QUEUED
**Priority:** HIGH, but deferred until prerequisites are reached
**Source event:** CUDA Toolkit 13.4 and MPS V3
**Decision date:** 11 September 2026
**Target evidence:** E3
**Current sequence impact:** NONE

## Research question

Can controlled shared-GPU execution increase useful workload throughput while preserving numerical correctness, latency bounds, workload attribution and NSDM/EDEP semantic integrity?

## Why it matters

Peak throughput alone is not the ACE optimization objective.

The stronger objective is:

**maximize valid, traceable and service-level-compliant executions per unit cost**

subject to:

- correctness
- latency
- auditability
- workload isolation
- provenance integrity

## Current constraints

- Current primary device: RTX 5070 Laptop GPU, 8 GB VRAM
- Current recorded NVIDIA driver: 610.47
- Current primary operating environment: Windows
- CUDA 13.4 new features require a compatible R615-or-newer driver
- NVIDIA documents MPS for Linux and QNX, not native Windows
- WSL compatibility must not be assumed
- Exact RTX 5070 MPS V3 functionality is not yet established

## Stage A — Windows concurrency precursor

**Status:** DEFERRED UNTIL CUDA CONCURRENCY PREREQUISITES

Build one reusable benchmark harness comparing:

1. Sequential execution
2. Two unmanaged CUDA processes
3. CUDA-stream concurrency

Required evidence:

- environment manifest
- deterministic reference output
- benchmark configuration
- raw results
- p50/p95/p99 latency
- useful throughput
- GPU and memory utilization
- interference ratio
- numerical-equivalence result
- semantic-equivalence result
- trace-attribution result
- limitations

## Stage B — Platform-feasibility gate

**Status:** NOT STARTED

Pass conditions:

- native Linux environment available
- compatible R615-or-newer driver
- CUDA 13.4 installed in an isolated, reproducible environment
- MPS V3 daemon available
- target GPU recognized
- required resource-control capabilities enumerated
- profiling path operational

Failure does not invalidate the research question. It establishes that residency or external infrastructure is required.

## Stage C — MPS V3 controlled comparison

**Status:** BLOCKED BY STAGE B

Comparators:

1. Sequential reference
2. Unmanaged concurrent processes
3. MPS V3 controlled sharing

Initial experimental hypothesis:

A bounded MPS allocation will improve aggregate useful throughput by at least 15% over unmanaged concurrency without:

- correctness failure
- provenance misattribution
- semantic output change
- p95 latency degradation greater than 20%

These thresholds are preregistration candidates, not expected performance claims.

## NSDM/EDEP invariants

- Decision state must match the reference.
- UNKNOWN and abstention states must be preserved.
- Every execution must remain associated with the correct trace identifier.
- No evidence or provenance record may cross workload boundaries.
- Performance traces must remain attributable.
- Audit overhead must be measured.
- A faster incorrect or unattributable execution is a failed result.

## Commercialization gate

No commercial capability is currently demonstrated.

A future **AI GPU Utilization and Governed Workload Assessment** becomes defensible only after:

1. E3 controlled evidence exists.
2. The test is reproduced on appropriate infrastructure.
3. Isolation is described accurately as resource/workload isolation—not automatically as a security boundary.
4. Cost findings use measured infrastructure inputs.
5. Limitations and failure modes are disclosed.

## Decision

**KEEP IN BACKLOG. DO NOT INTERRUPT FOUNDATION SPRINT 0 OR CURRENT COMPUTER-ARCHITECTURE WORK.**
