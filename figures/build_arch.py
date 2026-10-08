# -*- coding: utf-8 -*-
from pathlib import Path

OUT = Path(__file__).resolve().parent

SVGS = {}

SVGS["alphagenome_arch.svg"] = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 520" width="1040" height="520" role="img">
  <title>AlphaGenome 架构</title>
  <desc>1 Mb DNA 经序列并行进入 U-Net，再分成一维功能轨道和二维染色质接触图。</desc>
  <defs>
    <marker id="ag-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="#334155"/>
    </marker>
  </defs>
  <rect width="1040" height="520" fill="#ffffff"/>
  <text x="28" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="20" font-weight="700" fill="#1e293b">AlphaGenome 架构</text>
  <text x="250" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#64748b">序列到功能 · U-Net · 人和小鼠</text>
  <rect x="372" y="58" width="640" height="148" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="388" y="80" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" font-weight="700" fill="#64748b">U-Net 骨干</text>
  <rect x="24" y="78" width="150" height="108" rx="10" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="99" y="114" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">输入</text>
  <text x="99" y="138" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">1 Mb DNA</text>
  <text x="99" y="158" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">物种：人 / 鼠</text>
  <line x1="174" y1="132" x2="206" y2="132" stroke="#334155" stroke-width="1.6" marker-end="url(#ag-arrow)"/>
  <rect x="210" y="78" width="146" height="108" rx="10" fill="#e8f1fb" stroke="#2F5D8C"/>
  <text x="283" y="114" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">序列并行</text>
  <text x="283" y="138" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">切成 131 kb</text>
  <text x="283" y="158" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">8 路同时计算</text>
  <line x1="356" y1="132" x2="388" y2="132" stroke="#334155" stroke-width="1.6" marker-end="url(#ag-arrow)"/>
  <rect x="392" y="92" width="180" height="96" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="482" y="124" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">编码器</text>
  <text x="482" y="148" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">下采样 · 卷积</text>
  <text x="482" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">局部 motif</text>
  <line x1="572" y1="140" x2="604" y2="140" stroke="#334155" stroke-width="1.6" marker-end="url(#ag-arrow)"/>
  <rect x="608" y="92" width="190" height="96" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="703" y="124" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">Transformer</text>
  <text x="703" y="148" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">跨设备通信</text>
  <text x="703" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">增强子–启动子</text>
  <line x1="798" y1="140" x2="830" y2="140" stroke="#334155" stroke-width="1.6" marker-end="url(#ag-arrow)"/>
  <rect x="834" y="92" width="160" height="96" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="914" y="128" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">解码器</text>
  <text x="914" y="152" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">上采样</text>
  <line x1="860" y1="188" x2="700" y2="236" stroke="#334155" stroke-width="1.6" marker-end="url(#ag-arrow)"/>
  <line x1="968" y1="188" x2="932" y2="236" stroke="#334155" stroke-width="1.6" marker-end="url(#ag-arrow)"/>
  <rect x="500" y="240" width="340" height="118" rx="10" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="670" y="268" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">一维表示 → 功能轨道</text>
  <text x="670" y="292" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">分辨率 1 bp 与 128 bp</text>
  <text x="670" y="314" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">表达、剪接、可及性</text>
  <text x="670" y="336" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">组蛋白、转录因子</text>
  <rect x="860" y="240" width="156" height="118" rx="10" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="938" y="276" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">二维表示</text>
  <text x="938" y="300" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">2,048 bp</text>
  <text x="938" y="322" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">染色质接触图</text>
  <rect x="24" y="392" width="992" height="96" rx="10" fill="#fff7ed" stroke="#D4762C"/>
  <text x="44" y="424" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#9a3412">变异效应</text>
  <text x="44" y="450" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#7c2d12">没有单独的变异输出头。同一段序列分别输入参考等位基因和替代等位基因，各预测一次，再取差值。</text>
  <text x="44" y="472" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#7c2d12">人 5,930 条轨道，小鼠 1,128 条，共 11 类输出。</text>
