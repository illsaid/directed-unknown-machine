#!/usr/bin/env python3
"""Shape one labeled decision-support scenario into a bounded decision brief."""

from __future__ import annotations

import re
import sys
from pathlib import Path

LABELS = ("Decision", "Evidence", "Constraints", "Success")

REQUIREMENT_GROUPS = (
    (
        "Governed recommendation",
        (
            "Recommend one action and state how the supplied success or reversal rule governs it.",
            "Preserve supplied observations, interpretations, assumptions, and unresolved gaps as distinct statuses; compare conflicting interpretations only against supplied observations, never promote an interpretation or assumption to fact, leave unsupported conflict explicit, and name the evidence that would distinguish it.",
        ),
    ),
    (
        "Gate judgments",
        (
            "Judge every constraint separately against Success: state whether each gate is satisfied, violated, or unresolved; name the supplied evidence for that status; preserve independent gates rather than collapsing them into one overall verdict; and state when any violated or unresolved gate blocks a supported recommendation.",
        ),
    ),
    (
        "Evidence provenance",
        (
            "Map every source to the measurements and values it actually supplies; disclose overlapping coverage without counting it as support for a different measurement or as additional independent evidence, and when sources disagree on the same measurement, preserve every value and leave the conflict explicit unless supplied evidence establishes which source applies.",
        ),
    ),
    (
        "Evidence transformation",
        (
            "For any source-exclusion or value-adjustment step, preserve every original value and require supplied support for the specific transformation used: exclusion requires both an observed mismatch and why it changes applicability to the target decision population, while adjustment requires the adjusted value, an auditable method, the target population, and every governing assumption with its supplied support. Evidence sufficient for one transformation cannot substitute for the other; unsupported exclusion is invalid, opaque adjustment cannot resolve a gate, and an auditable adjustment remains conditional when a governing assumption lacks support.",
        ),
    ),
    (
        "Boundary evaluation",
        (
            "Judge a supplied supported sensitivity range against the full decision boundary: if the range crosses the threshold, preserve the full range and state the conditional outcome on each side; if every value lies on one side, resolve the gate from the whole range. Never select a midpoint, best case, or other convenient point estimate, and do not mark a same-side range unresolved merely because it is a range.",
            "Resolve equality only from comparison wording supplied by the contract: equality satisfies an inclusive boundary such as ‘at or below’ or ‘at least,’ violates a strict boundary such as ‘below,’ ‘strictly below,’ ‘above,’ or ‘strictly above,’ and remains unresolved when a numeric threshold has no explicit strict or inclusive wording rather than inheriting an unstated convention.",
        ),
    ),
    (
        "Boundary reconciliation",
        (
            "Preserve every conflicting threshold statement and leave the gate unresolved unless the contract supplies support for the exact reconciliation used: precedence may select a governing same-metric rule only while preserving displaced rules and reporting each result; cross-unit or cross-representation statements may be reconciled only by a supplied conversion or equivalence. Do not choose by strictness, looseness, field order, or recency, introduce an unsupplied conversion, or let evidence sufficient for precedence substitute for equivalence or vice versa.",
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