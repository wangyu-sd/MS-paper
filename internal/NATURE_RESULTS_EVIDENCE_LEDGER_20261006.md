# ORBIT-MS Nature results evidence ledger — 2026-10-06

Status: internal factual source for the Nature manuscript.  
Primary implementation repository: `wangyu-sd/orbit-ms`.  
Paper repository: `wangyu-sd/MS-paper`.

This document records **completed, source-bound results only**. It is intentionally stricter than a project progress log. Training losses, smoke tests, incomplete jobs, post-hoc examples selected after seeing the target, and unofficial extrapolations are not promoted to manuscript results.

The intended Nature paper is not a benchmark paper. The central scientific argument should be:

> **Molecular formula is largely recoverable from MS/MS, whereas exact molecular connectivity remains underdetermined by current proposal mechanisms. An explicit forward fragmentation World provides spectrum-specific structural evidence, allowing proposal failure, structural ambiguity and evidence quality to be separated rather than hidden inside a single end-to-end score. The final paper must then show that this evidence can be converted into high-confidence structure hypotheses at scale and reveal organized dark chemistry.**

The evidence below is therefore organized by the role it can play in that argument.

---

## 0. Evidence classes used in this document

### A — main-text-ready completed evidence
A result is class A only if:
- the full declared population was evaluated;
- denominator and identity definition are explicit;
- official VAL/TEST were not opened unless explicitly stated;
- the artifact is immutable/source-bound;
- the result supports a scientific claim that remains valid under the current fingerprint-free direction.

### B — Extended Data / mechanism / failure-analysis evidence
Completed and reproducible, but not suitable as a headline result because it is:
- a development-set diagnosis;
- an open-prior setting;
- an over-budget diagnostic;
- a historical architecture;
- or a fixed-candidate causal test rather than end-to-end structure generation.

### C — historical/internal only
Do not use as a Nature headline. Typical reasons:
- molecular fingerprints influence the candidate route;
- the result has been superseded by a cleaner protocol;
- the experiment is only an engineering sample;
- or the method is not the current canonical WGV path.

Morgan/Tanimoto is evaluation-only in the current canonical project. No molecular-fingerprint-to-structure route may be used in the final de novo method.

---

# 1. Frozen population and leakage-control facts

## 1.1 Full TRAIN and SEARCH_DEV

Current chemical-evidence development uses:

| Split | Spectra | Molecule groups | SHA-256 |
|---|---:|---:|---|
| Full TRAIN | 175,548 | 20,430 | `22d175af0bff31ece9f53cf9b896ae36def748a107b432280dfcecce56e75875` |
| SEARCH_DEV | 8,401 | 1,135 | `d004798e6b623a50c38b33631a2bf8bd54ba2c92d3bf17513d5f06cc6c62c11c` |

A complete split-integrity audit reports:
- case-ID overlap: **0**;
- molecule-group overlap: **0**;
- 2D identity: first 14 characters of the RDKit InChIKey;
- official VAL/TEST used: **false**.

Artifact:
`orbit-ms/docs/results/pr90_search_dev_disjointness_20261006.json`

Relevant PR90 commit:
`952a914d` — *Verify full SEARCH_DEV disjointness by 2D molecular identity*.

**Evidence class: A.**

---

# 2. Direct molecular-formula inference is already strong without molecular fingerprints

This is currently the cleanest completed component result in the new chemical-evidence pipeline.

## 2.1 Code and model version

Repository: `wangyu-sd/orbit-ms`  
PR: #90  
Direct-formula source commit: `baa6870471a4eeed759b948783b0338e797c9ca8`  
Full result archive commit: `bba4734c`  
Checkpoint SHA-256:  
`b730da4a35d49785f825afc3a6ddac89d668a512d8dcda1ac9110cbca1040eb5`

Principal code:
- `src/orbit_ms/wgv/direct_formula_posterior.py`
- `scripts/train_pr90_direct_formula.py`
- `scripts/eval_pr90_direct_formula_search_dev.py`

Result:
- `docs/results/pr90_direct_formula_full_search_dev_20261006.json`

Inputs are direct observables only:
- precursor m/z;
- adduct;
- measured peak m/z and intensity;
- collision energy;
- instrument encoding.

No molecular fingerprint is an input, target or intermediate representation.

## 2.2 Full 8,401-spectrum SEARCH_DEV result

