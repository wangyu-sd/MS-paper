# Figure 1 | Text-to-image prompt and scientific production requirements

**Manuscript:** ORBIT-MS: Self-improving molecular structure elucidation of metabolomic dark matter  
**Figure title:** From reference-unmatched tandem spectra to a structurally interpretable dark-metabolome landscape  
**Figure contract:** \`main.tex\` → \`\\figureonetodo\` → panels **a–e**, label \`fig:dark_landscape\`.  
**Final PDF:** \`figures/fig1_dark_structure_landscape.pdf\`. Also export editable SVG and source tables.

**Purpose:** Generate a high-quality *visual layout concept* with an image generator, then rebuild the scientific panels using actual data, code-based vector graphics, real experimental MS/MS and RDKit molecular SVGs. A generated concept is **not** itself a publishable scientific results figure.

## A. Master image-generation prompt — copy and paste

> Create a sophisticated scientific **journal Figure 1 visual design mockup** for a Nature Machine Intelligence–level paper on **metabolomic dark matter and mass-spectrometry-based molecular structure elucidation**. The intended reader is a computational chemist or mass spectrometrist. Figure 1 should visually communicate one central scientific narrative: *a large source-audited set of unknown tandem spectra can be converted into calibrated, structurally interpretable hypotheses and ultimately a navigable map of molecular-family relationships*.
>
> **Aesthetic:** premium scientific editorial design, clean white background, academically restrained and precise, professionally drawn quantitative panels, high information density without crowding. Flat vector aesthetics, extremely sharp lines, high typographic clarity, almost no ornament. Use charcoal #273239, slate #68747E, muted scientific blue #52778C, low-saturation teal #4B8582, light gray #CAD4D8 and a very subtle warm gray for unresolved categories. No gradients, no shadows, no 3D molecules, no marketing graphics, no colorful cards.
>
> **Canvas:** a landscape journal two-column figure, approximately **1.55:1 aspect ratio**, 3600×2320 pixel design target or the nearest supported aspect ratio. White space at borders, compact axis labels readable at 180 mm printed width, consistent small bold panel letters **a, b, c, d, e**. Use one scientific sans-serif family similar to Helvetica/Arial, with black body labels. Fine plot axes and short metadata annotations; avoid excessive large titles.
>
> **Precise layout:** Upper 38% of canvas contains panels **a, b, c**, arranged in unequal widths: (a) source accounting ~32%, (b) empirical spectral recurrence ~24%, (c) structural resolution ~40%, with small gutters. Lower 62% contains **d** across ~66–70% width, the largest and visually dominant chemistry landscape, and **e** on the right ~27–30% width with two or three stacked molecular-evidence case slots. Align margins and panel letters to one invisible grid. Natural reading order a→b→c→d→e. Distinguish panels through spacing and fine rules rather than background cards.
>
> **Panel a | What is the source-audited dark MS/MS universe?** A compact dual-level accounting figure with readable proportional bars. Show acquisition-file figures **348 expected; 272 verified; 76 unavailable** in a small top band, separated from the much larger MS/MS-query denominator. Below, show **835,953 QC-eligible biological MS/MS queries**, categorized exactly as **13,884 unambiguous reference identities; 14,289 ambiguous accepted identities; 613,331 without accepted reference match; 194,449 unassessable**. A proportionally segmented horizontal bar should give muted teal emphasis to the reference-unmatched segment. Include small provenance note “UC, IBD200 and VEO-IBD; three audited study collections”. These are *spectral queries*, NOT 835,953 independent compounds, and 613,331 does NOT mean 613,331 undiscovered molecules. Keep decimal grouping and labels exact. Do not mix acquisition-file counts with spectrum counts in one bar.
>
> **Panel b | Cross-study recurrence of unexplained spectra.** A small, serious statistical recurrence graphic, preferably a thin two-tier strip or point/bar comparison (not a Venn diagram with made-up overlaps). The sourced claims are **2,255 reference-unmatched spectral communities recur across at least two study collections**, **98 recur across all three**. Below use the annotation **“Spectral communities are not molecular families.”** If visual room permits, add **“Conditional topology null: p = 0.91; not enriched.”** No invented per-study community numbers, no fabricated edges and no unverified enrichment claims. Distinguish study recurrence from chemical identification.
>
> **Panel c | How much structural information can be recovered?** Present an elegant ordinal, five-level structural-resolution scheme (not invented quantitative fractions): **Putative unique 2D connectivity → Bounded isomer alternatives → Supported common molecular core → Formula / class only → Unresolved**. Vary only muted colors or line weights to distinguish categories. Leave neutral, clearly demarcated **empty data slots** for future calibrated per-category fractions and empirical true-structure containment. For this concept mockup, label these empty regions **“MODEL RESULTS PENDING”** in very small gray type; do not fabricate percentage bars or claim unique structure identification. Key distinction: reporting structural-resolution category is not claiming experimental confirmation.
>
> **Panel d | Chemical landscape of the unresolved metabolome — the visual anchor.** Draw a beautifully organized large quantitative plotting region with x-axis **“Graph-level structural distance to characterized metabolites”** and y-axis **“Independent-study support”**. Provide an unobtrusive legend showing planned encoding for structure-supported families, bounded isomer/core hypotheses and unresolved cases, but without real data **DO NOT draw scatterplot points, molecular-family networks, embeddings, fake contours or imaginary chemical relationships**. Leave generous blank central plot area for source-derived molecular-family data to be overlaid during vector production. Optionally add a quiet center note **“Source-derived molecular-family data to be inserted”**. The plot's empty-but-polished scientific design should make it clear that the data are an explicit future deliverable.
>
> **Panel e | What is the chemical evidence behind one structural hypothesis?** A right-hand vertical rail with two or three highly disciplined **source-evidence slots**, each reserving space for (1) an authentic experimental tandem MS stick spectrum, (2) an RDKit-rendered molecular graph or a bounded isomer/common-core depiction, and (3) a compact fragment-support explanation. At this concept stage use crisp white insertion spaces with small gray labels **“Measured MS/MS · insert”**, **“RDKit molecular graph · insert”**, **“Fragment evidence · insert”**, rather than generating fake spectral peaks or chemical structures. Include a tiny future status field for “putative / bounded / independent reference”, but no invented confirmed compounds. Each case should ultimately use real source accession and precursor/adduct labels.
>
> **Visual flow:** Panel a demonstrates the extent of the unresolved measured universe. Panel b demonstrates empirical recurrence. Panel c defines the measurable structural output. Panel d is the chemical-space result the reader wants to discover. Panel e shows what fragment evidence supporting a structural hypothesis looks like. Make this transition intuitive through figure composition, NOT a sequence of oversized arrows.
>
> **WGV/RSI presence:** This paper develops a self-improving ORBIT-MS system, but **Figure 1 is discovery-first**. The Agent-driven RSI workflow has its own detailed Figure 3. Figure 1 may have only a tiny understated connector text **“ORBIT-MS · evidence-guided, self-improving elucidation”** near the transition from experimental spectra to resolution outputs. Do not draw large LLM-agent diagrams, gear icons, neural networks, W/G/V boxes, recursive loops or tool-call UI.
>
> **Overall impression:** exacting analytical chemistry, carefully typeset experimental data, substantial negative space, low-saturation palette, credible academic visual grammar, balanced multi-panel composition, visually memorable *dark chemical landscape* without any fabricated scientific evidence.

### Negative prompt

> Cartoon chemistry, giant glossy 3D ball-and-stick molecules, fabricated molecular rings, made-up chemical formulas or SMILES, fake mass spectral peaks or false m/z labels, generic stock DNA helices, robotic scientists, glowing AI brain, SaaS dashboard, bright multicolor bubbles, random UMAP clouds, made-up scatter points, arbitrary network nodes and graph edges, invented percentages, invented spectra, imaginary chemical-family identities, gradient backgrounds, dropshadows, rounded decorative cards, marketing arrows, icon soup, textbook flowchart, overlapping text, microscopic fonts, mislabeled axes, fake benchmark improvement, hallucinated study counts, any implication that all unmatched spectra are new metabolites or that recurrent spectral communities are established molecular families.

## B. Verified numeric content — use exactly these source values

| Scientific unit | Number | Interpretation |
| --- | ---: | --- |
| Expected acquisition files, three collections | 348 | Source-file inventory |
| Verified acquisition files | 272 | Accessible verified sources |
| Unavailable files | 76 | Keep distinct from usable data |
| QC-eligible biological MS/MS queries | 835,953 | One spectrum/query accounting denominator, not unique molecules |
| Unambiguous accepted reference identity | 13,884 | Mutually exclusive status |
| Ambiguous accepted reference identity | 14,289 | Mutually exclusive status |
| No accepted reference match | 613,331 | Dark-spectrum source pool under the stated library protocol |
| Unassessable | 194,449 | Not confirmed unmatched |
| Recurrent reference-unmatched **spectral** communities (≥2 studies) | 2,255 | Not chemically identified families |
| Recurrent in all three studies | 98 | Subset of 2,255 |
| Conditional topology null | p = 0.91 | No observed enrichment under this specific null |

**Source:** ORBIT-MS [PR94](https://github.com/wangyu-sd/orbit-ms/pull/94) and the merged \`MS-paper/main.tex\` first Results section. The four query statuses sum to 835,953. Counts are from UC, IBD200 and VEO-IBD; do **not** call them a global repository census.

### Pending empirical assets, not to be invented

- **c:** actual number of distinct dark spectral entities; distribution across five structural-resolution tiers; calibrated truth containment.
- **d:** real structurally supported molecular-family IDs, their graph-level distance to characterized metabolites and independent recurrence; currently no source-derived family landscape to plot.
- **e:** specific real dark-spectrum accession, experimental measured peaks, correctly drawn molecular candidate(s), fragment assignments, competing structures and independent spectral evidence; must be selected from completed chemical analyses.

No image generator can infer these items from the numeric panel a–b source accounting.

## C. Design-to-publication production workflow

1. **Concept image:** Run the English prompt through the chosen text-to-image generator. Save a concept preview in a clearly named **mockup** asset; it is only a visual reference. If image-text fidelity is poor, drop embedded numerals and composite the verified numbers later.
2. **Vector recreation:** Rebuild all panels in Python/matplotlib or equivalent vector software using **original CSV/JSON/Parquet and RDKit**, not an upscaled generative image. Type all numerical labels manually or in code. No layout-image pixels should serve as empirical data.
3. **Data binding:** Panel a–b must link to PR94 counts and source snapshot. Panels c–e remain deliberately unfinished until real data and molecules are available.
4. **Scientific QC:** Ensure full source-denominator accounting, independent units, exact chemical graph validity, measured-spectrum provenance and distinction between model hypothesis and confirmed chemical identity. No fictional reaction pathways.
5. **Final outputs:** \`figures/fig1_dark_structure_landscape.pdf\`, editable SVG, source plotting script, tables supporting every numeric element and at least one high-resolution preview. The current repo has no \`figures/\` folder on main; create it when source-derived figure assets are actually produced.

## D. Panel-level review checklist

- **a:** contains the two separate source and query denominators, with correct labels.
- **b:** demonstrates spectral recurrence but does not prematurely identify chemicals.
- **c:** clear structural-resolution hierarchy and reserved space for true outcome counts.
- **d:** largest panel, plotting real graph-based chemical-family relations when data exist; no synthetic dots.
- **e:** reserved for measured MS/MS and real RDKit graphs; no fantasy spectra or chemistry.
- **Whole figure:** a quiet chemical-discovery narrative, not a machine-learning benchmarking dashboard or an overdecorated AI architecture panel.

## E. Draft figure caption

**Fig. 1 | From reference-unmatched tandem spectra to a structurally interpretable dark-metabolome landscape.** **a**, Source-audited acquisition and biological MS/MS reference-assessment counts for three public metabolomics study collections. **b**, Recurrent reference-unmatched spectral communities across studies, distinguished from molecular-family assignments. **c**, Planned calibrated levels of structural information returned by ORBIT-MS. **d**, Planned source-derived molecular-family chemical landscape with explicit relation to characterized chemistry. **e**, Planned representative source-linked experimental spectra, proposed molecular structures and fragment-specific evidence. Panels c–e will contain actual quantitative structural results only after the corresponding model inference and chemical analyses have been completed.

**Implementation reference:** \`main.tex\` → \`\\figureonetodo\` / \`fig:dark_landscape\`. This file introduces an image-generation prompt and asset requirements only; it does not change manuscript claims or assert completed results.
