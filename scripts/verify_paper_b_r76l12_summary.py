#!/usr/bin/env python3
"""Validate Paper B R76L12 public-safe bibliography class totals.

Checks arithmetic only; does not confirm access to primary sources,
study eligibility, a completed systematic review or any causal outcome.
"""
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "PaperB_R76L12_SourceRole_Summary.csv"
EXPECTED = {
    "Official / public administrative evidence": 34,
    "Observed / empirical research": 25,
    "Legal / doctrinal": 16,
    "Standard / methods": 9,
    "Review / methodology": 6,
    "Other scholarship / sector evidence": 3,
}
TOTAL = 93


def main() -> None:
    with DATA.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    found = {}
    for row in rows:
        role = row["source_role"]
        assert role not in found, f"Duplicate source role: {role}"
        count = int(row["count"])
        found[role] = count
        percent = Decimal(count * 100) / Decimal(TOTAL)
        displayed = percent.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        assert displayed == Decimal(row["percentage_rounded_1dp"]), (
            role, str(displayed), row["percentage_rounded_1dp"]
        )
    assert found == EXPECTED, f"Unexpected source roles/counts: {found}"
    assert sum(found.values()) == TOTAL
    print("PASS: 6 source roles, 93 cited identities, 1-decimal shares checked.")
    print("LIMIT: Counts describe a curated bibliography; no review eligibility verified.")


if __name__ == "__main__":
    main()
