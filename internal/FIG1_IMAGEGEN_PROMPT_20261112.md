# Figure 1 | ORBIT-MS scientific-method figure — detailed text-to-image prompt

**Paper:** *ORBIT-MS: Self-improving molecular structure elucidation of metabolomic dark matter*  
**Figure 1 working title:** **From ambiguous MS/MS to evidence-guided and recursively improvable molecular structure elucidation**  
**Role:** A single, complete **scientific method overview with a worked structure-elucidation example**. It must explain the real problem, the inferential steps, and what becomes learnable across generations.  
**Figure in LaTeX:** `main.tex`, `\figureonetodo`, panels **a–e**, label `fig:orbit_method`, final PDF `figures/fig1_orbit_ms_method_overview.pdf`.  
**Status:** This file is a concrete **text-to-image composition prompt + source-asset specification**, not a claim that fully grounded molecular figure assets or an autonomous RSI accuracy result already exist.

## 1. The three problems this method solves — these MUST be visible on the page

The diagram must NOT be a sequence of boxes labelled "MS/MS → G → W → V → Agent". Every box must have a visually distinct scientific object, a specific failure it addresses, and a visible consequence for molecular interpretation.

| Unsolved chemical-inference problem | Why common pipelines fail | ORBIT-MS operation that addresses it | Observable consequence |
| --- | --- | --- | --- |
| **P1: Structural hypothesis coverage.** Sparse product-ion masses do not uniquely specify a connected precursor graph; long atom-wise generation fails on complex rings and natural products. | Pure spectral matching requires reference coverage; direct molecular generation can produce invalid or plausible-but-wrong connectivities and never reach the target. | **G + MMA + Canonical Hybrid**: mass/formula-constrained graph assembly guided by observed peak relations, multi-atom motif/ring starts and chemically legal atom/ring/motif attachments, with beam search and candidate diversity. | A real pool of full candidate molecular graphs, including structures that might have been inaccessible to the original generator; **candidate reach** is measured separately from final rank. |
| **P2: Evidence-based structural discrimination.** Competing same-formula structures explain many of the same peaks. | Producing more structures can improve candidate reach while lowering top-1 selection; generic fragment matching or molecular prior alone cannot reliably separate close isomers. | **W then V**: for each candidate, W supplies structural fragment-ion possibilities without using the target product-ion spectrum, and V confronts those possibilities with actually measured masses/intensities to score competing graphs. | Candidate-specific explained versus unexplained peaks, discriminative fragment hypotheses and evidence-supported ranking or bounded structural alternatives; a true candidate already in the pool can move upward. |
| **P3: Static capability / repeated failure.** A trained system repeatedly encounters missing motifs, ungenerated structures or poorly discriminated isomers. | A single inference pass has no mechanism for selecting what to learn next; endlessly enlarging a library or retraining G every time need not improve chemical understanding. | **Scientific Improver Agent / RSI**: diagnose TRAIN failures, propose a testable scientific hypothesis, choose one of EXPAND_KNOWLEDGE, IMPROVE_GENERATOR, IMPROVE_VERIFIER or COLLECT_EVIDENCE, run existing tools, measure before/after changes, remember outcomes and repeat. | Updated MMA/G/V and agent decision memory in the following generation; the *target scientific result* is newly recoverable molecular structure, not an extra line of agent reasoning. |

**One-sentence legend that the picture must communicate without explanation:**  
**“When the true structure is missing, learn better chemical proposals; when the true structure is present but indistinguishable, learn better spectral evidence; when the same type of failure recurs, a scientific agent decides which knowledge to acquire next.”**

**Critical distinction:** The *inference loop* reasons about a single unknown spectrum. The *RSI learning loop* uses correctly labelled TRAIN FIT diagnostic cases to change subsequent inference capability. The World W is frozen during the initial PR96 controlled RSI experiment. The Agent's experience memory changes its next decision **without changing the Agent LLM weights**.

