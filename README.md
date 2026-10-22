# 主特化 Schur 系数与 GL₂ plethysm 的对数空间算法

[English](README.en.md) · [完整中文证明](docs/proof.zh-CN.md) · [英文短稿 PDF](paper/logspace_note.pdf) · [复现说明](results/README.md)

本仓库整理一份关于主特化 Schur 系数、两行 GL₂ plethysm 重数及 Hermite 系数的研究稿。核心结论是：**在下述一元输入模型中，这些函数可在确定性对数空间 FL 中计算。** 该结论回答 Gutiérrez–Ikenmeyer–Panova 的 [Counting in logarithmic space，arXiv:2607.15881v1](https://arxiv.org/pdf/2607.15881v1) 中三个明确提出的问题。

**研究状态：完整证明稿，内部数学复核及独立精确算例核验通过；尚未经外部同行确认，全球优先权未确认。** 三个问题来自同一主定理及其推论。一般 Kronecker 系数是否不属于 #P 的猜想仍未解决。详见[范围与优先权说明](docs/scope-and-priority.zh-CN.md)。

版本：0.1.0。整理日期：2026-10-22。维护账号：fengqiaoqu。

## 主结果

给定任意分拆 $\lambda$ 以及 $k,r\ge0$，各部分与参数采用一元编码，整数输出采用二进制编码。分拆的行数不受常数限制。则

$$
c_r(\lambda,k)=[q^r]s_\lambda(1,q,\ldots,q^k)
\in \mathrm{FL}_{\ge0}\subseteq\#\mathrm L.
$$

这里 FL 表示：只读输入、对数大小工作空间、只写输出的确定性计算；无需把整个输出整数存入工作带。

对 $\mu\vdash w$ 及 $0\le 2r\le wk$，两行 GL₂ plethysm 系数满足

$$
a_{\mu[(k)]}^{(wk-r,r)}
=c_r(\mu,k)-c_{r-1}(\mu,k),\qquad c_{-1}=0,
$$

因而也属于 $\mathrm{FL}_{\ge0}\subseteq\#\mathrm L$。取 $\mu=(n)$ 得到 Hermite 特例：

$$
g((nk-r,r),(n^k),(n^k))
=[q^r]\binom{n+k}{k}_q-[q^{r-1}]\binom{n+k}{k}_q.
$$

| 原论文固定 v1 PDF 问题 | 本稿结论 |
|---|---|
| Question 6.22：任意行数主特化 Schur 系数是否在 #L | 实际上在 FL |
| Question 6.29：无界外分拆行数的指定 GL₂ plethysm 系数是否可在多项式时间、log² 空间计数 | 实际上在 FL，因而在 #L |
| Question 6.4：Hermite 系数是否在 #L | 实际上在 FL |

实验性 HTML 的对应编号为 6.21、6.27、6.4；本文以固定 v1 PDF 为准。

另有一个编码扩展：保持 $\lambda,r$ 为一元输入时，允许 $k$ 采用二进制编码，因为提取不超过第 $r$ 次的系数前可以把 $k$ 截断为 $\min(k,r)$。这没有将所有参数改为二进制。

## 证明为什么成立

1. 用经典 hook-content 公式把单变量主特化写为乘积之商。
2. 选择二的幂基数 $B$，严格大于全部系数，保证代入整数的各位块之间没有进位。
3. 证明所用整数的二进制位长关于一元输入长度为多项式。
4. 引用 Hesse–Allender–Barrington 的均匀整数乘除定理，逐位计算整数商，再取相应位块。
5. 用相邻系数差得到 GL₂ plethysm 结论，并显式构造非负 FL 函数对应的 #L 计数机器。

经典算术定理和 hook-content 公式均为引用输入，本稿的重点是它们在所述编码与系数提取问题中的组合及规模分析。[中文证明](docs/proof.zh-CN.md)与[英文证明](docs/proof.en.md)列出所有步骤，包括退化情形、均匀性、空间合成及相邻差的合法性。

## 一条命令复现

需要 **Python 3.10 或更新版本**，仅使用标准库，无需安装依赖或联网：

~~~bash
python -B reproduce.py
~~~

输出写入未跟踪的 artifacts 目录，已发布结果保存在 results 中。程序用独立组合算法进行精确对照，并与冻结结果比较：

| 核验 | 覆盖 |
|---|---|
| 高斯二项式整数代入与矩形分拆 DP | 441 对矩形，44,541 个系数，22,441 个有效相邻差 |
| hook-content 整数代入与直接 SSYT 枚举 | 102 对有效形状/字母数，1,228 个系数 |
| 混合编码截断与二进制饱和读取 | 1,602 个参数实例，84 次读取检查 |

**Python 程序核对取值，不是对数空间乘除的实现。** 空间复杂度结论依据正文证明和所引用的算术定理；有限算例不替代一般证明。

## 文件导航

| 文件 | 内容 |
|---|---|
| [完整中文证明](docs/proof.zh-CN.md) | 定理、引理、边界与编码扩展 |
| [完整英文证明](docs/proof.en.md) | 独立阅读的英文论证 |
| [英文短稿](paper/logspace_note.pdf) / [LaTeX](paper/logspace_note.tex) | 可下载审阅的论文稿与源码 |
| [范围与优先权](docs/scope-and-priority.zh-CN.md) | 原问题、结论范围、查新边界与经典工具依赖 |
| [结果说明](results/README.md) | 独立核验方法及冻结结果 |
| [参考文献](references.md) / [BibTeX](references.bib) | 固定来源、算术定理与勘误 |
| [来源和 AI 使用说明](NOTICE.md) | AI 辅助、内部审查及责任边界 |
| [引用建议](CITATION.md) | 仓库引用方式 |

欢迎提出指向具体公式、参数范围、空间模拟或先行文献的反馈。仓库不是期刊接收或外部同行评审记录。
