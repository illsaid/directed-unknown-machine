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
- **Runs 63–87:** Ordered and simplified the six audit operations, removed presentation-only wrappers, and made complete, missing-field, and unlabeled contract states increasingly exact without changing the schema or refusal boundaries.
- **Run 88 / `SCENARIOS/087-unsupported-fields-first.md`:** Replaced the dense unsupported-field sentence with a three-part refusal that leads with the unsupported label, restates the unchanged four-field schema, and preserves the extra meaning by remapping it under the supported field matching its role.
- **Run 89 / `SCENARIOS/088-allowed-schema-shorthand.md`:** Shortened the schema reminder to `Allowed: Decision, Evidence, Constraints, Success.` and retained explicit remapping guidance, preserving the refusal boundary with less repeated wording.
- **Run 90 / `SCENARIOS/089-matching-field-remap.md`:** Shortened the remapping instruction to `Place each extra meaning under its matching allowed field.` The repair still preserves the unsupported meaning, leaves field selection to the operator, and refuses schema expansion or automatic classification.
- **Run 91 / `SCENARIOS/090-no-repeated-allowed.md`:** Removed the repeated word `allowed` from the remapping instruction. The schema line establishes the fixed fields once, while `Place each extra meaning under its matching field.` keeps remapping operator-directed.
- **Run 92 / `SCENARIOS/091-multiple-unsupported-fields.md`:** Replaced singular-sounding `matching field` guidance with `Remap each extra meaning to one of those fields.` Two unsupported labels remain separately visible, the preceding schema list is the only destination set, and field choice remains with the operator rather than the executable.
- **Run 93 / `SCENARIOS/092-repeated-unsupported-label.md`:** Collapsed repeated case-insensitive occurrences of the same unsupported label into one repair item while preserving first-seen spelling and leaving every distinct source meaning untouched for operator-directed remapping.
- **Run 94 / `SCENARIOS/093-case-variant-unsupported-label.md`:** Verified that `Owner:` and `owner:` collapse to one unsupported-field repair item, preserve the first supplied spelling, and leave both distinct source meanings untouched. No executable change was needed; the Run 93 boundary survived a hostile case-variation regression.
- **Run 95 / `SCENARIOS/094-spaced-unsupported-label.md`:** Trimmed captured unsupported labels before case-insensitive deduplication, so `Owner:` and `Owner :` now produce one `- Owner` repair item while both source meanings remain untouched and the four-field schema remains fixed.
- **Run 96 / `SCENARIOS/095-spaced-allowed-label.md`:** Allowed insignificant pre-colon spacing on the four fixed labels, including lookahead boundaries, so `Decision :` reaches the same complete-contract output as `Decision:` instead of escaping unsupported-field repair and then being falsely reported missing.

**Evidence against:** The transformation does not apply to coordination problems or unlabeled prose. The executable does not classify sentences or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on an operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Verify that pre-colon tolerance remains limited to horizontal spacing and does not accept a line break that would blur field structure.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests. Run 4 exposed a concrete category error.

**Evidence against:** Runs 5–96 produced useful results by shaping and auditing decision contracts, not by providing general failure explanations.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.