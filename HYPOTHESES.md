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
- **Run 64 / `SCENARIOS/063-recommendation-versus-gate-judgments.md`:** Confirmed that Governed recommendation and Gate judgments are distinct audit questions. Gate judgments evaluates each constraint from supplied evidence; Governed recommendation selects the action required by the supplied success or reversal rule.
- **Run 65 / `SCENARIOS/064-source-record-versus-evidence-transformation.md`:** Confirmed that Evidence provenance and Evidence transformation are distinct audit questions. Provenance preserves what each source reports; transformation validates supplied support before exclusion or adjustment changes how a value applies. Renaming `Applicability and adjustment` to `Evidence transformation` makes the operation explicit without changing behavior.
- **Run 66 / `SCENARIOS/065-visible-reasoning-sequence.md`:** Reordered the unchanged six audit groups into dependency order: Evidence provenance, Evidence transformation, Boundary reconciliation, Boundary evaluation, Gate judgments, and Governed recommendation. The output now exposes the audit trail before the conclusion instead of presenting the recommendation first.
- **Run 67 / `SCENARIOS/066-evidence-status-versus-recommendation.md`:** Moved the unchanged observation, interpretation, assumption, and unresolved-gap status obligation from Governed recommendation to Evidence provenance. Claim status is now preserved at the source-record stage before transformations or downstream judgments use it; Governed recommendation is narrowed to action selection under the supplied rule.
- **Run 68 / `SCENARIOS/067-consolidated-evidence-provenance.md`:** Consolidated source mapping and claim-status preservation into one immutable-record invariant. The combined requirement still prevents measurement spill, duplicate-evidence inflation, conflicting-value erasure, and promotion of interpretations or assumptions to fact.
- **Run 69 / `SCENARIOS/068-consolidated-boundary-evaluation.md`:** Consolidated full-range handling and supplied equality semantics into one boundary-application invariant. The combined requirement still resolves same-side ranges from the whole range, preserves conditional outcomes for threshold-crossing ranges, honors explicit inclusive and strict equality wording, and refuses to invent semantics for a bare numeric threshold.
- **Run 70 / `SCENARIOS/069-boundary-reconcile-then-apply.md`:** Renamed the two unchanged boundary stages to `Boundary: reconcile` and `Boundary: apply`. The shared prefix and imperative verbs expose their dependency—establish the governing boundary before applying evidence—without merging conflict resolution with threshold application or changing either refusal boundary.
- **Run 71 / `SCENARIOS/070-evidence-preserve-then-transform.md`:** Renamed the two unchanged evidence stages to `Evidence: preserve` and `Evidence: transform`. The shared prefix and imperative verbs expose that the source record must be fixed before any supported exclusion or adjustment changes how it applies, without merging provenance with transformation or weakening either support boundary.
- **Run 72 / `SCENARIOS/071-judge-gates-then-recommend.md`:** Renamed the two unchanged final stages to `Decision: judge gates` and `Decision: recommend`. The shared prefix and imperative verbs expose that independent gate results must be established before the supplied success rule selects an action, without collapsing gate judgment into recommendation.
- **Run 73 / `SCENARIOS/072-visible-sequence-summary.md`:** Added one literal sequence line before the detailed requirements: preserve evidence, transform evidence, reconcile boundaries, apply boundaries, judge gates, recommend. The line makes the complete workflow visible on first scan while leaving all six detailed obligations and refusal boundaries unchanged.

**Evidence against:** The transformation does not apply to coordination problems or unlabeled prose. The executable does not classify sentences or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on an operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Test whether the longest remaining requirement can be shortened by removing redundant wording while preserving its exact refusal boundary. Do not add another summary or presentation layer.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests. Run 4 exposed a concrete category error.

**Evidence against:** Runs 5–73 produced useful results by shaping and auditing decision contracts, not by providing general failure explanations.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.