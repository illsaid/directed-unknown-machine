#!/usr/bin/env python3
"""
Directed Unknown Machine starter executable.

This is not intended to be the final product. It is a small pressure chamber:
read a scenario, infer what usefulness would mean, and emit a structured report.

Usage:
    python machine.py run SCENARIOS/001-friendly.md
    python machine.py run SCENARIOS/001-friendly.md --json
    python machine.py list SCENARIOS
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List

FIELD_NAMES = [
    "type",
    "user",
    "situation",
    "input",
    "expected useful outcome",
    "actual outcome",
    "whether the system helped",
    "what broke",
    "what would make the result more useful",
]


@dataclass
class Scenario:
    path: str
    title: str
    fields: Dict[str, str]


@dataclass
class UsefulnessReport:
    scenario: str
    scenario_type: str
    user: str
    inferred_problem: str
    expected_outcome: str
    actual_outcome: str
    helped: str
    reasoning: List[str]
    failure_points: List[str]
    next_improvement: str
    hypothesis_pressure: str


def normalize_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def read_scenario(path: Path) -> Scenario:
    if not path.exists():
        raise SystemExit(f"scenario not found: {path}")
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = path.stem
    fields: Dict[str, str] = {}
    current_key = None
    current_value: List[str] = []

    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            continue
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            if current_key:
                fields[current_key] = "\n".join(current_value).strip()
            current_key = normalize_key(match.group(1))
            current_value = []
        elif current_key:
            current_value.append(line)

    if current_key:
        fields[current_key] = "\n".join(current_value).strip()

    missing = [name for name in FIELD_NAMES if name not in fields]
    if missing:
        raise SystemExit(f"scenario {path} is missing sections: {', '.join(missing)}")

    return Scenario(path=str(path), title=title, fields=fields)


def compact(text: str, fallback: str = "unspecified") -> str:
    text = " ".join((text or "").split())
    return text if text else fallback


def infer_problem(scenario: Scenario) -> str:
    user = compact(scenario.fields.get("user", ""), "the user")
    situation = compact(scenario.fields.get("situation", ""))
    expected = compact(scenario.fields.get("expected useful outcome", ""))
    return f"Help {user} get from this situation — {situation} — to this useful outcome: {expected}"


def analyze_helped(value: str) -> str:
    value_norm = normalize_key(value)
    if value_norm in {"yes", "helped", "true"}:
        return "yes"
    if value_norm in {"no", "not helped", "false"}:
        return "no"
    if "partial" in value_norm or "unknown" in value_norm or "not yet" in value_norm:
        return "unknown"
    return "unknown"


def build_report(scenario: Scenario) -> UsefulnessReport:
    fields = scenario.fields
    helped = analyze_helped(fields.get("whether the system helped", "unknown"))
    what_broke = compact(fields.get("what broke", ""), "nothing recorded yet")
    improvement = compact(fields.get("what would make the result more useful", ""), "run the scenario and record a concrete failure")
    scenario_type = compact(fields.get("type", ""), "unknown")

    reasoning = [
        f"Scenario type is {scenario_type}.",
        f"Useful output is defined by the scenario, not by feature count.",
        f"The current system should be judged against: {compact(fields.get('expected useful outcome', ''))}",
    ]

    failure_points = []
    if helped == "unknown":
        failure_points.append("The scenario has not yet produced a yes/no usefulness result.")
    if "unspecified" in compact(fields.get("input", ""), "unspecified").lower():
        failure_points.append("The input is underspecified; a real tool would need to recover or constrain it.")
    if what_broke.lower() not in {"none", "nothing", "nothing recorded yet"}:
        failure_points.append(what_broke)
    if not failure_points:
        failure_points.append("No failure recorded; add a hostile or comparative scenario before increasing confidence.")

    if helped == "yes":
        pressure = "strengthen the tested hypothesis, but only if a simpler baseline would not do as well"
    elif helped == "no":
        pressure = "weaken or kill the tested hypothesis unless one small change directly fixes the failure"
    else:
        pressure = "do not raise confidence yet; run or refine the scenario until the outcome is observable"

    return UsefulnessReport(
        scenario=scenario.title,
        scenario_type=scenario_type,
        user=compact(fields.get("user", "")),
        inferred_problem=infer_problem(scenario),
        expected_outcome=compact(fields.get("expected useful outcome", "")),
        actual_outcome=compact(fields.get("actual outcome", ""), "not yet recorded"),
        helped=helped,
        reasoning=reasoning,
        failure_points=failure_points,
        next_improvement=improvement,
        hypothesis_pressure=pressure,
    )


def print_text(report: UsefulnessReport) -> None:
    print(f"Scenario: {report.scenario}")
    print(f"Type: {report.scenario_type}")
    print(f"User: {report.user}")
    print()
    print("Inferred problem:")
    print(f"- {report.inferred_problem}")
    print()
    print("Expected useful outcome:")
    print(f"- {report.expected_outcome}")
    print()
    print("Actual outcome:")
    print(f"- {report.actual_outcome}")
    print()
    print(f"Helped: {report.helped}")
    print()
    print("Reasoning:")
    for item in report.reasoning:
        print(f"- {item}")
    print()
    print("Failure points:")
    for item in report.failure_points:
        print(f"- {item}")
    print()
    print("Next improvement:")
    print(f"- {report.next_improvement}")
    print()
    print("Hypothesis pressure:")
    print(f"- {report.hypothesis_pressure}")


def cmd_run(args: argparse.Namespace) -> int:
    scenario = read_scenario(Path(args.scenario))
    report = build_report(scenario)
    if args.json:
        print(json.dumps(asdict(report), indent=2, sort_keys=True))
    else:
        print_text(report)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    root = Path(args.directory)
    if not root.exists():
        raise SystemExit(f"scenario directory not found: {root}")
    for path in sorted(root.glob("*.md")):
        try:
            scenario = read_scenario(path)
            print(f"{path}: {compact(scenario.fields.get('type', 'unknown'))} — {scenario.title}")
        except SystemExit as exc:
            print(f"{path}: invalid ({exc})")
    return 0


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run scenario pressure tests for the Directed Unknown Machine.")
    sub = parser.add_subparsers(dest="command", required=True)

    run_p = sub.add_parser("run", help="run one scenario and emit a usefulness report")
    run_p.add_argument("scenario", help="path to a scenario markdown file")
    run_p.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    run_p.set_defaults(func=cmd_run)

    list_p = sub.add_parser("list", help="list scenario files")
    list_p.add_argument("directory", nargs="?", default="SCENARIOS", help="scenario directory")
    list_p.set_defaults(func=cmd_list)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
