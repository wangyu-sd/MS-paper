# MS-paper — ORBIT-MS

Nature-oriented manuscript workspace for molecular structure elucidation and discovery of previously unrecognized metabolite families in public tandem mass spectra.

## Manuscript title

**Accurate molecular structure elucidation from tandem mass spectra with ORBIT-MS**

The same title is already installed in default-branch main.tex and Supplementary Information. The modifier "Accurate" remains conditional on complete held-out structural benchmarks and appropriate independent evidence. ORBIT-MS is the name of the full model; World (W), Verifier (V) and Generator (G) are internal components, not separate model names.

## Scientific proposition: Nature discovery first

**The paper is not a World architecture showcase followed by downstream applications.** The proposed contribution is to infer chemically defensible relationships among reference-unmatched metabolomic spectra, discover previously unrecognized molecular families, characterize their chemical relationships, examine their biological distribution, and independently confirm selected structures.

The method enables that task but cannot manufacture its outcome. Unmatched MS2 scans, source-independent spectral-similarity communities, structurally supported molecular families and new-to-science chemical structures are **different analysis units and evidence levels**. Do not turn one into another without external chemistry or calibrated structural inference.

The six Nature main figures were designed in manuscript PR #2 and restored as the governing plan on PR #7; **do not use the erroneous model-first ordering temporarily introduced in PR #7**. The source of truth is [internal/FIGURE_PLAN.md](internal/FIGURE_PLAN.md), with explicit panel/subfigure-level statistics and plot geometry.

| Main figure | Central scientific question | Dominant visual |
| --- | --- | --- |
| **Fig. 1 — Previously unrecognized molecular families** | What previously unseen family relationships can the public unannotated MS/MS record reveal? | **1c** family-level novelty-distance × independent-study recurrence landscape |
| **Fig. 2 — Molecular relationships to known chemistry** | What real chemical relationships are shared with characterized metabolites? | **2a** RDKit structure-based chemical relationship graph |
| **Fig. 3 — Structural evidence and reliability** | How much chemical structure does each measured spectrum truly support? | Full-population candidate reduction, hard decoy/controls and risk–coverage; ORBIT-MS model assessment |
| **Fig. 4 — Biological distribution** | Where do supported molecular families occur across real independent biological cohorts? | **4b** family-by-sample-context adjusted effect map |
| **Fig. 5 — Controlled perturbations** | Which families respond reproducibly to microbiota, diet and other interventions? | **5c** family-by-intervention effects with confidence intervals |
| **Fig. 6 — Independent chemical validation** | Which proposed structure and family-level findings survive independent experimental checks? | Real spectra/standards, complete successes and failures, confirmed family chemistry |

This is **not** a future-positive-results guarantee. Figures 1c, 2a, 4b, 5c and 6b/f cannot become real numerical figures until structure support, source and biological controls, and independent validation are available. Pending panels in LaTeX remain unboxed text-only design specifications, never made-up structures, spectra or plotted metrics.

### ORBIT-MS model placement

Fig. 1b may contain a small, accurately bounded ORBIT-MS inference inset, without displacing the dominant discovery result. Detailed G/W/V architecture, conditioning firewalls, benchmark comparisons, generator-online versus terminal verifier ablation and empirical structural calibration belong in **Fig. 3 and Extended Data**, with reproducible Methods. A W fragment candidate prior is not a fully learned gas-phase reaction network; V posterior fragment evidence is not experimentally confirmed structure-specific reaction pathways. Unverified self-distillation must not appear as achieved performance.

## Main figure file contract

main.tex loads a verified PDF if present and otherwise renders its labelled design specification:

| Figure | Asset |
| --- | --- |
| 1 | figures/fig1_discovered_families.pdf |
| 2 | figures/fig2_chemical_relationships.pdf |
| 3 | figures/fig3_structure_reliability.pdf |
| 4 | figures/fig4_biological_distribution.pdf |
| 5 | figures/fig5_perturbation_effects.pdf |
| 6 | figures/fig6_chemical_validation.pdf |

For actual plot assets, use frozen data/code provenance, low-saturation scientific palette, correctly scaled real RDKit molecule vectors, experimentally measured MS/MS, statistical controls, case denominators and study independence. Main figures should not show artificial reaction schemes, invented spectra or optimistic simulations.

## What the current evidence supports

1. **MassSpecGym:** 11 supplementary result tables S2–S12 report source-audited, percentage-formatted **TRAIN-derived 8,401-case development** metrics. Their conditional fragment W/V numbers and historical graph-generation/fixed-pool retrieval are *not* completed official TEST performance of an integrated ORBIT-MS model.
2. **Public resource:** orbit-ms PR94's model-independent UC/IBD200/VEO-IBD accessible-source corpus has 348 expected / 272 verified / 76 unavailable acquisition files, with 613,331 reference-unmatched eligible measured MS2. Its 2,255 recurrent **spectral** communities (98 across three studies) are not identified molecules. A conditional three-study topology null yielded **p=0.91 (no enrichment)**. PR94's pan-repository study/file/scan inventory is separate and not a completed global structural-discovery denominator.
3. **Final integrated G/W/V:** orbit-ms PR93 contains full training activity and an official 17,556-case V4 TEST submission, but submitted jobs and TRAIN W improvements do not establish final verified official system accuracy. End-to-end structure recovery and independent calibration remain separately sourced.
4. **Chemistry, biology and standards:** target Nature structural-family, chemical relationship, independent-context, controlled-intervention and orthogonal chemical-confirmation claims require actual completed experiments. Negative findings must remain available.

For every reported metric, retain a declared full eligible denominator, independent unit (molecular connectivity group / study / biological sample), method, source snapshot, result receipts and uncertainty or failure counts.

## Editing and PR coordination

- Manuscript text, six main-figure macros, caption slots and scientific references: **main.tex**.
- Detailed Nature figure layout and per-panel data/controls: **internal/FIGURE_PLAN.md**.
- Promised versus completed scientific evidence: **internal/CLAIM_EVIDENCE_MATRIX.md**, **internal/RESULTS_PLACEHOLDERS.md**.
- Full-population experiment dependencies: **internal/EXPERIMENT_EXECUTION_PLAN.md**.
- Supplementary Information: **supplementary/Supplementary_Information.tex**; original 11 MassSpecGym development tables remain **supplementary/MassSpecGym_Development_Results.tex**.
- PR #2 is the discovery-first design authority; PR #7 is the manuscript implementation being realigned; PR #3's V2 Methods are not automatically the final current model. Earlier five-figure/World-first and temporarily model-first plans are retained only in Git history and historical archives.

## Overleaf

For the main manuscript, set root **main.tex** as the Main document. For the full separate supplement choose **supplementary/Supplementary_Information.tex**. To compile the 11 auditable result tables S2–S12 separately choose root **massspecgym_tables_preview.tex**, not the input-only table fragment.

The **article title** is already live in default-branch main. The **corrected six-figure Results and placeholders** are on PR #7 until that branch is merged. To preview them before merge, compile the PR #7 branch in a separate clone or merge after reviewing; changing the figure plan on a draft PR does not affect Overleaf's main branch.
