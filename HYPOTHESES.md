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
- **Runs 88–99:** Simplified unsupported-field repair, deduplicated label variants, and aligned allowed and unsupported labels around same-line horizontal colon spacing.
- **Run 100:** Exposed that `Owner\n:` stayed outside explicit-label detection but was absorbed into Success; confidence dropped to 0.98.
- **Run 101:** Added a narrow malformed unsupported-label preflight, closing the contamination failure and restoring confidence to 0.99.
- **Runs 102–104:** Verified allowed-label exclusion, first-occurrence location reporting, and case-insensitive collapse of repeated malformed labels.
- **Run 105 / `SCENARIOS/103-distinct-line-broken-unsupported-labels.md`:** Verified that two different malformed unsupported labels remain separately visible in source order with their own first occurrence locations. Changed the repair wording from ambiguous `(line N)` to `(input line N)`, accurately identifying that numbering is relative to the extracted `## Input` block rather than the full scenario file.
- **Run 106 / `SCENARIOS/104-repeated-and-distinct-line-broken-labels.md`:** Verified that first-occurrence deduplication composes correctly with distinct-defect preservation: `Owner`, `Deadline`, and later `owner` produce exactly `Owner (input line 2)` and `Deadline (input line 5)` in source order. No executable change was justified.
- **Run 107 / `SCENARIOS/105-ambiguous-wrapped-prose.md`:** Showed that a standalone word followed by a colon-start line can be either malformed schema or wrapped prose. The executable still refuses before extraction, but now reports an `Ambiguous field-like break` and gives both valid repairs instead of claiming semantic certainty it does not have.
- **Run 108 / `SCENARIOS/106-multiline-evidence-preservation.md`:** Exposed that valid multiline Evidence was accepted but flattened into one sentence. Field extraction now strips only surrounding whitespace, preserving internal line and paragraph structure without broadening the four-field grammar.
- **Run 109 / `SCENARIOS/107-evidence-paragraph-break.md`:** Verified that a blank-line paragraph break inside Evidence survives extraction exactly and does not create a false field boundary. No executable change was needed; the Run 108 preservation fix already covered the stronger paragraph case.
- **Run 110 / `SCENARIOS/108-duplicate-allowed-label.md`:** Exposed that an Evidence sentence formatted as `Success:` caused the first structurally explicit Success occurrence to replace the actual authorized Success rule. Added a duplicate allowed-label preflight that reports every occurrence location and refuses before extraction rather than guessing which occurrence is prose.

**Evidence against:** The transformation does not apply to coordination problems or unlabeled prose. The executable does not classify sentences or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on an operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Verify the refusal is narrow: ordinary Evidence continuation prose beginning with an allowed-label word but without a colon must remain inside Evidence and reach complete-contract output.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests. Run 4 exposed a concrete category error.

**Evidence against:** Runs 5–110 produced useful results by shaping and auditing decision contracts, not by providing general failure explanations.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.