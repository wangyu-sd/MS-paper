# Peer-reviewed literature positioning

This document defines the competitive landscape used to write the manuscript. The central scientific argument should be supported primarily by peer-reviewed work; preprints can be acknowledged later as frontier context but should not carry essential claims.

| Work | Venue | What it established | What ORBIT-MS must not re-claim | ORBIT-MS distinction |
|---|---|---|---|---|
| CSI:FingerID (Dührkop et al., 2015) | PNAS | spectrum/fragmentation-tree to molecular fingerprint for database search | fingerprint-based retrieval | candidate-specific auditable evidence against hard alternatives |
| SIRIUS 4 (Dührkop et al., 2019) | Nature Methods | fast formula/structure inference integrating fragmentation trees and CSI:FingerID | generic “turn MS/MS into structure information” | evidence frontier that changes as candidate frontier becomes harder |
| CANOPUS (Dührkop et al., 2021) | Nature Biotechnology | compound-class annotation of unknown spectra; biological application including mouse digestive system | class-level interpretation of unknown metabolomes | structure-level candidate discrimination with calibrated fallback to lower resolution |
| COSMIC (Hoffmann et al., 2022) | Nature Biotechnology | confidence-aware structure annotation beyond spectral libraries | confidence scoring alone | confidence tied to candidate-specific mechanistic evidence and explicit non-resolution |
| MSNovelist (Stravs et al., 2022) | Nature Methods | de novo molecular reconstruction from predicted fingerprints | fingerprint-to-SMILES generation | evidence is a scientific object, not only a decoder condition |
| BUDDY (Xing et al., 2023) | Nature Methods | bottom-up MS/MS-explainable formula space and FDR-aware formula discovery | MS/MS-constrained formula discovery | discrimination within same-formula structural candidate sets |
| MIST (Goldman et al., 2023) | Nature Machine Intelligence | domain-inspired spectrum transformer with formula/neutral-loss inductive bias | domain-aware spectrum encoding | reciprocal hypothesis/evidence learning and evidence authority |
| MassFormer (Young et al., 2024) | Nature Machine Intelligence | strong forward spectrum prediction with graph transformers and collision-energy modeling | forward spectral simulation | simulation is separated from discriminative evidence |
| MassSpecGym (Bushuiev et al., 2024) | NeurIPS Datasets & Benchmarks | standardized leakage-resistant de novo/retrieval/simulation benchmark | benchmark creation itself | uses the benchmark to expose candidate/evidence co-difficulty |
| DiffMS (Bohde et al., 2025) | ICML | formula-constrained graph diffusion and scalable structure-only decoder pretraining | formula-constrained de novo generation | tests whether evidence adapts to stronger generated alternatives |
| Coverage bias (Kretschmer et al., 2025) | Nature Communications | structural coverage can dominate apparent small-molecule ML performance | generic split criticism | explicit pretraining/candidate leakage audit and cross-frontier evaluation |
| FIORA (Nowatzky et al., 2025) | Nature Communications | bond-local fragmentation-event modeling improves forward MS/MS prediction | explainable fragment prediction alone | atom-traceable trajectories are evaluated for GT–decoy discrimination, not only spectrum similarity |
| DreaMS (Bushuiev et al., 2026) | Nature Biotechnology | repository-scale self-supervised spectrum representation and 201M-spectrum atlas | foundation-model scale or spectral embedding novelty | uses unlabelled spectra as external deployment while focusing on evidence and falsification |
| MetGenX (Wang et al., 2026) | Nature Communications | structure-informed de novo generation; mouse-liver application and unknown-metabolite discovery | “we generated unknown mouse metabolites” as sufficient novelty | mouse cohort must show auditable alternative rejection, calibration and orthogonal validation |
| Reverse metabolomics (Gentry et al., 2024) | Nature | chemically grounded discovery by linking synthesized structures to repository-scale metabolomics and phenotypes | broad discovery claim without validation | motivates a high evidentiary bar for biological/novel-structure claims |

## Editorial positioning

The Nature-level proposition is **not**:
- a larger mass-spectrometry language model;
- an agent workflow;
- a fragmentation simulator;
- another de novo generator;
- another benchmark leaderboard gain;
- an unvalidated set of unknown mouse structures.

The proposition is:

> As molecular hypotheses become more faithful, the spectral evidence required to falsify their closest alternatives changes. Structure elucidation therefore benefits from reciprocal improvement of the hypothesis frontier and the candidate-specific evidence frontier.

## Three distinctions to defend throughout the paper

### 1. Simulation ≠ explanation
A forward model can reproduce a spectrum without identifying a chemically unique causal trajectory.

### 2. Explanation ≠ discrimination
A plausible fragment can be shared by the GT and every hard decoy. The manuscript therefore evaluates evidence on matched competing structures.

### 3. Prediction ≠ identification
A unique generated SMILES for a dark mouse spectrum remains a hypothesis until the evidence level supports a unique structure and, where identification is claimed, orthogonal validation is obtained.

## Preprint policy

Preprints may be added to the Related Work paragraph only when they materially define the contemporary frontier. They should be described as emerging approaches and should not be used to establish the central premise, benchmark validity or biological claim.
