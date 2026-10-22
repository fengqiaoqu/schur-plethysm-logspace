#!/usr/bin/env python3
"""Compare carry-free hook-content evaluation with direct SSYT enumeration.

This is optional finite supporting evidence, not a proof of a space bound.
Only Python's standard library is required.
"""
from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
import json
from pathlib import Path

from report_io import write_report


@cache
def partitions(n: int, maximum: int | None = None) -> tuple:
    if n == 0:
        return ((),)
    maximum = n if maximum is None else min(maximum, n)
    return tuple((first,) + tail for first in range(maximum, 0, -1) for tail in partitions(n - first, first))


def enumerate_ssyt(shape: tuple, d: int) -> tuple:
    """Row weak, column strict entries 1..d; weight is sum(entry-1)."""
    cells = [(i, j) for i, width in enumerate(shape) for j in range(width)]
    entries = {}
    counts = Counter()

    def visit(index: int, weight: int) -> None:
        if index == len(cells):
            counts[weight] += 1
            return
        i, j = cells[index]
        minimum = max(entries.get((i, j - 1), 1), entries.get((i - 1, j), 0) + 1)
        for entry in range(minimum, d + 1):
            entries[i, j] = entry
            visit(index + 1, weight + entry - 1)
        entries.pop((i, j), None)

    visit(0, 0)
    return tuple(counts[weight] for weight in range((d - 1) * sum(shape) + 1))


def verify() -> dict:
    rows = []
    for size in range(7):
        for shape in partitions(size):
            for d in range(1, 6):
                if len(shape) > d:
                    continue
                # d**size bounds the number of all fillings, including non-SSYT.
                block_bits = size * d.bit_length() + 1
                base = 1 << block_bits
                numerator = denominator = 1
                for i, width in enumerate(shape):
                    for j in range(width):
                        height = sum(row_width > j for row_width in shape)
                        hook = width - j + height - i - 1
                        numerator *= (1 << (block_bits * (d + j - i))) - 1
                        denominator *= (1 << (block_bits * hook)) - 1
                quotient, remainder = divmod(numerator, denominator)
                assert remainder == 0
                shift = sum(i * width for i, width in enumerate(shape))
                evaluated = quotient << (block_bits * shift)
                coefficients = enumerate_ssyt(shape, d)
                assert sum(coefficients) <= d ** size < base
                recovered = tuple((evaluated >> (block_bits * weight)) & (base - 1) for weight in range(len(coefficients)))
                assert recovered == coefficients, (shape, d, recovered, coefficients)
                assert evaluated >> (block_bits * len(coefficients)) == 0
                rows.append({
                    'shape': shape, 'd': d, 'size': size,
                    'all_coefficients_from_SSYT_enumeration': coefficients,
                })
    report = {
        'status': 'all_exact_checks_passed',
        'scope': {'size': [0, 6], 'd': [1, 5], 'length_at_most_d': True},
        'identity': 's_lambda(1,q,...,q^(d-1)) = q^b(lambda) product_(i,j in lambda)(1-q^(d+j-i))/(1-q^h(i,j)), with one-based (i,j)',
        'base_bound': 'B=2^(|lambda|*bit_length(d)+1) > d^|lambda| >= total number of SSYT',
        'shape_dimension_pairs': len(rows),
        'coefficient_checks': sum(len(row['all_coefficients_from_SSYT_enumeration']) for row in rows),
        'exact_divisibility_checks': len(rows),
        'limitations': 'Finite exact comparisons with direct SSYT enumeration; no logspace or counting-class conclusion is inferred from the computation.',
        'all_results': rows,
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parent.parent / 'artifacts' / 'schur_specialization_verification.json')
    args = parser.parse_args()
    report = verify()
    write_report(args.output, report)
    print(json.dumps({key: value for key, value in report.items() if key != 'all_results'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
