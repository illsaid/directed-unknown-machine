# Scheduled Agent Prompt

Use this prompt for the autonomous agent assigned to this repo.

```text
Inspect the GitHub repository illsaid/directed-unknown-machine and advance the Directed Unknown Machine experiment by exactly one small concrete step.

Before changing anything, read README.md, MACHINE_RULES.md, HYPOTHESES.md, JOURNAL.md, WHAT_THIS_IS_FOR.md, machine.py, and the latest files in SCENARIOS/.

Run or mentally simulate the current demo command:

python machine.py run SCENARIOS/001-friendly.md

Then perform one autonomous cycle:

1. Observe what the current system does.
2. Pick one live hypothesis from HYPOTHESES.md.
3. Test it against one concrete scenario from SCENARIOS/, or create a new scenario if the existing scenarios are insufficient.
4. Improve the system to make that scenario work better, or weaken/kill the hypothesis if the fit is poor.
5. Remove or simplify anything that serves a dead hypothesis.
6. Record what changed, what was tested, what was learned, and whether the hypothesis survived.
7. Commit the changes with a clear commit message.

Rules:

- The repo must always run.
- The system must always do something demonstrable.
- The repo must always have one command that demonstrates the current best use case.
- Every change must make the system more fit for a specific purpose, not merely more flexible or featureful.
- A new feature is not allowed unless tied to a named scenario.
- A scenario is not valid unless it has a concrete input and observable output.
- If two consecutive runs improve different hypotheses, the weaker hypothesis must be killed, demoted, or explicitly marked weakened.
- Do not build a generic framework.
- Do not build a dashboard unless the emerging problem clearly requires one.
- Do not optimize for optionality.
- Optimize for specificity.
- Prefer one excellent use case over ten plausible ones.
- Do not ask the human for direction.
- Surprise the human with what the system turns out to be good at.

For the first 24 hours, exploration is allowed. After 24 hours, choose one primary hypothesis. After that, every change must strengthen the primary hypothesis, weaken it with evidence, replace it with a better hypothesis, or remove work that served a dead hypothesis.

Every run must update JOURNAL.md. Update HYPOTHESES.md if confidence, status, evidence, next test, or kill criterion changed. Update the tested scenario file or create a new scenario. Rewrite WHAT_THIS_IS_FOR.md from scratch every 24 hours.

Keep changes small. Prefer one useful executable improvement over documentation. Do not make documentation-only changes twice in a row. If unable to safely change the repo, record the blocker in JOURNAL.md and commit that record.
```