| Stratum | Cases | Top1 | Top5 | Top8 | Top16 |
|---|---:|---:|---:|---:|---:|
| All | 8,401 | **87.87%** | **96.64%** | 97.50% | **98.44%** |
| [M+H]+ | 7,429 | 89.45% | 97.47% | 98.17% | 98.84% |
| [M+Na]+ | 972 | 75.82% | 90.33% | 92.39% | 95.37% |
| Sulfur-containing | 1,183 | 76.08% | 90.70% | 91.72% | 92.39% |
| Halogen-containing | 1,037 | 73.38% | 93.92% | 95.47% | 97.69% |
| Phosphorus-containing | 668 | **94.01%** | 98.65% | 99.10% | 99.55% |

Molecule-group-equal Top1:
- all: **86.50%**;
- [M+H]+: **86.17%**;
- [M+Na]+: **80.96%**.

Calibration:
- case-weighted Top1 accuracy: **87.87%**;
- mean Top1 posterior: **93.45%**;
- 10-bin ECE: **5.58%**;
- [M+Na]+ ECE: **11.83%**.

There are 888 cases where the correct formula is ranks 2–16. The median posterior assigned to the correct formula in these cases is 5.67%; for the 190 sodium cases in this group the median is only 1.38%.

### Nature-level interpretation

The data support:

> **For the great majority of molecule-disjoint spectra, precursor composition can be recovered among a compact hypothesis set without a molecular-fingerprint bridge. The principal unsolved problem is therefore not simply formula enumeration.**

Do not claim that formula inference is solved universally: sodium, sulfur and halogen strata remain materially weaker and the posterior is overconfident.

**Evidence class: A. Candidate for main Figure 1/2 or the first Results section.**

---

# 3. Formula support does not imply structural support

## 3.1 Fingerprint-free current entry audit

Using the frozen direct-formula Top16 and the TRAIN-only formula structural prior:

| Necessary condition | Cases / 8,401 |
|---|---:|
| True precursor formula in direct posterior Top16 | **8,270 (98.44%)** |
| True formula Top16 and at least one TRAIN structural seed with that formula | **5,752 (68.47%)** |
| True formula Top16 but no TRAIN structural seed for that formula | **2,518 (29.97%)** |
| True formula outside Top16 | 131 (1.56%) |
| No structural seed for any predicted Top16 formula | **1,682 (20.02%)** |

Because the current local G preserves formula and requires a starting molecular graph, at least **2,649/8,401 = 31.53%** of SEARCH_DEV cases are unreachable through that entry route irrespective of W/V ranking quality.

Artifact:
`orbit-ms/docs/results/PR90_FORMULA_SEED_BOTTLENECK_20261006.md`

Current associated implementation/result line was archived during PR90's chemical-evidence chain (around commits `05f94af5` / `d50f1a7f`).

### Nature-level interpretation

> **High formula recall does not solve de novo structure elucidation: a second bottleneck appears before topology repair even begins, because a formula-compatible molecular state is often absent from the structural entry prior.**

This is a necessary-condition/entry analysis, not end-to-end accuracy.

**Evidence class: A/B. Main-text decomposition is appropriate; detailed prior mechanics belong in Extended Data.**

---

# 4. Historical full-population evidence identifies topology as the dominant inverse bottleneck

The following analysis comes from the PR87 generator route. It is complete and highly informative, but the historical generator/candidate route is not the final fingerprint-free architecture. Use it as a problem diagnosis, not as the final method's performance.

## 4.1 Same-formula topology gap

Repository: `orbit-ms`  
PR: #87  
Archive commit: `5efdbef3` — *Audit full G0 formula to structure gap without MCES*  
Analysis:
- `docs/research/PR87_G0_SAME_FORMULA_STRUCTURE_GAP_20261004.md`
- `docs/results/pr87_vg_autoresearch_20261001/g0_same_formula_structure_gap_full_20261004.json.gz`

Full SEARCH_DEV:

| Quantity | Cases |
|---|---:|
| spectra | 8,401 |
| target formula sampled | 7,829 |
| at least one emitted candidate with target formula | **7,822 (93.11%)** |
| target connectivity in emitted candidates | **528 (6.28%)** |
| correct-formula candidate present but exact topology absent | **7,294** |

Conditional exact-connectivity reach given at least one same-formula candidate:

**528 / 7,822 = 6.75%.**

