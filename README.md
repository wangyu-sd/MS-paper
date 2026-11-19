# ORBIT-MS manuscript

## Title

**ORBIT-MS: Recursive chemical learning for molecular structure elucidation from tandem mass spectra**

This repository contains the Nature Machine Intelligence manuscript, supplementary results and experiment/figure plans. The scientific contribution combines molecular structure elucidation from tandem spectra with recursive learning that updates reusable chemical knowledge, the molecular generator and the verifier in response to observed failures. A Scientific Improver selects the existing learning interventions and retains their outcomes for later decisions.

## Current manuscript and experiment design

The active manuscript is `main.tex`. The governing experiment plan is [the five-result NMI plan](internal/NMI_CHEMICAL_ELUCIDATION_RESULTS_PLAN_20261112.md). The earlier Nature six-figure outline remains historical context in the repository and git history.

| Result | Main question | Figure asset |
| --- | --- | --- |
| 1. Structurally resolving the reference-unmatched metabolome | How much structural information can be recovered from unassigned experimental spectra? | figures/fig1_dark_structure_landscape.pdf |
| 2. Fragment evidence enables molecular construction and discrimination | How do reusable motifs and measured fragment evidence improve candidate generation and ranking? | figures/fig2_fragment_guided_elucidation.pdf |
| 3. Agent-guided recursive self-improvement expands the recoverable chemical space | Which additional molecular structures become recoverable after targeted learning? | figures/fig3_recursive_recoverable_space.pdf |
| 4. Previously unresolved spectra reveal molecular-family relationships | Which supported graph relationships link unresolved spectra to characterized chemistry? | figures/fig4_molecular_family_relationships.pdf |
| 5. Independent spectral evidence supports molecular hypotheses from the dark metabolome | Which assignments are supported by independently acquired spectra or orthogonal measurements? | figures/fig5_independent_chemical_evidence.pdf |

The paper follows this sequence and retains the existing component experiments, external development evaluations and chemical endpoints. Main figures load the named PDF when supplied; until then, their panel specifications remain visible. Final molecular drawings and spectra are generated from the actual chemical structures and measured data.

## Mechanistic evidence and independent validation

The focused 19 November 2026 manuscript revision replaces broad explanations with traceable tests of chemical-knowledge transfer, paired spectral discrimination, agent intervention selection, and independent structural corroboration. The four expert questions---additional unrequested experiments, original raw materials, concrete analysis tools, and external evidence---are documented in [Expert evidence redesign](internal/EXPERT_EVIDENCE_REDESIGN_20261119.md). This is a research and verification plan, not a claim that the planned experiments are already completed.

## Draft notation

Completed experiments retain their recorded values and evaluation settings. Pending outcomes are written as complete result sentences with **x** for the value or chemical identifier to be filled. These sentences express the expected result direction for the working manuscript. The LaTeX pending macro prints x; [the editorial revision record](internal/EDITORIAL_REVISION_20261118.md) maps its identifiers to their experiment and position in the text. A short note outside the abstract explains the convention in the PDF.

The abstract is one unreferenced paragraph of at most 150 words. Introduction has no heading, followed by Results with five topical subsections, Discussion and Methods. The title is identical in the main manuscript and Supplementary Information.

## Source files

- Main manuscript: main.tex, with main figure definitions, captions and Extended Data legends.
- Typography: orbit-nmi.sty, with optional review mode.
- Scientific references: references.bib.
- Separate supplement: supplementary/Supplementary_Information.tex.
- Retained development tables: supplementary/MassSpecGym_Development_Results.tex and supplementary/ORBIT_WGV_RSI_Results.tex.
- Active experimental design: internal/NMI_CHEMICAL_ELUCIDATION_RESULTS_PLAN_20261112.md.
- Latest editorial changes and pending-result map: internal/EDITORIAL_REVISION_20261118.md.
- Layout and build instructions: NMI_FORMATTING_AND_PRESERVATION.md.

Source development is in [wangyu-sd/orbit-ms](https://github.com/wangyu-sd/orbit-ms): [PR #94](https://github.com/wangyu-sd/orbit-ms/pull/94) for the public spectral resource, [PR #95](https://github.com/wangyu-sd/orbit-ms/pull/95) for WGV development, and [PR #96](https://github.com/wangyu-sd/orbit-ms/pull/96) for the Scientific Improver. The Methods specify evaluation populations, formula access, model states and candidate supply for each experiment.

## Build and Overleaf

Set main.tex as the Overleaf Main document for the manuscript. Choose supplementary/Supplementary_Information.tex for the separate supplement, or massspecgym_tables_preview.tex for the retained development tables alone.

```bash
latexmk -pdf -halt-on-error -interaction=nonstopmode -file-line-error main.tex
```

The reading layout is the default. To enable double spacing and continuous line numbers, insert \orbitreviewtrue immediately before \orbittypeset in main.tex.

Author and affiliation information remains in the manuscript's existing provisional block; its provenance is recorded in [the author metadata note](internal/AUTHOR_METADATA_RECOVERY_20261118.md).

