"""Finite checks of the mixed-encoding cutoff; complexity rests on the proof."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from report_io import write_report

from verify_schur_specialization import enumerate_ssyt, partitions


def capped_binary(bits: str, ceiling: int) -> int:
    assert bits and all(bit in "01" for bit in bits)
    value = 0
    for bit in bits:
        value = min(ceiling, 2 * value + int(bit))
    return value


def verify() -> dict:
    cache = {}

    def coeffs(shape, k):
        key = (shape, k)
        if key not in cache:
            cache[key] = enumerate_ssyt(shape, k + 1)
        return cache[key]

    count = 0
    for n in range(6):
        for shape in partitions(n):
            for k in range(9):
                actual = coeffs(shape, k)
                for r in range(min(n * k, 12) + 1):
                    cutoff = capped_binary(bin(k)[2:], r)
                    assert cutoff == min(k, r)
                    shorter = coeffs(shape, cutoff)
                    for t in (r, r - 1):
                        if t < 0:
                            continue
                        a = actual[t] if t < len(actual) else 0
                        b = shorter[t] if t < len(shorter) else 0
                        assert a == b, (shape, k, r, t, a, b)
                    count += 1
    saturation_checks = 0
    for bits in ("0", "1", "10", "1" + "0" * 4096):
        for r in range(21):
            expected = min(int(bits[:32], 2), r) if len(bits) <= 32 else r
            assert capped_binary(bits, r) == expected
            saturation_checks += 1
    report = {
        "status": "passed",
        "claim": "For 0<=t<=r, specialization coefficients are unchanged by k -> min(k,r).",
        "shape_size_maximum": 5,
        "k_maximum": 8,
        "r_maximum": 12,
        "shape_k_r_cases": count,
        "saturation_checks": saturation_checks,
        "binary_k_length_tested_maximum": 4097,
        "oracle": "direct semistandard Young-tableau enumeration",
        "limitation": "Finite identity and capped-input checks; not an implementation or proof of a logspace bound.",
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).resolve().parent.parent / 'artifacts' / 'mixed_truncation_verification.json')
    args = parser.parse_args()
    report = verify()
    write_report(args.output, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
