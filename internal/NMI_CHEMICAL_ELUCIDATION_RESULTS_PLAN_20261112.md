# ORBIT-MS NMI chemical-elucidation manuscript and experimental results plan

**Date:** 2026-11-12  
**Active draft:** `main.tex` on branch `paper/nmi-dark-chemical-elucidation-20261112`.  
**This proposal supersedes the six-main-figure, biology-heavy Nature outline for the current NMI draft.** Earlier nature/discovery plans remain historical context, not the figure contract for this branch.

## Scientific proposition

**Recover structural information and chemical relationships from experimental tandem spectra that conventional reference libraries leave unannotated, and use agent-directed recursive self-improvement (RSI) to extend the molecular structures that can be resolved.**

Two contributions must remain visible: (i) a source-linked dark-MS/MS structural resource containing calibrated resolution levels and chemically interpretable family relationships; and (ii) **an agent-directed, experience-driven RSI process** that identifies what WGV cannot yet generate or distinguish, chooses a targeted learning intervention, and uses the measured result to improve both later WGV capability and the agent's subsequent choices. The decisive RSI outcome is *new recoverable chemistry*, not a generic Agent leaderboard. No disease mechanism, microbial biosynthesis or new compound identity is inferred without independent evidence.

**Working title:** ORBIT-MS: Self-improving molecular structure elucidation of metabolomic dark matter.

## Figure and Results contract

| Main result | Figure PDF | Primary scientific object | Already sourced | Critical new work |
| --- | --- | --- | --- | --- |
| R1. Structurally resolving the reference-unmatched metabolome | **Fig. 1: `figures/fig1_orbit_ms_method_overview.pdf` is the METHOD SCHEMATIC**, with resource statistics in Extended Data 1–3 and family landscape in Fig. 4 | Unique dark-spectral entities and calibrated structural-resolution tiers, introduced through the end-to-end WGV–RSI scientific workflow | PR94: 835,953 QC-eligible MS/MS queries; 613,331 without accepted library match; 2,255 recurrent *spectral* communities | Render real MS/MS and molecular example placements in Fig. 1; freeze entity definitions; report full-tier population counts and supported-family landscape in their dedicated result panels |
| R2. Fragment evidence enables molecular construction and discrimination | `figures/fig2_fragment_guided_elucidation.pdf` | Recovery of known molecular connectivity using observed fragmentation evidence | PR95/SI: MMA on/off known-formula CAL Exact@1 1.50/6.00%; fixed-pool G/WV 7.00/8.50%; NPLIB1 and CASMI external development | Final target-free full MassSpecGym TEST; source-linked representative fragment/structure panels; formula/isomer/known-formula evaluation strata |
| R3. **Agent-guided recursive self-improvement expands the recoverable chemical space** | `figures/fig3_recursive_recoverable_space.pdf` | Closed-loop scientific decisions, updated WGV chemical capability, accumulated experience and newly recovered molecular structures | PR95: MMA 4.23M -> 12.98M -> 31.11M entries and 10 historical engineering generations; PR96: bounded Scientific Improver and persistent episode memory (code, not measured autonomous gains) | Genuine 3-generation RSI trajectories with fresh FIT diagnosis each generation, action/reflection/memory lineage, source-linked new gains/losses, independent chemical-space transfer, matched fixed/scripted/no-memory controls |
| R4. Previously unresolved spectra reveal molecular-family relationships | `figures/fig4_molecular_family_relationships.pdf` | Real molecular graph relationships among recovered unknowns and known metabolites | Recurrent spectral communities only; no established graph-level families yet | Graph-supported family definitions, structure edit network and matched known-chemistry/proposal-prior controls; dated recognition evidence |
| R5. Independent spectral evidence supports molecular hypotheses | `figures/fig5_independent_chemical_evidence.pdf` | Independently corroborated precursor hypotheses and bounded ambiguities | Existing source identifiers, W/V evidence capability and available public references | Prespecified 5–10 promising chemical anchors, independently sourced MS/MS/multienergy/MSn where available, limited authentic-standard follow-up if feasible; record null/ambiguous cases |

## Figure 1 design authority: SCIENTIFIC PROBLEM → EXPLANATORY WGV MECHANISM → AGENTIC RSI

