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

**Status:** weakened  
**Confidence:** 0.20

**Problem statement:** People with rough tasks, notes, or ideas need a quick way to test whether a proposed tool/output would actually help in a concrete situation before building more.

**Specific user:** A solo builder deciding whether an idea is worth another hour of implementation.

**Evidence for:** Run 1 on `SCENARIOS/001-friendly.md` showed that the starter `machine.py` can read a concrete scenario and produce a structured usefulness report. Run 2 on `SCENARIOS/003-comparative.md` found that this is somewhat better than a plain checklist because it converts the scenario into a decision and next action.

**Evidence against:** Run 2 showed only a thin advantage over a disciplined checklist. Run 3 on `SCENARIOS/002-hostile.md` showed that evaluation alone could identify vagueness but could not turn it into useful work. Run 5 produced a useful bounded artifact without relying on the usefulness-report layer, further reducing H1's claim to primary value.

**Next test:** Do not lead implementation. Retain only while it helps compare shaped output with scenario expectations.

**Kill criterion:** Kill if the next decision-support test can be judged directly from its bounded output and scenario success condition without the usefulness report.

## H2 — Constraint-preserving decision-brief shaper

**Status:** alive  
**Confidence:** 0.34

**Problem statement:** People with messy decision-support notes need help turning them into one bounded decision-brief task while preserving the actual decision, evidence requirements, domain constraints, and observable success condition.

**Specific user:** A nontechnical operator trying to give an agent or contractor a bounded decision-analysis task without losing important caveats or accidentally requesting a dashboard or generic information system.

**Evidence for:** Run 3 showed that vague decision-support input becomes more useful when converted into one bounded brief. Run 5 on `SCENARIOS/005-decision-support.md` showed a narrower executable can preserve a named publishing decision, evidence categories, anti-causal constraint, non-invention rule, and success condition instead of substituting a generic three-option structure.

**Evidence against:** Run 4 on `SCENARIOS/004-transfer-collaboration.md` showed the transformation does not apply to coordination problems. Run 5 depends on labeled `Decision`, `Evidence`, `Constraints`, and `Success` sections; it has not shown that it can recover these reliably from unlabeled prose.

**Next test:** Use a second real decision-support scenario without explicit labels. If preservation fails, keep labeled note sets as an explicit input contract rather than adding a generic extractor.

**Kill criterion:** Kill if two decision-support scenarios produce briefs that lose the actual decision, evidence, constraints, or success condition. Narrow rather than generalize if unlabeled input fails.

## H3 — Failure-mode explainer for small tools

**Status:** alive  
**Confidence:** 0.12

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests from the start. Run 4 exposed a concrete category error: the fixed task shaper changed a coordination problem into a decision-support problem.

**Evidence against:** The current repo has no real external tool under test except itself, and Run 5's useful result came from shaping a decision task rather than explaining a failure.

**Next test:** Do not lead implementation. Reassess only if failure analysis contributes a specific correction the decision-brief shaper could not derive directly.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.
