# ACE Master Atlas

**Programme:** Accelerated Compute Platform & AI Infrastructure Efficiency Engineer  
**Target completion:** 31 July 2027  
**Study intensity:** ~15 focused hours/week core + interleaved platform practice  
**Programme status:** ACTIVE  
**Current phase:** Phase 1 — Computer Architecture  
**Current course:** Princeton Computer Architecture  
**Evidence gates:** 16  

---

# North Star

**ALGORITHM → NUMERICAL METHOD → MODEL → COMPILER → KERNEL → ACCELERATOR → HOST → MEMORY → NETWORK → SCHEDULER → PLATFORM → TELEMETRY → CAPACITY → COST → BUSINESS OUTCOME**

The objective is not course completion.

The objective is demonstrable engineering competence across heterogeneous accelerated-computing systems and the platforms required to operate them reliably.

---

# Target Professional Identity

## Accelerated Compute Platform & AI Infrastructure Efficiency Engineer

The programme combines three intersecting engineering layers:

### Numerical and Algorithmic Computing

- Floating-point arithmetic
- Error analysis
- Conditioning and stability
- Linear algebra
- Numerical solvers
- Optimization
- Iterative methods
- Precision/performance trade-offs

### Accelerated Computing

- Computer architecture
- Parallel computing
- High-performance computing
- CUDA
- GPU performance engineering
- NVIDIA ecosystem
- AMD ROCm / HIP
- TPU / JAX
- Compiler systems
- Distributed accelerators
- ML systems
- Performance economics

### Compute Platform Engineering

- Linux systems
- Compute networking
- Containers
- GPU runtime infrastructure
- Kubernetes
- GPU scheduling
- Observability
- Site Reliability Engineering
- Inference serving
- Platform security
- Infrastructure automation
- Capacity engineering
- Compute FinOps

The professional moat is the ability to connect numerical correctness, low-level compute behaviour, platform reliability, capacity and economic outcomes.

---

# Status Key

| Status | Meaning |
|---|---|
| **ACTIVE** | Current focus |
| **QUEUED** | Required later |
| **SELECTIVE** | Complete only specified high-value material |
| **OPTIONAL** | Reference / gap-filler |
| **DONE** | Learning work completed |
| **GATE PASSED** | Competence demonstrated with evidence |

---

# ACE Core Course Atlas

