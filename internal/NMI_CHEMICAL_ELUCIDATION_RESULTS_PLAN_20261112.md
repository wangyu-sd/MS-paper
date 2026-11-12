# ORBIT-MS NMI chemical-elucidation manuscript and experimental results plan

**Date:** 2026-11-12  
**Active draft:** `main.tex` on branch `paper/nmi-dark-chemical-elucidation-20261112`.  
**This proposal supersedes the six-main-figure, biology-heavy Nature outline for the current NMI draft.** Earlier nature/discovery plans remain historical context, not the figure contract for this branch.

## Scientific proposition

**Recover structural information and chemical relationships from experimental tandem spectra that conventional reference libraries leave unannotated, and measure whether evolving fragment-informed inference expands what can be resolved.**

Primary scientific output: a source-linked dark-MS/MS structural resource, calibrated structure-resolution assignments, structure-supported molecular-family relationships, and independent experimental spectral corroboration. No disease mechanism, microbial biosynthesis or new compound identity is claimed without suitable chemistry. Agentic RSI is an enabling strategy, not the primary result object.

**Working title:** ORBIT-MS: Evidence-guided molecular structure elucidation of metabolomic dark matter.

## Figure and Results contract

| Main result | Figure PDF | Primary scientific object | Already sourced | Critical new work |
| --- | --- | --- | --- | --- |
| R1. Structurally resolving the reference-unmatched metabolome | `figures/fig1_dark_structure_landscape.pdf` | Unique dark-spectral entities and calibrated structural-resolution tiers | PR94: 835,953 QC-eligible MS/MS queries; 613,331 without accepted library match; 2,255 recurrent *spectral* communities | Freeze spectral-entity definition; run WGV on source-linked representative spectra; produce all-tier population counts and a supported-family landscape |
| R2. Fragment evidence enables molecular construction and discrimination | `figures/fig2_fragment_guided_elucidation.pdf` | Recovery of known molecular connectivity using observed fragmentation evidence | PR95/SI: MMA on/off known-formula CAL Exact@1 1.50/6.00%; fixed-pool G/WV 7.00/8.50%; NPLIB1 and CASMI external development | Final target-free full MassSpecGym TEST; source-linked representative fragment/structure panels; formula/isomer/known-formula evaluation strata |
| R3. Recursive learning expands the recoverable chemical space | `figures/fig3_recursive_recoverable_space.pdf` | Previously unsuccessful molecules newly recovered; dark spectra promoted to higher justified resolution | PR95: MMA 4.23M -> 12.98M -> 31.11M entries and 10 historical engineering generations; PR96: bounded episode controller (code, not a completed experiment) | Measured before/after per-case transitions, 2–3 or more real learning generations, new gains/losses, cross-structure reuse and matched fixed/scripted comparison |
| R4. Previously unresolved spectra reveal molecular-family relationships | `figures/fig4_molecular_family_relationships.pdf` | Real molecular graph relationships among recovered unknowns and known metabolites | Recurrent spectral communities only; no established graph-level families yet | Graph-supported family definitions, structure edit network and matched known-chemistry/proposal-prior controls; dated recognition evidence |
| R5. Independent spectral evidence supports molecular hypotheses | `figures/fig5_independent_chemical_evidence.pdf` | Independently corroborated precursor hypotheses and bounded ambiguities | Existing source identifiers, W/V evidence capability and available public references | Prespecified 5–10 promising chemical anchors, independently sourced MS/MS/multienergy/MSn where available, limited authentic-standard follow-up if feasible; record null/ambiguous cases |

## Priority sequence: discovery first, efficient reuse of existing WGV

### Work package A — structurally interpretable dark-MS/MS collection (R1)
- Reuse verified PR94 UC/IBD200/VEO-IBD acquisitions and 613,331 reference-unmatched queries. Keep accession, scan, adduct, collision-energy and missing-source provenance.
- Deduplicate repeated measurements into explicitly defined entities; obtain representative spectra; retain all entities in the reported denominators.
- Rank inference candidates and their fragmentation support using a frozen WGV checkpoint and resource snapshot.
- Assign a calibrated output tier: putative unique 2D connectivity, bounded isomer set, shared core, formula/class or unresolved. Tier counts must describe *entities*, not raw scans or candidate-SMILES count.
- The 2,255 cross-study **spectral** communities are a discovery substrate, not 2,255 molecular families. Display negative network-topology null p=0.91 as applicable.

