# Figure 1 — ORBIT-MS METHOD OVERVIEW: text-to-image prompt

**Paper:** *ORBIT-MS: Self-improving molecular structure elucidation of metabolomic dark matter*  
**Figure 1 title:** *Evidence-guided molecular elucidation and agent-directed recursive self-improvement in ORBIT-MS*  
**Purpose:** A scientifically precise **METHOD FRAMEWORK FIGURE**, not a public-metabolomics census or chemical-discovery results plot.  
**Revised manuscript contract:** \`main.tex\` → \`\\figureonetodo\` → panels **a–e** → \`fig:orbit_method\`.  
**Final figure file:** \`figures/fig1_orbit_ms_method_overview.pdf\`; final editable SVG and source drawings required.

## 1. Essential scientific message

This is the **main ORBIT-MS methods figure**. In one coherent image, show how a measured tandem spectrum becomes a set of molecular hypotheses, how the fragmentation World generates candidate-specific evidence, how the Verifier uses that evidence to distinguish alternatives, and how the Scientific Improver Agent learns from failures to update the chemical system for the next generation.

There are **two linked loops, and they must be visibly different**:
- **Within-sample inference:** measured MS/MS → molecule generator G → candidate-specific fragmentation World W → experiment-conditioned Verifier V → structure ranking / bounded resolution. A shared chemical knowledge library MMA supplies graph-building motifs and ring/fragment evidence.
- **Across-generation scientific RSI:** known-identity **TRAIN FIT** failures and previous episode outcomes → Scientific Improver Agent → one typed intervention (expand MMA / improve G / improve V / collect evidence) → actual training/evaluation → persistent reflection/experience memory → next-generation decisions and improved WGV capabilities.

**Precise information boundary:** W is **structure conditioned but blind to the observed target product-ion peaks** during forward fragmentation; V receives both predicted W fragments and measured experimental MS/MS. During deployment on unknown dark spectra, the true precursor structure is NOT available. Ground-truth labels are available only in a separate TRAIN FIT diagnostic/training lane. Initial controlled RSI freezes W and updates MMA/G/V, not LLM weights. This distinction should be evident without a sprawling validation checklist.

**Positioning:** This is an AI-for-chemical-discovery paper, so the visible scientific subject should be **real tandem mass spectra, chemically valid molecular graphs, evidence-supported structural alternatives and a learning loop that expands chemically resolvable space**. The figure is NOT a generic LLM multi-agent diagram. Methods architecture dominates Figure 1; actual dark-metabolome population counts and discovery results belong to later figures or Extended Data, not this figure.

## 2. MASTER TEXT-TO-IMAGE PROMPT — ready to copy

> Design a clean, serious, high-impact **scientific framework figure (Figure 1: METHOD OVERVIEW)** for a Nature Machine Intelligence paper titled **“ORBIT-MS: Self-improving molecular structure elucidation of metabolomic dark matter.”** The method is a chemically constrained World–Generator–Verifier (WGV) system with a lightweight scientific Agent conducting recursive self-improvement (RSI).
>
> **Core visual narrative:** A real experimental MS/MS is an incomplete measurement. A structure Generator proposes multiple chemically valid precursor molecules. A forward fragmentation World predicts chemically represented fragments for each candidate without seeing the target product-ion spectrum. A Verifier uses the measured MS/MS to judge the candidates and produces ranked or bounded structural hypotheses. Failures observed on labelled training examples are diagnosed by a Scientific Improver Agent, which selects one of a few pre-existing learning interventions; those experiments update the MMA knowledge library, Generator or Verifier. The measured outcomes and the Agent's reflection enter persistent memory, guiding the following generation.
>
> **Canvas and style:** Wide landscape, **16:9 or around 1.65–1.8:1**, targeting 3500–4000 px across for conceptual render; designed for a 180-mm two-column journal figure. White background, sharp flat vector-like lines, balanced negative space, carefully aligned 1-pt connectors and small panel letters (a–e). A sophisticated analytical-chemistry layout: no decorative elements, no 3D objects, no gradients, no marketing glow, no broad tinted containers or rounded SaaS cards. Use charcoal #263238, low-saturation blue-gray #637C89, dark slate #566D78, muted teal #4A8884, light gray #CED6D9. Black/gray molecular drawings. Emphasis comes from composition and actual chemical information, not colors.
>
> **Overall layout:** A compact horizontal upper portion (~57–62% height) for **inference and chemical evidence**; a thin horizontal divider; a wide lower portion (~38–43% height) for **agent-directed scientific RSI**. Design an integrated flow, not five disconnected equal-size boxes. Use **four small lettered stages a–d on the upper level**, while **e covers the lower cross-generation learning mechanism**. A narrow vertical guide line on the left separates **inference on an unknown spectrum** (no known structure) from **labelled TRAIN FIT failure analysis** in the bottom loop. Make the chemical content visually dominant and the text subordinate.
>
> **Panel a — Experimental observation / unknown query (upper-left, ~20% width).** A precise black stick-spectrum insertion area labelled **“Experimental MS/MS”**, with small neutral metadata labels **“precursor m/z”**, **“adduct”** and **“fragment m/z, intensity”**. Place an understated compact “formula hypotheses” strip under or beside the spectrum, from measured precursor/adduct evidence. Add a small subtitle **“Unannotated precursor”**. This is the *only* real measured spectral input; draw a clear slim connector from this spectrum directly to G **and separately to V**. Do not show the target SMILES, real molecular formula ground truth, fingerprint, or a fabricated exact m/z list at inference.
>
> **Panel b — G: chemistry-constrained molecular hypotheses (~25% width).** Title **“Generator G”**, small subtitle **“Spectrum-conditioned graph construction”**. Show a short staged graph-build sequence with three visually plausible two-dimensional molecular graph insertion slots: **atom → ring/motif attachment → complete candidate structures**. Include a tiny connected lower mini-band **“MMA: fragment and ring knowledge”** with short teal lines feeding into G; the MMA library is a reusable chemistry resource, not a neural text agent. Show two or three competing candidate-structure slots \`m1, m2, m3\` with the **same precursor-composition constraint**, but visibly distinct 2D connectivity in the eventual source-derived SVG. A small optional caption **“Canonical Hybrid: atom / ring / motif”**. No claims that candidate m1 is true without measured case evidence.
>
> **Panel c — W: candidate-conditioned forward fragmentation (~24% width).** Title **“Fragmentation World W”**, subtitle **“Spectrum-blind forward evidence”**. A candidate molecular graph passes into a narrow, chemically interpretable fragment tree: precursor graph → two or three **structurally represented fragment slots** connected by thin arrows; small neutral-loss / formula evidence labels as reserved insertion fields. Crucially, the measured target spectrum from a must **NOT** connect into W. W sees only the candidate structure and permitted acquisition context. It predicts *candidate-dependent chemical fragment hypotheses*, not a demonstrated unique electron-flow reaction mechanism. Do not invent electron-pushing arrows, charged rearrangement intermediates or actual fragment structures in the generated concept: reserve clean slots for source-derived RDKit SVGs.
>
> **Panel d — V: experimental evidence and molecular resolution (upper-right, ~28% width).** Title **“Verifier V”**, subtitle **“Match fragment hypotheses to observed MS/MS”**. Two thin labelled connectors converge into V: one from **W structural fragments**, one from **a experimental peaks** (a direct overhead/baseline routed arrow, not through W). A compact alignment view contains reserved lines for matched measured ions and candidate-specific fragment support, with a visually evident distinction between shared peaks and discriminative peaks. To the right, show an elegantly typeset **ranked alternative-structure output** labelled **“Evidence-supported hypotheses”**, with either a top-ranked 2D graph or a small **bounded isomer set** when evidence is insufficient. Use neutral rank labels and optional uncertainty notation, no fake confidence percentages. In this schematic, a thin **dashed local guidance** path from evidence to subsequent G steps may be shown only with the label **“optional online guidance; implementation-dependent”**; the clearly implemented comparison is **terminal W/V reranking** on completed G candidates. Do not depict an unsupported always-on iterative repair loop as completed science.
>
> **Panel e — Agent-directed recursive self-improvement (full-width lower band).** Use a relatively large but sparse flow with **two distinct feedback paths**, titled **“Scientific Improver Agent — recursive chemical learning”**. Start at the left with a compact **“TRAIN FIT failures / measured past episodes”** observation area, not unknown-test ground truth. Show three actual diagnostic meanings in small aligned labels: **“Correct graph not reached”**; **“Candidate reached, misranked”**; **“Missing transferable motif / fragment knowledge”**. Next place a restrained, prominent central node **“Scientific Improver Agent”** with short sublabels **“Diagnose → hypothesis → choose intervention”**. Then a tidy three-branch intervention strip **“Expand MMA knowledge”**, **“Train G”**, **“Train V”** plus a smaller textual alternative **“Collect evidence”**. Do not represent them as independent competing robot agents; they are existing computational training actions.
>
> Immediately after those actions, show a right-side narrow **“Execute & evaluate”** stage containing only *before/after structural recovery*, reach/ranking changes and a real experiment receipt/checkpoint icon made of thin rectangles. From there show the **first feedback**: a strong but thin muted teal arc returning **updated MMA / G / V** to the upper inference pipeline of the *next generation*, labelled **“WGV capability update”**; W remains labeled **“fixed during initial RSI experiment”**. Show the **second feedback**: an unobtrusive lower curved line from evaluation to **“Reflection + episodic memory”**, then back into **Scientific Improver Agent**, labelled **“experience for next decision”**. These are distinct loops: system-parameter / knowledge adaptation versus agent-context / decision adaptation. The underlying Agent LLM is not weight-updated here.
>
> At the end of the lower band, a compact phrase **“Next generation: expand recoverable chemical space”** connects the full scientific method to dark-metabolome analysis. Make this phrase the clear scientific purpose of self-improvement, not a floating performance number.
>
> **Chemical credibility:** Molecular drawings are expected to be final **real RDKit-derived 2D structures**, spectrograms are final **real experimental tandem MS/MS** and fragmentation details are source-supported. For the concept image, use clearly reserved blank insertion slots and technical labels if exact molecular data are not provided. Do not hallucinate molecule atom connectivity, molecular formulas, mass values, reaction pathways or spectra. Use correct arrows that make the data dependencies unambiguous: measured MS/MS goes to G and V, candidate graphs go to W, W fragment hypotheses go to V, V evidence scores go to terminal ranking. The Agent is outside the per-spectrum inference path and operates on training diagnostics to improve the next-generation system.
>
> **Editorial finishing:** A researcher should understand at first glance how ORBIT-MS thinks about a molecule, how it obtains candidate-specific fragmentation evidence, and how its scientific learning loop changes the next generation. Scientific diagrams in Nature Machine Intelligence are compact, technically accurate and restrained. No random icons or marketing language; moderate text density, precise alignment, true hierarchy and publication-like typography.

### Negative prompt

> Dark metabolome census funnel, 613331 unknown spectra as the dominant graphic, population scatterplot, chemical-space UMAP, molecular family network, full-figure benchmark plot, oversized biological tissues, generic AI startup infographic, 3D ball-and-stick molecules, random bonds, fictional smiles, fake chemistry, made-up MS/MS peaks or numerical mass fragments, decorative electron pushing arrows, fabricated neutral losses, gigantic W/G/V rounded feature cards, overcomplicated algorithm flowchart, chatbot UI, robotic scientists, colorful icons, gradient fills, glossy reflections, neon effects, thick loop arrows, multiple redundant circular cycles, exaggerated big arrows, illegible text, over-detailed background, generic three-column symmetry, false test-ground-truth in unknown inference, observed experimental spectrum entering the World, Verifier scoring molecules without the measured spectrum, LLM weights automatically trained by each agent reflection.

## 3. Required elements and truthful information boundaries

| Feature | Must be shown | Must not be depicted |
| --- | --- | --- |
| Experimental query | Measured precursor/product ions, available adduct metadata and predicted formula hypotheses | Target precursor graph or target fingerprint as an inference input |
| G / MMA | Existing PR95 Peak-Ladder / Canonical Hybrid using atom, ring and motif actions; MMA provides reused fragment/ring knowledge | MMA as generic text retrieval / prompt library |
| W | Molecular graph-conditioned structural fragment prediction, spectrum-blind at test inference | Experimental target peaks entering W, guaranteed true intermediate structures, universal CID mechanism |
| V | W fragment hypotheses **plus measured MS/MS** enter a candidate-specific evidence comparison; ranked or bounded structural output | Only structural prior without measured peaks, certainty where alternatives persist |
| Inference vs RSI | Unknown dark MS/MS upper lane; labelled TRAIN FIT evidence lower lane | Dark-sample GT structures shown to Agent during deployment or test-set labels used for training |
| Agent | Scientific diagnosis → one typed action → actual learning/evaluation → reflection and memory → next decision | Free-form code modification, multiple anthropomorphic agents, automatic LLM parameter updates |
| Model adaptation | MMA/G/V learning can change the next model generation | W updated in the initial controlled PR96 RSI (it is held fixed) |

**Implementation sources:** [orbit-ms PR95](https://github.com/wangyu-sd/orbit-ms/pull/95) (G, W, V and MMA development), [orbit-ms PR96](https://github.com/wangyu-sd/orbit-ms/pull/96) (Scientific Improver action grammar and bounded episode memory), current [MS-paper main.tex](https://github.com/wangyu-sd/MS-paper/blob/main/main.tex) (method claims).

## 4. Panel/source preparation for the final journal figure

**Panel a:** Select one actual experimentally measured, source-identified query spectrum from a known-identity development case or independent public unknown case. Provide precursor m/z, adduct, collision energy if available and the real stick spectrum (not synthetic peaks).

**Panel b:** Export two or three *actual G proposals* for that SAME spectral query as chemically valid RDKit SVG, including one difficult competing connectivity if present. Capture two or three genuine intermediate partial graphs showing atom/ring/motif construction. If no real intermediate state was saved, use a generic labeled placeholder rather than constructing false graph states.

**Panel c:** Extract W's actual structural fragment support on those exact candidate graphs. Draw only source-backed fragment graph and neutral-loss links; label proposed fragment assignments as predictions rather than experimentally observed fragment structures.

**Panel d:** Compute V evidence on the same measured spectrum and candidate pool; provide source-backed fragment matches, molecular ranks and resolution status (unique putative vs bounded alternatives). Do not reassign the correct rank just for a figure.

**Panel e:** Use real PR96 episode receipts and memory traces *when available* to illustrate a measured Agent selection, model/knowledge change and next-generation performance. Until then use a strictly **schematic** action/loop layout labelled “Proposed RSI workflow”, not pseudo-real training curves, invented metrics or a Gen0–Gen3 improvement chart.

### Output artifacts

- **Design exploration only:** \`figures/mockups/fig1_orbit_ms_method_overview_concept.png\` (when actually generated), labelled *conceptual visualization*. This PR includes a prompt, not an image.
- **Final:** \`figures/fig1_orbit_ms_method_overview.pdf\`, corresponding editable SVG, real spectrum and RDKit component SVGs, and source/plot script. Do not directly upscale the raster concept as the final paper figure.
- **Panel lettering / caption:** a–e and the LaTeX filename/label must match \`main.tex\`.

## 5. What to review in the first concept image

1. A reader follows the upper evidence flow **spectrum → G → molecular candidates → W → V → ranked/bounded structural hypotheses** without tracing long arrows.
2. The measured spectrum **enters V separately** and does not enter W.
3. G's multi-granularity chemistry and MMA evidence, and W's structured fragments, are visually recognizable as chemistry, not text-only abstractions.
4. RSI is a **distinct lower band** operating on TRAIN diagnostics, with one action choice and two different feedback loops (WGV capability, agent experience memory).
5. Method emphasis does not crowd out real molecular structures and spectrum slots; the diagram remains clean at journal scale.
6. No public MS/MS dataset counts, biological group analysis, molecular-family scatterplots or benchmarking bar charts in Figure 1. Those are results, not this method overview.

## 6. Caption draft

**Fig. 1 | Evidence-guided molecular structure elucidation and agent-directed recursive self-improvement in ORBIT-MS.** **a**, An experimental tandem spectrum and precursor/adduct information provide spectrum-conditioned input without a known molecular structure. **b**, The Generator uses chemically legal atom, ring and MMA motif operations to construct competing precursor graphs. **c**, The fragmentation World predicts candidate-specific structural fragment hypotheses independently of the measured target fragment peaks. **d**, The Verifier evaluates those hypotheses against the observed spectrum to rank or bound the surviving molecular alternatives. **e**, A Scientific Improver Agent diagnoses training-spectrum failures, selects a bounded intervention to update MMA, G or V, and learns from recorded experimental outcomes through persistent episode memory. Updated chemical capabilities and decision experience are carried into the next round of molecular structure elucidation.

**Editorial principle:** Figure 1 answers **“How does ORBIT-MS work, and what recursively changes?”** The following figures answer **“How much chemistry can it resolve, and what can it discover?”**
