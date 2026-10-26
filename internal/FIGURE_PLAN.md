# Proposed main-figure plan — discovery of previously unrecognized metabolite families

**Status: DESIGN PROPOSAL (2026-10-08). Not a report of completed discoveries.**

**Purpose:** This is the proposed figure plan for the Nature-oriented ORBIT-MS manuscript. It replaces the **figure planning document only**. It does not change `main.tex`, Supplementary Information, numerical results, the current model, or experimental thresholds. The former five-figure WGV-first plan is preserved in `internal/archive/FIGURE_PLAN_WGV_FIRST_20261006.md`. The authors should approve the figure direction before the manuscript is rewritten.

## What is the paper trying to establish?

**We develop a mass-spectral structure-inference approach and use it to discover and characterize metabolite families that were not previously recognized in large public metabolomics collections.**

The manuscript should lead with the **discovered families**, not the name of the algorithm, a benchmarking table, or the general existence of unannotated spectra. The method matters because it makes those family-level findings possible and testable.

Three claims must be kept distinct throughout:
- **Reference-unmatched spectra:** no accepted match in specified frozen reference spectra. This is not proof of a new metabolite.
- **Previously unrecognized molecular families:** a family supported by molecular evidence and independent observations, whose corresponding family-level relationship was not already catalogued in the frozen reference/literature search. This is the intended main discovery.
- **Previously unreported molecular structures:** a stronger assertion requiring structure-level novelty audit and orthogonal evidence; a model-generated SMILES alone cannot support it.

The intended argument is:

```text
Fig. 1  Which previously unrecognized metabolite families can be discovered?
Fig. 2  What are their structures and relationships to known metabolites?
Fig. 3  Why can we trust the structural statements and where is the limit?
Fig. 4  Where are the families found across biological samples/studies?
Fig. 5  Which families respond reproducibly to biological perturbations?
Fig. 6  Which discoveries survive independent chemical validation and change biological interpretation?
```

The figure order is a narrative hypothesis, not a demand to manufacture positive results. Do not write positive-result captions until the experiments succeed.

---

## Figure 1 | Previously unrecognized metabolite families in public tandem mass spectra

**Question:** Can the method identify meaningful, independently recurrent molecular families among public spectra that lack accepted library matches?

**Main impression:** Readers should first see **the families we have discovered**, not a large WGV diagram or a generic spectrum-count funnel.

### a. Public data and the unannotated subset (small)

**Visual:** A restrained horizontal count flow: public MS/MS records → usable/QC-passing spectra → accepted reference matches vs no accepted reference match. Alongside, a compact distribution of unmatched fractions under predeclared match/QC settings.

**Data:** Frozen accessions/source files, polarity and adduct, scan provenance, reference-library snapshot and search scores, exact eligibility denominator.

**Control:** Library score thresholds, duplicates, possible in-source/adduct/isotope artefacts where feature-level metadata permit. Do not call spectrum counts 'unique molecules'.

### b. What fraction can be described chemically? (small)

**Visual:** One population composition plot showing all eligible unmatched spectra partitioned into: unique putative 2D hypothesis / bounded isomers / shared core or chemical class / formula only / unresolved or out-of-support. A narrow inset gives empirical truth containment from a separate known-structure calibration sample.

**Data:** Frozen generator and evidence/checkpoint manifest; molecular identity groups; candidate-set membership and failure status.

**Control:** Retain all unresolved cases in the denominator. No family-level unique structure claim when only formula/class is supported.

### c. Large family-level landscape (dominant)

**Visual:** A wide 2D density/hexbin plus clearly marked independently recurrent structural families. x-axis: distance to a frozen characterized-metabolite reference (defined only for sufficient structural resolution); y-axis: number of independent studies/datasets supporting the family (log scale if needed). Dot size may encode number of structurally supported members. Label only a small, preselected set of families.

**Data:** One row per frozen family, not per spectrum; chemical-resolution level, independent study IDs, novelty distance with uncertainty/alternatives.

**Control:** Discovery data define the families; replication and biological labels do not influence family formation. Do not force 'near/remote' clouds through coloring or embedding. Family membership must not rely only on predicted graph similarity without support.

### d. Replication outside the discovery collection

**Visual:** Discovery→frozen-family→held-out search schematic plus a **distribution** for family replication under matched study/family permutations with the observed statistic indicated; optional compact point estimates of replication by discovery recurrence stratum.

**Data:** Independent accessions/repositories/laboratories, frozen family fingerprints/structural definitions, null replicates, uncertainty resampled at the family/study level as appropriate.

**Control:** No re-clustering or threshold adjustment in replication. De-duplicate redepositions and shared biological samples.

### e. What is truly unrecognized? (small)

**Visual:** Three-column family status composition: (i) previously catalogued/reference-supported relation, (ii) previously unrecognized relationship among known/proposed structures, (iii) potentially new structure/scaffold requiring validation. Include 'cannot determine' explicitly.

