# Figure Plan

The revised main text uses **five** primary figures. Each figure must establish one scientific proposition. Agent architecture, detailed CoT tests and implementation diagnostics belong in Extended Data or Supplementary Information.

## Figure 1 — A cross-model evidence bottleneck

**Message:** increasingly faithful molecular alternatives systematically erode the discriminative power of fixed spectral evidence.

This figure must not be a METEOR-only phenomenon.

- **a** One spectrum with GT, easy alternatives and hard same-formula/near-isomer alternatives.
- **b** Candidate difficulty across at least two independent candidate sources plus matched database candidates: MCES, Morgan Tanimoto, same-formula and scaffold relation.
- **c** Multiple frozen evidence systems evaluated on the same difficulty strata: exact mass, forward-spectrum similarity, external fragmentation-aware comparator(s), initial pLSE.
- **d** Molecule-group candidate fidelity versus separability after matching pool size/formula/mass constraints.
- **e** Representative case where peaks that separate an early decoy become shared among late alternatives.

**Critical control:** do not infer the phenomenon from arbitrarily selecting harder negatives. Candidate-set size and precursor constraints must be matched.

## Figure 2 — Candidate-specific fragmentation evidence

**Message:** fragmentation becomes a useful structural-evidence object when the support is atom-traceable and specific relative to competing molecules.

This is the scientific centre of the manuscript.

- **a** Definition: candidate → legal trajectories → peak support `s_jp` → competitor-relative specificity `d_jp` → candidate score.
- **b** External/standard comparator panel under identical hard candidate pools: exact mass, opportunity-normalized matching, forward-spectrum similarity, CFM-ID/SIRIUS-derived or other executable fragmentation-aware score, pLSE.
- **c** Same-formula and near-isomer GT rank / pairwise win / false-strong distributions.
- **d** Mechanistic ablation ladder: isolated peak coverage → candidate-relative specificity → reaction-centre eligibility → atom/charge/H accounting → full trajectory authority.
- **e–g** Three chemically distinct case studies with large structures, spectra, atom lineage, bond changes and exact m/z/ppm.
- **h** Discriminative margin versus global explained intensity.

**Critical claim:** broad peak coverage is neither necessary nor sufficient for structural discrimination.

## Figure 3 — Experimental spectrum versus chemical prior

**Message:** chemically plausible explanations are not automatically experimental evidence.

- **a** Chemical-World / Spectral-Reality matched views of the same structure prior.
- **b** Correct / no-spectrum / mass-adduct-matched shuffled-spectrum controls.
- **c** Spectral lift and identity lift for METEOR ranking and pLSE candidate-specific evidence.
- **d** Evidence-authority decomposition: spectrum-specific, shared, unsupported, beyond trace authority.
- **e** One candidate set where chemical priors are similar but the true spectrum changes the supported hypothesis.

**Move out of main figure:** parent/pilot × normal/no-CoT/shuffled-CoT six-arm experiment → Extended Data Figure 6.

## Figure 4 — Reciprocal adaptation, transfer and calibrated resolution

**Message:** adapting both sides gives a measurable benefit beyond adapting either side alone, the gain survives external candidate distributions, and uncertainty is represented explicitly.

- **a** Factorial endpoint design: `(H0,E0)`, `(HT,E0)`, `(H0,ET)`, `(HT,ET)`.
- **b** Main held-out endpoint and interaction effect `Δ_int`.
- **c** Reciprocal gated adaptation versus fixed-side and ungated/blind alternation controls.
- **d** Post-freeze cross-generation challenge–recovery matrix `A_ij`.
- **e** External-generator/retrieval transfer: initial versus final pLSE.
- **f** Generator recall versus conditional discrimination versus end-to-end resolution.
- **g** Risk-controlled structural candidate sets: empirical coverage, set size, resolvable and unresolved examples.

**Critical control:** the cross-generation matrix is descriptive. The factorial endpoint experiment carries the causal claim.

## Figure 5 — Independent mouse deployment

**Message:** adaptive fragmentation evidence narrows previously unlabelled biological spectra while preserving the distinction between hypothesis and identification.

- **a** Cohort design with blinded anchor and dark-spectrum branches.
- **b** Blinded anchor: generator recall, conditional discrimination, risk-controlled end-to-end resolution, applicable baselines.
- **c** Dark-spectrum candidate-space contraction: formula-compatible pool → evidence-supported risk-controlled set.
- **d** Recurrence/reproducibility across independent mouse samples.
- **e** Deep resolved/strongly narrowed case with atom-traceable evidence and orthogonal validation.
- **f** Deep unresolved isomer case.
- **g** Biological association only if predefined, replicated and independently supported.

**Nature-main-track extension:** if prospective MSn/CE experiment selection is completed, it can become a new Figure 5 or Figure 6 and move the mouse deployment later.

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
- Encode scientific roles consistently: observed spectrum, candidate hypothesis, candidate-specific evidence and unresolved alternatives.
- Molecular structures, atom labels and reaction arrows must be interpretable at journal print size.
- Do not use a heatmap or training curve as the visual centre of the paper; the key panels should show chemistry and held-out structural discrimination.