## 2. Graphical organization — specific layout before rendering

Use an asymmetrical **16:9 landscape canvas**, 3840 × 2160 reference composition (or closest permitted output aspect ratio), white background, journal two-column figure typography. This should be reproducible as a multi-panel vector figure at 180 mm print width.

Instead of five visually disconnected blocks, organize the figure into **three integrated horizontal visual levels**:

**LEVEL I: Scientific inference challenge (upper ~18% of the page).** One large measured MS/MS input beside two *actual alternative precursor-connectivity* drawings of the same formula and an understated caption: **“The same peaks admit multiple molecular graphs.”** This is the scientific problem statement; it is NOT a benchmark dataset funnel or global chemical-space plot. Panel **a** primarily occupies this level.

**LEVEL II: Hypothesis–evidence reasoning (middle ~47%).** The dominant region contains **b, c and d** as three genuinely different scientific workstations:
- **b / left:** spectrum-conditioned, chemistry-constrained *graph building*, with partial graph trajectories and a small accessible MMA fragment/ring resource;
- **c / center:** **one candidate at a time** passes through spectrum-blind forward fragmentation W, yielding atom-level structural fragment hypotheses, mass and formula information;
- **d / right:** measured MS/MS and the W predictions meet inside V, producing a **candidate-by-observed-peak evidence comparison** and a *ranked or bounded* structural decision.
Arrange the connections so someone can trace the same target spectrum and candidates across all three stages. The measured spectrum has a direct data line into **both G and V**; there is **NO arrow** from target experimental fragment peaks into W. Chemical graphs, not abstract colored feature vectors, are the main content.

**LEVEL III: Learning from failures (lower ~35%).** One visually unified wide panel **e** shows a **specific causal diagnostic→action→evaluation→memory sequence**, with an easy-to-follow return to G/MMA/V. Do **not** draw a fourth interchangeable model box. Two separate feedback arrows are necessary:
1. **chemical capability feedback** updates G, V or MMA (W fixed initially);
2. **experience feedback** saves decision, outcome and reflection for the Agent's next choice.
Use one muted teal upward return arrow for the system update and a separate thinner gray horizontal return for memory. Both end at their actual destinations.

Put an extremely concise small **scientific outcome statement** at the bottom right, not a giant claim:  
**“Previously unresolved spectrum → better-supported structural hypotheses → recoverable chemical relationships.”**  
This is the *purpose and proposed output* of recursive learning, not yet a measured before/after result.

Visual percentage split is a design guide; optimize actual size to keep real molecular structure and stick-spectrum regions legible. Good science figures use multiple aligned grids, not equal-height cards.

### Compact wireframe for the illustrator (structure, not literal final typography)