**Data:** Frozen GNPS/MassBank/MoNA/HMDB/reference-structure versions; literature and structural-neighbour audit; candidate resolution. Record reasons for uncertainty.

**Control:** 'No spectral library hit' is never equated with 'not previously discovered'.

### f. Representative families (narrow strip)

**Visual:** At most three families selected by a preregistered score combining structural support, independent recurrence and novelty. Show RDKit vector structures or **bounded core / isomer sets**, one actual spectrum per family, the number of independent studies, and their recognition status.

**Control:** Label proposed structures as hypotheses. Do not use fabricated structures/peaks or imply authentic-standard confirmation without it.

**Main claim if supported:** A measurable population of molecularly related, previously unrecognized families can be recovered from public data and independently observed elsewhere.

---

## Figure 2 | How the newly identified families relate to characterized metabolites

**Question:** Do the newly recovered families extend known chemistry in recognizable structural ways, or do they occupy distinct regions?

**Main impression:** A chemical relationship map with interpretable structure edits and rigorous null comparisons. Not another clustering figure.

### a. Structural relationships between known and previously unrecognized families (dominant)

**Visual:** A sparse, large network of measured/supported structures. Characterized/reference metabolites in neutral gray; supported but reference-unmatched families in muted navy; a limited second muted accent only for independently replicated, structurally distant families. Edges are **verified graph-level structural differences**, not just UMAP neighbours or m/z differences.

**Data:** Frozen reference structures, bounded sets when structures cannot be resolved uniquely, atom mapping / MCS / local graph changes, provenance of each link.

**Control:** A graph edit between two structures is not evidence of a biological conversion or of an enzyme.

### b. Distance to characterized metabolites

**Visual:** Real-family distribution of minimum valid graph-edit/path distance (1 / 2 / 3 / ≥4 / unconnected) beside structure/formula/size/source-matched nulls. Retain a separate 'insufficient resolution' group.

**Control:** Correct for the strong tendency of seed-based/retrieval-based generators to return structures near existing metabolites. The comparison must be conditioned on the same model proposal prior, candidate supply and chemical composition; otherwise 'near-known enrichment' is circular.

### c. Which structural differences recur across families?

**Visual:** Horizontal frequency distribution of explicitly defined graph changes (oxygen addition-like, degree of saturation, chain variation, group addition, ring edits, etc., only if actually resolved); include distribution of number of independent families/studies supporting each edit, with uncertainty/null.

**Control:** Class names describe structural differences, not confirmed reactions. Never label them 'enzyme transformations' without external evidence.

### d. Are similar structural differences found in distinct chemical classes?

**Visual:** A scaffold/class × graph-change heatmap of independent-family frequency or matched-null enrichment, with sample-size side strips. Classes should be defined independently of the reported recurrence effect.

**Control:** Match composition, scaffold size and prior/library coverage; show missing/uncertain class assignments rather than imputing them.

### e. Confirmation using records added to reference knowledge later

**Visual:** Historical T0 reference neighbours + frozen unannotated family assignments → subsequent T1 reference additions. Statistical comparison: observed future confirmed family relations vs matched branches/null, preferably an empirical effect-size distribution plus example pairs.

**Data:** True first-appearance dates and independent depositors, library snapshots, T0-only model/retrieval/training knowledge.

**Critical boundary:** A 2026 model trained on molecules/reference information from after T0 is NOT historically prospective merely because the spectral library is rolled back. If T0 model knowledge cannot be reconstructed, label the analysis as temporal external validation with its leakage boundary, or move it to Extended Data.

**Main claim if supported:** The previously unrecognized families occupy non-random chemical relationships to characterized metabolites, and some relations are corroborated independently.

---

## Figure 3 | How much structural information can the spectra actually support?

**Question:** Can spectrum-specific chemical evidence reduce incorrect molecular possibilities while retaining the true structure at a measured rate?

**Main impression:** Population statistics and uncertainty. NOT another case-study-centric model diagram or a SOTA leaderboard.

### a. Candidate-space reduction over the full known-structure evaluation population

**Visual:** 2D hexbin of initial plausible candidate count vs candidate count after frozen chemical-evidence filtering (log axes; diagonal is no reduction). Inset: distribution of retained-set size.

**Data:** Frozen candidate pools, ground-truth identity (for evaluation only), all failures including no proposal.

**Control:** No oracle-GT candidate insertion in native proposal-coverage claims.

### b. Performance across hard structural alternatives

**Visual:** Raincloud/box-plus-points distributions of retained candidate counts and GT containment separately for same formula, same scaffold, positional/regioisomers, high-similarity and controls.

**Control:** Candidate counts/difficulty and formula access matched among competing methods. Multiple spectra of one molecule are not independent N.