The owner explicitly fixes **Figure 1 as the ORBIT-MS scientific method overview**, not merely an architecture diagram. The complete **copy-ready 16:9 text-to-image prompt, source-case extraction specification and acceptance tests** are in [FIG1_IMAGEGEN_PROMPT_20261112.md](FIG1_IMAGEGEN_PROMPT_20261112.md).

**A diagram with four labelled boxes and no chemical example is not acceptable.** A reviewer must visually understand:

1. **Hypothesis-coverage problem:** measured MS/MS does not determine unique molecular connectivity; long atom-wise generation can miss correct complex graphs. The remedy is Peak-Ladder/Canonical Hybrid G with MMA atom/ring/motif building and chemical inventory constraints. Show a real stepwise partial-graph trajectory.
2. **Discriminative-evidence problem:** several same-formula generated connectivities may explain common peaks, and candidate reach does not equal correct rank. The remedy is candidate-conditioned spectrum-blind W structural fragment hypotheses plus V comparison to the actually measured MS/MS. Show two actual competing molecular graphs and a source-derived common-versus-specific fragment/peak comparison.
3. **Learning-capability problem:** recurring failure should trigger a targeted change rather than blind retraining. The remedy is Scientific Improver's TRAIN-only hypothesis → one typed MMA/G/V/evidence action → experiment → observed structural recovery/loss → memory-conditioned next action. Show separate return paths for the updated WGV chemistry and for the agent experience memory.
4. **Scientific payoff:** the system is designed to expand the **recoverable molecular structures and bounded chemical relationships in metabolomic dark matter**, not maximize the quantity of generated SMILES or LLM tool calls.

**One source-grounded molecular example must connect input spectrum, partial G graphs, at least two candidate graphs, W predicted fragments and V observed-peak evidence.** First search real source-linked PR95 traces; MassSpecGym 0002114 provides a documented historical isomer-repair example only if a real MS/MS and scoring trace can be recovered. Do not invent chemical structures, fragment-ion assignments, scores or RSI improvements.

**Layout:** top scientific ambiguity (~18% height); middle detailed G/W/V evidence reasoning (~47%); lower detailed agent-driven RSI (~35%). Panels a–e cover these levels; Figure 1's final figure is \`figures/fig1_orbit_ms_method_overview.pdf\`. If text-to-image model cannot draw exact 2D chemistry, use deliberate insertion slots, then composite actual RDKit SVGs and vector experimental stick spectra.


The owner explicitly fixes **Figure 1 as the ORBIT-MS method overview**. See [FIG1_IMAGEGEN_PROMPT_20261112.md](FIG1_IMAGEGEN_PROMPT_20261112.md) for the copy-ready text-to-image prompt and exact scientific layout.

- **a Experimental ambiguity:** one measured spectrum next to two verified same-composition, different-connectivity candidate graphs; no target graph supplied to inference.
- **b Generator G and MMA:** actual peak-select/grow partial-graph trajectory using atom/ring/motif actions to produce competing complete structures; solves candidate-space coverage.
- **c World W:** structure-conditioned, target-spectrum-blind structural fragment predictions for each competing graph, showing shared versus candidate-specific chemical possibilities.
- **d Verifier V and structural reporting:** align actual measured ions to W's candidate-specific predictions, distinguish common evidence from discriminating fragment support, produce ranking or bounded interpretation.
- **e Agentic RSI:** three distinct TRAIN FIT failure modes, one testable chemical hypothesis, one selected action, measured structural recovery and loss, two feedback paths (chemical capability versus agent experience memory) and next-generation inference.

Figure 1 is not the 613,331-query bar chart or a family-distance landscape. Those results remain part of the source-accounting Results section and Extended Data Fig. 1–3; graph-supported family chemistry is represented in Figure 4. The page must show the two-level process, not generic colored AI workflow cards.

**Figure 2 remains the chemistry/benchmark evidence figure. Figure 3 is the measured RSI result and agent-decision mechanism. Figures 4–5 cover chemical relationships and independent chemical evidence.** Do not repeat the entire high-level architecture in Figure 2.

## Priority sequence: chemistry-first evidence, method Fig. 1, efficient reuse of existing WGV