For structures with at least 20 heavy atoms:
- same-formula candidate present: 5,064;
- exact target connectivity present: 41;
- conditional reach: **0.81%**.

### Interpretation

This is strong empirical evidence that:
- elemental composition and exact connectivity are very different inference problems;
- large-molecule topology is particularly difficult;
- improving formula validity alone cannot close the gap.

**Evidence class: B / strong mechanism result.**  
For the final Nature manuscript, preferably pair this with the new fingerprint-free formula result rather than presenting the old G0 route as the final method.

---

# 5. The old monotone inverse action space is structurally incapable of repairing most same-formula errors

Repository: `orbit-ms`  
PR: #87

Key commits:
- `cf7f6317` — *Audit full-formula inverse G monotone edit reachability*
- `2c96bc3` — *Report full target-blind G0 nonmonotone edit reach*

Artifact:
`docs/research/PR87_MONOTONE_FULL_SEED_ACTION_GAP_20261004.md`

## 5.1 Target-blind full-seed necessary-condition audit

Among 8,401 SEARCH_DEV cases:

| Top-ranked seed state | Cases |
|---|---:|
| no valid seed | 8 |
| already target connectivity | 235 |
| wrong formula | 2,337 |
| correct formula, wrong connectivity | **5,821** |
| of those, provably unreachable under monotone full-seed edits | **5,732 (98.47%)** |
| undecided by the necessary-condition proof | 89 |

The 5,732 provably unreachable cases span 866 molecule groups.

The reason is structural: after loading a complete same-formula molecular graph, the old action vocabulary could add/connect/increase but could not remove or relocate existing heavy-atom connectivity when no heavy atoms remained to add.

## 5.2 One-round non-monotone diagnostic

Using a frozen target-blind seed and one round of explicit non-monotone edits:
- seed itself hits target: 235 cases;
- seed + one edit round: 431;
- newly recovered beyond seed: 196;
- original independent G0 100-draw pool: 528;
- additive union: 662.

This proves that non-monotone operations repair real errors, but a single random local-edit round remains far from sufficient.

### Nature-level interpretation

> **The need for topology-revising operations is not an architectural preference; it follows from a reachability failure of monotone complete-graph editing.**

**Evidence class: A/B. Strong method motivation; full operator details in Extended Data.**

---

# 6. A forward fragmentation World contains real spectrum-specific structural information

This is the strongest completed evidence supporting the central World concept. Two versions are retained below.

## 6.1 Fixed candidate causal test on full SEARCH_DEV

Repository: `orbit-ms`  
PR: #87  
Result commit: `31bfe061` — *Archive full official FP20 W/V result and paired decision*

World checkpoint SHA-256:
`df10668b0cc78ba9a0f5cc12171abea43d33f48cdde4a8c6b15b32ae1de26d14`

Artifacts:
- `docs/research/PR87_OFFICIAL_FP20_WV_FULL_DECISION_20261004.md`
- `docs/results/pr87_vg_autoresearch_20261001/official_fp20_wv_independent_analysis_20261004.json`
- `docs/results/pr87_vg_autoresearch_20261001/official_fp20_wv_paired_analysis_20261004.json`

Population:
- 8,401 spectra;
- 1,135 molecule groups;
- candidate IDs fixed between matched and fixed-precursor peer arms;
- target connectivity present in 4,672/8,401 candidate pools (55.61%).

Ranking:

| Fixed pool ranker | Matched Top1 | Matched Top10 | Peer Top1 |
|---|---:|---:|---:|
| raw historical proposal score | 1,710 | 3,773 | 342 |
| proposal after W-scorability control | 1,974 | 4,019 | 410 |
| **forward World evidence** | **2,509 (29.87%)** | **4,418 (52.59%)** | **239** |
| old V molecule evidence | 2,567 | 4,374 | 443 |

The relevant controlled World effect is W versus the W-scorable proposal baseline:

- case-weighted Top1 gain: +6.37 percentage points;
- **molecule-group macro Top1 gain: +14.78 pp**;
- 4,000-bootstrap 95% CI: **[+12.58, +16.91] pp**;
- **matched-minus-peer group-macro Top1 gain: +15.18 pp**;
- 95% CI: **[+13.02, +17.39] pp**.

The old V does **not** improve on W under the group-aware control:
- V minus W group-macro Top1: **−0.96 pp**;
- 95% CI: **[−1.81, −0.15] pp**.

