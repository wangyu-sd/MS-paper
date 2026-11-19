# ORBIT-MS | NMI method framework: MMA-centric vector figure execution brief

**Date:** 2026-11-16  
**Status:** design and Codex implementation brief, NOT manuscript text or a completed figure  
**Working study:** *ORBIT-MS: Agent-Driven Recursive Self-Improvement for Molecular Structure Elucidation*  
**Scope of this PR:** one new Markdown instruction document. Leave the manuscript, its Figure 1 numbering, its existing Results plan, and all current figure PDFs untouched.

## 0. Immediate task for Codex

**Produce an original, publication-quality, editable vector method framework figure in a follow-up implementation PR. Do not respond with another abstract architecture plan.**

The figure must communicate four coupled objects: **(1) peak-conditioned mass-matched substructure alignment (MMA), (2) molecular Generator G + fragmentation World W + experimental-spectrum Verifier V, (3) information-guided semi-supervised experience creation, and (4) bounded Scientific Improver / recursive learning.**

Above all, **MMA must have its own substantial mechanistic panel** with actual chemical representations and neural alignment details: it is neither a bare library cylinder nor a generic arrow labelled "chemical knowledge". Its value is converting observed fragment-ion masses into *soft, graph-structured, executable* chemical hypotheses.

Do not generate arbitrary compounds, arbitrary fragment peaks, fake ion formulas, predicted results or autonomous RSI gains. Retrieve one real query/candidate set from ORBIT-MS source artifacts where possible; if any required source-linked asset is unavailable, implement a precisely sized, clearly annotated **asset insertion slot** and record it in a source manifest. The final paper figure must use real source-derived spectra, RDKit fragment and precursor graphs, and real W/V outputs.

**This is a method graphic, not a Results accuracy dashboard.** Show no unsupported performance, benchmark claims, biological discoveries or speculative chemical reactions.

## 1. How this differs from earlier paper proposals

