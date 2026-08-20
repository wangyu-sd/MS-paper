# Figure Plan

The main text is capped at six modest display items. Each main figure must advance one scientific proposition; implementation detail goes to Extended Data.

## Figure 1 — The evidence bottleneck

**Message:** better generators do not monotonically simplify structure elucidation.

- **a** One spectrum, GT, early easy decoys and late hard near-isomer decoys.
- **b** Candidate fidelity over generations: MCES, Tanimoto, same-formula, scaffold proximity.
- **c** Frozen-evidence performance over the same generations.
- **d** Molecule-group scatter: candidate fidelity vs spectral separability.
- **e** One visual example showing shared peaks that lose discriminative value.

Avoid architecture graphics here.

## Figure 2 — Chemical evidence is a discrimination object

**Message:** explainable fragmentation becomes scientifically useful when it is candidate-specific.

- **a** Compact pLSE trajectory: ion state → reaction centre → elementary event → product/co-product → peak.
- **b** Ablation ladder under identical candidate pools.
- **c** GT/decoy distributions in same-formula and near-isomer strata.
- **d–f** Three chemical case studies, preferably different reaction families.
- **g** Discriminative evidence vs global peak-coverage contribution.

Chemical structures, atom mapping and peak labels must be large enough to inspect.

## Figure 3 — Spectrum evidence versus chemical prior

**Message:** a plausible chemical explanation is not proof that the experimental spectrum was used.

- **a** Chemical-World / Spectral-Reality matched views.
- **b** Correct / no-spectrum / shuffled-spectrum controls.
- **c** Spectral lift and identity lift.
- **d** Six-arm reasoning causal experiment.
- **e** Evidence-authority categories for generated mechanistic claims.
- **f** Accuracy–coverage after abstention.

## Figure 4 — Reciprocal falsification

**Message:** hypothesis and evidence frontiers produce challenge–recovery dynamics.

- **a** ORBIT control loop, with agent/runtime visually secondary to scientific objects.
- **b** Cross-generation matrix `A_ij`.
- **c** Candidate hardness ↑ and evidence recovery curves.
- **d** Accepted/rejected/evidence-required/stop rounds.
- **e** Frozen anchor and success-bank protection.
- **f** One full causal round.

## Figure 5 — Transfer and calibrated non-resolution

**Message:** evidence improvement is not opponent-specific and the system does not force an answer when the spectrum is ambiguous.

- **a** Independent candidate-source design.
- **b** Initial vs final pLSE across external generators.
- **c** Strict same-formula/near-isomer transfer.
- **d** Accuracy–coverage and calibration.
- **e** Resolvable pair.
- **f** Unresolvable pair.

## Figure 6 — Mouse dark metabolome

**Message:** ORBIT turns unlabelled experimental spectra into auditable, confidence-aware hypotheses.

- **a** Mouse cohort; blinded anchor and dark-spectrum branches.
- **b** Annotation-depth Sankey/stack: unknown → formula → class/family → candidate set → uniquely resolved.
- **c** Recurrence/reproducibility across samples.
- **d** Deep resolved case.
- **e** Deep unresolved case.
- **f** Orthogonal validation; use biological association only if strong.

## Extended Data

1. Dataset composition and leakage audit.
2. Reaction-basis coverage/search truncation.
3. Instrument/adduct/collision-energy robustness.
4. Full hard-decoy benchmark.
5. Full fragmentation ablations.
6. ORBIT replicate/seed stability.
7. Full cross-generator transfer.
8. Calibration/abstention.
9. Mouse QC and recurrence.
10. Complete mouse evidence certificates.

## Visual style

- Nature-like: white background, sparse panels, large molecular structures and spectra.
- Avoid dense agent-box diagrams and decorative AI icons.
- Reuse the same spectrum/candidate examples across Figures 1–3 when possible to create continuity.
- Primary colors should encode scientific roles consistently: hypothesis, evidence, observation, unresolved. Final palette should be color-blind safe.
- Molecular structures and reaction arrows must remain chemically interpretable at journal print size.