### Work package A — structurally interpretable dark-MS/MS collection (R1)
- Reuse verified PR94 UC/IBD200/VEO-IBD acquisitions and 613,331 reference-unmatched queries. Keep accession, scan, adduct, collision-energy and missing-source provenance.
- Deduplicate repeated measurements into explicitly defined entities; obtain representative spectra; retain all entities in the reported denominators.
- Rank inference candidates and their fragmentation support using a frozen WGV checkpoint and resource snapshot.
- Assign a calibrated output tier: putative unique 2D connectivity, bounded isomer set, shared core, formula/class or unresolved. Tier counts must describe *entities*, not raw scans or candidate-SMILES count.
- The 2,255 cross-study **spectral** communities are a discovery substrate, not 2,255 molecular families. Display negative network-topology null p=0.91 as applicable in the **source accounting/Extended Data**, not in Figure 1's method schematic.

### Work package B — chemical evidence and known-ground-truth validation (R2)
- Reuse full-TRAIN Peak-Ladder Canonical Hybrid, MMA and W/V checkpoints from PR95; do not rebuild a new model.
- Reproduce strict same-checkpoint MMA ablation, fixed candidate-pool G-only vs G+W/V, generated reach vs final Exact@1/10 and hard same-formula examples.
- Complete target-free MassSpecGym (17,556 spectra) with fixed parent checkpoint and report independent molecule groups, exact model version, formula recall, running cost, raw reach, Exact@1/10 and uncertainty.
- Run only the selected final version on available external NPLIB1/CASMI sets; earlier reported values are versioned historical references, not interchangeable with final release.
- Keep **known-formula** CAL200 and homology-**Macro-Core-assisted** recovery separate from native de novo inference.
- Select actual real spectra and molecular graphs (e.g. known benchmark macrolides) for explaining candidate-specific fragment evidence. These are *known benchmark examples*, not newly discovered metabolites.

### Work package C — Agent-directed recursive self-improvement for chemically recoverable space (R3)

**System-level RSI is the primary AI-method contribution, and chemical recovery is its scientific test.** Two recursions must both be visible:
- **Chemical capability recursion:** WGV failure evidence -> a bounded intervention on MMA, G or V -> new structural capabilities -> later WGV inference.
- **Scientific decision recursion:** a testable agent hypothesis -> intervention outcome -> reflection/memory ledger -> updated intervention choice next generation. This adapts decisions through experience; it does not claim weight-space fine-tuning of the underlying LLM.

**An autonomous generation contains all of the following measured steps:**
1. **Diagnose** using fresh TRAIN FIT WGV inference from the current generation. Distinguish true candidate absent (G/chemical coverage), reference reachable but misranked (V) and explanatory chemical-knowledge gaps; include real candidate scores and structurally interpretable failure examples.
2. **Hypothesize and act** with the PR96 Scientific Improver. Choose one of `EXPAND_KNOWLEDGE`, `IMPROVE_GENERATOR`, `IMPROVE_VERIFIER` or `COLLECT_EVIDENCE`. Record selected action, falsifiable expected change, supporting case IDs, reasoning and source inputs. Reuse existing PR95 actions, not new agent framework code. Keep W fixed for this controlled study.
3. **Evaluate and remember** the updated WGV on the same independent and frozen evaluation molecules, recording new correct structures, lost correct structures, changes in Reach and conditional ranking, model and knowledge checksums and actual compute. Promote only an evaluated improvement. Store a reflection and measured outcome in memory.
4. **Repeat** the sequence with the promoted state and *newly recomputed FIT diagnostics*; reusing Gen0 failure reports in Gen1/2 would not test adaptive RSI. The next decision receives previous episode history and can legitimately change its intervention.

**Minimum figure-worthy experiment (not a code-unit test):** one frozen Gen0 checkpoint, three completed sequential generations each for an agent-guided path, strongest fixed intervention and scripted failure routing, common compute limits and equivalent inference budgets. A no-memory agent arm tests the value of feedback to decision-making; it can be performed on matched decision states rather than retraining a second full model chain if measured consistently. Prefer multiple molecule-disjoint seeds/slices for group-level error bars, but never substitute tiny diagnostic subsets for the final structural outcome.

**Figure 3 panel design:**
- **3a:** small explanatory RSI circle, highlighting chemical-state update and agent-memory update as separate feedback paths;
- **3b (dominant):** cumulative *newly recovered true molecular identities* (and losses) per real generation, coupled to calibrated higher-resolution dark-spectral entities; use independent molecule IDs, not repeated spectra or memory count;
- **3c:** real spectrum -> competing graph hypothesis -> diagnosed error -> selected learning experience -> new predicted structure and discriminatory fragments, ideally transfer to a different molecule;
- **3d:** failure-type by action matrix, showing agent decision, prior memory, and observed chemical outcome;
- **3e:** Frozen WGV vs Best Fixed vs Scripted vs Full Agent; source-derived evaluation, real compute accounting and uncertainty.