### Interpretation

This supports a central claim:

> **Forward fragmentation evidence makes spectrum-specific structural decisions on an identical candidate set.**

Important boundary: the candidate pool itself came from a historical fingerprint-based proposal route. Therefore this experiment is a causal test of World evidence, not a clean final de novo benchmark.

**Evidence class: A for the World causal mechanism; C for final de novo performance.**

---

# 7. Cleaner open-prior evidence: mass-only PubChem candidates + World ranking

This is preferable when the manuscript needs a fingerprint-free practical ranking example.

Repository: `orbit-ms`  
PR: #87  
Result archive commit: `436fe1bc` — *Archive full SEARCH_DEV W V PubChem reranking result*

Artifacts:
- `docs/research/PR87_PUBCHEM_FULL_WV_INDEPENDENT_RESULT_20261004.md`
- `docs/results/pr87_vg_autoresearch_20261001/pubchem_full_wv_independent_analysis_20261003.json`

Setting:
- OPEN_PUBCHEM_PRIOR;
- target-blind fixed mass-window PubChem Top20;
- same candidate IDs under matched and fixed-precursor peer spectra;
- no G generation;
- no official VAL/TEST;
- no MCES.

Results:

| Fixed Top20 ranking | Matched Top1 | Matched Top10 | Peer Top1 | Peer Top10 |
|---|---:|---:|---:|---:|
| mass-only order | 306 | 1,991 | 306 | 1,991 |
| **World score** | **1,213** | **2,429** | **62** | 1,334 |
| old V molecule score | 1,221 | 2,473 | 327 | 1,568 |

Pool target connectivity reach:
**2,567 / 8,401 = 30.56%.**

Among reachable targets, W ranks:
**1,213 / 2,567 = 47.3%** first.

World molecule-group macro matched-minus-peer Top1 gain versus mass order:
**+7.67 pp**, 95% CI **[+6.33, +9.10] pp**.

### Nature-level interpretation

This is clean evidence that a forward World can convert a broad mass-compatible chemical prior into spectrum-specific structural discrimination.

It remains an open-prior setting, not closed-book de novo structure generation.

**Evidence class: A/B. Strong main/Extended-Data support for practical dark-metabolome ranking.**

---

# 8. Expanded open PubChem prior: proposal reach dominates even when W/V ranking is strong

Repository: `orbit-ms`  
PR: #87  
Top80 result commit: `7dc2ef06`  
Frozen rank-fusion archive: `30530435`

Artifacts:
- `docs/research/PR87_PUBCHEM_TOP80_WV_RESULT_20261004.md`
- `docs/results/pr87_vg_autoresearch_20261001/pubchem_full_wv_top80_independent_summary_20261004.json`
- `docs/results/pr87_vg_autoresearch_20261001/pubchem_top80_rank_fusion_independent_summary_20261004.json`

Pure W Top80:
- candidate pool connectivity reach: **4,858 / 8,401 = 57.83%**;
- World Top1: **1,199**;
- World Top10: **3,625**;
- peer Top1: **33**;
- World group-macro matched-minus-peer Top1 gain vs fixed hybrid order:
  **+14.85 pp [13.02,16.75]**.

The historical mass+FP+W+V RRF fusion reached:
- Top1 **2,191/8,401 = 26.08%**;
- Top10 4,168.

However, this fusion uses molecular-fingerprint retrieval and is **not allowed in the current canonical de novo method**.

The scientifically useful conclusion is the proposal ceiling:
- 3,543 targets are absent from the Top80 connectivity pool;
- among the 4,858 reachable cases, the historical fusion put 4,168 (85.8%) in Top10 but only 2,191 (45.1%) at Top1.

**Evidence class:**
- pure World/open-prior reach: B;
- fingerprint-fused headline numbers: C / historical only.

---

# 9. Historical closed-book de novo baselines and proposal-scaling headroom

These are useful to quantify how difficult the inverse task is, but they are not the final canonical method because the historical candidate route predates the no-fingerprint project invariant.

## 9.1 Frozen historical fair-budget baseline

Result:
`docs/results/pr87_vg_autoresearch_20261001/g_fixed_pool_mass_full_result_20261002.json`

