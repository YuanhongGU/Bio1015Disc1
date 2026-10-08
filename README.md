# 如何说明一个模型是有效的
## 和实验测量的相关

输入是序列，真值是已经测到的信号，对照是上一代模型。AlphaGenome 在没见过的基因组区间上，24 项轨道预测里 22 项超过当时最强外部模型，26 项变异效应评估里 25 项达到或超过最强外部模型。下图只保留能与 Borzoi 直接比较的三项。

![AlphaGenome 与 Borzoi 的三项变异效应指标](figures/alphagenome.png)

高置信 eQTL 的相关系数是 0.73，Borzoi 是 0.61；可变多聚腺苷酸化是 0.894 对 0.790。因果 eQTL 的 auROC 是 0.75 对 0.71，其中 0.75 已经是多模态分数再经随机森林的结果，模型自己只有 0.68。全体 17,675 个精细定位 eQTL 的有符号 Spearman 相关是 0.50，只看效应绝对值则降到 0.10。有效性集中在强信号子集。

Avsec, Ž. et al. *Nature* (2026). https://doi.org/10.1038/s41586-025-10014-0

## 通过率

事先定一条及格线，再数有多少样本越过它。ESMFold2 的及格线是 DockQ ≥ 0.23。抗体–抗原来自 FoldBench；蛋白–蛋白的单序列 70% 来自 Runs N' Poses，带多序列比对的 76% 与 AlphaFold 3 的 73% 为论文直接对照。

![ESMFold2 与 AlphaFold 3 的复合物通过率](figures/esmfold2.png)

仅用序列时，抗体–抗原通过率 50%，高于带多序列比对的 AlphaFold 3（47%）。加上多序列比对后，抗体–抗原为 53%，蛋白–蛋白为 76%，两类都高于 AlphaFold 3。误差约 ±1 到 ±2 个百分点。单序列蛋白–配体通过率为 66%，论文未给同设定的 AlphaFold 3 对照，故未画入。这证明的是结构坐标，结合自由能和细胞功能要另测。

Candido, S. et al. *bioRxiv* (2026). https://doi.org/10.64898/2026.06.03.729735

## 湿实验读数

做出分子，再测结合或活性。BoltzGen 共 8 组实验、26 个靶点，读出为表面等离子共振或生物层干涉的亲和力，部分还有细胞或抑菌功能。下图按靶点计成功率。

![BoltzGen 按靶点计的湿实验成功率](figures/boltzgen.png)

9 个新靶点在整个蛋白质数据银行中没有序列一致度高于 30% 的结合态蛋白，每个靶点最多测 15 个设计：纳米抗体和普通蛋白结合剂都是 9 个里 6 个达到纳摩尔。3 条生物活性肽各测 6 个设计，2 条达到纳摩尔。灰色柱是训练集里已经有已知复合物的靶点，5 个靶点里 4 个得到结合剂；作者写明，这里的成功可能只是重组见过的界面，证据弱于新靶点。每个靶点的实验样本量小，9 个新靶点里仍有 3 个没有纳摩尔结合剂。

Stark, H. et al. *bioRxiv* (2025). https://doi.org/10.1101/2025.11.20.689494

RFdiffusion3 把计算分数和湿实验放在同一张图里。右图才是实验：DNA 结合测试 5 个设计，1 个结合，EC50 = 5.89 ± 2.15 μM；半胱氨酸水解酶测试 190 个，35 个多次周转，最高 *k*<sub>cat</sub>/*K*<sub>m</sub> = 3557。催化所用的 Cys-His-Asp 几何来自天然酶 Ulp1，由人指定。

![RFdiffusion3 的计算成功簇与湿实验成功数](figures/rfdiffusion3.png)

Butcher, J. et al. *bioRxiv* (2025). https://doi.org/10.1101/2025.09.18.676967

## 另一个折叠模型的置信度

上图左栏的及格线来自 AlphaFold 3：链间最小 pAE ≤ 1.5，结合蛋白 pTM ≥ 0.8，RMSD < 2.5 Å。五个靶点各 400 个骨架，按 TM-score 0.6 聚类后，平均独特成功簇 8.2，RFdiffusion 为 1.4。不聚类时，五个靶点里四个超过 RFdiffusion。原子基序酶基准 41 例中 37 例超过 RFdiffusion2。这些数字说明生成结构更多样，且更符合 AlphaFold 3 的置信度。计算通过率明显高于右图的湿实验成功率。

Proteina-Complexa 的成功标准来自 AlphaFold 2-Multimer：pLDDT > 90，界面 pAE < 7，结合剂 RMSD < 1.5 Å。每个方法、每个靶点生成 200 个长度 40–250 的结合剂，成功者再聚类。

![Proteina-Complexa 的平均独特成功数](figures/proteina_complexa.png)

Complexa 自身序列的独特成功数 9.10，高于需要 ProteinMPNN 重设计的 RFdiffusion（4.68）和 APM（3.15）；再经 ProteinMPNN 为 14.4。小分子四个靶点（SAM、OQO、FAD、IAI）的独特成功数，RFdiffusion-AllAtom 为 2、3、5、8，Complexa 为 10、6、17、19。酶活性位点基准 41 项里 38 项超过 RFdiffusion2。训练用的 Teddymer 来自 AlphaFold 预测结构，评分又用 AlphaFold 2-Multimer，上升的是模型家族内部的一致性。论文没有给出亲和力或细胞实验。

Didi, K. et al. *arXiv*:2603.27950 (2026). https://arxiv.org/abs/2603.27950

相关和通过率说明模型会预测，湿实验说明设计能测到，折叠模型打分说明两套模型彼此一致。
