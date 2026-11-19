# ORBIT-MS — 一手证据驱动的论文深化方案（2026-11-19）

**目标：深化因果论证，而非扩写 Results。** 对 `main.tex` 的实际编辑只替换泛泛叙述；原始五张主图、实验指标、已报告的百分比及全部 `x` 结果槽位保留。本文件回答四个研究层面的问题，既提供编辑原则，也明确具体素材、操作与独立证据。任何“应做”的实验不等同于已完成。

## 一、顶尖研究者通常会额外做什么

**最重要的三个反事实，而不是扩大实验清单：**

1. **切断“只是候选变多”的解释。** 在同一前体、同一候选 ID、同一 W/V 与计算预算下，只替换匹配谱图为同离子类型/近似前体质量的独立 peer；或只替换 MMA 对齐与图动作。若结果只来自结构先验而非观测碎片，错误/匹配谱图之间的评分差应显著缩小。先看分子级 paired score delta，再看 Exact@1；固定池 Reach 必须不变。
2. **证明化学知识的跨分子转移，而非原样重现 source。** 对每个声称“学习带来的新恢复”记录 source 结构与原始谱图、质量/元素匹配、MMA 片段的分子图原子映射、实际执行的 motif/ring/atom 动作、target 分子新旧候选列表。关键对照：同样大小的随机/近邻 motif 词库、同样数量和预算的结构样本，以及关闭目标特定 motif 的恢复差。source 与 target 需要独立连接体，按结构近邻分层，报告新恢复与遗忘。**如果没有“source→action→target”的可追溯链，就不把知识库规模称为转移机制。**
3. **证明 Agent 的贡献是决策，而不是更多更新。** 冻结同一 Gen0 的 W、G、V、MMA、FIT 数据、独立评测和 GPU 预算，对比 Agent / 固定动作 / scripted failure-routing；每一代重算 FIT，记录决策、模型改变、目标恢复及损失。优先做三轮完整闭环，不需要新 agent framework。把 agent 的 advantage 定义为**预算匹配下净新增的独立正确分子数**，同时报告 memory-off 与决策变更的证据。历史 PR95 Gen 迭代和 PR96 LLM action receipts 是既有资产，但不能直接作为这个反事实的结果。

额外的专家判断是：`P(M\mid S, K)` 中由化学先验 `K` 贡献的确定性，和由实验谱图 `S` 提供的**候选特异信息**应分别识别。NMI 的创新不在于“又多一个 Agent”，而在于一条有可检验中间变量的**观测谱图→片段知识→实际图动作→新结构恢复→下一轮科学选择**链。

## 二、直接从哪些最原始的材料开始

