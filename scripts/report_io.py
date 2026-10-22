"""Deterministic result writing without machine-specific metadata."""
from __future__ import annotations

import json
from pathlib import Path


def write_report(output: Path, report: dict) -> None:
    """Write UTF-8 JSON while protecting the package's frozen results."""
    frozen = Path(__file__).resolve().parent.parent / "results"
    destination = output.resolve()
    if destination == frozen or frozen in destination.parents:
        raise SystemExit("Output must be outside the frozen results directory.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
