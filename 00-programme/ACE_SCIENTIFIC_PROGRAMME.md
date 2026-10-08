# ACE Scientific Programme and Public Evidence Roadmap

**Decision date:** 8 October 2026
**Status:** LOCKED EXECUTION AND PUBLICATION METHOD; EXPERIMENTS REQUIRE INDIVIDUAL ADMISSION
**Programme owner:** Rajesh Singh / MetaForgeX AI
**Professional identity:** Accelerated Compute Platform & AI Infrastructure Efficiency Engineer
**Foundation:** 7 October–30 November 2026
**Formal core:** 1 December 2026
**Target evidence closure:** 31 October 2027
**Canonical curriculum:** [ACE Locked Baseline](ACE_LOCKED_BASELINE.md), [ACE Atlas](ACE_ATLAS.md)
**Calendar:** [Weekly Evidence Calendar](ACE_WEEKLY_EVIDENCE_CALENDAR.md)

## 1. The scientific purpose

Investigate how intelligent workloads can deliver useful outcomes while preserving the meaning, ownership, lifecycle and accounting of the work they execute. Explain each result through numerical methods, architecture, compilation, memory movement, scheduling, platform behaviour and measurement.

The overarching question is:

**Under what conditions does an implementation deliver more correct, authorised, traceable, service-compliant work for a defensible infrastructure cost?**

This is an engineering research question, not a claim that MetaForgeX already operates a complete governed infrastructure platform.

The research chain is:

**Human purpose → decision contract → algorithm/model → compiler/kernel → accelerator/host → memory/network → scheduler/platform → telemetry → correctness/service objective → capacity/cost → outcome.**

NSDM developed independently as a decision-systems programme. It retains evidence semantics, justification and action-state definitions. ACE investigates computational execution. Behavioural science, decision science and neuromarketing contribute use-case questions and measurement discipline. Their relationship is explicit collaboration across layers, not a revised origin story.

AGI and superintelligence are bounded future research scenarios. Neither their arrival nor solved alignment is asserted. The present programme tests finite workloads and observable infrastructure behaviour.

## 2. Curriculum and scheduling control

The 12 core phases, CP1–CP8 platform overlay, existing course choices and 16 evidence gates remain locked. This document deepens experiment scope and makes scientific communication part of the execution loop; it creates no seventeenth gate or additional compulsory course.

Foundation work takes priority until 30 November. Existing Gate 1 evidence remains credited; the Computer Architecture sprint remains ACTIVE until its remaining learning and diagnostic requirements pass.

Use approximately 15 focused core hours per week as the existing planning basis. Reuse analysis, graphs and interpretation already required by the labs for publication. Budget approximately 60–90 minutes to package those artefacts; longer essays may require separately recorded optional time. If packaging displaces required learning, use a short field note rather than adding untracked effort or accelerating the curriculum.

Only one substantial experiment is active at a time. A controlled experiment may take two to four weeks. An unsupported platform, failed hypothesis, delayed run or correction can produce an honest weekly record. A calendar date cannot force a PASS.

Course/resource links are maintained in the Atlas. Version support, prices, licences, access and installation prerequisites must be freshly verified before use.

## 3. Focus matrix: what the programme must be able to explain