| # | Phase | Course / Resource | Provider | Priority | Score | Hours | Target Window | Core Focus | Evidence / Outcome | Status | Link |
|---:|---|---|---|---|---:|---:|---|---|---|---|---|
| **1** | Architecture | **Computer Architecture** | Princeton / Coursera | CORE | **9.5** | **40** | Sep 2026 | Pipelines, caches, memory hierarchy, branch prediction, OoO, multicore | CPU/cache/memory benchmark | **ACTIVE** | https://www.coursera.org/learn/comparch |
| **2** | Numerical Computing | **CS205A — Mathematical Methods for Robotics, Vision and Graphics (selected)** | Stanford | SELECTIVE CORE SUPPORT | **9.5** | **20–25** | Sep–Oct 2026 | Floating point, conditioning, LU/QR/SVD, eigenproblems, optimization, iterative solvers, preconditioning | Numerical stability + solver benchmark suite | **SELECTIVE** | https://www.youtube.com/playlist?list=PLQ3UicqQtfNvQ_VzflHYKhAqZiTxOkSwi |
| **3** | Parallel Computing | **CS149 — Parallel Computing** | Stanford | CORE | **10** | **45** | Sep–Oct 2026 | SIMD/SIMT, decomposition, synchronization, locality, GPU architecture | Parallel scaling benchmark | QUEUED | https://cs149.stanford.edu/ |
| **4** | HPC | **High-Performance & Parallel Computing** | CU Boulder | CORE | **9.5** | **20** | Oct 2026 | HPC architecture, performance models, parallel workloads | HPC workload analysis | QUEUED | https://www.coursera.org/specializations/high-performance-parallel-computing |
| **5** | HPC | **Efficient Programming** | CU Boulder | CORE | **9.5** | **10** | Oct 2026 | Bottlenecks, optimization, profiling | CPU optimization experiment | QUEUED | https://www.coursera.org/learn/hpc-efficient-programming |
| **6** | HPC | **Parallel Computing with MPI** | CU Boulder | CORE | **9.5** | **10** | Oct 2026 | MPI, collectives, nonblocking communication, decomposition | MPI scaling experiment | QUEUED | https://www.coursera.org/learn/advanced-parallel-computing-mpi |
| **7** | CUDA | **CUDA Introduction / Primer** | NVIDIA | CORE | **9** | **3** | Oct 2026 | Kernels, threads, blocks, grids, host/device model | First CUDA kernel | QUEUED | https://developer.nvidia.com/cuda |
| **8** | CUDA | **Modern CUDA C++** | NVIDIA DLI | CORE | **10** | **15** | Oct–Nov 2026 | Native CUDA programming | CUDA implementation | QUEUED | https://learn.nvidia.com/ |
| **9** | CUDA | **CUDA Programming Guide + ACE Labs** | NVIDIA | CORE | **10** | **35** | Nov 2026 | Memory hierarchy, synchronization, occupancy, reductions, matmul | Nontrivial CUDA kernels | QUEUED | https://docs.nvidia.com/cuda/cuda-programming-guide/ |
| **10** | Profiling | **Nsight Systems** | NVIDIA | CORE | **10** | **10** | Nov 2026 | CPU/GPU timelines, launch overhead, idle time, transfers | Timeline diagnosis | QUEUED | https://docs.nvidia.com/nsight-systems/ |
| **11** | Profiling | **Nsight Compute** | NVIDIA | CORE | **10** | **15** | Nov 2026 | Kernel metrics, stalls, occupancy, bandwidth | Kernel diagnosis | QUEUED | https://docs.nvidia.com/nsight-compute/ |
| **12** | GPU Performance | **CUDA Memory Optimization Lab** | NVIDIA + ACE | CORE | **10** | **15** | Nov–Dec 2026 | Coalescing, shared memory, tiling, registers, caches | Before/after optimization | QUEUED | https://docs.nvidia.com/cuda/ |
| **13** | GPU Performance | **Streams / Async / CUDA Graphs** | NVIDIA | CORE | **9.5** | **15** | Dec 2026 | Latency hiding, overlap, asynchronous execution | Concurrency benchmark | QUEUED | https://docs.nvidia.com/cuda/cuda-programming-guide/ |
| **14** | GPU + ML | **PyTorch Custom CUDA Extension** | PyTorch | CORE | **9.5** | **12** | Dec 2026 | PyTorch integration with native GPU kernels | Custom accelerated operation | QUEUED | https://docs.pytorch.org/tutorials/advanced/cpp_extension.html |
| **15** | Advanced HPC | **CS267 — Applications of Parallel Computers** | UC Berkeley | CORE | **10** | **40** | Dec 2026–Jan 2027 | Parallel algorithms, distributed memory, communication, scalability | HPC scalability study | QUEUED | https://sites.google.com/lbl.gov/cs267-spr2025 |
| **16** | AMD | **AMD AI Academy** | AMD | CORE | **9.5** | **10** | Jan 2027 | ROCm ecosystem and AMD acceleration stack | ROCm architecture map | QUEUED | https://developer.amd.com/ |
| **17** | AMD | **HIP / ROCm Programming** | AMD | CORE | **10** | **20** | Jan 2027 | Portable accelerator programming | HIP kernels | QUEUED | https://rocm.docs.amd.com/projects/HIP/ |
| **18** | AMD | **CUDA → HIP Port + ROCm Profiling** | AMD + ACE | CORE | **10** | **20** | Jan 2027 | Cross-vendor portability and profiling | NVIDIA vs AMD analysis | QUEUED | https://rocm.docs.amd.com/ |
| **19** | TPU | **TPU Architecture + JAX Fundamentals** | Google | CORE | **9.5** | **20** | Feb 2027 | TPU architecture, JAX, JIT, compiler-first execution | JAX accelerator workload | QUEUED | https://cloud.google.com/tpu |
| **20** | TPU | **JAX on TPU / Scaling** | Google | CORE | **9.5** | **20** | Feb 2027 | Meshes, sharding, distributed TPU execution | TPU scaling experiment | QUEUED | https://jax.readthedocs.io/ |
| **21** | Compilers | **LLVM Compiler Fundamentals** | LLVM | CORE | **9.5** | **25** | Feb–Mar 2027 | AST, IR, optimization, lowering, JIT | LLVM IR artifact | QUEUED | https://llvm.org/docs/tutorial/ |
| **22** | Compilers | **Triton Kernel Programming** | Triton | CORE | **10** | **25** | Mar 2027 | Compiler-mediated GPU kernels, fusion, matmul, softmax | Triton vs CUDA benchmark | QUEUED | https://triton-lang.org/main/getting-started/tutorials/ |
| **23** | Compilers | **PyTorch Compiler / torch.compile** | PyTorch | CORE | **9.5** | **20** | Mar 2027 | TorchDynamo, Inductor, graph capture, generated kernels | Compiler-generated workload analysis | QUEUED | https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html |
| **24** | Distributed | **NCCL + Distributed GPU Systems** | NVIDIA | CORE | **10** | **25** | Mar–Apr 2027 | Collectives, topology, AllReduce, NVLink, PCIe, multi-GPU | Communication/scaling analysis | QUEUED | https://docs.nvidia.com/deeplearning/nccl/ |
| **25** | ML Systems | **CS336 — Language Modeling from Scratch** | Stanford | CORE | **10** | **60** | Apr–May 2027 | Transformers, training, scaling, evaluation, systems | Transformer profiling study | QUEUED | https://cs336.stanford.edu/ |
| **26** | ML Systems | **CME 295 — Transformers & LLMs** | Stanford | SELECTIVE | **9** | **15** | May 2027 | Training, MoE, quantization, hardware optimization, reasoning | LLM systems synthesis | SELECTIVE | https://cme295.stanford.edu/ |
| **27** | ML Systems | **Full Stack Deep Learning** | FSDL | CORE | **10** | **35** | May–Jun 2027 | Production ML, deployment, observability, infrastructure | Production ML artifact | QUEUED | https://fullstackdeeplearning.com/ |
| **28** | Self-Improving Systems | **CS329A — Self-Improving AI Agents** | Stanford | SELECTIVE | **9.5** | **15–20** | Jun 2027 | RL, test-time compute, verifiers, memory, long-horizon evaluation, AI optimization | AI-assisted performance-engineering synthesis | SELECTIVE | https://cs329a.stanford.edu/ |
| **29** | Agent Evaluation | **Writing Evals** | Anthropic | SELECTIVE | **9** | **2–3** | Jun 2027 | Evaluation design, verification, measurable agent performance | Evaluation specification | SELECTIVE | https://www.anthropic.com/learn |
| **30** | Agent Systems | **Building with Claude API** | Anthropic | SELECTIVE | **9** | **5–8** | As needed | Tool architecture and structured execution | Applied reference | SELECTIVE | https://docs.anthropic.com/ |
| **31** | Agent Systems | **MCP + MCP Advanced** | Anthropic | SELECTIVE | **9.5** | **6–8** | As needed | Tool/data connectivity and context architecture | MCP implementation | SELECTIVE | https://docs.anthropic.com/ |
| **32** | Agent Systems | **Effective Agents / Context Engineering** | Anthropic | SELECTIVE | **9** | **6–10** | As needed | Agent loops, delegation, context, tools | Engineering reference | SELECTIVE | https://www.anthropic.com/engineering/building-effective-agents |
| **33** | Agent Reference | **Microsoft MCP — selected labs** | Microsoft | OPTIONAL | **8** | **4–6** | As needed | Cross-language MCP | Implementation reference | OPTIONAL | https://github.com/microsoft/mcp-for-beginners |
| **34** | Agent Reference | **Microsoft AI Agents — selected lessons** | Microsoft | OPTIONAL | **7.5** | **5–8** | As needed | Enterprise agent patterns | Microsoft ecosystem familiarity | OPTIONAL | https://github.com/microsoft/ai-agents-for-beginners |
| **35** | Capstone | **Heterogeneous AI Compute Platform Capstone** | ACE | CORE | **10** | **40+** | Jun–Jul 2027 | Accelerators + platform + observability + economics | Final evidence portfolio | QUEUED | — |