Version:
- worker source commit: `10b8c98f4ca1425d0aaafabf0ce59cee7041b454`;
- merger commit: `968723a39ea355ae31099b1ed12aa340ff682daa`;
- G checkpoint SHA-256:
  `8d8fdf605219c567cfaf700c0d844a62b83c841327988faa1f529c6427fb6ef5`;
- 8×V100;
- no ground-truth formula;
- 100 terminal candidates;
- full 8,401 SEARCH_DEV.

Results:

| Metric | Result |
|---|---:|
| Exact@1 | **3.43%** |
| Exact@10 | **11.28%** |
| Reach@100 | **14.00%** |
| full-key Exact@1 | 2.49% |
| full-key Exact@10 | 8.55% |
| large-molecule Reach@100 | 5.65% |
| Morgan@1 | 0.3198 |
| best Morgan@10 | 0.4112 |

Matched-minus-peer Reach@100:
**+4.34 pp**, molecule-group bootstrap 95% CI **[+1.49,+7.78] pp**.

**Evidence class: C/B historical baseline.**

## 9.2 Over-budget exhaustive proposal diagnostic

Result:
`docs/results/pr87_vg_autoresearch_20261001/g_exhaustive_h_full_result_20261002.json`

Source commit:
`223979bb9855b03d816734a3e2079a7befba7c49`

All 8,401 SEARCH_DEV:
- H: exhaustive existing operator union;
- Na: unchanged native baseline;
- mean H candidate union: **2,761 unique connectivities/case**;
- explicitly marked `DIAGNOSTIC_ONLY_OVERBUDGET_NOT_G_CHAMPION`.

Results:

| Metric | Historical fair budget | Exhaustive diagnostic |
|---|---:|---:|
| Exact@1 | 3.43% | **4.71%** |
| Exact@10 | 11.28% | **17.21%** |
| Reach@100 | 14.00% | **21.91%** |

Group-macro Recall@100:
**7.03% → 12.64%**, gain **+5.61 pp**, 95% CI **[+4.41,+6.85] pp**.

Matched-minus-peer group-macro gain:
**+4.83 pp [3.58,+6.11]**.

Within the 7,429 H cases:
- target present in complete expanded pool: 2,070;
- target in Top100: 1,801;
- target present but below Top100: 269;
- **target absent from complete existing-operator union: 5,359**.

### Interpretation

Increasing compute substantially raises proposal recall, but the majority of structures remain outside the existing operator-generated support. Search scaling alone does not solve the structural problem.

**Evidence class: B. Excellent headroom/limitation figure; never report as matched-budget SOTA.**

---

# 10. G90 non-monotone editor: complete negative result and failure decomposition

Repository: `orbit-ms`  
PR: #90  
Frozen source commit:
`ebbcdbe9e920e1dc655d68c644937ab77c01c734`

Task:
`pr90_topology_editor_search_dev_8v100_20261005_063616`

Full independent analysis SHA-256:
`6742d4f225de41a47874862257dce08a125423da9e93e391bb2464fd1f898316`

Artifacts:
- `docs/results/pr90_g90_full_search_dev_20261005.md`
- `docs/results/pr90_g90_bad_case_analysis_20261005.md`
- `docs/results/pr90_g90_formula_bottleneck_20261005.json`

Protocol:
- no supplied GT formula;
- 16 formula-diversified seeds;
- two edit depths;
- beam 16;
- three attempts per operator/parent;
- terminal Top100 unique connectivities;
- all 8,401 SEARCH_DEV cases.

## 10.1 End-to-end result

| Metric | Frozen historical baseline | G90 |
|---|---:|---:|
| Exact@1 | 288 / 8,401 = **3.43%** | 157 / 8,401 = **1.87%** |
| Exact@10 | 948 / 8,401 = **11.28%** | 787 / 8,401 = **9.37%** |
| Reach@100 | 1,176 / 8,401 = 14.00% | **1,317 / 8,401 = 15.68%** |

Thus G90 increases net proposal reach but substantially worsens terminal ranking.

Of the 288 historical baseline Top1 hits:
- 241 lose Top1;
- **240 of those correct structures remain somewhere in G90 Top100**.

This is direct evidence of a ranking/calibration failure, not merely a generation failure.

## 10.2 Exhaustive failure decomposition

The 8,401 cases partition exactly into:

| G90 outcome | Spectra |
|---|---:|
| exact target rank 1 | **157** |
| exact target ranks 2–100 | **1,160** |
| target absent, but correct formula/charge present | **3,881** |
| correct formula/charge absent | **3,203** |

