# Accelerated Computing Engineer — Competency Matrix

**Programme:** Accelerated Computing Engineer (ACE)  
**Target completion:** 31 July 2027  
**Purpose:** Define objective competence levels across the ACE programme.

---

# Competency Levels

## Level 0 — Unfamiliar
I have little or no working understanding of the domain.

## Level 1 — Foundational
I understand the terminology and major concepts and can follow guided examples.

## Level 2 — Working
I can implement standard tasks independently, troubleshoot common problems, and explain what I am doing.

## Level 3 — Strong
I can diagnose unfamiliar problems, make engineering trade-offs, optimize implementations, and defend my reasoning using evidence.

## Level 4 — Engineer-Level
I can apply the domain to novel workloads, integrate it with adjacent systems, quantify trade-offs, and produce reproducible engineering evidence.

The ACE target is not Level 4 in every subfield.

The target is:

- Level 3+ in the core accelerated-computing domains
- Level 2–3 in adjacent accelerator ecosystems
- Level 4 in integrated performance reasoning

---

# 1. Computer Architecture

**Target level:** 3 — Strong

## Level 1
- Understand CPU, core, instruction, register, cache, RAM
- Understand basic pipelining
- Explain latency and throughput
- Recognize SIMD

## Level 2
- Explain L1/L2/L3 cache hierarchy
- Explain temporal and spatial locality
- Understand branch prediction
- Explain cache misses and memory latency
- Reason about multicore execution
- Benchmark different memory-access patterns

## Level 3
- Diagnose performance effects caused by cache and memory behaviour
- Explain why two algorithmically equivalent implementations perform differently
- Relate processor architecture to observed benchmark results
- Reason about arithmetic intensity and memory pressure
- Distinguish compute limitations from data-movement limitations

## Level 4
- Build architecture-aware implementations for unfamiliar workloads
- Predict major bottlenecks before profiling
- Relate CPU architectural constraints to GPU/accelerator design choices

### ACE Evidence
- [ ] Cache/locality benchmark
- [ ] Memory-access benchmark
- [ ] Written interpretation
- [ ] Architecture-to-performance explanation

**Current level:** 0  
**Target:** 3

---

# 2. Parallel Computing

**Target level:** 3 — Strong

## Level 1
- Understand concurrency vs parallelism
- Understand threads and processes
- Understand SIMD and SIMT
- Understand synchronization

## Level 2
- Decompose workloads into parallel work
- Understand race conditions
- Use synchronization primitives correctly
- Reason about load balancing
- Explain strong vs weak scaling

## Level 3
- Identify parallelism opportunities in unfamiliar workloads
- Diagnose synchronization and contention problems
- Quantify parallel overhead
- Explain scalability limits
- Select appropriate parallel decomposition strategies

## Level 4
- Design architecture-independent parallel algorithms
- Map algorithms effectively to CPUs, GPUs and distributed systems
- Optimize work distribution across heterogeneous hardware

### ACE Evidence
- [ ] Parallel implementation
- [ ] Scaling benchmark
- [ ] Parallel-efficiency calculation
- [ ] Bottleneck explanation

**Current level:** 0  
**Target:** 3

---

# 3. High-Performance Computing

**Target level:** 3 — Strong

## Level 1
- Understand HPC terminology
- Understand compute nodes and clusters
- Understand OpenMP and MPI conceptually

## Level 2
- Write OpenMP code
- Write basic MPI programs
- Use point-to-point communication
- Use collective operations
- Measure workload scaling

## Level 3
- Use nonblocking communication
- Overlap communication and computation
- Perform domain decomposition
- Diagnose communication overhead
- Reason about parallel I/O
- Analyse scalability across nodes

## Level 4
- Design distributed HPC workloads
- Select decomposition strategies based on workload and architecture
- Optimize communication patterns
- Evaluate accelerator-enabled HPC architectures

