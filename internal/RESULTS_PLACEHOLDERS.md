# Results Placeholder Registry

Use this as the checklist for replacing every `[RESULT: ...]`, `[DATA: ...]` and `[METHOD: ...]` marker in `main.tex`.

The revised manuscript has five main figures. The structured-CoT causal analysis is supporting Extended Data rather than a core manuscript claim.

## Figure 1 — Cross-model evidence bottleneck

### Candidate sources and matching
- Final candidate sources: successive METEOR snapshots plus at least one genuinely independent peer-reviewed generator/retrieval source and formula/mass-matched database candidates.
- Independent molecule-group count.
- Frozen candidate count per spectrum.
- Difficulty-bin definition (MCES/Tanimoto/same-formula/scaffold relation).
- Matching procedure controlling candidate count, formula and precursor mass.
- Candidate validity and duplicate-removal statistics.

### Frozen evidence systems
- Exact-mass baseline.
- Forward-spectrum similarity baseline.
- CFM-ID/SIRIUS-derived or other executable fragmentation-aware comparator(s).
- Initial pLSE evidence snapshot.

### Main results
- Pairwise GT win rate by candidate difficulty and evidence system.
- GT-versus-best-decoy margin.
- False-strong alternative rate.
- Same-formula and near-isomer stratification.
- Molecule-group association between candidate fidelity and fixed-evidence separability.
- Cross-source consistency of the evidence-bottleneck slope/effect.
- Confidence intervals and preregistered significance tests.
- Pretraining/test leakage audit statistics.

## Figure 2 — Candidate-specific fragmentation evidence

### Scientific object to freeze first
- Exact production definition of trajectory support `Q(τ,p)`.
- Exact candidate-relative specificity definition.
- Exact pLSE aggregation equation.
- Peak weights.
- Candidate-opportunity correction `Ω(M)`.
- Mass tolerances by source.
- Peak-to-fragment assignment policy.
- Policy for unsupported peaks/negative evidence.

### Benchmark
- Number of independent molecule groups.
- Number of candidates per group.
- Formula/mass/scaffold/similarity strata.
- Hard-decoy construction without test leakage.

### Comparator set
- Exact-mass matching.
- Opportunity-normalized matching.
- Forward-spectrum similarity.
- CFM-ID/SIRIUS-derived or other peer-reviewed executable fragmentation comparator(s).
- Generic-cut reachability analysis/ablation.
- Initial/non-candidate-relative pLSE.
- Full candidate-specific pLSE.

### Main endpoints
- GT rank.
- Pairwise GT win rate.
- AUROC or frozen ranking metric.
- False-strong decoy rate.
- Same-formula and near-isomer subsets.
- Effect of reaction-centre, atom/charge/H, candidate-relative and opportunity-control ablations.
- Fraction of discriminative margin versus fraction of explained intensity.

### Chemical case studies
For at least three chemically distinct examples:
- observed spectrum and precursor;
- GT and nearest decoy structures;
- exact observed/theoretical m/z;
- signed/absolute ppm error;
- reaction family and reaction-centre identity;
- atom/component lineage;
- broken/formed bonds;
- charge/H transfer;
- evidence authority;
- strongest alternative explanation and why it is weaker/shared/unavailable.

## Figure 3 — Experimental spectrum beyond chemical prior

### Dataset/controls
- Chemical-World record count.
- Spectral-Reality record count.
- Correct-spectrum cases.
- No-spectrum sentinel definition.
- Shuffled-donor construction: distinct molecule group, adduct match, neutral-mass window and peak/acquisition matching.

### Endpoints
- METEOR same-formula candidate rank/likelihood under correct/no/shuffled conditions.
- pLSE candidate-specific evidence under correct/shuffled spectra.
- Spectral lift with group-level interval.
- Identity lift with group-level interval.
- Spectrum-specific/shared/unsupported/beyond-authority explanation fractions.

### Supporting ED6
- Parent/pilot × normal/no-reasoning/shuffled-reasoning six-arm effect.
- Family-wise error threshold.
- Group bootstrap/sign-flip results.
- Non-target gates.