Important subgroups:

| Subset | Reach@100 | Correct formula in Top100 |
|---|---:|---:|
| [M+H]+ | 17.1% | 64.7% |
| [M+Na]+ | 4.4% | 40.1% |
| ≤15 heavy atoms | **44.4%** | 74.5% |
| >30 heavy atoms | **7.4%** | 54.7% |
| acyclic | 28.2% | 74.6% |
| ≥5 rings | **4.3%** | 59.2% |
| halogen-containing | **2.4%** | **12.4%** |
| no halogen | 17.5% | 68.8% |
| sulfur-containing | 6.5% | 42.7% |

### Nature-level interpretation

This result is useful precisely because it localizes three separate scientific problems:
1. formula acquisition;
2. topology proposal;
3. global structural ranking.

It also motivated abandoning parent-conditioned latent-cosine ranking in favor of an explicit chemical evidence interface.

**Evidence class: B. Strong failure-analysis figure; not a final performance claim.**

---

# 11. Full-TRAIN chemical-evidence statistics supporting the new WGV design

Repository: `orbit-ms`  
PR: #90  
Chemical-statistics completion was archived around commit `dd1a4784`.

Artifact:
`docs/research/PR90_TRAIN_CHEMICAL_EVIDENCE_AUDIT_20261006.md`

Full TRAIN:
- 175,548 spectra;
- 20,430 molecule groups;
- 6,583,412 measured fragment peaks;
- 12,306 precursor formula classes;
- 3,539 formula classes containing at least two molecule groups;
- 5,394,703 fragment appearance-frequency rows;
- 6,401,647 peak-relation neutral-loss rows.

Under the present paired precursor-formula + H/Na ion-state ledger:
- **1,408,325 / 6,583,412 = 21.4%** of measured peaks have no mass-close supported subformula.

This number **must not be called a noise rate**. It is an out-of-model support rate; isotopes, alternative ion states, contaminants, rearrangements, mass error and missing chemistry can all contribute.

A deterministic 351-spectrum TRAIN sample showed:
- unsupported-peak median normalized intensity: 0.00204;
- supported-peak median normalized intensity: 0.01702.

This motivates an explicit learned out-of-model/noise state in V rather than hard deletion of unsupported peaks.

**Evidence class: B. Methods/Extended Data, not a headline result.**

---

# 12. Current fixed-three-cut World has a measurable representation/proposal gap

This is an engineering diagnosis, not a population result, but it is important for the next architecture.

Artifacts:
- `docs/results/pr90_world_proposal_gap_train30_20261006.json`
- `docs/results/pr90_world_cut_envelope_train30_20261006.json`

Deterministically selected 30 TRAIN spectra:
- 1,144 measured peaks.

| Fragment support surface | Strict peak hit | Intensity-weighted hit | High-intensity (≥0.1) hit |
|---|---:|---:|---:|
| learned World Top128 | 27.19% | 53.73% | 57.14% |
| deduplicated Top128 ion states | 30.86% | 55.44% | 59.29% |
| all valid current World variants | 34.00% | 56.16% | 60.00% |
| full ≤3-cut H/Na mass envelope | **53.32%** | **70.77%** | **78.57%** |

The gap from 34.00% to 53.32% indicates missing breakpoint/component proposals beyond simple terminal truncation. The remaining gap after exhaustive ≤3-cut enumeration indicates that the three-cut/H/Na representation itself does not cover all measured peaks.

Do not present these percentages as SEARCH_DEV or test performance.

**Evidence class: C/B engineering motivation only.**

---

# 13. Results that must NOT yet be used as manuscript endpoints

As of paper ledger date 2026-10-06, the following are not finished scientific results:

## Chemical V
An epoch-1 full-TRAIN receipt exists:
- structural-pair TRAIN win rate: 82.90%;
- matched-context peer TRAIN win rate: 78.70%;
- mean peak explained by World: 23.61%.

Artifact:
`docs/results/pr90_chemical_v_epoch1_interim_20261006.json`

These are TRAIN diagnostics only. **Do not put them into a Results table or abstract.**

## Residual-guided G
Implementation and feature-activation audits exist, but no completed full-TRAIN final checkpoint and no complete SEARCH_DEV end-to-end result were frozen at the time of this ledger.

