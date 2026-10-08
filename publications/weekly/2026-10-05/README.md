# ACE-WEEK-2026-10-05 — Scientific programme launch

**Reporting window:** 8–11 October 2026 (partial week)
**State:** TECHNICAL PACKAGE READY; SUBSTACK DRAFT PENDING AUTHOR SIGN-OFF
**New experiment executed:** NO
**Technical proof:** previously committed Gate 1 experiment; new publication artefacts generated from its complete CSV
**Current phase:** Foundation Sprint 0; Gate 1 remains PASSED; architecture sprint ACTIVE

## Website evidence entry

Question: how will MetaForgeX make the journey from decision semantics to accelerated execution scientifically inspectable?

This release locks a scope matrix, 14 reusable protocol families, a dated weekly calendar and a release template. It curates the existing memory-locality experiment as the first measured visual. It does not add a new GPU, TPU, cloud or distributed benchmark.

The graph contains all 13 sizes and four conditions. Medians and inclusive interquartile ranges use nine observations per condition/size. Ratios are ratios of medians. No bootstrap confidence interval or new hypothesis test is implied.

The original Windows CSV hash uses CRLF serialization. Git-normalized LF bytes have a different SHA-256; the plotting script verifies both serializations and leaves the source unchanged. See [visual provenance](visual-provenance.json).

## Artefacts

- [Scientific programme](../../../00-programme/ACE_SCIENTIFIC_PROGRAMME.md)
- [Weekly calendar](../../../00-programme/ACE_WEEKLY_EVIDENCE_CALENDAR.md)
- [Substack draft](NEUROALCHEMIST_FIELD_NOTE.md)
- [Scientific graph SVG](memory-locality.svg) / [PNG](memory-locality.png)
- [Summary CSV](locality-summary.csv)
- [Regeneration script](plot_memory_locality.py)

## Trend adjudication

No new release claim is introduced by this package. September intelligence remains historical motivation for protocol design and is not asserted as current platform support. The weekly Friday task will evaluate fresh primary-source changes against the active question.

## Claim boundary

This graph measures one CPU implementation on its recorded platform. It does not establish exact cache capacities, raw DRAM latency, GPU behaviour, AGI or infrastructure savings. The scientific programme and future protocol families are proposed/specification evidence; Gate 1 remains the existing recorded pass.

## Reproduction

From repository root, use an environment with Python and Matplotlib:

```powershell
python publications/weekly/2026-10-05/plot_memory_locality.py
```

The figure was generated with Matplotlib 3.10.8; the exact version is recorded in the provenance file. Plotting is a publication step, not a new timing run.

## Next decision

Continue Foundation Sprint 0 and improve reproducible engineering fixtures. No early serving, Kubernetes, MPS or Topograph installation. Use a short field note if publication would displace prerequisite work.