| 主张 | 从原始输入回溯（按优先顺序） | 仓库中已有证据入口 / 缺口 |
| --- | --- | --- |
| 未注释谱图资源 | 原始 vendor RAW / mzML / mzXML、MS level、前体与产物 `m/z, intensity`、CE、adduct、source accession/USI、同一实验里的 scan IDs、空白/QC 和 reference-library 原始匹配 | `orbit-ms` PR94: `docs/results/pr94_model_independent_ms_full_raw_inventory_20261012/`、`...full_scan_qc_20261012/`、`...full_reference_match_20261012/`、`...full_recurrence_communities_20261013/`；PR94 的跨库哈希与 USI 对账目录。**这些是回执/来源目录，不等于已获得所有原始 RAW 字节。** |
| 已知分子正确性 | MassSpecGym v1.5 原始 spectra、原始 SMILES/SDF、官方 molecule-group / MCES 划分、原始 precursor formula 与 ion/adduct；原始 NPLIB1、CASMI 结构和实验谱图 | 上游 [MassSpecGym](https://github.com/pluskal-lab/MassSpecGym)、实际读取的官方数据快照与 SHA。现有 `docs/results/pr93_multi_regime_benchmark_summary.json` 只是聚合结果，**不应当是再分析的起点**。 |
| MMA 的知识转移 | 每条训练分子的 source 结构图、候选碎片的原子掩码及离子化假设、MMA 匹配记录、G beam 每步选择/剪枝、生成与排序原始候选列表 | `orbit-ms` PR95 的 `src/orbit_ms/wgv/`、`scripts/train_pr93_peak_ladder_hybrid.py`、每个 shard 的 `rank_*.jsonl`、libv1/v2/v3 构建回执。论文补充材料目前只有统计结果，无法替代逐 target 轨迹。 |
| 多代恢复 | Gen0 基线与每代真实 checkpoint、MMA 资源版本、FIT 失败原始 case IDs、原始模型输出、promotion 判据、实验计时/资源记录 | PR95 `docs/results/pr93_agent_generations_io_archive.json` 与关联 receipt；PR96 `src/orbit_ms/agents/scientific_improver.py`、`scripts/run_pr93_scientific_improver.py`。**PR95 累积多代融合、单谱和已知 molecule-group 多能量聚合必须分开**。 |
| 暗谱图化学关系 | 原始对应 USI 的实际实验峰、所提候选分子图、RDKit 原子映射与 graph edit、已知参比分子的数据库入库版本、独立其他采集或标品记录 | PR94 仅提供观察来源；PR95 GeMS-1000 主要是模型候选/评分。实际图关系及独立化学确认必须逐个回源，不直接把质量差转成酶反应。 |

**素材单位优先级：原始扫描/真实结构/逐分子模型候选/真实执行回执 > 逐分子汇总 > 项目报告。**

## 三、具体方法、工具与可执行验证方式

| 核查问题 | 建议工具 | 操作和产出 |
| --- | --- | --- |
| 一条谱图能否从公开记录复现 | GNPS2 Dataset Explorer、MassIVE、MetaboLights、GNPS USI；ProteoWizard `msconvert`、`Pyteomics` / `pymzML`、`matchms` | 从 accession/USI 取原始文件；保留原始和标准化峰数组及处理参数；独立生成原始峰图和峰匹配表；对原始字节、转档与扫描归属分别计算 SHA-256 |
| 分子是否在训练或外部知识中出现 | RDKit canonical SMILES、InChIKey-14、Murcko scaffold、ECFP/Morgan；官方 MCES；MassSpecGym v1.5 | 用真正进入预训练/MMA/检索的 SDF/SMILES 集合做 exact + nearest-neighbour audit；按独立分子组报告，不以“看不到测试 MS2”替代结构级排除 |
| W/V 何以优于结构先验 | `matchms`、`numpy/scipy`、`pandas` 或 `duckdb`、自有 W/V evaluator | 同一候选池 × (matched MS/MS / compatible peer / peak-mass ablation) 逐候选配对，统计 score margins、Exact@1、Reach 和显著诊断峰；保持候选数相同 |
| MMA 是否真的跨分子迁移 | RDKit `FindMCS`、原子映射、SMARTS 匹配；G beam trace；图动作复演 | 按 motif source→target 追踪，对关闭该 motif / 体积匹配随机 motif / 相近 scaffold 种子做消融；输出独立 target 的原始候选池和新增真分子 |
| Agent 是否比固定规则更高效 | PR96 Scientific Improver controller；`pytest`；`scipy.stats`、cluster bootstrap / paired permutation | 相同 Gen0/数据/模型预算下 Agent vs Fixed vs Scripted，核对每轮 FIT、决策、训练记录与净新增/遗忘分子；按独立分子组 bootstrap CI，按 GPU-hour 比较效率 |
| 分子家族是否是真正的化学关系 | RDKit MCS/最大公共骨架、可解释 graph edit、MassBank/MoNA/HMDB/ChEBI 日期快照 | 输出 2D 图而非嵌入图，列出逐原子差异和对应实测峰；结构近邻与离子形式/重复扫描排除；使用先验/尺寸/分子式匹配对照 |
| 化学假设能否独立复核 | 外部独立 MS/MS / 实测 MSn；标准品 LC-MS/MS 与 retention/coelution；人工化学专家盲审 | 对 5–10 个选定锚点逐案例比较可区分的候选结构；保留确认、歧义、否定结果和源号。**只有真实获得的证据才计入完成。** |

具体论文引用与可独立使用的工具入口：

- MassSpecGym v1.5 及 2026 年评测问题审查：https://github.com/pluskal-lab/MassSpecGym ；https://arxiv.org/abs/2606.19624
- GNPS2 / Pan-ReDU 原始来源与文件级下载：https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/ReDU_overview/
- matchms 原始谱图处理与对比：https://github.com/matchms/matchms
- Pyteomics：https://pyteomics.readthedocs.io/ ；RDKit：https://www.rdkit.org/

## 四、除了我们之外，什么证据真正能确认结论

**不同主张需要不同的、互不替代的证明人/证明物。**

1. **统计层面：** 由独立团队运行开源评估代码，对官方未触碰的分子组复现 Top-K/Reach，检验 `Exact@1 <= Exact@10 <= Reach`、候选池单位、完整分母和不同先验条件。独立方不使用作者选定的成功案例或仅作者汇总表。
2. **模型机理层面：** 候选集合不变时更换真实谱图的 counterfactual 控制，说明模型对化学观测敏感。另由训练之外的 source→target 分子证据链表明具体知识确实被用于新的连接关系，而不是仅因为分子库覆盖更广。
3. **自主学习层面：** 第三方根据冻结 checkpoints、FIT snapshots 和历史 receipts 重新执行 Agent/Fixed/Scripted 的同步队列，对齐 GPU 预算与输出指标。真正的外部证明是**运行结果和模型权重改变**，不是 LLM 自己描述成功。
4. **化学层面：** 与训练、候选筛选均独立的仪器测量/真实参考谱；尽可能由其他实验室测量同一标品或相关可区分的异构体。公开 GNPS/MassBank 谱图、USI 和实际 MSn 对应观测可以构成外部谱学支持；标准品 LC-MS/MS 加 retention/coelution 可构成更强确认。
5. **科学意义层面：** 从模型所提真实结构和新关系出发，先追踪既有结构数据库与文献，再验证一个可以独立复测的结构变化系列。真实分子家族发现不等于算法聚类，也不必强行延伸到未经验证的生物机制。

## 建议仅优先完成的三项决定性新实验

**P1 — Fixed-candidate paired-spectrum counterfactual.** 量化测得峰真正引入的结构判别信息（R2/Extended Data），低成本重排和对照。

**P2 — One source-to-target motif-transfer chain + matched ablation.** 用真实 source 谱图、motif 原子映射、目标分子的 G 动作和候选恢复构成端到端化学故事（R2/R3）。

**P3 — Three-episode Agent vs Fixed vs Scripted at matched GPU cost.** 用新独立分子净新增恢复率与遗忘来证明递归科学决策的价值（R3）。

主文**保留全部已有数值、正向但尚未完成的 x 占位、五张主图**；具体测量可依次替换对应 x，而不再扩大 Results 的模块和名词数量。
