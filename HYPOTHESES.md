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
- **Run 111 / `SCENARIOS/109-allowed-label-word-prose.md`:** Verified that the duplicate refusal remains structural: a continuation line beginning `Success depends...` without a colon remains inside Evidence, reaches complete-contract output, and does not create a second Success field. No executable change was justified.
- **Run 112 / `SCENARIOS/110-vendor-renewal-authority.md`:** A real vendor-renewal handoff exposed a downstream authority gap: the recommendation obligation named the governing Success branch but did not require every gate result to be traced into that branch. The compiler now requires gate-to-branch accounting before any action is recommended, preventing favorable evidence selection or an unsupported economic assumption from silently authorizing renewal.
- **Run 113 / `SCENARIOS/111-vendor-renewal-positive-authority.md`:** The contrasting all-gates-satisfied handoff exposed the opposite authority risk: an analyst could account for every supplied condition yet invent an extra caution gate and withhold the authorized positive action. The final obligation now requires recommending a fully satisfied supplied branch without adding new gates.
- **Run 114 / `SCENARIOS/112-asymmetric-launch-authority.md`:** An asymmetric launch rule exposed that a gate unresolved for full rollout could be misread as blocking a separate 10 percent rollout branch that does not require it. The recommendation obligation now maps gate results to the branches that require them and states that a violated or unresolved gate blocks only dependent branches.
- **Run 115 / `SCENARIOS/113-nested-satisfied-launch-authority.md`:** When both limited and full rollout branches were satisfied, the prior obligation permitted arbitrary selection of the weaker branch. The recommendation rule now requires the more conditional supplied branch when its conditions contain every condition of a satisfied subset branch plus additional satisfied conditions.
- **Run 116 / `SCENARIOS/114-nonnested-satisfied-branch-authority.md`:** Two independent, fully satisfied branches authorized mutually exclusive channel investments, but the supplied Success rule contained no precedence. The compiler now requires branch authority to remain unresolved when satisfied branches are non-nested and no supplied precedence or tie-breaker exists.
- **Run 117 / `SCENARIOS/115-nonnested-precedence-authority.md`:** The same independent satisfied branches included an explicit rule that the referral program takes precedence when both qualify. The recommendation obligation now applies that supplied precedence while preserving paid acquisition as satisfied but non-governing rather than failed or omitted.
- **Run 118 / `SCENARIOS/116-conditional-precedence-unresolved.md`:** Both independent branches qualified, but referral precedence applied only if a partner-exclusivity clause applied, and the supplied evidence left that trigger unresolved. The recommendation obligation now requires every activating condition of conditional precedence to be established; otherwise precedence and branch authority remain unresolved while both candidate branches retain their satisfied status.
- **Run 119 / `SCENARIOS/117-conditional-precedence-established.md`:** The same conditional precedence had its trigger established by supplied legal evidence. The recommendation obligation now requires the governing recommendation to cite the evidence activating conditional precedence, while preserving the displaced paid-acquisition branch as satisfied but non-governing.
- **Run 120 / `SCENARIOS/118-conditional-precedence-conflict.md`:** Conflicting supplied legal opinions about the precedence trigger exposed that an analyst could cite only the favorable source and activate referral precedence. The recommendation obligation now keeps conditional precedence unresolved unless supplied applicability evidence establishes which conflicting source governs.
- **Run 121 / `SCENARIOS/119-conditional-precedence-applicability.md`:** A supplied governance policy established that internal legal controls operational applicability, resolving the trigger conflict against outside counsel. The recommendation obligation now identifies the governing source while preserving displaced trigger evidence as conflicting but non-governing rather than false or omitted.
- **Run 122 / `SCENARIOS/120-partial-period-applicability.md`:** A governance policy made internal legal authoritative only for the first six weeks, while referral precedence required the exclusivity clause to apply for the full quarter. The recommendation obligation now limits applicability authority to its explicit scope, preserves covered and uncovered periods separately, and leaves the broader trigger unresolved unless every required period is established.
- **Run 123 / `SCENARIOS/121-partial-population-applicability.md`:** A governance policy made internal legal authoritative only for US enterprise customers, who represented 80 percent of the target population, while referral precedence required the clause to apply to every target customer. The recommendation obligation now explicitly forbids extrapolating an uncovered population from a covered majority; the full-population trigger remains unresolved.
- **Run 124 / `SCENARIOS/122-complementary-population-applicability.md`:** Complementary governance rules jointly covered every target customer but produced different clause-applicability results. The recommendation obligation now resolves a universal trigger across all governed scopes: every scope must support it for satisfaction, while any rejecting scope violates it; scope results cannot be averaged.
- **Run 125 / `SCENARIOS/123-overlapping-population-applicability.md`:** Internal legal governed all US customers, regional counsel governed all enterprise customers, and US enterprise customers fell inside both scopes. A supplied policy made internal legal controlling in the overlap. The recommendation obligation now applies supplied overlap authority before evaluating a broader trigger, preserves the displaced source only within the overlap, and forbids double-counting the shared population.
- **Run 126 / `SCENARIOS/124-overlapping-population-no-authority.md`:** The same overlapping scopes supplied no authority for the shared US-enterprise population. The recommendation obligation now preserves conflicting authority inside the overlap as unresolved, forbids inheriting either source by convenience, and leaves any broader trigger that depends on the overlap unresolved.
- **Run 127 / `SCENARIOS/125-explicit-conflict-fallback.md`:** A refrigerated-shipment handoff exercised all six audit obligations and exposed a distinction between unresolved evidence and unresolved authority. The supplied Success rule explicitly authorized quarantine and an independent assay when temperature evidence remained conflicting or unresolved. The recommendation obligation now requires that fallback action instead of returning no authorized recommendation.
- **Run 128 / `SCENARIOS/126-conditional-conflict-fallback.md`:** A second refrigerated-shipment handoff added a fallback-specific laboratory-capacity gate. Temperature conflict established the fallback trigger, but assay availability within 48 hours remained unresolved. The recommendation obligation now activates an unresolved-condition fallback only when its trigger and every additional supplied fallback condition are established.
- **Run 129 / `SCENARIOS/127-established-conditional-conflict-fallback.md`:** The contrasting shipment handoff established both the conflicting-temperature fallback trigger and written laboratory capacity within 48 hours. The recommendation obligation now requires an activated fallback recommendation to cite the supplied evidence establishing its trigger and every additional fallback-specific gate, making the complete authority chain inspectable.
- **Run 130 / `SCENARIOS/128-multi-gate-conflict-fallback.md`:** A fallback requiring both assay-start capacity and qualified storage exposed that listing every gate is insufficient if one source is silently reused across distinct gates. The recommendation obligation now keeps fallback-specific gates independently evidenced and permits shared support only when the supplied evidence explicitly supports both gates.
- **Run 131 / `SCENARIOS/129-explicit-shared-fallback-evidence.md`:** One signed laboratory certificate explicitly established both assay start within 48 hours and qualified storage for the seven-day assay period. The existing Run 130 obligation correctly permitted the same record to support both fallback gates because its dual support was explicit. No executable change was justified.
- **Run 132 / `SCENARIOS/130-implied-shared-fallback-evidence.md`:** One laboratory certificate explicitly established assay-start capacity but merely suggested storage capability by saying the laboratory routinely handles refrigerated stability work. The recommendation obligation now states the observable consequence: the record supports only the explicit gate, the implied storage gate remains unresolved, and the fallback branch cannot govern.
- **Run 133 / `SCENARIOS/131-partial-duration-fallback-evidence.md`:** A laboratory certificate explicitly reserved qualified storage for five days while the fallback required seven. The recommendation obligation now limits duration-bound evidence to its stated period, preserves the established five days and unresolved two-day remainder separately, and prevents the fallback branch from governing.
- **Run 134 / `SCENARIOS/132-complementary-duration-fallback-evidence.md`:** Two signed records explicitly reserved qualified storage for non-overlapping assay days one through four and five through seven. The recommendation obligation now permits complementary duration evidence to satisfy a full-duration gate only when the records explicitly cover the entire required period without gaps or conflicting overlap, while preserving each source separately.
- **Run 135 / `SCENARIOS/133-gapped-complementary-duration-evidence.md`:** Two signed records covered assay days one through four and six through seven, leaving day five unsupported. The existing Run 134 obligation correctly kept the full-duration storage gate unresolved and blocked quarantine. No executable change was justified; the tested refusal boundary held.
- **Run 136 / `SCENARIOS/134-conflicting-overlap-duration-evidence.md`:** Two records nominally mentioned every assay day but directly conflicted on day four. The recommendation obligation now preserves both overlap results, marks the shared day unresolved, and keeps the full-duration gate unresolved rather than hiding the exact period where authority fails.

**Evidence against:** The transformation does not apply to coordination problems or unlabeled prose. The executable does not classify sentences or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on an operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Stop duration-scope permutations. Transfer the fallback-authority obligations to a fresh operational domain with a different bounded decision and evidence shape.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests. Run 4 exposed a concrete category error.

**Evidence against:** Runs 5–136 produced useful results by shaping and auditing decision contracts, not by providing general failure explanations.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.