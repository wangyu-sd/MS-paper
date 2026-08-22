# Figure Plan

The main text uses **six** primary figures. The ordering is intentional: the first figure establishes the core scientific object contributed by the paper, the second shows why that object becomes necessary as molecular hypotheses improve, Figures 3–4 establish causal and adaptive properties, and Figures 5–6 carry the work into metabolomics-scale resource construction and biological discovery. Agent architecture, detailed CoT tests and low-level protocol diagnostics belong in Extended Data or Supplementary Information.

The visual story should read as a scientific progression even without the manuscript text:

`discriminative fragmentation evidence → evidence bottleneck → experimental evidence → counterexample-driven adaptation → dark-metabolome map → biological discovery`.

## Figure 1 — Discriminative fragmentation evidence resolves molecular alternatives

**Message:** the structural information in a tandem mass spectrum is concentrated in observations that distinguish competing molecular hypotheses, not necessarily in the most intense, most numerous or most broadly explained fragments.

This is the chemical and conceptual centre of the manuscript and should appear before the field-level bottleneck analysis.

- **a** One intuitive real-spectrum example with a ground-truth structure and close alternatives. Show the evidence hierarchy directly: structure-derived fragment-mass support → competitor-relative specificity → atom-traceable chemical authority.
- **b** Real-spectrum bridge analysis: ground-truth versus same-formula best-decoy fragment-mass support and candidate-relative margin under identical pools.
- **c** Comparator panel under identical hard candidate pools: exact mass, opportunity-normalized matching, forward-spectrum similarity, CFM-ID/SIRIUS-derived or other executable fragmentation-aware score, fragment-mass support, candidate-relative evidence and pLSE authority layers.
- **d** Same-formula and near-isomer GT rank / pairwise win / false-strong distributions.
- **e** Ablation ladder: fragment-mass support → candidate specificity → reaction-centre eligibility → atom/charge/H accounting → full trajectory authority, including fragment-space size / overgeneration controls.
- **f–h** Three chemically distinct case studies with large structures, spectra, decisive m/z values, atom lineage, bond changes and evidence certificates; include one explicitly unresolved case.
- **i** Fraction of discriminative margin captured versus fraction of observed/explained intensity and theoretical fragment-space size.

**Critical claim:** fragment support is not equivalent to structural evidence. Broad peak coverage and broad theoretical reachability are neither necessary nor sufficient for discrimination.

**Visual priority:** the first panel should let a non-specialist editor understand within seconds why one peak can be more structurally informative than many shared peaks. Structures and spectra should dominate; equations and architecture should not.

## Figure 2 — Better molecular hypotheses expose an evidence bottleneck

**Message:** advances in molecular hypothesis generation systematically move structure elucidation from a generation-limited regime towards an evidence-limited regime in which close alternatives share much of the observable fragmentation support.

Having established the evidence object in Figure 1, this figure explains why it becomes increasingly important.

- **a** Conceptual regime shift: easy/implausible alternatives in a generation-limited regime versus close same-formula alternatives in an evidence-limited regime.
- **b** Candidate difficulty across at least two independent candidate sources plus matched database candidates: MCES, Morgan Tanimoto, same-formula and scaffold relation.
- **c** Multiple frozen evidence systems evaluated on the same difficulty strata: exact mass, forward-spectrum similarity, external fragmentation-aware comparator(s), initial pLSE / initial evidence model.
- **d** Molecule-group candidate fidelity versus GT–best-decoy separability after matching pool size, formula and precursor constraints.
- **e** Shared-versus-specific fragment-mass support as candidate similarity increases.
- **f** Representative spectrum in which peaks that exclude an early decoy become shared among later near-isomeric alternatives.

**Critical control:** do not infer the phenomenon by arbitrarily selecting harder negatives. Candidate-set size and precursor constraints must be matched, and the trend must reproduce across independent candidate sources.

**Visual priority:** this should look like a field-level regime shift, not a METEOR benchmark.

## Figure 3 — Experimental spectra distinguish evidence from chemical plausibility

**Message:** a chemically plausible fragment or fragmentation path is not automatically experimental evidence; useful evidence is the part of the measured observation that changes the relative support of competing structures.

- **a** Matched structure-only and spectrum-conditioned views of the same chemical fragmentation prior. Keep the internal labels Chemical-World/Spectral-Reality out of the main visual if possible.
- **b** Correct / no-spectrum / mass-adduct-matched shuffled-spectrum controls.
- **c** Spectral lift and identity lift for molecular ranking and discriminative fragmentation evidence.
- **d** Evidence-authority decomposition: spectrum-specific, shared, unsupported and beyond trace authority.
- **e** One candidate set where chemical plausibility is similar across alternatives but the true spectrum changes the supported hypothesis.

**Move out of main figure:** parent/pilot × normal/no-CoT/shuffled-CoT six-arm experiment → Extended Data Figure 6.

## Figure 4 — Counterexamples adapt fragmentation evidence to harder hypotheses

**Message:** hard molecular alternatives expose specific failures of a fixed evidence model; bounded, verified revisions recover discrimination and transfer beyond the candidate source that exposed the failure.

The scientific object is adaptation of the executable evidence model, not the agent architecture itself.

- **a** Initial evidence loses discrimination on later/harder hypotheses, followed by recovery with adapted evidence.
- **b** Failure decomposition into missing informative support, overgenerated/shared support and insufficient chemical authority.
- **c** Factorial endpoint design: `(H0,E0)`, `(HT,E0)`, `(H0,ET)`, `(HT,ET)` and interaction effect `Δ_int`.
- **d** Gated adaptation versus fixed-side and ungated/blind alternation controls.
- **e** Post-freeze cross-generation challenge–recovery matrix `A_ij`.
- **f** External-generator/retrieval transfer: initial versus adapted evidence model.
- **g** Generator recall versus conditional discrimination versus end-to-end resolution.
- **h** Calibrated/risk-controlled structural candidate sets: empirical coverage, set size, resolvable and unresolved examples.