| Lane | Required scope | Engineering evidence | Curriculum / gates | Explicit claim boundary |
|---|---|---|---|---|
| Scientific foundations | Python, Git, Linux, C/C++, build/link/debug, linear algebra, calculus, probability, sampling, conditioning | Reproducible code, build log, numerical reference, experimental prediction | Foundation; CS205A; all gates | Course attendance is not competence |
| Architecture and locality | Pipelines, branch prediction, out-of-order execution, SIMD, cache/TLB effects, dependency, CPU affinity | Working-set sweeps, locality/dependency contrast, mechanism and confound analysis | Phase 1; G1 | A timing inflection is not an exact cache boundary |
| Numerical validity | Precision, summation order, error propagation, conditioning, LU/QR/SVD, direct/iterative solvers, tolerances | Error/performance frontier, stable reference, decision-threshold fixtures | CS205A; G3/4/5/9/11/12 | Speed with unacceptable error is inadmissible |
| Parallel algorithms | Decomposition, task/data parallelism, synchronization, load balance, contention, arithmetic intensity, Amdahl-style limits | Strong/weak scaling, serial reference, problem-size controls | Phases 2–3/6; G2/3/6 | More workers do not prove efficiency |
| CUDA and GPU execution | Threads/blocks, SIMT, divergent branches, coalescing, tiling, registers, occupancy, atomics, reductions, launch/transfer overhead | Correct kernels, compiler manifest, timeline and kernel diagnosis | Phases 4–5; G4/5 | High occupancy is not a universal objective |
| Asynchronous execution and sharing | Streams/events, overlap, graph capture, interprocess interference, host/device synchronization | Sequential/concurrent controls, equivalence, traced synchronization | Phase 5; CP3/4/5; G5/14/15 | Resource sharing is not automatically a security boundary |
| Heterogeneous portability | CPU/CUDA/HIP/ROCm/JAX/TPU, supported operators, memory, compilation, developer effort | Comparable workload contract, supported backend comparison | Phases 7–8/12; G7/8/12 | No AMD/TPU measurement without actual access |
| Compiler-mediated execution | IR/lowering, fusion, generated kernels, graph breaks, shape specialization, warm-up, flags, correctness regressions | Eager/compiled/native controls, generated artefact, correctness/performance adjudication | Phase 9; G9 | Same model name is not proof of equivalent computation |
| Host and data pipeline | Processes, cgroups/namespaces, filesystems, NUMA concepts, storage, data loading, pinned memory, CPU bottlenecks | Host diagnostic, transfer/pipeline trace, induced fault and recovery | CP1/3; G13 | Toolchain support must match the exact environment |
| Networking and topology | TCP/IP, DNS/TLS/MTU, bandwidth/latency, PCIe/NIC locality, collectives, RDMA concepts, topology metadata | Network diagnosis, simulated placement controls, physical comparator where available | CP2/4; Phase 10; G6/10/14 | Virtual nodes cannot establish physical fabric performance |
| Scheduling and resource identity | Admission, queues, priority, fairness, retries, reservations, effective demand, allocation/release | State-machine ledger, fault injection, raw/effective/allocated reconciliation | CP4; G14/16 | Logical eviction is not physical release |
| Serving and model systems | Tokenization, attention/KV cache, batching, quantization, speculative paths, queueing, load, backpressure | Workload matrix, request IDs, reference semantics, service objectives | Phases 11–12; CP6; G11/15 | Max tokens/s alone does not establish useful capacity |
| Observability and reliability | Nsight, profiler overhead, Prometheus/Grafana/DCGM, OpenTelemetry trace context, SLI/SLO, incidents | Joined trace, distributions, induced incident, recovery/runbook | CP5/6; G5/13/15 | Counters and dashboards alone are not explanations |
| Authority, security and deployment | Actor/owner/delegation/revocation, RBAC, secrets, image provenance, IaC, reproducible configuration | Denied-state equivalence, policy tests, deployment manifest, ownership ledger | CP7; G13/14/15/16 | A local authority test is not complete security assurance |
| Capacity, energy and economics | Local/cloud inputs, queue capacity, service compliance, GPU-hours, billing, showback, reliability cost | Cost model with measured/estimated fields and sensitivity analysis | CP8; G16/12 | TDP is not measured energy; simulations are not realised savings |
| Human and consequential use cases | Construct/predictive/incremental validity, decision utility, consent, uncertainty, abstention, context shift | Defined application contract and bounded synthetic/consented fixtures | Applied lens across all phases | Behavioural signals do not reveal inner mental states |
| Future intelligence scenarios | Longer autonomy, broader tool use, changing models, delegated execution, distributed coordination | Finite failure fixtures and explicit action bounds | Selective agent material; capstone | No consciousness, AGI, SI or universal alignment proof |

## 4. Persistent workload family

Use small reusable workloads, not a new benchmark for every release.

1. **Numerical substrate:** reductions, matrix operations and one stable solver, with known reference/error properties.
2. **Governed decision fixture:** deterministic synthetic evidence scores and discrete states, including supported, unsupported, under-specified, contradiction, UNKNOWN and abstention where the actual NSDM contract defines them. Preserve unsupported versus under-specified; do not invent a replacement ontology.
3. **Lifecycle fixture:** requests with IDs, admission outcomes, attempts, priority, cancellation, failure, retry and terminal reconciliation.
4. **Resource fixture:** policy-derived effective compute/memory vectors, reservations, allocations and physical stop/release events.
5. **Authority fixture:** two isolated owners, allowed operations, delegation, expiry and revocation.
6. **Placement fixture:** four CPU mock workers, versioned virtual topology, hard/preferred policies and trace reconstruction.
7. **Serving fixture:** a small model and fixed input corpus fitting verified memory constraints; record model/tokenizer revision, prompts, generation settings and actual backend.

