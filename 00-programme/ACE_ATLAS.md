# ACE Master Atlas

**Programme:** Accelerated Computing & AI Infrastructure Efficiency Engineer  
**Target completion:** 31 July 2027  
**Study intensity:** ~15 focused hours/week  
**Programme status:** ACTIVE  
**Current phase:** Phase 1 — Computer Architecture  
**Current course:** Princeton Computer Architecture

---

# North Star

**ALGORITHM → MODEL → COMPILER → KERNEL → ACCELERATOR → MEMORY → INTERCONNECT → CLUSTER → ENERGY → COST**

The objective is not course completion.

The objective is demonstrable engineering competence across heterogeneous accelerated-computing systems.

---

# Status Key

| Status | Meaning |
|---|---|
| **ACTIVE** | Current focus |
| **QUEUED** | Required later |
| **SELECTIVE** | Complete only specified high-value material |
| **OPTIONAL** | Reference / gap-filler |
| **DONE** | Course complete |
| **GATE PASSED** | Competence demonstrated with evidence |

---

# ACE Master Course Atlas

| # | Phase | Course / Resource | Provider | Priority | Score | Hours | Target Window | Core Focus | Evidence / Outcome | Status | Link |
|---:|---|---|---|---|---:|---:|---|---|---|---|---|
| **1** | Architecture | **Computer Architecture** | Princeton / Coursera | CORE | **9.5** | **40** | Aug–Sep 2026 | Pipelines, caches, memory hierarchy, branch prediction, OoO, multicore | CPU/cache/memory benchmark | **ACTIVE** | https://www.coursera.org/learn/comparch |
| **2** | Parallel Computing | **CS149 — Parallel Computing** | Stanford | CORE | **10** | **45** | Sep–Oct 2026 | SIMD/SIMT, parallel decomposition, synchronization, locality, GPU architecture | Parallel scaling benchmark | QUEUED | https://cs149.stanford.edu/ |
| **3** | HPC | **High-Performance & Parallel Computing** | CU Boulder / Coursera | CORE | **9.5** | **20** | Oct 2026 | HPC architecture, performance models, parallel workloads | HPC workload analysis | QUEUED | https://www.coursera.org/specializations/high-performance-parallel-computing |
| **4** | HPC | **Efficient Programming** | CU Boulder | CORE | **9.5** | **10** | Oct 2026 | Performance bottlenecks, optimization, profiling | CPU optimization experiment | QUEUED | https://www.coursera.org/learn/hpc-efficient-programming |
| **5** | HPC | **Parallel Computing with MPI** | CU Boulder | CORE | **9.5** | **10** | Oct 2026 | MPI, collectives, nonblocking communication, decomposition | MPI scaling experiment | QUEUED | https://www.coursera.org/learn/advanced-parallel-computing-mpi |
| **6** | CUDA | **CUDA Introduction / Even Easier CUDA** | NVIDIA | CORE | **9** | **3** | Oct 2026 | Kernels, threads, blocks, grids, host/device mental model | First CUDA kernel | QUEUED | https://developer.nvidia.com/cuda |
| **7** | CUDA | **Modern CUDA C++** | NVIDIA DLI | CORE | **10** | **15** | Oct–Nov 2026 | Native CUDA programming and execution | CUDA implementation | QUEUED | https://learn.nvidia.com/courses/course-detail?course_id=course-v1%3ADLI+S-AC-04+V2 |
| **8** | CUDA | **CUDA Programming Guide + Labs** | NVIDIA | CORE | **10** | **35** | Nov 2026 | Memory hierarchy, synchronization, occupancy, reductions, matmul | Nontrivial CUDA kernels | QUEUED | https://docs.nvidia.com/cuda/cuda-programming-guide/ |
| **9** | Profiling | **Nsight Systems** | NVIDIA | CORE | **10** | **10** | Nov 2026 | CPU/GPU timeline, launch overhead, idle time, transfers | Timeline diagnosis | QUEUED | https://docs.nvidia.com/nsight-systems/UserGuide/index.html |
| **10** | Profiling | **Nsight Compute** | NVIDIA | CORE | **10** | **15** | Nov 2026 | Kernel metrics, stalls, occupancy, bandwidth | Kernel diagnosis | QUEUED | https://docs.nvidia.com/nsight-compute/NsightCompute/index.html |
| **11** | GPU Performance | **CUDA Memory Optimization Lab** | NVIDIA + ACE Lab | CORE | **10** | **15** | Nov–Dec 2026 | Coalescing, shared memory, tiling, registers, caches | Before/after optimization | QUEUED | https://docs.nvidia.com/cuda/ |
| **12** | GPU Performance | **Streams / Async / CUDA Graphs** | NVIDIA | CORE | **9.5** | **15** | Dec 2026 | Latency hiding, overlap, async execution, graphs | Concurrency benchmark | QUEUED | https://docs.nvidia.com/cuda/cuda-programming-guide/ |
| **13** | GPU + ML | **PyTorch Custom CUDA Extension** | PyTorch | CORE | **9.5** | **12** | Dec 2026 | Connect PyTorch to custom native GPU kernels | Custom accelerated op | QUEUED | https://docs.pytorch.org/tutorials/advanced/cpp_extension.html |
| **14** | Advanced HPC | **CS267 — Applications of Parallel Computers** | UC Berkeley | CORE | **10** | **40** | Dec 2026–Jan 2027 | Parallel algorithms, distributed memory, communication cost, scalability | HPC scalability study | QUEUED | https://sites.google.com/lbl.gov/cs267-spr2025 |
| **15** | AMD | **AMD AI Academy** | AMD | CORE | **9.5** | **10** | Jan 2027 | ROCm ecosystem and AMD acceleration stack | ROCm architecture map | QUEUED | https://developer.amd.com/amd-ai-academy/ |
| **16** | AMD | **HIP / ROCm Programming** | AMD | CORE | **10** | **20** | Jan 2027 | Portable accelerator programming | HIP kernels | QUEUED | https://rocm.docs.amd.com/projects/HIP/ |
| **17** | AMD | **CUDA → HIP Port + ROCm Profiling** | AMD + ACE Lab | CORE | **10** | **20** | Jan 2027 | Cross-vendor portability and profiling | NVIDIA vs AMD comparison | QUEUED | https://rocm.docs.amd.com/ |
| **18** | TPU | **TPU Architecture + JAX Fundamentals** | Google | CORE | **9.5** | **20** | Feb 2027 | TPU architecture, JAX, JIT, compiler-first execution | JAX accelerator workload | QUEUED | https://docs.cloud.google.com/tpu/docs/intro-to-tpu |
| **19** | TPU | **JAX on Cloud TPU / Scaling** | Google | CORE | **9.5** | **20** | Feb 2027 | Device meshes, sharding, distributed TPU execution | TPU scaling experiment | QUEUED | https://docs.cloud.google.com/tpu/docs/run-calculation-jax |
| **20** | Compilers | **LLVM — Kaleidoscope / Compiler Fundamentals** | LLVM | CORE | **9.5** | **25** | Feb–Mar 2027 | AST, IR, optimization, lowering, JIT | LLVM IR artifact | QUEUED | https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/ |
| **21** | Compilers | **Triton Kernel Programming** | Triton | CORE | **10** | **25** | Mar 2027 | Compiler-mediated GPU kernels, fusion, matmul, softmax | Triton vs CUDA benchmark | QUEUED | https://triton-lang.org/main/getting-started/tutorials/ |
| **22** | Compilers | **PyTorch Compiler / torch.compile** | PyTorch | CORE | **9.5** | **20** | Mar 2027 | TorchDynamo, Inductor, graph capture, generated kernels | Compiler-generated workload analysis | QUEUED | https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html |
| **23** | Distributed | **NCCL + Distributed GPU Systems** | NVIDIA | CORE | **10** | **25** | Mar–Apr 2027 | Collectives, topology, AllReduce, NVLink/PCIe, multi-GPU | Scaling / communication analysis | QUEUED | https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/ |
| **24** | ML Systems | **CS336 — Language Modeling from Scratch** | Stanford | CORE | **10** | **60** | Apr–May 2027 | Tokenization, transformers, training, scaling, evaluation | Transformer profiling study | QUEUED | https://cs336.stanford.edu/ |
| **25** | ML Systems | **CME 295 — Transformers & LLMs** | Stanford | SELECTIVE | **9** | **15** | May 2027 | Training, MoE, quantization, hardware optimization, reasoning | LLM systems synthesis | SELECTIVE | https://cme295.stanford.edu/ |
| **26** | ML Systems | **Full Stack Deep Learning** | FSDL | CORE | **10** | **35** | May–Jun 2027 | Production ML, deployment, observability, infrastructure | Production ML artifact | QUEUED | https://fullstackdeeplearning.com/ |
| **27** | Self-Improving Systems | **CS329A — Self-Improving AI Agents** | Stanford | SELECTIVE | **9.5** | **15–20** | Jun 2027 | RL, test-time compute, verifiers, memory, long-horizon evaluation, AI-generated optimization | AI-assisted performance engineering synthesis | **SELECTIVE** | https://cs329a.stanford.edu/ |
| **28** | Agent Evaluation | **Writing Evals** | Anthropic Academy | SELECTIVE | **9** | **2–3** | Jun 2027 | Evaluation design, verifiers, measurable agent performance | Evaluation specification | SELECTIVE | https://www.anthropic.com/learn |
| **29** | Agent Systems | **Building with Claude API** | Anthropic | SELECTIVE | **9** | **5–8** | As needed | API/tool architecture and structured execution | Applied reference | SELECTIVE | https://docs.anthropic.com/en/docs/resources/courses |
| **30** | Agent Systems | **MCP + MCP Advanced** | Anthropic | SELECTIVE | **9.5** | **6–8** | As needed | Tool/data connectivity, context architecture | MCP implementation | SELECTIVE | https://docs.anthropic.com/en/docs/resources/courses |
| **31** | Agent Systems | **Agent SDK / Effective Agents / Context Engineering** | Anthropic | SELECTIVE | **9** | **6–10** | As needed | Agent loops, delegation, context, tool architecture | Engineering reference | SELECTIVE | https://www.anthropic.com/engineering/building-effective-agents |
| **32** | Cross-vendor Agent Reference | **MCP for Beginners — selected labs** | Microsoft | OPTIONAL | **8** | **4–6** | As needed | Multi-language MCP: Python, TS, Java, .NET, Rust | Cross-language reference | OPTIONAL | https://github.com/microsoft/mcp-for-beginners |
| **33** | Cross-vendor Agent Reference | **AI Agents for Beginners — selected lessons** | Microsoft | OPTIONAL | **7.5** | **5–8** | As needed | Enterprise agent implementation patterns | Microsoft ecosystem familiarity | OPTIONAL | https://github.com/microsoft/ai-agents-for-beginners |
| **34** | Capstone | **Cross-Accelerator Engineering Capstone** | ACE | CORE | **10** | **40+** | Jun–Jul 2027 | CPU vs CUDA vs HIP vs Triton vs compiler vs TPU | Final evidence portfolio | QUEUED | — |

