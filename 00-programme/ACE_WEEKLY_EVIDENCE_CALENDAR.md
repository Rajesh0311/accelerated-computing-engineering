# ACE Weekly Evidence Calendar

**Created:** 8 October 2026
**Planning horizon:** now through 31 October 2027
**Authority:** [Scientific Programme](ACE_SCIENTIFIC_PROGRAMME.md), locked baseline and Atlas
**Status:** PLANNED; no row asserts completion

Every row produces a dated website evidence entry, a NeuroAlchemist release candidate and a useful visual. Entries link to an immutable protocol/result commit or to a clearly attributed external source. A flagship candidate is replaced by a shorter field note if evidence or time does not justify an essay.

Dates are reporting windows. Technical work follows prerequisites and actual progress. If a planned experiment is blocked, publish its protocol, access limitation, negative finding or replication audit. Do not substitute a mock result for a hardware-required gate. No Topograph/Kubernetes/serving installation is brought into Foundation Sprint 0 by this calendar.

Week 0 is the current partial week. The first formal-core reporting week includes 1 December; work before that date remains foundation. The final reporting week ends at the existing 31 October target.

| Week | Reporting window | Technical focus | Repository artefact and website entry | NeuroAlchemist angle | Visual |
|---:|---|---|---|---|---|
| 0 | 2026-10-08–2026-10-11 | Existing evidence and scientific scope | Programme record + Gate 1 dossier | Dispatch: following execution | Existing architecture SVG |
| 1 | 2026-10-12–2026-10-18 | Git and reproducible Python | Pin a tiny engineering fixture, dependencies and reproduction command | Field note: Why the experiment starts before the benchmark | Reproduction map |
| 2 | 2026-10-19–2026-10-25 | C/C++ build and linking | Compile a reference operation; record compiler/flags and errors | Field note: A result has a toolchain | Build pipeline diagram |
| 3 | 2026-10-26–2026-11-01 | Linux and host processes | Record verified host path and process/file-system observations | Field note: The machine beneath the model | Host responsibility map |
| 4 | 2026-11-02–2026-11-08 | Linear algebra and conditioning | Worked reference problem; label as numerical exercise | Flagship candidate: When a precise answer is unstable | Conditioning diagram |
| 5 | 2026-11-09–2026-11-15 | Debugging and build discipline | GDB/build-log reproduction or supported local equivalent | Field note: Bugs are part of the evidence | Fault and recovery diagram |
| 6 | 2026-11-16–2026-11-22 | Statistics and repeatability | Sampling/exclusion plan; analyse an existing dataset if available | Field note: The fastest run is a poor witness | Distribution plot or sampling diagram |
| 7 | 2026-11-23–2026-11-29 | Foundation readiness | Competence checklist; unresolved prerequisites and next decisions | Field note: The right to begin | Readiness matrix |
| 8 | 2026-11-30–2026-12-06 | Core-entry week; 1 December gate | Admit core only after prerequisite checks; retain Gate 1 credit | Flagship candidate: A start date cannot certify competence | Gate map |
| 9 | 2026-12-07–2026-12-13 | Architecture and existing locality evidence | Curate full Gate 1 CSV and its registered analysis | Field note: What memory makes computation pay | Measured locality plot |
| 10 | 2026-12-14–2026-12-20 | Latency, throughput and dependency | Explain B/C order contrast and C/D dependency contrast | Field note: One nanosecond is not another | Measured ratio plot with dispersion |
| 11 | 2026-12-21–2026-12-27 | Numerical error and decision thresholds | Preregister SCI-02; reference/threshold-edge fixtures | Field note: A tiny error can change an action | Threshold fixture diagram |
| 12 | 2026-12-28–2027-01-03 | Parallel decomposition | Serial reference and task contract for SCI-03 | Flagship candidate: Work divided is not work accelerated | Task/dependency diagram |
| 13 | 2027-01-04–2027-01-10 | Parallel scaling and memory | Run admitted worker/problem-size matrix or progress note | Field note: Where more workers stop helping | Measured scaling curve |
| 14 | 2027-01-11–2027-01-17 | HPC and efficient programming | Profile CPU bottleneck; compare one justified change | Field note: The optimization the model never sees | Profile/attribution graphic |
| 15 | 2027-01-18–2027-01-24 | MPI/OpenMP communication | Admit SCI-03 collective/overlap controls on supported host | Field note: The cost of agreeing | Communication/scaling plot |
| 16 | 2027-01-25–2027-01-31 | CUDA entry and numerical reference | First correct kernel; CPU reference and toolchain manifest | Flagship candidate: Moving work changes the proof | Host/device execution diagram |
| 17 | 2027-02-01–2027-02-07 | CUDA memory model | Correct reduction/matmul baseline; transfer costs separated | Field note: The data must arrive | Transfer/kernel timeline |
| 18 | 2027-02-08–2027-02-14 | CUDA synchronization and correctness | Admitted negative/control fixtures; race/error record | Field note: Synchronization is a correctness decision | Dependency/synchronization diagram |
| 19 | 2027-02-15–2027-02-21 | Nsight Systems and instrument overhead | CPU/GPU timeline; compare traced/minimal conditions | Field note: A busy chart can hide an idle system | Measured timeline |
| 20 | 2027-02-22–2027-02-28 | Nsight Compute and bottleneck diagnosis | Counters plus competing mechanism explanations | Flagship candidate: Occupancy is a clue, not a verdict | Counter/bottleneck comparison |
| 21 | 2027-03-01–2027-03-07 | Memory optimization | SCI-04 one-factor tiling/coalescing comparison | Field note: The price of feeding arithmetic | Measured before/after with uncertainty |
| 22 | 2027-03-08–2027-03-14 | Async streams and overlap | SCI-05 sequential/stream control after prerequisites | Field note: Waiting is an architectural choice | Measured overlap timeline |
| 23 | 2027-03-15–2027-03-21 | CUDA graphs and admission | Warm/startup costs, equivalence and fixed-shape scope | Field note: Speed must earn admission | Error/performance frontier |
| 24 | 2027-03-22–2027-03-28 | PyTorch custom extension | Correct operator, reference tests and actual dispatch path | Flagship candidate: The interface is part of the computation | Operator execution map |
| 25 | 2027-03-29–2027-04-04 | Containers; CS267 entry | Reproducible GPU container if supported; manifest otherwise | Field note: Portability begins with an honest environment | Environment/version matrix |
| 26 | 2027-04-05–2027-04-11 | Advanced HPC scaling | SCI-03 compute/communication budget and limits | Field note: Parallelism meets the network | Strong/weak scaling plot |
| 27 | 2027-04-12–2027-04-18 | Host and platform failure | CP1 induced fault/recovery; supported environment only | Field note: The host can make a GPU look slow | Incident timeline |
| 28 | 2027-04-19–2027-04-25 | AMD portability entry | HIP port specification/compilation; hardware access ledger | Flagship candidate: Portable source, conditional performance | Backend capability matrix |
| 29 | 2027-04-26–2027-05-02 | Scheduling and conservation precursor | SCI-07/08 protocol or platform-neutral fixture after admission | Field note: The work that disappeared from the denominator | Reconciled lifecycle diagram |
| 30 | 2027-05-03–2027-05-09 | HIP/ROCm profiling or access limitation | Actual AMD comparison only with access; unresolved gate otherwise | Field note: Absence of hardware is a result about scope | Measured plot or limitation map |
| 31 | 2027-05-10–2027-05-16 | JAX/TPU semantics and compilation | Admit JAX reference; device/runtime manifest | Field note: Another accelerator, another execution path | Compile/execution diagram |
| 32 | 2027-05-17–2027-05-23 | TPU sharding or supported-access record | Actual sharding result if feasible; unresolved G8 if unavailable | Flagship candidate: Scaling needs a place to happen | Sharding/placement map |
| 33 | 2027-05-24–2027-05-30 | LLVM and governed transformations | IR artefact and one semantics-preserving transform | Field note: The compiler participates in the decision | IR/lowering diagram |
| 34 | 2027-05-31–2027-06-06 | Automation, security and authority | SCI-09 allowed/denied/delegated fixtures and audit | Field note: An observer is not an owner | Authorization/state-diff map |
| 35 | 2027-06-07–2027-06-13 | Triton versus native reference | SCI-06/12 candidate; correctness before accepted speedup | Field note: A generated kernel still owes a proof | Runtime/error comparison |
| 36 | 2027-06-14–2027-06-20 | torch.compile and graph breaks | Warm/cold/runtime provenance and numerical equivalence | Flagship candidate: The same model can take a different path | Graph-break and timing visual |
| 37 | 2027-06-21–2027-06-27 | Kubernetes scheduling and topology admission | RB-002 Gate 0; simulation only after all prerequisites | Field note: Where a workload runs belongs in its passport | Exact virtual topology map |
| 38 | 2027-06-28–2027-07-04 | Topology controls and resource transitions | RB-002 A–F if admitted; SCI-08 requeue/release fixtures | Field note: False capacity and false scarcity | Allocation/placement timeline |
| 39 | 2027-07-05–2027-07-11 | NCCL and physical scaling scope | Actual collectives when available; model separated from measurement | Field note: The fabric joins the computation | Measured communication or labelled model |
| 40 | 2027-07-12–2027-07-18 | SRE and critical control traffic | SCI-11 failure/recovery and starvation fixture where supported | Flagship candidate: Small control messages can carry large consequences | Incident/control-path timeline |
| 41 | 2027-07-19–2027-07-25 | Transformer workload internals | CS336 small workload profile and reference contract | Field note: The model meets its physical limits | Memory/compute attribution plot |
| 42 | 2027-07-26–2027-08-01 | Serving request conservation | SCI-07 admitted load/priority matrix and terminal ledger | Field note: Tokens per second cannot count missing work | Request outcome counts with reconciliation |
| 43 | 2027-08-02–2027-08-08 | Batching and queueing | Registered service target; request-level distributions | Field note: Throughput has a waiting room | Queue/service/end-to-end distributions |
| 44 | 2027-08-09–2027-08-15 | Quantization and governed semantics | SCI-06 numerical and discrete threshold validation | Flagship candidate: A cheaper answer may be a different decision | Precision/error/performance frontier |
| 45 | 2027-08-16–2027-08-22 | KV cache and memory pressure | Admitted cache/batch perturbation; provenance checks | Field note: Memory is a policy choice | Measured memory/latency curve |
| 46 | 2027-08-23–2027-08-29 | FSDL and reproducible service | Deployment/rollback/manifest and scoped recovery evidence | Field note: A deployment should be inspectable | Service/trace architecture |
| 47 | 2027-08-30–2027-09-05 | Capacity and cost denominators | SCI-13 measured/estimated inputs and failed-work costs | Field note: What exactly did the infrastructure buy? | Cost/service sensitivity plot |
| 48 | 2027-09-06–2027-09-12 | Evaluation and autonomous actions | Bounded long-horizon/retry/delegation fixture | Flagship candidate: Capability expands; authority stays explicit | Bounded action-state diagram |
| 49 | 2027-09-13–2027-09-19 | Capstone workload and preregistration | Freeze comparison contract, access and metrics | Field note: One workload, several valid questions | Comparison design map |
| 50 | 2027-09-20–2027-09-26 | Capstone reference and backend runs | SCI-12 accessible-backend controlled comparisons | Field note: Which machine earns this workload? | Measured backend frontier |
| 51 | 2027-09-27–2027-10-03 | Capstone reliability and semantics | C1–C4 failure fixtures and service adjudication | Field note: The fastest admissible path | Failure/admissibility matrix |
| 52 | 2027-10-04–2027-10-10 | Capstone economics and recommendation | SCI-13 sensitivity and policy-aware choice | Flagship candidate: Efficiency depends on what must remain true | Measured/estimated cost frontier |
| 53 | 2027-10-11–2027-10-17 | Independent reproduction or review | Fresh-clone rerun; external review if secured, otherwise limitation | Field note: Can someone else obtain the result? | Reproduction/check matrix |
| 54 | 2027-10-18–2027-10-24 | Counterexamples and evidence gaps | Attempt to falsify mechanism and infrastructure recommendation | Field note: The result worth publishing can be the one that breaks | Alternative-explanation map |
| 55 | 2027-10-25–2027-10-31 | Final 16-gate review and closure | Report actual pass/incomplete states; no invented completion | Field note: What the programme earned, and what it still owes | Final evidence map |

## Recurring acceptance checklist

- [ ] One question and a claim/evidence label.
- [ ] Current phase and prerequisites respected.
- [ ] Protocol/data/configuration or primary-source link.
- [ ] Result, current state, failure/null/unsupported status and limitations.
- [ ] Visual answers the question; measured data and conceptual imagery distinguished.
- [ ] Numerical/discrete semantics, lifecycle, resources and authority checked where required.
- [ ] Uncertainty and measured/estimated cost fields identified.
- [ ] Website style, paper downloads and old results preserved.
- [ ] Substack source notes/disclosure and final editorial line-edit.
- [ ] Human sign-off and actual published URLs recorded.
- [ ] Next falsifiable test; no automatic competency upgrade.

## Release ledger

Use [the release template](templates/WEEKLY_EVIDENCE_RELEASE.md). Record planned, drafted, reviewed, published and corrected as separate states. The publication date and experiment date need not match. Historical records are never rewritten to make an old experiment look new.

## Workload and effort rule

The weekly item packages the current technical work. It does not commission 56 unrelated experiments. Reuse SCI-01–SCI-14 families, shared manifests, fixtures, plotting code and IDs. Course hours and target windows remain those of the Atlas; if required evidence is incomplete at the target date, report it and revise the schedule explicitly.