## Closed chemical-evidence WGV
The runner exists, but the definitive 8,401-case Exact@1 / Exact@10 / Reach@100 result is not yet available in this snapshot.

## Official MassSpecGym held-out TEST
Not opened for the new final model.

## SOTA claim
Not authorized.

---

# 14. Recommended Nature Results architecture using only currently defensible evidence

This is not the final manuscript text. It is the evidence order that best supports a Nature-level argument.

## Result 1 — The inverse problem is not primarily formula identification

Primary numbers:
- direct formula Top1: **87.87%**;
- direct formula Top16: **98.44%**;
- fingerprint-free structural-entry support after Top16 formula recovery: **68.47%**;
- 29.97% have the true Top16 formula but no same-formula TRAIN structural seed.

Narrative:
MS/MS already contains sufficient information to narrow elemental composition strongly; the difficult step is converting that composition and fragment evidence into the correct connectivity.

Preferred main panel:
formula TopK recall + structural-entry funnel, with H/Na/rare-element strata.

## Result 2 — Connectivity is a separate and much harder structural inference problem

Use:
- historical full-population same-formula topology gap: 93.11% formula-candidate support versus 6.28% exact topology support;
- 98.47% monotone-unreachable target-blind same-formula seeds;
- G90 decomposition into ranking, topology and formula failures;
- strong size/ring dependence.

Narrative:
Exact topology failure is not adequately described as “the formula predictor failed” or “the ranker needs more capacity.” The topology space and action-space reachability are independently limiting.

## Result 3 — A forward fragmentation World supplies candidate-specific experimental evidence

Primary clean evidence:
- mass-only PubChem Top20:
  - mass-order Top1 306;
  - World Top1 1,213;
  - group-macro matched-minus-peer gain **+7.67 pp [6.33,9.10]**.

Secondary causal evidence:
- fixed historical FP20 identical pool:
  - World Top1 2,509/8,401;
  - W vs scorability-controlled proposal group-macro gain
    **+14.78 pp [12.58,16.91]**;
  - matched-minus-peer
    **+15.18 pp [13.02,17.39]**.

Narrative:
The World is useful because it changes structural decisions when and only when the measured spectrum is changed, under a fixed molecular candidate set.

## Result 4 — Search scaling reveals headroom but not a solution

Use:
- fair historical Reach@100: 14.00%;
- over-budget exhaustive Reach@100: 21.91%;
- Exact@10: 11.28% → 17.21%;
- 5,359/7,429 H targets remain absent even from the exhaustive existing-operator union.

Narrative:
More compute recovers additional hypotheses, but existing proposal operators leave most correct structures outside support. This motivates a new structure proposal mechanism rather than mere beam expansion.

## Result 5 — Final chemical-evidence WGV

**Currently pending. This is the decisive missing result.**

The final paper needs one frozen fingerprint-free WGV result with:
- Exact@1;
- Exact@10;
- Reach@100;
- target proposed before pruning;
- target retained after pruning;
- formula TopK;
- matched-vs-peer causal effect;
- H/Na;
- size/ring/rare-element strata;
- runtime/World calls;
- official held-out result after model freeze.

Do not fill this section from G90 or TRAIN metrics.

## Result 6 — Dark metabolome scale and biology

Still required for Nature:
- full dark-corpus denominator;
- structural evidence funnel;
- recurrent structural entities/families across independent datasets;
- near-known versus remote chemistry;
- biological-source organization;
- feature-versus-family biological reproducibility;
- orthogonal standard validation for selected anchors.

A Nature submission should not stop at benchmark improvement. The model results above establish the inference problem and the World evidence principle; the dark-metabolome discovery programme must provide the scientific consequence.

---

# 15. What belongs in the main paper versus Extended Data

## Main-text candidates now
1. Direct formula Top1/Top16 and subgroup behavior.
2. Formula-to-structure / structural-entry decomposition.
3. Monotone reachability failure as motivation for topology-revising inference.
4. Clean fixed-candidate World matched-vs-peer evidence.
5. One compact search-headroom analysis.
6. Final fingerprint-free WGV result when complete.
7. Dark-metabolome discovery and biological findings when complete.

## Extended Data
- complete formula calibration curves;
- all H/Na/S/P/halogen strata;
- detailed G90 failure cohorts;
- full candidate proposal/retention decomposition;
- historical G_BASE and exhaustive-search diagnostics;
- open-PubChem Top20/Top80 results;
- old V negative result;
- World representation/support diagnostics;
- TRAIN chemical-evidence statistics.

