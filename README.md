# Directed Unknown Machine

This repository is an autonomous experiment in purpose discovery.

The agent is not being asked to build a product, a framework, a dashboard, or a bag of utilities. It is being asked to repeatedly build, test, simplify, and converge until this repo becomes unusually good at one narrow real-world task.

## Core directive

You are building a single-purpose tool whose purpose is not known at the start.

The goal is to discover, through repeated implementation and testing, what specific real-world problem this system is becoming unusually good at solving.

Every run must:

1. Observe the current system.
2. Read `MACHINE_RULES.md`, `HYPOTHESES.md`, `JOURNAL.md`, `WHAT_THIS_IS_FOR.md`, and the latest files in `SCENARIOS/`.
3. Hypothesize what problem the system is becoming good at solving.
4. Test that hypothesis against a concrete scenario.
5. Improve the system to make that scenario work better, or abandon the hypothesis if the fit is weak.
6. Remove or simplify anything that serves dead hypotheses.
7. Record what changed, what was tested, and whether the hypothesis survived.

## Current runnable artifact

The repo must always run. The starter artifact is intentionally small:

```bash
python machine.py run SCENARIOS/001-friendly.md
python machine.py run SCENARIOS/001-friendly.md --json
```

`machine.py` is not the final product. It is the first pressure chamber: it reads a scenario and emits a structured usefulness report. The agent should mutate, replace, narrow, or delete this harness when evidence points toward a more specific tool.

## Success condition

The project succeeds if, after many autonomous runs, a human can:

1. Understand what the tool does in one sentence.
2. Use it for a real task without reading much documentation.
3. Trust its output because the system explains its reasoning.
4. See why the architecture fits the purpose.
5. Prefer it over a spreadsheet, grep, a notebook, ChatGPT, or a 30-line script for at least one narrow problem.

The project fails if it becomes a generic toolkit, a vague research playground, a dashboard of weak signals, a pile of unrelated utilities, a demo that works but solves no painful problem, or a system whose usefulness is explained only in prose.

## Repo map

- `MACHINE_RULES.md` — operating rules for autonomous runs.
- `HYPOTHESES.md` — ranked hypotheses about what problem this system might solve.
- `SCENARIOS/` — concrete tests, including friendly, hostile, comparative, and transfer scenarios.
- `JOURNAL.md` — run-by-run learning log.
- `WHAT_THIS_IS_FOR.md` — rewritten every 24 hours to force convergence.
- `machine.py` — current runnable artifact.
- `RUNS/` — machine-readable run records when useful.