## Figure 4 — Reciprocal adaptation, transfer and structural risk control

### Factorial adaptation experiment
- Frozen identities of `H0`, `E0`, `HT`, `ET`.
- Identical final held-out cases and candidate-pool protocol.
- Primary endpoint for `(H0,E0)`, `(HT,E0)`, `(H0,ET)`, `(HT,ET)`.
- Interaction effect `Δ_int` with confidence interval/test.
- Fixed-hypothesis adaptation control.
- Fixed-evidence training control.
- Ungated/blind-alternation control.
- Replicate/seed stability.

### Challenge–recovery
- Complete post-freeze `A_ij` matrix.
- Candidate hardness by hypothesis snapshot.
- Evidence discrimination by evidence snapshot.
- Accepted/rejected/evidence-required/stopped move counts.
- Frozen-anchor, non-target and success-bank retention.

### External transfer
- Final independent candidate sources and exact versions/checkpoints.
- No-pLSE-guided generation/reranking confirmation.
- Candidate counts/hardness by source.
- Initial versus final pLSE effect by source.
- Same-formula and near-isomer transfer.

### Risk-controlled structural resolution
- Candidate-set size `K` used for generator recall.
- `P(GT ∈ C_K)` generator recall.
- Conditional discrimination given GT present.
- End-to-end resolution.
- Calibration split identity.
- Final split-conformal/risk-control method.
- Target alpha/coverage.
- Empirical set coverage.
- Median/quantile candidate-set size.
- Unique-resolution rate.
- False-resolution rate.
- One resolvable and one unresolved isomer case.

## Figure 5 — Private mouse cohort

### Cohort metadata
- Tissue(s), condition(s), sex/age if scientifically relevant and permitted.
- Number of animals, biological samples, injections and MS/MS features.
- Instrument, ion mode, acquisition method and collision-energy regime.
- Ethics/source-study approval and data-use provenance.
- Blank/QC/chimeric/duplicate filtering.

### Blinded anchor subset
- Independent-reference definition.
- Number of anchor spectra/molecule groups.
- Reference concealment procedure.
- Generator recall.
- Conditional discrimination.
- Risk-controlled end-to-end resolution.
- Applicable baseline performance.
- Complete error analysis.

### Dark subset
- Frozen spectral-library search protocol defining dark/unlabelled.
- Number before/after QC.
- Formula-compatible candidate count distribution.
- Risk-controlled candidate-set size distribution after pLSE.
- Number of unique putative structures at the frozen risk threshold.
- Formula/class/family-only outcomes.
- Deliberately unresolved outcomes.
- Recurrence across independent mouse samples.

### Orthogonal validation
For every structure-level case:
- authentic standard/coelution or RT;
- targeted MSn;
- blinded reveal;
- NMR or other applicable evidence;
- confidence terminology;
- surviving alternative-candidate dossier.

### Optional biology
Only include a tissue/condition association if predefined, replicated and statistically supported after annotation-confidence stratification.

## Nature-main-track extension — Active evidence acquisition

If pursued:
- definition of candidate experiment action (fragment/precursor/CE/adduct);
- information-gain or candidate-space-contraction objective;
- baseline acquisition policy;
- ambiguous MS2 cases frozen before acquisition;
- prospective MSn/CE measurements;
- candidate-space contraction after measurement;
- fraction of cases resolved by ORBIT-selected versus baseline-selected experiments.

## Methods placeholders

- Exact molecular standardization and molecule-group identity.
- Pretraining/test exclusion radius and full leakage audit.
- Final candidate-difficulty matching protocol.
- Final pLSE reaction basis, trajectory-quality function and aggregation equation.
- Mass tolerances and global assignment policy.
- Final METEOR architecture/checkpoint lineage and spectrum interface.
- Reciprocal-run promotion thresholds.
- Factorial endpoint metric.
- External-generator versions/checkpoints.
- Conformal/risk-control procedure and alpha.
- Statistical tests and multiplicity correction.
- Mouse processing software/settings and public accession.
- Frozen code/model release and Zenodo DOI.