### ACE Evidence
- [ ] OpenMP implementation
- [ ] MPI implementation
- [ ] Scaling study
- [ ] Communication/computation analysis

**Current level:** 0  
**Target:** 3

---

# 4. CUDA Programming

**Target level:** 3 — Strong

## Level 1
- Understand host and device
- Understand kernel launches
- Understand thread/block/grid hierarchy
- Understand basic device memory

## Level 2
- Write CUDA kernels independently
- Allocate and transfer device memory
- Synchronize correctly
- Implement vector operations
- Implement reductions
- Implement basic matrix operations

## Level 3
- Use shared memory intentionally
- Optimize memory access
- Understand coalescing
- Reason about occupancy
- Manage registers and shared-memory trade-offs
- Design kernels for unfamiliar workloads
- Diagnose correctness and performance issues

## Level 4
- Develop highly optimized custom kernels
- Use advanced synchronization and warp primitives
- Apply architecture-aware optimization
- Integrate custom CUDA into production ML/HPC workloads

### ACE Evidence
- [ ] Vector kernel
- [ ] Reduction
- [ ] Naive matrix multiplication
- [ ] Tiled matrix multiplication
- [ ] Optimized nontrivial kernel
- [ ] PyTorch CUDA extension

**Current level:** 0  
**Target:** 3+

---

# 5. GPU Performance Engineering

**Target level:** 4 — Engineer-Level

This is one of the programme's core differentiators.

## Level 1
- Understand GPU utilization
- Understand memory bandwidth
- Understand occupancy conceptually
- Run basic profiling tools

## Level 2
- Use Nsight Systems
- Use Nsight Compute
- Identify idle GPU periods
- Identify transfer overhead
- Read common kernel metrics
- Distinguish compute-bound and memory-bound workloads

## Level 3
- Diagnose kernel bottlenecks from profiler evidence
- Identify memory coalescing problems
- Identify register/shared-memory constraints
- Interpret warp stalls
- Diagnose launch/synchronization overhead
- Optimize and quantitatively validate changes

## Level 4
Given an unfamiliar GPU workload:

1. Establish a baseline
2. Profile execution
3. Form a bottleneck hypothesis
4. Identify the architectural cause
5. Implement an optimization
6. Re-profile
7. Quantify improvement
8. Check numerical correctness
9. Explain trade-offs
10. Determine whether further optimization is economically worthwhile

### ACE Evidence
- [ ] Nsight Systems report
- [ ] Nsight Compute report
- [ ] Bottleneck hypothesis
- [ ] Optimization
- [ ] Before/after benchmark
- [ ] Written engineering interpretation

**Current level:** 0  
**Target:** 4

---

# 6. NVIDIA Accelerated-Computing Ecosystem

**Target level:** 3 — Strong

## Level 1
- Understand CUDA ecosystem
- Recognize CUDA-X libraries
- Understand role of cuBLAS, cuDNN and TensorRT

## Level 2
- Use CUDA runtime effectively
- Use Nsight tools
- Understand CUDA Graphs
- Understand NCCL conceptually
- Recognize when optimized NVIDIA libraries should replace custom code

## Level 3
- Select among CUDA, Triton, libraries and framework-generated kernels
- Analyze NVIDIA GPU workloads end-to-end
- Understand multi-GPU topology
- Reason about NVLink, PCIe and communication costs
- Integrate custom acceleration into ML systems

## Level 4
- Architect large-scale NVIDIA accelerated systems
- Optimize workload execution from kernel through multi-node infrastructure

### ACE Evidence
- [ ] CUDA workload
- [ ] Nsight diagnosis
- [ ] CUDA Graph experiment
- [ ] NCCL/multi-GPU experiment
- [ ] Library vs custom-kernel comparison

**Current level:** 0  
**Target:** 3

---

# 7. AMD ROCm / HIP

**Target level:** 2–3