---

# CS205A Numerical Computing Foundations — Selected Scope

CS205A is not treated as a full robotics/vision/graphics course. It is used as a targeted numerical-computing foundation for accelerated computing.

## Deep Study

- Floating-point representation and IEEE-754 reasoning
- Forward error, backward error and relative error
- Conditioning, stability and accuracy
- Gaussian elimination and LU factorization
- Least squares and condition numbers
- QR factorization and orthogonality
- Eigenvalues/eigenvectors and spectral reasoning
- Singular Value Decomposition
- Unconstrained optimization
- Conjugate Gradient
- Preconditioning

## Fast Pass / Reference

- Nonlinear systems and Newton-style methods
- Numerical differentiation and integration
- ODE methods
- PDE foundations
- Finite-element overview

## ACE Numerical Evidence Labs

### N1 — Floating-Point Accumulation

Compare:

- naive summation
- pairwise summation
- Kahan compensated summation

Across practical precisions where available.

Measure runtime, absolute error and relative error.

Later repeat on GPU and connect the result to parallel reduction design.

### N2 — Conditioning

Generate increasingly ill-conditioned linear systems and measure residual, forward error and condition number.

Explain why a numerically small residual does not necessarily imply a numerically accurate solution.

### N3 — Direct vs Iterative Solver

