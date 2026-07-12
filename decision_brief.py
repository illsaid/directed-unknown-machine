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
    print("- Check each constraint separately against Success; for every constraint, state whether it is satisfied, violated, or unresolved and name the supplied evidence supporting that judgment; identify shared sources and the measurements each source actually supplies; when different sources overlap on the same measurement, disclose the overlap without counting it as support for a different measurement or as additional independent evidence beyond that shared measurement; when sources report different values for the same measurement, preserve each value and leave the disagreement explicit unless supplied evidence establishes which source applies; if excluding a source as non-comparable, name the excluded value, the supplied comparability reason, the direct supplied observation establishing that reason, and the supplied evidence establishing why that observation changes applicability to the target decision population—a direct difference without evidence of relevance cannot justify exclusion, and a conclusion or interpretation derived from observations that are not supplied cannot justify exclusion; when an adjusted or reweighted value is used to establish target-population applicability, preserve the original value and name the adjusted value, the supplied adjustment method, and the target population; an adjusted numeric result without a supplied auditable method cannot resolve a gate and must remain an unresolved claim; when an auditable adjustment method depends on an assumption, name the assumption and its supplied support, and keep the adjusted result conditional if that support is absent; when a supplied sensitivity range crosses a gate threshold, report the full range and supplied decision boundary, state the conditional outcome on each side, and do not select a midpoint, best case, or other convenient point estimate to resolve the gate; when every value in a supplied supported sensitivity range lies on the same side of a gate threshold, judge the gate from the full range and do not mark it unresolved merely because the evidence is a range—against a maximum, a wholly lower range satisfies the gate and a wholly higher range violates it; when a supported range touches a threshold exactly, use the supplied comparison wording to judge equality and do not assume the boundary is strict or inclusive; when a numeric threshold is supplied without explicit strict or inclusive comparison wording, equality cannot resolve the gate and must remain unresolved rather than inheriting an unstated convention; when the same threshold is supplied with conflicting strict and inclusive comparison wording, preserve both rules and leave the gate unresolved unless the contract supplies an explicit precedence or reconciliation rule—do not select a rule based on field order; when the same metric is supplied with conflicting numeric thresholds, preserve every threshold value and leave the gate unresolved unless the contract supplies an explicit precedence or reconciliation rule—do not silently choose the stricter threshold, the looser threshold, or the value appearing later; under a strict maximum such as ‘below’ or ‘strictly below,’ equality violates the gate rather than leaving it unresolved; under an inclusive minimum such as ‘at least,’ equality satisfies the gate rather than leaving it unresolved; under a strict minimum such as ‘above’ or ‘strictly above,’ equality violates the gate rather than leaving it unresolved; do not collapse independent gates into one overall pass or fail, do not silently override either field, and state when any failed or unresolved gate prevents a supported recommendation.")
    print("- For threshold statements in different units or representations, preserve both statements. Reconcile them only when the contract explicitly supplies the conversion or equivalence; otherwise leave the gate unresolved. Never introduce an unsupplied conversion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())