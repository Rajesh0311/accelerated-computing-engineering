# Accelerated Computing Engineer Roadmap

**Programme:** Accelerated Computing Engineer (ACE)
**Foundation Sprint 0 (replanned):** 7 October–30 November 2026  
**Formal ACE core start:** 1 December 2026  
**Target completion:** 31 October 2027
**Primary objective:** Develop demonstrable competence across accelerated computing, GPU performance engineering, HPC, heterogeneous accelerators, compiler systems, distributed compute, and AI infrastructure efficiency.

---

## Schedule Basis

The schedule was revised on 23 September 2026 due to unforeseen circumstances. The [locked baseline](ACE_LOCKED_BASELINE.md#schedule-lock) governs the dates. The formal core runs from 1 December 2026 through 31 October 2027, with integrated capstone work and evidence closure in September–October 2027. Course hours, order, prerequisites and evidence requirements remain unchanged. Target windows permit interleaving only after prerequisites pass; unfinished work moves later rather than being compressed.

Earlier architecture study and the recorded Gate 1 pass remain credited. ACTIVE identifies the unfinished technical focus, not an assertion that the formal core has begun. Remaining architecture work is scheduled for December 2026; Foundation Sprint 0 takes priority before core entry.

The phase windows below summarize the Atlas course windows. Phase 8 includes preparatory review in April with the TPU/JAX courses in May; Phase 10 spans the full June–July NCCL window; Phase 11 includes FSDL through September. Phase 12 covers August preparation and September–October integration and closure.

## Programme Principle

Course completion is not the primary measure of progress.

The programme is complete only when:

1. The core curriculum has been completed.
2. The required engineering artefacts exist.
3. All 16 competency evidence gates defined by the canonical ACE Atlas have been passed.
4. A cross-accelerator capstone demonstrates practical competence.

The operating loop is:

**LEARN → BUILD → PROFILE / MEASURE → EXPLAIN → IMPROVE → COMMIT**

---

# Phase 1 — Computer Architecture

**Target:** December 2026
**Expected effort:** ~40 hours

### Core course
- Princeton — Computer Architecture

### Focus
- Processor architecture
- Instruction pipelines
- Cache hierarchy
- Memory hierarchy
- Locality
- Branch prediction
- Superscalar execution
- SIMD
- Latency vs throughput
- Multicore fundamentals

### Evidence gate
Demonstrate measurable CPU/cache/memory effects through benchmarks and explain the results.

---

# Phase 2 — Parallel Computing

**Target:** December 2026–January 2027
**Expected effort:** ~45 hours

### Core course
- Stanford CS149 — Parallel Computing

### Focus
- Parallel decomposition
- SIMD and SIMT
- Threads
- Work distribution
- Synchronization
- Locality
- Communication
- Contention
- Scalability
- GPU architecture
- Parallel programming models

### Evidence gate
Implement and benchmark a parallel workload and explain scaling efficiency and overhead.

---

# Phase 3 — High-Performance Computing

**Target:** January 2027
**Expected effort:** ~40 hours

### Core material
- CU Boulder — High-Performance and Parallel Computing
- Efficient Programming
- Parallel Computing with MPI

### Focus
- HPC architecture
- OpenMP
- MPI
- Point-to-point communication
- Collective communication
- Nonblocking communication
- Domain decomposition
- Parallel I/O
- Communication/computation overlap
- Performance modelling

### Evidence gate
Implement both OpenMP and MPI workloads and demonstrate measurable parallel scaling.

---

# Phase 4 — CUDA Core

**Target:** January–February 2027
**Expected effort:** ~53 hours

### Core material
- NVIDIA CUDA introductory material
- Modern CUDA C++
- CUDA Programming Guide

### Focus
- CUDA execution model
- Host vs device
- Kernels
- Threads
- Blocks
- Grids
- Synchronization
- Device memory
- Shared memory
- Registers
- Memory hierarchy
- Occupancy
- Reductions
- Matrix multiplication

### Evidence gate
Write correct nontrivial CUDA kernels without depending entirely on framework abstractions.

---

# Phase 5 — GPU Performance Engineering

**Target:** February–March 2027
**Expected effort:** ~67 hours

### Core tools
- NVIDIA Nsight Systems
- NVIDIA Nsight Compute
- CUDA profiling tools

### Focus
- CPU/GPU timelines
- Kernel launch overhead
- GPU idle time
- Memory bandwidth
- Memory coalescing
- Shared memory
- Cache behaviour
- Register pressure
- Warp stalls
- Occupancy
- Compute-bound vs memory-bound workloads
- Streams
- Asynchronous execution
- CUDA Graphs
- PyTorch CUDA extensions

### Evidence gate
Take an inefficient GPU workload through:

**PROFILE → HYPOTHESIS → OPTIMIZATION → RE-PROFILE → QUANTIFIED IMPROVEMENT**

---

# Phase 6 — Advanced HPC

**Target:** March–April 2027
**Expected effort:** ~40 hours

### Core course
- UC Berkeley CS267 — Applications of Parallel Computers

### Focus
- Parallel algorithms
- Distributed memory
- Communication costs
- Scalability
- Sparse computation
- Graph algorithms
- FFT
- Scientific computing
- Accelerator-aware HPC

### Evidence gate
Explain and demonstrate the relationship between algorithm design, computation, communication and scalability.

---

# Phase 7 — AMD ROCm / HIP

**Target:** April 2027
**Expected effort:** ~50 hours

### Core material
- AMD AI Academy
- ROCm
- HIP
- AMD profiling tools

### Focus
- AMD accelerator architecture
- ROCm software stack
- HIP programming
- CUDA portability
- GPU profiling on AMD
- Vendor-neutral accelerator concepts

### Required project
Port at least:

1. Reduction kernel
2. Tiled matrix multiplication
3. One additional CUDA workload

from CUDA to HIP.

### Evidence gate
Run equivalent workloads on NVIDIA and AMD environments and explain meaningful performance differences.

---

# Phase 8 — TPU / JAX / Compiler-First Accelerators

**Target:** April–May 2027
**Expected effort:** ~40 hours

### Core material
- Google TPU architecture
- JAX
- XLA concepts
- Cloud TPU
- TPU scaling material

### Focus
- TPU architecture
- Matrix accelerators
- JAX transformations
- JIT compilation
- Vectorization
- Device meshes
- Sharding
- Data/model parallelism
- Compiler-driven accelerator execution

### Evidence gate
Execute a real workload on TPU, use JAX compilation/sharding, and explain how the execution model differs from CUDA.

---

# Phase 9 — Compiler Systems

**Target:** May–June 2027
**Expected effort:** ~70 hours

### Core material
- LLVM
- Triton
- PyTorch compiler stack

### Focus
- Lexing and parsing concepts
- AST
- Intermediate representations
- LLVM IR
- Optimization passes
- Code generation
- JIT compilation
- Triton kernels
- Kernel fusion
- torch.compile
- TorchDynamo
- Inductor
- Generated GPU kernels

### Evidence gate
Implement and benchmark a Triton kernel against a CUDA/PyTorch equivalent and explain compiler-generated optimization behaviour.

---

# Phase 10 — Distributed Accelerators

**Target:** June–July 2027
**Expected effort:** ~25 hours

### Core material
- NVIDIA NCCL
- Multi-GPU execution
- Distributed PyTorch

### Focus
- Collective communication
- AllReduce
- Multi-GPU topology
- PCIe
- NVLink
- Communication bottlenecks
- Computation/communication overlap
- Distributed accelerator scaling

### Evidence gate
Run or simulate a distributed GPU experiment and produce a scaling analysis.

---

# Phase 11 — AI Workload Internals

**Target:** July–September 2027
**Expected effort:** ~110 hours

### Core material
- Stanford CS336 — Language Modeling from Scratch
- Stanford CME 295 — selected modules
- Full Stack Deep Learning

### Focus
- Tokenization
- Transformer architecture
- Training
- Data pipelines
- Scaling
- Quantization
- Mixture of Experts
- Memory behaviour
- LLM inference
- Evaluation
- Production ML
- Deployment
- Observability
- AI systems infrastructure

### Evidence gate
Profile an actual transformer workload and connect model architecture to accelerator utilization, memory behaviour, throughput and cost.

---

# Phase 12 — Cross-Accelerator Capstone

**Target:** August–October 2027
**Expected effort:** 40+ hours

### Objective

Demonstrate genuine accelerated-computing competence across multiple computing models.

### Required comparison

Use one representative workload and compare where practical:

- CPU baseline
- NVIDIA CUDA
- AMD HIP / ROCm
- Triton
- PyTorch compiler-generated execution
- TPU / JAX

### Measure

- Runtime
- Throughput
- Latency
- Memory consumption
- Accelerator utilization
- Scaling behaviour
- Developer effort
- Portability
- Energy or power where measurable
- Estimated compute cost

### Final question

For this workload:

**Which accelerator/software architecture is most appropriate, why, and under what assumptions would that conclusion change?**

### Final evidence gate

Produce:

- reproducible code
- benchmark dataset
- profiler evidence
- written technical analysis
- architecture diagrams
- performance recommendations
- cost/performance interpretation

---

# Target Professional Identity

By 31 October 2027 the goal is to be able to defend the title:

## Accelerated Compute Platform & AI Infrastructure Efficiency Engineer

with demonstrated competence across:

1. Computer Architecture
2. Parallel Computing
3. High-Performance Computing
4. CUDA
5. GPU Performance Engineering
6. NVIDIA Accelerated Computing
7. AMD ROCm / HIP
8. TPU / JAX
9. Compiler Systems
10. Distributed Accelerators
11. ML Systems
12. Infrastructure Performance Economics

---

# Long-Term Direction

CUDA is a major specialization, not the final identity.

The long-term engineering stack is:

**ALGORITHM
→ MODEL
→ COMPILER
→ KERNEL
→ ACCELERATOR
→ MEMORY
→ INTERCONNECT
→ CLUSTER
→ ENERGY
→ COST
→ BUSINESS OUTCOME**

The objective is to understand and optimize the complete chain.

---

# CUDA 13.4 / MPS V3 Research Delta

**Decision date:** 11 September 2026
**Classification:** ADD TO RESEARCH BACKLOG
**Syllabus impact:** NO CHANGE
**Atlas impact:** NO CHANGE
**Commercial claim permitted:** NO

## Authority

The canonical programme definition is:

1. `ACE_LOCKED_BASELINE.md`
2. `ACE_ATLAS.md`
3. This roadmap as a derived execution view
4. `ACE_RESEARCH_BACKLOG.md` for intelligence-derived experiments

Where an older roadmap statement conflicts with the locked baseline or Atlas, the locked baseline and Atlas prevail.

## Decision

CUDA Toolkit 13.4 introduces a valuable future experimental surface through Multi-Process Service V3, including named servers, namespaces, resource controls, streaming-multiprocessor partitioning and Linux cgroup-integrated GPU-memory controls.

This does not justify a new course, a change to the current sequence or an immediate CUDA upgrade.

The work enters the existing CUDA, GPU-performance, platform-engineering, observability and compute-economics programme layers.

## Experiment sequence

### Stage A — Windows-compatible concurrency precursor

Build a reusable comparison harness for:

1. Sequential GPU execution
2. Unmanaged concurrent CUDA processes
3. CUDA-stream concurrency

Measure:

- useful throughput
- p50, p95 and p99 latency
- GPU utilization
- memory utilization
- interference
- numerical correctness
- semantic equivalence
- trace attribution
- cost per valid execution

### Stage B — MPS V3 feasibility gate

Before claiming home-lab compatibility, verify:

1. Native Linux availability
2. R615-or-newer compatible NVIDIA driver
3. CUDA 13.4 compatibility
4. `nvidia-cuda-mps-control` availability
5. RTX 5070 MPS V3 feature exposure
6. Streaming-multiprocessor partition support
7. cgroup v2 and GPU-memory-control support
8. profiler and trace compatibility

Failure at this gate is recorded as evidence and moves the experiment to suitable residency infrastructure.

### Stage C — Governed shared-accelerator benchmark

Compare:

**sequential → unmanaged concurrency → controlled MPS V3 sharing**

Evaluate whether controlled sharing improves useful throughput without violating:

- correctness
- numerical tolerance
- latency service-level objectives
- workload attribution
- provenance integrity
- NSDM/EDEP semantic equivalence

## Placement

- Stage A: GPU Performance Engineering / Streams and Concurrency
- Stage B: Containers and GPU Runtime
- Stage C: GPU Scheduling, Observability and Capacity Engineering
- External execution where necessary: Axiz, MTN, Telkom, Solcon or other suitable residency infrastructure

## Permanent evidence invariant

Every accelerated-computing result must record:

**hardware → operating system → driver → toolkit → compiler → libraries → workload → policy → trace → correctness → latency → throughput → failure → cost**

For NSDM/EDEP workloads, also record:

- Case or workload identifier
- Decision-trace identifier
- provenance association
- semantic-equivalence result
- abstention or UNKNOWN-state preservation
- tenant or workload attribution
- auditability outcome

Performance evidence is invalid when the toolchain, correctness result or trace identity is missing.

---

# NVIDIA Topograph Research Delta

**Decision date:** 28 September 2026
**Classification:** ADD TO RESEARCH BACKLOG / SPECIFY NOW / DEFER EXECUTION
**Syllabus impact:** NO CHANGE
**Atlas impact:** NO CHANGE
**Commercial claim permitted:** NO

## Decision

NVIDIA Topograph creates a useful future ACE experimental boundary by normalizing discovered or simulated cluster topology into scheduler-consumable representations.

The opportunity is not a local GPU-cluster benchmark. It is a simulation-first precursor that tests whether ACE can preserve an auditable chain from topology model through scheduler-visible metadata and placement to EDEP execution provenance.

Topograph supplies topology information. Kubernetes, KAI Scheduler, Kueue or Slurm performs placement. The experiment must not attribute scheduler behaviour or physical performance to Topograph alone.

## Experiment placement

The canonical backlog specification is:

**ACE-RB-002 — Simulated Topology Publication, Placement and Trace Reconstruction**

Repository target:

`experiments/topology/EXP-TOPO-001-topograph-edep-simulation/`

Execution is deferred until:

1. the formal ACE core has begun on 1 December 2026;
2. the prerequisite platform, container, Kubernetes and scheduling competence exists;
3. Gate 0 confirms the local Kind/KWOK/Topograph path;
4. the experiment is explicitly prioritized without displacing the locked learning sequence.

## Evidence boundary

The simulation may establish:

- topology normalization and label publication;
- placement-constraint compliance;
- refresh and stale-label behaviour;
- EDEP trace-to-placement reconstruction;
- reproducible failure handling.

It cannot establish physical GPU/network performance, energy efficiency, infrastructure cost reduction or production-cluster competence.

Initial evidence is capped at E2. E3 requires a documented controlled comparison and independent rerun from repository instructions.

## Future residency extension

Physical topology-performance and economics claims require an authorized multi-node environment and measurement of:

**GPU → NIC → switch/fabric → placement → communication latency → useful throughput → tail latency → energy/cost → EDEP outcome**

Potential execution environments include Axiz, MTN, Telkom, Solcon or a suitable cloud GPU platform.

## Permanent topology provenance extension

For distributed or concurrent workloads, extend the ACE evidence chain with:

**topology model/snapshot → provider → engine → scheduler policy → workload placement → trace attribution → correctness → SLO → cost**

No topology-related efficiency claim is admissible when the physical topology, placement result or trace association is missing.

---

# Scientific Programme and Weekly Public Evidence

**Decision date:** 8 October 2026
**Classification:** LOCK EXECUTION/PUBLICATION METHOD
**Course sequence / gate count / schedule impact:** NO CHANGE

The comprehensive focus and protocol authority is [ACE Scientific Programme](ACE_SCIENTIFIC_PROGRAMME.md). The dated output plan is [ACE Weekly Evidence Calendar](ACE_WEEKLY_EVIDENCE_CALENDAR.md), with [a reusable release template](templates/WEEKLY_EVIDENCE_RELEASE.md).

The scientific programme maps numerical, algorithmic, accelerator, compiler, host, network, scheduling, reliability, authority and economics questions to the existing 12 phases, CP1–CP8 and 16 evidence gates. It defines 14 reusable protocol families, C1–C4 admission checks, Gate 0, negative controls, uncertainty, source adjudication, reproduction and a bounded capstone.

Each reporting week produces:
1. a website technical-evidence entry;
2. a NeuroAlchemist field note, experiment dispatch or occasional flagship essay;
3. a purposeful graph, exact diagram or labelled conceptual illustration;
4. one source-adjudicated material trend or an explicit no-change finding;
5. a reusable technical artefact with a repository/source link.

Publication does not require a new experiment every week. Multi-week experiments, null results, failed hypotheses, unsupported configurations, corrections and preregistrations remain publishable with honest status. No image substitutes for measured data.

Canonical proof stays in GitHub; the NSDM site is the technical dossier; Substack supplies authored interpretation. Preserve all original papers, research statuses, null findings and the site's established visual identity. Human review precedes publication.

The ~15-hour core planning basis remains unchanged. Reuse required lab interpretation and visualisation; record optional editorial effort separately. If a publication displaces a prerequisite, shorten it rather than compressing the curriculum.

Foundation remains 7 October–30 November 2026; formal core begins 1 December; completion target remains 31 October 2027. Gate 1 remains PASSED while the Computer Architecture sprint remains ACTIVE. The weekly calendar does not authorize early Topograph, Kubernetes, serving or MPS installation.

**Operating loop:** QUESTION → PREREGISTER → BUILD → MEASURE → ADJUDICATE → REPRODUCE → EXPLAIN → VISUALISE → COMMIT → PUBLISH → CORRECT.