```text
 ┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
 │ a. SCIENTIFIC AMBIGUITY                                                                       (~18%) │
 │ REAL measured MS/MS (mz,intensity; precursor/adduct) ──→ same-formula candidate graphs A / B / C     │
 │                                               QUESTION: which connectivity actually explains peaks?  │
 ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
 │ b. BUILD HYPOTHESES                   c. PREDICT FRAGMENTS               d. TEST AGAINST EXPERIMENT   │
 │                                  │                                  │                              │
 │ spectrum ──→  select peak       │ candidate A → [fragment A1,A2]   │ measured peaks ──┐          │
 │              grow partial      │ candidate B → [fragment B1,B2]   │                 ▼          │
 │              atom/ring/motif   │ shared + candidate-specific      │ candidate × peak evidence    │
 │ MMA motif knowledge ──┐        │                                  │ common vs distinguishing      │
 │                       ▼        │ **NO target spectrum into W**     │ evidence → rank / bounded set │
 │    partial 0 → 1 → 2 → A,B,C   ─────────────→ W fragments ─────────────────────────────→ V          │
 │  WHY: expand reachable graphs            WHY: structural evidence          WHY: separate isomers     │
 ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
 │ e. LEARN WHICH SCIENTIFIC CAPABILITY TO IMPROVE                                            (~35%)    │
 │                                                                                                      │
 │ TRAIN FIT: unreached graph / misranked isomer / unresolved fragments                                  │
 │                   │                                                                                  │
 │                   ▼                                                                                  │
 │          SCIENTIFIC IMPROVER AGENT  ←────  EPISODE MEMORY ←──── measured outcome/reflection            │
 │             diagnose / hypothesis / choose                       ▲                                    │
 │                   │                                              │                                    │
 │          ONE action: Expand MMA | Train G | Train V | Collect evidence                                │
 │                   │                                              │                                    │
 │                   ▼                                              │                                    │
 │            execute existing tool → evaluate: newly reached / reranked / lost structures              │
 │                   │                                                                                  │
 │                   └──── capability update ────→ next-generation MMA/G/V (W fixed initially)          │
 │                                    SCIENTIFIC GOAL: more recoverable chemical structure               │
 └──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

The top candidate graphs A/B/C must be **the same real candidates** whose graph-growth traces appear in b, whose structural fragment hypotheses appear in c, and whose experimentally measured peak alignment appears in d. The top row presents their ambiguity; the middle explains how the method resolves (or bounds) that ambiguity. The bottom panel operates on **a separate labelled TRAIN FIT feedback stream**, not the unknown-query truth.

### Why the problem is real (historical measured motivation; optional tiny annotation, not required in Fig. 1)

In PR95's **known-formula 200-molecule Calibration development condition**, switching from an empty-graph G-only policy pool to MMA-seeded starts **increased Reach from 16.0% to 19.0% but decreased Exact@1 from 7.0% to 5.5%**. On that **same MMA-start candidate pool**, terminal W/V ranking improved Exact@1 to **10.0% while Reach remained 19.0%**. Thus *hypothesis coverage* and *evidence discrimination* are demonstrably different problems. If a historical observation is typeset within Figure 1 as a very small scientific motivation, explicitly label the conditional known-formula setting and avoid mixing it with the single-case worked chemical example. The actual comparison and full breakdown belong to Figure 2.

## 3. One continuous source-grounded chemical example is mandatory

The upper section should be built around **ONE real experimental MS/MS and its true recorded G-candidate set**, not a collection of three unrelated example molecules. Choose a source-backed case where the recorded inference illustrates a clear chemical distinction:

- **First preference:** a documented same-formula **reachable-but-misranked** case containing at least two actual generated connected graphs and a recorded W/V comparison. Extract the exact measured spectrum, candidate SMILES, precursor/adduct, G/W/V values, W-supported fragments and any observed rank change from the same case receipt. This most cleanly illustrates the need for candidate-specific evidence.
- **Source-backed alternate to investigate:** **MassSpecGym case 0002114**, the cyclic tetrapeptide reported in PR95/SI as having a top-2 candidate with a linear *n*-propyl side chain whose local reattachment to isopropyl recovers the exact reference connectivity. This is a **known benchmark example** from the historical post-W/V refinement path, not a novel dark metabolite; use it only if its actual spectrum, two candidate structures and fragmentation/evaluation receipts can be reconstructed from the code outputs. Do not claim that W/V reranking *alone* performed the structural edit.
- Other historical candidates include **0000201 (beauvericin)** and **0064680 (epigallocatechin gallate)**, but only use one if it has a complete and internally consistent source-linked chemical-evidence trail. **Do not copy named compound structures without extracting the corresponding real experiment and generated candidates.**

Before inserting any chemical drawing, build a **case evidence package** containing:
`case_id`, `source_dataset / accession`, `precursor_mz`, `adduct`, `collision_energy_if_available`, measured `[(mz,intensity)]` peaks, permitted/predicted precursor-formula hypotheses, each candidate's `SMILES / InChIKey14 / formula / source`, actual `G_score / W_score / V_score / final_rank` when recorded, **G's genuine partial-state and action trajectory**, predicted W fragment graph/formula/mass provenance, V measured-peak alignment and result, and an explanation of whether the reference graph was absent, reached or reranked. Avoid target formula as a model input unless the illustrated experiment is explicitly a known-formula conditional example.

Use RDKit **Kekulé or appropriate aromatic 2D chemical graph rendering**, consistent atom labels, correct ring closures, formula-preserving alternative connectivities, visually balanced bond lengths and no compression. Bond strokes and heteroatom labels should survive reduction to print width. Draw only 2–3 real measured stick-spectrum peaks as prominent labeled examples if the actual spectrum supports that simplification, but preserve all measured peaks in the source artifact. Align highlights on candidate graph atom/bond positions with the predicted W fragment assignments and actual measured peak relationships. Labels indicating fragment structures must say **“predicted structural fragment”**, not “experimentally observed fragment molecule”.

If the complete example is not yet available, the image generator must create **specific white vector-replacement slots** with semantic captions, rather than drawing chemically false cartoons. The source-driven finished figure is the deliverable after evidence extraction.

## 4. MASTER TEXT-TO-IMAGE PROMPT (English; paste as-is)

> **Create the opening METHOD FIGURE for a Nature Machine Intelligence research paper, not an infographic and not a chemistry leaderboard.**
>
> Figure heading for the illustrator: **“ORBIT-MS | From ambiguous tandem spectra to self-improving molecular structure elucidation.”**
>
> The figure must solve and explain three linked scientific problems: **(1) molecular-graph generation from sparse, non-unique MS/MS evidence; (2) discrimination between plausible same-formula competing structures using chemically represented fragmentation evidence; and (3) learning from recurrent inference failures through an agent-directed recursive self-improvement loop.** The ultimate application is recovering chemically interpretable structure from metabolomic dark matter, not inferring disease mechanisms.
>
> **Visual atmosphere and production:** Research-grade, two-column journal diagram, landscape **16:9**, white canvas. Crisp monochrome chemical 2D graphs and mass-spectral sticks, clean compact technical typography, thin gray connectors with small arrowheads and consistent alignments. Low-saturation palette: charcoal `#26353B` for measured chemistry, blue-gray `#657986` for molecular hypotheses, muted teal `#4F8582` for informative fragmentation evidence and learning updates, warm gray `#9D9C95` for unresolved alternatives; pale neutral rules only. Panel letters a–e at top left of their subregions. The viewer must see the problem, actual chemistry, and adaptive resolution without reading a paragraph. Avoid giant box labels, repetitive cards, ornamental gradients and floating icons.
>
> **Top 18%, panel a — show why the task is hard.** On the left, a large reserved **actual experimental MS/MS stick spectrum**, with precursor/adduct and observed fragment m/z/intensity labels. Immediately beside it, two or three **same-formula, different-connectivity molecular-graph slots**. Use a minimal thin bracket under their overlapping predicted mass evidence, and a clear short scientific annotation **“A measured spectrum does not uniquely encode a molecular graph.”** A small gray subline explains **“No accepted reference match / limited structural evidence”**. Make the contrast immediately visible: the input spectrum is measured, but the precursor structures are competing hypotheses. Do not draw a ground-truth molecule as if it is supplied during unknown inference. Avoid fake peaks or molecules; preserve blank slots for chemically verified source images.
>
> **Middle 47% — the large WGV hypothesis–evidence mechanism, visually detailed enough to teach the method.** Start with **b: “G | Construct molecular hypotheses”**. Draw a horizontal 3-step growth trajectory **empty or motif-seeded partial graph → ring/motif attachment under precursor inventory → complete chemically valid molecular candidate**, with small action annotations **“select peak / grow / attach motif or ring”**. A narrow source strip under the growth path shows **“MMA | observed-peak-related fragment and motif hypotheses”** with two or three small reserved fragment graph slots and a teal upward link into the G trajectory. Include the word **“Canonical Hybrid: atom · ring · motif”** in tiny technical type. On the right edge of b, display two to three actual different connected candidate structures labelled **m1, m2, m3**, all compatible with the same permitted molecular formula. Under b put the consequence **“Addresses missing candidate structures and long graph-construction horizons”**. The reader should see what G physically creates, not merely a box called Generator.
>
> Immediately adjacent place **c: “W | Predict candidate-specific fragments”**. Show one or two candidate precursor structures each with a small *hypothesized* cleavage/fragment-support tree: a large molecular graph at root, two smaller **structure-bearing fragment graph insertion slots**, formula/neutral-loss/mass labels reserved as editable source-derived overlays, sparse arrows showing **candidate → possible fragment structures**. Add a tight annotation **“structure conditioned; target-spectrum blind”**. W receives a candidate molecular graph and acquisition context, and it **does not receive measured target product-ion peaks**. Avoid a fictional complete electron-flow mechanism. Show how the two different precursor candidates can yield some **shared fragment-mass support** but different **candidate-specific structural fragment hypotheses**. Under c put the consequence **“Provides chemically structured, candidate-specific evidence”**.
>
> To the right place **d: “V | Test structures against measured MS/MS”**. Draw two incoming narrow labeled paths converging at one comparison plane: a teal-gray arrow from W labelled **“predicted fragment structures + masses”** and a neutral dark thin line routed **directly from the actual spectrum in panel a** labelled **“observed MS/MS peaks”**. Within d show a small **candidate × observed-peak match matrix**: columns = 4–6 source-derived observed peaks; rows = candidate m1/m2/m3; distinguish **common explained peaks (gray)**, **candidate-specific supporting evidence (muted teal)** and **unexplained observations (light hatch)**. This is an evidence schematic, not an empirical heatmap; numeric values and peak identities will be inserted only from actual outputs. Place a narrow **ranked molecular structure / bounded alternative set** to the right, and a small text note **“same candidate pool; evidence changes ranking, not reach”**. Avoid marking a candidate as confirmed solely on the model score. Under d put the consequence **“Addresses reached-but-misranked and chemically ambiguous candidates”**.
>
> **Upper-flow connector accuracy is mandatory.** Measured MS/MS from a supplies the G spectrum encoder and, on a separate directed line, the V measured-evidence comparison. G's candidate graphs pass into W; W's fragment predictions pass into V; ranked candidates are produced by combining permitted G and W/V evidence. **Never connect the observed target product-ion spectrum to W.** A dashed small side arrow toward further G moves is allowed only when labelled **“optional online guidance, if implemented”**; depict terminal W/V reranking as the unambiguous actual capability. Make graph data dependencies intelligible without crossing large decorative arrows.
>
> **Lower 35%, panel e — a concrete Scientific Improver Agent RSI learning process, NOT a decorative loop.** Along the left side show three **real failure classes as tiny mini-cases**, visually related to the upper structural output:
> - **Failure I / G or knowledge gap:** “Correct structure absent from candidate pool”; visual: measured spectrum, ghosted target only inside a TRAIN-labelled audit, candidate shortlist lacks it. Example diagnosis: motif coverage / trajectory failure.
> - **Failure II / V discrimination gap:** “Correct structure present, ranked below close isomer”; visual: two competing same-formula candidate graphs with a small rank-order icon; diagnosis: insufficient or misweighted differentiating evidence.
> - **Failure III / unresolved evidence:** “Current fragment hypotheses do not support a unique distinction”; visual: shared fragment peaks and a bounded isomer set; diagnosis might call for further evidence rather than unconditional training.
>
> Send these TRAIN-only diagnostic observations to a middle-sized **“Scientific Improver Agent”** decision region with a short scientific three-step record, **“Observe failure → formulate testable chemical hypothesis → choose one intervention.”** Show tiny *example text only*, not an invented real agent decision: **“Hypothesis: missing motif causes candidate coverage gap”** / **“Expected: Reach improves”**. A separate strip called **“Previous episode memory”** feeds the decision region and displays three concise fields: **“Action / measured outcome / next hypothesis”**. This is not an LLM Chat UI.
>
> Next, draw an **actual action-routing strip** with four precisely named possible choices: **“Expand MMA knowledge”** (new transferable structural fragments and motifs), **“Improve G”** (train on valid difficult graph-growth trajectories or supported generated examples), **“Improve V”** (train on hard same-formula competing structures and fragment evidence), and **“Collect evidence”** (re-evaluate/train diagnostic packets before deciding). **Only ONE action is selected per episode**; show the decision as a single selected route with nonselected routes gray and subtle. Do not show all three neural models being blindly retrained at once.
>
> The chosen route reaches **“Execute existing training/analysis → Evaluate before vs after”**. Show a tiny source-ready outcome table with blank values for **“newly reached true structures”**, **“correct structures recovered at rank 1”**, **“previous successes lost”** and **“time / GPU cost”**. This illustrates exactly what is tested, without inventing improvements. When criteria are met, a teal return arrow updates the **next-generation MMA/G/V** state in the middle inference band; **W remains fixed in the initial controlled episode**. From the measured outcome, a SECOND thinner gray return path passes through **“Reflection + episode memory”** back to the Scientific Improver decision region. This is **knowledge/model recursion plus decision-memory recursion**; the LLM model parameters are not updated.
>
> At lower right, a small chemistry-centered destination caption: **“Goal: previously unresolved spectra become structurally more interpretable in the next generation”**. Provide two quiet before/after case slots for *actual source-derived* predicted structures and fragment evidence, with no fabricated score, no fake observed improvement and no “new molecules discovered” claim. Indicate “Scientific objective; experimental outcome to be supplied” if not measured.
>
> **Make the novelty and value legible:** The method does not merely increase the number of proposed SMILES. It uses chemical fragmentation to test competing hypotheses, diagnoses why inference failed, directs the next training investment and evaluates whether this enables new structure recovery. Emphasize the **structure-level scientific feedback** over the generic use of an LLM.
>
> **Formal visual quality:** confident but restrained typography, high-precision arrows, thick-enough molecular bond strokes, believable spectra, real chemical graph placeholders, original publication-grade visual hierarchy. No meaningless rounded rectangles, emojis, glowing algorithms, deep neural net brain imagery, generic three-column grid, fictitious ion reactions, fabricated m/z values or model-performance figures.