**Required output artifacts:** complete per-episode decision/diagnosis/receipt and reflection memory, initial/promoted G/V/MMA hashes, same-group before/after predictions (not just accuracy aggregates), recovered/lost structure IDs, chemical-class stratification, independently supported dark-spectral resolution changes and final paired comparison.

Known existing data: PR95 resource expansion and the historical G/W/V generation history. At 2026-11-12, PR96 has the real cluster execution recipe and source implementation but **no completed autonomous multi-generation experimental results**. Keep this explicit until Figure 3 is generated from real runs. No large library-size number is a substitute for newly elucidated chemistry.

### Work package D — interpretable family chemistry (R4)
- Start with supported candidate connectivities or common cores from work package A; family graph nodes are proposed molecular entities, not scans.
- Use explicit, chemically valid atom/bond differences, traceable known-metabolite references and independently recurrent source spectra.
- Separate new-to-library, uncatalogued structural *relationship*, potentially unreported chemical *structure* and indeterminate. A structure predicted from an unmatched spectrum is not automatically new chemistry.
- Quantify distance to characterized metabolites against formula-, size-, scaffold-, source- and candidate-prior-matched controls.
- Choose 2–3 strong real family examples for manuscript visuals; do not invent reactions or structures.

### Work package E — independent chemical evidence (R5)
- Preselect around 5–10 candidate anchors by chemistry and evidence quality, not by biological phenotype.
- Compare actual separately sourced experimental spectra and matched precursor/adduct settings; use measured multiple collision energies or MSn ancestry where source-verified.
- Apply optional authentic-standard/coelution evidence only to experimentally accessible anchors (ideally a few), clearly separated from public library reference matching.
- Report confirmed, externally corroborated, bounded, contradicted and inaccessible outcomes. Preserve full candidate alternatives and provenance.

## Writing rules for this branch

1. Lead with dark-spectrum structural information, **but clearly identify Agent-directed RSI as the second core contribution** in the title, abstract, introduction, Result 3, discussion and graphical loop. Do not substitute an Agent leaderboard for chemical recovery.
2. In Methods, explicitly describe the scientific decision loop and its two recursions: structured failure packets -> one typed chemical intervention -> measured update -> persistent episode memory -> next-generation diagnosis/decision. Distinguish historical human/scripted development from actually measured autonomous Agent episodes.
3. Report historical real results with their setting, denominator and conditional formula access. Never substitute CAL, sampled TEST or fixed-pool retrieval for full target-free test performance.
4. Use real RDKit molecular drawings and measured spectra in final figures; never stylized substitute data. For **Figure 1**, use the image-generation prompt only for compositional exploration and rebuild the final framework in editable vector graphics with real chemistry.
5. Every positive chemical-discovery or completed RSI improvement claim in `main.tex` without source evidence has an explicit `\\result{...}` placeholder. Replace only with source-derived data.
6. The old `internal/FIGURE_PLAN.md` and `internal/CLAIM_EVIDENCE_MATRIX.md` describe an earlier Nature six-figure, biology-dependent proposal. They are archived research context; this document defines the current NMI manuscript's five-figure contract.

## Reproducibility map

- **WGV development experiments, chemistry/model code:** [orbit-ms PR95](https://github.com/wangyu-sd/orbit-ms/pull/95).
- **Scientific Improver implementation:** [orbit-ms PR96](https://github.com/wangyu-sd/orbit-ms/pull/96).
- **Dark-source inventory and recurrence:** [orbit-ms PR94](https://github.com/wangyu-sd/orbit-ms/pull/94).
- **Supplementary sourced historical tables:** `supplementary/ORBIT_WGV_RSI_Results.tex` and `supplementary/MassSpecGym_Development_Results.tex`.
- **Current main manuscript:** `main.tex` on this branch; Figure 1 revised to `fig:orbit_method` and `figures/fig1_orbit_ms_method_overview.pdf`.

Do not add speculative biological phenotype, tissue, microbial pathway or diet intervention panels to the present five main figures. Those are possible future applications, not required scientific evidence for this chemical-elucidation study.
