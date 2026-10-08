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

---

# ACE-RB-002 — Simulated Topology Publication, Placement and Trace Reconstruction

**Status:** SPECIFIED — DEFERRED UNTIL FORMAL CORE ENTRY AND GATE 0
**Priority:** HIGH research value; no current-sequence interruption
**Source event:** NVIDIA Topograph v1.0.0 and the 22 September 2026 engineering publication
**Decision date:** 28 September 2026
**Target evidence:** E2 initially; E3 only after repeatable independent rerun
**Current sequence impact:** NONE

## Research question

Can ACE create a deterministic, auditable evidence chain from a declared simulated cluster topology through scheduler-visible metadata and workload placement to an EDEP execution record without physical multi-node GPUs?

## Claim boundary

This is a scheduler, provenance and reproducibility precursor.

It may provide evidence about:

- topology-model normalization;
- scheduler-consumable label publication;
- hard placement-constraint compliance;
- preferred-placement satisfaction rates;
- topology refresh and stale-label removal;
- EDEP trace-to-placement reconstruction.

It cannot establish:

- GPU communication performance;
- physical network latency or bandwidth;
- distributed useful-throughput improvement;
- energy efficiency;
- infrastructure cost reduction;
- production GPU-cluster competence.

## Gate 0 — Platform feasibility

**Status:** NOT STARTED

Record and verify:

1. Supported Windows/WSL/Linux execution path
2. Go
3. `make`
4. Docker container runtime
5. Kind
6. `kubectl`
7. Helm 3.10+ or 4.x
8. `yq`
9. KWOK and `kwok-nodes`
10. Topograph test-provider simulation path
11. Exact operating-system, kernel and tool versions
12. Available CPU, memory and storage headroom

Unsupported prerequisites are recorded as feasibility evidence, not experimental failure.

No installation begins before the formal ACE core start on 1 December 2026 and explicit experiment prioritization.

## Version and provenance controls

Use a tagged Topograph release rather than an unbounded `main` branch.

Record:

- release version and Git commit;
- container-image digest;
- Helm-chart version and digest where available;
- topology-model checksum;
- provider and engine configuration;
- Kubernetes, Kind, KWOK, Helm and scheduler versions;
- experiment repository commit.

## Fixed experimental conditions

### A — No topology metadata

Negative control using the selected scheduler without Topograph-derived topology information.

### B — Labels only

Verify Topograph topology normalization, Kubernetes label publication and trace capture without claiming improved placement.

### C — Preferred affinity

Measure the proportion of placements satisfying the declared preference. Preferred affinity is a scoring input, not a deterministic or globally optimal gang-placement guarantee.

### D — Required constraint

Test a hard placement rule and require zero placements that violate the declared constraint.

### E — Changed topology model

Regenerate topology and verify that changed labels are published and stale Topograph-managed labels are removed.

### F — Corrupted or incomplete metadata

Inject missing, stale or inconsistent topology metadata and verify that the validation harness detects the condition and preserves an auditable failure record.

## Workload

Use four lightweight CPU-only mock workers representing concurrent EDEP execution. GPU computation is deliberately excluded from the simulation precursor.

Every execution record must preserve:

**EDEP identifier → workload/pod → node → topology domain → topology-model version**

The discrete EDEP result, including UNKNOWN and abstention states where present, must remain identical across conditions.

## Preregistered success criteria

- 100% expected-label publication for the fixed topology fixture
- Zero hard-constraint placement violations
- 100% EDEP trace-to-placement reconstruction
- Zero EDEP semantic divergence
- Correct detection of the negative/corrupted metadata case
- Correct removal or replacement of stale managed labels after regeneration

Preferred-affinity satisfaction is reported as a rate and distribution. It is not required to produce identical node placement on every run.

No physical-performance threshold is permitted in the simulation experiment.

## Null condition

Topograph-derived metadata produces no material improvement in topology provenance, refresh correctness, constraint validation or reproducibility compared with a manually labelled control.

A null result is retained as valid evidence.

## Security and authority boundary

- Use the default cluster-internal service path for the local experiment.
- Do not expose the Topograph API externally without a separate authentication and network-control design.
- Record the actor and configuration responsible for topology regeneration.
- Preserve the generation request identifier, status, timestamp and failure result.
- Treat reported topology as observed metadata, not automatically as intended infrastructure state.

## Evidence record

The experiment must produce a machine-readable Topology-Aware Execution Evidence Record containing:

- topology fixture and checksum;
- toolchain manifest;
- Topograph provider/engine configuration;
- scheduler configuration;
- workload and EDEP identifiers;
- placement outcome;
- topology-refresh outcome;
- trace mapping;
- semantic-equivalence result;
- negative/control case;
- limitations and claim boundary;
- reproduction command.

