# Figure redesign review — 2026-10-08

**Scope:** Proposed revisions to the main-figure design in `wangyu-sd/MS-paper`. These notes do not report newly completed experimental results and do not authorize changing the model or running confirmatory tests with interim checkpoints.

## Editorial decision requested

**Should the Nature manuscript lead with discovery and characterization of numerous previously unrecognized metabolite families, with ORBIT-MS as the enabling analytical approach?**

If yes, the figure sequence must change. The currently checked-in five-figure layout was written for an earlier WGV-first story. The proposed six-figure order is:

| Figure | Existing paper plan | Proposed scientific job |
|---|---|---|
| 1 | Full WGV concept, World mechanics, reranking, dark output | Show the newly recovered families immediately: scale, structural support, independent recurrence and representative chemistry |
| 2 | Event language, reaction DAG and Free/Guided/Inverse mechanics | Test how families relate to previously characterized metabolites and whether repeated structural differences are real |
| 3 | Dark structural-entity census | Establish structural reliability and ambiguity quantitatively on known-structure data |
| 4 | Biological source labels on a chemistry map | Establish biological distribution and cross-cohort reproducibility while controlling platform/study confounding |
| 5 | Feature-versus-family biological value + case + standards | Evaluate biological perturbation dependence and whether family-level analysis improves interpretation |
| 6 | No main-text figure | Independent chemical confirmation of selected family discoveries, including successes, failures and one integrative biological finding |

This prioritizes a coherent field-level discovery: **many previously unrecognized families**. It does not predeclare that they exist in the desired numbers, have new-to-science structures, or exhibit biological function.

## Changes that matter most

### A. Move discoveries into the first two main figures

Current old Fig. 1 mixes three incompatible jobs: architecture, quality of model inference and repository-scale dark-metabolome results. The reader's first impression is a model framework.

New Fig. 1: **What did we discover?** Show a large family landscape with independent recurrence and clearly bounded chemical structure statements. Small data/QC and calibration panels establish that the result is not an arbitrary set of generated structures.

New Fig. 2: **What chemistry did we discover?** Show chemically interpretable relationships from real structures to known metabolites, realistic novelty distributions and appropriate chemical-prior-matched controls. This is not merely another embedding or a manually arranged network.

### B. Move the scientific reliability test into Fig. 3

The old Fig. 2 is mainly mechanics plus benchmark. The newly proposed Fig. 3 instead measures how much MS/MS can reduce plausible structure sets, how often the true structure survives, and where formula/proposal/ranking limitations occur.

This addresses the strongest objection to Figs. 1–2: generated structures are hypotheses. Do not call uncalibrated structural predictions chemical discoveries.

Recommended statistical panels: candidate-count 2D density, hard-isomer distributions, correct-vs-shuffled paired effects, evidence ablations, reliability points with confidence intervals, whole-denominator failure flow and subgroup composition. Keep benchmark/SOTA in one compact table or Extended Data rather than taking over the main figure.

### C. Separate biological distribution, intervention evidence and chemical confirmation

The old Figs. 4–5 attempt to demonstrate source dependence, phenotype association, feature-vs-family gains and standard confirmation in two very crowded figures.

New Fig. 4: where families occur; robust cohort structure and technical-confound controls.

New Fig. 5: whether controlled comparisons (germ-free, antibiotics, diet and other verified perturbations) lead to reproducible responses; whether molecular families improve an analysis using the same samples over anonymous spectral features.

New Fig. 6: independent chemistry and a small number of detailed findings, keeping failed/unresolved anchors visible.

### D. Stronger novelty and circularity protections

Do not confuse:
- no library match;
- structurally unrecognized family;
- previously unreported compound structure.

A new-family assertion requires a frozen recognition/reference audit and molecularly meaningful family definition. Family-scale counts must not come from raw spectral feature totals or blindly from predicted Top-1 SMILES.

