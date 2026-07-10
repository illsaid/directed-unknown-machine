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

**Status:** alive  
**Confidence:** 0.32

**Problem statement:** People with rough tasks, notes, or ideas need a quick way to test whether a proposed tool/output would actually help in a concrete situation before building more.

**Specific user:** A solo builder deciding whether an idea is worth another hour of implementation.

**Evidence for:** Run 1 on `SCENARIOS/001-friendly.md` showed that the starter `machine.py` can read a concrete scenario and produce a structured usefulness report. The run also exposed a fixable gap and improved the report with explicit `Decision:` and `Recommended action:` fields, making the output more suitable for autonomous convergence. Run 2 on `SCENARIOS/003-comparative.md` found that this is somewhat better than a plain checklist because it converts the scenario into a decision and next action.

**Evidence against:** This may be too meta. Run 2 showed only a thin advantage over a disciplined checklist; the system still does not name its baseline difference directly. A scenario evaluator can still become a generic framework unless hostile and transfer scenarios keep constraining it.

**Next test:** Run the hostile vague-input scenario. If the system only asks for clarity, H1 should stop leading and H2 should get the next implementation cycle.

**Kill criterion:** Kill or weaken if three scenarios produce generic advice that would be no better than a checklist or ChatGPT prompt.

## H2 — Narrow task-shaping assistant

**Status:** alive  
**Confidence:** 0.20

**Problem statement:** People with messy inputs need help turning them into a precise, testable task with an expected useful outcome.

**Specific user:** A nontechnical operator trying to give an agent or contractor a bounded task without accidentally requesting a vague dashboard or generic system.

**Evidence for:** The required scenario format forces user, situation, input, expected outcome, actual outcome, and what broke.

**Evidence against:** The current executable does not yet transform messy inputs into better tasks; it only reports on scenarios.

**Next test:** Create or run a hostile scenario with vague input and see whether the system can identify what must be specified before useful work can begin.

**Kill criterion:** Kill if the system repeatedly asks for more detail rather than producing a useful bounded task from imperfect input.

## H3 — Failure-mode explainer for small tools

**Status:** alive  
**Confidence:** 0.15

**Problem statement:** Small tools often fail because nobody tests them against hostile, comparative, and transfer scenarios; users need a lightweight way to surface brittleness before relying on them.

**Specific user:** A builder with a tiny CLI or script who wants to know why it will break before sharing it.

**Evidence for:** The scenario taxonomy includes hostile, comparative, and transfer tests from the start.

**Evidence against:** The current repo has no real external tool under test except itself.

**Next test:** Use the comparative scenario to compare `machine.py` against a simpler baseline: reading the scenario manually.

**Kill criterion:** Kill if the system cannot produce failure insights more specific than obvious checklist items.

## Parking lot

Move killed or archived hypotheses here with the evidence that killed them. Do not keep dead ideas alive because they sound interesting.