### Negative prompt

> Generic W/G/V three-box pipeline, empty labels without chemical states, giant architecture cards, chatbot screen, multiple anthropomorphic agents, fake instrument screenshot, random spectra, invented peaks, fantastical reaction mechanisms, invalid Kekulé molecular bonds, random chemical names, made-up same-formula alternatives, unverified neutral losses, fictional molecular-family network, fabricated accuracy values, invented RSI improvement, all three actions activated at once, LLM weights becoming trained after reflection, TEST ground truth flowing into agent, target spectrum entering W, input molecular graph revealed for unknown-query inference, thick looping arrows obscuring molecule drawings, low-resolution text, overly busy tiny stacked panels, dashboard infographic, RGB/gradient glow, stock research icons, DNA strands or tissues, large dark background.

## 5. Exact panel-to-message map for the final SVG/PDF

| Panel | Scientific question the figure itself answers | What a reviewer must see visually | Output object |
| --- | --- | --- | --- |
| **a** | Why can a spectrum fail to identify a unique precursor graph? | One real experimental spectrum and ≥2 same-formula *competing structural hypotheses*, no known graph supplied | Measured query and ambiguity |
| **b** | How does the method create *new* plausible molecular hypotheses rather than just retrieve a library item? | An actual staged select/grow/atom/ring/motif partial-graph sequence; MMA fragments and formula/chemical constraints | G-generated full molecular candidate pool |
| **c** | How can one use molecular chemistry to evaluate a proposed graph? | Candidate-conditioned structural fragment tree and meaningful fragment graph / ion-mass hypotheses without measured peaks as World inputs | W chemical evidence proposals |
| **d** | How does the observed spectrum distinguish close alternatives, and when does it fail? | W-predicted vs actual measured peaks per *candidate*, shared vs discriminatory support; rank or bounded isomer set | V-specific evidence and structural-resolution decision |
| **e** | How do repeated chemical inference failures make the next-generation system more capable? | Structured TRAIN-only failure classes; one specific agent scientific hypothesis/action; actual training or evidence gathering; before/after structural results; separate system and experience-memory returns | Reusable learning and next-generation WGV |

