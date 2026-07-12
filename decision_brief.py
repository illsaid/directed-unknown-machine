#!/usr/bin/env python3
"""Shape one labeled decision-support scenario into a bounded decision brief."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LABELS = ("Decision", "Evidence", "Constraints", "Success")

REQUIREMENT_GROUPS = (
    (
        "Decision",
        (
            "Recommend one action.",
            "State how the supplied success or reversal rule governs that action.",
            "Separate known facts, assumptions, and unresolved gaps.",
            "Do not promote interpretations embedded in Evidence to facts.",
            "Compare conflicting interpretations only against supplied observations; leave unresolved conflict explicit and name the evidence that would distinguish it.",
        ),
    ),
    (
        "Gate judgments",
        (
            "Check each constraint separately against Success; for every constraint, state whether it is satisfied, violated, or unresolved and name the supplied evidence supporting that judgment.",
            "Do not collapse independent gates into one overall pass or fail, do not silently override either field, and state when any failed or unresolved gate prevents a supported recommendation.",
        ),
    ),
    (
        "Evidence provenance",
        (
            "Map each source to the measurements it actually supplies; when sources overlap on a measurement, disclose the overlap without counting it as support for a different measurement or as additional independent evidence beyond that shared measurement.",
            "When sources report different values for the same measurement, preserve each value and leave the disagreement explicit unless supplied evidence establishes which source applies.",
        ),
    ),
    (
        "Applicability and adjustment",
        (
            "Exclude a source as non-comparable only by preserving its value and naming supplied evidence of both the observed mismatch and why that mismatch changes applicability to the target decision population; an unsupported conclusion, an unsupplied observation, or a difference with no established relevance cannot justify exclusion.",
            "When using an adjusted or reweighted value, preserve the original value and name the adjusted value, supplied auditable method, target population, and every governing assumption with its supplied support; an opaque method cannot resolve a gate, and an auditable result remains conditional when a governing assumption lacks supplied support.",
        ),
    ),
    (
        "Sensitivity",
        (
            "Judge a supplied supported sensitivity range against the full decision boundary: if the range crosses the threshold, preserve the full range and state the conditional outcome on each side; if every value lies on one side, resolve the gate from the whole range. Never select a midpoint, best case, or other convenient point estimate, and do not mark a same-side range unresolved merely because it is a range.",
        ),
    ),
    (
        "Threshold semantics",
        (
            "When a supported range touches a threshold exactly, apply the supplied comparison wording: equality satisfies an inclusive boundary such as ‘at or below’ or ‘at least,’ and violates a strict boundary such as ‘below,’ ‘strictly below,’ ‘above,’ or ‘strictly above.’",
            "When a numeric threshold is supplied without explicit strict or inclusive comparison wording, equality cannot resolve the gate and must remain unresolved rather than inheriting an unstated convention.",
        ),
    ),
    (
        "Threshold conflict",
        (
            "When the same metric has conflicting threshold statements—whether the comparison wording or numeric value differs—preserve every supplied rule and leave the gate unresolved unless the contract supplies explicit precedence or reconciliation; do not choose by strictness, looseness, field order, or which value appears later.",
            "When precedence is supplied, identify the governing threshold, preserve every displaced threshold, and report the result under each rather than silently deleting or rewriting the non-governing rule.",
            "For threshold statements in different units or representations, preserve both statements. Reconcile them only when the contract explicitly supplies the conversion or equivalence; otherwise leave the gate unresolved. Never introduce an unsupplied conversion.",
        ),
    ),
)


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


def print_requirements() -> None:
    print("Brief requirements:")
    for group, requirements in REQUIREMENT_GROUPS:
        print(f"{group}:")
        for requirement in requirements:
            print(f"- {requirement}")


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
    print_requirements()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
