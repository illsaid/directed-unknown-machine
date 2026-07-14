# What This Is For

_Last rewritten: 2026-07-15 after Run 105_

## 1. What problem is this system currently the best solution to?

Preflighting a small, explicitly labeled decision handoff so an analyst or agent cannot silently alter the evidence, boundary rules, gate logic, or authorized outcome.

## 2. Who has this problem?

A nontechnical operator delegating one bounded decision whose source notes already identify the decision, evidence, constraints, and success rule. The risk is not missing strategy; it is distortion during transfer.

## 3. What is the narrowest version it already solves well?

Given exactly `Decision`, `Evidence`, `Constraints`, and `Success`, the tool either returns a repairable refusal or emits six ordered audit obligations. It rejects missing, unsupported, and malformed field structures before extraction, preserves distinct defects and their Input-relative locations, and never invents a destination for extra meaning.

## 4. What is the most ambitious disciplined version?

A tiny compiler for delegated decision analysis: supplied notes go in; a bounded, auditable analysis contract or exact structural refusal comes out. It should remain a preflight tool, not become the analyst, semantic classifier, threshold engine, or workflow platform.

## 5. Why use it instead of a prompt or checklist?

Because the refusal boundaries are executable and accumulated from hostile scenarios. Unsupported transformations cannot borrow authority from adjacent evidence, unresolved gates cannot disappear into an overall verdict, malformed extra fields cannot contaminate allowed fields, and recommendations must stay inside the supplied success branches.

## 6. What is the biggest threat to usefulness?

Polishing edge-case grammar long after the core contract is stable. Further changes are justified only when a concrete handoff can lose meaning, misstate a repair, or weaken an established refusal boundary.

## 7. What should be removed or avoided?

Keep `machine.py` only for the required historical demo. Do not add automatic field classification, calculations, domain modes, configuration, dashboards, or generic parsing abstractions. Prefer exact repairs for demonstrated contract failures over broader input tolerance.