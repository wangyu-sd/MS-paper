# ORBIT-MS NMI Methods update — source-to-manuscript audit (2026-10-08)

## Scope

This change revises only `main.tex`'s Methods and its Figure 1 **textual** methods placeholder, plus the CoCoGraph reference. It does **not** assert that ORBIT-MS has completed PR91 V2 training, performed self-distillation, demonstrated NMI-level performance, or discovered experimentally confirmed new metabolites.

This PR is deliberately independent of PR #2 (`paper/figure-revision-discovery-first-20261008`), which addresses an earlier discovery-first Nature figure plan.

## Implemented source components

| Manuscript content | Source of implementation | Correct boundary |
| --- | --- | --- |
| W: spectrum-blind connected fragment prior | `src/orbit_ms/wgv/fragment_candidate_world.py`; `scripts/train_pr86_candidate_world.py`; `scripts/prepare_pr86_structural_targets.py` | Up to three precursor-bond cuts, heavy-atom masks, hydrogen offsets and carrier masses; **not** a complete bond–electron mechanistic simulator. |
| V: observed-spectrum-conditioned fragment posterior | `src/orbit_ms/wgv/v_set_posterior.py`; `scripts/run_pr87_v_learned_set.py` | Learns posterior reweighting on **frozen W fragments**; no observed fragment-structure truth; spectrum evidence is not calibrated molecule correctness. |
| W/V structured transfer | `src/orbit_ms/wgv/wv_structured_evidence.py`; `scripts/score_pr87_frozen_wv_graph_edit.py` | Verified heavy-atom mapping; atom 3, pair 6 and global 2 channels; fragmentation boundary is observability, **not** an automatically signed bond removal. |
| G: spectrum-conditioned CoCoGraph V2 | `src/orbit_ms/wgv/cocograph_spectrum_v2.py`; `scripts/train_pr91_cocograph_spectrum_v2.py` | Clean-adjacency remove/add/bond-order heads and separate graph-only noise time; old V1 inverse-step imitation is only an auxiliary term. |
| V2 sampling and evidence feedback | `scripts/eval_pr91_cocograph_spectrum_v2.py`; `scripts/pr91_wv_online_rollout.py`; `scripts/pr91_wv_online_selection.py` | Predicted formula Top8, 4 draws/formula, bounded DES, online 2-child resampling only at defined late steps, separate terminal W/V scoring. |
| Historical/other W and V families | PR82 electron-event pipeline, PR90 BreakpointWorld/ChemicalEvidenceVerifier | Kept in code history but **not** silently described as the frozen PR86/87 teacher pair used in V2. |

Pinned evaluated teacher components in PR91:
- PR86 three-cut W SHA256: `df10668b0cc78ba9a0f5cc12171abea43d33f48cdde4a8c6b15b32ae1de26d14`.
- PR87 VSetPosterior SHA256: `06300f8200dcf201ba8d0eb812c5c89e7035e67c0d3e2e3b17e0846bbd703bb1`.

### Honest component evidence

- PR86 W, when scored conditionally on *reference precursor graphs*: 0.753212 macro intensity-weighted fragment-mass recall with at most 512 emitted peaks, tolerance 5 mDa, across 8,401 SEARCH_DEV spectra. This is **not** 75% correct candidate structures.
- PR87 fragment V on the same reference-structure W set: 0.627884 all-peak matched Top100 weighted recall, +0.077047 relative to shuffled spectrum, 243/290 strict same-formula/context decoy wins; the frozen W prior won 245/290. Avoid claiming robust improvement over the prior from this narrow comparison.
- Historical PR91 local W/V one-step gradient-style gate stopped at 53.15% correct-inverse-vs-sibling wins across 2,005 TRAIN-internal groups; sharp deterioration at deep corruption. V2 uses a different *supervised* denoiser, not a monotone V-energy optimization.
- No completed full PR91 V2 G checkpoint or complete V2 SEARCH_DEV metrics were evidenced at this draft freeze. Read live PR91 receipts before promoting this branch.

## Proposed, unimplemented self-distillation

The method now specifies the intended outer loop as an integrated research component:
1. Freeze W/V and formula predictor; fit and checkpoint supervised G0.
2. Generate target-free candidate structures on previously unlabelled **real** experimental MS/MS, no ICEBERG/CFM-ID pseudo-spectrum teacher.
3. Score those candidates with frozen W/V and convert *relative* evidence to soft, calibrated or abstained pseudo-targets. **The calibrator and confidence thresholds have not yet been implemented or frozen.**
4. Construct constrained DES corruptions of retained pseudo structures. Train G with weighted clean-graph denoising plus original paired supervision; do not blindly update W/V on G's own pseudo structures.
5. Promote Gt+1 only after independent, pre-registered structural evaluation shows reproducible improvement, particularly raw candidate reach rather than terminal reranking alone.

**Important split caveat:** all 20,430 TRAIN molecule groups were already used to train W/V. The 2,005-group internal G holdout is *not* a valid independent W/V calibration set. Pseudo-label structural correctness calibration requires genuinely independent confirmed chemistry or a freshly cross-fit teacher protocol. Do not use SEARCH_DEV labels adaptively and then present them as final held-out benchmark scores.

## Pending tasks before any manuscript-level accuracy claim

- Run actual PR91 V2 regression and real TRAIN W/V-to-G/backward smoke, inspect complete checkpoint and hashes.
- Complete immutable 8,401-case SEARCH_DEV evaluation of (A) no W/V, (B) terminal W/V only on the **same generated pool**, (C) online plus terminal W/V, including failed cases and group bootstrap.
- Implement, freeze and evaluate the full unlabelled-data self-distillation stage; report no-distillation, G-only teacher, shuffled-spectrum and W/V-guided pseudo-label controls.
- Audit exact-structure/family overlap of all evaluation chemistry with G/W/V molecular pretraining and self-distillation inputs.
- Replace `\methodtodo` with immutable experimental artifacts, or explicitly remove unexecuted claims before submission.
- **Manuscript consistency:** title, abstract, Introduction, Results, Discussion, Figure 2–5 textual placeholders, old nature-oriented discovery plan and Supplementary Information still describe the prior executable bond–electron World and dark-metabolome Nature story. They require a separate coordinated NMI rewrite after PR91 V2 results. This PR does not claim otherwise.