### c. Is the experimental spectrum doing the discrimination?

**Visual:** Paired matched-spectrum minus peer/shuffled-spectrum effect distribution, with a zero reference and molecule-group 95% CI; 'no spectrum / structural prior only' control. Avoid several visually identical violin panels.

**Control:** Fixed molecular candidate IDs and compute budgets across arms; preserve precursor/adduct compatibility of shuffled donors.

### d. What evidence is informative?

**Visual:** Population distribution of incremental false-candidate exclusion or ranking gain from shared/common peaks vs candidate-specific peaks vs formula/neutral-loss relations vs measured MSn ancestry (when genuinely observed). Ablate matched evidence mass/intensity budgets.

**Control:** Do not interpret 'unexplained by bounded World search' as chemically impossible. Distinguish weak/non-specific support from true contradiction.

### e. Reliability of the reported structural resolution

**Visual:** Point-and-interval estimates of known-GT containment for unique putative structure, bounded isomer set, shared core, formula/class, unresolved. Directly below, show the fraction of all evaluation cases receiving each report.

**Control:** Freeze calibration before this test; include group-level uncertainty and risk–coverage analysis. Use 'putative' until orthogonal confirmation. Rare-element/adduct subgroup reliability must be audited.

### f. Where are conclusions limited?

**Visual:** One population flow: formula unsupported → target absent from proposal pool → target proposed but ranked/pruned incorrectly → reliable bounded output / unresolved. Maintain mutually exclusive counts; do not call model failure 'intrinsic spectral ambiguity' without appropriate empirical proof.

### g. Limitations across molecule types

**Visual:** Horizontal 100% composition strips for molecule size, ring count, adduct and element strata, derived from (f); optionally a small 2D density for novelty vs resolution if support is adequate.

**Extended Data:** Full official MassSpecGym comparator table, benchmark SOTA/comparability decision, W/V/G architecture and learning curves; a single small real case is optional, not the main figure.

**Main claim if supported:** ORBIT yields empirically calibrated structural statements, including honest ambiguity/abstention, from specific measured spectra.

---

## Figure 4 | Where do the newly recovered molecular families occur?

**Question:** Are family distributions reproducible across biological sample types and independent cohorts?

### a. The available biological evidence base

**Visual:** Cohort × biological sample-type dot matrix; point size = biological sample count, grouped by study/repository. Show explicitly which contrasts have common protocols and usable metadata.

### b. Family distribution across sample contexts (dominant)

**Visual:** Frozen family × sample-context heatmap of **within-study estimated presence/enrichment effects**, combined only where designs are comparable. Common axes may include gut/faeces, plasma/serum, urine, tissue, microbial culture, food/environment when adequately represented.

**Control:** Do not compare raw intensity in gut studies with raw intensity in unrelated blood studies and call the difference tissue specificity.

### c. Are distributions context-associated?

**Visual:** Distribution of effect concentration/context specificity across real families versus metadata-shuffled null and matched known metabolites.

### d. Does an association replicate?

**Visual:** Discovery vs held-out cohort effect-size 2D density/hexbin, with 1:1 reference and confidence contours. Independence checked at cohort/subject level.

### e. Does direction recur across laboratories?

**Visual:** Distributions of cross-cohort sign agreement/replication fraction conditional on number of eligible studies, with permutation benchmark.

### f. Could acquisition technology explain the signal?

**Visual:** Unadjusted vs study/instrument/batch-adjusted effect density, complemented by sensitivity to study exclusion and detection-rate differences.

### g. Are chemically unusual families biologically distributed as well?

**Visual:** Family chemical-distance × replicated-context-effect 2D density, with insufficiently resolved families shown separately. No claim that distance implies function.

**Main claim if supported:** Some previously unrecognized molecular families exhibit reproducible biological distributions, beyond study and instrument effects.

---

## Figure 5 | Which families change with microbiota, diet or other perturbations?

**Question:** Do controlled comparisons connect selected families to reproducible biological changes?

### a. Perturbation dataset inventory

**Visual:** Small cohort/contrast coverage matrix: germ-free/conventional, antibiotic treatment, dietary intervention, microbial culture, genetics if validated and actually available.

### b. Benchmark the analysis with known metabolites

**Visual:** Distribution of positive-control effect recovery and label-permutation null under the identical analysis.

### c. Perturbation effects over families (dominant)

**Visual:** Forest/dot-and-CI distributions for predeclared family × intervention contrasts across studies; do not pool raw intensities from incompatible acquisition protocols.

### d. Cross-intervention consistency

**Visual:** Family × perturbation standardized-effect heatmap for adequately replicated studies, including mixed or null results.

### e. Does family-level analysis outperform isolated unidentified features?

**Visual:** Paired per-cohort/contrast distribution comparing anonymous-feature vs frozen-family replication rate, sign agreement or a preregistered primary endpoint using exactly the same biological samples and covariates.

