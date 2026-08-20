# Figure Plan

The main text uses **five** primary figures. Each figure must establish one scientific proposition before showing implementation detail. Agent architecture, detailed CoT tests and low-level protocol diagnostics belong in Extended Data or Supplementary Information.

The visual story should read as a scientific progression even without the manuscript text:

`better hypotheses → evidence bottleneck → discriminative fragments → experimental evidence → adaptive evidence → testable dark-spectrum hypotheses`.

## Figure 1 — Better molecular hypotheses create an evidence bottleneck

**Message:** advances in molecular hypothesis generation move structure elucidation from a generation-limited to an evidence-limited regime.

This figure must look like a field-level phenomenon, not a METEOR benchmark.

- **a** Conceptual regime shift: easy/implausible alternatives in a generation-limited regime versus close same-formula alternatives in an evidence-limited regime.
- **b** Candidate difficulty across at least two independent candidate sources plus matched database candidates: MCES, Morgan Tanimoto, same-formula and scaffold relation.
- **c** Multiple frozen evidence systems evaluated on the same difficulty strata: exact mass, forward-spectrum similarity, external fragmentation-aware comparator(s), initial pLSE.
- **d** Molecule-group candidate fidelity versus separability after matching pool size/formula/mass constraints.
- **e** Representative spectrum where peaks that exclude an early decoy become shared among later alternatives.

**Critical control:** do not infer the phenomenon from arbitrarily selecting harder negatives. Candidate-set size and precursor constraints must be matched.

**Visual priority:** panel a should be immediately understandable to a non-specialist editor. Avoid leading with a heatmap or benchmark table.

## Figure 2 — Discriminative fragments resolve close molecular alternatives

**Message:** the structural information in a spectrum is concentrated in fragments that distinguish competing hypotheses, not necessarily in the most intense or most broadly explained peaks.

This is the chemical centre of the manuscript.

- **a** Conceptual distinction: candidate support versus competitor-relative structural specificity, linked to one atom-traceable trajectory.
- **b** Comparator panel under identical hard candidate pools: exact mass, opportunity-normalized matching, forward-spectrum similarity, CFM-ID/SIRIUS-derived or other executable fragmentation-aware score, pLSE.
- **c** Same-formula and near-isomer GT rank / pairwise win / false-strong distributions.
- **d** Mechanistic ablation ladder: isolated peak coverage → candidate-relative specificity → reaction-centre eligibility → atom/charge/H accounting → full trajectory authority.
- **e–g** Three chemically distinct case studies with large structures, spectra, atom lineage, bond changes and exact m/z/ppm.
- **h** Fraction of discriminative margin captured versus fraction of total observed/explained intensity.

**Critical claim:** broad peak coverage is neither necessary nor sufficient for structural discrimination.

**Visual priority:** structures and decisive peaks should dominate the figure; equations and architecture should not.

## Figure 3 — Experimental spectra distinguish evidence from chemical plausibility

**Message:** a chemically plausible explanation is not automatically experimental evidence; useful evidence is the part of the observation that changes the relative support of competing structures.

- **a** Matched structure-only and spectrum-conditioned views of the same chemical fragmentation prior. Keep the internal labels Chemical-World/Spectral-Reality out of the main visual if possible.
- **b** Correct / no-spectrum / mass-adduct-matched shuffled-spectrum controls.
- **c** Spectral lift and identity lift for molecular ranking and discriminative fragmentation evidence.
- **d** Evidence-authority decomposition: spectrum-specific, shared, unsupported, beyond trace authority.
- **e** One candidate set where chemical plausibility is similar across alternatives but the true spectrum changes the supported hypothesis.

**Move out of main figure:** parent/pilot × normal/no-CoT/shuffled-CoT six-arm experiment → Extended Data Figure 6.

## Figure 4 — Evidence must adapt as molecular hypotheses become harder

**Message:** the evidence needed to resolve a spectrum changes with the hypothesis space; adaptation restores discrimination and transfers beyond the candidate generator that exposed the failure.

- **a** Initial evidence loses discrimination on later/harder hypotheses, followed by recovery with adapted evidence.
- **b** Factorial endpoint design: `(H0,E0)`, `(HT,E0)`, `(H0,ET)`, `(HT,ET)` and interaction effect `Δ_int`.
- **c** Gated adaptation versus fixed-side and ungated/blind alternation controls.
- **d** Post-freeze cross-generation challenge–recovery matrix `A_ij`.
- **e** External-generator/retrieval transfer: initial versus adapted pLSE.
- **f** Generator recall versus conditional discrimination versus end-to-end resolution.
- **g** Calibrated/risk-controlled structural candidate sets: empirical coverage, set size, resolvable and unresolved examples.

**Critical control:** the cross-generation matrix is descriptive. The factorial endpoint experiment carries the causal claim.

**Visual priority:** panel a should communicate the scientific result before the reader encounters the ORBIT protocol.

## Figure 5 — From dark spectra to testable molecular hypotheses

**Message:** the practical output of evidence-bounded structure elucidation is not a forced SMILES but a molecular hypothesis at the resolution justified by the experiment, with explicit alternatives and evidence.

- **a** Independent mouse cohort with blinded anchor and dark-spectrum branches.
- **b** Blinded anchor: generator recall, conditional discrimination and end-to-end resolution with applicable baselines.
- **c** Dark-spectrum candidate-space contraction: formula-compatible population → evidence-supported structural set.
- **d** Recurrence/reproducibility across independent mouse samples.
- **e** Deep resolved/strongly narrowed case with atom-traceable evidence and orthogonal validation.
- **f** Deep unresolved isomer case showing that non-resolution is a scientifically valid outcome.
- **g** Biological association only if predefined, replicated and independently supported.

**Narrative requirement:** the resolved and unresolved cases should be visually parallel so that both outcomes appear as consequences of the same evidence principle.

**Nature-main-track extension:** if prospective MSn/CE experiment selection is completed, it can become a new final figure showing `ambiguity → missing evidence → new measurement → candidate contraction`.

## Extended Data

1. Dataset composition, split and pretraining leakage audit.
2. Candidate-difficulty matching and evidence-bottleneck sensitivity analyses.
3. Reaction-basis coverage and search truncation diagnostics.
4. Complete hard-decoy benchmark across all fragmentation/spectrum comparators.
5. Full fragmentation-evidence ablations and evidence-authority decomposition.
6. Parent/pilot × normal/no-reasoning/shuffled-reasoning six-arm causal analysis.
7. Reciprocal-run replicates, fixed-side/ungated controls and full cross-generation matrix.
8. External transfer, generator recall, conditional discrimination, conformal/risk-controlled candidate sets and calibration.
9. Mouse QC, library overlap, blinded-anchor evaluation and recurrence.
10. Complete mouse evidence dossiers and orthogonal validation.

## Visual principles

- Use a white background, sparse panels and large molecular structures/spectra.
- Avoid dense multi-agent diagrams and decorative AI icons.
- Reuse one or two anchor spectra across Figures 1–3 so the scientific logic is visually continuous.
- Encode scientific roles consistently: observed spectrum, candidate hypothesis, discriminative evidence and unresolved alternatives.
- Molecular structures, atom labels and reaction arrows must be interpretable at journal print size.
- Do not use a heatmap, architecture diagram or training curve as the visual centre of the paper; the key panels should show chemistry, structural alternatives and the information supplied by the experiment.
- Figure titles and panel headings should describe scientific findings, not implementation modules.