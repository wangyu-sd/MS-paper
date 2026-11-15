# ORBIT-MS Gen1–Gen10 全量代际结果账本

**整理日期：2026-11-15（Asia/Shanghai）**  
**用途：** 完整保留 PR93/PR95 中 Gen1–Gen10 的研究动机、干预、训练与评测结果、跨 benchmark 进展、正负结果及数据口径。  
**本文件不是重新训练或重新评分的报告**：数值逐项来自已有 PR 记录、结果文档和 MS-paper Supplementary。Ceph 上未同步到 GitHub 的所有逐例预测/日志/模型 checkpoint 尚未全部直接复算。

## 0. 阅读原则：Gen代际不是一个单一、同分母的准确率曲线

Gen1–Gen10 是持续演进的 WGV/RSI 工程与科学开发序列。各代会同时改变训练数据、MMA词表、生成动作、候选起点、候选排序和多谱图聚合，因此不同代际的 TEST200、CAL200、CAL100、完整TEST分片、NPLIB1、CASMI不能直接画成一条单调上升的准确率曲线。

- **CAL200 49.00%/52.50%** 是同源 Macro-Core 辅助补全，不是空图纯 de novo。
- Gen1–Gen10 历史开发结果不等于 PR96 Lightweight Scientific Improver 已完成十轮自主 Agent 实验。多数代际是根据失败诊断开展的人工/脚本工程干预；Gen10有一次可核对的LLM Principal决策receipt。
- Official TEST在开发过程中被用于评估与选型。即使有InChIKey去重，也不能把这些迭代TEST结果称为最终untouched blind benchmark。
- 报告中有数值关系不自洽（如Exact@10大于Reach），本账本忠实保留原报告值并显式标注，不自行“修正”。

