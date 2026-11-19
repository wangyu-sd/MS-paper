# ORBIT-MS — five Results figures: production-ready panel map

**Paper-specific layout:** an introductory method overview figure (`figures/fig1_orbit_ms_method_framework.pdf`) already exists before Results. This document describes **five Results figure assets**, R1–R5, not necessarily printed Figure 1–5; final manuscript `\\ref{fig:...}` references control numbering. Keep established TeX captions and filenames intact.

**Art direction:** restrained white background, dark navy (#25465D), low-saturation teal (#397D83), graphite (#858B90). No rounded decoration, fake spectra, gradient fills, complex arrow networks or invented chemical diagrams. Use RDKit to render actual molecular structures, measured peaks with clear m/z axes, unambiguous denominator and controlled statistical plots. One dominant scientific panel per figure; relocate dense stratifications to Extended Data.

## R1 | Structurally resolving the reference-unmatched metabolome

**Asset:** `figures/fig1_dark_structure_landscape.pdf`. Emphasis: observable unassigned chemical space becomes a structured spectrum resource.

| Panel | Evidence to visualize | Design |
|---|---|---|
| a | three source studies; origin/accession, 835,953 eligible queries | compact data-source to scan diagram |
| b | 13,884 unambiguous accepted, 14,289 ambiguous accepted, 613,331 reference-unmatched, 194,449 unassessable | single horizontal distribution bar, exact counts |
| c | 2,255 recurrent spectral communities; 98 shared all three studies | clean study-recurrence / intersection panel |
| d | GeMS Tier A/B/C/D = 7/47/240/706 | tier bar + retained resolution labels |
| e | one source-linked experimental scan and chemical hypotheses | measured spectrum and real RDKit 2D structure |

**Strong Results message:** the public spectral dark matter is a large, traceable experimental population that supports progressively specific chemical structure hypotheses.

## R2 | Fragment evidence enables molecular construction and discrimination

**Asset:** `figures/fig2_fragment_guided_elucidation.pdf`. Emphasis: different chemical information solves candidate reach versus ranking.

| Panel | Evidence to visualize | Design |
|---|---|---|
| a | G, MMA motifs, W, V, experimental fragments | small evidence interface, reference already-existing method figure |
| b | formula Top1 87.87% and historical graph Reach 6.28% | short constraint-vs-connectivity comparison |
| c | strict MMA off/on Exact1 1.50→6.00%, Reach 6.50→19.00% | dominant paired improvement plot |
| d | fixed pool W/V (7→8.5%, 16 Reach) and MMA starts (5.5→10%, 19 Reach) | two paired comparisons |
| e | Canonical Hybrid CAL200 (12.50/21.50/22.50%) | inset metrics with same-denominator annotation |
| f | MassSpecGym pure partial-core + database setting, NPLIB1 (16.73/31.98%), CASMI (4.64/11.39%) | protocol-stratified benchmark comparison |
| g | H₀→H₁→H₂: Exact1 7.48→8.52→8.99% | small mechanistic step chart |
| h | genuine macrolide/alkaloid/peptide competing structures with exclusive ions and true measured spectrum | one enlarged chemical case narrative |

**Strong Results message:** mass-matched motifs increase constructible graphs while pairwise diagnostic fragmentation evidence resolves difficult competing connectivity hypotheses.

## R3 | Agent-guided recursive self-improvement expands recoverable chemical space

**Asset:** `figures/fig3_recursive_recoverable_space.pdf`. This is the flagship **long-term learning figure**, with the Gen trajectory visually dominant.

| Panel | Evidence to visualize | Design |
|---|---|---|
| a | MMA 4.23M → 12.98M → 31.11M and HMDB-W Sleep | compact knowledge growth |
| b | 17,556 full TEST: Gen0–19 Exact1, Exact10, Reach | **large line figure**, [actual SVG preview](../figures/previews/gen_curve_main.svg) |
| c | CAL200 per-episode Gen0–4 Exact1/Exact10/Reach and promotion | [evaluated model candidates & selection](../figures/previews/gen_curve_rsi.svg) |
| d | Two-Episode paired-only 15.67→17.35% and HMDB/COCONUT 17.58→19.01% | two paired deltas |
| e | +41 newly reached unique molecule groups; +201 spectra; 35 rank-one groups in latest pinned wave | group-level new recoveries with structures |
| f | real LLM Principal diagnosis, selected intervention, experiment receipt, experience memory | one chronological true episode trace, no abstract agent icons |

**Strong Results message:** repeated feedback first expands structural reach and later improves difficult isomer resolution; measured episodes govern promotion and subsequent decisions.

## R4 | Previously unresolved spectra reveal molecular-family relationships

**Asset:** `figures/fig4_molecular_family_relationships.pdf`. Emphasis: a concrete chemical graph rather than a generic UMAP.

| Panel | Evidence to visualize | Design |
|---|---|---|
| a | 294 higher-support GeMS candidate structures | selected RDKit graph/structure miniatures; evidence grades |
| b | six transformation-mass categories (68/30/23/18/16/13 edges) | horizontal bar; [data](../figures/data/gems_mass_deltas.csv) |
| c | 168 observed vs 43.04 ± 7.71 null edges, 3.90× | dot + uncertainty comparison |
| d | five application chemistry themes: host–microbe, ECM peptide, glutathione, lipids, exposome | 2–3 source-linked small molecule families |
| e | actual graph differences and their matched experimental fragments | structural alignment pair |

**Strong Results message:** inferred unknown chemistry exhibits interpretable, non-random candidate-structure relationships that are suitable for follow-up.

## R5 | Independent spectral evidence supports molecular hypotheses

**Asset:** `figures/fig5_independent_chemical_evidence.pdf`. Emphasis: experimentally supported specificity of final assignments.

| Panel | Evidence to visualize | Design |
|---|---|---|
| a | observed fragment set, ground-truth/alternative known case, candidate-specific diagnostic masses | mirror spectrum + two real molecules |
| b | 390 available H/Na dual-ion molecule groups and selected actual spectral views | available independent ion forms; do not invent convergence rate |
| c | 399 model-tie spectrum cases / 63.32% top-three local-bond similarity | bounded structural resolution |
| d | cLogP mean abs delta 0.6233 vs 0.6891 and TPSA 11.26 vs 13.41 Å² | two paired property bars |
| e | x independently corroborated dark-molecule anchors using experimental MS/MS, measured MSn, standards if available | measured spectra and explicit identified vs ambiguous structural outcomes |

**Strong Results message:** source-verified ion evidence supports defined levels of molecular structural resolution and enables external testing of promising unknowns.

## Extended Data and Supplementary architecture

| Slot | Existing experiments to retain in full |
|---|---|
| ED1 | Raw-source accession/USI audits, matching status and recurrence sensitivities |
| ED2 | Formula models, W fragment coverage, V conditioning, fixed-mass PubChem retrieval |
| ED3 | MMA, graph-edit, Canonical Hybrid, beam/cost ablations |
| ED4 | All ten full-population generalization axes / six superfamilies |
| ED5 | Full System vs strict partial-core vs external tests and published methods |
| ED6 | Full Gen archive, individual RSI promotion ledger, Sleep/Wake/Hindsight, LLM decisions |
| ED7 | GeMS tiers, chemical mass shift network and chemical-group case details |
| ED8 | H₁/H₂ tournament, equivalent candidate ties, H/Na, cLogP/TPSA |

**Immediate scientific materials required for final case panels:** actual query USIs, raw peak arrays, collision energy/adduct, original SMILES, W theoretical fragments, G candidate ranks, and per-Gen decision receipts. We should retrieve rather than redraw them from high-level report text. All quantitative panels are already prepared as CSV + plot script.