**Three key scientific annotations**, one per unresolved challenge, should be plainly typeset somewhere in the figure with small bold text:
1. **Coverage problem → chemically constrained hypothesis generation**
2. **Discrimination problem → structure-specific fragmentation evidence**
3. **Repeated failure → targeted agent-directed scientific learning**

## 6. Implementation evidence and what should be extracted from the source

The image generator is a design aid. The correct final chemistry must be assembled from specific model outputs:

| Needed illustration | Current source entry point | Extraction requirements |
| --- | --- | --- |
| Real MS/MS and candidate structures | `scripts/train_pr93_peak_ladder.py` `generate_case`, `evaluate`, generated/ranked rows, `outputs/pr93_paper_figures_20261109` | A single identical query ID in every upper panel; measured real peaks, exact candidate SMILES, admissible precursor mass/formula and ranking fields |
| G trace with meaningful decisions | `src/orbit_ms/wgv/peak_ladder_motif.py` `hybrid_trajectory`, `HybridStagePolicy`, `mstart`, `mattach`, `rstart`, `rattach`; `scripts/analyze_pr93_ladder_failures.py` | Source-derived partial molecular graphs, chosen peak, real atom/ring/motif attachment and chemical validity |
| MMA structural knowledge | `src/orbit_ms/wgv/peak_fragment_prior.py` `PeakFragmentLibrary.hypotheses`, `motif_graph`; PR95 MMA libraries | Actual peak-linked fragment/motif template and source-provenance information; no invented GT substructure |
| W candidate-conditioned evidence | PR95 `scripts/train_pr93_peak_ladder.py` `_get_wv_scorer`, `_wv_scores`; corresponding W inference/export | Candidate-specific predicted fragment-ion structures, ion masses and where possible atom lineage. Show finite candidate support, not proven mechanism steps |
| V measured-spectrum comparison | Same `generate_case` and frozen W/V scorer, V ranking / output details | Actual spectrum-to-fragment matches for each candidate and source-derived W/V evidence scores; shared vs discriminating peaks based on real data |
| RSI diagnosis and action | PR96 `src/orbit_ms/agents/scientific_improver.py`: `observation`, `choose`, `compare` | TRAIN FIT reach/ranking diagnosis, action among four typed choices, actual outcome + hypotheses |
| RSI execution and memory | PR96 `scripts/run_pr93_scientific_improver.py`: `start`, `advance`, `finish`, `previous_experiences` | Real promoted checkpoints, one decision/episode and reflection memory, not hypothetical autonomous accuracy |
| Historical real benchmark exemplar | PR95/SI `supplementary/ORBIT_WGV_RSI_Results.tex`, MassSpecGym 0002114 (cyclic tetrapeptide) | Source-backed *n*-propyl versus isopropyl competing connectivity; post-generation edit documented. Check raw spectrum and score receipts before drawing |

