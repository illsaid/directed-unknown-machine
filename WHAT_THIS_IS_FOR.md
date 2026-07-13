# What This Is For

_Last rewritten: 2026-07-13 after Run 65_

## 1. What problem is this system currently the best solution to?

Turning four explicitly labeled decision notes into a delegated analysis contract whose source record, transformations, boundary handling, gate judgments, and final recommendation can be audited as separate operations.

## 2. Who has this problem? Be specific.

A nontechnical operator handing a consequential but bounded decision to an analyst, agent, or contractor. The operator already has evidence and decision rules, but needs assurance that the recipient will not silently merge sources, discard inconvenient measurements, adjust values without support, invent threshold semantics, or detach the recommendation from the supplied fallback rule.

## 3. What is the narrowest version of this problem that the system already solves well?

Given exactly `Decision`, `Evidence`, `Constraints`, and `Success`, the tool preserves the supplied contract and emits six fixed audit questions: what action the success rule governs, how each gate is judged, what every source reports, whether an evidence transformation is supported, how evidence applies to one boundary, and whether conflicting boundaries can be reconciled.

## 4. What is the most ambitious version it could solve if we stay disciplined?

A tiny preflight compiler for delegated decision analysis. Before work leaves the operator's hands, it would expose a stable reasoning sequence that preserves source claims, permits only supported transformations, keeps unresolved boundaries visible, and makes the final recommendation traceable without becoming a semantic decision engine.

## 5. Why would someone use this instead of a spreadsheet, notebook, ChatGPT prompt, or 30-line script?

Because the useful artifact is not the calculation; it is the enforced separation of operations. The source record cannot be rewritten by an adjustment, a transformation cannot inherit authority from provenance alone, a gate cannot disappear into the overall verdict, and a recommendation cannot float free of the supplied success rule. The executable makes those refusal boundaries repeatable and inspectable.

## 6. What is the biggest threat to usefulness?

The six audit groups are individually defensible but not yet presented as an obvious reasoning sequence. If their order remains arbitrary, the output will still read like a dense checklist rather than a compact delegated-analysis contract.

## 7. What should be removed today?

Do not expand `machine.py`; it remains only for the required historical demo. Do not add automatic source classification, an adjustment engine, a threshold parser, a unit converter, domain modes, configuration, or a dashboard. The next useful step should improve the visible sequence of the six existing audit operations without adding another obligation.