Compare LU, Conjugate Gradient and preconditioned Conjugate Gradient where mathematically appropriate.

Measure convergence, runtime and numerical behaviour.

Later map the workload to CPU and accelerator implementations.

### N4 — Precision / Performance Trade-off

Where supported, compare representative matrix workloads across FP64, FP32, TF32, FP16 and BF16.

Measure speed, memory consumption and numerical error.

This lab becomes a bridge to Tensor Cores, mixed precision, quantization and scientific-computing accuracy.

---

# Compute Platform Engineering Overlay

The ACE accelerated-computing core remains intact.

Compute Platform Engineering is interleaved with the core programme rather than becoming a separate second syllabus.

| ID | Module | Priority | Hours | Target Window | Core Capability | Evidence | Status |
|---|---|---:|---:|---|---|---|---|
| **CP1** | **Linux Systems Engineering** | **10/10** | **25–30** | Sep–Oct 2026 | Processes, cgroups, namespaces, systemd, filesystems, kernel, NUMA, logs | Diagnose deliberately broken GPU host | QUEUED |
| **CP2** | **Networking for Accelerated Compute** | **10/10** | **25–30** | Sep–Nov 2026 | TCP/IP, routing, DNS, TLS, MTU, bandwidth, NIC/GPU topology, RDMA concepts | Network performance + fault diagnosis | QUEUED |
| **CP3** | **Containers + NVIDIA GPU Runtime** | **10/10** | **15–20** | Nov–Dec 2026 | Docker, containerd, OCI, NVIDIA Container Toolkit, runtime compatibility | Reproducible GPU container environment | QUEUED |
| **CP4** | **Kubernetes + GPU Scheduling** | **10/10** | **40–50** | Jan–Mar 2027 | Kubernetes, GPU Operator, device plugins, quotas, priorities, Kueue | Operational GPU-aware cluster | QUEUED |
| **CP5** | **Observability + SRE for Compute** | **10/10** | **25–30** | Mar–Apr 2027 | Prometheus, Grafana, DCGM, SLI/SLO, alerts, incidents, runbooks | Dashboard + induced incident + recovery | QUEUED |
| **CP6** | **Inference Serving Engineering** | **10/10** | **30–40** | Apr–Jun 2027 | vLLM, TensorRT/TensorRT-LLM, Triton, KV cache, batching, latency/throughput | Serving benchmark | QUEUED |
| **CP7** | **Infrastructure Automation + Security** | **9/10** | **20–25** | Feb–Jun 2027 | Terraform/OpenTofu, Helm, GitOps, RBAC, secrets, image/security policy | Reproducible secured deployment | QUEUED |
| **CP8** | **Compute Capacity Engineering + FinOps** | **10/10** | **20–25** | Apr–Jul 2027 | GPU-hours, utilization, placement, cloud/local/spot/reserved, showback | Placement + cost model | QUEUED |

---

# Compute Platform Scope

## CP1 — Linux Systems Engineering

Required competence:

- processes and scheduling
- cgroups
- namespaces
- systemd
- `/proc`
- `/sys`
- kernel modules
- filesystems
- package/version management
- permissions
- logs
- memory and swap
- NUMA
- PCIe/device visibility
- driver troubleshooting

Core tools:

```text
ps
top
htop
systemctl
journalctl
dmesg
lsof
strace
lsmod
modprobe
mount
df
du
iostat
vmstat
free
numactl
ulimit
```

Evidence:

Diagnose failures involving driver state, runtime, CUDA libraries, memory, permissions, process contention, storage or device placement.

---

## CP2 — Networking for Accelerated Compute

Required competence:

- TCP/IP
- routing
- DNS
- TLS
- NAT
- MTU
- packet loss
- congestion
- latency vs throughput
- Ethernet
- RoCE concepts
- InfiniBand concepts
- RDMA concepts
- GPU/NIC/NUMA locality

