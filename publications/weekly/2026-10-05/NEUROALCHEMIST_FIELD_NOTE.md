# The machine must account for its work
*The next chapter of The NeuroAlchemist follows a decision all the way into the infrastructure that executes it.*

The first chart in this chapter comes from a CPU memory experiment. It contains no prediction about superintelligence. It asks a smaller question: what happens when the same mathematical work reaches memory in a different order?

On 11 September 2026, our ACE memory-locality experiment recorded 468 observations across 13 nominal data sizes, four access conditions and nine observations per condition and size. The checksums passed. That establishes the benchmark's recorded output checks; it does not establish that every possible explanation of the timing curves is correct.

At the three largest registered sizes, random indexed traversal was slower than sequential indexed traversal by ratios of 5.207, 6.273 and 8.107. Both conditions used independent indexed accesses. Their comparison concerns access order and locality. The pointer-chase condition added a result-dependent chain, making future addresses wait on preceding loads.

The calculation did not become more sophisticated. The route through the machine became more expensive.

## Follow the decision into the machinery

This is where the wider programme begins.

NSDM developed independently around evidence and decision boundaries: when can a system support an answer, recognise contradiction, preserve UNKNOWN, abstain or act? Behavioural science asks a related human question: what do our measures actually tell us about judgement, intention and outcomes?

ACE extends the inquiry into execution. A decision may pass its evidence checks and still travel through an implementation that changes its numerical result, loses its request identity, miscounts its resources or acts under the wrong authority.

Those are concrete questions. Each needs a workload, a reference, a trace and a way to fail.

The framework we are developing therefore checks four proposed invariants: request and lifecycle conservation; semantic conservation; resource accounting; and authority. Their specifications are research commitments. They are not four completed experiments or a claim that we have solved AI safety.

## A scientific programme needs room for disappointment

The new roadmap pairs engineering work with a weekly public record: a website evidence entry, a NeuroAlchemist field note and a visual that makes the question inspectable.

Some weeks will contain measured comparisons. Others will contain a preregistration, a failed hypothesis, a platform limitation or a correction. Experiments can take several weeks. The publishing calendar will not be allowed to manufacture a result.

The graph accompanying this note uses the already committed September experiment. Its shaded bands show interquartile ranges, not confidence intervals. The sizes describe nominal data storage; indexed conditions also use index storage. The curve cannot identify an exact cache boundary, and pointer-chase timing is not a universal DRAM-latency number.

That specificity matters more than a dramatic interpretation.

GPU, TPU, cloud and data-centre comparisons will enter when their prerequisites and platform access are established. More capable AI, including AGI and superintelligence scenarios, motivates future questions about autonomy and control. It does not certify answers we have yet to obtain.

The work starts closer to the ground: keep the papers inspectable, preserve the null findings, record the toolchain and follow the execution.

A machine's speed becomes useful evidence when we can also account for what it did.

## Sources and evidence

- [Committed Gate 1 evidence and synthesis](https://github.com/Rajesh0311/accelerated-computing-engineering/tree/f97cdc8/01-computer-architecture/evidence-gate-01-memory-locality).
- [Original preregistration and implementation record](https://github.com/Rajesh0311/accelerated-computing-engineering/tree/7421ee7/01-computer-architecture/evidence-gate-01-memory-locality).
- [Scientific programme](../../../00-programme/ACE_SCIENTIFIC_PROGRAMME.md) and [weekly evidence calendar](../../../00-programme/ACE_WEEKLY_EVIDENCE_CALENDAR.md).
- [Reproducible graph](memory-locality.svg), [summary data](locality-summary.csv) and [plotting script](plot_memory_locality.py).

## Editorial disclosure

This field note was developed with AI assistance under human direction. Its experimental claims trace to committed records; interpretations remain open to correction. This is a publication-ready draft awaiting Rajesh Singh's final editorial sign-off and Substack publication.

## Publication record

**State:** DRAFT — NOT PUBLISHED ON SUBSTACK
**Experiment date:** 11 September 2026
**Draft date:** 8 October 2026
**Article URL:** PENDING
**Visual placement:** insert `memory-locality.svg` after the paragraph ending “The calculation did not become more sophisticated. The route through the machine became more expensive.”
**Alt text:** Two measured plots show median CPU access times and random-to-sequential indexed ratios across increasing nominal data sizes. Ratios at the three registered largest sizes exceed the H1 threshold; interquartile bands describe dispersion rather than confidence.
