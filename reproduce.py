#!/usr/bin/env python3
"""Run the offline finite checks and compare all results with frozen JSON.

Usage: python -B reproduce.py [--output-dir artifacts]
Only the Python standard library is required. These finite computations do not
verify the claimed space complexity and do not replace the mathematical proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


SUITES = (
    "gaussian_substitution",
    "schur_specialization",
    "mixed_truncation",
)


def canonical_hash(report: dict) -> str:
    normalized = json.dumps(report, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(normalized).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or newer is required.")
    if not __debug__:
        parser.error("Run without -O or -OO: assertions are part of the verification.")

    package = Path(__file__).resolve().parent
    output_dir = (args.output_dir or package / "artifacts").resolve()
    frozen = package / "results"
    if output_dir == frozen or frozen in output_dir.parents:
        parser.error("--output-dir must be outside the frozen results directory.")
    output_dir.mkdir(parents=True, exist_ok=True)

    verified = []
    for suite in SUITES:
        filename = f"{suite}_verification.json"
        generated = output_dir / filename
        process = subprocess.run(
            [sys.executable, "-B", str(package / "scripts" / f"verify_{suite}.py"),
             "--output", str(generated)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        if process.returncode:
            # Avoid copying local paths from Python tracebacks into public reports.
            print(f"FAIL: {suite}; verifier exited with code {process.returncode}.", file=sys.stderr)
            return 1
        actual = json.loads(generated.read_text(encoding="utf-8"))
        expected = json.loads((frozen / filename).read_text(encoding="utf-8"))
        if actual != expected:
            print(f"FAIL: {suite}; generated JSON differs from frozen results.", file=sys.stderr)
            return 1
        verified.append({"suite": suite, "status": "matched_frozen_results",
                         "canonical_sha256": canonical_hash(actual)})
        if suite == "gaussian_substitution":
            print(f"PASS: Gaussian: {actual['rectangle_pairs']} rectangles; "
                  f"{actual['coefficient_checks']} coefficients; "
                  f"{actual['nonnegative_difference_checks']} differences.")
        elif suite == "schur_specialization":
            print(f"PASS: Schur: {actual['shape_dimension_pairs']} shape-dimension pairs; "
                  f"{actual['coefficient_checks']} coefficients.")
        else:
            print(f"PASS: Mixed encoding: {actual['shape_k_r_cases']} truncation cases; "
                  f"{actual['saturation_checks']} saturated-reader checks.")

    summary = {
        "status": "all_finite_checks_passed_and_frozen_results_matched",
        "suites": verified,
        "limitation": "Finite exact checks support the identities; they do not prove a space bound.",
    }
    (output_dir / "reproduction_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print("PASS: All three generated JSON files match the frozen mathematical results.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
