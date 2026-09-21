# Claim–Evidence Matrix

Internal truth contract. The paper is not a model paper with an application appendix. It makes a field-level claim that the dark metabolome can be measured as a recurrent, structured and biologically organized chemical layer.

No main-text claim is submission-ready until its evidence cell is bound to an immutable artifact.

---

## Figure 1 — Credibility of bounded structural measurement

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C1** | The system can convert spectra into bounded structural statements at a controllable soundness–resolution operating point. | Sweep elimination/retention stringency on leakage-controlled known-structure spectra; measure false exclusion and achieved resolution level. | molecule group | molecule-disjoint split; matched candidate pools; candidate recall reported separately; mass-tolerance and noise sensitivity | `TBD:C1_soundness_resolution` |
| **C2** | Reported confidence remains informative on chemistry not available when the system was frozen. | Historical library freeze followed by evaluation on spectra dark at freeze whose structures were independently deposited later. | spectrum / structure | exact + analogue exclusion at freeze; independent depositing groups; frozen model/rule/calibration artifacts; structural-distance stratification | `TBD:C2_prospective_calibration` |
| **C3** | Mechanistic evidence contributes candidate discrimination beyond precursor/formula and generic spectral similarity. | Same-formula and near-isomer matched-pool benchmark with identical spectra/pools across comparators. | molecule group | exact-mass, forward-spectrum, CFM-ID, SIRIUS/CSI:FingerID or executable equivalent; spectrum-shuffle control; full leakage audit | `TBD:C3_discrimination` |

**Boundary:** Figure 1 earns trust; it is not the scientific climax. Raw model loss, selector accuracy, trace exact-match and agent progress never substitute for C1–C3.

---

## Figure 2 — Structural census

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C4** | Spectral-feature counts materially overstate the number of distinct dark chemical entities. | Frozen entity-collapsing pipeline over mouse + repository dark spectra. | structural entity | collapsing validated on known compounds; uncertainty propagated from measured collapsing error; no phenotype/sample labels used | `TBD:C4_census_contraction` |
| **C5** | A substantial subset of dark entities is recurrent across independent datasets and therefore represents reproducible chemistry rather than one-study artefacts. | Cross-dataset recurrence analysis after entity definition is frozen. | structural entity / independent dataset | independence audit across shared samples/labs; sensitivity to recurrence threshold; corpus-stratified counts | `TBD:C5_recurrence` |
| **C6** | The census preserves uncertainty: entity counts can be partitioned by structural resolution instead of being reported as unique identifications. | Resolution hierarchy over the complete recurrent census. | structural entity | confidence threshold frozen; unique putative structures separated from standard-confirmed structures | `TBD:C6_resolution_distribution` |

**Headline quantity:** `N_dark features → N_recurrent structural entities` with an uncertainty interval.

---

## Figure 3 — Chemical organization

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C7** | Recurrent dark chemistry is non-randomly organized relative to characterized metabolism. | Structural-distance landscape between recurrent resolved entities and a frozen reference-metabolite set. | structural entity / family | reference set frozen; multiple distance definitions; class-level-only entities not assigned precise distances | `TBD:C7_structural_landscape` |
| **C8** | The dark metabolome contains both a near-known halo and recurrent structural families beyond a predefined neighbourhood of characterized chemistry. | Pre-registered near/remote partition + family recurrence analysis. | structural entity / family | neighbourhood definition frozen before counting; reference-set sensitivity; uncertainty by resolution level | `TBD:C8_remote_families` |
| **C9** | Reference libraries systematically underrepresent specific regions/classes of recurrent dark chemistry. | Chemical-class composition of recurrent entities versus matched reference libraries. | structural entity | detectability/ionization caveats; acquisition-stratified sensitivity; no claim of organism-wide abundance | `TBD:C9_library_bias` |

**Boundary:** structural relationship or mass difference does not establish an enzymatic reaction.

---

