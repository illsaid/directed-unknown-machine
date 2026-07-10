#!/usr/bin/env python3
"""Run scenario pressure tests for the Directed Unknown Machine."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
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

VAGUE_TERMS = {
    "flexible",
    "smart",
    "many things",
    "better decisions",
    "messy information",
    "organize",
    "useful",
}


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
    decision: str
    bounded_task: str
    reasoning: List[str]
    failure_points: List[str]
    next_improvement: str
    recommended_action: str
    hypothesis_pressure: str


def normalize_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def compact(text: str, fallback: str = "unspecified") -> str:
    value = " ".join((text or "").split())
    return value if value else fallback


def read_scenario(path: Path) -> Scenario:
    if not path.exists():
        raise SystemExit(f"scenario not found: {path}")

    fields: Dict[str, str] = {}
    title = path.stem
    current_key = None
    current_value: List[str] = []

    for line in path.read_text(encoding="utf-8").splitlines():
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
    return Scenario(str(path), title, fields)


def analyze_helped(value: str) -> str:
    normalized = normalize_key(value)
    if normalized in {"yes", "helped", "true"}:
        return "yes"
    if normalized in {"no", "not helped", "false"}:
        return "no"
    if "partial" in normalized:
        return "partial"
    return "unknown"


def is_vague_input(text: str) -> bool:
    normalized = normalize_key(text)
    matches = sum(term in normalized for term in VAGUE_TERMS)
    return matches >= 3 or len(normalized.split()) < 8


def shape_bounded_task(scenario: Scenario) -> str:
    raw_input = compact(scenario.fields.get("input", ""))
    if not is_vague_input(raw_input):
        return "No reshaping needed: run the concrete input against the expected outcome."

    user = compact(scenario.fields.get("user", "the operator"))
    return (
        f"For {user}, take one real messy note set, identify one decision it must support, "
        "produce a one-page decision brief with three evidence-backed options and one recommendation, "
        "then judge success by whether the user can choose an option without requesting a new dashboard or platform."
    )


def infer_problem(scenario: Scenario) -> str:
    user = compact(scenario.fields.get("user", ""), "the user")
    situation = compact(scenario.fields.get("situation", ""))
    expected = compact(scenario.fields.get("expected useful outcome", ""))
    return f"Help {user} get from this situation — {situation} — to this useful outcome: {expected}"


def decision_for(helped: str) -> str:
    return {
        "yes": "candidate-strengthen",
        "partial": "hold-but-improve",
        "no": "weaken-or-kill",
    }.get(helped, "hold-confidence")


def action_for(scenario: Scenario, helped: str, improvement: str, bounded_task: str) -> str:
    if is_vague_input(scenario.fields.get("input", "")):
        return f"Run this bounded task instead of expanding the request: {bounded_task}"
    if helped == "yes":
        return "Run a comparative scenario before raising confidence; a simpler checklist may still be enough."
    if helped == "partial":
        return f"Make one scenario-tied improvement: {improvement}"
    if helped == "no":
        return "Fix exactly one recorded failure, or lower the tested hypothesis confidence."
    return f"Record a yes/partial/no outcome in {scenario.path}, then run a hostile or comparative scenario."


def build_report(scenario: Scenario) -> UsefulnessReport:
    fields = scenario.fields
    helped = analyze_helped(fields.get("whether the system helped", "unknown"))
    what_broke = compact(fields.get("what broke", ""), "nothing recorded yet")
    improvement = compact(fields.get("what would make the result more useful", ""), "run the scenario")
    scenario_type = compact(fields.get("type", ""), "unknown")
    decision = decision_for(helped)
    bounded_task = shape_bounded_task(scenario)

    reasoning = [
        f"Scenario type is {scenario_type}.",
        "Useful output is defined by the scenario, not by feature count.",
        f"The current system should be judged against: {compact(fields.get('expected useful outcome', ''))}",
        f"Scenario outcome currently maps to decision: {decision}.",
    ]
    if is_vague_input(fields.get("input", "")):
        reasoning.append("The input uses broad capability language, so it was converted into one observable task.")

    failure_points: List[str] = []
    if helped == "unknown":
        failure_points.append("The scenario has not yet produced a yes/no usefulness result.")
    if helped == "partial":
        failure_points.append("The scenario helped partially; target the recorded gap instead of adding a mode.")
    if is_vague_input(fields.get("input", "")):
        failure_points.append("The input lacks one named decision, one artifact, and one observable success condition.")
    if what_broke.lower() not in {"none", "nothing", "nothing recorded yet", "not yet tested"}:
        failure_points.append(what_broke)
    if not failure_points:
        failure_points.append("No failure recorded; add a hostile or comparative scenario before increasing confidence.")

    pressure = {
        "yes": "strengthen the tested hypothesis only if a simpler baseline would not do as well",
        "partial": "keep the hypothesis alive but do not raise confidence until the recorded gap is fixed",
        "no": "weaken or kill the tested hypothesis unless one small change directly fixes the failure",
    }.get(helped, "do not raise confidence yet; run or refine the scenario until the outcome is observable")

    return UsefulnessReport(
        scenario=scenario.title,
        scenario_type=scenario_type,
        user=compact(fields.get("user", "")),
        inferred_problem=infer_problem(scenario),
        expected_outcome=compact(fields.get("expected useful outcome", "")),
        actual_outcome=compact(fields.get("actual outcome", ""), "not yet recorded"),
        helped=helped,
        decision=decision,
        bounded_task=bounded_task,
        reasoning=reasoning,
        failure_points=failure_points,
        next_improvement=improvement,
        recommended_action=action_for(scenario, helped, improvement, bounded_task),
        hypothesis_pressure=pressure,
    )


def print_text(report: UsefulnessReport) -> None:
    print(f"Scenario: {report.scenario}")
    print(f"Type: {report.scenario_type}")
    print(f"User: {report.user}\n")
    print(f"Inferred problem:\n- {report.inferred_problem}\n")
    print(f"Expected useful outcome:\n- {report.expected_outcome}\n")
    print(f"Actual outcome:\n- {report.actual_outcome}\n")
    print(f"Helped: {report.helped}")
    print(f"Decision: {report.decision}\n")
    print(f"Bounded task:\n- {report.bounded_task}\n")
    print("Reasoning:")
    for item in report.reasoning:
        print(f"- {item}")
    print("\nFailure points:")
    for item in report.failure_points:
        print(f"- {item}")
    print(f"\nNext improvement:\n- {report.next_improvement}\n")
    print(f"Recommended action:\n- {report.recommended_action}\n")
    print(f"Hypothesis pressure:\n- {report.hypothesis_pressure}")


def cmd_run(args: argparse.Namespace) -> int:
    report = build_report(read_scenario(Path(args.scenario)))
    print(json.dumps(asdict(report), indent=2, sort_keys=True) if args.json else "", end="") if args.json else print_text(report)
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
    run_p.add_argument("scenario")
    run_p.add_argument("--json", action="store_true")
    run_p.set_defaults(func=cmd_run)
    list_p = sub.add_parser("list", help="list scenario files")
    list_p.add_argument("directory", nargs="?", default="SCENARIOS")
    list_p.set_defaults(func=cmd_list)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        raise SystemExit(0)