**Do not conflate analysis modes:** known-formula CAL, macro-core-assisted neural completion and true formula-blind de novo structure identification are distinct. A known-GT benchmark is acceptable to *illustrate* a success/failure, provided its GT is not drawn as an input to upper-lane unknown inference. The PR95 historical Gen 1–10 record contains human/scripted interventions; the PR96 agent code does not by itself establish measured autonomous multi-generation accuracy gains.

## 7. Design-to-final-asset workflow (for Codex/illustrator)

1. **First render the concept:** Feed the English master prompt to the image generator. Save a design concept preview separate from the paper figure; use it to assess composition, not chemistry.
2. **Select one complete source case:** Retrieve source spectrum and model outputs, create an `evidence_case_manifest.json` plus source-path references. A single inconsistent case across panels invalidates the worked example.
3. **Make the chemical drawings:** RDKit generates all 2D molecule and fragment SVGs, same bond-length scale wherever possible. Avoid rescaling molecule drawings with non-uniform X/Y dimensions. Use vector stick spectra with all actual measured peaks. Draw structural fragment maps only from exported model support, and use real chemical differences.
4. **Create the scientific layout:** Vector graphics via SVG / Inkscape / Illustrator / Python, with precisely traced input edges. Use literal strings that remain readable at print scale. Diagram should include scientifically meaningful arrows and not use five big rounded colored cards.
5. **Agent RSI inset:** Show action grammar and two feedback routes; only insert quantitative before/after or specific past memory from an actually completed measured PR96 episode.
6. **Export:** `figures/fig1_orbit_ms_method_overview.pdf`, editable SVG, source graph/plot script and `evidence_case_manifest.json` with provenance, plus a low-resolution preview. For the current PR, these are deliverables **to be produced later**, not files currently present.

