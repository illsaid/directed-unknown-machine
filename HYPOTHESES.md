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

**Status:** primary  
**Confidence:** 0.75

**Problem statement:** People with messy labeled decision-support notes need help turning them into one bounded decision-brief task while preserving the actual decision, supplied evidence, domain constraints, and observable success condition.

**Specific user:** A nontechnical operator trying to give an agent or contractor a bounded decision-analysis task without losing important caveats, confusing interpretation with observation, or accidentally requesting a dashboard or generic information system.

**Evidence for:** Runs 3–5 showed that the system becomes useful when it stops evaluating vague requests and instead preserves one explicit decision contract. Run 6 established a trustworthy refusal boundary for unlabeled prose; Runs 7–8 made that boundary repairable and observable without inference. Runs 9–10 transferred the unchanged four-field contract across editorial and commercial decisions. Runs 11–13 showed that unsupported structure can be rejected and repaired under the correct existing field without schema expansion. Run 14 showed that observations can live under Evidence without becoming requirements. Run 15 showed that a mixed Evidence field can preserve operator interpretation without promoting it to fact. Run 16 on `SCENARIOS/015-conflicting-evidence-interpretations.md` showed that two incompatible interpretations can remain preserved and unresolved while the assignment requires them to be adjudicated only against supplied observations. Run 17 on `SCENARIOS/016-three-conflicting-interpretations.md` showed that three interpretations still fit the contract, but the accumulated one-line deliverable stopped being quickly inspectable; splitting the fixed obligations into five explicit requirements restored inspectability without classifying the evidence. Run 18 on `SCENARIOS/017-constraint-success-conflict.md` showed that the four fields can preserve a met success threshold alongside a constraint that blocks the implied action, provided the assignment explicitly requires the analyst to expose the conflict instead of silently overriding either field. Run 19 on `SCENARIOS/018-satisfied-constraint-success-gate.md` showed that supplied evidence can satisfy a constraint gate, and that the assignment must distinguish an ordinary satisfied gate from a genuine conflict rather than treating every Constraints/Success interaction as a blocker. Run 20 on `SCENARIOS/019-incomplete-constraint-success-gate.md` showed that a met performance threshold can coexist with an unresolved evidence gate; the assignment now names insufficient evidence as distinct from both a satisfied constraint and a violation.

**Evidence against:** Run 4 showed the transformation does not apply to coordination problems. Run 6 showed that unlabeled prose is outside the current use case. Unsupported fields still require the operator to choose the correct destination. The executable does not classify evidence sentence by sentence or detect semantic conflict automatically; it constrains the downstream analyst, so trust still depends on the operator being able to inspect the supplied fields and fixed reasoning obligations.

**Next test:** Test a gate that the supplied evidence directly violates, verifying that the assignment identifies a failed constraint without misdescribing it as missing evidence or internal conflict.

**Kill criterion:** Kill if two labeled decision-support scenarios still lose the actual decision, supplied evidence, constraints, or success condition, or if preserving the boundary requires automatic semantic classification of the notes.

## H3 — Failure-mode explainer for small tools

**Status:** weakened  
**Confidence:** 0.09

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests from the start. Run 4 exposed a concrete category error: the fixed task shaper changed a coordination problem into a decision-support problem.

**Evidence against:** The current repo has no real external tool under test except itself. Runs 5 through 20 produced their useful result by shaping, rejecting, repairing, preserving, bounding, clarifying, or consistency-checking decision notes, not by offering a general failure explanation.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a specific correction the decision-contract shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.