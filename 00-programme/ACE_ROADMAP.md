# Accelerated Computing Engineer Roadmap

**Programme:** Accelerated Computing Engineer (ACE)  
**Target completion:** July 2027  
**Primary objective:** Develop demonstrable competence across accelerated computing, GPU performance engineering, HPC, heterogeneous accelerators, compiler systems, distributed compute, and AI infrastructure efficiency.

---

## Programme Principle

Course completion is not the primary measure of progress.

The programme is complete only when:

1. The core curriculum has been completed.
2. The required engineering artefacts exist.
3. All 12 competency evidence gates have been passed.
4. A cross-accelerator capstone demonstrates practical competence.

The operating loop is:

**LEARN → BUILD → PROFILE / MEASURE → EXPLAIN → IMPROVE → COMMIT**

---

# Phase 1 — Computer Architecture

**Target:** August–September 2026  
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

**Target:** September–October 2026  
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

**Target:** October 2026  
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

**Target:** October–November 2026  
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

**Target:** November–December 2026  
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

**Target:** December 2026–January 2027  
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

**Target:** January 2027  
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

**Target:** January–February 2027  
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

**Target:** February–March 2027  
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

**Target:** March 2027  
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

**Target:** April–May 2027  
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

**Target:** May–July 2027  
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

By July 2027 the goal is to be able to defend the title:

## Accelerated Computing & AI Infrastructure Efficiency Engineer

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