Start synthetic. Label synthetic results. Proprietary or person-level data enters only with an appropriate data agreement, consent/legal basis, licensing and de-identification controls. Private-office/financial/healthcare applications remain synthetic reference scenarios until suitable access and validation exist.

Shared workload and attempt IDs connect these fixtures. The platform-neutral harness tests contracts; an external engine such as vLLM or Kueue is a later comparator, not an inference from a mock implementation.

## 5. Experiment coverage registry

These are protocol families, not completed experiments. Each must receive its own preregistration before execution. Links to ACE-RB-001 and ACE-RB-002 preserve their existing specifications and deferrals.

| ID | Testable question / hypothesis | Baseline and perturbation | Required outcomes and falsifier | Entry / evidence target |
|---|---|---|---|---|
| SCI-01 | Do locality and dependent addressing change measured access cost as the footprint grows? | Existing Gate 1 A/B/C/D records; later GPU translation after prerequisites | Reproduce designated comparisons; report reversals/dispersion; do not relocate registered decision sizes | Existing Gate 1 PASS; GPU work later |
| SCI-02 | Can a precision or accumulation change cross a governed decision threshold? | Stable higher-precision/reference solver versus one precision/order change | Numerical error plus exact registered discrete states; any prohibited crossing rejects candidate | CS205A foundations; E3 target |
| SCI-03 | Where does added parallelism stop improving useful throughput? | Serial, worker-count and fixed/expanded problem-size conditions | Correctness, speedup/efficiency, uncertainty, synchronization and memory costs; flat/negative scaling retained | CS149/HPC; G2/3/6 |
| SCI-04 | Does a profiled kernel change improve the registered objective while preserving output? | Correct unoptimized kernel versus one tiling/coalescing/fusion change | Timeline/kernel mechanism, error, latency/throughput, resource use; no benefit or failed equivalence retained | CUDA + profiling; G4/5 |
| SCI-05 | Does asynchronous or shared execution improve useful throughput within a defined latency bound? | Sequential versus streams/unmanaged processes; MPS only under RB-001 | Traces, interference, service distribution, semantics and attribution; apply RB-001 thresholds only to its admitted protocol | CUDA concurrency/Gate 0; G5/14/15 |
| SCI-06 | Can an optimization produce a better timing metric but an inadmissible decision? | Reference versus compile, precision, batch, cache or graph change, one factor at a time | C1–C4, threshold-edge/held-out fixtures, actual backend and candidate decision; do not manufacture a failing optimization | Numerical/compiler competence; E3 |
| SCI-07 | Can the harness detect every deliberately injected missing, duplicate or misattributed request? | Sequential ledger versus concurrency/priority/queue bounds and fault injections | Zero unexplained terminal-ID loss after drain; detection coverage and false positives; throughput cannot conceal loss | Platform-neutral first; serving later |
| SCI-08 | Does effective resource demand survive retry/requeue, and does release follow actual cessation? | Policy-normalized reference versus dropped overhead, duplicate release, delayed stop | Zero unexplained vector divergence; no orphan allocation after registered reconciliation deadline; detect early release | Platform-neutral first; CP4 comparator |
| SCI-09 | Are foreign, stale, revoked or expired mutations rejected without state change? | Policy-authorized owner/delegate operation versus negative fixtures | Zero unauthorized mutation/deletion; complete audit; unchanged state after denial; valid delegated operations also tested | Platform-neutral first; CP7 |
| SCI-10 | Can placement provenance be reconstructed under topology refresh and corrupted metadata? | RB-002 A–F conditions, including manual-label control | Hard compliance, preferred-placement rates, stale-label removal, semantic identity and trace reconstruction | RB-002 stays deferred; G14 |
| SCI-11 | Can observability and isolation of critical control traffic explain and limit injected service failure? | Healthy service versus one failure/load/limiter perturbation | Detection/recovery, queue/lease evidence where applicable, trace completeness, measurement overhead and service impact | CP5/6, later controller environment |
| SCI-12 | Which accessible backend best satisfies this fixed workload contract? | CPU plus actually available CUDA/HIP/JAX/TPU/compiler paths | End-to-end and steady-state time, correctness, memory, portability effort, service/cost sensitivity; record unsupported | Phase 12; G7/8/9/12 |
| SCI-13 | Does policy-aware placement lower cost per valid service-compliant outcome under explicit inputs? | Same workload/SLO with measured placement options | Denominator reconciliation, billed/estimated cost distinction, sensitivity, no simulated physical savings claim | CP8 + topology/service evidence; G16 |
| SCI-14 | Does a behavioural proxy add decision utility beyond a cheap baseline? | Consented/licensed observations or clearly labelled synthetic fixture; simple baseline versus added proxy | Holdout/calibration, context/population shift, uncertainty and utility; no inference of mind-reading or purchase causality | Applied sidecar; must not displace core |

