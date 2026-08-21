# Peer-reviewed literature positioning

This document defines the competitive landscape used to write the manuscript. The central argument is grounded primarily in peer-reviewed work; preprints can be acknowledged as frontier context but must not carry the manuscript's essential scientific claims.

## Nature-level external scaffold

Three recent Nature papers now provide the highest-authority framing for the manuscript, but they serve different purposes and must not be over-read.

1. **Alexandrov & Zamboni, Nature Perspective (2026)** establishes that metabolite identification remains a shared challenge as metabolomics expands from single-cell to population scale and towards metabolic atlases/foundation models. It supports the **importance and persistence of the identification problem**, not the specific evidence-bottleneck mechanism.
2. **Qiang et al., DeepMet, Nature (2026)** demonstrates that chemical language models plus predicted MS/MS can substantially advance mammalian metabolite hypothesis generation and prioritization. The same work explicitly requires matched reference standards for high-confidence annotation and reports candidate assignments that fail retention-time or spike-in validation despite substantial MS/MS agreement. It therefore supports the distinction **generation/spectral agreement ≠ established chemical identity**.
3. **Gentry et al., Reverse metabolomics, Nature (2024)** explicitly notes that many computational strategies can match structures to MS data while leaving no easy path to determine which possible matching structure is correct. It supports the unresolved **verification/alternative-discrimination gap**.

The manuscript should therefore not claim that ambiguity or validation has been ignored by the field. The sharper contribution is:

> The field already recognizes that computational plausibility does not establish molecular identity. ORBIT-MS identifies how this gap becomes systematically limiting as candidate hypotheses improve, formalizes the missing object as discriminative fragmentation evidence relative to competing structures, and tests whether that evidence must adapt with the hypothesis space.

| Work | Venue | What it established | What ORBIT-MS must not re-claim | ORBIT-MS distinction |
|---|---|---|---|---|
| CSI:FingerID (Dührkop et al., 2015) | PNAS | spectrum/fragmentation-tree to molecular fingerprint for database search | fingerprint-based retrieval | candidate-specific evidence evaluated directly against hard alternatives |
| SIRIUS 4 (Dührkop et al., 2019) | Nature Methods | integrated formula/structure inference using fragmentation trees and CSI:FingerID | generic “turn MS/MS into structure information” | asks how discriminative evidence changes when alternatives become harder |
| CFM-ID 4.0 (Wang et al., 2021) | Analytical Chemistry | rule/probability-based ESI-MS/MS prediction and compound identification | fragmentation-aware candidate scoring | atom-traceable, competitor-relative evidence rather than spectrum fit alone |
| CANOPUS (Dührkop et al., 2021) | Nature Biotechnology | compound-class annotation of unknown spectra and biological deployment | class-level interpretation of unknown metabolomes | attempts structure-level contraction with calibrated fallback to lower resolution |
| COSMIC (Hoffmann et al., 2022) | Nature Biotechnology | confidence-aware structural annotation beyond spectral libraries | confidence scoring alone | risk control is tied to candidate-specific chemical evidence and candidate recall |
| MSNovelist (Stravs et al., 2022) | Nature Methods | de novo structure reconstruction from predicted fingerprints | fingerprint-to-SMILES generation | focuses on the evidence needed to adjudicate generated alternatives |
| BUDDY (Xing et al., 2023) | Nature Methods | bottom-up MS/MS formula discovery and FDR-aware formula inference | formula-space contraction | discrimination within same-formula structural candidate sets |
| MIST (Goldman et al., 2023) | Nature Machine Intelligence | domain-inspired spectrum transformer with formula/neutral-loss inductive bias | domain-aware spectrum encoding | separates chemical prior from experimental identity evidence and adapts the evidence model |
| Reverse metabolomics (Gentry et al., 2024) | Nature | computational matching leaves a verification gap over possible matching structures; reverse search grounds discovery in synthesized structures and repository data | claiming that the field never recognized the verification problem | operationalizes peak-level evidence for discriminating the competing structures rather than bypassing the ambiguity through synthesis-first search |
| MassFormer (Young et al., 2024) | Nature Machine Intelligence | strong forward-spectrum prediction with graph transformers | forward simulation | explicitly separates simulation from candidate discrimination |
| MassSpecGym (Bushuiev et al., 2024) | NeurIPS Datasets & Benchmarks | standardized leakage-resistant de novo/retrieval/simulation benchmark | benchmark construction | uses hard candidate strata to expose candidate/evidence co-difficulty |
| DiffMS (Bohde et al., 2025) | ICML | formula-constrained graph diffusion and structure-only decoder pretraining | formula-constrained de novo generation | provides an external candidate distribution for testing adaptive evidence |
| Coverage bias (Kretschmer et al., 2025) | Nature Communications | structural coverage can dominate apparent small-molecule ML performance | generic split criticism | motivates explicit pretraining leakage audit and matched candidate-difficulty analysis |
| FIORA (Nowatzky et al., 2025) | Nature Communications | bond-local fragmentation-event modeling improves forward MS/MS prediction | explainable forward fragmentation | evaluates atom-traceable fragmentation for GT–decoy specificity, not only spectral similarity |
| DreaMS (Bushuiev et al., 2026) | Nature Biotechnology | repository-scale self-supervised spectrum representation and 201M-spectrum atlas | foundation-model scale or spectral embedding novelty | uses unlabelled spectra as deployment data while focusing on evidence and structural falsification |
| MetGenX (Wang et al., 2026) | Nature Communications | structure-informed de novo generation and mouse-liver unknown-metabolite discovery | “we generated unknown mouse metabolites” as sufficient novelty | mouse deployment must show blinded calibration, alternative rejection and orthogonal validation |
| DeepMet (Qiang et al., 2026) | Nature | language-model anticipation of mammalian metabolites; candidate prioritization using molecular prior plus predicted MS/MS; high-confidence confirmation with matched standards and orthogonal analytical evidence | chemical-language generation, mammalian-metabolite anticipation, or “MS/MS prediction + prior” as novelty | studies the next bottleneck after strong generation: which observations distinguish close alternatives and how to retain unresolved ambiguity when spectral agreement is insufficient |
| Metabolomics across scales (Alexandrov & Zamboni, 2026) | Nature Perspective | metabolite identification remains a shared bottleneck across single-cell and population-scale metabolomics and future atlas/foundation-model efforts | claiming the Perspective established the ORBIT evidence-bottleneck mechanism | positions evidence-limited identity resolution as a scaling constraint that remains relevant as metabolomics models and atlases grow |

