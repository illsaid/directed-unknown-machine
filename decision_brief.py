#!/usr/bin/env python3
"""Shape one labeled decision-support scenario into a bounded decision brief."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LABELS = ("Decision", "Evidence", "Constraints", "Success")

REQUIREMENT_GROUPS = (
    (
        "Evidence: preserve",
        (
            "Preserve the supplied evidence record: map each source only to the measurements and values it supplies; disclose overlap without double-counting or measurement spill; retain conflicting values unless supplied applicability evidence resolves which source applies; and keep observations, interpretations, assumptions, and unresolved gaps distinct. Compare interpretations only with supplied observations, never promote interpretations or assumptions to fact, leave unsupported conflicts explicit, and name the evidence that would distinguish them.",
        ),
    ),
    (
        "Evidence: transform",
        (
            "Transform preserved evidence only with support for the exact operation. Exclude a source only when supplied evidence shows an observed mismatch and why it changes applicability to the target population. Adjust a value only when supplied evidence provides the adjusted value, an auditable method, the target population, and support for every governing assumption. Preserve original values; do not let exclusion support authorize adjustment or adjustment support authorize exclusion. Unsupported exclusion is invalid, opaque adjustment cannot resolve a gate, and an auditable adjustment remains conditional while any governing assumption is unsupported.",
        ),
    ),
    (
        "Boundary: reconcile",
        (
            "Reconcile conflicting boundaries only with support for the exact operation. For same-metric rules, supplied precedence may select one governing rule only while preserving displaced rules and reporting each result. For cross-unit or cross-representation statements, require a supplied conversion or equivalence. Otherwise leave the gate unresolved. Do not choose by strictness, looseness, field order, or recency, introduce an unsupplied conversion, or let precedence support authorize equivalence or equivalence support authorize precedence.",
        ),
    ),
    (
        "Boundary: apply",
        (
            "Apply preserved evidence to the governing boundary exactly as written. For ranges, evaluate the whole supplied range: mark threshold-crossing ranges conditional and resolve same-side ranges from the whole range; never choose a midpoint, best case, or convenient point, or leave a same-side range unresolved merely because it is a range. For equality, use only supplied comparison wording: equality satisfies inclusive boundaries such as ‘at or below’ and ‘at least,’ violates strict boundaries such as ‘below’ and ‘above,’ and remains unresolved when a numeric threshold lacks an explicit comparator rather than inheriting a convention.",
        ),
    ),
    (
        "Decision: judge gates",
        (
            "Judge each constraint independently against Success. For every gate, report satisfied, violated, or unresolved; cite the supplied evidence; and state its effect on the recommendation. Do not replace gate-level results with an overall verdict: each violated or unresolved gate retains its blocking effect under the supplied rule.",
        ),
    ),
    (
        "Decision: recommend",
        (
            "Recommend one authorized action and name the governing Success branch.",
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
    return f"Missing explicit fields:\n{fields}"


def unsupported_template(unsupported: list[str]) -> str:
    fields = "\n".join(f"- {label}" for label in unsupported)
    allowed = ", ".join(LABELS)
    return (
        f"Unsupported explicit fields:\n{fields}\n"
        f"Allowed: {allowed}.\n"
        "Place each extra meaning under its matching field."
    )


def print_requirements() -> None:
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
        raise SystemExit(unsupported_template(unsupported))
    values = {label: labeled_value(raw, label) for label in LABELS}
    missing = [label for label, value in values.items() if not value]
    if missing:
        raise SystemExit(repair_template(missing))
    print(f"Contract: complete — {len(LABELS)}/{len(LABELS)} fields explicit; nothing inferred.")
    print(f"Decision: {values['Decision']}")
    print(f"Evidence supplied: {values['Evidence']}")
    print(f"Constraints: {values['Constraints']}")
    print(f"Success: {values['Success']}")
    print_requirements()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
