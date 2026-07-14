# What This Is For

_Last rewritten: 2026-07-14 after Run 87_

## 1. What problem is this system currently the best solution to?

Turning four explicitly labeled decision notes into a compact delegated-analysis contract that prevents an analyst or agent from silently rewriting evidence, inventing boundary semantics, or recommending an action outside the supplied success rule.

## 2. Who has this problem? Be specific.

A nontechnical operator delegating one consequential but bounded decision. The operator already knows the decision, evidence, constraints, and fallback logic; the failure risk is distortion during handoff, not lack of information.

## 3. What is the narrowest version of this problem that the system already solves well?

Given exactly `Decision`, `Evidence`, `Constraints`, and `Success`, the tool verifies that all four fields are explicit, requests only missing fields when the contract is incomplete, and emits six ordered audit obligations: preserve evidence, transform it only with exact support, reconcile boundaries, apply them literally, judge each gate, and recommend one action authorized by the governing success branch.

## 4. What is the most ambitious version it could solve if we stay disciplined?

A tiny preflight compiler for delegated decision analysis: a repeatable contract that makes unsupported transformations and recommendations visibly invalid before consequential work begins, without becoming a semantic classifier or decision engine.

## 5. Why would someone use this instead of a spreadsheet, notebook, ChatGPT prompt, or 30-line script?

Because its value is refusal discipline. Evidence transformations cannot borrow authority from unrelated support, unresolved boundaries remain unresolved, individual gate failures cannot disappear into an overall verdict, and the recommendation must name the supplied branch that authorizes it.

## 6. What is the biggest threat to usefulness?

The fixed audit requirements are still dense enough that the output may feel like policy prose rather than an immediately usable delegation contract. Simplification is useful only while every tested refusal boundary remains intact.

## 7. What should be removed today?

Remove generic framing whenever the schema labels or audit headings already communicate the same information. Do not add automatic classification, calculations, threshold parsing, unit conversion, domain modes, configuration, or a dashboard. Keep `machine.py` unchanged solely because the historical demo command is required.