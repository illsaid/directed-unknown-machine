# Hypotheses

Maintain a ranked list of possible problems this system might solve. Each hypothesis must include a problem statement, specific user, confidence, evidence for and against, next test, kill criterion, and status.

Confidence is 0.00–1.00. Keep scores conservative. Scenario evidence beats speculation.

## H1 — Scenario usefulness evaluator

**Status:** killed  
**Confidence:** 0.08

**Problem statement:** People with rough tasks, notes, or ideas need a quick way to test whether a proposed tool or output would help in a concrete situation before building more.

**Specific user:** A solo builder deciding whether an idea is worth another implementation cycle.

**Evidence for:** Runs 1–2 showed that `machine.py` can convert a scenario into a structured report, decision, and next action.

**Evidence against:** Runs 2–6 showed only a thin advantage over a disciplined checklist. The bounded decision-support scenarios were judged without the usefulness-report layer.

**Next test:** None. Remove supporting code only when that can be done without breaking the historical demo command.

**Kill criterion:** Met in Run 6.

## H2 — Labeled decision-contract shaper

**Status:** primary  
**Confidence:** 0.99

**Problem statement:** People with messy labeled decision-support notes need help turning them into one bounded decision-brief task while preserving the actual decision, supplied evidence, constraints, and observable success condition.

**Specific user:** A nontechnical operator handing a bounded decision-analysis task to an agent, analyst, or contractor without losing caveats, confusing interpretation with observation, or accidentally requesting a generic information system.

**Evidence for:**

- **Runs 3–13:** Established the four-field `Decision`, `Evidence`, `Constraints`, and `Success` contract; rejected unlabeled prose and unsupported fields without inference or schema expansion.
- **Runs 14–21:** Preserved observations, interpretations, assumptions, and unresolved conflicts as distinct statuses; added evidence-backed satisfied, violated, and unresolved gate judgments.
- **Runs 22–33:** Preserved source provenance, overlapping and conflicting measurements, applicability limits, exclusions, adjustments, methods, and unsupported assumptions.
- **Runs 34–46:** Established full-range sensitivity handling, explicit strict and inclusive equality semantics, the no-comparator refusal boundary, conflicting threshold preservation, cross-unit equivalence, and explicit precedence.
- **Runs 47–62:** Consolidated accumulated obligations into six inspectable audit groups without changing the four-field contract or weakening established boundaries.
- **Run 63 / `SCENARIOS/062-boundary-application-versus-reconciliation.md`:** Confirmed that Boundary evaluation and Boundary reconciliation are distinct audit questions. Evaluation applies evidence to one supplied boundary; reconciliation requires exact supplied support before choosing among incompatible boundaries.
- **Run 64 / `SCENARIOS/063-recommendation-versus-gate-judgments.md`:** Confirmed that Governed recommendation and Gate judgments are distinct audit questions. Gate judgments evaluates each constraint from supplied evidence; Governed recommendation selects the action required by the supplied success or reversal rule. Renaming `Decision` to `Governed recommendation` makes the operation explicit without adding behavior.

**Evidence against:** The transformation does not apply to coordination problems or unlabeled prose. The executable does not classify sentences or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on an operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Inspect whether Evidence provenance and Applicability and adjustment remain distinct audit questions: recording what each source says versus determining whether a supported transformation may change how that evidence applies.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests. Run 4 exposed a concrete category error.

**Evidence against:** Runs 5–64 produced useful results by shaping and auditing decision contracts, not by providing general failure explanations.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.
