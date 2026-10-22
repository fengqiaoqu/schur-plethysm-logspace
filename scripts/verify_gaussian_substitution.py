#!/usr/bin/env python3
"""Exact checks of carry-free Gaussian-polynomial evaluation at a large base.

The integer-product quotient is compared with an independent combinatorial
recurrence for partitions in a rectangle.  All integer arithmetic is exact.
This finite computation does not prove a logspace or #L complexity claim.
"""

from __future__ import annotations

import argparse
from functools import cache
import json
from math import comb
from pathlib import Path

from report_io import write_report


@cache
def rectangle_partition_dp(n: int, k: int) -> tuple[int, ...]:
    """Count partitions of each weight with largest part <=n and <=k parts.

    A partition either has no part n, or loses one such part and then fits
    into the n by (k-1) rectangle.  This uses no rational product identity.
    """
    if n == 0 or k == 0:
        return (1,)
    without_n = rectangle_partition_dp(n - 1, k)
    remove_one_n = rectangle_partition_dp(n, k - 1)
    result = [0] * (n * k + 1)
    for weight, count in enumerate(without_n):
        result[weight] += count
    for weight, count in enumerate(remove_one_n):
        result[weight + n] += count
    return tuple(result)


def quotient_at_large_base(n: int, k: int) -> dict:
    block_bits = n + k + 1
    base = 1 << block_bits
    numerator = denominator = 1
    for i in range(1, k + 1):
        numerator *= (1 << (block_bits * (n + i))) - 1
        denominator *= (1 << (block_bits * i)) - 1
    quotient, remainder = divmod(numerator, denominator)
    assert remainder == 0, (n, k, 'nonintegral evaluated quotient')
    # Empty products equal one, so their bit-length bound is recorded as one.
    numerator_bit_bound = max(1, block_bits * k * (2 * n + k + 1) // 2)
    denominator_bit_bound = max(1, block_bits * k * (k + 1) // 2)
    quotient_bit_bound = block_bits * (n * k + 1)
    assert numerator.bit_length() <= numerator_bit_bound
    assert denominator.bit_length() <= denominator_bit_bound
    assert quotient.bit_length() <= quotient_bit_bound
    return {
        'n': n, 'k': k, 'block_bits': block_bits, 'base': base,
        'quotient': quotient,
        'numerator_bits': numerator.bit_length(),
        'denominator_bits': denominator.bit_length(),
        'quotient_bits': quotient.bit_length(),
        'numerator_bit_bound': numerator_bit_bound,
        'denominator_bit_bound': denominator_bit_bound,
        'quotient_bit_bound': quotient_bit_bound,
    }


def verify(max_dimension: int) -> dict:
    rows = []
    coefficient_checks = difference_checks = 0
    for n in range(max_dimension + 1):
        for k in range(max_dimension + 1):
            row = quotient_at_large_base(n, k)
            coefficients = rectangle_partition_dp(n, k)
            coefficient_sum_bound = comb(n + k, k)
            assert sum(coefficients) == coefficient_sum_bound
            assert coefficients == rectangle_partition_dp(k, n)
            assert coefficient_sum_bound < row['base']
            assert all(0 <= count <= coefficient_sum_bound < row['base'] for count in coefficients)
            evaluated = row.pop('quotient')
            mask = row['base'] - 1
            recovered = []
            leftover = evaluated
            for _ in range(n * k + 1):
                recovered.append(leftover & mask)
                leftover >>= row['block_bits']
            assert leftover == 0
            assert tuple(recovered) == coefficients, (n, k, recovered, coefficients)
            assert coefficients[0] == coefficients[-1] == 1
            assert coefficients == coefficients[::-1]
            # Leading coefficient 1 and no carries give this sharper exact value.
            assert evaluated.bit_length() == row['block_bits'] * n * k + 1
            coefficient_checks += len(coefficients)
            differences = []
            for r in range(n * k // 2 + 1):
                digit = (evaluated >> (row['block_bits'] * r)) & mask
                previous_digit = 0 if r == 0 else (evaluated >> (row['block_bits'] * (r - 1))) & mask
                difference = digit - previous_digit
                dp_difference = coefficients[r] - (0 if r == 0 else coefficients[r - 1])
                assert difference == dp_difference >= 0, (n, k, r, difference, dp_difference)
                differences.append(difference)
                difference_checks += 1
            row.update({
                'degree': n * k,
                'coefficient_sum': sum(coefficients),
                'binomial_coefficient_sum_bound': coefficient_sum_bound,
                'maximum_coefficient': max(coefficients),
                'r_range_checked': [0, n * k // 2],
                'all_coefficients_from_independent_DP': coefficients,
                'differences_through_middle': differences,
            })
            rows.append(row)
    return {
        'status': 'all_exact_checks_passed',
        'scope': {'n': [0, max_dimension], 'k': [0, max_dimension], 'all_coefficients': True, 'all_differences_through_floor_nk_over_2': True},
        'rectangle_pairs': len(rows), 'exact_divisibility_checks': len(rows),
        'coefficient_checks': coefficient_checks,
        'nonnegative_difference_checks': difference_checks,
        'coefficient_sum_and_base_bound_checks': len(rows),
        'dimension_swap_symmetry_checks': len(rows),
        'palindromicity_checks': len(rows),
        'bit_bound_checks': 3 * len(rows),
        'exact_quotient_bit_length_checks': len(rows),
        'all_results': [{
            'n': row['n'], 'k': row['k'],
            'coefficients': row['all_coefficients_from_independent_DP'],
            'differences_through_middle': row['differences_through_middle'],
        } for row in rows],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-dimension', type=int, default=20)
    parser.add_argument('--output', type=Path, default=Path(__file__).resolve().parent.parent / 'artifacts' / 'gaussian_substitution_verification.json')
    args = parser.parse_args()
    if not 0 <= args.max_dimension <= 50:
        parser.error('this bounded verification supports 0 <= --max-dimension <= 50')
    report = verify(args.max_dimension)
    write_report(args.output, report)
    print(json.dumps({key: value for key, value in report.items() if key != 'all_results'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