## 8. Draft Figure 1 caption

**Fig. 1 | From ambiguous tandem spectra to evidence-guided and recursively improvable molecular structure elucidation.** **a**, A measured precursor and tandem fragment spectrum may be compatible with multiple molecular connectivities even under a common elemental composition. **b**, The spectrum-conditioned Generator proposes legal molecular graphs through peak-ladder reasoning and Canonical Hybrid atom, ring and MMA motif construction, expanding the candidate structures available for further evaluation. **c**, For each precursor hypothesis, the fragmentation World predicts chemically represented fragment and ion-mass candidates without accessing the measured target product-ion spectrum. **d**, The Verifier compares these World predictions with the actual experimental MS/MS to evaluate common and candidate-specific fragment evidence, yielding ranked molecular hypotheses or a bounded structural interpretation. **e**, On labelled training failures, a Scientific Improver Agent identifies the main unresolved capability, chooses one bounded knowledge, Generator, Verifier or evidence-collection intervention, and evaluates the effect on structural recovery. Updated MMA/G/V knowledge and episode reflection follow separate feedback routes to later model inference and agent decisions, respectively. The goal is to progressively extend the set of molecular structures that can be recovered from metabolomic dark matter.

## 9. Acceptance test: does the Figure 1 actually explain the scientific solution?

