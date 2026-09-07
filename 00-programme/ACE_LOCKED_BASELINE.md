# ACE Locked Baseline

**Status:** LOCKED  
**Lock date:** 7 September 2026  
**Programme:** Accelerated Compute Platform & AI Infrastructure Efficiency Engineer  
**Foundation Sprint 0:** 7 September 2026 – 31 October 2026  
**Formal ACE core start:** 1 November 2026  
**Target completion:** 30 September 2027  

---

# Purpose

This file locks the Accelerated Computer Engineer Programme baseline.

The programme is no longer an open-ended course-discovery exercise. The existing `ACE_ATLAS.md`, together with the decisions recorded here, is the approved technical curriculum.

The objective is not to accumulate courses or certificates. The objective is defensible engineering competence demonstrated through reproducible evidence.

---

# Target Professional Identity

## Accelerated Compute Platform & AI Infrastructure Efficiency Engineer

The required reasoning chain is:

**MATHEMATICAL / NUMERICAL PROBLEM → ALGORITHM → MODEL → COMPILER → KERNEL → ACCELERATOR → HOST → MEMORY → INTERCONNECT / NETWORK → SCHEDULER → PLATFORM → TELEMETRY → PERFORMANCE → CAPACITY → COST → BUSINESS OUTCOME**

ACE must build competence across numerical computing, computer architecture, parallel computing, HPC, CUDA/GPU performance, heterogeneous accelerators, compiler systems, distributed compute, ML systems, Linux/networking/container/Kubernetes platform engineering, observability/SRE, inference serving, security, infrastructure automation and compute economics.

---

# Foundation Sprint 0 — Mandatory Prerequisite Layer

Foundation Sprint 0 runs from 7 September through 31 October 2026.

Its purpose is to remove avoidable weakness before the accelerated-computing core begins.

## Mandatory foundation capabilities

1. Python for engineering and automation
2. Git and GitHub
3. Linux command line and systems fundamentals
4. C programming on Linux
5. Modern C++ bridge for CUDA and systems programming
6. GCC / Clang compilation and linking
7. Make / CMake
8. GDB and systems debugging
9. Basic performance tooling including `time` and `perf`
10. Linear algebra
11. Multivariate calculus
12. Probability and statistics
13. Numerical-computing foundations

## Preferred formal foundation credentials

- Python for Everybody — University of Michigan / Coursera — full or accelerated completion according to demonstrated prior competence
- C Programming with Linux Specialization — Dartmouth College + Institut Mines-Télécom / Coursera — full
- Mathematics for Machine Learning Specialization — Imperial College London / Coursera — full
- Probability & Statistics from Mathematics for Machine Learning and Data Science — DeepLearning.AI / Coursera — full or evidence-based selective completion
- Red Hat Linux Fundamentals — full
- One Git/GitHub certificate-bearing course — full

Modern C++, Bash, GCC/Clang, Make/CMake, GDB and `perf` are competence-driven rather than certificate-driven.

## Foundation completion rule

1 November is a **competence gate**, not a certificate gate.

Outstanding formal certificates may be completed after Coursera Plus renewal if the required engineering competence has already been demonstrated.

---

# Locked ACE Academic / Engineering Core

The following curriculum is locked as the approved core sequence. The detailed scope, links, hours and evidence requirements remain in `ACE_ATLAS.md`.

1. Princeton Computer Architecture
2. Stanford CS205A — selected numerical-computing foundations
3. Stanford CS149 — Parallel Computing
4. CU Boulder High-Performance & Parallel Computing
5. CU Boulder Efficient Programming
6. CU Boulder Parallel Computing with MPI
7. NVIDIA CUDA introductory foundation
8. NVIDIA Modern CUDA C++
9. CUDA Programming Guide + ACE laboratories
10. NVIDIA Nsight Systems
11. NVIDIA Nsight Compute
12. CUDA Memory Optimization
13. CUDA Streams / Async / CUDA Graphs
14. PyTorch Custom CUDA Extension
15. Berkeley CS267 — Applications of Parallel Computers
16. AMD AI Academy
17. AMD HIP / ROCm Programming
18. CUDA → HIP Port + ROCm Profiling
19. TPU Architecture + JAX Fundamentals
20. JAX on TPU / Scaling
21. LLVM Compiler Fundamentals
22. Triton Kernel Programming
23. PyTorch Compiler / `torch.compile`
24. NCCL + Distributed GPU Systems
25. Stanford CS336 — Language Modeling from Scratch
26. Stanford CME295 — selected material
27. Full Stack Deep Learning
28. Stanford CS329A — selected self-improving / autonomous performance material
29. Anthropic evaluation / agent-system material — selected
30. Heterogeneous AI Compute Platform Capstone

The detailed Atlas may contain more granular numbered items because selected agent-system resources are separated individually. This lock file defines the curriculum families and their mandatory/selective status; the Atlas defines implementation detail.

---