</svg>
"""

SVGS["esmfold2_arch.svg"] = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 560" width="1040" height="560" role="img">
  <title>ESMFold2 架构</title>
  <desc>冻结的 ESMC 掩码语言模型提供各层表征，汇聚后经配对编码器、48 层循环折叠和扩散模块得到全原子坐标。</desc>
  <defs>
    <marker id="esm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="#334155"/>
    </marker>
  </defs>
  <rect width="1040" height="560" fill="#ffffff"/>
  <text x="28" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="20" font-weight="700" fill="#1e293b">ESMFold2 架构</text>
  <text x="230" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#64748b">冻结的蛋白语言模型 + 循环折叠 + 原子扩散</text>
  <rect x="20" y="56" width="1000" height="196" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="6 4"/>
  <text x="40" y="82" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#475569">ESMC · 60 亿参数 · 权重冻结</text>
  <text x="760" y="82" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#64748b">掩码语言建模</text>
  <rect x="40" y="104" width="160" height="112" rx="10" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="120" y="142" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">氨基酸序列</text>
  <text x="120" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">推理时完整输入</text>
  <text x="120" y="190" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">训练时随机遮盖</text>
  <line x1="200" y1="160" x2="236" y2="160" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="240" y="104" width="200" height="112" rx="10" fill="#e8f1fb" stroke="#2F5D8C"/>
  <text x="340" y="142" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">逐位点嵌入</text>
  <text x="340" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">60 亿档：2,560 维</text>
  <text x="340" y="190" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">每个残基一个向量</text>
  <line x1="440" y1="160" x2="476" y2="160" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="480" y="104" width="250" height="112" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="605" y="142" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">Transformer 层</text>
  <text x="605" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">自注意力与前馈交替</text>
  <text x="605" y="190" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">保留每一层激活</text>
  <line x1="730" y1="160" x2="766" y2="160" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="770" y="104" width="220" height="112" rx="10" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="880" y="142" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">掩码位点预测</text>
  <text x="880" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">输出氨基酸分布</text>
  <text x="880" y="190" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">折叠时不使用该头</text>
  <line x1="605" y1="252" x2="605" y2="292" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <text x="618" y="278" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">各层表征汇入折叠网络</text>
  <rect x="20" y="296" width="1000" height="236" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="40" y="324" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#475569">ESMFold2 · ESMC 保持冻结</text>
  <rect x="40" y="348" width="150" height="120" rx="10" fill="#e8f1fb" stroke="#2F5D8C"/>
  <text x="115" y="386" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">汇聚</text>
  <text x="115" y="410" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">所有层合成</text>
  <text x="115" y="432" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">一个表示</text>
  <line x1="190" y1="408" x2="222" y2="408" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="226" y="348" width="190" height="120" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="321" y="382" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">残基对表示</text>
  <text x="321" y="406" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">投影到二维</text>
  <text x="321" y="428" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">4 层编码器</text>
  <text x="321" y="450" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#64748b">可选 MSA</text>
  <line x1="416" y1="408" x2="448" y2="408" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="452" y="348" width="200" height="120" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="552" y="386" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">循环折叠</text>
  <text x="552" y="410" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">48 层，可反复迭代</text>
  <text x="552" y="432" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">Fast 版为 24 层</text>
  <line x1="652" y1="408" x2="684" y2="408" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="688" y="348" width="150" height="120" rx="10" fill="#fff7ed" stroke="#D4762C"/>
  <text x="763" y="386" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">扩散模块</text>
  <text x="763" y="410" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">滑动窗口</text>
  <text x="763" y="432" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">原子注意力</text>
  <line x1="838" y1="408" x2="870" y2="408" stroke="#334155" stroke-width="1.6" marker-end="url(#esm-arrow)"/>
  <rect x="874" y="348" width="122" height="120" rx="10" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="935" y="386" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">输出</text>
  <text x="935" y="410" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">全原子坐标</text>
  <text x="935" y="432" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">蛋白、核酸</text>
  <text x="935" y="452" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">和小分子</text>
</svg>
"""