### Work package B — chemical evidence and known-ground-truth validation (R2)
- Reuse full-TRAIN Peak-Ladder Canonical Hybrid, MMA and W/V checkpoints from PR95; do not rebuild a new model.
- Reproduce strict same-checkpoint MMA ablation, fixed candidate-pool G-only vs G+W/V, generated reach vs final Exact@1/10 and hard same-formula examples.
- Complete target-free MassSpecGym (17,556 spectra) with fixed parent checkpoint and report independent molecule groups, exact model version, formula recall, running cost, raw reach, Exact@1/10 and uncertainty.
- Run only the selected final version on available external NPLIB1/CASMI sets; earlier reported values are versioned historical references, not interchangeable with final release.
- Keep **known-formula** CAL200 and homology-**Macro-Core-assisted** recovery separate from native de novo inference.
- Select actual real spectra and molecular graphs (e.g. known benchmark macrolides) for explaining candidate-specific fragment evidence. These are *known benchmark examples*, not newly discovered metabolites.

### Work package C — growth of recoverable chemistry (R3)
- First measure a complete Gen0 failure decomposition using the same molecules and spectra: true formula absent, true structure not generated, correct structure present but misranked, and correctly resolved.
- Reuse PR96 scientific controller with frozen W and existing interventions `EXPAND_KNOWLEDGE`, `IMPROVE_GENERATOR`, `IMPROVE_VERIFIER`; avoid new agent framework or separate learning model.
- Run real bounded interventions and frozen paired evaluations. Track **newly correct**, **previously correct lost**, Reach improvement, ranking-only recovery, molecular-class/scaffold transfer and per-update resource cost. An update of library size with no new structure recovery is not a positive scientific endpoint.
- Demonstrate that a few source-linked dark-spectral entities gain more defensible structural resolution as the capability matures; avoid declaring a unique structure solely from increased model confidence.
- Matched fixed and scripted controls support RSI mechanism in Extended Data; main figure foregrounds recoverable chemical-space gain.
- At 2026-11-12, PR96 has code and recipe but no verified completed autonomous Taiji episode. Do not insert numerical agent gains as measured results.

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

1. Lead with dark-spectrum structural information, not an Agent leaderboard and not disease/perturbation analysis.
2. In Methods, describe WGV, MMA, Canonical Hybrid, homology-assisted Macro-Core and Scientific Improver without claiming all variants were jointly evaluated in one experiment.
3. Report historical real results with their setting, denominator and conditional formula access. Never substitute CAL, sampled TEST or fixed-pool retrieval for full target-free test performance.
4. Use real RDKit molecular drawings and measured spectra in final figures; never stylized substitute data.
5. Every positive discovery sentence in `main.tex` without a completed source has an explicit `\\result{...}` placeholder. Replace only with source-derived data.
6. The old `internal/FIGURE_PLAN.md` and `internal/CLAIM_EVIDENCE_MATRIX.md` describe an earlier Nature six-figure, biology-dependent proposal. They are archived research context; this document defines the current NMI manuscript's five-figure contract.

## Reproducibility map

- **WGV development experiments, chemistry/model code:** [orbit-ms PR95](https://github.com/wangyu-sd/orbit-ms/pull/95).
- **Scientific Improver implementation:** [orbit-ms PR96](https://github.com/wangyu-sd/orbit-ms/pull/96).
- **Dark-source inventory and recurrence:** [orbit-ms PR94](https://github.com/wangyu-sd/orbit-ms/pull/94).
- **Supplementary sourced historical tables:** `supplementary/ORBIT_WGV_RSI_Results.tex` and `supplementary/MassSpecGym_Development_Results.tex`.
- **Current main manuscript:** `main.tex` on this branch.

Do not add speculative biological phenotype, tissue, microbial pathway or diet intervention panels to the present five main figures. Those are possible future applications, not required scientific evidence for this chemical-elucidation study.
