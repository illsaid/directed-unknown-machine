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
            "Recommend one authorized action and name the governing Success branch. Connect every gate result to the branches that require it. A violated or unresolved gate blocks only branches that depend on it; it must not block a separate branch whose supplied conditions are fully satisfied. When every condition of a supplied branch is satisfied, recommend that branch without inventing additional gates. When one fully satisfied branch contains every condition of another plus additional satisfied conditions, recommend the more conditional supplied branch rather than arbitrarily choosing its weaker subset. When multiple fully satisfied branches are not nested and the supplied rule gives no precedence or tie-breaker, report branch authority unresolved and identify the missing precedence; do not choose among them. A conditional precedence rule governs only when every supplied condition activating it is established; if any activating condition is violated or unresolved, preserve the candidate branches and report precedence unresolved. When supplied precedence selects among fully satisfied non-nested branches, recommend the governing branch and preserve each displaced branch as satisfied but non-governing rather than failed or omitted.",
        ),
    ),
)


def scenario_input(text: str) -> str:
    match = re.search(r"^## Input\s*$\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not match:
        raise SystemExit("scenario is missing an Input section")
    return match.group(1).strip().strip('"')


def unsupported_labels(raw: str) -> list[str]:
    explicit = re.findall(r"^([A-Za-z][A-Za-z \t]*):", raw, re.MULTILINE)
    allowed = {item.lower() for item in LABELS}
    seen: set[str] = set()
    unsupported: list[str] = []
    for label in explicit:
        label = label.strip()
        key = label.lower()
        if key not in allowed and key not in seen:
            seen.add(key)
            unsupported.append(label)
    return unsupported


def malformed_unsupported_labels(raw: str) -> list[tuple[str, int]]:
    allowed = {item.lower() for item in LABELS}
    seen: set[str] = set()
    malformed: list[tuple[str, int]] = []
    lines = raw.splitlines()
    for index, line in enumerate(lines[:-1]):
        if not re.fullmatch(r"[A-Za-z][A-Za-z \t]*", line):
            continue
        if not re.match(r"^[ \t]*:", lines[index + 1]):
            continue
        label = line.strip()
        key = label.lower()
        if key not in allowed and key not in seen:
            seen.add(key)
            malformed.append((label, index + 1))
    return malformed


def duplicate_allowed_labels(raw: str) -> list[tuple[str, list[int]]]:
    occurrences: dict[str, list[int]] = {label.lower(): [] for label in LABELS}
    canonical = {label.lower(): label for label in LABELS}
    pattern = re.compile(
        rf"^({'|'.join(LABELS)})[ \t]*:",
        re.IGNORECASE | re.MULTILINE,
    )
    for match in pattern.finditer(raw):
        line_number = raw.count("\n", 0, match.start()) + 1
        occurrences[match.group(1).lower()].append(line_number)
    return [
        (canonical[key], line_numbers)
        for key, line_numbers in occurrences.items()
        if len(line_numbers) > 1
    ]


def labeled_value(raw: str, label: str) -> str | None:
    next_labels = "|".join(LABELS)
    match = re.search(
        rf"(?:^|\n){label}[ \t]*:[ \t]*(.*?)(?=\n(?:{next_labels})[ \t]*:|\Z)",
        raw,
        re.IGNORECASE | re.DOTALL,
    )
    return match.group(1).strip() if match else None


def repair_template(missing: list[str]) -> str:
    fields = "\n".join(f"{label}:" for label in missing)
    return f"Missing explicit fields:\n{fields}"


def malformed_template(malformed: list[tuple[str, int]]) -> str:
    fields = "\n".join(f"- {label} (input line {line_number})" for label, line_number in malformed)
    return (
        f"Ambiguous field-like breaks:\n{fields}\n"
        "Keep prose continuous, or keep each field label and colon on the same line."
    )


def duplicate_template(duplicates: list[tuple[str, list[int]]]) -> str:
    fields = "\n".join(
        f"- {label} (input lines {', '.join(str(line) for line in line_numbers)})"
        for label, line_numbers in duplicates
    )
    return (
        f"Duplicate explicit fields:\n{fields}\n"
        "Keep each allowed field exactly once; rewrite ordinary prose so it does not mimic a field label."
    )


def unsupported_template(unsupported: list[str]) -> str:
    fields = "\n".join(f"- {label}" for label in unsupported)
    allowed = ", ".join(LABELS)
    return (
        f"Unsupported explicit fields:\n{fields}\n"
        f"Allowed: {allowed}.\n"
        "Remap each extra meaning to one of those fields."
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
    malformed = malformed_unsupported_labels(raw)
    if malformed:
        raise SystemExit(malformed_template(malformed))
    unsupported = unsupported_labels(raw)
    if unsupported:
        raise SystemExit(unsupported_template(unsupported))
    duplicates = duplicate_allowed_labels(raw)
    if duplicates:
        raise SystemExit(duplicate_template(duplicates))
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