- [PR #12: results-first narrative and evidence inventory](https://github.com/wangyu-sd/MS-paper/pull/12) sets the science story: headline molecular recovery first, then the generation–discrimination bottleneck, information-guided learning, adaptive agent interventions, and actual dark-metabolomics relevance. This figure supports that Results story but should not duplicate its empirical plots.
- [PR #11: prior Fig. 1 concept](https://github.com/wangyu-sd/MS-paper/pull/11) contains a five-panel design focused on ambiguity, MMA, G, W/V and Agent. **This brief refines the visual hierarchy and adds an explicit, independent Sleep/Wake/Hindsight + acquisition panel without shrinking MMA.** Consult PR #11 for evidence/chemistry constraints; do not indiscriminately merge its older composition with this new one.
- At the current `main` branch, `main.tex` still assigns a *dark-structure-landscape* slot to Figure 1. The exact manuscript figure number of this method schematic is **provisional**. Do **not** modify `main.tex` or overwrite its `fig1_dark_structure_landscape.pdf`. Prepare a separate method figure and leave placement/renumbering for author review.
- This new figure is a **scientific mechanism map**, not a depiction of 11 completed autonomous agent episodes. Historic engineering generations and real autonomous episodes must remain distinct.

## 2. Conceptual statement that the reader should learn in 5–10 seconds

> Measured MS/MS peaks generate mass-compatible structural fragment hypotheses through MMA. G uses this reusable graph knowledge to construct plausible precursor candidates. W predicts fragment evidence *from each candidate structure*, and V compares that evidence with the measured spectrum to discriminate candidates. Sleep, Wake and Hindsight provide learning experience selected for chemical informativeness and diversity; a Scientific Improver diagnoses failure and selects which chemical/model capability to update, carrying outcome memory into the next decision.

Three types of arrows must remain visually separable:
1. **Inference** (solid charcoal/slate): measured spectrum → MMA/G; candidate molecular graph → W; W-proposed fragments + measured spectrum → V; output candidates/ranking.
2. **Learning data/update** (teal, medium solid): Sleep/Wake/Hindsight → experience selection → MMA/G/V updates. In initial PR96 experiments W remains frozen.
3. **Scientific decision and episodic memory** (muted purple, fine solid/dashed): TRAIN FIT failure evidence → agent → one allowed intervention → evaluation → later agent decision. Memory changes decision context, not LLM weights.

## 3. Exact spatial composition (recommended)

A **16:9 horizontal scientific canvas**, reference size **3600 × 2025 px** (vector-master, independently scalable). White `#FFFFFF` background, margins ~4% and meaningful whitespace. Five visually integrated, **non-equal** areas, with no thick boxed dashboard aesthetic:

| Region | Position | Relative height / width | Purpose |
|---|---|---|---|
| **a · Scientific task** | Narrow strip across top | ~13–15% height | One source-grounded measured MS/MS and two same-formula competing molecular graphs; establish chemical ambiguity immediately |
| **b · MMA mechanism (dominant inset)** | Middle-left | ~52–55% middle-band height, **43–45% middle-band width** | Four concrete MMA stages, with the largest chemical illustration dedicated to peak–ion formula–motif–growing graph alignment |
| **c · G → W/V elucidation** | Middle-right | Same middle height, 55–57% middle width | Same query: atom/ring/motif graph construction, W structural fragment hypotheses, V measured-spectrum comparison, ranked/bounded molecular output |
| **d · Information-guided learning** | Bottom-left | ~25–28% height, ~58–60% width | Sleep / Wake / Hindsight converging on entropy/scarcity/diversity-quality selection and reusable new experience |
| **e · Scientific Improver / RSI** | Bottom-right | Same bottom height, ~40–42% width | Diagnosed chemical failures, one bounded action, evaluated update, reflection/memory; loop back to b/c and d |

This version intentionally uses ordinary reader scan order **a → b → c → d → e**, while preserving the integrated core and two learning loops. Do not make five disconnected cards. Use a common quiet panel grid and routed arrows **outside molecular bonds and spectral sticks**. A few slender cross-panel arrows are enough. Make the MMA panel visually prominent through **correct chemical objects and meaningful graph correspondences**, not a large brightly colored background.

If the exact dimensions require adjustment for readable chemistry, keep the hierarchy: **MMA >= 40% of middle width; inference engine the remainder; data and RSI along a restrained lower band.** No decorative header taller than necessary.

## 4. Panel a — the chemical inverse problem (minimal context)

**In-figure heading:** `a  Molecular structure elucidation from MS/MS`

Show one genuine experimental MS/MS stick spectrum with precursor mass/adduct and 3–5 real peak ticks highlighted; next to it show two *actual formula-compatible* candidate precursor graphs with visibly different bond connectivity. The spectral query and the two candidates should be the **same case used in panels b and c**. If benchmark ground truth is shown for explanatory purposes, annotate it as a known-identity benchmark case and do not depict GT as an unknown-inference input.

One short line: `One spectrum, competing molecular structures`. Do not claim an observed mass difference alone proves a fragmentation reaction.

## 5. Panel b — MMA is the scientific centerpiece

**In-figure heading:** `b  Mass-matched substructure alignment (MMA)`  
**Local subtitle:** `Observed ions → reusable graph-structured fragment hypotheses`

It must resolve **four structural levels** with real visual evidence:

**b1. Build a chemically grounded fragment knowledge resource.** Display a small pair of precursor molecule/fragment drawings and the mined local fragment graph (not a database cylinder). Sources are labeled TRAIN structural evidence and structure-conditioned W-simulation. Source-group counts and `(adduct, ion formula, fragment motif)` keys explain how chemically plausible hypotheses are stored. If showing support/provenance, state that TRAIN retrieval excludes the query group's own contribution during TRAIN evaluation. Supported mining types include connected structural subsets, H-shift and restricted migration **only when source records justify them**. Ion formula and a motif's neutral skeletal formula may differ by hydrogen/charge; do not silently equate them.

**b2. Peak-conditioned retrieval.** Highlight one actual measured peak from a and show the chain:
`observed m/z_i → mass-compatible ion formula hypotheses → top-K candidate fragment graphs`.
Show **two or three alternate fragment subgraphs for one peak**, each as a soft candidate, not as confirmed identity. A thin local label can indicate `mass tolerance / precursor formula / support prior`. Actual implementation: the peak fragment library sorts selected peaks, matches ion masses and formula inventory, ranks supported motifs and implements own-group exclusion. It is not a single deterministic peak-to-structure mapping.

**b3. Neural motif / graph alignment (largest internal illustration).** A candidate motif's *actual atom-and-bond graph* is encoded by a motif message-passing encoder; a peak-conditioned query weights motif candidates; motif atoms are explicitly aligned with atoms/bonds of an **incomplete G molecular graph**. Use small teal highlights on matching graph bonds/atoms and thin dashed correspondence segments. Include two small labelled computational pathways:
- `peak ↔ motif attention` updates peak-spectrum memory;
- `motif atoms ↔ partial graph atoms` updates G atom/graph memory, with optional mass-aware interactions.
Never draw a fully ground-truth-aligned precursor graph at inference time. Explain visually that unplaced target motifs can still inform the current partial graph through motif atom memory.

**b4. Executable use, not just embeddings.** From the aligned motif show two compact outputs:
- `G: peak-informed atom/ring/motif actions, MMA/multi-motif starts`;
- `V: optional motif evidence channel alongside W fragments`.
Use a small 3-frame real G construction action strip (e.g. fragment→mstart/mattach→larger legal partial graph), with chemical valence/formula constraints. `R_t` may be a tiny action-selection/gating tag only if that checkpoint is actually illustrated. Macro-Core is **homology-assisted optional route**, not an unqualified pure de novo construction; if included, use a dashed, labeled side path.

**Faithfulness checks from code:** `PeakFragmentHypothesis` stores peak index, fragment, ion formula, support, prior and peak weight. `PeakMMA` adds motif-encoded signal to peak memory and aligned atom features; `PeakMMAAtomMemory` permits atom-to-all-motif memory; `MassAwarePeakMMA` additionally uses exact mass, H-shift and peak interaction features in its respective variant. `VSetPosteriorMMA` adds a *learned per-peak mixture* of W-derived and aligned motif likelihoods. These are **implemented architectural variants**; do not make an unsupported claim that every deployed checkpoint uses all variants simultaneously.

**Design objective:** a reader must be able to explain how **m/z information becomes a concrete graph action**, rather than thinking MMA is a static lookup table.

## 6. Panel c — molecular hypotheses and evidential discrimination

**In-figure heading:** `c  Generate, simulate and discriminate molecular hypotheses`

Use the **same real query** as a/b. Present 3–4 source-derived partial-to-full G states under `formula / valence / bond constraints`. The outcomes should be at least two candidate molecules with the same precursor formula and a meaningful local connectivity difference.

Depict World and Verifier as two *causally distinct* operations:
- `G: atom / ring / motif construction` — makes candidate graphs.
- `W: structure → fragmentation hypotheses` — forward predicts candidate-specific ion fragments and masses; **W does NOT ingest the measured target product-ion spectrum during forward inference**.
- `V: measured MS/MS + W fragment evidence (+ enabled MMA channel) → candidate discrimination` — evidence-conditioned ranking or a bounded isomer set.

A small 2-candidate × 3–5-observed-peak grid can distinguish **shared** evidence (gray), **candidate-specific/discriminating** evidence (teal), and **unexplained** observations (hollow). Real W and V receipts are needed before populating cells; otherwise show clearly empty slots.

Route a separate thin measured-spectrum arrow from a directly into V. The outgoing result should be `ranked hypothesis / bounded alternatives`, not an always-certain unique structure. The figure must make clear that higher candidate **Reach** alone is not the same as better **Exact@1**.

## 7. Panel d — semisupervised experience, intentionally compact

**In-figure heading:** `d  Information-guided semi-supervised learning`

Three short, parallel horizontal source lanes converge to one acquisition gate:

- **Sleep:** unpaired chemical structures → frozen W → structure–simulated-spectrum pairs.
- **Wake:** real unlabeled experimental spectra → G candidates → evidence-based pseudo-label gating.
- **Hindsight:** G-proposed candidate graphs → W counterfactual spectra → paired experience / hard negatives.

Below the three lanes use ONE concise selector:
`spectral entropy  +  structural scarcity  +  scaffold diversity  +  evidence-quality gates`.

Show teal arrows from selected experience back to **MMA, G and V**, not to the agent LLM weights. If useful, draw a tiny real molecular scaffold or real spectral stick inset; do not replace the data pathways with three large anonymous database/icons.

**Methodological caution:** the existing GeMS/Hindsight builder implements W/V pseudo-label gates, a Murcko `max_per_scaffold` cap and an emitted-spectrum Shannon entropy **threshold**; PR95 reports broader entropy/scarcity-informed scheduling. Do not label this `globally maximum entropy` or assert demonstrated information gain. Call it `information-guided acquisition` unless new measured controlled ablations support a stronger term. Show no numerical benefit unless the corresponding run artifacts can be linked.

## 8. Panel e — bounded agent-driven recursive improvement

**In-figure heading:** `e  Scientific Improver: diagnosis → intervention → evidence`

One compact scientific loop, no robot, assistant avatar or chat window:

`TRAIN FIT failure cases → diagnose missing knowledge / missing candidate / misranking → scientific hypothesis → one selected action → train/evaluate → memory`.

Use the real PR96 closed action vocabulary, with only four visible choices:
`EXPAND_KNOWLEDGE`, `IMPROVE_GENERATOR`, `IMPROVE_VERIFIER`, `COLLECT_EVIDENCE`.

A single active action is selected at a time. Show **two distinct return arrows**:
1. `chemical capability update` from executed action to MMA/G/V (and d when collecting experience), **not W model weights** in the controlled experiment;
2. `episode outcome/reflection` to the Agent's later decision context.

The evaluation receipt should show metric **types** only: `newly reached structures`, `re-ranked true structures`, `regressions`, `resource cost`. Leave values absent unless sourced. Never draw a smooth G0→G11 autonomous performance curve from the historical engineering version ledger.

The loop is about **scientific improvement of the chemical inference system**, not the language model fine-tuning itself.

## 9. Editorial visual system (NMI-quality, chemistry-first)

- **Background:** pure white `#FFFFFF`; panel segmentation by thin charcoal rules or very faint neutral washes, not heavy colored card borders. No gradient, glow, drop shadow, 3D molecule spheres, dashboard gadgets, repeating curved thick arrows or "AI brain".
- **Primary text and chemical bonds:** charcoal `#30373C`; primary routes `#435F75`; secondary annotations `#78838C`.
- **MMA / learning and graph highlights:** muted teal `#4E8C89` with pale background `#E8F2EF`; this color highlights actual matching atom/bond regions and learned-experience returns.
- **W/V discriminative physical evidence:** restrained warm ochre `#BD8A58` for a small number of measured/matched peak marks, never whole panels.
- **Agent and memory:** desaturated violet-gray `#796A82`; use in loop labels, action selection and memory arrow only.
- **Typographic hierarchy:** Arial/Helvetica-like sans serif (or an available metrically equivalent sans); section labels 20–24 pt at 3600 px reference equivalent, body panel descriptors 14–18 pt, micro annotation 12–14 pt minimum at master scale. Verify readability in a 180 mm two-column-width journal preview; adjust sizes instead of shrinking everything.
- **Molecular graphics:** RDKit SVG, consistent bond length, non-isomeric versus stereochemical rendering matched to actual evidence (InChIKey-14 assesses connectivity only); dark gray bonds, legible atom labels, no stretched/skewed graph drawings. Different molecule IDs must not be visually mislabeled as identical cases.
- **Spectra:** thin crisp vector sticks, correct m/z numeric positioning and measured relative intensity. At most a few chosen peaks highlighted; axes and tick values remain honest.
- **Connectors:** mostly orthogonal/slight straight bends with arrowheads at true downstream endpoint. No connector crosses molecular bonds, label text, mass spectral ticks or other connectors. Solid for inference; teal for training; purple for decisions; gray dashed for episodic memory. Include at most one minimal arrow legend if necessary.
- **Compactness:** one short phrase per stage; move architecture implementation jargon, citations, data volumes and equations to caption/Methods or Extended Data. A figure should remain understandable without an embedded paragraph.

## 10. Source retrieval and single-case manifest

Codex should search the actual ORBIT-MS run artifacts and PR95 code for **one coherent measured query** with complete evidence. A known benchmark cyclic peptide, macrolide or glycoside can be considered only if it has **real peak lists, GT/candidate SMILES, fragment hypotheses, a partial graph trajectory and W/V scores**. Choose a source based on available artifacts, not name recognition.

Prepare a local `case_manifest.json` (or Markdown if simpler) containing:
- source dataset + case ID / accession / file hashes, measured precursor mass/adduct/collision energy and the actual peak array;
- neutral/formula constraints and candidate structural graph IDs, candidate formula and RDKit image source;
- each highlighted MMA peak → ion formula → fragment graph → support/prior, plus any atom-mapping/partial-state evidence;
- real G intermediate states/actions, checkpoint, final candidate list and which construction regime (pure G, MMA-seeded, Macro-Core assisted);
- candidate-specific W structural fragment support, V matched/measured peak grid and ranking provenance;
- for Agent, actual implemented action semantics only. If no completed per-episode receipt, caption says **schematic controller**, no quantitative success marker.

**Do not infer chemistry that is absent from source code/receipts.** In particular, a measured neutral-loss mass difference is not a confirmed electron-rearrangement reaction.

### Exact upstream code to read first

At ORBIT-MS PR95 source snapshot `a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8`:
- [MMA peak hypothesis/library](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/src/orbit_ms/wgv/peak_fragment_prior.py)
- [MMA motif encoder, peak/atom alignment and mass-aware variants](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/src/orbit_ms/wgv/cocograph_v4_peak_msa.py)
- [MMA-conditioned atom/ring/motif generator](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/src/orbit_ms/wgv/peak_ladder_motif.py)
- [Optional homology partial-core construction](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/src/orbit_ms/wgv/peak_ladder_scaffold.py)
- [MMA-aware V evidence mixture](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/src/orbit_ms/wgv/v_set_mma.py)
- [Sleep/Wake/Hindsight asset builder](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/scripts/build_pr93_unlabeled_gems_rsi_cycle.py)
- [Legacy training/controller](https://github.com/wangyu-sd/orbit-ms/blob/a7b5f15e5f4fd2a19ef4cd08037d7db85ba24ad8/scripts/run_pr93_autonomous_rsi.py)

At ORBIT-MS PR96 source:
- [Bounded Scientific Improver](https://github.com/wangyu-sd/orbit-ms/blob/c63c32ce24b29d959164c2b081e511b25641a1c4/src/orbit_ms/agents/scientific_improver.py)
- [Scientific Improver run interface](https://github.com/wangyu-sd/orbit-ms/blob/c63c32ce24b29d959164c2b081e511b25641a1c4/scripts/run_pr93_scientific_improver.py)

Related paper-side design context: [PR #11](https://github.com/wangyu-sd/MS-paper/pull/11), [PR #12](https://github.com/wangyu-sd/MS-paper/pull/12).

## 11. Concrete implementation deliverables for the *drawing* follow-up PR

**Deliver an actual composed figure**, not only a prose description or a figure prompt. Suggested names, deliberately isolated from manuscript auto-include slots until author review:

- `figures/method_framework/orbit_ms_nmi_method_overview.svg` — master **editable vector**.
- `figures/method_framework/orbit_ms_nmi_method_overview.pdf` — publication vector export.
- `figures/method_framework/orbit_ms_nmi_method_overview.png` — 300-dpi or higher review preview.
- `figures/method_framework/assets/` — RDKit fragment/precursor SVGs and source-derived spectrum/vector assets.
- `figures/method_framework/case_manifest.json` — provenance and placeholders.
- One reproducible drawing/assembly script (Python / RDKit / Matplotlib / SVG preferred, or an equivalent true-vector workflow).

**Iteration standard:** produce an initial complete layout; inspect at 100% and at article-column width; repair chemistry bonds, overlapping text/arrows and line weights; export again. Do not submit a visually attractive but scientifically incorrect illustration. Do not embed a raster screenshot into an SVG and call it editable.

**Pass/fail figure checklist:**
1. MMA is a **mechanistic 40%+ middle region** with real fragment-graph correspondence and visible contribution to graph actions.
2. One actual measured spectrum and corresponding candidate structures recur across a/b/c.
3. Observed MS/MS enters G/MMA and V, **not W**.
4. Sleep / Wake / Hindsight are three distinct and correctly oriented data paths, with information-based selection described conservatively.
5. The Agent chooses a typed action, has evaluation and persistent memory, and shows **separate chemistry update and agent-memory feedback**.
6. No invented spectroscopy, structural drawings, reaction mechanisms, made-up gain numbers or unsupported autonomous episodes.
7. Source SVG/PDF is clean, white, vector-based, color-consistent, typography readable, arrows and chemical structures non-overlapping.
8. This new implementation PR should **not modify `main.tex`, manuscript Results or existing published figure paths** until author approves placement.

## 12. Candidate caption (working only)

**ORBIT-MS integrates mass-matched chemical knowledge, fragment-evidence-guided molecular inference and recursive scientific learning.** **a**, An experimental tandem mass spectrum constrains but does not uniquely identify precursor connectivity. **b**, MMA retrieves source-supported ion-formula and structural fragment hypotheses, encodes their motif graphs and aligns evidence with the growing precursor graph to guide molecular construction and, when enabled, motif-aware verification. **c**, A chemically constrained Generator constructs candidate structures, a structure-conditioned World predicts fragment hypotheses without access to the measured target product-ion peaks, and an observation-conditioned Verifier discriminates candidates using measured spectral evidence. **d**, Complementary Sleep, Wake and Hindsight processes contribute spectrum–structure experience selected using evidentiary and chemical-diversity considerations. **e**, A Scientific Improver diagnoses TRAIN-derived failures, selects a bounded knowledge/model intervention, evaluates updates and retains the resulting episode evidence for subsequent decisions. The learning controller is shown schematically; autonomous performance gains must be established separately.

---

**Stop condition for this design-only PR:** once this specification is committed and the PR is opened, do not modify other repo files. Codex can read this PR and implement the vector artwork in a separate follow-up branch.