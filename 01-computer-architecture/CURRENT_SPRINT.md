# ACE Sprint 01 — Computer Architecture

**Phase:** 1 of 12  
**Status:** ACTIVE  
**Start:** 18 August 2026  
**Target completion:** September 2026  
**Planned effort:** ~40 focused hours  
**Evidence Gate:** CPU / Cache / Memory Behaviour

---

# Primary Course

## Princeton University — Computer Architecture

Official course — FREE FULL COURSE, NO CERTIFICATE:
https://www.coursera.org/learn/comparch

**Access model:** Full Course, No Certificate
**Coursera Plus required:** No
**Cost:** Free
**Credential:** None — ACE evidence replaces certificate value


Instructor:
David Wentzlaff — Princeton University

---

# Why This Sprint Exists

The goal is not to become a CPU designer.

The goal is to understand the machine well enough that later concepts in:

- CUDA
- GPU architecture
- cache behaviour
- memory bandwidth
- SIMD / SIMT
- occupancy
- compiler optimisation
- accelerator design
- HPC

have a physical and architectural meaning.

---

# Sprint Outcomes

By the end of this sprint I should be able to explain:

1. How instructions move through a processor.
2. Why pipelines improve throughput.
3. Why branches can reduce performance.
4. Why caches exist.
5. Why locality matters.
6. Why memory access can dominate computation.
7. Why two implementations of the same algorithm can perform very differently.
8. How instruction-level parallelism works.
9. What superscalar and out-of-order execution achieve.
10. How multicore architecture changes the execution model.
11. How CPU parallelism relates conceptually to later GPU parallelism.

---

# High-Priority Topics

Focus deeply on:

- Instruction execution
- Pipelining
- Data hazards
- Control hazards
- Branch prediction
- Superscalar execution
- Out-of-order execution
- Registers
- Cache hierarchy
- Cache hits and misses
- Temporal locality
- Spatial locality
- Memory latency
- Memory bandwidth
- Multicore processors
- Cache coherence
- Vector/SIMD concepts
- Throughput vs latency

Do not spend disproportionate time on historical architecture details unless they help explain a modern mechanism.

---

# Accelerated-Computing Connections

For every major concept ask:

## CPU concept
What is happening architecturally?

## GPU equivalent
What related problem appears on a GPU?

## Performance consequence
How can the mechanism affect runtime?

Examples:

CPU cache locality
→ GPU coalesced/global/shared-memory behaviour

SIMD
→ SIMT / warps

CPU pipelines
→ GPU execution pipelines

Memory latency
→ latency hiding

Multicore execution
→ massive parallel execution

Cache coherence
→ distributed/shared-state challenges

---

# Evidence Gate 1

## CPU / Cache / Memory Behaviour

Build experiments that demonstrate real architectural effects.

Required:

- [ ] Sequential memory access benchmark
- [ ] Random memory access benchmark
- [ ] Working-set/cache-size experiment
- [ ] Repeatable timing methodology
- [ ] Results captured
- [ ] Results interpreted
- [ ] Architecture mechanism explained
- [ ] Connection to future GPU behaviour documented

---

# Required Repository Outputs

Use:

```text
ace/01-computer-architecture/
│
├── CURRENT_SPRINT.md
├── notes/
├── labs/
├── benchmarks/
└── synthesis.md
By sprint completion there must be:

notes/

Short learning notes only.

labs/

Executable experiments.

benchmarks/

Results and comparison evidence.

synthesis.md

Final 2–4 page sprint synthesis.

Study Method

Every substantial topic follows:

CONCEPT
↓
MECHANISM
↓
HARDWARE CONSEQUENCE
↓
PERFORMANCE CONSEQUENCE
↓
EXPERIMENT
↓
INTERPRETATION

Session Rule

Do not merely watch lectures.

For each serious study session:

Learn one meaningful concept.
Explain the mechanism in my own words.
Connect it to execution/performance.
Build or inspect something when appropriate.
Record evidence.
Commit meaningful progress.
Gemini Notebook Setup

Create a Gemini Notebook named:

ACE — SPRINT 01 — COMPUTER ARCHITECTURE

This is the active study notebook.

Add only sources relevant to this sprint.

Source 1

Princeton Computer Architecture:
https://www.coursera.org/learn/comparch

**Access model:** Full Course, No Certificate
**Coursera Plus required:** No
**Cost:** Free
**Credential:** None — ACE evidence replaces certificate value

Source 2

Princeton official course description:

Source 3

This file:
CURRENT_SPRINT.md

Additional Sources

Add lecture PDFs, notes or official supporting material only as they become relevant.

Do not bulk-upload unrelated ACE material.

Gemini Notebook Tutor Instruction

Use the following as the standing study instruction:

Act as my Accelerated Computing Engineering tutor for this Computer Architecture sprint.

The objective is engineering competence, not course completion.

Ground explanations in the supplied sources whenever possible.

For important concepts, teach using:

CONCEPT
→ MECHANISM
→ HARDWARE CONSEQUENCE
→ PERFORMANCE CONSEQUENCE
→ EXPERIMENT
→ INTERPRETATION

Do not immediately solve exercises for me.

Ask me to predict results first.

Force me to explain mechanisms in my own words.

Correct misconceptions explicitly.

Connect CPU architecture concepts to future GPU, CUDA, HPC and accelerator concepts where technically justified.

Prefer diagnostic questions over definition questions.

Examples:

Why might sequential traversal outperform random traversal even when both touch the same number of array elements?

What architectural mechanism could explain the difference?

What experiment would distinguish between competing explanations?

Periodically revisit concepts I previously answered poorly.

Sprint Completion Test

Before declaring this phase complete I must be able to answer, without notes:

Question 1

Why can two programs performing the same mathematical computation have substantially different execution times?

Question 2

When does cache locality materially affect performance?

Question 3

What is the difference between latency and throughput?

Question 4

Why does branch prediction exist and what happens when prediction fails?

Question 5

What does out-of-order execution achieve?

Question 6

How does SIMD differ conceptually from scalar execution?

Question 7

Why does faster arithmetic not automatically produce a faster computer?

Question 8

What is the relationship between CPU memory hierarchy and GPU memory hierarchy?

Sprint Exit Criteria

The sprint is complete only when:

 Required learning material completed
 Notes exist
 Benchmarks execute reproducibly
 Evidence Gate 1 passed
 synthesis.md completed
 Gemini Notebook final diagnostic quiz passed
 ACE_PROGRESS.md updated
 Competency level reassessed
 Git evidence committed
Expected Competency Change

Start:

Computer Architecture — Level 0/1

Target:

Computer Architecture — Level 3

I should finish this sprint able to use processor architecture to explain observed performance rather than merely define architecture terminology.