Core tools:

```text
ip
ss
ping
traceroute
mtr
ethtool
tcpdump
iperf3
dig
nslookup
```

Accelerator relationship:

```text
GPU
 ↓
PCIe
 ↓
NIC
 ↓
NETWORK FABRIC
 ↓
NIC
 ↓
PCIe
 ↓
GPU
```

---

## CP3 — Containers + GPU Runtime

Required competence:

- Docker
- containerd
- OCI
- images and layers
- registries
- mounts
- device exposure
- NVIDIA Container Toolkit
- host/driver/container compatibility
- runtime classes
- reproducibility

Required experiment:

```text
LINUX HOST
    ↓
NVIDIA DRIVER
    ↓
DOCKER / CONTAINERD
    ↓
NVIDIA CONTAINER TOOLKIT
    ↓
PYTORCH CONTAINER
    ↓
CUDA WORKLOAD
```

Then deliberately introduce a compatibility or runtime fault and diagnose it.

---

## CP4 — Kubernetes + GPU Scheduling

Foundation:

- control plane
- kubelet
- Pods
- Deployments
- Services
- namespaces
- requests/limits
- QoS
- taints/tolerations
- affinity
- topology spread
- priority/preemption
- RBAC
- quotas
- CNI
- CSI
- admission policy

Accelerator layer:

- NVIDIA GPU Operator
- NVIDIA device plugin
- GPU Feature Discovery
- `nvidia.com/gpu`
- GPU node labels
- GPU health
- MIG
- MPS
- time slicing
- topology-aware placement
- Kueue

Target scenario:

```text
PRODUCTION INFERENCE
       ↓
reserved / priority capacity

TRAINING
       ↓
high-performance capacity

DEVELOPMENT
       ↓
shared / lower-priority capacity

EXCESS DEMAND
       ↓
policy-controlled queue
```

---

## CP5 — Compute Observability + SRE

Profiler question:

> Why is this kernel slow?

Platform question:

> Why is this compute service unhealthy?

Primary stack:

- Prometheus
- Grafana
- NVIDIA DCGM
- DCGM Exporter
- logs
- alerts
- SLIs
- SLOs
- incident response
- runbooks
- postmortems

Key metrics:

- GPU utilization
- GPU memory
- power
- temperature
- ECC/Xid
- job queue depth
- allocation
- failed jobs
- TTFT
- ITL
- p50/p95/p99 latency
- tokens/sec
- waiting requests
- KV-cache use

Evidence:

Detect → alert → diagnose → recover → document → prevent recurrence.

---

## CP6 — Inference Serving Engineering

Primary platform:

**vLLM**

Secondary:

- TensorRT
- TensorRT-LLM
- Triton Inference Server

Required concepts:

- continuous batching
- prefill vs decode
- KV cache
- PagedAttention concepts
- prefix caching
- speculative decoding
- quantization
- tensor parallelism
- model loading
- concurrency
- warm-up
- health checks
- autoscaling
- rollout strategies

Required metrics:

```text
TTFT
ITL
p50
p95
p99
requests/sec
tokens/sec
tokens/sec/GPU
VRAM
KV-cache use
GPU utilization
cost / million tokens
```

Where practical compare:

```text
BASELINE FRAMEWORK
        vs
vLLM
        vs
TensorRT / Triton
```

---

## CP7 — Infrastructure Automation + Security

Infrastructure:

- Terraform or OpenTofu
- Helm
- GitOps concepts
- CI/CD
- reproducible images
- configuration as code

Security:

- RBAC
- least privilege
- workload identity
- secrets
- network policy
- egress control
- signed images
- image scanning
- SBOM concepts
- audit trails
- tenant isolation

The objective is not generic DevOps mastery.

The objective is secure, repeatable accelerated-compute infrastructure.

---

## CP8 — Compute Capacity Engineering + FinOps

Required measures:

- GPU-hours
- effective GPU-hours
- utilization
- throughput/GPU
- cost/training run
- cost/request
- cost/million tokens
- performance/cost
- performance/watt where measurable

Capacity choices:

- local
- cloud
- on-demand
- reserved/committed
- spot/preemptible
- specialist accelerators

Placement model input:

```text
workload
model
accelerator-memory requirement
latency SLO
throughput target
data sensitivity
region
capacity availability
budget
```