One experiment may satisfy multiple lanes, but it cannot pass a gate requiring hardware or operational evidence it did not collect. Do not build a new scheduler, inference engine or profiler to reproduce a failure class.

## 6. Correctness admission: C1–C4

**C1 — Work and lifecycle:** At a registered cutoff, every unique request is terminal or explicitly accounted as in-flight. The final adjudication follows the declared drain/timeout rule. Keep attempt IDs separate from logical request IDs. Rejection, cancellation and failure are visible outcomes; duplicate completions are errors rather than additional useful work.

**C2 — Meaning:** Define the semantic contract before optimization. Deterministic governed fixtures require exact agreement in required discrete states and pre-registered numerical tolerance. For inherently stochastic model outputs, define seed/replay controls and task-level equivalence or distributional criteria; universal token identity is not a blanket requirement. Continuous agreement does not excuse a prohibited decision-state change.

**C3 — Resources:** Effective demand is derived by the actual normalization policy, including defaults, limits and overhead where relevant; do not assume a universal additive formula. Workload demand, current allocation and capacity reservations are different vectors. Account per allocation/attempt; retry can legitimately obtain a new allocation. Every allocation has an auditable lifecycle and idempotent release. Measure control, accounting and physical-stop timestamps separately.

**C4 — Authority:** Evaluate actor, target, operation, policy, scope, time, ownership and delegation. Actor/controller name equality alone is insufficient. Test invalid and valid delegation, revocation and ownership transfer; authorization must be checked at the relevant transition.

A check may be PASS, FAIL, UNKNOWN or NOT APPLICABLE with justification. UNKNOWN for a required check blocks acceptance. A simulated pass does not establish real-controller correctness.

Performance can be measured during diagnosis. It becomes an accepted improvement only after the required correctness checks pass and the registered service/performance objective is met. An optimization that changes the task's semantics is a new task requiring a new contract.

## 7. Minimum experimental protocol

Every admitted experiment records:

1. Question, falsifiable hypotheses and competing explanations.
2. Reference workload contract, baseline, negative control and smallest relevant perturbation.
3. Frozen code/data/configuration identifiers and licence/provenance.
4. Gate 0: exact hardware, OS/kernel, driver/runtime/toolkit/compiler/framework, memory headroom, feature availability and unsupported paths.
5. Independent variables, response variables, workload size/shape, warm/cold conditions and expected confounds.
6. Sample/run budget, power or precision rationale where applicable, ordering/randomization and blocking across sessions.
7. Registered exclusions, interruption policy, timeout/drain rules and numerical/semantic acceptance criteria.
8. Request/attempt/owner IDs, trace joining, resource vectors and terminal reconciliation.
9. Build/JIT/startup costs, steady-state costs and their amortization reported separately.
10. Raw records, timings, correctness outcomes, measured/estimated economic inputs and checksums.
11. Distribution/dispersion and uncertainty; no p99 claim from nine aggregate runs. Tail claims require adequate request-level observations and an uncertainty assessment.
12. Adjudication, null/failure/unsupported cases, threats, scope, reproduction command and next decision.

Resampling must respect the unit of independence; accesses within one run are not independent experiment replicates. Multiple configurations and post-hoc exploration are identified separately from registered hypothesis tests. Do not cherry-pick the fastest run or revise thresholds after seeing results.

An exploratory pattern may justify a new preregistration, not a retrospective confirmation claim. Hardware counters support a mechanism argument but do not automatically identify a sole cause.

For instrumentation, compare minimally instrumented and traced conditions when overhead could matter. Ensure measurement-unit consistency and clock alignment before joining distributed events.

## 8. Evidence levels and completion rules

Use the existing backlog definitions unchanged:

