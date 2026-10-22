# Principal Schur specialization and GL2 plethysm in logarithmic space

Maintainer: [fengqiaoqu](https://github.com/fengqiaoqu). Draft dated 22 October 2026.

## Abstract

For an arbitrary partition $\lambda$ and unary integers $k,r\geq0$, the coefficient $[q^r]s_\lambda(1,q,\ldots,q^k)$ is computable by a deterministic logarithmic-space transducer, with its answer written in binary. Consequently, these coefficients, two-row GL2 plethysm coefficients with an arbitrary outer partition, and Hermite coefficients belong to $\mathrm{FL}_{\geq0}\subseteq\#\mathrm L$. The argument combines carry-free integer substitution, the principal-specialization hook-content formula, and the uniform small-space consequences of the Hesse-Allender-Barrington integer-arithmetic theorem. It also permits binary encoding of $k$ when $\lambda$ and $r$ remain unary. This provides affirmative answers to Questions 6.4, 6.22, and 6.29 in the fixed v1 PDF of *Counting in logarithmic space*. The contribution is an application of classical tools; external peer review and priority assessment remain outstanding.

## 1. Conventions and exact statements

Let $\lambda=(\lambda_1\geq\cdots\geq\lambda_\ell>0)$ be a partition, with size $w=|\lambda|$; the empty partition is permitted. Put

$$
S_{\lambda,k}(q)=s_\lambda(1,q,\ldots,q^k)
=\sum_{t\geq0}c_t(\lambda,k)q^t.
$$

The partition parts and the nonnegative integers $k,r$ are initially encoded in unary, with fixed separators. Write $L$ for the total input length. Outputs are binary integers with no leading zeros, except for the output `0`. An invalid encoding is assigned value zero. There is no fixed bound on $\ell(\lambda)$.

A function is in FL if a deterministic transducer computes its binary output using a read-only input tape, $O(\log L)$ work space, and a write-only output tape. All transducers below run in polynomial time and have polynomial output length. The notation $\mathrm{FL}_{\geq0}$ restricts attention to nonnegative integer-valued functions. The class $\#\mathrm L$ counts accepting paths of polynomial-time nondeterministic logarithmic-space machines.

**Theorem 1 (principal specialization).** The function

$$
(\lambda,k,r)\longmapsto c_r(\lambda,k)
$$

belongs to $\mathrm{FL}_{\geq0}\subseteq\#\mathrm L$.

For a partition $\mu\vdash w$, use the Schur expansion

$$
s_\mu[s_{(k)}]=\sum_{\nu\vdash wk}a_{\mu[(k)]}^{\nu}s_\nu.
$$

**Theorem 2 (two-row plethysm).** With unary input and $0\leq2r\leq wk$,

$$
(\mu,k,r)\longmapsto a_{\mu[(k)]}^{(wk-r,r)}
$$

belongs to $\mathrm{FL}_{\geq0}\subseteq\#\mathrm L$, without a bound on $\ell(\mu)$. Define its value as zero outside the specified range.

**Theorem 3 (mixed encoding).** The conclusions of Theorems 1 and 2 remain true when $k$ is encoded in binary and the partition and $r$ remain unary. For Theorem 2 the target shape is specified implicitly by $(\mu,k,r)$.

## 2. Arithmetic and composition

We use [Hesse, Allender, and Barrington (2002), Corollary 6.3](https://people.cs.rutgers.edu/~allender/papers/division.pdf): integer division and iterated multiplication are computable in DLOGTIME-uniform TC0. The number of factors and the total length of the explicitly represented binary inputs may be polynomial. In particular these operations have deterministic logarithmic-space bit algorithms.

For completeness, a uniform constant-depth threshold circuit of polynomial size can be evaluated at one output gate in logarithmic space. A depth-first recursive evaluation stores a constant number of gate indices. At a threshold gate, evaluate its incoming gates one at a time and maintain a polynomially bounded counter. The uniformity algorithm generates gate types and wiring from their indices. The circuit depth is constant, so the stored indices and counters use $O(\log m)$ space on an arithmetic input of length $m$, and the recomputation takes polynomial time. Repeating this for each output position gives a transducer.

The [2014 corrigendum](https://people.cs.rutgers.edu/~allender/papers/hab.corrigendum.pdf) retracts parts 1 and 3 of Corollary 6.6, concerning bounded arithmetic. The integer-arithmetic theorem used here is not among the retracted statements. We use neither those statements nor the polynomial-arithmetic corollary of the 2002 paper.

**Lemma 4 (virtual-input composition).** A constant number of logarithmic-space transducers with polynomially bounded intermediate lengths can be composed in logarithmic space and polynomial time.

*Proof.* To simulate $F(G(x))$, keep the virtual input-head position of $F$. Whenever $F$ requests the $j$-th bit of $G(x)$, rerun $G$ with an output-position counter until that bit is reached. The position is polynomially bounded, hence needs only $O(\log L)$ bits. The configurations of the simulated machine and the bit-generating machine use additive space. Their runtimes and the number of recomputations are polynomial. A fixed number of such layers preserves both bounds. No intermediate output is stored in full. $\square$

**Lemma 5 (carry-free substitution).** If

$$
P(q)=\sum_{t=0}^d u_tq^t,\qquad 0\leq u_t<2^W,
$$

and $B=2^W$, then

$$
u_r=\left\lfloor\frac{P(B)}{2^{Wr}}\right\rfloor\bmod 2^W.
\tag{1}
$$

*Proof.* The expression $\sum_tu_tB^t$ is already the base-$B$ expansion of $P(B)$, because every digit is strictly smaller than $B$. Equation (1) extracts its $r$-th digit. In binary this is the block of width $W$ beginning at bit $Wr$, numbering the least significant bit by zero. If these positions and the bit length are polynomially bounded and the bit function of $P(B)$ is in logarithmic space, scan the block to find its highest nonzero bit and then output from that position downwards. This uses counters, not a stored block. Output zero if every bit is zero. $\square$

## 3. Proof of Theorem 1

### 3.1 Boundary cases and a coefficient bound

Input validation, size, length, and the unary parameters can all be computed by repeated scans with logarithmic-space counters. If $w=0$, then $S_{\lambda,k}=1$. If $\ell(\lambda)>k+1$, then $S_{\lambda,k}=0$. If $r>wk$, its coefficient is zero. These cases can be answered directly.

Assume henceforth $w>0$, set $K=k+1$, and suppose $\ell(\lambda)\leq K$ and $r\leq wk$. Define

$$
W=1+w\lceil\log_2K\rceil,\qquad B=2^W,
\qquad b(\lambda)=\sum_i(i-1)\lambda_i.
\tag{2}
$$

By the semistandard Young tableau definition of a Schur polynomial, $c_t\geq0$. Evaluating at $q=1$ counts semistandard tableaux with entries in $\{1,\ldots,K\}$, so

$$
\sum_t c_t(\lambda,k)=s_\lambda(1^K)\leq K^w
\leq2^{w\lceil\log_2K\rceil}<B.
\tag{3}
$$

The bound counts all assignments to the $w$ boxes and therefore does not depend on a length restriction. For $K=1$ it gives $W=1$ and remains valid. Lemma 5 applies to every coefficient.

### 3.2 Exact integer evaluation

For a box $u=(i,j)\in[\lambda]$, put

$$
a_u=K+j-i,\qquad
h_u=\lambda_i-j+\lambda'_j-i+1.
$$

The principal-specialization hook-content formula, also used in [Gutiérrez, Ikenmeyer, and Panova, §6](https://arxiv.org/pdf/2607.15881v1), gives

$$
S_{\lambda,k}(q)
=q^{b(\lambda)}\frac{\prod_{u\in[\lambda]}(1-q^{a_u})}
{\prod_{u\in[\lambda]}(1-q^{h_u})}.
$$

Since $\ell(\lambda)\leq K$, every exponent is positive, with

$$
1\leq a_u\leq K+w,\qquad 1\leq h_u\leq w.
\tag{4}
$$

Substitute $q=B>1$ and cancel the signs of the $w$ numerator and $w$ denominator factors:

$$
S_{\lambda,k}(B)=
\frac{B^{b(\lambda)}\prod_u(B^{a_u}-1)}
{\prod_u(B^{h_u}-1)}.
\tag{5}
$$

The denominator is strictly positive. The quotient is an exact integer because its value is an integer-coefficient polynomial evaluated at an integer. We therefore need integer multiplication and division only.

### 3.3 Polynomial bit lengths

Unary encoding implies $w,k,r=O(L)$. Also $b(\lambda)\leq w^2$ and $W=O((L+1)^2)$, a deliberately coarse bound. The numerator in (5) has bit length at most

$$
1+W\left(b(\lambda)+\sum_u a_u\right)
\leq1+W\bigl(w^2+w(K+w)\bigr)
=O((L+1)^4).
\tag{6}
$$

The denominator has bit length at most $1+Ww^2$; the quotient is no longer than the numerator. Each factor is similarly polynomial in length. Thus the arithmetic instances have polynomial *binary length*, although their values can be exponentially large.

### 3.4 Logarithmic-space generation and extraction

Store a box coordinate $(i,j)$ and scan the input to obtain $\lambda_i$. The number of parts at least $j$ is $\lambda'_j$, found by another scan. The quantities in (2) and (4), together with the necessary lengths and offsets, are polynomially bounded integers. A constant number of $O(\log L)$-bit counters suffices to compute them; there is no need to store the partition.

A factor $B^e-1=2^{We}-1$ consists of $We$ binary ones. The factor $B^{b(\lambda)}$ is a one followed by $Wb(\lambda)$ zeros. Consequently, the two factor lists in (5), with fixed-width padding and separators as required by an arithmetic input encoding, are virtual strings of polynomial length whose individual bits are computable in logarithmic space.

Apply iterated multiplication to each list, and then integer division to the products. Lemma 4 gives the bit function of $S_{\lambda,k}(B)$ in logarithmic space. These are a constant number of arithmetic/composition layers; the number of boxes is the number of factors in one iterated-multiplication instance, not the number of composition layers. Finally, equations (1) and (3) extract $c_r(\lambda,k)$ by scanning the appropriate block. This proves the FL claim.

### 3.5 An explicit counting machine

To establish the counting claim, use $0\leq c_r<2^W$. A nondeterministic machine guesses exactly $W$ bits, from most significant to least significant, representing an integer $y\in\{0,\ldots,2^W-1\}$. It maintains only a position counter and the three-way comparison state of the prefixes of $y$ and $c_r$. At each position it deterministically recomputes the corresponding bit of $c_r$, using the bit algorithm just proved and padding with zeros. Accept if and only if $y<c_r$.

Each integer $y$ has exactly one length-$W$ representation, so this machine has exactly $c_r$ accepting paths. Its work space is $O(\log L)$, and its time is polynomial on every path. Each guessed bit is consumed once; previous nondeterministic choices are never guessed again to reconstruct a witness. The direct boundary cases admit the same construction, or machines with zero or one accepting path as appropriate. This completes Theorem 1. $\square$

## 4. Two-row plethysm and Hermite coefficients

Since $s_{(k)}(1,q)=1+q+\cdots+q^k$, evaluation of the plethysm alphabet gives

$$
s_\mu[s_{(k)}](1,q)=s_\mu(1,q,\ldots,q^k).
$$

Schur polynomials of length greater than two vanish in these two variables. For $0\leq2t\leq wk$,

$$
s_{(wk-t,t)}(1,q)=q^t+q^{t+1}+\cdots+q^{wk-t}.
$$

Thus, on $0\leq2r\leq wk$, coefficient comparison yields

$$
c_r(\mu,k)=\sum_{t=0}^r a_{\mu[(k)]}^{(wk-t,t)},
\qquad
a_{\mu[(k)]}^{(wk-r,r)}=c_r(\mu,k)-c_{r-1}(\mu,k),
\tag{7}
$$

where $c_{-1}=0$. The two coefficients on the right are in FL by Theorem 1. Binary subtraction is computable in logarithmic space: to output a particular bit, recompute the borrow by scanning the less significant positions, keeping a single borrow bit. Apply Lemma 4 to the coefficient bit functions. The difference is nonnegative because it is a representation multiplicity, and it is at most $c_r<2^W$. The fixed-length comparison machine in §3.5 therefore puts the difference in $\#\mathrm L$. This proves Theorem 2 without asserting that $\#\mathrm L$ is closed under subtraction. $\square$

For $\mu=(n)$, let $p_r(n\times k)$ count partitions of $r$ contained in an $n$-by-$k$ rectangle. Then

$$
s_{(n)}(1,q,\ldots,q^k)={n+k\brack k}_q
=\sum_r p_r(n\times k)q^r.
$$

The Hermite identity, recorded in equations (6.1)-(6.2) of the fixed v1 PDF, gives

$$
a_{(n)[(k)]}^{(nk-r,r)}
=g\bigl((nk-r,r),(n^k),(n^k)\bigr)
=p_r(n\times k)-p_{r-1}(n\times k).
\tag{8}
$$

Here $(n^k)$ has $k$ parts equal to $n$. Equation (8) is used in the valid range $0\leq2r\leq nk$; zero/empty cases are interpreted through the corresponding constant Schur polynomial. These Hermite coefficients belong to $\mathrm{FL}_{\geq0}\subseteq\#\mathrm L$.

A separate elementary size bound is available in this special case. Take $W=n+k+1$, since $\sum_rp_r(n\times k)=\binom{n+k}{k}<2^W$. For $k>0$,

$$
{n+k\brack k}_{2^W}
=\frac{\prod_{i=1}^k(2^{W(n+i)}-1)}
{\prod_{i=1}^k(2^{Wi}-1)}.
$$

The numerator and denominator have at most $Wk(2n+k+1)/2$ and $Wk(k+1)/2$ bits respectively. They have polynomial length for unary input. When $k=0$, both products are empty and the value is one.

## 5. Binary encoding of the alphabet bound

For any $t\leq r$, the tableau expansion gives

$$
[q^t]s_\lambda(1,q,\ldots,q^k)
=[q^t]s_\lambda(1,q,\ldots,q^{\min(k,r)}).
\tag{9}
$$

Indeed, a tableau using a letter of weight $q^j$ with $j>r$ already has total degree greater than $r$, since all other weights have nonnegative degree. Tableaux using only the retained letters satisfy exactly the same row and column conditions. This is a bijective restriction, including cases where the truncated alphabet is too short for the shape.

Read binary $k$ with a saturated counter, updating $z\leftarrow\min(r,2z+b)$ for the next bit $b$. It computes $\min(k,r)$ in logarithmic space, even if the numerical value of $k$ is enormous. The truncated parameter is at most the unary value $r$, and its virtual unary encoding has polynomial length. Theorem 1 and Lemma 4 now compute the coefficient. The same truncation preserves both coefficients in (7).

For the validity condition in Theorem 2, if $w>0$, compute $\widehat k=\min(k,2r+1)$. Then $2r\leq wk$ if and only if $2r\leq w\widehat k$. The latter multiplication involves polynomially bounded integers. If $w=0$, validity requires $r=0$. Thus the implicitly specified target partition can be checked without storing a large binary product. This proves Theorem 3. It does not allow every parameter to be encoded in binary. $\square$

## 6. Relation to the published questions and scope

The reference is the [fixed arXiv v1 PDF of *Counting in logarithmic space*](https://arxiv.org/pdf/2607.15881v1), dated 17 July 2026. Its experimental HTML rendering has different numbering.

| Fixed v1 PDF | PDF page | HTML label | Consequence here |
| --- | --- | --- | --- |
| Question 6.4 | 28 | 6.4 | Hermite coefficients belong to FL and #L. |
| Question 6.22 | 36 | 6.21 | Principal Schur specialization coefficients belong to FL and #L for arbitrary partition length. |
| Question 6.29 | 38 | 6.27 | The stated two-row GL2 plethysm coefficients belong to FL and #L for arbitrary outer-partition length. |

For the last question, $\#\mathrm L\subseteq\#\mathrm{TISP}(\operatorname{poly}(L),\log^2L)$, so the conclusion implies the requested inclusion. The three answers derive from one principal-specialization theorem. They are not three independent methods or a solution to a general Kronecker problem.

The proof relies on a single-variable polynomial whose degree and exact integer-evaluation length are polynomially bounded. It does not establish an analogous algorithm for general Littlewood-Richardson coefficients or general Kronecker coefficients. In particular, it does not resolve whether general Kronecker coefficients lie in #P or separate them from #P.

## 7. Verification and research status

The accompanying Python checks compare exact integer substitution with independently computed tableau and rectangle-partition values. They check the identities and small examples. They do **not** implement the logarithmic-space multiplication or division transducers, and their memory use is not evidence for the space theorem. The space bound follows from the mathematical proof and the cited arithmetic theorem.

This draft received internal AI-assisted mathematical review and finite exact checks. It has not received external peer review or author confirmation. It is not a Lean formalization. No global priority claim is made; a literature search is not proof of novelty. The central observation applies classical formulas and integer-arithmetic results to the stated coefficient functions.

## References

1. Álvaro Gutiérrez, Christian Ikenmeyer, and Greta Panova. *Counting in logarithmic space*. arXiv:2607.15881v1, 17 July 2026. [Fixed v1 PDF](https://arxiv.org/pdf/2607.15881v1); [v1 HTML](https://arxiv.org/html/2607.15881v1).
2. William Hesse, Eric Allender, and David A. Mix Barrington. *Uniform constant-depth threshold circuits for division and iterated multiplication*. Journal of Computer and System Sciences 65(4), 695-716, 2002. [Author PDF](https://people.cs.rutgers.edu/~allender/papers/division.pdf).
3. William Hesse, Eric Allender, and David A. Mix Barrington. *Corrigendum for Uniform Constant-Depth Threshold Circuits for Division and Iterated Multiplication*. Journal of Computer and System Sciences 80, 496-497, 2014. [Author PDF](https://people.cs.rutgers.edu/~allender/papers/hab.corrigendum.pdf).