**Critical control:** the cross-generation matrix is descriptive. The factorial endpoint experiment and external transfer carry the causal/generalization claims.

**Visual priority:** panel a should communicate the scientific result before the reader encounters any ORBIT protocol details.

## Figure 5 — Evidence-bounded mapping of the dark metabolome

**Message:** the practical output of structure elucidation at metabolomics scale is an evidence-bounded molecular map, not a forced unique SMILES for every dark spectrum.

This figure upgrades the previous small mouse case-study panel into a resource-scale result.

- **a** Independent metabolomics cohort(s) and frozen dark-spectrum construction: all MS/MS → quality-controlled spectra → exact-library-hit removal → blinded anchors + dark spectra.
- **b** Blinded-anchor validation: generator recall, conditional discrimination, end-to-end resolution and applicable peer-reviewed baselines.
- **c** Resource-wide resolution landscape: unresolved → formula → structural family → bounded candidate set → high-confidence putative 2D structure → orthogonally confirmed structure.
- **d** Candidate-space contraction across the dark resource, including calibrated set-size distributions and false-resolution control.
- **e** Chemical-space / molecular-family organization of previously dark spectra, with evidence level encoded independently of molecular similarity.
- **f** Recurrence and reproducibility of prioritized dark features across biological samples / cohorts.
- **g** Parallel deep examples: one resolved/strongly narrowed case and one unresolved isomer case, both with explicit evidence and alternatives.

**Critical claim:** the resource must expose uncertainty rather than convert every spectrum into a structure prediction. Exact structures are claimed only at the evidence level justified by the frozen protocol and orthogonal validation.

**Resource deliverable:** release spectrum identifiers, formula / candidate-family assignments, candidate sets, discriminative masses, evidence authority, resolution level, reproducibility and validation status.

## Figure 6 — Dark-metabolome mapping reveals previously hidden biology

**Message:** organizing dark spectra by evidence-bounded molecular structure reveals a reproducible biological pattern that was inaccessible when the same features remained chemically unresolved.

The exact biological finding must be data-driven rather than pre-scripted, but the figure should be designed around one coherent discovery rather than a catalogue of associations.

- **a** Resource-wide screen identifying one reproducible molecular family, structural transformation series or metabolite programme associated with a predefined tissue, condition, genotype or phenotype.
- **b** Replication of the family-level / metabolite-level pattern across independent biological samples or an independent cohort where available.
- **c** Structural organization of the discovery: shared scaffold / transformation series / discriminative fragments connecting the previously dark features.
- **d** Selection of 2–4 anchor metabolites or spectra that carry the biological interpretation.
- **e** Orthogonal structure validation for representative anchors using authentic standards, matched MS/MS and RT/co-elution; targeted MSn or spike-in where informative.
- **f** Focused biological validation appropriate to the discovery, only if scientifically justified by the source cohort (for example perturbation, isotope tracing, microbiome dependence or pathway-context validation).
- **g** Integrated model linking the newly resolved molecular family to the biological process without overextending beyond the validated evidence.

**Critical claim:** Figure 6 must show that the resource enabled a biological conclusion that could not be made reliably from unannotated features alone. A large number of annotations without a coherent biological discovery is not sufficient.

**Nature-main-track extension:** if prospective experiment selection is completed, one panel can show `ambiguity → predicted missing discriminative evidence → targeted MSn/CE measurement → candidate contraction` as a direct demonstration that ORBIT changes the experimental elucidation workflow.

## Extended Data

1. Dataset composition, split and pretraining leakage audit.
2. Complete hard-decoy benchmark and real-spectrum fragment-mass support diagnostics.
3. Candidate-difficulty matching and evidence-bottleneck sensitivity analyses.
4. Reaction-basis coverage, search truncation and fragment-space overgeneration diagnostics.
5. Full fragmentation-evidence ablations and evidence-authority decomposition.
6. Parent/pilot × normal/no-reasoning/shuffled-reasoning six-arm causal analysis.
7. Reciprocal-run replicates, fixed-side/ungated controls and full cross-generation matrix.
8. External transfer, generator recall, conditional discrimination, conformal/risk-controlled candidate sets and calibration.
9. Dark-metabolome resource QC, library overlap, blinded-anchor evaluation, recurrence and resolution-level audit.
10. Complete dark-spectrum evidence dossiers and orthogonal validation.
11. Resource-wide biological association statistics, multiple-testing control and replication.
12. Full standard / RT / MSn validation records for Figure 6 anchor metabolites.

## Visual principles

- Use a white background, sparse panels and large molecular structures/spectra.
- Avoid dense multi-agent diagrams and decorative AI icons.
- Reuse one or two anchor spectra across Figures 1–3 so the scientific logic is visually continuous.
- Encode scientific roles consistently: observed spectrum, candidate hypothesis, fragment-mass support, discriminative evidence, chemical authority and unresolved alternatives.
- Molecular structures, atom labels and reaction arrows must be interpretable at journal print size.
- Do not use a heatmap, architecture diagram or training curve as the visual centre of the paper; key panels should show chemistry, structural alternatives, evidence supplied by the experiment and the biological structure exposed by the resource.
- Figure titles and panel headings should describe scientific findings, not implementation modules.
- Figures 5–6 should visually resemble metabolomics discovery/resource figures rather than model benchmark figures.