| Level | Meaning | Public wording |
|---|---|---|
| E0 | Reading, course or source review | Reviewed / specified; no local validation |
| E1 | Guided reproduction | Reproduced with guidance under stated configuration |
| E2 | Independent implementation with tests | Implemented and tested; controlled comparison still needed |
| E3 | Controlled comparison | Measured under the registered workload and conditions |
| E4 | External reproduction or review | Independently reproduced/reviewed with accessible record |
| E5 | Peer-reviewed, adopted or upstream contribution | Name the exact peer-review/adoption/contribution; distinguish them |

Public content can be valuable at every level. Portfolio competence claims require the relevant E3 evidence or stronger under the baseline, plus the actual gate-specific requirements. E3 does not automatically mean independent external reproduction. RB-002 retains its stricter rerun condition.

An official release-note defect is external observed evidence. A vendor speedup is a vendor claim. A synthetic fault injection is a local contract test, not reproduction of an upstream production bug.

Maintain separate fields for experimental validity, hypothesis outcome, optimization admissibility and programme-gate result. A sound null experiment can be valid even when an optimization fails. Gates are passed only by their own exit criteria.

## 9. Source-to-experiment intelligence system

Track official publications, papers, tagged releases, resolved/known issues and reproducible artefacts across:

- Numerical/architecture/HPC: canonical university materials, primary papers and maintained scientific libraries.
- Accelerators: NVIDIA CUDA/Nsight, AMD HIP/ROCm, Google TPU/JAX and supported cloud accelerator documentation.
- Compilers/runtime: LLVM/MLIR, Triton, PyTorch and JAX/OpenXLA.
- Platform/scheduling: Linux, container runtimes, Kubernetes, Kueue, Topograph, GPU-runtime/operator documentation.
- Serving/reliability: vLLM and registered serving comparators, OpenTelemetry, Prometheus, DCGM and profiler documentation.
- Economics: actual billing/usage inputs, provider pricing and FinOps primary guidance.
- Human decision applications: original behavioural/neuroscience studies, datasets and methods, with population/construct limits.

This is a watchlist, not an instruction to install all tools. Pin sources when an experiment is admitted.

For a consequential signal record publication and event date, exact version/issue, claim class, mechanism, workload consequence, platform fit, evidence gaps, smallest falsifiable test, priority and action. Inspect correctness defects as seriously as performance features. Verify versions and platform prerequisites anew; do not re-use September intelligence as current support documentation.

Rank candidates by correctness consequence, learning relevance, falsifiability, local feasibility, reuse and effort. Accept at most one new active experiment per month unless it replaces rather than adds work. A trend only changes the locked sequence through an explicit documented decision.

## 10. A weekly public evidence release

Each week has one release ID: `ACE-WEEK-YYYY-MM-DD`, using the Monday date; the initial partial week uses 2026-10-05. The issue contains:

- A website evidence entry: question, status/level, one useful artefact, result or current state, scope, limitations, next test and immutable repository link.
- A NeuroAlchemist piece: usually a 400–700-word field note or experiment dispatch. Once per four-week cycle, use an 1,000–1,600-word flagship essay only when the material warrants it.
- A visual: graph when measurements exist; an exact diagram, source-comparison map or clearly labelled conceptual illustration otherwise.
- A trend adjudication: one material development affecting the current work, or an explicit statement that no relevant change cleared the gate.
- A reusable technical artefact: protocol, reference fixture, script, dataset subset, graph source, failure record, reproduction improvement or correction.

This is a weekly evidence cadence, not a promise of a new experimental result every seven days. If no valid new result exists, publish a limitation, preregistration, replication audit or correction. Do not manufacture data or a trendy narrative.

### Operating rhythm

| Day | Deliverable | Decision |
|---|---|---|
| Monday | Select one question from the current phase; inspect fresh sources | Reuse, test, watch or reject; name the claim boundary |
| Tuesday–Wednesday | Build/measure or advance the multi-week protocol | Record all outcomes and interruptions |
| Thursday | Analyse, regenerate visual, draft evidence entry and essay/note | Check equivalence, uncertainty, trace and citations |
| Friday | Release candidate and human editorial sign-off | Update website/commit; publish approved Substack copy |
| Weekend, optional | Reproduction check or reader-feedback triage | Feedback informs a next test; it does not validate a result |

Automation prepares the release candidate and identifies missing evidence; it must not invent measurements or sign off in the author's name. Substack publication remains human-directed. Website publication uses the established repository path and validated site changes.

## 11. Channel responsibilities and site preservation