### f. One carefully selected biology example (optional small panel)

**Visual:** A single family with independent perturbation effect replication, representative supported molecular structures, and explicitly bounded biological conclusion.

**Control:** Antibiotic/germ-free association supports 'microbiota-dependent', NOT microbial biosynthesis; food association does not itself prove dietary production or a pathway.

**Main claim if supported:** Previously unrecognized families are connected to reproducible biological perturbation effects, and family-level structure adds information beyond isolated peaks.

---

## Figure 6 | Independent chemical confirmation of the discovered families

**Question:** Are at least some of the newly reported chemical structures and family relationships true outside the inference system?

### a. Selection and full-denominator validation outcomes

**Visual:** Funnel/flow from preregistered high-priority families → accessible independent evidence/standards → confirmed / bounded / disproved / unavailable. Report failed anchors in the denominator.

### b. Authentic or independently measured reference evidence

**Visual:** Mirror MS/MS spectra, precursor/adduct evidence and, where genuinely available and comparable, RT/coelution and existing MSn/CCS. Clearly label external-library confirmation as different from same-lab authentic-standard confirmation.

### c. Chemical structure within validated families

**Visual:** RDKit structures or validated shared cores of family members; show actual observed differences and how many members are independently supported.

### d. Was this family already known?

**Visual:** Reference/literature/database audit by date for the validated family; distinguish 'new-to-this-library', 'previously unrecognized relationship', and 'previously unreported structure'. This may be a compact distribution, not a gallery of many cases.

### e. What difference does family identity make to biological inference?

**Visual:** Paired effect/replication comparison on identical cohorts for features vs experimentally supported family groupings, with uncertainty and negative results retained. If Figure 5e is strong, put its expanded confirmatory version here rather than repeat both.

### f. One decisive, deeply verified discovery (small)

**Visual:** One family linking chemical evidence, independent study recurrence, orthogonal validation and a replicated biological comparison; optionally one functional test only if actually performed.

**Main claim if supported:** Selected previously unrecognized metabolite families survive independent chemical validation and yield testable biological insight. Do not claim many structures are chemically confirmed if only a few representative anchors are confirmed.

---

## Dependencies and genuine stopping rules

- **Final model authority:** Use only a formally frozen configuration, after current model-development PRs finish, for any confirmatory paper analysis. The October 6 paper evidence ledger is a factual development summary, not a substitute for a final model release.
- **Calibration precedes family structure claims:** Include proposal failures and non-reportable outputs in denominators. Do not build the claimed 'new family' total from uncalibrated Top1 guesses.
- **Chemical relationships follow sufficient resolution:** If only a class/formula is supported, do not fabricate graph-edit distances or named transformations.
- **Independence:** Model evaluation = molecule group; family recurrence = study/sample provenance; biological inference = biological sample/subject.
- **No active new-MS3/CE programme:** Existing multispectral data may validate structural predictions, but this manuscript does not claim a newly executed active measurement.
- **Negative outcomes are informative:** If novelty vanishes after controlling for database/proposal bias, the claimed number of genuinely new families must decrease; if perturbation labels are confounded, the biological panel must become descriptive rather than causal.
- **Model method and benchmark in supporting figures:** The Figure 3 reliability analysis and compact benchmark table must establish capability without displacing the principal molecular-family discoveries.

## Visual style for all six figures

- Wide landscape composition; target width:height around **2.0–2.3:1** when panel content permits.
- White background, no rounded cards, drop shadows, colored containers, full-figure titles or bottom takeaway strips within image assets.
- Panel letters **a–g**; short panel labels only when essential. Captions belong in manuscript text.
- Black/gray plus **one muted navy** accent. A second very restrained muted rust may mark independently supported unusual chemistry in Figures 1–2 only, if scientifically needed.
- Use distributions, 2D densities, ECDFs, dot/interval plots, forest plots and heatmaps; avoid repeated line/violin plots or decorative Sankey charts.
- Real experimental spectra; RDKit SVG structures with readable atoms/bonds, correct aspect ratios and no fabricated chemistry.
- Matplotlib/Seaborn for quantitative panels. Source data and plot code must be reproducible. Every displayed number comes from a bound machine-readable result.

## Repository alignment

Current `main.tex` and `supplementary/Supplementary_Information.tex` still reflect an older **five-figure, WGV-first** narrative. This design PR deliberately does not rewrite those manuscripts. Do not interpret the current old Figure 1–5 macros as describing the newly proposed Figures 1–6. The current claim/evidence ledger remains the authority on completed PR85–PR90 measurements.

Once the design is approved, open a separate manuscript-alignment PR that changes Results headings, figure macros, captions, claim matrix/experiment plan, and references together. Do not partially rename figure numbers in one source file.