## Future physical comparator

After the simulation methodology reaches E3, a separate experiment may test:

**GPU → NIC → switch/fabric → placement → communication latency → useful throughput → tail latency → energy/cost → EDEP outcome**

This requires controlled multi-node infrastructure through Axiz, MTN, Telkom, Solcon, a suitable cloud environment or another authorized residency host.

## Decision

**KEEP IN BACKLOG. SPECIFY NOW. DO NOT INSTALL OR EXECUTE BEFORE FORMAL CORE ENTRY, GATE 0 AND EXPLICIT PRIORITIZATION.**

---

# Scientific Coverage Additions — 8 October 2026

The [Scientific Programme](ACE_SCIENTIFIC_PROGRAMME.md) defines protocol families and scientific/publication standards. The families do not automatically enter the active sequence. Existing RB-001/RB-002 specifications and their deferrals remain unchanged.

## ACE-RB-003 — Request and Lifecycle Conservation

**Status:** SPECIFIED / QUEUED; execution requires foundation competence and explicit prioritization
**Protocol mapping:** SCI-07
**Target:** E3 controlled comparison; serving-engine reproduction later

Question: can the harness reconcile each logical request and distinguish legitimate attempts from lost or duplicate work under concurrency, priority and admission bounds?

Reference: sequential, ID-based ledger with explicit rejection/cancellation/failure and drain rules. Perturbations: silent drop, duplicate completion, foreign trace attribution, timeout, cancellation and retry. Success requires zero unexplained request loss after the registered drain/cutoff policy, detection of injected defects and a measured false-positive rate. In-flight work is explicit before drain. A count match alone does not establish unique-ID reconciliation.

Platform-neutral first; vLLM is a later Gate-0-qualified comparator. Upstream scheduling defects remain external observations until reproduced. No current installation is authorized.

## ACE-RB-004 — Resource and Physical-Release Conservation

**Status:** SPECIFIED / QUEUED
**Protocol mapping:** SCI-08
**Target:** E3; real scheduler comparison later

Question: does policy-normalized effective demand survive retry/requeue, and does accounting release agree with actual cessation?

Reference: effective demand derived by the specified policy, with per-attempt allocations. Faults: dropped defaults/overhead or preprocessed resources, early reservation release, orphan allocation, duplicate release and delayed physical stop. Distinguish demand, reservation and allocation vectors; retries can legitimately allocate again. Require zero unexplained demand divergence and no orphan allocations after the declared reconciliation deadline; audit idempotent releases and detect early release.

Kueue defect classes motivate fixtures, not automatic local reproduction claims. Use the same lifecycle/trace infrastructure as RB-003. No Kubernetes installation is authorized by this specification.

## ACE-RB-005 — Authority and Ownership Conservation

**Status:** SPECIFIED / QUEUED
**Protocol mapping:** SCI-09
**Target:** E3; controller comparator later

Question: can every state-changing operation prove authorization for this actor, target, operation and time?

Reference: valid owner and explicitly delegated operations. Faults: foreign mutation/deletion, stale owner, expiry, revocation, invalid transfer and duplicated identity. Require zero unauthorized mutation/deletion, unchanged governed state after denial, and complete actor/operation/policy audit. Include valid delegation controls; actor/controller name equality is not a sufficient authorization model.

No production security or complete multi-tenant isolation claim follows from a local fixture.

## ACE-RB-006 — Optimization Admissibility Matrix

**Status:** SPECIFIED / QUEUED
**Protocol mapping:** SCI-02/04/06/12
**Target:** E3

Question: which candidate transformations preserve the workload contract and improve its registered objective?

Reference: deterministic numerical/governed workload, one transformation at a time. Candidates include precision, compilation, batching, CUDA graphs and cache representation only where prerequisites and Gate 0 pass. Require exact registered discrete-state agreement, declared numerical tolerances, C1–C4 where applicable, actual backend provenance, holdout/threshold-edge fixtures and uncertainty-aware comparison.

An inherently stochastic output needs workload-specific equivalence criteria rather than assumed universal token identity. A required UNKNOWN result blocks acceptance. No improvement is a valid null; unsupported configurations are retained as scope evidence.

Reuse the semantic-equivalence infrastructure instead of creating a duplicate course or serving engine. Hardware-specific release defects are external observed records until independently reproduced.

## Prioritization rule

Foundation first; one active substantial experiment; no execution because a publishing slot needs a result. Catalogue trends as READ/REUSE/TEST/WATCH/REJECT and map them to existing families. The dated calendar is a reporting plan, not permission to bypass Gate 0, prerequisite competence or existing RB-001/RB-002 deferrals.