## Internal/historical only
- fingerprint-fused PubChem RRF headline numbers;
- training losses as scientific claims;
- 30-case World engineering percentages as population estimates;
- selected post-hoc examples presented as performance evidence;
- any official-SOTA wording before the frozen held-out run.

---

# 16. Result provenance index

| Result | orbit-ms code/result version | Primary artifact |
|---|---|---|
| split disjointness | PR90 `952a914d` | `docs/results/pr90_search_dev_disjointness_20261006.json` |
| direct formula | source `baa68704`, archived `bba4734c` | `docs/results/pr90_direct_formula_full_search_dev_20261006.json` |
| formula structural-entry gap | PR90 chemical-evidence chain | `docs/results/PR90_FORMULA_SEED_BOTTLENECK_20261006.md` |
| formula→topology gap | PR87 `5efdbef3` | `docs/research/PR87_G0_SAME_FORMULA_STRUCTURE_GAP_20261004.md` |
| monotone reachability | PR87 `cf7f6317`, `2c96bc3` | `docs/research/PR87_MONOTONE_FULL_SEED_ACTION_GAP_20261004.md` |
| fixed-pool World causal ranking | PR87 `31bfe061` | `docs/research/PR87_OFFICIAL_FP20_WV_FULL_DECISION_20261004.md` |
| mass-only PubChem Top20 W/V | PR87 `436fe1bc` | `docs/research/PR87_PUBCHEM_FULL_WV_INDEPENDENT_RESULT_20261004.md` |
| PubChem Top80 W/V | PR87 `7dc2ef06` | `docs/research/PR87_PUBCHEM_TOP80_WV_RESULT_20261004.md` |
| historical fair-budget G | worker `10b8c98f`, merger `968723a3` | `docs/results/pr87_vg_autoresearch_20261001/g_fixed_pool_mass_full_result_20261002.json` |
| exhaustive proposal diagnostic | source `223979bb` | `docs/results/pr87_vg_autoresearch_20261001/g_exhaustive_h_full_result_20261002.json` |
| G90 full failure result | PR90 source `ebbcdbe9` | `docs/results/pr90_g90_full_search_dev_20261005.md` |
| chemical-evidence TRAIN audit | PR90 ~`dd1a4784` | `docs/research/PR90_TRAIN_CHEMICAL_EVIDENCE_AUDIT_20261006.md` |
| three-cut World support diagnosis | current PR90 engineering audit | `docs/results/pr90_world_proposal_gap_train30_20261006.json` |

---

# 17. Nature-level claim discipline

The following language is supported now:
- “precursor formula can be recovered at high TopK rate on a molecule-disjoint development population”;
- “exact topology remains the dominant unresolved step”;
- “a forward fragmentation World provides spectrum-specific candidate discrimination under fixed molecular candidate sets”;
- “current molecular proposal spaces impose independent structural reach ceilings”;
- “non-monotone topology revision is necessary for most complete same-formula wrong structures.”

The following language is **not yet supported**:
- “ORBIT-MS solves de novo structure elucidation”;
- “ORBIT-MS is SOTA on MassSpecGym”;
- “the final WGV improves Exact@1”;
- “the World mechanistically explains all measured peaks”;
- “dark metabolites are newly discovered”;
- “biological source or biosynthesis is established from model predictions alone.”

For Nature, the model is only the enabling half of the paper. The submission-level story requires a second half in which a frozen, validated inference system turns previously dark spectra into reproducible chemical entities/families and exposes biological organization that anonymous-feature metabolomics could not reveal.

---

# 18. Immediate manuscript implications

1. **Do not retain old Exact@1 = 1.559% / Exact@10 = 4.404% prose in `main.tex` as the authoritative inverse result.** It is superseded by later development evidence and does not reflect the final planned method.
2. Do not make the fingerprint-fused Top80 26.08% a headline result.
3. Figure 1 for a Nature submission should be result-led. The first quantitative message should be the formula/topology separation and/or a clean World discrimination effect, not a large architecture diagram.
4. The final chemical-evidence WGV result should replace historical G90/G_BASE numbers in the main inverse-performance panel once frozen.
5. Dark-metabolome scale, recurrence, biological organization and orthogonal validation remain mandatory submission gates, not optional applications.
