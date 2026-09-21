# Claim–Evidence Matrix

Internal truth contract for the Nature manuscript.

The paper now makes two coupled contributions:

1. **Inference paradigm:** spectra are partial observations of a latent molecular fragmentation world; one learned World supports Free prediction, Guided explanation and Inverse structure inference.
2. **Scientific consequence:** this shared World yields a hierarchy of stronger structural evidence that enables repository-scale resolution and analysis of dark chemistry.

No claim is submission-ready until its evidence cell is bound to an immutable artifact.

---

## Figure 1 — A molecular fragmentation world unifies prediction, explanation and inverse inference

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C1** | A tandem mass spectrum is better modelled as a partial observation of a latent multibranch fragmentation world than as the complete target of a direct predictor. | Compare latent-network World modelling with direct spectrum prediction under matched molecular splits and compute, evaluating observed coverage, multistage transitions and probability consistency. | molecule group | molecule-disjoint split; identical acquisition conditions; direct-spectrum baseline; unobserved generated states remain unlabeled rather than false | `TBD:C1_world_vs_direct` |
| **C2** | One shared chemical World can support Free, Guided and Inverse inference without changing the underlying chemistry between tasks. | Shared-state/shared-transition ablation versus disconnected task-specific models; evaluate Free coverage, Guided matched-budget gain and Inverse recovery. | molecule group / task | same World checkpoint or shared encoder/transition semantics; task-specific heads; target spectrum forbidden in Free | `TBD:C2_shared_world` |
| **C3** | Hard conservation and typed execution constrain chemical legality while learned policies allocate probability and compute among legal alternatives. | State/action validity audit across training and inference; deliberate invalid-action challenge set; conservation/materialization statistics. | transition / molecule | atom, electron, charge, H, exact mass, formula/valence checks; no reward-only legality | `TBD:C3_conservation` |
| **C4** | A multibranch probabilistic reaction network explains spectra better than single-path fragmentation under matched compute. | Compare full sibling/STOP/reconvergent network against single-path or greedy rollout. | molecule group | same transition model; same expansion budget; report censored frontier mass | `TBD:C4_multibranch_world` |

**Boundary:** these are paradigm claims. Do not substitute training loss, selector MRR or probe tests for C1–C4.

---

## Figure 2 — World-based inference establishes graded structural evidence

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C5** | Free World recovers experimentally observed masses and ordered fragmentation relations with calibrated probability flow. | Held-out Free-network evaluation. | molecule group | target spectrum hidden from policy; coverage, intensity-weighted coverage, parent-child transitions, multistage gain, probability conservation | `TBD:C5_free_world` |
| **C6** | Guided inference improves spectrum explanation under the same compute budget by reallocating expansion toward evidence-bearing branches. | Matched-budget Free vs Guided comparison. | molecule group | identical molecule/World/action constraints; Guided alone sees target spectrum; same max expansions/wall time | `TBD:C6_guided_gain` |
| **C7** | Inverse inference recovers a diverse posterior set of molecular structures rather than only one rank-1 guess. | Molecule-disjoint Inverse benchmark. | molecule group | Exact@K/Recall@K; best similarity/MCES; posterior diversity; formula/chemical validity; candidate-count matched baselines | `TBD:C7_inverse` |
| **C8** | Bidirectional World consistency distinguishes true candidates from hard structural alternatives. | Spectrum→candidate→World→spectrum replay on GT + hard decoys. | molecule group | same-formula and near-isomer pools; generator recall reported separately; forward coverage/path evidence; cycle consistency | `TBD:C8_bidirectional` |
| **C9** | WGV produces a monotone evidence hierarchy whose stronger levels correspond to higher structural reliability. | Stratify known-structure cohorts by evidence level and measure containment/accuracy/calibration. | molecule group | fixed definitions; no post hoc threshold tuning; report coverage at every level | `TBD:C9_evidence_hierarchy` |
| **C10** | Calibrated bounded structural statements remain reliable on chemistry unavailable at model freeze. | Historical library-growth prospective-by-time evaluation. | spectrum / structure | exact+analogue exclusion at freeze; independent depositing groups; frozen model/calibration; structural-distance stratification; comparator calibration | `TBD:C10_prospective` |

**Boundary:** the claim is stronger evidence and controllable ambiguity, not that mechanism is universally more accurate than every black-box model.

---

## Figure 3 — High-evidence inference resolves the dark metabolome at scale

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C11** | Repository-scale dark spectra can be moved from weak mass/formula compatibility to stronger World-based evidence levels at non-trivial scale. | Frozen WGV run over the complete eligible dark corpus. | spectrum / structural entity | frozen evidence thresholds; no sample/phenotype labels in inference; report full denominator and unresolved fraction | `TBD:C11_dark_resolution_funnel` |
| **C12** | High-evidence structural resolution collapses many spectral observations onto fewer chemical entities. | Validated adduct/isotope/charge/in-source/redundant-acquisition collapsing after structural resolution. | structural entity | collapsing error measured on known compounds; uncertainty propagated into counts | `TBD:C12_entity_collapse` |
| **C13** | A substantial subset of high-evidence dark entities/families recurs across independent datasets. | Cross-dataset recurrence analysis. | structural entity/family | shared-sample/lab audit; recurrence threshold frozen; technical spectra not independent | `TBD:C13_recurrence` |
| **C14** | Recurrent dark chemistry occupies both a near-known halo and remote structural families outside the predefined neighbourhood of characterized metabolism. | Frozen structural-distance analysis over high-evidence recurrent entities. | structural entity/family | reference set and distance threshold frozen; insufficient-resolution cases excluded from precise-distance claims | `TBD:C14_near_remote` |