---

# Programme Timeline Atlas

| Period | Primary Identity Being Built | Main Courses / Work |
|---|---|---|
| **Aug 2026** | Architecture learner | Princeton Computer Architecture |
| **Sep 2026** | Architecture → Parallel systems | Princeton + Stanford CS149 |
| **Oct 2026** | Parallel/HPC practitioner | CS149 + CU Boulder HPC/MPI |
| **Nov 2026** | CUDA programmer | NVIDIA CUDA C++ + CUDA Guide |
| **Dec 2026** | GPU performance engineer | Nsight + memory + streams + CUDA extension |
| **Jan 2027** | HPC + heterogeneous accelerator engineer | Berkeley CS267 + AMD ROCm/HIP |
| **Feb 2027** | Multi-accelerator engineer | AMD → TPU/JAX → LLVM |
| **Mar 2027** | Compiler-aware accelerator engineer | LLVM + Triton + torch.compile |
| **Apr 2027** | Distributed ML systems engineer | NCCL + Stanford CS336 |
| **May 2027** | LLM systems engineer | CS336 + CME295 + FSDL |
| **Jun 2027** | Autonomous performance systems | FSDL + CS329A selected material |
| **Jul 2027** | **Accelerated Computing Engineer** | Cross-accelerator capstone + final evidence review |