# Locked Compute Platform Engineering Overlay

The platform overlay is mandatory and interleaved with the accelerated-computing core.

1. CP1 — Linux Systems Engineering
2. CP2 — Networking for Accelerated Compute
3. CP3 — Containers + NVIDIA GPU Runtime
4. CP4 — Kubernetes + GPU Scheduling
5. CP5 — Observability + SRE for Compute
6. CP6 — Inference Serving Engineering
7. CP7 — Infrastructure Automation + Security
8. CP8 — Compute Capacity Engineering + FinOps

Primary technologies are intentionally constrained:

- Scheduling: Kueue first; selective Volcano and Slurm
- Distributed ML: PyTorch DDP and FSDP first
- Serving: vLLM first; TensorRT / TensorRT-LLM and Triton second
- Observability: Prometheus + Grafana + NVIDIA DCGM
- Distributed Python: Ray understanding, not a separate specialization
- Languages: Python, Bash, C/C++, CUDA C++; Go progressively; Rust optional

---

# Formal Credential Pillars

Certificates support the engineering evidence; they do not replace it.

## Coursera / university foundation and HPC credentials

Target complete credentials include:

- Imperial College London — Mathematics for Machine Learning Specialization
- Dartmouth / Institut Mines-Télécom — C Programming with Linux Specialization
- CU Boulder — High-Performance and Parallel Computing Specialization and constituent certificate-bearing courses
- selected Python, Linux, Git and probability/statistics certificates where they add real foundation value

## NVIDIA

Target formal NVIDIA credentials are the strongest relevant certificate-bearing CUDA / accelerated-computing offerings available during the programme, with priority to:

- foundational CUDA C/C++ competency
- Modern CUDA C++
- streams / concurrent execution where certificate-bearing
- multi-GPU CUDA
- multi-node CUDA where practical and available

## AMD

Target formal AMD credentials are:

- selected AMD AI Academy completion certificates
- ROCm Certified Associate when available and accessible
- ROCm Certified Professional if available in time and justified by the programme stage

## Stanford / Berkeley / public university material

Publicly accessible Stanford, Berkeley and similar material is used for academic depth. It is never misrepresented as a university credential when no formal credential has been earned.

The proof from these sources is the implementation, benchmark, profiler trace, technical report and evidence gate.

---

# Evidence Standard — Non-Negotiable

No phase is considered complete merely because videos were watched or assessments were passed.

Every major phase must produce:

1. working implementation
2. reproducible benchmark or experiment
3. profiler / telemetry evidence where applicable
4. correctness validation
5. numerical-error validation where applicable
6. before/after comparison when optimizing
7. written engineering interpretation
8. Git history / commit
9. PASS / FAIL evidence-gate result

The programme retains 16 major evidence gates as defined in the Atlas.

Numerical correctness is cross-cutting and cannot be traded away silently for higher performance.

---

# Final Capstone Standard

The final capstone is the **Heterogeneous AI Compute Platform Capstone**.

It must demonstrate the complete engineering chain from workload formulation through numerical correctness, accelerator selection, compiler/kernel execution, runtime/platform operation, observability, capacity and cost.

Where practical it compares multiple execution paths such as CPU, NVIDIA CUDA, AMD ROCm/HIP, Triton, PyTorch compiler and TPU/JAX.

The capstone must include platform deployment, scheduling, telemetry, performance analysis, numerical/correctness validation, capacity reasoning, economics and an evidence-backed engineering recommendation.

---

# Course Intake Lock

From this date forward, ACE is locked against course sprawl.

A newly discovered course, certification or resource enters only if it satisfies at least one of the following:

- replaces a currently selected resource with something materially stronger;
- closes a genuine capability gap not covered by the locked syllabus;
- is an official certification directly validating a locked ACE competency;
- provides unique evidence capability unavailable elsewhere in the programme.

New resources do **not** automatically add programme hours.

Default decision for interesting but overlapping material is **SKIP**, **OPTIONAL** or **SELECTIVE**, not ADD.

Prestige, novelty, social-media enthusiasm, a free certificate or simple availability are not sufficient reasons to alter the programme.

---

# Schedule Lock

## 7 September – 31 October 2026
Foundation Sprint 0

## 1 November 2026
Formal ACE accelerated-computing core begins

## November 2026 – August 2027
Core accelerated-computing, heterogeneous accelerator, compiler, distributed and ML-systems progression with the compute-platform overlay interleaved

## August – September 2027
Integrated platform work, final evidence closure and heterogeneous capstone

## 30 September 2027
Target programme completion

Depth and evidence take precedence over preserving an obsolete earlier completion date.

---

# Final Rule

**LEARN → BUILD → MEASURE → EXPLAIN → IMPROVE → COMMIT → PROVE**

ACE is complete only when the professional title **Accelerated Compute Platform & AI Infrastructure Efficiency Engineer** is supported by reproducible technical evidence rather than aspiration, course attendance or certificate count.