## Level 1
- Understand ROCm ecosystem
- Understand HIP
- Recognize AMD accelerator architecture terminology

## Level 2
- Write HIP kernels
- Port CUDA code to HIP
- Compile and execute ROCm workloads
- Use AMD profiling tools
- Explain major CUDA/HIP similarities and differences

## Level 3
- Analyze performance differences between NVIDIA and AMD implementations
- Optimize workloads on AMD hardware
- Make architecture-aware portability decisions
- Identify vendor-specific dependencies

## Level 4
- Architect cross-vendor accelerator software at production scale

### ACE Evidence
- [ ] CUDA reduction ported to HIP
- [ ] CUDA tiled matmul ported to HIP
- [ ] Third workload port
- [ ] AMD profiling
- [ ] NVIDIA vs AMD analysis

**Current level:** 0  
**Target:** 2–3

---

# 8. TPU / JAX / XLA

**Target level:** 2–3

## Level 1
- Understand TPU purpose and architecture
- Understand JAX execution model
- Understand JIT compilation conceptually

## Level 2
- Run JAX workloads
- Use jit
- Use vectorization transformations
- Execute on TPU
- Understand device meshes and sharding
- Profile basic TPU workloads

## Level 3
- Design workloads with TPU execution characteristics in mind
- Analyze sharding strategies
- Compare TPU and GPU execution models
- Reason about compiler-driven accelerator optimization

## Level 4
- Architect large distributed TPU workloads
- Optimize complex TPU model training/inference systems

### ACE Evidence
- [ ] JAX workload
- [ ] TPU execution
- [ ] Sharding experiment
- [ ] TPU vs GPU architectural comparison

**Current level:** 0  
**Target:** 2–3

---

# 9. Compiler Systems

**Target level:** 3 — Strong

## Level 1
- Understand source code, AST, IR and machine code
- Understand compiler optimization conceptually

## Level 2
- Generate and inspect LLVM IR
- Understand optimization passes
- Understand JIT compilation
- Write basic Triton kernels
- Understand torch.compile pipeline

## Level 3
- Explain lowering from high-level model operations to accelerator kernels
- Benchmark compiler-generated kernels
- Compare Triton against CUDA
- Reason about kernel fusion
- Inspect generated code
- Diagnose cases where compiler optimization succeeds or fails

## Level 4
- Develop custom compiler transformations or advanced backend integrations
- Perform hardware/software co-design work

### ACE Evidence
- [ ] LLVM artifact
- [ ] IR inspection
- [ ] Triton vector operation
- [ ] Triton softmax or matmul
- [ ] Triton vs CUDA benchmark
- [ ] torch.compile investigation

**Current level:** 0  
**Target:** 3

---

# 10. Distributed Accelerators

**Target level:** 3 — Strong

## Level 1
- Understand data parallelism
- Understand model parallelism
- Understand collective communication
- Understand multi-GPU systems

## Level 2
- Use distributed PyTorch
- Understand NCCL collectives
- Measure multi-GPU scaling
- Understand PCIe and NVLink implications

## Level 3
- Diagnose communication bottlenecks
- Analyze AllReduce overhead
- Reason about topology
- Overlap computation and communication
- Compare data, tensor and pipeline parallel approaches
- Interpret scaling efficiency

## Level 4
- Architect multi-node accelerator clusters
- Optimize network, accelerator and workload interaction at scale

### ACE Evidence
- [ ] Distributed workload
- [ ] NCCL experiment
- [ ] Scaling measurement
- [ ] Communication analysis

**Current level:** 0  
**Target:** 3

---

# 11. ML Systems / LLM Workloads

**Target level:** 3 — Strong

## Level 1
- Understand transformer architecture
- Understand training vs inference
- Understand tokens and context length

## Level 2
- Build/train a small transformer
- Understand attention computation
- Understand batching
- Understand quantization
- Understand model memory requirements
- Profile an ML workload