If the generator retrieves/edits known structures as seeds, near-known enrichment can be a **model-prior artefact**. Compare the real inferred families to matched predictions drawn through the same prior/search process, plus formula/size/source-matched controls. Otherwise Fig. 2's organizing claim is circular.

Transformations in a molecular graph are *structural differences*, not proof of biosynthetic reactions or enzymes.

### E. Stronger independence and historical validation rules

Discovery family construction must be chemically defined and frozen before external replication or biological-label analysis. Count independent studies and biological samples rather than repeated spectra, collision energies or deposits.

Historical T0/T1 evaluation is prospective-style only if all relevant model information at T0 is also sealed (training molecules, simulated spectra, pretraining/retrieval databases). Freezing the reference library alone while retaining a modern model does not create legitimate future prediction.

### F. Do not conflate model progress with confirmed manuscript results

The paper's `internal/NATURE_RESULTS_EVIDENCE_LEDGER_20261006.md` records valuable **development-stage** results on formula recovery, structural proposal failures and fixed-candidate World evidence. Those remain valid with their explicitly stated boundaries.

The definitive final fingerprint-free Generator/system model remains dependent on ongoing model work (PR91 at the time this plan was prepared). This redesign should not paste historical G90/G_BASE, World, PubChem or TRAIN figures into the new discovery panels as if they were final results.

## Critical experimental dependencies

**Priority 1: prove credible structural inference**
- final frozen model/identical configuration for a confirmatory readout;
- molecule-disjoint structural-resolving calibration with honest GT containment;
- native proposal failure decomposition and matched-spectrum vs shuffled-spectrum controls.

**Priority 2: demonstrate discovered families**
- public-source provenance and frozen library search;
- real structural-family definitions on reportable spectra;
- independent replication with immutable family identities;
- literature/reference novelty audit and explicit uncertainty.

**Priority 3: substantiate chemical relationships**
- graph-level edits on resolvable structures;
- matched-prior nulls (especially seed-bias controls);
- cross-class recurrence and independent reference support.

**Priority 4: biology and orthogonal confirmation**
- study-level verified metadata with usable within-study contrasts;
- cross-cohort reproducibility before biological source claims;
- preregistered standard/external-anchor selection, transparent positive and negative outcomes;
- functional interpretations only when independently tested.

A strong positive result in Priority 1 does not substitute for Priorities 2–4 if the target is a discovery-led Nature submission.

## What NOT to change in this PR

- Do not update `main.tex` numerical claims or manuscript section titles yet.
- Do not edit Supplementary Information to match speculative new figures.
- Do not alter `internal/NATURE_RESULTS_EVIDENCE_LEDGER_20261006.md` without new sourced data.
- Do not overwrite the PR90/PR91 development workflow or open official sealed evaluation sets.
- Do not fabricate molecular structures, new-family counts, independent-study totals or empirical statistical curves to fill the figure design.
- Do not insert large decorative architecture diagrams, full-figure headings, colorful containers, drop shadows or summary slogans into artwork.

## Proposed next editorial checkpoint

Review and approve this six-figure sequence first. Once approved, a second paper PR should align the abstract/Introduction, Results order, all figure macros/legends, the claim–evidence matrix, and Supplementary experiment numbering **in one coordinated change**. Implement each proposed figure only from real result tables, and mark missing experiments as planned rather than silently reusing inapplicable historical results.

## References inside these repositories

- `internal/FIGURE_PLAN.md` — detailed new panels and plot/analysis contracts.
- `internal/archive/FIGURE_PLAN_WGV_FIRST_20261006.md` — exactly the prior figure plan.
- `internal/NATURE_RESULTS_EVIDENCE_LEDGER_20261006.md` — existing measured results and boundaries.
- `internal/CLAIM_EVIDENCE_MATRIX.md` — existing old-figure claims, to be re-mapped if the redesign is approved.
- `internal/EXPERIMENT_EXECUTION_PLAN.md` — old WGV-first experiment logic, to be re-mapped later.
- `main.tex` / `supplementary/Supplementary_Information.tex` — unchanged in this design-only PR.