## Figure 4 — Biological source organization

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C10** | Recurrent dark structural families show reproducible dependence on microbiota, diet or host context. | Harmonized public germ-free/gnotobiotic, antibiotic and dietary-intervention datasets. | structural family / biological dataset | positive-control metabolites; label permutation; batch/platform model; mixed/unresolved category retained | `TBD:C10_source_partition` |
| **C11** | Source dependence is coupled to chemical structure rather than being a detached abundance pattern. | Overlay source assignments on the frozen structural landscape and test motif/class enrichment with cross-dataset consistency. | structural family | family definitions frozen before attribution; cross-dataset direction consistency; detectability sensitivity | `TBD:C11_structure_source` |

**Boundary:** use “microbiota-dependent”, “diet-dependent” and “host-associated”; do not claim direct biosynthesis without direct experiments.

---

## Figure 5 — Biological value of structural family resolution

| ID | Claim | Experiment | Unit | Minimum controls | Artifact |
|---|---|---|---|---|---|
| **C12** | Structural-family analysis yields more reproducible biological signal than treating the same dark spectra as anonymous features. | Pre-registered feature-versus-family comparison across available biological contrasts/cohorts. | biological sample / family | family definitions frozen before testing; same underlying spectra; multiplicity control; cross-cohort replication endpoint selected a priori | `TBD:C12_family_gain` |
| **C13** | At least one recurrent dark structural programme shows a replicated association with a biologically meaningful contrast. | Frozen family-level association plus independent-cohort replication. | biological sample | covariates; multiplicity; metadata permutation; leave-one-cohort-out sensitivity | `TBD:C13_programme` |
| **C14** | Selected structural anchors survive orthogonal validation, while unresolved alternatives remain explicitly bounded. | Authentic standards for frozen commercially available anchors + complete unresolved-case dossier. | molecular hypothesis | anchor criterion frozen before purchase; report failed anchors; MS/MS + retention/coelution criteria; alternative-candidate dossier | `TBD:C14_anchors` |

**Boundary:** one strong family is supporting evidence for C12, not a replacement for the global feature-versus-family test.

---

## Supporting claims — Methods / Extended Data

| ID | Claim | Role |
|---|---|---|
| **S1** | Forward fragmentation, spectrum-guided explanation and inverse structure construction share a conservation-preserving fragmentation World. | Methods / ED2 |
| **S2** | Candidate generation and evidence discrimination are separable bottlenecks. | ED2 |
| **S3** | Explicit atom/electron/H/charge bookkeeping and mass-aware state/action constraints reduce chemically invalid reasoning. | Methods / ED2 |
| **S4** | Automated programme/rule evolution expands coverage without being allowed to self-accept revisions. | ED6 |
| **S5** | Verified hypothesis-model traces correlate with structural accuracy at matched confidence. | ED4 |
| **S6** | World scientific KPIs must be evaluated independently of training loss. | ED2/ED6 |

These are important for technical credibility but must not expand into separate main-text claims unless they directly change C4–C14.

---

## Nature submission gates

### Minimum scientific gate
- C1–C3 establish credible bounded structural measurement.
- C4 yields a defensible entity-count contraction with uncertainty.
- C5 shows a non-trivial recurrent subset.
- C7/C8 reveal a reproducible chemical organization beyond a trivial nearest-neighbour picture.
- C12 demonstrates a global biological advantage of structural-family analysis.
- C14 includes at least two successful standard-confirmed anchors if commercially feasible.

### Strong Nature gate
The paper should contain all of:
1. a field-level census number not previously available (C4);
2. a non-obvious global chemical-organization result (C7–C9);
3. reproducible biological source organization (C10/C11);
4. a systematic family-level biological gain, not only a case study (C12);
5. prospective credibility that remains useful under structural-distance shift (C2).

If the atlas only resolves near-known analogues, or if family-level biology does not improve on anonymous features, the Nature framing must be reconsidered rather than cosmetically preserved.

---

## Standing rules

1. Repeated spectra are not independent samples.
2. Feature count is not molecule count.
3. Generator failure is not evidence failure.
4. Model-derived unique structure is not standard-confirmed identification.
5. “Dark” means absent from the frozen accepted spectral-library match protocol, not absent from all databases.
6. Structural proximity is not biosynthetic mechanism.
7. Source attribution is dependence, not synthesis.
8. Mechanistic completeness is empirical and must be calibrated.
9. Training improvement is not scientific improvement.
10. Main figures prioritize discoveries about the chemical world; implementation evidence belongs in ED unless indispensable for belief.
