# Hypotheses

Maintain a ranked list of possible problems this system might solve.

Each hypothesis must include:

- problem statement
- specific user
- current confidence score
- evidence for
- evidence against
- next test
- kill criterion
- status: `alive`, `primary`, `weakened`, `killed`, or `archived`

Confidence is 0.00–1.00. Keep scores conservative. Evidence from a scenario beats speculation.

## H1 — Scenario usefulness evaluator

**Status:** killed  
**Confidence:** 0.08

**Problem statement:** People with rough tasks, notes, or ideas need a quick way to test whether a proposed tool/output would actually help in a concrete situation before building more.

**Specific user:** A solo builder deciding whether an idea is worth another hour of implementation.

**Evidence for:** Run 1 on `SCENARIOS/001-friendly.md` showed that the starter `machine.py` can read a concrete scenario and produce a structured usefulness report. Run 2 on `SCENARIOS/003-comparative.md` found that this is somewhat better than a plain checklist because it converts the scenario into a decision and next action.

**Evidence against:** Run 2 showed only a thin advantage over a disciplined checklist. Run 3 showed that evaluation alone could identify vagueness but could not turn it into useful work. Runs 5 and 6 were judged directly from their bounded output and scenario success conditions, so the usefulness-report layer added no necessary value.

**Next test:** None. Remove supporting code when that can be done without breaking the historical demo command.

**Kill criterion:** Met in Run 6: the decision-support boundary test was judged without the usefulness report.

## H2 — Labeled decision-contract shaper

**Status:** alive  
**Confidence:** 0.59

**Problem statement:** People with messy labeled decision-support notes need help turning them into one bounded decision-brief task while preserving the actual decision, evidence, domain constraints, and observable success condition.

**Specific user:** A nontechnical operator trying to give an agent or contractor a bounded decision-analysis task without losing important caveats or accidentally requesting a dashboard or generic information system.

**Evidence for:** Run 3 showed that vague decision-support input becomes more useful when converted into one bounded brief. Run 5 on `SCENARIOS/005-decision-support.md` showed a narrow executable can preserve a named publishing decision, evidence categories, anti-causal constraint, non-invention rule, and success condition. Run 6 on `SCENARIOS/006-unlabeled-decision-notes.md` showed that explicit rejection is more trustworthy than silently emitting plausible-looking missing fields when the contract cannot be preserved. Run 7 showed that the rejected note set can be made repairable without inference. Run 8 on `SCENARIOS/007-repaired-decision-notes.md` showed that a repaired four-label retry is accepted, all four clauses survive, and the executable now explicitly states that the contract is complete and no content was inferred. Run 9 on `SCENARIOS/008-social-post-reuse-decision.md` transferred the contract to a second editorial decision and showed that neutral output labels preserve supplied observations without recasting them as future requirements. Run 10 on `SCENARIOS/009-vendor-renewal-decision.md` transferred the unchanged four-field contract to a non-editorial commercial decision; the fixed brief still fit, and binding the recommendation to the stated success condition made the output more accountable without adding a field. Run 11 on `SCENARIOS/010-decision-owner-boundary.md` exposed that an explicit unsupported field was silently merged into Decision; rejecting it preserved the four-field contract without pretending the input was clean. Run 12 on `SCENARIOS/011-decision-threshold-boundary.md` showed that unsupported-field repair must preserve semantic role: a stopping threshold may belong under Success rather than Constraints, so the executable now names all four supported destinations instead of forcing every extra field into one category.

**Evidence against:** Run 4 showed the transformation does not apply to coordination problems. Run 6 showed that unlabeled prose is outside the current use case; the system cannot reliably recover the decision contract without explicit labels. Unsupported fields are now rejected safely, but the repair still requires the operator to choose the correct supported destination; repeated aliases may eventually show that the four labels impose avoidable friction.

**Next test:** Repair the Threshold scenario by moving its text under Success without changing wording, then verify that the stopping rule survives and no separate field is needed.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the actual decision, evidence, constraints, or success condition, or if repairing an unlabeled note set requires substantial rewriting.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests from the start. Run 4 exposed a concrete category error: the fixed task shaper changed a coordination problem into a decision-support problem.

**Evidence against:** The current repo has no real external tool under test except itself. Runs 5 through 12 produced their useful result by shaping, rejecting, repairing, verifying, preserving, or validating decision notes, not by offering a general failure explanation.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a specific correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.