---

# 12 Evidence Gates

| Gate | Capability | Required Evidence | Status |
|---:|---|---|---|
| **1** | Computer Architecture | Cache/locality/memory benchmark | ACTIVE |
| **2** | Parallel Computing | Parallel implementation + scaling analysis | QUEUED |
| **3** | HPC | OpenMP/MPI experiments | QUEUED |
| **4** | CUDA | Correct nontrivial CUDA kernels | QUEUED |
| **5** | GPU Performance | Profile → diagnose → optimize → measure | QUEUED |
| **6** | Advanced HPC | Compute/communication scaling analysis | QUEUED |
| **7** | AMD | CUDA→HIP port and AMD profiling | QUEUED |
| **8** | TPU/JAX | Real TPU workload + sharding | QUEUED |
| **9** | Compilers | Triton vs CUDA/PyTorch benchmark | QUEUED |
| **10** | Distributed | Multi-GPU/NCCL scaling analysis | QUEUED |
| **11** | ML Systems | Transformer workload profiler study | QUEUED |
| **12** | Cross-Accelerator | Full comparative capstone | QUEUED |

---

# Target Competency Levels

| Domain | July 2027 Target |
|---|---:|
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
| Infrastructure Performance Economics | **Level 4** |
| **Integrated ACE Capability** | **Level 4** |