**核心来源：**
- [PR95](https://github.com/wangyu-sd/orbit-ms/pull/95)（分支 `feat/pr93-v4-wgv-train-loop`）
- [PR93](https://github.com/wangyu-sd/orbit-ms/pull/93)
- [Gen1–Gen10 evolution ledger, 2026-11-09](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_rsi_evolution_plan_and_gen7_report_20261109.md)
- [PR95 progress and ablations, 2026-11-09](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_test_generalization_and_mma_ablation_20261109.md)
- [MS-paper Supplementary Tables S14 onward](https://github.com/wangyu-sd/MS-paper/blob/main/supplementary/ORBIT_WGV_RSI_Results.tex)
- [2026-11-14 multi-regime / V_g10 report](https://github.com/wangyu-sd/orbit-ms/blob/feat/pr93-v4-wgv-train-loop/docs/results/pr93_multi_regime_benchmark_and_rsi_results.md)

## 1. Gen1–Gen10：逐代科学诊断、干预与当代结果

| Generation | 在TRAIN calibration诊断出的瓶颈 | 主要方法 / 训练干预 | 该代报告的关键结果 | 解释与边界 |
|---|---|---|---|---|
| **Gen1** `20261107a` | **38.6-step atom-by-atom horizon explosion**：37-heavy-atom分子平均约38.6个连续原子/键决策，长程误差累积；未见骨架Top-1为0 | MMA libv1（4.23M entries）+ 500-entry RingVocab；HybridStagePolicy引入 `mstart/mattach/rstart/rattach` | Official TEST `test200` Exact@1 **0.00%**、Exact@10 **1.00%**；Tanimoto@1 **0.1612**、@10 **0.2175**、pool max **0.2480** | 建立motif/ring多粒度动作接口；仍未解决完整结构恢复 |
| **Gen2** `138698b2` | **Replay disqualification gap**：75%有效多原子MMA Motif被相邻peak stages切开，无法按完整motif回放，只能退回单原子add | Closed Motif Ladder Sets（rings + motifs）；`_select_canonical_step` motif-first tie-break | 平均轨迹长度：38.6 → 24.3 → **10.59 decisions/molecule**；单原子add均值 **4.45**；`top_canon=60.2%`。Official TEST `test200` Exact@1 **0.00%**、Exact@10 **0.00%**；Tanimoto@1 **0.1699**、@10 **0.2142**、max **0.2410** | 主要改善可执行轨迹和动作表示；没有带来可测TEST精确命中 |
| **Gen3** `20261108b/d` | **Beam normalization gap**：按step平均的beam score惩罚一次接入10个原子的mattach，导致Motif被剪枝 | Heavy-atom normalized beam：`score / max(4, n_atoms+2)`；每步保留top-3 `mattach/rattach` expansion | Evolution report：CAL200 Exact@1 **12.50%**、Reach **22.50%**；Official TEST `test200` Exact@1 **0.50%**。Supplementary official-test ledger：Exact@1 **0.50%**、Exact@10 **0.50%**；Tanimoto@1 **0.1799**、@10 **0.2174**、max **0.2495** | CAL结果的代际标签与Supplementary calibration progression存在错位：后者把12.50%归到Stage Gen4，需按checkpoint/run ID统一 |
| **Gen4** `20261109b` | **Symbolic vocabulary coverage gap**：18,425 TRAIN groups对未见天然产物/药物子结构的fragment覆盖不足 | Frozen 3-cut W对 **99,302** 个无VAL/TEST重叠HMDB代谢物模拟MS2；MMA从v1扩至libv2：**12,983,158 entries / 115,383 groups** | Official TEST `test200` Exact@1 **2.00%**（[M+H]+ **2.53%**）；Tanimoto@1 **0.1904**、@10 **0.2291**、max **0.2700** | 首次大规模Forward Sleep扩展MMA；数据扩展后TEST200较Gen3提高 |
| **Gen5** `20261109e` | **Single-start fragility / prototropic shift gap**：MMA首个peak hypothesis噪声会导致单起点失败；keto-enol互变导致近似结构错误 | Dual empty start（beam=12）+ MMA-seeded rollouts；8-GPU继续训练libv2；first-order post-W/V refinement | Official TEST `test200` Exact@1 **2.00%**、Exact@10 **2.50%**；Tanimoto@1 **0.1972**、@10 **0.2469**、max **0.2840**；[M+H]+ Tanimoto@1 **0.2067**、max **0.2949** | 相较Gen4主要改善Top-10与结构相似度，不应声称Exact@1提升 |
| **Gen6** `e4d4c72c / 20261109f` | **Long-horizon macro-scaffold gap**：>32 heavy atoms的macrocycle/polycycle在第12–18步前beam已掉出，核心环闭合失败 | Biogenetic Homology Macro-Core Peeling：从非VAL/TEST、L1≤3同源分子裁剪partial graph；`complete_macro_starts`由神经G补1–3步 | Held-out CAL200：Exact@1 **49.00% (98/200)**、Exact@10 **73.00%**、Reach **90.00% (180/200)**、Tanimoto@1 **0.6601**、@10 **0.8253**、max **0.8640**。Official TEST `test200`的Supplementary快照：Exact@1 **4.00%**、Exact@10 **10.00%**、Tanimoto@1 **0.2803**、@10 **0.3603**、max **0.4114**。Evolution摘要另记TEST200 Reach **6.50%**、Tanimoto max **0.3889** | CAL高分是**同源骨架辅助神经补全**；不能称纯空图de novo。不同TEST200快照存在指标差异 |
| **Gen7** `58a85509 / 6a5fa7c1` | **Isomer ranking gap**：Gen6已生成Beauvericin、Letrozole、Roxithromycin、Clarithromycin、EGCG、Erythromycin等，但被ring-closure/quinoid decoys压过 | Within-formula Morgan MBR consensus centrality；Hückel aromaticity + Baeyer ring-strain prior；第二轮64态keto-enol、10×24 substituent relocation self-inversion | Evolution摘要：Top-10中的真解100%升到Rank1；Exact@1 **5.00%（full test200）**、first100 **10.00%**、first60 **16.67%**。Supplementary另一官方TEST快照：Exact@1 **10.00%**、Exact@10 **10.00%**、Tanimoto@1 **0.2904**、@10 **0.3603**、max **0.4114**。恢复cyclic tetrapeptide `0002114`、tetracycline `0058046` | 不是G-only：包括MBR centrality和手工化学topology prior；不同test200子集/版本的5%与10%不可合并 |
| **Gen8** `02416f06 / 20261110a,b` | **Glycoside vocabulary / sim-to-real gap**：HMDB对植物糖苷/皂苷覆盖不足；报告称37% TEST cases的formula未进入Top-3 | Dual Wake–Sleep：93,374条COCONUT+ChEBI+LipidMaps+NIST23模拟谱；MMA libv3 **31,106,023 entries / 187,232 groups**；GeMS-1000 real-unlabeled wake pseudo-labeling + **2,580 hindsight W spectra**；8-GPU Gen8 `ladder_epoch_0..5.pt`；15-ppm homolog formula rescue | Bare policy CAL100：Exact@1 **7.37%**、Exact@10 **11.58%**、Reach **16.84%**、Tanimoto@1 **0.3053**。报告列出5个天然产物糖苷案例：Tubuloside B（#1）、Acteoside（#3）、Strictosidine、Ginsenoside、Lignan glycoside；Tanimoto max **0.4122**。Official TEST `test200` Gen7∪Gen8 cross-gen memory：Exact@1 **5.50%**（second-round **6.50%**）、Exact@10 **6.00%**、Reach **9.50%**（cross-gen **10.50%**）、Tanimoto@1 **0.2583**、@10 **0.3404**、max **0.4122** | CAL bare policy与TEST cross-generation memory是不同协议。libv3是结构/模拟知识规模，不等于全部31M条均已转化为wake监督 |
| **Gen9** `e0207ac9 / 1dc1cd1f` | **InChI iminol-amide representation gap + 3-step combinatorial dilution**：标准InChI表示将部分amide写成iminol；3-step partial cores挤占1-step候选预算 | Thermodynamic iminol→amide restoration；alicyclic ring-CH2 contraction pruning；优先`rem==1`，其次2/3；`_PRUNE_STATE_CACHE` | TEST200 exact-GT substructure coverage报告由 **13.5%升至27.0–33.5%**（这是substructure coverage，不是Exact@1）。启动64-shard MassSpecGym 17,556、CASMI2022、NPLIB1评估。p0of4首1,072条结果：Exact@1 **17.63%**（[M+H]+ **18.84%**）、Exact@10 **25.65%**（[M+H]+ **27.60%**）、Reach **29.41%**；这是带有Gen9路径名的中途分片 | 主要提升partial-core候选覆盖与搜索预算分配；17.63%只对应已完成首1,072条，不是全TEST |
| **Gen10** `5cfb2d8f / 20261111c,d` | **Acyclic polyazo artifact + PKS/NRPS branching + isolated single-energy decoding**：同一precursor在不同collision energy的证据此前分开解码 | Acyclic polyazo instability filter；PKS tertiary-carbinol / NRPS isopropyl branching priors；按`(adduct, precursor_mz)`对跨collision energy证据做unsupervised precursor-cluster consensus | Evolution report：p0of4累计 **1,996 spectra / 471 groups**：Exact@1 **8.02% (160/1996)**（[M+H]+ **8.72%**）；Exact@10 **16.58% (331/1996)**（[M+H]+ **18.28%**）；Reach **15.33% (306/1996)**；Tanimoto@1 **0.3120**、@10 **0.4180**、max **0.4790**。Gen10b block-transform test200：Exact@1 **4.50% raw / 6.50% cross-gen**；Exact@10 **6.00%**；Reach **7.50% single / 10.50% cross-gen**；Tanimoto@1 **0.2445**、@10 **0.3202**、max **0.4156** | 1,996条表中Exact@10计数331大于Reach计数306，违反同一候选池下Exact@10≤Reach；原报告值保留但**不能作为最终主指标**，必须回到逐例rank和reach定义 |

## 2. 官方 TEST 代际快照：Supplementary 中 Gen1–Gen7 的逐代数值

以下逐字按 MS-paper Supplementary 的 `tab:rsi_gen_ledger` 整理。它明确说明Gen6/Gen7为interim partial snapshots，官方TEST在开发迭代中被查看，不能解释为最终独立blind holdout。

| Gen | Exact@1 | Exact@10 | Tanimoto@1 | Tanimoto@10 | Pool maximum |
|---|---:|---:|---:|---:|---:|
| Gen1 | 0.00% | 1.00% | 0.1612 | 0.2175 | 0.2480 |
| Gen2 | 0.00% | 0.00% | 0.1699 | 0.2142 | 0.2410 |
| Gen3 | 0.50% | 0.50% | 0.1799 | 0.2174 | 0.2495 |
| Gen4 | 2.00% | 2.00% | 0.1904 | 0.2291 | 0.2700 |
| Gen5 | 2.00% | 2.50% | 0.1972 | 0.2469 | 0.2840 |
| Gen6† | 4.00% | 10.00% | 0.2803 | 0.3603 | 0.4114 |
| Gen7† | 10.00% | 10.00% | **0.2904** | 0.3603 | 0.4114 |

† Gen6/Gen7为中间评测快照。与Evolution report中的Gen7 full-test200 Exact@1=5.00%不一致，需核对模型/候选池/后处理版本。

## 3. CAL / VAL：生成能力与组件进步（另一个独立命名序列）

### 3.1 Held-out CAL200，known-formula，Beam=16：同checkpoint MMA消融

| 配置 | Teacher loss↓ | Teacher@1 | Start@1 | Select@1 | Exact@1 | Exact@10 | Reach | Tan@1 | Tan@10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Without MMA | 0.996 | 69.1% | 76.4% | 54.6% | 1.50% | 4.50% | 6.50% | 0.2009 | 0.2640 |
| With MMA | **0.757** | **76.0%** | **86.3%** | **67.5%** | **6.00%** | **14.50%** | **19.00%** | **0.3221** | **0.4215** |

### 3.2 Held-out CAL200，known-formula：逐步加入MMA starts、W/V和Canonical Hybrid

| Stage | 配置 | Exact@1 | Exact@10 | Reach | Tanimoto@1 | Tanimoto@10 |
|---|---|---:|---:|---:|---:|---:|
| Gen0 | Atom-only / no MMA | 1.50% | 4.50% | 6.50% | 0.2009 | 0.2640 |
| Gen1 | MMA features | 6.00% | 14.50% | 19.00% | 0.3221 | 0.4215 |
| Gen2 | MMA features + W/V terminal ranking | 8.50% | 13.50% | 16.00% | 0.3351 | 0.4152 |
| Gen3 | Eight MMA starts + W/V | 10.00% | 18.00% | 19.00% | 0.3752 | 0.4685 |
| Gen4 | Canonical Hybrid + atom-normalized/motif-reserved beam | **12.50%** | **21.50%** | **22.50%** | 0.3811 | **0.4938** |

**注意：** 此表中的Gen0–Gen4是CAL消融stage标签，不是上面RSI Gen1–Gen10历史账本的同一代际编号。不要直接按相同数字拼表。

### 3.3 Canonical Hybrid 256分子、1×H20、30轮对照

| Branch | Mean decisions | top_canon | top_valid | seen64 Exact@1 | seen64 Reach | seen64 Tan@1 | fit100 Reach |
|---|---:|---:|---:|---:|---:|---:|---:|
| stg256 random order, beam4 | 32.4 | — | 90.6% | 25.0%（ep24 20.3%） | 37.5% | 0.488 | 13.3% |
| hyb256 canonical+motif+R_t, beam4 | 24.5 | 84.7% | 90.6% | **32.8%**（ep24 31.3%） | 42.2%（ep24 43.8%） | 0.518 | 14.3% |
| dir256b16 direct one-stage | **9.1** | 74.6% | 82.9% | 17.2% | 31.3% | 0.367 | **31.3%** |
| hyb256b16 canonical+motif+R_t gate | 24.6 | **86.0%** | **90.7%** | 28.1% | **53.1%** | **0.534** | **27.1%**（ep9 Exact@1 12.5%） |

GT-conditioned 98分子轨迹探针：平均总步数32.4→24.8（-23.5%）；真实长分子决策20.1→12.9（-36%）；87%分子使用Motif动作，平均一次接入4.5 heavy atoms；98/98可沿GT canonical action完整重建。此为trajectory feasibility，不是未知谱图准确率。

### 3.4 8卡全量训练主模型 `otflr8c48`

- 在18,425 TRAIN fit molecule groups上从第11轮续训，48轮完成（60轮等效），checkpoint `ladder_epoch_47.pt`。
- Train loss：0.578 → **0.427–0.432**。
- 单步train top1 **86.0%**；teacher loss **0.451**；teacher top1 **85.0%**（grow **79.7%**）。
- 100个拟合集分子、beam4：Exact@1峰值 **16.0%**、Reach **20.0%**。
- 这些是训练拟合集诊断，不能当作独立VAL/TEST性能。

### 3.5 W/V固定候选池重排（200 CAL/VAL）

| 同一候选池评分方式 | Exact@1 | Exact@10 | Reach | Tan@1 |
|---|---:|---:|---:|---:|
| G policy only | 7.00% | 11.50% | 16.00% | 0.3170 |
| G + explained intensity | 7.00% | 11.50% | 16.00% | 0.3179 |
| G + W/V higher weights | 7.50% | 13.50% | 16.00% | 0.3327 |
| G + W/V selected weights | **8.50%** | **13.50%** | 16.00% | **0.3351** |

这组同池实验说明W/V提升候选排序而不改变Reach。

## 4. Gen7代表性结构恢复与二轮refinement案例

### 4.1 Gen7候选升至Rank 1的代表性案例

| MassSpecGym ID | Molecule | Formula | Heavy atoms | 初始→最终排名 |
|---|---|---|---:|---:|
| 0000201 | Beauvericin | C45H57N3O9 | 57 | 2→1 |
| 0039311 | Roxithromycin | C41H76N2O15 | 58 | 4→1 |
| 0012997 | Clarithromycin | C38H69NO13 | 52 | 5→1 |
| 0012696 | Erythromycin | C37H67NO13 | 51 | 9→1 |
| 0064680 | Epigallocatechin gallate | C22H18O11 | 33 | 6→1 |
| 0014764 | Verapamil | C27H38N2O4 | 33 | 1 |
| 0028493 | Candesartan | C24H20N6O3 | 33 | 1 |
| 0142445 | Diphenoxylate | C30H32N2O2 | 34 | 1 |
| 0076066 | Letrozole | C17H11N5 | 22 | 3→1 |
| 0181733 | Unnamed MassSpecGym entry | C16H23N5O | 22 | 1 |

这些案例使用Morgan-fingerprint centrality和手工chemical-topology prior；Gen6/7 Macro-Core路线也是partial homology seed + G completion。它们不是fingerprint-free G-only结果。

### 4.2 二轮candidate-guided W/V refinement

| Molecule | 初始候选 | 干预 | 结果 |
|---|---|---|---|
| Cyclic tetrapeptide（0002114） | Top-2，linear n-propyl side chain，Tanimoto 0.833 | 外围n-propyl→isopropyl重新连接 | Exact GT recovered |
| Tetracycline（0058046） | Top-1，shifted keto-enol tautomer，Tanimoto 0.697 | 枚举最多64个tautomer并用W/V评分 | Exact GT recovered |
| EGCG（0064680） | Gen6 Top-1 quinoid artifact，Tanimoto 0.431 | topology prior score -0.80，拒绝该候选，提升原rank6 | Exact GT promoted to rank1 |

## 5. Gen8–Gen10资源、Wake–Sleep与自适应课程

### 5.1 代际资源增长

| 资源/阶段 | 规模 | 报告状态 |
|---|---:|---|
| MMA libv1 | 4,230,707 entries / 20,430 groups | TRAIN-derived，已建立 |
| HMDB-W模拟谱 | 99,302 HMDB metabolites（Gen4报告） | W forward-sleep输入 |
| MMA libv2 | 12,983,158 entries / 115,383 groups | TRAIN + HMDB-W；220,642 ion-formula keys |
| HMDB-W另一汇总口径 | 129,146 spectra / 32,229 groups | Supplementary资源表记录 |
| Gen8 multi-source simulated spectra | 93,374 | COCONUT + ChEBI + LipidMaps + NIST23 |
| MMA libv3 | 31,106,023 entries / 187,232 groups | Gen8/10报告记录 |
| GeMS-A de-leaked MS/MS | 41,578,985 spectra | 可用于real wake的资源总量，不等于全量都已训练 |
| GeMS-1000 wake | 1,000 queries | Gen8 bounded wake配置 |
| Hindsight W spectra | 2,580 pairs | 已生成；需区分生成与全部被后续训练消费 |

### 5.2 Failure-cluster & anchor-gated adaptive curriculum

`compute_adaptive_curriculum_mix`使用TRAIN calibration残差决定四路训练流：

- 18,425个真实MassSpecGym TRAIN groups作为anchor，每个epoch保留100%。
- 如果`seen.exact1`没有下降超过0.005，合成self-distillation quota×1.25（19,200→24,000 groups/epoch，Real:Self-distilled约43.4:56.6）；若anchor forgetting超过0.020，合成quota×0.75。
- 三类残差：小分子unreached（reach=0）；大型天然产物/糖苷unreached（len(SMILES)>42或nO≥6）；候选已reach但ranking失败（reach=1, exact1=0）。
- Evolution报告给出的CAL200例子：HMDB-W **5.7%**、MultiSource COCONUT/ChEBI/LipidMaps-W **15.6%**、GeMS Real-Wake+Hindsight **78.7%**（18,881 groups/epoch）。

这是规则化自适应课程控制器的代码/报告结果；它不等于十代都由LLM自主选择。

### 5.3 Gen10 LLM Principal receipt（一次真实决策，不代表全部Gen自动化）

`outputs/pr93_rsi_daemon/llm_principal_gen10_receipt.json`记录：
- API/model：DeepSeek V4 Flash（receipt标记`LLM_PRINCIPAL_VERIFIED`）。
- Hypothesis：真实GeMS wake不足，复杂天然产物和异构体敏感结构的reach/rank不足；HMDB/NP glycoside sleep占比稀释区分性信号。
- Selected intervention：`EXPAND_NP_AND_WAKE`。
- Synthetic self-play budget：26,000 / epoch。
- Stream weights：HMDB sleep **0.04**；multi-source NP glycoside sleep **0.12**；GeMS real wake + hindsight **0.84**。
- Target families：alkaloids、terpenoids、glycosides、macrolides、polyketides、aromatic heterocycles。
- Rerank weights：W **0.7**、V **0.2**、centrality **0.1**。

Receipt证明决策被记录，不证明该次决策导致了Gen10完整TEST或V_g10的性能提升。需对应checkpoint、训练完成、同ID前后评测才能建立因果链。

## 6. Gen9/Gen10报告的多benchmark结果

这些是当时PR95记录的跨benchmark完整运行，不应被当作同一benchmark的一条Gen1→Gen10曲线。

| Benchmark / 运行 | N | Exact@1 | Exact@10 | Reach | 其他 |
|---|---:|---:|---:|---:|---|
| MassSpecGym TEST p0of4 first 1,072 | 1,072 | 17.63%（[M+H]+ 18.84%） | 25.65%（[M+H]+ 27.60%） | 29.41% | Tan@1 .3890 / @10 .4850 / max .5420 |
| MassSpecGym TEST p0of4 latest cumulative | 1,996 / 471 groups | 8.02%（160/1996；[M+H]+ 8.72%） | 16.58%（331/1996；[M+H]+ 18.28%） | 15.33%（306/1996） | Tan@1 .3120 / @10 .4180 / max .4790 |
| MassSpecGym p0of4 shard | 4,400 spectra / 950 groups | 5.59% [M+H]+ | 11.27% [M+H]+ | 10.73%（472/4400；96 groups） | 与首1,072分片不一致，须按统一rank文件复算 |
| NPLIB1/CANOPUS official test | 813 | 16.73%（136/813；raw14.02%） | 31.98%（260/813） | 41.82%（340/813） | Formula@K 85.12%；Tan@1 .4540 / @10 .6069 / max .6433 |
| CASMI 2022 positive-mode blind | 237 | 4.64%（11/237；raw3.38%） | 11.39%（27/237） | 16.46%（39/237） | Formula@K 90.30%；Tan@1 .3017 / @10 .4105 / max .4466 |
| Gen7∪Gen8 cross-generation memory test200 | 200 | 5.50%（second-round 6.50%） | 6.00% | 9.50%（cross-gen 10.50%） | Tan@1 .2583 / @10 .3404 / max .4122 |
| Gen10b biogenetic block-transform test200 | 200 | 4.50% raw（cross-gen 6.50%） | 6.00% | 7.50% single（cross-gen 10.50%） | Tan@1 .2445 / @10 .3202 / max .4156 |

**严重一致性问题：** 1,996条报告中的Exact@10 331/1996 > Reach 306/1996；4,400 shard报告中的Exact@10 11.27% > Reach 10.73%。若Reach指同一候选池内GT出现，理论上不应发生。需回查逐例输出、分母、candidate pool与post-refinement是否一致，不能把这些行作为正式最终指标。

## 7. Gen10之后的结果：不要错误归入Gen1–Gen10

2026-11-12至11-14又有Gen12 destroy/regrow、Gen13 cross-energy W/V、Agent SMARTS prior、MMA scoring权重和multi-regime评测等后续代码/结果。它们应另列为post-Gen10 extension。2026-11-14的14,370-spectrum multi-regime报告与V_g10 hard-isomer win-rate **56.00%（相对初始50.78%，+5.22pt）**，不是Gen10主代际表里已完成的同口径完整TEST结果。

## 8. 投稿前必须保留的解释与审计边界

1. **Official TEST迭代使用：** MS-paper Supplementary明确说明Official TEST子集曾用于迭代开发。即使报告称模型/自生成库按InChIKey-14排除3,906个VAL/TEST/CASMI/NPLIB键，也不能将迭代TEST称为最终未触碰盲测。
2. **不同代际编号冲突：** Evolution report Gen3 CAL200 Exact@1=12.5%，而Supplementary calibration progression把12.5%放在Stage Gen4。保留两套命名，需用checkpoint SHA和run ID对齐。
3. **Gen7 TEST200冲突：** Evolution report写full test200 5.0%、first100 10%、first60 16.67%；Supplementary表写Gen7 10%/10%。需要原始200 case manifest确认。
4. **Gen6 TEST Reach冲突：** Supplementary Gen6表有Exact1 4%、Exact10 10%；Evolution摘要另给Reach6.5%、Tanimoto max .3889；不在没有run receipt时拼接。
5. **Gen10 Exact@10 > Reach：** 1,996和4,400两个报告行均有子集关系冲突。
6. **CAL200 49%/52.5%：** Evolution multi-benchmark table将49.00% raw和52.50% Gen10并列，但需要对应postprocess与模型/评估receipt解释差值。
7. **Gen8资源：** 93,374模拟谱、2,580 hindsight pairs的“生成”与“全部被下一代训练消费”是两个不同状态；Supplementary明确full-scale GeMS wake–sleep cycle仍需receipt闭环。
8. **Anti-leakage：** Evolution report声称InChIKey-14 overlap 0/3,906、purge 372,937 GeMS spectra；这些是报告声明，应保留原始清单/脚本/哈希以供审稿人复核。
9. **Gen1–10不等于PR96 autonomous RSI：** 这是持续迭代的WGV开发代际。Gen10的LLM Principal receipt是一条真实Agent决策，但尚未证明十代均由Agent自主选择或Agent相对固定策略带来独立增益。

## 9. 对主文和补充材料的建议

- Supplementary保留本文件的完整代际历史、每代机制与历史数值。
- Main Results不要把Gen1–10画成简单Exact@1单调增长曲线；应按**候选构造能力、证据判别、训练/知识扩展、跨benchmark和多维泛化**分组。
- 对CAL200高结果明确标注known-formula与homology-assisted。
- 对数据库候选识别保留17,556谱图的31.57%结果，和G生成/补全系列分开报告。
- 对RSI科学主张，下一步应使用同起点同预算的固定策略/规则策略/Agent决策对照，提供每一代的失败诊断、决策receipt、训练数据diff、checkpoint SHA和held-out分子级收益。

**结论：** Gen1–Gen10的研究价值不仅是一个分数从0%上升到某个高点，而是每一代针对不同的瓶颈做了可解释的干预：动作跨度、轨迹回放、beam归一化、MMA知识覆盖、起点鲁棒性、macro-core长程生成、异构体排序、天然产物sim-to-real、结构表示/搜索预算、跨能量共识。以上所有已报告结果应当保留，同时将不同评测协议和未闭环回执明确区分。