SVGS["rfdiffusion3_arch.svg"] = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 560" width="1040" height="560" role="img">
  <title>RFdiffusion3 架构</title>
  <desc>原子级扩散 U-Net。条件经 2 层 Pairformer 进入，稀疏注意力只在近邻原子和残基之间传递。</desc>
  <defs>
    <marker id="rfd-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="#334155"/>
    </marker>
  </defs>
  <rect width="1040" height="560" fill="#ffffff"/>
  <text x="28" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="20" font-weight="700" fill="#1e293b">RFdiffusion3 架构</text>
  <text x="270" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#64748b">原子扩散 · 约 1.68 亿参数 · 无三角注意力</text>
  <rect x="24" y="64" width="250" height="468" rx="14" fill="#fff7ed" stroke="#D4762C"/>
  <text x="149" y="94" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#9a3412">条件</text>
  <text x="149" y="116" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#9a3412">设计时给定，可部分省略</text>
  <rect x="44" y="136" width="210" height="52" rx="8" fill="#ffffff" stroke="#fdba74"/>
  <text x="149" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#7c2d12">靶点或 motif 坐标</text>
  <rect x="44" y="200" width="210" height="52" rx="8" fill="#ffffff" stroke="#fdba74"/>
  <text x="149" y="232" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#7c2d12">氢键供体 / 受体</text>
  <rect x="44" y="264" width="210" height="52" rx="8" fill="#ffffff" stroke="#fdba74"/>
  <text x="149" y="296" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#7c2d12">溶剂可及性、相对质心</text>
  <rect x="44" y="328" width="210" height="64" rx="8" fill="#ffffff" stroke="#fdba74"/>
  <text x="149" y="354" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#7c2d12">核酸或小分子身份</text>
  <text x="149" y="376" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#9a3412">构象可与蛋白一起采样</text>
  <text x="149" y="430" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#9a3412">分类器无关引导</text>
  <text x="149" y="452" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#c2410c">加强或减弱这些条件</text>
  <line x1="274" y1="280" x2="318" y2="280" stroke="#334155" stroke-width="1.6" marker-end="url(#rfd-arrow)"/>
  <rect x="322" y="64" width="470" height="468" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="342" y="94" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#334155">扩散 U-Net · 多步去噪</text>
  <rect x="348" y="114" width="418" height="56" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="557" y="148" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#1e293b">初始：随机原子坐标</text>
  <line x1="557" y1="170" x2="557" y2="188" stroke="#334155" stroke-width="1.6" marker-end="url(#rfd-arrow)"/>
  <rect x="348" y="192" width="418" height="64" rx="8" fill="#fff7ed" stroke="#D4762C"/>
  <text x="557" y="218" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">Pairformer · 2 层</text>
  <text x="557" y="240" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">只编码条件。AlphaFold 3 这里是 48 层</text>
  <line x1="557" y1="256" x2="557" y2="278" stroke="#334155" stroke-width="1.6" marker-end="url(#rfd-arrow)"/>
  <rect x="348" y="282" width="130" height="96" rx="8" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="413" y="318" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">下采样</text>
  <text x="413" y="342" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">原子特征</text>
  <text x="413" y="360" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">加残基特征</text>
  <line x1="478" y1="330" x2="506" y2="330" stroke="#334155" stroke-width="1.6" marker-end="url(#rfd-arrow)"/>
  <rect x="510" y="282" width="140" height="96" rx="8" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="580" y="314" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">稀疏注意力</text>
  <text x="580" y="338" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">只连接几何上</text>
  <text x="580" y="356" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">接近的原子</text>
  <line x1="650" y1="330" x2="678" y2="330" stroke="#334155" stroke-width="1.6" marker-end="url(#rfd-arrow)"/>
  <rect x="682" y="282" width="84" height="96" rx="8" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="724" y="322" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">上采样</text>
  <text x="724" y="346" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#475569">坐标更新</text>
  <path d="M724 378 L724 408 L413 408 L413 378" fill="none" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4" marker-end="url(#rfd-arrow)"/>
  <text x="557" y="428" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="12" fill="#64748b">下一步噪声更小，重复直到收敛</text>
  <line x1="792" y1="280" x2="836" y2="280" stroke="#334155" stroke-width="1.6" marker-end="url(#rfd-arrow)"/>
  <rect x="840" y="64" width="176" height="468" rx="14" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="928" y="100" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#115e59">输出</text>
  <text x="928" y="148" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">全原子蛋白</text>
  <text x="928" y="180" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">每残基固定</text>
  <text x="928" y="202" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">4 个骨架原子</text>
  <text x="928" y="224" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">加 10 个侧链位</text>
  <text x="928" y="264" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">较短侧链的空位</text>
  <text x="928" y="286" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">是放在 Cβ 上的</text>
  <text x="928" y="308" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">虚拟原子</text>
  <text x="928" y="360" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#115e59">去噪结束后</text>
  <text x="928" y="382" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#115e59">按原子身份</text>
  <text x="928" y="404" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#115e59">读出氨基酸</text>
</svg>
"""

SVGS["boltzgen_arch.svg"] = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 540" width="1040" height="540" role="img">
  <title>BoltzGen 架构</title>
  <desc>沿用 Boltz-2。Trunk 只运行一次；扩散模块反复去噪。待设计残基的种类由虚拟侧链原子的几何编码。</desc>
  <defs>
    <marker id="bz-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="#334155"/>
    </marker>
  </defs>
  <rect width="1040" height="540" fill="#ffffff"/>
  <text x="28" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="20" font-weight="700" fill="#1e293b">BoltzGen 架构</text>
  <text x="230" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#64748b">Boltz-2 骨干 · Trunk 一次 · 扩散多次</text>
  <rect x="24" y="64" width="280" height="300" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="164" y="94" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#334155">输入</text>
  <rect x="44" y="112" width="240" height="100" rx="10" fill="#f1f5f9" stroke="#94a3b8"/>
  <text x="164" y="144" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">分子实体</text>
  <text x="164" y="168" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">蛋白、DNA、RNA、小分子</text>
  <text x="164" y="190" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">翻译后修饰、共价键</text>
  <rect x="44" y="228" width="240" height="108" rx="10" fill="#fff7ed" stroke="#D4762C"/>
  <text x="164" y="258" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#9a3412">设计说明</text>
  <text x="164" y="282" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#7c2d12">哪些残基待设计</text>
  <text x="164" y="304" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#7c2d12">结合位点、二级结构</text>
  <text x="164" y="324" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#7c2d12">结构模板</text>
  <line x1="304" y1="214" x2="352" y2="214" stroke="#334155" stroke-width="1.6" marker-end="url(#bz-arrow)"/>
  <rect x="356" y="64" width="300" height="300" rx="14" fill="#e8f1fb" stroke="#2F5D8C"/>
  <text x="506" y="98" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e3a8a">Trunk</text>
  <text x="506" y="122" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#1d4ed8">整次生成只运行一次</text>
  <rect x="380" y="148" width="252" height="80" rx="8" fill="#ffffff" stroke="#93c5fd"/>
  <text x="506" y="180" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">残基表示</text>
  <text x="506" y="204" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">每个 token 一个向量</text>
  <rect x="380" y="244" width="252" height="88" rx="8" fill="#ffffff" stroke="#93c5fd"/>
  <text x="506" y="278" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">残基对表示</text>
  <text x="506" y="302" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">两两关系，供扩散使用</text>
  <line x1="656" y1="214" x2="704" y2="214" stroke="#334155" stroke-width="1.6" marker-end="url(#bz-arrow)"/>
  <rect x="708" y="64" width="308" height="300" rx="14" fill="#fff7ed" stroke="#D4762C"/>
  <text x="862" y="98" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#9a3412">扩散模块</text>
  <text x="862" y="122" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#c2410c">同一模块反复去噪</text>
  <rect x="732" y="148" width="260" height="72" rx="8" fill="#ffffff" stroke="#fdba74"/>
  <text x="862" y="178" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">全部原子坐标</text>
  <text x="862" y="202" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">过程与 Boltz-2 相同</text>
  <rect x="732" y="236" width="260" height="96" rx="8" fill="#ffffff" stroke="#fdba74"/>
  <text x="862" y="266" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#1e293b">残基种类等于几何</text>
  <text x="862" y="290" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">侧链空位放虚拟原子</text>
  <text x="862" y="312" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">其位置编码氨基酸</text>
  <rect x="24" y="388" width="992" height="124" rx="14" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="44" y="422" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#115e59">一次前向同时给出两件事</text>
  <text x="44" y="452" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#134e4a">若靶点只提供序列，扩散过程一边折叠靶点，一边设计结合剂的残基身份和全原子结构。</text>
  <text x="44" y="480" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#134e4a">待设计残基、固定残基和结合位点写在同一次条件里，不分成先折叠、再设计两个网络。</text>
</svg>
"""

SVGS["proteina_complexa_arch.svg"] = r"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 580" width="1040" height="580" role="img">
  <title>Proteina-Complexa 架构</title>
  <desc>α 碳显式生成，序列和侧链放在每个残基的固定维潜变量里。靶点条件调制潜变量，推理时可用界面分数引导搜索。</desc>
  <defs>
    <marker id="pc-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0 L10 5 L0 10 Z" fill="#334155"/>
    </marker>
  </defs>
  <rect width="1040" height="580" fill="#ffffff"/>
  <text x="28" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="20" font-weight="700" fill="#1e293b">Proteina-Complexa 架构</text>
  <text x="330" y="36" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#64748b">La-Proteina 的部分潜变量表示 + 靶点条件</text>
  <rect x="24" y="58" width="992" height="168" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="44" y="86" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#475569">一条蛋白被拆成两种表示</text>
  <rect x="44" y="104" width="300" height="98" rx="10" fill="#e8f1fb" stroke="#2F5D8C"/>
  <text x="194" y="140" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">α 碳坐标 · 显式</text>
  <text x="194" y="166" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">直接生成骨架走向</text>
  <text x="194" y="186" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">不经过潜变量</text>
  <rect x="380" y="104" width="600" height="98" rx="10" fill="#dbeafe" stroke="#2F5D8C"/>
  <text x="680" y="136" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">序列 + 其余原子 → 变分自编码器</text>
  <text x="680" y="162" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">每个残基压成固定长度的潜变量</text>
  <text x="680" y="184" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">侧链长短不同，生成时维度不变</text>
  <line x1="194" y1="226" x2="194" y2="268" stroke="#334155" stroke-width="1.6" marker-end="url(#pc-arrow)"/>
  <line x1="680" y1="226" x2="520" y2="314" stroke="#334155" stroke-width="1.6" marker-end="url(#pc-arrow)"/>
  <rect x="24" y="278" width="992" height="168" rx="14" fill="#fff7ed" stroke="#D4762C"/>
  <text x="44" y="306" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" font-weight="700" fill="#9a3412">生成 · 流匹配</text>
  <rect x="44" y="322" width="200" height="96" rx="10" fill="#ffffff" stroke="#fdba74"/>
  <text x="144" y="358" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">靶点</text>
  <text x="144" y="382" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">条件加在潜变量上</text>
  <text x="144" y="402" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">自编码器不改</text>
  <line x1="244" y1="370" x2="286" y2="370" stroke="#334155" stroke-width="1.6" marker-end="url(#pc-arrow)"/>
  <rect x="290" y="322" width="430" height="96" rx="10" fill="#ffffff" stroke="#fdba74"/>
  <text x="505" y="354" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#1e293b">逐步去噪</text>
  <text x="505" y="378" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">同时更新 α 碳和每个残基的潜变量</text>
  <text x="505" y="400" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#475569">从噪声走到一条结合剂</text>
  <line x1="720" y1="370" x2="762" y2="370" stroke="#334155" stroke-width="1.6" marker-end="url(#pc-arrow)"/>
  <rect x="766" y="322" width="220" height="96" rx="10" fill="#e7f5f2" stroke="#2A7F6F"/>
  <text x="876" y="354" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#115e59">解码器</text>
  <text x="876" y="378" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#134e4a">潜变量还原为序列</text>
  <text x="876" y="398" text-anchor="middle" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="13" fill="#134e4a">并补全原子结构</text>
  <rect x="24" y="466" width="992" height="88" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-dasharray="6 4"/>
  <text x="44" y="500" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="15" font-weight="700" fill="#334155">推理时可选，不是另一套网络</text>
  <text x="44" y="528" font-family="Microsoft YaHei, PingFang SC, Noto Sans SC, sans-serif" font-size="14" fill="#475569">用结构预测器的界面分数，或氢键能量，对去噪中途的候选做束搜索，把生成拉向高分结合剂。</text>
</svg>
"""


def main():
    for name, text in SVGS.items():
        path = OUT / name
        path.write_text(text.strip() + "\n", encoding="utf-8")
        raw = path.read_bytes()
        raw.decode("utf-8")
        print(name, len(raw))


if __name__ == "__main__":
    main()
