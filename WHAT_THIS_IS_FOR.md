# What This Is For

_Last rewritten: 2026-07-10 after Run 15_

## 1. What problem is this system currently the best solution to?

Turning a small set of explicitly labeled decision notes into a bounded assignment for an analyst or agent without losing the operator's decision, supplied evidence, constraints, or success rule.

## 2. Who has this problem? Be specific.

A nontechnical operator delegating a consequential but narrow decision analysis to an agent, contractor, or colleague. The operator has the relevant context but needs confidence that observations, interpretations, prohibitions, and reversal conditions will not be blurred during handoff.

## 3. What is the narrowest version of this problem that the system already solves well?

Given exactly four labeled fields — `Decision`, `Evidence`, `Constraints`, and `Success` — the tool checks that the contract is explicit, rejects unsupported structure instead of silently absorbing it, preserves the supplied wording, and emits one fixed decision-brief assignment.

## 4. What is the most ambitious version it could solve if we stay disciplined?

A trustworthy preflight step for agent delegation: small enough to inspect, strict enough to expose missing or unsupported decision structure, and opinionated enough to prevent supplied interpretations from quietly becoming facts.

## 5. Why would someone use this instead of a spreadsheet, notebook, ChatGPT prompt, or 30-line script?

Because the value is the narrow trust boundary, not formatting. The tool makes explicit what came from the operator, refuses to infer missing contract fields, rejects extra labels rather than hiding them, and produces the same bounded deliverable every time.

## 6. What is the biggest threat to usefulness?

Becoming a semantic classifier for arbitrary notes. If the tool starts guessing field destinations, judging every sentence, supporting aliases, or adding domain modes, it loses the inspectable boundary that currently makes it trustworthy.

## 7. What should be removed today?

Do not expand `machine.py`; it survives only as the historical required demo command. New work should strengthen `decision_brief.py` or falsify H2. Remove the old harness only when the repository rules no longer require the historical command.