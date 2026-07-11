# What This Is For

_Last rewritten: 2026-07-11 after Run 22_

## 1. What problem is this system currently the best solution to?

Turning four explicitly labeled decision notes into an auditable assignment for an analyst or agent, with every supplied constraint preserved and separately accounted for before a recommendation is made.

## 2. Who has this problem? Be specific.

A nontechnical operator delegating a narrow consequential decision to an agent, contractor, or colleague. The operator already has the relevant evidence and rules but needs confidence that the handoff will not blur observations with interpretations, hide missing evidence, or collapse multiple gates into one unexplained verdict.

## 3. What is the narrowest version of this problem that the system already solves well?

Given exactly `Decision`, `Evidence`, `Constraints`, and `Success`, the tool checks that the contract is explicit, rejects unsupported structure, preserves the supplied wording, and emits one fixed brief requiring a separate evidence-backed judgment for every constraint.

## 4. What is the most ambitious version it could solve if we stay disciplined?

A trustworthy preflight step for delegated decision analysis: strict enough to expose missing structure and unsupported conclusions, but small enough that an operator can inspect the entire contract and every reasoning obligation before handing it off.

## 5. Why would someone use this instead of a spreadsheet, notebook, ChatGPT prompt, or 30-line script?

Because the value is a repeatable trust boundary rather than formatting. The tool distinguishes operator input from analyst judgment, refuses to infer missing fields, prevents interpretations from becoming facts, and requires every supplied gate to remain visible in the final reasoning.

## 6. What is the biggest threat to usefulness?

Becoming a semantic decision engine. Automatic field classification, threshold calculation, domain modes, or hidden precedence rules would replace the inspectable contract with judgments the operator can no longer audit easily.

## 7. What should be removed today?

Do not expand `machine.py`; it remains only because the repository requires the historical demo command. New work should strengthen or falsify the four-field decision-contract boundary in `decision_brief.py`.