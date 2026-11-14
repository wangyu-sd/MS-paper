# ORBIT-MS | Master Results Ledger / 研究结果总账

**截至：2026-11-14（Asia/Shanghai）** · **用途：科学结果归档、Figure/Results 规划、投稿前审计**  
**归档范围：** orbit-ms [PR93](https://github.com/wangyu-sd/orbit-ms/pull/93), [PR95](https://github.com/wangyu-sd/orbit-ms/pull/95), [PR96](https://github.com/wangyu-sd/orbit-ms/pull/96) 与 MS-paper `main.tex` / `supplementary/ORBIT_WGV_RSI_Results.tex`。PR95 已核对至 SHA **4a07dc08b545**（2026-11-14；最后一次提交为提高 MMA alignment 权重，**晚于本表主要实验数据**）；PR93 原始分支 SHA **e7f4d18968ba**；PR96 分支 SHA **c63c32ce24b2**。主要新结果报告提交 **17abc117025c**。未直接挂载集群 Ceph 上所有逐例 `rank_*.jsonl`、原始 checkpoint 和所有 GPU log，因此表中明确区分**源报告给出的数值**和**已复核的 JSON/代码**；此表不代表对所有集群作业重新复算。

**重要原则：保留全部研究路线，不把公共 HMDB / ChEBI / COCONUT / LipidMaps / SwissLipids 检索当作无效实验。** 公共化学候选识别、MMA/G 自主候选扩展、已知分子式补全、同源骨架辅助、W/V 证据判别、多谱图聚合及真实暗谱图解析，是不同且互补的科学问题。跨协议的 Exact@1 不能当作一条可直接相减的学习曲线。

## 0. 度量与证据等级（所有表统一）

- **Exact@1/10**：参考分子 **InChIKey 前14位的 2D connectivity** 是否位于首位/前十位；不是完整立体化学鉴定或标准品确认。
- **Reach**：参考 connectivity 是否进入指定实际候选池，不代表被正确排序；`Exact@1 ≤ Exact@10 ≤ Reach` 仅在相同候选池、同一分母与明确定义下必然成立。
- **Tanimoto@1、Tanimoto max**：基于同一参考指纹的结构相似度；不能替代正确连接结构。
- **macro / micro**：优先同时给谱图级和独立分子组级；一个分子多张谱图会影响谱图级比例。
- **BLIND-PRED-FORMULA**：实验可观测 precursor 和模型的分子式估计，未直接输入 GT 公式。
- **KNOWN/ORACLE-FORMULA**：参考分子式已经输入，属于更容易的条件结构推断。
- **DB-CANDIDATE**：候选结构直接来自公共化学库（可与 G 生成补充候选联合）；可以是合理的结构鉴定任务，但不是无数据库纯 de novo。
- **HOMOLOGY-CORE**：从非评价分子库中得到相近完整骨架、裁剪成不完整结构后由 G 补全；不是从空分子图开始。
- **AGG-GROUP**：按 GT 分子组 ID 跨谱图聚合，用于诊断；不可称为严格未知目标盲聚类。
- **AGG-BLIND**：以观测中性质量和预测分子式进行候选聚合；仍需误聚类和原始分片污染审计。
- **报表状态：** `R` = 已记录数字和来源；`J` = 可读机器 JSON；`C` = 已核对核心实现；`D` = 诊断/开发；`P` = 部分样本/中间结果；`X` = 取消；`U` = 待原始回执核验。一个数字可以同时属于多类（例如 R+J+D）。

## 1. 总体实验地图：哪些结果可以同表比较

| 任务簇 | 输入条件 | 主要候选来源 | 数据规模/协议 | 要解决的科学问题 | 报告代表性结果 | 状态 |
|---|---|---|---|---|---|---|
| A：公共数据库鉴定 | BLIND-PRED-FORMULA + MS/MS | MassSpecGym TRAIN / HMDB / ChEBI / LipidMaps / COCONUT / SwissLipids 候选 + 可选 G 新结构 | Official TEST **17,556 spectra / 2,998 molecules** | 既有公共结构能否用化学证据从竞争候选中识别？ | Bio-Prior+MMA+cleavage Exact@1 **31.57%**, Exact@10 **56.70%** | R+C；候选来源审计待补 |
| B：公共数据库鉴定，公式已知 | KNOWN/ORACLE-FORMULA | 同 A | 同 17,556 | 上限及分子式不确定性的影响 | Exact@1 **42.74%**, Exact@10 **63.08%** | R+C，**oracle** |
| C：MMA/G 真正从结构约束构建 | KNOWN/ORACLE-FORMULA | G 的 atom/ring/motif + MMA starts | CAL200 | 局部化学知识是否提高新完整结构的 Reach？ | Canonical Hybrid Exact@1 **12.50%**, Reach **22.50%** | R |
| D：同源骨架辅助 G 补全 | KNOWN/ORACLE-FORMULA + partial macro-core | 非评价同源库 → 严格 partial start → G 补 1–3 个重原子 | CAL200 | 接近的可用化学结构能提高多少可恢复性？ | Exact@1 **49.00%** raw / **52.50%** 后续报告，Reach **90%** | R；需固定版本 |
| E：G 与共识的目标条件生成 | BLIND-PRED-FORMULA + MS/MS | peak-ladder / multi-start / core completion + W/V | Official TEST **14,370 / 17,556**，2,577 molecules | 严格结构距离与多谱图聚合下的实际能力边界？ | 表中原分片 1.66%、AGG-BLIND 2.83%、AGG-GROUP 3.37% Exact@1 | R+J+P+U |
| F：天然产物外部测试 | 报告规定的公式与候选源 | Peak-Ladder/WGV + 生物合成先验 | NPLIB1 813 / CASMI22 237 | 跨数据源可迁移性？ | Exact@1 **16.73% / 4.64%** | R；分母完成 |
| G：化学证据判别 | 参考结构与同式异构体 | W / V / MMA fragments | SEARCH_DEV 300 / TRAIN 765或800 / CAL谱图 | 结构特异碎裂证据是否超越单纯覆盖？ | W 胜近异构体 **87.94%**；V_g10 硬负例胜率 **56.00%** | R+J |
| H：暗代谢物源数据 | 实测多队列、参考库无接受匹配 | 真实谱图、条件结构候选 | 三项研究 835,953 QC查询 | 可解释的暗谱图资源规模和跨研究复现？ | **613,331** 无接受参考匹配，**2,255** 跨研究社区 | MS-paper 数据/Methods |
| I：系统改进 RSI | TRAIN FIT诊断、非TEST结构库和经验 | MMA知识、G、V、固定W、脚本/Agent | Gen1–10 开发轨迹，V_g10 新结果 | 化学知识是否可复用、能否改变后续候选/判别能力？ | MMA libv1→v3 **4.23M→31.11M**；V harder win +5.22pt | R；真正 Agent 因果效应未建立 |

## 2. A/B — 公开化学知识库 + MMA / Physical Cleavage 的完整17,556条官方 TEST 消融

来源：[PR93/95 full-test prior + MMA report](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_test_generalization_and_mma_ablation_20261109.md) · [实现脚本](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/scripts/eval_pr93_prior_mma_wv.py) · MS-paper `tab:bio_prior_mma_cleavage`。库包含六类 parquet：MassSpecGym TRAIN、HMDB、ChEBI、LipidMaps、COCONUT、SwissLipids；按分子式组织候选，默认每式最多80个数据库候选、附加不在库中的 G 候选至多16个。**真实 GT 只用于事后评分和 oracle-formula 分支**，不可作为 blind 输入。分子结构在公开候选库中出现属于任务定义允许的知识，不应与独立于候选库的 de novo 相混淆。

| 固定公共候选源、不同证据权重 | Blind Exact@1 | Blind Exact@10 | Blind Tanimoto@1 | Oracle-formula Exact@1 | Oracle Exact@10 | Oracle Tanimoto@1 |
|---|---:|---:|---:|---:|---:|---:|
| A1 Uniform Pool（不使用 MS/MS/MMA 判别） | 17.36% | 47.02% | 0.3419 | 25.34% | 54.19% | 0.4284 |
| A2 Uniform + MMA substructure evidence | **20.11%** | 50.14% | 0.3708 | **29.39%** | 57.03% | 0.4656 |
| A3 Uniform + physical 1/2-cut cleavage | **23.73%** | 52.03% | 0.3972 | 32.56% | 58.74% | 0.4875 |
| A4 Uniform + MMA + cleavage | **24.47%** | **53.29%** | 0.4070 | 33.50% | 59.93% | 0.4982 |
| A5 Multi-DB Bio-Prior + MMA + cleavage | **31.57%** | **56.70%** | **0.4583** | **42.74%** | **63.08%** | **0.5625** |

**实验解释：** A1→A2 量化 MMA 相对无谱峰结构证据的增益；A1→A3 量化简化物理碎裂；A4→A5 同时改变 Bio-Prior 及其他打分权重，**不能将 +7.10pt 全部单独归因于数据库来源计数**；应固定 MMA/cleavage 系数补充正交先验消融。A1 已达17.36%说明**候选供给/公式及数据库本身**具有相当大的识别能力；绝不应把 31.57% 写成纯生成模型准确率。

**源代码已定义但本次提交结果表未披露的 3 个 arms**：`5_uniform_mma_cut_wv`、`6_bioprior_no_ms2`、`8_bioprior_mma_cut_wv`。这三条需要从真实运行的 `summary_shard_*.json` 汇总，不能按现有五行推算。还应区分“仅数据库正确候选”与“仅由 G 新提出正确候选”的各自贡献，并记录正确分子首次进入池的来源。

## 3. C — MMA + G + W/V 在已知分子式 CAL200 的生成消融

来源：MS-paper Supplementary `tab:mma_strict_ablation`、`tab:mma_wv_component_ablation`、`tab:wv_fixed_pool_reranking`；[PR95 description](https://github.com/wangyu-sd/orbit-ms/pull/95)。**这组不是公共 DB 完整候选池识别，也不是未知分子式。**

### 3.1 同 checkpoint 严格 MMA 特征消融

| Model/Inference | Teacher loss↓ | Teacher@1 | Select@1 | Exact@1 | Exact@10 | Reach | Tan@1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| MMA off | 0.996 | 69.1% | 54.6% | **1.50%** | 4.50% | 6.50% | 0.2009 |
| MMA on | 0.757 | 76.0% | 67.5% | **6.00%** | **14.50%** | **19.00%** | **0.3221** |

Start action@1：MMA off 76.4% → on 86.3%。这里同时改善的是 teacher 行为和结构生成，而不只是一种检索候选排序得分。

### 3.2 分阶段组合（原 Supplementary C1–C7）

| ID | MMA/G/WV 组合 | Exact@1 | Exact@10 | Reach | Tan@1 | Tan@10 |
|---|---|---:|---:|---:|---:|---:|
| C1 | MMA off + 空图 | 1.50% | 4.50% | 6.50% | 0.2009 | 0.2640 |
| C2 | MMA features + 空图 + G ranking | 7.00% | 11.50% | 16.00% | 0.3170 | 0.4136 |
| C3 | C2 候选池 + W/V terminal rerank | 8.50% | 13.50% | 16.00% | 0.3351 | 0.4136 |
| C4 | MMA seeded starts×8 + G ranking | 5.50% | 16.00% | 19.00% | 0.3103 | 0.4685 |
| C5 | C4 同池 + W/V rerank | 10.00% | 18.00% | 19.00% | 0.3752 | 0.4685 |
| C6 | 空图 Beam16 + MMA-starts 联合池 + W/V | 11.00% | 19.50% | 22.00% | **0.3872** | 0.4812 |
| C7 | Canonical Hybrid + heavy-atom normalized/motif-reserved beam + W/V | **12.50%** | **21.50%** | **22.50%** | 0.3811 | **0.4938** |

**因果分解：** C2→C3 和 C4→C5（同池）支持 W/V 的**判别**价值；C2→C4 提高 Reach 16→19%，同时 G-only Top1 7→5.5%，表明扩增候选并非单调改善排名；C6→C7 改动不只一项，属于算法组合，不可视作纯 MMA 净收益。

### 3.3 Canonical Hybrid 动作空间与 beam

| 方案 | 决策步数均值 | Canonical@1 | Valid@1 | Seen Exact@1 | Seen Reach | Fit Reach |
|---|---:|---:|---:|---:|---:|---:|
| P1 Random-order staged, Beam4 | 32.4 | — | 90.6% | 25.0% | 37.5% | 13.3% |
| P2 Canonical + Motif, Beam4 | 24.5 | 84.7% | 90.6% | **32.8%** | 42.2% | 14.3% |
| P3 Direct single stage, Beam16 | **9.1** | 74.6% | 82.9% | 17.2% | 31.3% | **31.3%** |
| P4 Canonical Hybrid + R_t, Beam16 | 24.6 | **86.0%** | **90.7%** | 28.1% | **53.1%** | 27.1% |

独立的 **GT-conditioned 98分子可行性探针**中，总步数 32.4→24.8，真实长图构建步数 20.1→12.9；87% 分子可使用 Motif 动作，每次平均接入4.5个重原子；98/98 在 teacher canonical 路径上可重建。此结果只支持动作表示**可行且缩短路径**，不是未知结构生成准确率。

### 3.4 HMDB-W + TRAIN联合训练历史

| Epoch | Train loss | Canonical@1 | Valid@1 | CAL100 Exact@1 | Reach |
|---:|---:|---:|---:|---:|---:|
| 0 | 1.997 | 54.4% | 64.7% | 4.21% | 7.37% |
| 2 | 1.690 | 58.4% | 67.8% | 7.37% | 9.47% |
| 6 | 1.588 | 60.3% | 69.6% | **8.42%** | **13.68%** |
| 9 | 1.575 | **60.6%** | **69.8%** | 7.37% | 11.58% |

**说明**：这些是空图起点、无 terminal W/V、无 MMA starts 的特定训练进程记录；不能取 max epoch 指标和另一条全系统结果拼成新配置。

## 4. D — 同源结构辅助的 Macro-Core completion

| 协议 | n | Exact@1 | Exact@10 | Reach | 解释 |
|---|---:|---:|---:|---:|---|
| CAL200 + known formula + 非VAL/TEST同源分子裁剪骨架 + G 补1–3重原子 | 200 | **49.00% raw**；历史 Gen10 汇总称52.50% | **73.00%** | **90.00%** | 高分代表**已知部分骨架 → 神经补全与候选判别**的强能力 |
| Official TEST200 + homolog-assisted 早期Gen6 | 200 | 未能从同一已冻结输出确认 | — | **6.50%** | 跨泛化距离落差巨大；开发迭代口径 |

**关键边界**：以 `len(s_0.symbols) < N_heavy` 约束保证 G 执行了至少一部分生成，并不意味着“没有外部骨架先验”。正确表述是 *homology-seeded partial-graph neural completion*。49% 与52.5%的具体后处理、模型 SHA、候选预算应分别归档后才可正式比较。

## 5. E — Official TEST 和外部 benchmark：完整任务条件并列

| Benchmark/评测快照 | 单位/规模 | Exact@1 | Exact@10 | Reach | 注释/不应作的比较 |
|---|---|---:|---:|---:|---|
| MassSpecGym 官方TEST全量，公共DB固定候选+Bio-Prior+MMA+Cleavage | **17,556 spectra / 2,998 molecules** | **31.57%** | **56.70%** | 未在五行表报告 | **DB-assisted**，非 G-only |
| MassSpecGym TEST latest G-branch 已汇总 | **14,370 spectra / 2,577 molecules** | 报告单谱排序 **1.66%** | — | — | 需核实生成 shard 是否预做 blind consensus |
| 同 14,370 条，观测中性质量+预测公式聚类 | 同上 | **2.83%** | 未单独列出 | **18.36%** | `AGG-BLIND`；需误合并/跨shard审计 |
| 同 14,370 条，已知分子组统一聚合 | 同上 | **3.37%** | **7.61%** | **22.78%** | `AGG-GROUP`，诊断用；以GT组聚合，不是未知目标完全盲测 |
| Official TEST 已早期完成首 1,072 条 | 1,072 spectra（非代表性先完成批次） | **17.63%** | **25.65%** | 29.41% | 中途快照，不能推广至全体 |
| NPLIB1 / CANOPUS Test | **813 / 813** | **16.73%**（raw 14.02%） | **31.98%** | **41.82%** | 报告另记 Formula@K=85.12%；需要核对候选源与排序版本 |
| CASMI 2022 | **237 / 237** | **4.64%**（raw 3.38%） | 11.39% | 16.46% | 报告另记 Formula@K=90.30% |
| Official TEST200 Gen7∪8 cross-generation memory | 200 | **5.50%**（二轮6.50%） | 6.00% | 9.50%（二轮10.5%） | 开发使用的TEST子集，不是最终 untouched TEST |

**所有 14,370 条结果均小于 17,556 完整分母：还差 3,186 条谱图。** 不能用 early 1,072 的 17.63% 或某个化学家族的高分代替整个TEST准确率。另一方面，也不能把 DB-assisted 31.57% 当作 G-only 1.66% 的失败或冲突：两者候选源不同。

## 6. F — 五维多情形（当前脚本实际 21 个分层类别）结构泛化

来源：[multi-regime report](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_multi_regime_benchmark_and_rsi_results.md)、[machine summary](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_multi_regime_benchmark_summary.json)、[implementation](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/scripts/build_pr93_multi_regime_splits.py)。

这里的“5-axis”指 MCES、Morgan相似度、Murcko层级、环词表覆盖、生源类别；代码有**4+4+3+4+6=21个分层类别**，报告标题写18与脚本不符。每一轴都由同一批14,370谱图划分，**不是五套独立新训练测试分割**；同一分子在不同轴会重复出现。表中“group-pool”采用参考分子组 ID，作能力诊断。

### F1. MCES / 与非TEST结构最小编辑距离

| MCES | spectra | unique mols | blind Exact@1 | group-pool Exact@1 | group-pool Exact@10 | blind Reach | group-pool Reach |
|---|---:|---:|---:|---:|---:|---:|---:|
| ≤5 | 4,211 | 329 | **6.93%** | **8.15%** | 14.96% | 33.70% | **43.96%** |
| 6–10 | 857 | 107 | 0.70% | 0.70% | 2.10% | 14.47% | 19.02% |
| 11–16 | 1,372 | 150 | 0.66% | 0.73% | **10.64%** | **43.00%** | **46.50%** |
| >16 | 7,930 | 1,991 | 1.26% | 1.58% | 3.78% | 6.37% | 7.84% |

**值得研究但不是已建立原因：** 11–16 的高Reach/低Exact现象可能受家族/同一分子重复谱图、候选池、排序策略交互影响，需要分子组 macro 和固定候选池诊断。

### F2. Morgan Tanimoto 与既有结构最大相似度

| Smax | spectra | unique mols | blind Exact@1 | group-pool Exact@1 | group-pool Reach |
|---|---:|---:|---:|---:|---:|
| ≥0.80 | 2,655 | 205 | 5.54% | 6.97% | **44.29%** |
| 0.60–0.80 | 2,999 | 219 | 2.50% | 2.80% | 41.51% |
| 0.40–0.60 | 1,445 | 206 | **7.47%** | **9.13%** | 22.91% |
| <0.40 | 7,271 | 1,947 | 1.06% | 1.14% | 7.18% |

Smax 与性能**并非单调**。不能忽视化学家族与公式大小的混杂因素。

### F3. Murcko 原子骨架与通用拓扑

| Level | spectra | unique mols | blind Exact@1 | group-pool Exact@1 | group-pool Reach |
|---|---:|---:|---:|---:|---:|
| TRAIN 已见原子 Murcko scaffold | 1,059 | 166 | 1.98% | 2.36% | 12.65% |
| 已见 generic carbon ring skeleton，具体 chemistry 未见 | 2,099 | 491 | 3.72% | **5.24%** | 18.72% |
| 未见 generic topological ring skeleton | 11,212 | 1,920 | 2.75% | 3.11% | **24.50%** |

第三类 Reach 反而高于“已见原子骨架”类别，**说明跨分层难度与谱图数/家族构成不平衡，不能直接作单一能力排序**。

### F4. RingVocab 覆盖

| Rings | spectra | unique mols | blind Exact@1 | group-pool Exact@1 | group-pool Reach |
|---|---:|---:|---:|---:|---:|
| 100% ring词表可见 | 10,625 | 1,939 | 2.94% | 3.47% | 23.04% |
| 部分 OOV | 2,640 | 407 | 3.30% | 3.98% | **27.20%** |
| 全部 ring OOV | 951 | 202 | 0.84% | 1.05% | 10.41% |
| 无环 | 154 | 29 | 0.00% | 0.00% | 5.84% |

### F5. 天然产物/生物合成家族

| Family | spectra | unique mols | blind Exact@1 | group-pool Exact@1 | group-pool Exact@10 | group-pool Reach |
|---|---:|---:|---:|---:|---:|---:|
| 大环内酯、大环分子 | 1,022 | 123 | **15.85%** | **18.79%** | **28.38%** | 45.69% |
| 糖苷、皂苷 | 1,696 | 126 | 0.12% | 0.24% | 8.43% | **49.47%** |
| 黄酮、苯丙素 | 1,088 | 159 | 0.18% | 0.18% | 11.58% | 28.12% |
| 肽、缩肽 | 4,482 | 853 | 3.01% | 3.90% | 5.15% | 13.74% |
| 生物碱、含氮杂环 | 5,599 | 1,228 | 1.89% | 1.95% | 5.29% | 18.38% |
| 萜类、脂质、聚酮 | 483 | 88 | 0.00% | 0.41% | 1.66% | 3.52% |

**最高价值的诊断之一：糖苷在 group-pool Reach 49.47%，但 Exact@1 仅 0.24%。** 值得优先核查同式异构体是否被混淆、候选数/谱图重复数、排名与 reference 标准化，不能自动断言是 V 单独的问题。

## 7. G — 碎裂 World 和 Verifier：为什么“更多解释”可能更差

### 7.1 W 自身区分能力（SEARCH_DEV，300分子，每个参考与同式随机/近似分子比较）

| W分数信号 | GT胜随机 | GT胜相近异构体 | GT在10候选中排第1 | score与GT相似度 Spearman |
|---|---:|---:|---:|---:|
| W deployed `world_score` | **94.44%** | **87.94%** | **68.00%** | 0.3522 |
| W coverage only | 87.08% | 79.44% | 41.33% | 0.2523 |
| W predicted-spectrum cosine | 92.44% | 85.61% | 64.67% | 0.3097 |
| Hand cost-score | 87.69% | 80.50% | 48.33% | 0.3135 |

同一 source JSON 对 W 正确分子的模拟谱 cosine 中位数 **0.4182**，coverage中位数 **0.8924**；对 Na 子集 Rank1仅 **48.57%**（35例）。因此 W 是有判别信息的评分器，但还不是高精度物理碎裂轨迹模拟器，也不是足够平滑的G局部编辑指引。

### 7.2 765 TRAIN分子：碎裂模式从保守到宽松（固定比较对象）

| 可用解释模式 | GT平均解释强度 | 相同分子式错误结构平均解释强度 | GT成对胜率 |
|---|---:|---:|---:|
| 当前 ≤3-cut，±6H | 84.46% | 65.25% | **65.23%** |
| 加同位素 | 87.45% | 69.19% | 64.91% |
| 加单个中性丢失 | 93.32% | 89.03% | 42.25% |
| 加两个中性丢失 | 94.81% | 93.28% | 28.71% |
| 任意子分子式覆盖 | **96.29%** | **96.20%** | **15.50%** |

**机制结论**：提升未加权峰覆盖，不代表提升结构可辨识性；过宽解释库让错误异构体也几乎全能解释。另在同一 TRAIN诊断中，加入固定碎裂路径代价后，成对GT胜率约 **85.36%**（探索性手工成本，不是新 W 训练提升）。[主文件](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_fragmentation_gap_20261014/discrimination_summary.json) / [cost-weighted](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_fragmentation_gap_20261014/cost_weighted_summary.json)。

### 7.3 W 与 MMA碎片证据是否互补（TRAIN 800 groups）

| 信号 | 与近同分异构体胜率 | 与随机同式异构体胜率 |
|---|---:|---:|
| W fragments | **81.20%** | 87.36% |
| MMA motifs | 79.64% | 83.68% |
| W+MMA 直接并集 | 80.17% | 87.05% |

W 未解释的真实强度约 **21.61%**；MMA 还能覆盖其中约 **15.00%**，但直接并集没有提升近异构体判别。说明需要校准兼容性和证据区分力，而不是越多越好。来源：`docs/results/pr93_g_peak_msa_20261015/v_mma_complement_audit.json` 与 MS-paper Supplementary。

### 7.4 W 模型续训（与不同 baseline 比较需固定）

| 版本/协议 | SEARCH_DEV300 GT胜近异构体 | 10候选 GT@1 | 备注 |
|---|---:|---:|---|
| Original W | **87.94%** | 68.00% | 与 W训练不相交 |
| Contrastive R2 W候选的 `world_score` | **91.11%** | **73.67%** | 其 JSON 另提供 paired bootstrap 与 plain-W 对照 |
| H-shift-conditioned R5a `world_score` | 91.00% | **73.67%** | Na子集仍困难；`decision_vs_baseline.promote=true`，需要结果版本与条件同步记录 |

这里是 W 结构鉴别能力改善，不是端到端 MS/MS 分子 Exact@1。相关原始记录：`pr93_w_round2_20261014/gate_contrast_r2_best.json`、`pr93_w_round5_20261015/gate_honly_r5a_best.json`。

### 7.5 Na 加合物单独诊断

TRAIN 600 Na + 600 H样本（1–3 cuts、±2H）；Na谱中 **37.27%** 的碎片强度只能由带 Na 的碎片解释，而同口径 H谱假 Na-only 仅 **5.52%**。Na 碎裂下物理离子携带、氢迁移与低信息量会显著改变模型能力；需单独分层报告，不得只给总准确率。

### 7.6 V_g10 自进化：已报告实测判别结果

| V训练阶段 | ordinary same-formula peer win | hardest mined-negative win | evidence margin `matched_minus_peer` |
|---|---:|---:|---:|
| V_r5a_mined 初始 | **77.41%** | **50.78%** | 3.4020 |
| Epoch0 | 76.60% | 51.09% | 3.4502 |
| Epoch1 | 77.09% | 53.14% | 3.4608 |
| Epoch2 | 77.33% | 52.83% | 3.4429 |
| V_g10 Epoch3 | **77.50%** | **56.00%（+5.22pt）** | **3.4815** |

报告采用 **158,704 TRAIN spectra + 6,436 同分子式hard negatives + MMA libv3 31.11M**，在 **16,844 calibration spectra（其中1,609 hardest）**记录验证结果。需核查难负例来源与 held-out molecules 是否重合、和 PR96 Agent/fixed 对照；+5.22pt 仅是这个判别评测的收益，不能写成整体 Exact@1 +5.22pt。来源：`pr93_multi_regime_benchmark_and_rsi_results.md`。

## 8. H — 历史 G/碎片构建的失败结果（应保留以解释方法动机）

### 8.1 早期 SEARCH_DEV 8,401条谱图的真实结构恢复

| 方法 | Exact@1 计数 /8401 | Exact@10计数 /8401 | Reach计数 /8401 | 说明 |
|---|---:|---:|---:|---|
| PR87 G_BASE，同式检索 + 1–2步改键 | 288 | 948 | 1,176 | 绝大部分命中是很近的 TRAIN 近邻 |
| PR87 H广度穷举 | 396 | 1,446 | 1,841 | 每谱图候选数明显更大，不能当同预算标准SOTA |
| PR90 G90 编辑器 | 157 | 787 | 1,317 | 有大量0–2步种子直接转化 |
| PR87 图扩散v2（从零） | 0 | 1 | 1 | 真正从零生成几乎失败 |
| V4 随机图 + DES，部分官方TEST | **0/2368 Exact@1** | 0/2368 | 0/2368 | 早期系统历史失败，不是当前WGV最优结果 |

G_BASE中 **286/288** Top1来自TRAIN中同式 MCES≤4.5近亲；官方TEST中该近亲条件极少。早期 V4 随机起点与GT差约88个键单位，32步后仍差约63。来源：[PR93 G-history case analysis](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/PR93_G_HISTORY_CASE_ANALYSIS_20261014.md)。

### 8.2 结构修复上限、fragment anchor与峰相关能力

| 诊断 | 结果 | 说明 |
|---|---|---|
| G从GT本身(k0)开始，SEARCH_DEV128 | GT被访问约98.44%，最终Exact@1仅约17.19%（该 source 的 source-score协议） | 停止/排序不足 |
| G从GT扰动2步开始 | GT访问约50.00%，Exact@1约4.69% | 长距离局部重建能力快速下降 |
| G从GT扰动4步开始 | GT访问约15.63%，Exact@1约3.13% | 只做局部repair无法应对新骨架 |
| 独立MMA top1碎片，SEARCH_DEV128 | GT覆盖35.03%，严格Hit@0.8 46.09% | 有正确信息，但覆盖不完整 |
| 6-anchor合并 | GT覆盖40.86%，严格Hit@0.8降至22.66% | 多个碎片互相拼接会引入错误原子/边 |
| 谱图→结构子任务 probe，SEARCH_DEV8401 | Morgan平均AUROC 0.874、MACCS 0.935、59个RDKit FR片段0.924 | 表示层存在谱图信号；不直接证明完整分子能生成 |
| 官方TEST部分400分子Oracle MMA覆盖 | 最大真碎片的GT重原子覆盖中位数约29%，真碎片并集约61% | G仍需补全大量未由MMA确定的骨架 |

上述 oracle/GT-conditioned 结果是**上限或机制诊断**，不是可部署的匿名代谢物解析准确率。历史 `PR93_V5` DeepMech联合 W因初始离子化错误 **CANCELLED**；虽保留了 W联合候选拟合/export产物，V_joint full fit、G5、V5官方TEST均未运行，不应计算为成功实验。

## 9. I — 分子知识、自生成数据和 RSI 代际

### 9.1 真实建立的资源（各版本不能混在一个epoch假装同源）

| 资源 | 报告规模 | 作用/状态 |
|---|---:|---|
| MassSpecGym 训练符号 MMA v1 | **4,230,707 entries, 20,430 groups** | 已建立 |
| HMDB-W加入后 v2 | **12,983,158 entries, 115,383 groups** | 已建立；220,642 ion-formula keys |
| 多源 COCONUT/ChEBI/LipidMaps 等 W / GeMS Wake 加入后 v3 | **31,106,023 entries, 187,232 groups** | 2026-11-11 RSI报告称已建立；待完整source SHA |
| HMDB-W模拟MS/MS | **129,146 spectra、32,229 groups** | MS-paper supp 记录已生成/使用 |
| 多源模拟谱 | **93,374** | Gen8历史报告，需保留生成receipt |
| GeMS去重的未标谱资源 | **41,578,985 spectra** | 资源统计，不等于都已跑完Wake训练 |
| GeMS–Hindsight | **2,580 pairs** | Gen8历史报告，需检查训练实际consumption |
| 非VAL/TEST结构先验池 | **597,383 molecules**（早期报告）或analog池 **637,194**（后续） | 不同构建时间和过滤口径，不能视为互相矛盾或单一版本 |

### 9.2 Gen 1–10 方法/数据变化的历史开发账本

| Gen | 作者记录的核心化学/工程变化 | 报告结果或已证实作用 | 科学身份 |
|---|---|---|---|
| 1 | MMA v1 + RingVocab / atom-ring-motif动作 | TEST200 Exact@10 1% | 人工/脚本开发阶段 |
| 2 | Closed Motif Ladder、motif-first canonical ordering | 构建步数下降 | 训练算法结构修复 |
| 3 | Atom-normalized beam + motif/ring保留 | CAL200 Exact@1 12.5%, Reach22.5% | 已知分子式条件 |
| 4 | HMDB-W自合成 + MMA v2 12.98M | TEST200历史 Exact@1 2.0% | 某代开发快照 |
| 5 | 双起点、W/V局部修复 | TEST200 Exact@10 2.5% | 历史算法组合 |
| 6 | 非TEST同源Macro-Core → G短补全 | CAL200 raw 49.0% / Reach90% | **Homology-assisted** |
| 7 | 异构体共识、化学拓扑先验、二轮 tautomer/取代基重建 | TEST200历史 5% 等；若干实际示例 | 未构成独立自主Agent episode |
| 8 | 多源 sleep + GeMS Wake、MMA v3、formula rescue | CAL100 bare policy Exact@1 7.37%, Reach16.84% | 历史训练数据扩展 |
| 9 | iminol→amide修复、ring CH2 contraction、1-step partial priority | 多数据分片启动，局部结构覆盖改善 | 更新中的开发历史 |
| 10 | 不稳定 polyazo筛选、PKS/NRPS优先、跨能量共识 | 全TEST部分进展；具体历史数字见下一条审计 | 历史多阶段系统 |
| 11–13代码 | compound repair（destroy/regrow）、跨能量真正W/V比对、SMARTS规则 | **代码已有，不代表已有同口径新指标** | 待完整运行回执 |

最新主分支的 Agent/RSI 控制还包括按失败簇与 `seen` 保持率分配真实/模拟训练比例，及真实LLM Principal的一次已保存决定：`EXPAND_NP_AND_WAKE`、预算26,000/epoch、HMDB 0.04 / 多源天然产物 0.12 / GeMS Wake+Hindsight 0.84。该 receipt 证明决策记录存在，不证明它带来了相应完整TEST收益。

PR96 是独立 **draft**、更严格的 Scientific Improver implementation；截至本账本尚缺完整Agent-vs-fixed对应GPU训练episode与匹配性能结果。不要将PR95历史 Gen1–10称为 PR96 已完成的 autonomous RSI runs。

### 9.3 真实的单分子技术示例（全部是已知 benchmark 回溯，不是新代谢物发现）

| Case | 结构/分子 | 记录的排名或化学编辑 |
|---|---|---|
| 0000201 | Beauvericin | 曾从rank2提升rank1 |
| 0039311 | Roxithromycin | rank4→1 |
| 0012997 | Clarithromycin | rank5→1 |
| 0012696 | Erythromycin | rank9→1 |
| 0064680 | EGCG | 排除quinoid化学伪结构，历史rank6→1 |
| 0002114 | Cyclic tetrapeptide | n-propyl→isopropyl局部连接调整，曾恢复exact GT |
| 0058046 | Tetracycline | tautomer枚举与W/V比较，曾恢复GT |
| 0076066 | Letrozole | rank3→1 |

这些来自 MS-paper Supplementary `tab:gen7_landmark_cases` / `tab:second_round_refinement`。**若没有对应case的谱图/SMILES与前后排序回执，不可以直接用于量化主要机制或作为真实未知结构发现。**

## 10. J — 真实暗代谢组资源、跨研究复现与独立证据

来源：MS-paper `main.tex` 的 `Structurally resolving the reference-unmatched metabolome`：

| 数据/分析 | 数量 | 科学含义与边界 |
|---|---:|---|
| UC、IBD200、VEO-IBD 三项原始研究 | **348** expected acquisition files，已核验 **272**，缺失 **76** | 测量层级审计，不是化合物数 |
| QC eligible biological MS/MS queries | **835,953** | 查询/谱图级总量 |
| 无歧义接受reference身份 | **13,884** | 基于冻结匹配协议 |
| 有歧义接受reference身份 | **14,289** | 需要保留歧义 |
| 无接受参考谱匹配 | **613,331** | 未注释谱图查询，不等于613,331种新化合物 |
| 其余unassessable | **194,449** | 不能被算为暗谱图推断成功/失败 |
| 跨 ≥2 研究反复出现的谱图社区 | **2,255** | 社区，不是分子家族或已确认分子 |
| 跨全部3项研究的谱图社区 | **98** | 仅表示谱图再现；原文的拓扑随机对照p≈0.91 |

源论文中仍有用于暗谱图结构分辨等级、独立验证的 `\result{...}` 待完成内容；不得拿已注释benchmark上的漂亮数字替代真实暗谱图实验验证。

## 11. K — 实验审计：在投稿前必须锁定的数值冲突/归因风险

| 编号 | 问题/实际源码证据 | 对现有结果的影响 | 下一步最短修复 |
|---|---|---|---|
| QA-01 | `pr93_rsi_evolution_plan_and_gen7_report_20261109.md` 对同一1,996谱图写 Exact@10=331、Reach=306；违反相同池的子集关系 | 不能原样引用该行汇总 | 按case raw candidates与分母重算，标明候选池raw vs post-refinement |
| QA-02 | `eval_pr93_peak_ladder.generate()` 在写出rank shards后调用 `_apply_blind_precursor_cluster_consensus` 并覆盖rank文件；另一脚本把这些rank的top1称“single-spectrum” | 14,370的1.66%可能已部分被聚合污染 | 保存原始一次性single结果和共识后的独立文件，按同一谱图ID配对比较 |
| QA-03 | “multi_energy” 的脚本按 `meta[cid]["grp"]`参考分子ID聚合；blind组按 neutral mass + predicted formula | 3.37%不等于全未知条件下严格blind性能 | 单独标为“known-group assisted aggregate”并审计 blind neutral-mass误合并 |
| QA-04 | 多维summary中的zero-overlap字段硬编码0；`manifest_sha256`仅哈希5轴汇总字典 | 不能凭该summary单独声称证明所有外部候选无泄露 | 保留真实 input manifest SHA、原始库key14交集过程、最大MCES、预训练谱/结构来源审计 |
| QA-05 | “5-axis (18 sub-splits)”与脚本4+4+3+4+6=21不一致 | Caption/figure标签错误 | 明确五轴21层，各轴同一批样本，非独立新split |
| QA-06 | Public DB脚本 `A4→A5` 不只加数据库频次，还调整MMA/cleavage权重 | A5增益的因果归因不清 | 固定权重，只开关source-count先验，补“single DB vs union” |
| QA-07 | DB辅助表中的高分含公共库完整候选，known-formula和Macro-Core也有强先验 | 不可把31.57%、42.74%、52.5%称pure de novo | 在摘要/表头完整写setting |
| QA-08 | 历史官方TEST200、首1072、1996、14,370不共享最终完整分母和同一版本 | 数据不可当简单随Gen单调提高的准确率 | 冻结 model SHA、candidate来源、输入谱ID、预算，并输出 matched-case comparisons |
| QA-09 | Source中“Train-only decoys”与“cal200”有混用表述，需核对同分子组隔离 | V_g10 +5.22pt 可能只测同一hardnegative分布 | 分子/骨架组严格剔除、对照固定 V训练数据 |
| QA-10 | 最新4a07dc MMA打分权重变更发生于11月14日结果报告之后 | 不得把历史结果当成此commit再跑结果 | 固定`source_commit`和`eval_commit`不同字段 |
| QA-11 | 目前JSON各分类统计以谱图加权；一个分子可能有数十张谱图 | 超高/超低家族分层数可能受频次影响 | 加每分子macro与bootstrap-by-molecule置信区间 |
| QA-12 | 外部公共库中测试完整结构可作为候选；“0% InChIKey overlap in MMA/analog pool”不自动证明所有公共parquet也为0 | DB检索合理，但不具备“所有候选均未见GT”性质 | 候选来源分类：exact DB hit / homolog DB / G-only novelty / mixed |

## 12. 如何把结果写成科学论文（保留旧工作，不改变研究题目）

**R1. Available chemical knowledge and the limits of benchmark interpretation.** 用17,556条完整DB-assisted消融，报告“为何大规模化学知识有价值”，并区分 exact DB-known / novel-to-DB candidates、formula已知/盲、MMA/physical cleavage贡献；不要因为不是纯de novo就删除这条。

**R2. Fragment-guided molecular construction.** 用C1–C7、同checkpoint MMA、Canonical Hybrid动作与98分子序列证明G如何利用局部化学知识扩展候选。

**R3. Chemical evidence and structural identifiability.** 用W和MMA complement、765分子coverage-vs-discrimination、同池 W/V rerank与V_g10困难同式异构体证明“更多证据不一定有更高判别力”。

**R4. Multidimensional recoverability frontier.** 用五轴21层绘制结构泛化边界，并检查 family与候选来源/多视角的交互，要求分子组宏平均和候选池一致性。

**R5. Scientific Improver RSI and transferable expansion.** 用真实TRAIN FIT失败→Agent选择→同算力干预→held-out改善/退化→经验回流；区别Gen1–10历史工程过程与真实自主Agent因果结果。

**R6. Dark metabolomics application.** 将前述模型应用到 613,331 个no-reference-match谱图查询来源之中，汇总独立化学实体、具体结构解析等级及证据支持，不将谱图社区误报为已鉴定新分子。

**现有主框架与公共数据库先验路线保留。** 整篇论文的可检验主问题是：*不同可用化学知识与实验观测下，谱图能恢复多少分子结构信息，MMA/G/W/V各自怎样推进这一可恢复边界，Agent能否根据已测量的失败继续扩展它？*

## 13. 结果文件索引（固定源码路径）

下列是本次**确实重读过的关键权威来源**，不是仅凭过去对话的记忆：

1. [PR95 2026-11-14多维泛化+V_g10报告](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_multi_regime_benchmark_and_rsi_results.md)；[对应21层JSON](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_multi_regime_benchmark_summary.json)
2. [PR93/95 2026-11-09系统结果报告](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_test_generalization_and_mma_ablation_20261109.md)；[Gen1–10历史账本](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_rsi_evolution_plan_and_gen7_report_20261109.md)
3. [公共候选库八arm源码](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/scripts/eval_pr93_prior_mma_wv.py)；[多维分割源码](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/scripts/build_pr93_multi_regime_splits.py)；[G多谱图评测源码](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/scripts/eval_pr93_peak_ladder.py)
4. [G早期失败与近邻依赖](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/PR93_G_HISTORY_CASE_ANALYSIS_20261014.md)；[G结构修复上限](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_g_ceiling_20261019/summary.json)；[128例深度机制](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_g_mechanism_20261022/summary_cluster_all.json)
5. [W SEARCH_DEV300 诊断](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_model_audit_20261014/search_dev_summary.json)；[TRAIN765碎裂解释与异构体区分](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_fragmentation_gap_20261014/discrimination_summary.json)；[固定路径代价](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_fragmentation_gap_20261014/cost_weighted_summary.json)
6. [W contrastive R2](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_round2_20261014/gate_contrast_r2_best.json)；[W H-shift R5](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_w_round5_20261015/gate_honly_r5a_best.json)；[W/MMA补充](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_g_peak_msa_20261015/v_mma_complement_audit.json)
7. [MMA碎片严格合并](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_fragment_tree_mma_20261022/anchor_strict_merge6.json)；[TEST posthoc MMA选取上限](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_g_ranking_20261023/mma_selection_feasibility_3000.json)；[Na+携带诊断](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_na_adduct_audit_20261014/attachment_summary.json)
8. [DeepMech V5取消回执](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_v5_cancellation_20261013.json)；[Gen10 LLM Principal真实决定回执](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/outputs/pr93_rsi_daemon/llm_principal_gen10_receipt.json)
9. [MS-paper Supplementary WGV结果表](https://github.com/wangyu-sd/MS-paper/blob/main/supplementary/ORBIT_WGV_RSI_Results.tex)；[MS-paper 主文与真实暗谱图资源](https://github.com/wangyu-sd/MS-paper/blob/main/main.tex)

### 尚需直接访问才能闭环的原始集群产物

真实`outputs/pr93_v4loop_prior_mma_wv_fulltest_prior_mma_wv_w924c11f7_1h20_20261108a/results/`中的 **8-arm每shard summary**；14,370条的 **single pre-consensus 原始rank + blind/group共识rank及原始分子组meta**；真实`V_g10`的 **decoy_w.receipt、fit_receipt、实际split/重叠核验**；Gen1–10中每代的 **checkpoint SHA、前后同ID分子结果、Agent选择回执**；已提交但尚未纳入报告的 **全17,556 TEST剩余3,186条**及最新 `4a07dc` 更改后评测。

**覆盖声明**：这是已提交关键 source 文档/JSON中全部主要**可汇总实验系列**的总账，包含成功、负结果、历史/中途结果及拟执行的独立arms。项目有数百条训练/评测 job 和大量 Ceph-only输出；在没有共享存储逐次run清单前，不可假装已收录每一条具体GPU job或重算所有样本。本文件可作为后续追加逐次run的唯一母表。
