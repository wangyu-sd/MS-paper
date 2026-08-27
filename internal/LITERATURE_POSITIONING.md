# Literature Positioning

What the neighbouring work actually claims, what won it the venue it got, and where this manuscript sits. Written to prevent two failure modes: claiming novelty that does not survive contact with the literature, and claiming an advantage the literature says we do not have.

## The two Nature precedents, and what actually won them Nature

**Gentry et al., *Nature* 2023 — reverse metabolomics.** Combinatorially synthesized four metabolite classes, acquired reference spectra, then mined public repositories with MASST. Found 145 compounds in public data, 139 previously undescribed, and linked bile amidates to Crohn's disease across four cohorts, with effects on IFN-γ production in CD4⁺ T cells and PXR agonism, plus bacterial culture showing production.

What won it was **a general discovery strategy plus a disease association plus functional evidence** — not the 139 structures. Note also that its annotations were at MSI level 2/3: even in *Nature*, isomeric alternatives were left unresolved and stated as such. This is direct precedent that honest partial resolution is publishable at this level.

**Qiang et al., *Nature* 2026 — DeepMet.** A chemical language model trained on the SMILES of roughly 2,000 known metabolites anticipates metabolites that have not been observed; predicted spectra for those structures expand an in-silico library; matching against 29.1 M MS/MS spectra from 4,510 public human blood analyses raises annotation rates; 36 previously unrecognized mammalian metabolites reported.

What won it was **the demonstration that metabolite chemical space is learnable and can be extrapolated**, with the 36 metabolites as proof. Its constraint is structural: the prior is built from known metabolites, so it reaches chemistry adjacent to what is already characterized.

**Implication for us.** Both papers win on a general claim about *how discovery works*, with molecules as demonstration. A manuscript whose contribution is "we resolved N structures" will not clear this bar on either the computational or the wet-lab side.

## Pure wet-lab metabolite discovery: the bar is function, not structure

Recent *Nature* papers discovering individual metabolites — Lac-Phe (*Nature* 606:785, 2022), mandimycin (2025), the depsipeptide MKM-A (2026) — share a pattern: **structure elucidation is never the contribution.** Lac-Phe is a trivially simple lactate–phenylalanine conjugate; what carried it was CNDP2 as the synthesizing enzyme, knockout mice that eat more, chronic administration reducing adiposity, and conservation across mice, humans and racehorses. Mandimycin came with a BGC knockout and a membrane target; MKM-A with a cryo-EM structure bound to the ribosome E-site and resistance mutations.

Pure structure discovery without function lands in specialist journals (*J. Antibiot.*, *Nat. Commun.*), where "four new hydroxy fatty acids, structures by NMR, weak MIC" is a normal paper.

**Implication for us.** Under the current constraint of no new acquisition and standards only, the function-first route is closed. We cannot win on biology alone, which is why the conceptual and resource claims are not optional decoration — they are the only available lane.

## De novo structure generation: a race we should not enter

State of the art at time of writing: MS-GPT reports Top-1/Top-10 of 29.8%/41.1% on NPLIB1 and 23.9%/28.7% on MassSpecGym; MetGenX reports 55.9% Top-1 on NIST spectra and 68.5% on real biological samples via structure-to-structure generation; FlowMS, DiffMS, MADGEN and FRIGID occupy the graph-diffusion and flow-matching lines.

These numbers are not commensurable across papers. A critical review of the field puts leakage-controlled MassSpecGym performance at roughly **4.1% Top-10**, and attributes the gap to naive splits and to pretraining corpora overlapping the test set. "MassSpecGym in the Wild" documents the same pattern and releases analogue-excluded pretraining sets.

**Position.** We do not claim to beat these systems at exact-match accuracy, and the manuscript must not invite that comparison. METEOR is a component that supplies candidates where retrieval has none. Our claim concerns the form and reliability of the output, not its rank-1 accuracy. Where we do report accuracy, it is under MCES-controlled splits with a full analogue-leakage audit, and comparator numbers are recomputed by us on identical pools rather than quoted from papers.

## Mechanistic fragmentation: the literature says we are slower and less accurate

This is the most dangerous claim boundary in the manuscript.

