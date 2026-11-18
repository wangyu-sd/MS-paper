# ORBIT-MS editorial revision — 18 November 2026

## Purpose and scope

The requested revision makes the abstract and Introduction suitable for the intended scientific readership, aligns the paper to the title below, and writes the existing five-result design as complete manuscript prose. Recorded measurements are retained. Pending experiments have positive-direction result sentences with `x` values, as requested. The author authorized merging the completed revision into `main` through PR #22.

**ORBIT-MS: Recursive chemical learning for molecular structure elucidation from tandem mass spectra**

The abstract is a single unreferenced paragraph. It explains the chemical problem, recursive learning mechanism, matched learning comparison, recorded motif ablation, dark-spectral outcomes and scientific implication. The Introduction develops the distinction between generating the correct graph and discriminating it from alternatives, then explains how those failures guide chemical-capability updates and later agent decisions.

Results retain the five themes in the [active NMI experiment plan](NMI_CHEMICAL_ELUCIDATION_RESULTS_PLAN_20261112.md). Discussion has been edited for continuity and concision. The five figure definitions, captions and panel specifications are retained. Methods receive a layout correction to the intervention equation and the aggregation description for the newly included benchmark snapshot. Supplementary Information changes only its manuscript title; its result tables are retained.

The preceding manuscript remains available at [the pre-revision PR #22 commit](https://github.com/wangyu-sd/MS-paper/blob/b8357a9a12477bb1b5b9853424f7753735ae8598/main.tex). The earlier title and abstract are also retained in `ORIGINAL_TITLE_ABSTRACT_20261118.md`.

## Result notation

`\pending{metric-id}` renders the italic letter `x` in the manuscript. Its argument is an editing locator. The short note immediately after the abstract explains that x-bearing statements describe planned outcomes. The note is outside the abstract.

| Shared locator | Meaning | Occurrences |
| --- | --- | --- |
| `rsi-generations` | Completed autonomous generations in the matched comparison | Abstract and Result 3 |
| `rsi-gain-over-fixed` | Paired difference in newly recovered molecule groups retained at the final generation, agent minus strongest fixed intervention | Abstract and Result 3 |
| `dark-supported-upgrades` | Dark-spectral resolution upgrades upheld by calibration and independent supporting evidence | Abstract and Result 3 |
| `family-relationship-count` | Graph-supported molecular-family relationships in the structural network | Abstract and Result 4 |
| `independent-corroborated-anchors` | Prespecified structure hypotheses corroborated by separately deposited experimental spectra | Abstract and Result 5 |
| `family-count` | Supported molecular families in the same source-defined landscape/network | Results 1 and 4 |
| `family-median-distance` | Median graph-edit distance to characterized chemistry for those families | Results 1 and 4 |

| Locator group | Experiment and values to fill |
| --- | --- |
| `r1-01`–`r1-19` | Distinct spectral entities; five resolution-tier counts and percentages; tier-specific calibration; independently recurrent and bounded families; representative examples |
| `r2-01`–`r2-03` | Fixed-pool improvement in same-formula/same-scaffold strata and source-linked structural examples |
| `r2-04`–`r2-17` | Frozen atom/ring/motif generation without supplied partial cores: Exact@1/10, reach, their intervals, formula recall, runtime and calibrated coverage/containment |
| `r3-01`–`r3-50` | Cumulative first recoveries; final retained gains and losses; reach and ranking; class-specific changes; supported dark-spectral upgrades; matched agent/fixed/scripted/frozen/no-memory comparisons; cost, transfer, learning streams and experience selection |
| `r4-01`–`r4-24` | Network entities/neighbours; graph-distance distributions and matched controls; recurring graph differences; recognition status and representative chemical families |
| `r5-01`–`r5-30` | Prespecified anchors; multienergy/MSn support; candidate-set reduction; unique/bounded/contradicted/unassessable outcomes; standard/retention follow-up; evidence categories and complete family histories |

Cumulative first recovery and final retained recovery are distinct endpoints in Result 3. Net recovery also subtracts losses among molecules correctly recovered at baseline. The abstract's agent-versus-fixed comparison uses the explicitly named final retained-new-recovery endpoint.

## Additional recorded data incorporated

The 18 November PR95 update supplied measurements beyond the previous manuscript. The new full-population paragraph uses one coherent machine-readable snapshot rather than mixing values from different development versions.

- Source repository commit: `b59a84a10fab300be352fbfe2069c9d057ac8061`.
- [Multi-regime benchmark summary](https://github.com/wangyu-sd/orbit-ms/blob/b59a84a10fab300be352fbfe2069c9d057ac8061/docs/results/pr93_multi_regime_benchmark_summary.json), generated at `2026-11-18T08:13:01.229908+00:00`; blob `2e7656293d98d0d3d367e22bb02b59a92cdb81ee`.
- [Aggregation implementation](https://github.com/wangyu-sd/orbit-ms/blob/b59a84a10fab300be352fbfe2069c9d057ac8061/scripts/build_pr93_multi_regime_splits.py); blob `1a483b40cb4f130033026bb28bdae5e73f055feb`.

| Partial-core evaluation, all 17,556 spectra / 2,998 molecules | Exact@1 | Exact@10 | Reach |
| --- | ---: | ---: | ---: |
| Single spectrum | 1.75% | Not provided in the overall source summary | Not provided in the overall source summary |
| Neutral-mass consensus | 4.84% | Not provided in the overall source summary | 19.88% |
| Pooling by known benchmark molecule identity | 7.00% | 10.91% | 23.65% |

The producer consolidates generation-specific candidate records. It groups the neutral-mass analysis by measured neutral mass rounded to four decimals, and the molecule-group analysis by the benchmark group field. The manuscript therefore labels this as a full-population development snapshot and reports the identity-assisted aggregation separately. These values do not replace the distinct pending frozen atom/ring/motif evaluation without supplied partial cores.

The [contemporaneous benchmark report](https://github.com/wangyu-sd/orbit-ms/blob/b59a84a10fab300be352fbfe2069c9d057ac8061/docs/results/pr93_multi_regime_benchmark_and_rsi_results.md) supplies the external partial-core metrics:

| Benchmark | Spectra | Exact@1 | Exact@10 | Reach | Formula-hypothesis recall |
| --- | ---: | ---: | ---: | ---: | ---: |
| NPLIB1/CANOPUS | 813 | 16.73% | 31.98% | 41.82% | 85.12% |
| CASMI 2022 | 237 | 4.64% | 11.39% | 16.46% | 90.30% |

The previously reported Exact@1 values remain unchanged; the other three metrics have been added. The original MMA ablation, Canonical Hybrid calibration, trajectory feasibility, fixed-pool reranking, near-isomer comparison, Macro-Core completion, public-source census and knowledge-resource progression are retained with their original values and settings.

## Editorial and technical verification

- Abstract: 145 words after rendering the pending markers as x; one paragraph; no references or editorial result instructions.
- Main text: approximately 3,250 words, excluding abstract, Methods, references and figure legends/specifications.
- Title: identical in the manuscript and Supplementary Information.
- Structure: Introduction without a heading; one Results heading with five topical subsections; Discussion; Methods.
- Preservation: all original Results numerical values retained, and all five figure definitions/captions unchanged.
- Pending results: no `\result{...}`, `\methodtodo{...}` or `\datatodo{...}` instruction blocks remain in Abstract, Introduction or Results. Detailed preparation notes in Methods and backmatter remain available.
- Shared abstract/result endpoints use the same pending locators.
- Full-document compilation and visual inspection are recorded in `NMI_FORMATTING_AND_PRESERVATION.md` after the final build.

NMI Article length and structure were checked against the [journal's current content-type guidance](https://www.nature.com/natmachintell/content): unreferenced abstract up to 150 words and main text up to 3,500 words, excluding Methods, references and figure legends. The exact title requested by the author is retained.
