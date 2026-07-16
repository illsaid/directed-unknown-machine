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

- **Runs 3–21:** Established the four-field `Decision`, `Evidence`, `Constraints`, and `Success` contract; rejected unsupported structure; preserved observations, interpretations, assumptions, conflicts, and gate states without inference.
- **Runs 22–46:** Established provenance, applicability, adjustment, ranges, equality, conflicting boundaries, equivalence, and explicit precedence boundaries.
- **Runs 47–87:** Consolidated and ordered the behavior into six inspectable audit operations without broadening the schema.
- **Runs 88–111:** Tightened explicit-label grammar, repair output, duplicate handling, ambiguity reporting, and multiline preservation.
- **Runs 112–126:** Required gate-to-branch accounting, fully authorized recommendations, branch-local blocking, nested-branch specificity, non-nested precedence discipline, conditional precedence evidence, and scope-aware applicability.
- **Runs 127–140:** Distinguished unresolved evidence from authorized fallbacks; required every fallback gate and its evidence; preserved duration gaps, overlaps, violations, and unavailable branches without domain-specific machinery.
- **Runs 141–143:** Kept fallback failure branch-local, refused arbitrary selection between satisfied non-nested branches, and required applied unconditional precedence authority to remain visible.
- **Run 144:** Preserved conflicting precedence policies and left branch authority unresolved when no supplied rule established which policy controlled.
- **Run 145 / `SCENARIOS/143-governed-conflicting-fallback-precedence.md`:** A supplied governance rule established that DP-9 controlled the opposing NT-3 policy for the target disposition. The recommendation obligation now requires the full authority trace: cite the governance rule and selected precedence policy, preserve displaced policies as conflicting but non-governing, and preserve displaced satisfied branches as satisfied but non-governing.
- **Run 146 / `SCENARIOS/144-out-of-scope-governance-precedence.md`:** QG-2 resolved DP-9 versus NT-3 only for off-site disposition, while the target batch was on site. Existing scope-preservation obligations correctly prohibit borrowing that governance authority: both policies and both satisfied branches remain visible, branch authority remains unresolved, and the missing input is governance authority covering on-site disposition.
- **Run 147 / `SCENARIOS/145-governance-exception-blocks-precedence.md`:** QG-4 generally resolved DP-9 versus NT-3 but explicitly exempted contamination-hold batches, including B-261. The recommendation obligation now states that governance authority applies only when the target is inside the rule's scope and outside every explicit exception; the exception remains visible and the precedence conflict remains unresolved.
- **Run 148 / `SCENARIOS/146-unresolved-governance-exception-applicability.md`:** A contamination-review alert did not establish either an active hold or clearance. The recommendation obligation now requires supplied evidence that the target is outside every exception before governance may resolve precedence; unresolved exception applicability preserves the uncertainty, leaves governance and branch authority unresolved, and names the evidence needed to decide whether the exception applies.
- **Run 149 / `SCENARIOS/147-governed-conflicting-exception-applicability.md`:** CH-14 and CR-8 conflicted about whether B-271 was inside QG-4's contamination-hold exception, while AR-6 explicitly made the QA-director-signed release record governing. Existing evidence-preservation and governance obligations composed correctly without a new rule: CR-8 established that the exception did not apply, CH-14 remained conflicting but non-governing, QG-4 and DP-9 governed, and local reprocessing was authorized.

**Evidence against:** The transformation does not apply to coordination problems or unlabeled prose. The executable does not classify sentences or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on an operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Supply conflicting applicability authorities that select opposite exception-status records, testing whether authority remains unresolved rather than allowing either source to govern.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests. Run 4 exposed a concrete category error.

**Evidence against:** Runs 5–149 produced useful results by shaping and auditing decision contracts, not by providing general failure explanations.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.