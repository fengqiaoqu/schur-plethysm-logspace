# Principal Schur specialization and GL2 plethysm in logarithmic space

[中文](README.md) · [Complete proof](docs/proof.en.md) · [Research note PDF](paper/logspace_note.pdf) · [Reproduction](results/README.md)

This research draft proves deterministic logarithmic-space computation of the coefficients of principal Schur specializations, with no constant bound on the number of partition rows. Adjacent coefficient differences give the corresponding two-row GL2 plethysm multiplicities and Hermite coefficients.

**Status:** a complete proof draft checked internally and supported by independent exact computations. External peer review and global priority have not been established. The three questions below are consequences of one main theorem. The general conjecture that Kronecker computation lies outside #P remains unresolved.

Version 0.1.0 · 22 October 2026 · Maintained by fengqiaoqu.

## Result and encoding

For a partition $\lambda$ and $k,r\ge0$, encode every partition part and both parameters in unary, and output integers in binary. Then

$$
[q^r]s_\lambda(1,q,\ldots,q^k)
\in\mathrm{FL}_{\ge0}\subseteq\#\mathrm L.
$$

There is no constant restriction on $\ell(\lambda)$. FL uses a read-only input tape, logarithmic work space and a write-only output tape; polynomially many output bits need not be stored on the work tape.

For $\mu\vdash w$ and $0\le2r\le wk$, the identity

$$
a_{\mu[(k)]}^{(wk-r,r)}
=[q^r]s_\mu(1,q,\ldots,q^k)-[q^{r-1}]s_\mu(1,q,\ldots,q^k)
$$

places these two-row GL2 plethysm coefficients in the same class. The case $\mu=(n)$ gives the Hermite coefficients

$$
g((nk-r,r),(n^k),(n^k)).
$$

These results answer Questions **6.22, 6.29 and 6.4**, respectively, of the [fixed v1 PDF of Gutiérrez, Ikenmeyer and Panova](https://arxiv.org/pdf/2607.15881v1). The experimental HTML numbers the first two questions 6.21 and 6.27.

An additional cutoff observation permits binary $k$ while the partition and $r$ remain unary: coefficients through degree $r$ are unchanged by replacing $k$ with $\min(k,r)$. This does not permit all parameters to be binary.

## Method

The classical hook-content formula gives an exact product quotient. Substitute a sufficiently large power of two so that polynomial coefficients occupy separate binary blocks without carries. All arithmetic operands have polynomial bit length. Apply uniform integer multiplication and division from Hesse--Allender--Barrington, compose the bit computations in logarithmic space, and extract the desired block.

The main arithmetic theorem and specialization formula are established tools, not new results of this repository. The proof checks their application, size bounds and encoding conditions. See the [complete proof](docs/proof.en.md), [PDF](paper/logspace_note.pdf), and [scope and priority statement](docs/scope-and-priority.zh-CN.md).

## Reproduce

Python 3.10 or newer; standard library only; no network or model service:

~~~bash
python -B reproduce.py
~~~

The runner writes local outputs to the ignored artifacts directory and compares them with frozen results. It checks 44,541 Gaussian coefficients and 22,441 valid adjacent differences, 1,228 Schur-specialization coefficients against direct tableau enumeration, and 1,602 cutoff cases plus 84 capped binary-input checks.

**The Python programs validate exact values; they do not implement logarithmic-space integer arithmetic.** The complexity bound rests on the mathematical proof and the cited arithmetic theorem.

## Materials and status

- [English proof](docs/proof.en.md), [Chinese proof](docs/proof.zh-CN.md)
- [PDF](paper/logspace_note.pdf) and [LaTeX source](paper/logspace_note.tex)
- [Result snapshots and methods](results/README.md)
- [References](references.md), [BibTeX](references.bib), [citation](CITATION.md)
- [AI assistance, provenance and rights notice](NOTICE.md)

No claim of a general Kronecker algorithm, a #P separation, external endorsement or global first discovery is made. Concrete corrections and prior-literature pointers are welcome.