## Level 3
- Connect model architecture to accelerator behavior
- Identify memory-heavy vs compute-heavy operations
- Analyze inference bottlenecks
- Understand KV-cache implications
- Analyze throughput/latency trade-offs
- Relate precision changes to performance
- Connect distributed model execution to communication costs

## Level 4
- Design and optimize large-scale ML systems across model, compiler, kernel and infrastructure layers

### ACE Evidence
- [ ] Small transformer
- [ ] GPU training benchmark
- [ ] Inference benchmark
- [ ] Memory analysis
- [ ] Profiler evidence
- [ ] Model-to-hardware performance explanation

**Current level:** 0  
**Target:** 3

---

# 12. Infrastructure Performance Economics

**Target level:** 4 — Engineer-Level

This is the second major programme differentiator.

## Level 1
- Understand throughput
- Understand latency
- Understand utilization
- Understand GPU-hours

## Level 2
- Calculate throughput per accelerator
- Calculate compute cost per workload
- Compare hardware options
- Understand capacity utilization
- Measure performance-per-cost

## Level 3
- Translate profiler results into infrastructure implications
- Estimate impact of optimization on GPU-hours
- Compare accelerator options economically
- Reason about performance-per-watt
- Evaluate build-vs-buy and library-vs-custom trade-offs

## Level 4
Given an AI/HPC workload:

1. Characterize workload
2. Identify hardware bottlenecks
3. Measure actual execution
4. Recommend architecture
5. Quantify performance impact
6. Quantify infrastructure impact
7. Estimate cost impact
8. Explain assumptions
9. Identify operational risks
10. Recommend when further optimization is not economically justified

### ACE Evidence
- [ ] Cost/performance model
- [ ] GPU-hours calculation
- [ ] Accelerator comparison
- [ ] Optimization business-impact analysis
- [ ] Capstone infrastructure recommendation

**Current level:** 0  
**Target:** 4

---

# Integrated ACE Capability

The final ACE competence is not the sum of isolated technologies.

The programme target is the ability to trace a workload through:

**ALGORITHM**
↓
**MODEL / APPLICATION**
↓
**COMPILER**
↓
**KERNEL**
↓
**ACCELERATOR**
↓
**MEMORY**
↓
**INTERCONNECT**
↓
**CLUSTER**
↓
**ENERGY**
↓
**COST**

and determine where performance is lost and what should be changed.

---

# Final Engineering Test

By July 2027 I should be able to receive an unfamiliar accelerated-computing workload and independently:

- [ ] Establish a reproducible baseline
- [ ] Characterize the algorithm
- [ ] Identify relevant hardware characteristics
- [ ] Profile execution
- [ ] Determine the dominant bottleneck
- [ ] Explain the bottleneck mechanistically
- [ ] Select an appropriate optimization strategy
- [ ] Implement or prototype the change
- [ ] Re-measure performance
- [ ] Validate correctness
- [ ] Evaluate portability
- [ ] Evaluate scaling
- [ ] Estimate infrastructure implications
- [ ] Estimate economic implications
- [ ] Communicate the result clearly

If these can be demonstrated with reproducible evidence, the ACE objective has been achieved.

---

# Target Competency Profile — July 2027

| Domain | Target Level |
|---|---:|
| Computer Architecture | 3 |
| Parallel Computing | 3 |
| HPC | 3 |
| CUDA Programming | 3+ |
| GPU Performance Engineering | **4** |
| NVIDIA Ecosystem | 3 |
| AMD ROCm / HIP | 2–3 |
| TPU / JAX | 2–3 |
| Compiler Systems | 3 |
| Distributed Accelerators | 3 |
| ML Systems | 3 |
| Infrastructure Performance Economics | **4** |

## Overall target

**Integrated Accelerated Computing Engineering: Level 4**

The specialization is not merely CUDA.

It is the ability to reason across heterogeneous accelerated systems and translate low-level performance into system-level and economic outcomes.