- **ACE repository:** canonical protocol, code, manifest, raw results, analysis and scientific decisions.
- **NSDM website:** durable technical dossier and evidence index, with status labels and direct source links.
- **The NeuroAlchemist:** authored interpretation, experiment narratives, failures and human/commercial implications.
- **Social excerpts:** optional distribution; never the sole evidence record.

A claim should resolve from essay → website evidence → immutable experiment commit. An external trend instead resolves to its primary source. Use source notes, editorial disclosure and the final frozen-facts/structure line-edit for finished articles.

Retain NSDM's papers, downloads, null findings, URLs, logos, fonts, colours and navigation. Add evidence entries through existing components. Mark proposed, external, simulated and measured content distinctly.

Near-term site work: add a dated weekly-evidence index linked from the existing evidence page; use reusable issue cards rather than redesigning the homepage every week. No unrun experiment receives a result graph. An article listing requires a confirmed published URL; pending drafts are labelled pending.

## 12. Visual and graph standard

Every visual answers a question or makes a mechanism inspectable.

**Scientific graphs:** generate from committed data using a reproducible plotting script. Provide units, baseline, observation counts/unit of replication, condition labels, uncertainty/dispersion where warranted and a caption stating inference limits. Preserve raw data; do not smooth away reversals or crop axes to exaggerate a benefit. Supply SVG plus an accessible raster export when useful, alt text and a downloadable data link.

**Useful plot families:** locality curves; precision/error versus runtime; strong/weak scaling; timeline/transfer overlap; throughput under a latency constraint; queue wait/service/total latency; request funnel with reconciled IDs; allocated versus physically occupied capacity; authority-denial state diff; topology domain/placement map; cost sensitivity and measured/estimated separation.

**Conceptual diagrams:** use authored SVG or exact diagram tooling for mechanisms, states and topology. Generated imagery is editorial atmosphere only. Label it conceptual; it must not fabricate apparatus, chip behaviour, profiler evidence or a data chart.

**Visual identity:** existing warm off-white, ink, teal and amber, restrained typography, readable labels and one coherent visual idea per piece. Keep originals and code alongside exports. Do not encode outcome solely by colour. Test desktop/mobile legibility.

## 13. Monthly scientific review and drift control

Every fourth issue produces a short review:

- Which hypotheses gained, lost or received no evidence?
- Which artefacts are reproducible, and which gates remain incomplete?
- Which alternative explanation survived?
- Which external claim was reproduced, narrowed or rejected?
- Which tool became a dependency; which can be removed?
- What changed in supported platforms, risks or cost inputs?
- What did readership reveal about unclear communication rather than scientific truth?
- What gets continued, merged, deferred or killed next month?

After core entry, reserve one review per quarter for an independent rerun or external reviewer if available. Lack of access is recorded, not implied away.

Backlog capacity: one active major experiment, up to two small maintenance/fault fixtures, and a watchlist. Separate hard prerequisite work from elective research. Unsupported AMD/TPU/multi-node work moves to a documented access plan; the corresponding hardware gate does not pass by simulation.

## 14. Capstone and final proof

The capstone joins an unfamiliar workload contract to actually accessible backends, governed semantics, deployment, telemetry, service compliance and economics.

Required evidence includes baseline, manifests, numerical/discrete equivalence, request/attempt reconciliation, authority decisions, resource lifecycle, physical placement where measured, profiler traces, uncertainty, failure injections, service objective, cost sensitivity, reproduction instructions and the final architecture recommendation.

Gate 12 cross-accelerator comparisons and Gates 13–16 operational evidence retain their Atlas requirements. Record unavailable environments and unresolved gates; do not rename partial access as full heterogeneous competence.

The final review answers: **what implementation would we choose for this workload, what evidence supports the choice, what did it fail, and under which changed assumption would the choice reverse?**

## 15. Immediate release: 8–11 October 2026

Use already committed evidence and this protocol update. No new hardware benchmark is required.

- Website: publish the scientific-programme scope and weekly release promise with links to the canonical documents.
- Technical dossier: curate existing Gate 1 records, keeping its original dates and adjudication.
- Substack draft thesis: “Before we ask machines to think further, we must learn to follow what they do.”
- Visual: the architecture diagram already created; a measured locality graph is admitted only after loading the complete committed CSV and applying the registered analysis.
- Trend slot: source-adjudicated material relevant to the question, or no material change.
- Next experiment: foundation reproduction/build discipline, not an early vLLM/Kueue/Topograph installation.

Planning is not a completed experiment. The weekly programme is locked as a method; experimental admissions and public interpretations remain revisable by evidence.
