# ACE Today

**Last recorded learning-session date:** 16 September 2026
**Last recorded learning session:** ACE-2026-09-16-A
**Schedule updated:** 23 September 2026
**Foundation Sprint 0 (replanned):** 7 October–30 November 2026  
**Formal ACE core start:** 1 December 2026  
**Programme layer:** Accelerated Computing Engineering
**Active technical phase:** Phase 1 — Computer Architecture
**Current course:** Princeton — Computer Architecture
**Current evidence position:** Gate 1 — PASSED
**Sprint status:** ACTIVE
**Target completion:** 31 October 2027

---

# Schedule Control

The schedule was revised on 23 September 2026 due to unforeseen circumstances. The [locked baseline](ACE_LOCKED_BASELINE.md#schedule-lock) governs the dates. The formal core runs from 1 December 2026 through 31 October 2027, with integrated capstone work and evidence closure in September–October 2027. Course hours, order, prerequisites and evidence requirements remain unchanged. Target windows permit interleaving only after prerequisites pass; unfinished work moves later rather than being compressed.

Earlier architecture study and the recorded Gate 1 pass remain credited. ACTIVE identifies the unfinished technical focus, not an assertion that the formal core has begun. Remaining architecture work is scheduled for December 2026; Foundation Sprint 0 takes priority before core entry.

No new learning session or evidence completion is implied by this schedule update. The objective and completed work below describe the last recorded session; the next core learning session follows the revised December window.

# Last Recorded Session Objective

Consolidate the completed memory-locality evidence gate, synchronize the programme records and resume the remaining Computer Architecture learning and diagnostic work.

---

# Completed Evidence

- [x] Preregistered the memory-locality experiment.
- [x] Implemented and tested the benchmark.
- [x] Completed the smoke-validation run.
- [x] Completed the full 468-observation run.
- [x] Recorded zero checksum failures.
- [x] Supported H1 at all three registered decision sizes.
- [x] Supported H3 at all three registered decision sizes.
- [x] Completed the CPU-to-GPU transfer assessment.
- [x] Completed the final Gate 1 synthesis.
- [x] Committed and published the evidence as `f97cdc8`.
- [x] Adjudicated Evidence Gate 1 as `PASS`.

---

# Intelligence Decision

The recent vLLM and Kueue findings strengthen the future ACE experimental methodology.

Future serving and scheduling evidence should test:

1. request conservation;
2. scheduling progress and fairness;
3. semantic conservation;
4. resource-accounting conservation;
5. runtime and backend provenance;
6. performance-regression invariants.

These are research-backlog additions.

They do not authorize:

- a vLLM installation now;
- a Kueue installation now;
- an immediate CUDA toolchain change;
- an Atlas expansion;
- an interruption to Phase 1.

---

# Current Engineering Position

## Evidence Gate 1

**Status:** PASSED

The evidence demonstrates:

- controlled sequential and randomized memory-access measurement;
- working-set scaling;
- repeatable timing;
- correctness validation;
- locality and dependency analysis;
- latency-versus-throughput interpretation;
- bounded CPU-to-GPU transfer;
- explicit treatment of threats and limitations.

## Computer Architecture Sprint

**Status:** ACTIVE

Passing Gate 1 does not complete the sprint.

Remaining requirements include:

- [ ] Complete the remaining Princeton learning material.
- [ ] Complete and organize architecture notes.
- [ ] Review latency, throughput, branch prediction, out-of-order execution and SIMD.
- [ ] Complete the sprint-level synthesis.
- [ ] Pass the final diagnostic quiz without notes.
- [ ] Reassess Computer Architecture competency.
- [ ] Update the sprint status only after every exit criterion passes.

---

# Current Study Method

For every important concept:

**CONCEPT → MECHANISM → HARDWARE CONSEQUENCE → PERFORMANCE CONSEQUENCE → EXPERIMENT → INTERPRETATION**

Predict the outcome before checking the explanation.

Definitions alone do not demonstrate competence. Explain the mechanism and identify an experiment that could falsify the explanation.

---

# Next Core Learning Session — December 2026

Begin with a diagnostic review of:

1. latency versus throughput;
2. branch prediction and misprediction cost;
3. out-of-order execution and dependency limits;
4. SIMD versus scalar execution;
5. CPU and GPU memory-hierarchy relationships.

Then return to the next unfinished Princeton course unit.

---

# End-of-Session Rule

Do not mark the Computer Architecture sprint complete until the remaining learning, notes, sprint synthesis, diagnostic assessment, competency reassessment and Git evidence requirements pass.

**LEARN → BUILD → MEASURE → EXPLAIN → IMPROVE → COMMIT → PROVE**