## Editorial positioning

The Nature-level proposition is **not**:
- a larger mass-spectrometry language model;
- an agent workflow;
- a new forward-spectrum simulator;
- another de novo generator;
- another benchmark leaderboard gain;
- a set of unvalidated mouse structures;
- “CoT works for chemistry”.

The working proposition is:

> As molecular alternatives become more faithful, fixed spectral evidence loses discriminative power. Molecular structure elucidation therefore benefits from adaptive, candidate-specific fragmentation evidence that is evaluated relative to the alternatives actually under consideration.

This language is deliberately narrower than “co-evolving experimental evidence”. The experimental spectrum itself remains fixed unless a new measurement is physically acquired.

## Four distinctions to defend throughout the paper

### 1. Simulation ≠ explanation
A forward model can reproduce an observed spectrum without identifying a unique causal fragmentation trajectory.

### 2. Explanation ≠ discrimination
A chemically plausible fragment can be shared by the ground truth and every hard decoy. Figure 2 therefore evaluates evidence on matched competing structures.

### 3. Discrimination ≠ end-to-end identification
Even a perfect evidence model cannot recover a ground truth absent from the generated candidate set. Candidate recall, conditional discrimination and end-to-end resolution must be reported separately.

### 4. Prediction ≠ identification
A unique generated SMILES for a dark mouse spectrum remains a hypothesis until the evidence level supports unique resolution and, where identification is claimed, orthogonal validation is obtained. DeepMet provides a recent Nature-level example of why this boundary matters: substantial MS/MS agreement can still fail orthogonal analytical validation.

## Comparator priority

The hard-decoy evidence benchmark should include mature peer-reviewed comparator families wherever technically executable:

- exact-mass / formula-only scoring;
- forward-spectrum similarity;
- CFM-ID;
- SIRIUS/fragmentation-tree-derived evidence where a reproducible interface is available;
- FIORA or another peer-reviewed fragment-event model where suitable;
- the frozen initial pLSE and its internal ablations.

DeepMet should be treated primarily as a **paradigm-level reference and candidate-generation frontier**, not forced into Figure 2 unless its candidate outputs can be reproduced under the same frozen candidate-pool protocol.

Emerging methods that overlap strongly with fragmentation-aware ranking should be monitored, but an unreviewed preprint should not be used to support a central manuscript claim.

## Preprint policy

Preprints may be added to a final related-work paragraph only when they materially define the contemporary frontier. They should be described as emerging approaches and should not establish benchmark validity, the central evidence-bottleneck premise or biological conclusions.

## Nature-main-track extension

The strongest conceptual extension is prospective evidence-guided acquisition:

> residual candidate ambiguity → select the measurement expected to maximally separate survivors → acquire MSn/CE evidence → quantify candidate-space contraction.

Only after this loop is demonstrated should the manuscript claim literal co-evolution of hypotheses and experimental evidence or sequential hypothesis–experiment co-design.