Output:

```text
recommended accelerator
recommended platform
expected throughput
expected latency
expected cost
capacity risk
policy / sovereignty constraints
```

---

# Programme Timeline

| Period | Accelerated Computing Core | Numerical / Compute Platform Overlay |
|---|---|---|
| **Sep 2026** | Princeton Architecture / CS149 start | CS205A numerics + Linux fundamentals |
| **Oct 2026** | CS149 + HPC/MPI | CS205A selected solvers + Linux + networking |
| **Nov 2026** | CUDA Core | Networking + GPU containers |
| **Dec 2026** | GPU Performance | Containers + DCGM fundamentals |
| **Jan 2027** | CS267 + AMD | Kubernetes fundamentals |
| **Feb 2027** | AMD + TPU/JAX + LLVM | Kubernetes + IaC/security |
| **Mar 2027** | Triton + torch.compile + NCCL | GPU scheduling + Kueue + observability |
| **Apr 2027** | NCCL + CS336 | vLLM + observability/SRE |
| **May 2027** | CS336 + CME295 + FSDL | Serving optimization + FinOps |
| **Jun 2027** | FSDL + CS329A | Platform reliability + inference benchmark |
| **Jul 2027** | Integrated capstone | Policy-aware heterogeneous compute platform |

---

# 16 Evidence Gates

| Gate | Capability | Required Evidence | Status |
|---:|---|---|---|
| **1** | Computer Architecture | Cache/locality/memory benchmark | **ACTIVE** |
| **2** | Parallel Computing | Parallel implementation + scaling | QUEUED |
| **3** | HPC | OpenMP/MPI experiments | QUEUED |
| **4** | CUDA | Correct nontrivial CUDA kernels | QUEUED |
| **5** | GPU Performance | Profile → diagnose → optimize → measure | QUEUED |
| **6** | Advanced HPC | Compute/communication scaling analysis | QUEUED |
| **7** | AMD | CUDA→HIP port and AMD profiling | QUEUED |
| **8** | TPU/JAX | TPU/JAX workload + sharding | QUEUED |
| **9** | Compilers | Triton vs CUDA/PyTorch benchmark | QUEUED |
| **10** | Distributed | NCCL/multi-GPU scaling analysis | QUEUED |
| **11** | ML Systems | Transformer workload profiler study | QUEUED |
| **12** | Cross-Accelerator | Comparative accelerator analysis | QUEUED |
| **13** | Compute Host | Bootstrap and diagnose Linux GPU host | QUEUED |
| **14** | GPU Platform | GPU-aware Kubernetes cluster + scheduling policy | QUEUED |
| **15** | Observability & Serving | Model service + telemetry + SLO + incident response | QUEUED |
| **16** | Platform Economics | Policy-aware placement + capacity/cost analysis | QUEUED |

### Numerical Competence Requirement

CS205A does not create a seventeenth gate. Numerical correctness is a cross-cutting requirement inside Gates 3, 4, 5, 9, 11 and 12. An optimization does not pass if it improves performance while producing unjustified numerical degradation.

---

# Target Competency Levels

| Domain | July 2027 Target |
|---|---:|
| Numerical Computing / Stability | **Level 3** |
| Computer Architecture | **Level 3** |
| Parallel Computing | **Level 3** |
| HPC | **Level 3** |
| CUDA Programming | **Level 3+** |
| GPU Performance Engineering | **Level 4** |
| NVIDIA Ecosystem | **Level 3** |
| AMD ROCm / HIP | **Level 2–3** |
| TPU / JAX | **Level 2–3** |
| Compiler Systems | **Level 3** |
| Distributed Accelerators | **Level 3** |
| ML Systems | **Level 3** |
| Linux Systems Engineering | **Level 3** |
| Compute Networking | **Level 3** |
| Containers / GPU Runtime | **Level 3** |
| GPU-aware Kubernetes | **Level 3** |
| Compute Observability / SRE | **Level 3** |
| Inference Serving | **Level 3** |
| Infrastructure Automation / Security | **Level 2–3** |
| Compute Capacity / FinOps | **Level 4** |
| **Integrated Compute Platform Engineering** | **Level 4** |

---

# Technology Priority Rules

Do not attempt to master every adjacent technology.

## Scheduling

Primary: **Kueue**

Selective awareness:

- Volcano
- Slurm

## Distributed ML

Primary:

- PyTorch DDP
- PyTorch FSDP

Selective:

- DeepSpeed
- Megatron concepts

## Serving

Primary: **vLLM**

Secondary:

- TensorRT / TensorRT-LLM
- Triton Inference Server

## Observability

Primary:

- Prometheus
- Grafana
- NVIDIA DCGM

## Distributed Python

Understand: **Ray**

Do not make Ray an independent specialization.

## Languages

Primary:

- Python
- Bash
- C++
- CUDA C++

Add progressively: **Go**

Optional: **Rust**

---

# New Course Intake Rule

Any newly discovered course, certification, lecture series, vendor academy or social-media recommendation must pass this test:

1. Does it teach a capability not already covered?
2. Is it materially better than the currently selected source?
3. Does it create technical depth rather than prestige alone?
4. Can it generate engineering evidence?
5. Is the time cost justified?
6. Does it strengthen the July 2027 professional identity?

Possible decisions:

**ADD**  
**REPLACE**  
**SELECTIVE**  
**OPTIONAL**  
**DUPLICATE**  
**SKIP**

New resources do not automatically increase programme hours.

Where possible, stronger new material replaces weaker or duplicated material.

---

# Current Position

## ACTIVE

**Phase 1 — Computer Architecture**

### Princeton University — Computer Architecture

Planned effort: **~40 hours**

Current objective: **Computer Architecture → Level 3**

Current Evidence Gate: **Gate 1 — demonstrate and explain CPU cache/locality/memory-performance behaviour.**

Immediate learning principle:

**LEARN → BUILD → MEASURE → EXPLAIN → IMPROVE → COMMIT**

CS205A begins as an interleaved numerical-computing support block after the current architecture sprint is underway; it does not displace Princeton.

---

# Final Capstone

## Heterogeneous AI Compute Platform Capstone

The capstone must demonstrate the complete stack:

```text
USER / WORKLOAD
       ↓
MATHEMATICAL / NUMERICAL FORMULATION
       ↓
ALGORITHM
       ↓
POLICY
       ↓
SCHEDULER
       ↓
CONTAINER / RUNTIME
       ↓
ACCELERATOR SELECTION
       ↓
MODEL / APPLICATION
       ↓
COMPILER
       ↓
KERNEL
       ↓
ACCELERATOR
       ↓
MEMORY
       ↓
INTERCONNECT / NETWORK
       ↓
TELEMETRY
       ↓
PERFORMANCE + NUMERICAL ACCURACY
       ↓
CAPACITY
       ↓
COST
       ↓
ENGINEERING DECISION
```

Where practical compare:

- CPU
- NVIDIA CUDA
- AMD ROCm/HIP
- Triton
- PyTorch compiler
- TPU/JAX

The platform component should include:

- containerized execution
- scheduling policy
- observability
- workload health
- numerical correctness
- latency/throughput
- capacity utilization
- infrastructure economics
- portability
- security/policy constraints

---

# July 2027 Final Engineering Test

By July 2027 I should be able to receive an unfamiliar accelerated-compute workload and independently:

1. Characterize the mathematical and numerical problem.
2. Characterize the algorithm.
3. Characterize the workload.
4. Identify processor and accelerator requirements.
5. Select appropriate compute hardware.
6. Establish a reproducible environment.
7. Containerize the workload.
8. Place and schedule it appropriately.
9. Establish a performance and numerical-accuracy baseline.
10. Profile actual execution.
11. Identify the dominant compute bottleneck.
12. Diagnose relevant host/runtime/network bottlenecks.
13. Identify numerical stability or conditioning risks.
14. Select an optimization strategy.
15. Implement or prototype the change.
16. Re-measure performance.
17. Validate correctness and acceptable numerical error.
18. Evaluate portability.
19. Evaluate distributed scaling.
20. Operate and monitor the workload.
21. Define relevant SLIs/SLOs.
22. Diagnose infrastructure failures.
23. Quantify capacity implications.
24. Quantify economic implications.
25. Explain security and governance constraints.
26. Recommend the correct deployment target.
27. Communicate the engineering decision clearly.

---

# Completion Standard

Courses provide knowledge.

Labs create practical familiarity.

Benchmarks create evidence.

Numerical analysis establishes whether a result can be trusted.

Evidence gates establish competence.

The capstone establishes the integrated professional identity.

The programme is complete only when the title:

## Accelerated Compute Platform & AI Infrastructure Efficiency Engineer

is defensible through reproducible engineering evidence.
