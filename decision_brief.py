#!/usr/bin/env python3
"""Shape one labeled decision-support scenario into a bounded decision brief."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LABELS = ("Decision", "Evidence", "Constraints", "Success")


def scenario_input(text: str) -> str:
    match = re.search(r"^## Input\s*$\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise SystemExit("scenario is missing an Input section")
    return match.group(1).strip().strip('"')


def labeled_value(raw: str, label: str) -> str | None:
    next_labels = "|".join(LABELS)
    match = re.search(
        rf"(?:^|\n){label}:\s*(.*?)(?=\n(?:{next_labels}):|\Z)",
        raw,
        re.IGNORECASE | re.DOTALL,
    )
    return " ".join(match.group(1).split()) if match else None


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python decision_brief.py SCENARIOS/005-decision-support.md")
    path = Path(sys.argv[1])
    raw = scenario_input(path.read_text(encoding="utf-8"))
    values = {label: labeled_value(raw, label) for label in LABELS}
    missing = [label for label, value in values.items() if not value]
    if missing:
        required = ", ".join(f"{label}:" for label in missing)
        raise SystemExit(
            "cannot preserve the decision contract from unlabeled prose; "
            f"add these explicit fields: {required}"
        )
    print("Bounded decision brief task")
    print(f"Decision: {values['Decision']}")
    print(f"Evidence required: {values['Evidence']}")
    print(f"Constraints to preserve: {values['Constraints']}")
    print(f"Success condition: {values['Success']}")
    print("Deliverable: a one-page brief that recommends one action and separates known facts, assumptions, and unresolved gaps.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())