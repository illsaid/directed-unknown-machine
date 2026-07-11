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


def unsupported_labels(raw: str) -> list[str]:
    explicit = re.findall(r"^([A-Za-z][A-Za-z ]*):", raw, re.MULTILINE)
    return [label for label in explicit if label.lower() not in {item.lower() for item in LABELS}]


def labeled_value(raw: str, label: str) -> str | None:
    next_labels = "|".join(LABELS)
    match = re.search(
        rf"(?:^|\n){label}:\s*(.*?)(?=\n(?:{next_labels}):|\Z)",
        raw,
        re.IGNORECASE | re.DOTALL,
    )
    return " ".join(match.group(1).split()) if match else None


def repair_template(missing: list[str]) -> str:
    fields = "\n".join(f"{label}:" for label in missing)
    return (
        "cannot preserve the decision contract from unlabeled prose; "
        "add these explicit fields without rewriting the notes:\n"
        f"{fields}"
    )


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python decision_brief.py SCENARIOS/005-decision-support.md")
    path = Path(sys.argv[1])
    raw = scenario_input(path.read_text(encoding="utf-8"))
    unsupported = unsupported_labels(raw)
    if unsupported:
        names = ", ".join(unsupported)
        supported = ", ".join(LABELS)
        raise SystemExit(
            f"unsupported explicit field(s): {names}. Preserve each meaning under the supported field that matches its role: {supported}."
        )
    values = {label: labeled_value(raw, label) for label in LABELS}
    missing = [label for label, value in values.items() if not value]
    if missing:
        raise SystemExit(repair_template(missing))
    print("Bounded decision brief task")
    print(f"Contract check: complete — {len(LABELS)}/{len(LABELS)} explicit fields; no content inferred.")
    print(f"Decision: {values['Decision']}")
    print(f"Evidence supplied: {values['Evidence']}")
    print(f"Constraints: {values['Constraints']}")
    print(f"Success: {values['Success']}")
    print("Brief requirements:")
    print("- Recommend one action.")
    print("- State how the supplied success or reversal rule governs that action.")
    print("- Separate known facts, assumptions, and unresolved gaps.")
    print("- Do not promote interpretations embedded in Evidence to facts.")
    print("- Compare conflicting interpretations only against supplied observations; leave unresolved conflict explicit and name the evidence that would distinguish it.")
    print("- Check each constraint separately against Success; for every constraint, state whether it is satisfied, violated, or unresolved and name the supplied evidence supporting that judgment; identify shared sources and the measurements each source actually supplies; when different sources overlap on the same measurement, disclose the overlap without counting it as support for a different measurement or as additional independent evidence beyond that shared measurement; when sources report different values for the same measurement, preserve each value and leave the disagreement explicit unless supplied evidence establishes which source applies; if excluding a source as non-comparable, name the supplied comparability reason and the excluded value; do not collapse independent gates into one overall pass or fail, do not silently override either field, and state when any failed or unresolved gate prevents a supported recommendation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
