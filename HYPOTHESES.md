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

**Next test:** Do not lead the next implementation cycle. Keep only as supporting infrastructure while H2 is tested on a transfer scenario.

**Kill criterion:** Kill if the next transfer test shows the usefulness report adds no value beyond the bounded task itself.

## H2 — Narrow task-shaping assistant

**Status:** alive  
**Confidence:** 0.30

**Problem statement:** People with messy inputs need help turning them into a precise, testable task with an expected useful outcome.

**Specific user:** A nontechnical operator trying to give an agent or contractor a bounded task without accidentally requesting a vague dashboard or generic system.

**Evidence for:** The required scenario format forces user, situation, input, expected outcome, actual outcome, and what broke. Run 3 added executable vague-input detection and a `Bounded task` output. On the hostile scenario it converted a broad request for a flexible information platform into one observable decision-brief test without asking the human for direction.

**Evidence against:** The current bounded task is a fixed decision-brief default. It may fail outside messy-information and decision-support contexts, and it has not yet demonstrated transfer.

**Next test:** Create a transfer scenario in a different domain and test whether the bounded task remains useful. If not, narrow H2 specifically to shaping messy information into decision briefs.

**Kill criterion:** Kill if the system repeatedly asks for more detail, or if its bounded tasks remain generic or inappropriate across two transfer scenarios.

## H3 — Failure-mode explainer for small tools

**Status:** alive  
**Confidence:** 0.15

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests from the start.

**Evidence against:** The current repo has no real external tool under test except itself.

**Next test:** Wait until H2 has a transfer scenario; then judge whether the failure analysis contributes anything beyond task shaping.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.