CFM-ID 4.0 combines 313 hand-curated fragmentation rules with a learned module. The ICEBERG authors state plainly: *"We recently found CFM-ID to be far less accurate than black-box neural networks, an observation separately confirmed by Murphy et al."* They also note CFM-ID would need roughly three months on a 64-core machine to train on 300,000 spectra. Combinatorial approaches are described throughout the literature as slow and as over-generating fragments.

**Position.** Any sentence implying "mechanism is more accurate than learned models" will be rejected by a knowledgeable reviewer with a citation. The manuscript's claim is different and must be stated precisely: mechanistic enumeration produces **eliminations** — statements that a candidate cannot reach an observed mass — and eliminations compose, carry provenance, and can be calibrated to a measured false-exclusion rate. Learned similarity scores cannot, which is why they cannot underwrite a resource. Accuracy is not the axis; controllability is.

Two corollaries. First, we must report our own in-distribution accuracy honestly even where comparators win. Second, the automated rule evolution (§3, ED6) is the direct answer to the standing objection about hand-curated rule sets, and should be framed that way rather than as agent research.

## Analogue propagation: the dominant discovery mode, and its blind spot

The productive strategies in this field all locate new molecules by similarity to known ones:

- **Nearest-neighbour suspect library** — 87,916 unique spectra derived from 521 M spectra across 1,335 projects by propagating annotations along mass differences; roughly doubles annotation rates.
- **MetDNA3 / KGMN** — propagation along curated and predicted metabolic reaction networks.
- **COSMIC** — confidence scoring over fingerprint-based retrieval, trained on 16,703 structures, yielding 1,715 novel high-confidence annotations at repository scale.
- **DeepMet** — a learned prior over known metabolite structures.
- **Reverse metabolomics** — combinatorial analogues of a chosen known class.

**Position.** This is a strength of the field, not a weakness, and the manuscript should say so. But it defines a blind spot: chemistry not adjacent to anything characterized is systematically out of reach of every one of these methods. Section 3's composition analysis measures the size of that blind spot, which is why it is a finding rather than an opinion. Mechanistic elimination does not depend on similarity to known chemistry, which is why it reaches into that region at all.

Do not state the blind spot as a criticism of these works. State it as a measurement.

## The community has asked for exactly this output

Bittremieux et al. (*Metabolomics* 2022) state the problem qualitatively and call for the tool:

> Analyzing non-discriminative MS/MS spectra is equivalent to searching a genetic sequence database with a two-mer oligonucleotide.

> The goal of these tools should be to clearly communicate the maximum amount of knowledge that can be derived from the mass spectral data and then follow up with additional experiments to differentiate among all possible annotations.

The confidence-level conventions that encode this idea (Schymanski et al. 2014) are assigned by human judgement rather than computed.

**Position.** This is our strongest framing citation: a well-recognized, frequently restated, never-quantified problem with an explicit community request for the capability we deliver. Cite it in the introduction and return to it in the discussion.

## What is genuinely new here

1. **Resolution level computed from evidence** rather than assigned by convention, via mechanistic elimination.
2. **Calibration against prospective library growth** — a blinded assessment in which answers were produced by independent laboratories after predictions were frozen. We are not aware of this design being used in this field.
3. **A structure-based estimate of the size of the dark metabolome**, obtained by collapsing features onto entities on chemical rather than spectral grounds. The field currently cannot state this number.
4. **Composition of the dark metabolome by distance from characterized chemistry**, quantifying the blind spot above.
5. **Biological origin attribution by mining perturbation experiments others already performed**, which makes attribution possible without a wet-lab budget.

## What is not new and must not be claimed as new

- Repository-scale mining of public metabolomics data (MASST, ReDU, suspect library, COSMIC).
- Executable fragmentation modelling (MetFrag, MAGMa, CFM-ID, SIRIUS, ICEBERG).
- De novo structure generation from spectra.
- Self-supervised representation learning over unannotated spectra (DreaMS), which also supplies the corpus we use.
- The observation that MS/MS often cannot distinguish isomers.
- Conformal or risk-controlled prediction sets in chemistry.

## Citation policy

Peer-reviewed work carries every essential claim. Preprints provide frontier context only. Comparators must include mature methods (SIRIUS/CSI:FingerID, CFM-ID) alongside modern generative ones, with versions and configurations reported. Where the literature contradicts a convenient framing — as it does on mechanistic accuracy — the manuscript cites the contradiction rather than omitting it.