---

# New Course Intake Rule

Any newly discovered free course, certification, university lecture series, vendor academy or social-media recommendation must pass this test before entering the ACE programme:

1. Does it teach a capability not already covered?
2. Is it materially better than the resource already selected?
3. Does it provide deeper technical competence rather than prestige alone?
4. Can it produce engineering evidence?
5. Is the time cost justified?
6. Does it strengthen the July 2027 ACE identity?

Possible decisions:

**ADD**
**REPLACE**
**SELECTIVE**
**OPTIONAL**
**DUPLICATE**
**SKIP**

New resources do not automatically increase total programme hours.

Where possible, superior new material replaces or compresses weaker/duplicated material.

---

# Current Position

## ACTIVE

**Phase 1 — Computer Architecture**

### Princeton University
Computer Architecture

Planned effort: **~40 hours**

Current target:

**Computer Architecture Level 0/1 → Level 3**

Current Evidence Gate:

**Demonstrate and explain CPU cache/locality/memory-performance behaviour.**

---

# July 2027 Completion Definition

ACE is complete when I can receive an unfamiliar accelerated-computing workload and independently:

1. Characterize the algorithm.
2. Understand the relevant processor/accelerator architecture.
3. Establish a reproducible baseline.
4. Profile actual execution.
5. Identify the dominant bottleneck.
6. Explain the bottleneck mechanistically.
7. Select an appropriate optimization.
8. Implement or prototype it.
9. Re-measure performance.
10. Validate correctness.
11. Evaluate portability.
12. Evaluate distributed scaling.
13. Estimate infrastructure implications.
14. Estimate economic impact.
15. Communicate the recommendation clearly.

**Courses provide knowledge.**

**Evidence gates establish competence.**

**The capstone establishes the professional identity.**
