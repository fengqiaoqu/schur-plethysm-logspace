# References

This repository links to third-party full texts; it does not redistribute those papers. Bibliographic entries are also available in [references.bib](references.bib).

## Hesse–Allender–Barrington (2002)

William Hesse, Eric Allender, and David A. Mix Barrington. **Uniform constant-depth threshold circuits for division and iterated multiplication.** *Journal of Computer and System Sciences* **65**(4), 695–716 (2002).

- DOI: [10.1016/S0022-0000(02)00025-9](https://doi.org/10.1016/S0022-0000(02)00025-9).
- [Author-hosted PDF](https://people.cs.rutgers.edu/~allender/papers/division.pdf).
- Locations in that author-hosted PDF: Section 2 defines binary input and output and output-bit predicates; Sections 2.2–2.3 specify DLOGTIME uniformity and FOM. Corollary 6.3 on PDF page 16 places Division and Imult in FOM, equivalently DLOGTIME-uniform TC⁰. Corollary 6.5 on the same page includes polynomial division and iterated polynomial multiplication.
- The present argument uses the integer arithmetic result and polynomial-size virtual inputs. It does not treat this arithmetic theorem as a new contribution.

## Hesse–Allender–Barrington (2014), corrigendum

William Hesse, Eric Allender, and David A. Mix Barrington. **Corrigendum to “Uniform constant-depth threshold circuits for division and iterated multiplication” [J. Comput. System Sci. 65 (4) (2002) 695–716].** *Journal of Computer and System Sciences* **80**(2), 496–497 (2014).

- DOI: [10.1016/j.jcss.2013.09.002](https://doi.org/10.1016/j.jcss.2013.09.002).
- [Author-hosted corrigendum PDF](https://people.cs.rutgers.edu/~allender/papers/hab.corrigendum.pdf).
- The author manuscript has three PDF pages. Its second page explicitly retracts parts 1 and 3 of Corollary 6.6 and retains part 2. Those retractions concern bounded arithmetic and proof-theoretic consequences. The corrigendum does not retract Corollary 6.3, which is used here.
- [Author bibliography linking both papers](https://people.cs.rutgers.edu/~allender/publications/complete_list.html).

## Gutiérrez–Ikenmeyer–Panova (2026), fixed v1

Álvaro Gutiérrez, Christian Ikenmeyer, and Greta Panova. **Counting in logarithmic space.** arXiv:2607.15881v1, submitted 17 July 2026. Preprint.

- [Fixed v1 abstract page](https://arxiv.org/abs/2607.15881v1).
- [Fixed v1 PDF](https://arxiv.org/pdf/2607.15881v1).
- [Experimental v1 HTML](https://arxiv.org/html/2607.15881v1).
- Definition 2.3 and the discussion near equation (2.4) specify FL and its nonnegative-integer inclusion in #L.
- The principal Schur specialization hook-content formula and the adjacent-coefficient plethysm identity are used in Section 6.4. The identity is numbered (6.20) in the fixed PDF and (6.19) in the experimental HTML.

| Topic | Fixed v1 PDF | Experimental HTML |
|---|---|---|
| Hermite coefficients in #L | Question 6.4, PDF page 28 | Question 6.4 |
| Principal Schur specialization coefficients for unbounded partition length | Question 6.22, PDF page 36 | Question 6.21 |
| The specified GL₂ plethysm coefficients for unbounded outer-partition length | Question 6.29, PDF page 38 | Question 6.27 |

The numbering above refers to the retrieved fixed PDF, not an assumed match between PDF and HTML. These three answers are consequences of one principal-specialization FL theorem. Their appearance as questions in a preprint does not by itself establish novelty or global priority.

## Attribution and research status

The proof combines classical identities with the cited arithmetic theorem. It offers a complete affirmative proof draft for the stated unary-input questions; external peer review and global priority remain unconfirmed. See [the scope and priority statement](docs/scope-and-priority.zh-CN.md) and [status.json](status.json) for the precise claims and limits.
