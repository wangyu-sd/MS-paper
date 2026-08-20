# Results Placeholder Registry

Use this as the checklist for replacing every `[RESULT: ...]`, `[DATA: ...]` and `[METHOD: ...]` marker in `main.tex`.

## Figure 1 — Evidence bottleneck

- Number and identities of hypothesis frontiers.
- Independent molecule-group count.
- Candidate MCES/Tanimoto/same-formula/shared-scaffold distributions by frontier.
- Fixed-evidence GT margin by frontier.
- Pairwise GT win rate and false-strong decoy rate.
- Correlation between candidate fidelity and static-evidence separability.
- Confidence intervals and preregistered significance test.
- Leakage/pretraining exclusion statistics.

## Figure 2 — Candidate-specific fragmentation evidence

- Hard-decoy benchmark size and construction.
- Final pLSE score equation.
- Mass tolerance and assignment policy.
- Mass-only baseline.
- Candidate-opportunity-normalized baseline.
- Generic graph-cut oracle/ablation.
- Reaction-centre eligibility ablation.
- Charge-carrier and H-transfer ablations.
- Full trajectory evidence.
- Same-formula and near-isomer GT rank / AUROC / pairwise win / false-strong metrics.
- Three chemically persuasive case studies with exact m/z, ppm, structures and atom-lineage traces.
- Reaction families that contribute most to discrimination.
- Fraction of discriminative margin versus fraction of explained intensity.

## Figure 3 — Experimental evidence beyond chemical prior

- Chemical-World / Spectral-Reality dataset sizes.
- Correct/no-spectrum/shuffled-spectrum candidate-ranking metrics.
- Spectral lift and identity lift with group-level confidence intervals.
- Six-arm normal/no-CoT/shuffled-CoT causal result.
- Family-wise error threshold and exact/Monte Carlo test details.
- Supported / unsupported / non-specific mechanism-claim fractions.
- Accuracy–coverage result after evidence-based abstention.

## Figure 4 — Reciprocal challenge–recovery

- Final number of ORBIT rounds and frozen snapshot identities.
- Accepted/rejected/evidence-required/stopped round counts.
- Complete `A_ij` cross-generation matrix.
- Candidate hardness per hypothesis frontier.
- Evidence discrimination per evidence frontier.
- Frozen-anchor and success-bank non-regression.
- Blind-alternation or fixed-evidence ablation.
- One complete failure → hypothesis → discriminating experiment → intervention → recovery case.

## Figure 5 — Transfer and non-resolution

- External candidate sources that are genuinely independent of ORBIT.
- Candidate count and hardness distribution for each external method.
- Initial versus final pLSE on every source.
- Same-formula and near-isomer transfer.
- Calibration split and test split.
- Unique-resolution accuracy–coverage.
- Candidate-set coverage.
- False-resolution rate.
- One resolvable and one intrinsically ambiguous case.

## Figure 6 — Private mouse cohort

### Cohort metadata
- Tissue(s), condition(s), sex/age if scientifically relevant and permitted.
- Number of animals, biological samples, injections and MS/MS features.
- Instrument, ionization, adduct policy and collision energy.
- Ethics/source-study approval and data-use provenance.
- Blank/QC/chimeric filtering.

### Anchor subset
- Definition of independent reference support.
- Number of blinded anchor spectra/molecules.
- ORBIT and applicable baseline performance.
- Calibration and false-resolution rate.

### Dark subset
- Exact library-search protocol defining “unlabelled/dark”.
- Number of dark spectra before and after quality filters.
- Formula/class/candidate-set/unique-hypothesis counts.
- Recurrence across biological replicates.
- Number of prioritized case studies.
- Orthogonal validation level for every structure-level claim.

### Optional biology
- Only include a tissue/condition association if it is reproducible and statistically supported independently of annotation selection.

## Methods placeholders

- Exact structure standardization.
- Molecule-group identity.
- Pretraining leakage exclusion radius.
- Final METEOR architecture/checkpoint lineage.
- Final spectrum-conditioning interface.
- Final pLSE reaction basis and search policy.
- Final pLSE score and chance-match correction.
- Mass tolerances by data source.
- Statistical tests, alpha and multiplicity correction.
- External-generator versions/checkpoints.
- Mouse processing software and settings.
- Public accession / release / Zenodo DOI.