**Headline quantity:** how much dark chemistry reaches each evidence level, then how many recurrent entities remain after collapsing.

---

## Figure 4 — Resolved dark chemistry reveals structural and biological organization

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C15** | High-evidence recurrent dark chemistry is non-randomly organized into structural families. | Structural graph/landscape and family-size/recurrence analysis. | entity/family | multiple structural-distance definitions; reference-set sensitivity; null family graph | `TBD:C15_structural_organization` |
| **C16** | Recurrent dark structural families show reproducible dependence on microbiota, diet or host context. | Harmonized public germ-free/gnotobiotic, antibiotic and dietary-intervention analyses. | family / biological dataset | positive controls; label permutation; batch/platform/study model; mixed/unresolved retained | `TBD:C16_source_partition` |
| **C17** | Biological source labels are coupled to structural organization rather than randomly distributed over dark chemistry. | Overlay source labels on frozen structural landscape; test local label autocorrelation and motif/class enrichment. | family | family frozen before labels; cross-study effect consistency; permutation null | `TBD:C17_structure_source` |

**Boundary:** dependence is not biosynthesis; structural relation is not pathway evidence.

---

## Figure 5 — Dark molecular families reveal biology hidden from feature-level metabolomics

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C18** | Structural-family analysis is more reproducible than treating the same dark observations as independent anonymous features. | Paired feature-vs-family analysis across all eligible biological contrasts/cohorts. | biological sample / family | same samples/preprocessing/covariates; family definitions frozen before phenotype testing; one preregistered primary endpoint | `TBD:C18_family_gain` |
| **C19** | At least one high-evidence recurrent dark molecular programme shows replicated biological association. | Frozen family-level discovery + independent replication. | biological sample | multiplicity control; cohort replication; metadata permutation; leave-one-cohort-out | `TBD:C19_programme` |
| **C20** | Selected high-evidence structures survive orthogonal authentic-standard validation while unresolved alternatives remain explicitly bounded. | Standard MS/MS + retention/coelution; unresolved-case dossier. | molecular hypothesis | anchor criterion frozen before purchase; failures retained; full alternative set | `TBD:C20_standard` |

**Boundary:** one case study cannot replace C18.

---

# Supporting / Extended Data claims

| ID | Claim | Role |
|---|---|---|
| **S1** | Explicit atom/electron/H/charge/exact-mass state representation reduces invalid chemistry. | ED2 |
| **S2** | H-group action compression preserves chemistry while reducing redundant policy actions. | ED2 |
| **S3** | Closed charged/neutral state enables exact forward/backward accounting. | ED2 |
| **S4** | Canonical inverse graph state avoids duplicate GFlowNet/SMC states. | ED5 |
| **S5** | DAgger mitigates teacher/frontier distribution shift in Guided inference. | ED4 |
| **S6** | SubTB better represents many valid Free trajectories than winner-take-all optimization. | ED3 |
| **S7** | Inverse SMC/GFlowNet preserves posterior diversity under hard chemistry constraints. | ED5 |
| **S8** | Outer-loop agent evolution expands scientific capability only when held-out gates accept the change. | ED7 |
| **S9** | Scientific World KPIs can diverge from training loss; promotion therefore uses held-out science endpoints. | ED3/ED7 |

---

# Nature submission gates

## Paradigm gate
- C1/C4: the latent multibranch World must provide measurable value beyond direct/single-path prediction.
- C2: shared-World coupling must not be cosmetic; at least two of Free/Guided/Inverse should measurably benefit from shared semantics.
- C3: chemical validity must be essentially hard-constrained, not merely average-case.

## Capability/evidence gate
- C6: Guided must improve explanation or efficiency under matched compute.
- C7: Inverse must provide useful Recall@K/diversity under molecule-disjoint evaluation.
- C8/C9: stronger World evidence levels must correlate with structural reliability.
- C10: prospective credibility should remain meaningful under structural-distance shift.

## Discovery gate
- C11: a non-trivial fraction of dark spectra must reach strong World-based evidence.
- C13/C14: recurrent and remote dark chemistry must be quantitatively non-trivial.
- C16/C17: source dependence should organize structural space.
- C18: family-level biological analysis must show systematic gain, not only one positive family.

If only the paradigm succeeds, submit as a high-level methods paper. If only the atlas succeeds, the WGV novelty is underused. The Nature story requires both.

---

# Standing rules

1. A spectrum is a partial observation of the latent fragmentation world.
2. Unobserved World states are unlabeled unless the observation model supports a negative claim.
3. W/G/V are conditional inference modes over one chemical world, not three arbitrary scorers.
4. Chemical legality is hard-constrained; learning controls probability/value/search.
5. Candidate recall, evidence discrimination and end-to-end structure recovery are separate.
6. Evidence levels are fixed before evaluating dark chemistry.
7. Model-derived unique structures are not authentic-standard identifications.
8. Biological samples, not spectra, are units of biological inference.
9. Structural relation is not biosynthetic mechanism.
10. Training loss and agent activity are not manuscript endpoints.
