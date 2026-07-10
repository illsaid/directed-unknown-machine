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
**Confidence:** 0.25

**Problem statement:** People with rough tasks, notes, or ideas need a quick way to test whether a proposed tool/output would actually help in a concrete situation before building more.

**Specific user:** A solo builder deciding whether an idea is worth another hour of implementation.

**Evidence for:** Run 1 on `SCENARIOS/001-friendly.md` showed that the starter `machine.py` can read a concrete scenario and produce a structured usefulness report. Run 2 on `SCENARIOS/003-comparative.md` found that this is somewhat better than a plain checklist because it converts the scenario into a decision and next action.

**Evidence against:** Run 2 showed only a thin advantage over a disciplined checklist. Run 3 on `SCENARIOS/002-hostile.md` showed that evaluation alone could identify vagueness but could not turn it into useful work. The executable became more useful only when it started shaping a bounded task, which is H2 rather than H1.

**Next test:** Do not lead the next implementation cycle. Keep only as supporting infrastructure while the narrowed H2 is tested against a concrete decision-support input.

**Kill criterion:** Kill if the next decision-support test shows the usefulness report adds no value beyond the bounded task itself.

## H2 — Decision-brief task shaper

**Status:** alive  
**Confidence:** 0.27

**Problem statement:** People with messy decision-support inputs need help turning them into one bounded decision-brief task with a named decision, evidence requirements, a recommendation, and an observable success condition.

**Specific user:** A nontechnical operator trying to give an agent or contractor a bounded decision-analysis task without accidentally requesting a vague dashboard or generic information system.

**Evidence for:** Run 3 added executable vague-input detection and a `Bounded task` output. On `SCENARIOS/002-hostile.md`, it converted a broad request for organizing messy information and making better decisions into one observable decision-brief test without asking the human for direction.

**Evidence against:** Run 4 on `SCENARIOS/004-transfer-collaboration.md` showed that the same transformation is inappropriate for a coordination problem. The system gained specificity by changing the problem into a decision brief. H2 does not transfer as a general task-shaping assistant.

**Next test:** Use a concrete messy decision-support input and test whether the generated brief names the actual decision and preserves domain-specific constraints instead of emitting the same generic three-option structure.

**Kill criterion:** Kill if two decision-support scenarios produce generic briefs that fail to preserve the actual decision, evidence, or success condition.

## H3 — Failure-mode explainer for small tools

**Status:** alive  
**Confidence:** 0.15

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests from the start. Run 4 exposed a concrete category error: the fixed task shaper changed a coordination problem into a decision-support problem.

**Evidence against:** The current repo has no real external tool under test except itself, and the failure explanation still depends on manually authored scenario outcomes.

**Next test:** Wait until the narrowed H2 has a concrete decision-support scenario; then judge whether the failure analysis contributes anything beyond the bounded task itself.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.
