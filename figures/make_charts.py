# -*- coding: utf-8 -*-
"""Charts from published numbers. Not reproductions of paper figures."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.labelcolor"] = "#222222"
plt.rcParams["xtick.color"] = "#222222"
plt.rcParams["ytick.color"] = "#222222"

OUT = Path(__file__).resolve().parent
C_BLUE = "#2F5D8C"
C_ORANGE = "#D4762C"
C_TEAL = "#2A7F6F"
C_GRAY = "#8A8F98"
C_RED = "#A33B3B"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


def alphagenome():
    labels = ["高置信 eQTL\n相关系数", "可变多聚腺苷酸化\n相关系数", "因果 eQTL\nauROC"]
    ag = [0.73, 0.894, 0.75]
    borzoi = [0.61, 0.790, 0.71]
    ag_txt = ["0.73", "0.894", "0.75"]
    bz_txt = ["0.61", "0.790", "0.71"]
    x = np.arange(len(labels))
    w = 0.36
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    b1 = ax.bar(x - w / 2, ag, w, label="AlphaGenome", color=C_BLUE)
    b2 = ax.bar(x + w / 2, borzoi, w, label="Borzoi", color=C_GRAY)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("分数")
    ax.set_title("AlphaGenome 与 Borzoi：三项可直接比较的变异效应指标")
    ax.legend(frameon=False)
    ax.axhline(1.0, color="#dddddd", lw=0.6)
    for bars, texts in ((b1, ag_txt), (b2, bz_txt)):
        for bar, text in zip(bars, texts):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02, text, ha="center", va="bottom", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.01,
        -0.02,
        "来源：Avsec 等, Nature 2026。因果 eQTL 的 AlphaGenome 分数为多模态分数经随机森林后的结果（模型自身 auROC 为 0.68）。",
        fontsize=8,
        color="#555555",
    )
    save(fig, "alphagenome.png")


def esmfold2():
    labels = ["抗体–抗原", "蛋白–蛋白"]
    single = [50, 70]
    af3 = [47, 73]
    msa = [53, 76]
    x = np.arange(len(labels))
    w = 0.25
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    bars = [
        ax.bar(x - w, single, w, label="ESMFold2，仅序列", color=C_TEAL),
        ax.bar(x, af3, w, label="AlphaFold 3，带 MSA", color=C_GRAY),
        ax.bar(x + w, msa, w, label="ESMFold2，带 MSA", color=C_BLUE),
    ]
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 100)
    ax.set_ylabel("DockQ ≥ 0.23 通过率（%）")
    ax.set_title("ESMFold2 结构预测：复合物通过率")
    ax.legend(frameon=False, fontsize=9)
    for group in bars:
        for bar in group:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 1.5, f"{h:.0f}", ha="center", va="bottom", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.01,
        -0.02,
        "来源：Candido 等, bioRxiv 2026。误差约为 ±1–2 个百分点，图中取论文中心值。蛋白–配体仅报告了单序列结果（66%），未放入对照。",
        fontsize=8,
        color="#555555",
    )
    save(fig, "esmfold2.png")


def rfdiffusion3():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.2))

    ax = axes[0]
    names = ["独特成功簇\n（每靶点平均）"]
    x = np.arange(len(names))
    w = 0.32
    b1 = ax.bar(x - w / 2, [1.4], w, label="RFdiffusion", color=C_GRAY)
    b2 = ax.bar(x + w / 2, [8.2], w, label="RFdiffusion3", color=C_ORANGE)
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.set_ylim(0, 11)
    ax.set_ylabel("簇数")
    ax.set_title("计算：五个靶点的界面多样性")
    ax.legend(frameon=False, fontsize=8)
    for bars in (b1, b2):
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 0.25, f"{h:.1f}", ha="center", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax = axes[1]
    labels = ["DNA 结合\n5 个设计", "半胱氨酸水解酶\n190 个设计"]
    hit = [1, 35]
    miss = [4, 155]
    ax.bar(labels, hit, color=C_TEAL, label="实验成功")
    ax.bar(labels, miss, bottom=hit, color="#E6E8EB", label="未达成功标准")
    ax.set_ylim(0, 250)
    ax.set_ylabel("设计数量")
    ax.set_title("湿实验：成功数 / 测试数")
    ax.legend(frameon=False, fontsize=8)
    ax.text(0, hit[0] + miss[0] + 6, "1/5", ha="center", color="#222222", fontsize=10)
    ax.text(1, hit[1] + miss[1] + 6, "35/190", ha="center", color="#222222", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.suptitle("RFdiffusion3：计算多样性与湿实验成功率", y=1.02)
    fig.text(
        0.01,
        -0.04,
        "来源：Butcher 等, bioRxiv 2025。左图成功标准是 AlphaFold 3 置信度，不是湿实验。右图 DNA 成功为 EC50 = 5.89 μM；酶成功为多次周转。",
        fontsize=8,
        color="#555555",
    )
    save(fig, "rfdiffusion3.png")


def boltzgen():
    labels = ["新靶点\n纳米抗体", "新靶点\n蛋白结合剂", "新靶点\n生物活性肽\n（纳摩尔）", "已知复合物靶点\n蛋白结合剂"]
    rates = [6 / 9 * 100, 6 / 9 * 100, 2 / 3 * 100, 4 / 5 * 100]
    colors = [C_BLUE, C_BLUE, C_TEAL, C_GRAY]
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    bars = ax.bar(labels, rates, color=colors, width=0.62)
    ax.set_ylim(0, 110)
    ax.set_ylabel("得到纳摩尔或指定结合的靶点比例（%）")
    ax.set_title("BoltzGen 湿实验：按靶点计的成功率")
    notes = ["6/9", "6/9", "2/3", "4/5"]
    for bar, note in zip(bars, notes):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, note, ha="center", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.01,
        -0.06,
        "来源：Stark 等, bioRxiv 2025。新靶点与 PDB 中任何结合态蛋白的序列一致度 ≤30%，每个靶点最多测 15 个设计。灰色柱的靶点在训练集中已有已知复合物，作者认为证据较弱。",
        fontsize=8,
        color="#555555",
    )
    save(fig, "boltzgen.png")


def complexa():
    labels = ["RFdiffusion\n+ MPNN", "APM\n自身序列", "APM\n+ MPNN", "Complexa\n自身序列", "Complexa\n+ MPNN"]
    vals = [4.68, 0.31, 3.15, 9.10, 14.4]
    colors = [C_GRAY, C_GRAY, C_GRAY, C_BLUE, C_TEAL]
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    bars = ax.bar(labels, vals, color=colors, width=0.64)
    ax.set_ylabel("平均独特成功数")
    ax.set_ylim(0, 18)
    ax.set_title("Proteina-Complexa：蛋白靶点的计算独特成功数")
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.35, f"{v:.2f}", ha="center", fontsize=9)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.text(
        0.01,
        -0.04,
        "来源：Didi 等, arXiv:2603.27950，表 2。成功由 AlphaFold2-Multimer 定义（pLDDT>90，界面 pAE<7，RMSD<1.5 Å），不是湿实验。每个靶点生成 200 个结合剂后聚类。",
        fontsize=8,
        color="#555555",
    )
    save(fig, "proteina_complexa.png")


if __name__ == "__main__":
    alphagenome()
    esmfold2()
    rfdiffusion3()
    boltzgen()
    complexa()
    print("ok")