Before accepting the image concept or final vector figure, a colleague unfamiliar with ORBIT-MS should be able to answer *from the picture alone*:

- **Why not infer a SMILES directly?** Sparse MS/MS cannot uniquely encode connectivity; G must propose candidates under chemical constraints.
- **Why not stop after generating more candidates?** A correct graph can be present but ranked below plausible same-formula alternatives.
- **What is the World doing?** It predicts precursor-specific structural fragment hypotheses, *without target experimental peaks as input*.
- **What is the Verifier doing?** It tests those fragment hypotheses against actual observed ions, including candidate-specific discriminating evidence.
- **Why is MMA important?** The chemical fragment/ring resource changes how G builds molecular graphs and can be expanded through supported experience.
- **What does the Agent actually decide?** It selects which chemical capability to learn next on the basis of diagnosed TRAIN failures and recorded previous experiments.
- **What is recursively improving?** The chemistry resources and G/V models, plus the subsequent Agent decision context (via experience memory); W is initially fixed.
- **What is the actual scientific payoff?** Fewer unresolved structures and more reliable, interpretable chemical hypotheses, with the benefit measured on new molecules rather than merely claimed from the diagram.

**If a viewer can only recite “spectrum goes into G, then W, then V, then Agent”, the figure has failed and must be redesigned.**
