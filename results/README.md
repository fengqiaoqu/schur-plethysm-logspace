# Frozen finite evidence

These UTF-8 JSON files contain the deterministic mathematical results of the
finite checks. They omit elapsed time, Python executable paths, invocation
paths, and other machine-specific metadata. They were prepared from the
existing exact-check outputs, with redundant explanatory and bit-length fields
removed; the published scripts recompute the same identities and assertions.

| File | Independent comparison | Checked range and actual count |
| --- | --- | --- |
| `gaussian_substitution_verification.json` | Exact evaluated Gaussian product quotient versus the partition-in-a-rectangle recurrence | `0 <= n,k <= 20`: 441 rectangles, 44,541 coefficients and 22,441 differences through `floor(n*k/2)` |
| `schur_specialization_verification.json` | Exact hook-content product quotient versus direct semistandard Young-tableau enumeration | `0 <= |lambda| <= 6`, `1 <= d <= 5`, `length(lambda) <= d`: 102 shape-dimension pairs and 1,228 coefficients |
| `mixed_truncation_verification.json` | Direct tableau counts before and after `k -> min(k,r)`, plus a capped binary-input reader | `|lambda| <= 5`, `0 <= k <= 8`, `0 <= r <= min(|lambda|*k,12)`: 1,602 triples; 84 reader checks, including a 4,097-bit input |

For each mixed-encoding triple, the numerical comparison checks weights `r`
and `r-1` when the latter is nonnegative. The general identity stated in that
file is the claim supported by the mathematical proof, not an assertion that
all parameter values or all weights were exhaustively tested.

From the repository root, run:

```sh
python -B reproduce.py
```

Only Python 3.10 or newer and its standard library are needed. No network,
external packages, credentials, or external services are used. The default
output is the repository's `artifacts/` directory; select another output
directory with `python -B reproduce.py --output-dir DIRECTORY`. The verifier
compares the complete parsed JSON values with these frozen files and exits
nonzero on any failed assertion or mismatch. It never regenerates this
directory. Each script also accepts `--output FILE` and rejects destinations
inside `results/`.

The runner refuses optimized Python (`-O` or `-OO`) because the original
exact-check algorithms use assertions. Gaussian-only experiments can change
the finite range using `python -B scripts/verify_gaussian_substitution.py
--max-dimension N --output FILE` for `0 <= N <= 50`; only `N=20` is compared
by the standard reproduction command.

These computations validate finite algebraic identities and input truncation
behavior. They do not implement a logspace machine, prove a complexity-class
inclusion, establish novelty, or solve general Kronecker-coefficient questions.
