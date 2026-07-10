# Machine Rules

You are building a single-purpose tool whose purpose is not known at the start.

The goal is not to build a product, a framework, a dashboard, or a collection of utilities. The goal is to discover, through repeated implementation and testing, what specific real-world problem this system is becoming unusually good at solving.

## Hourly loop

Every autonomous run:

1. Observe the current system.
2. Read `README.md`, `MACHINE_RULES.md`, `HYPOTHESES.md`, `JOURNAL.md`, `WHAT_THIS_IS_FOR.md`, and the latest files in `SCENARIOS/`.
3. Run the current demo command before changing anything.
4. Pick one live hypothesis from `HYPOTHESES.md`.
5. Test it against one concrete scenario.
6. Improve the system to make that scenario work better, or weaken/kill the hypothesis if the fit is poor.
7. Remove or simplify anything that serves dead hypotheses.
8. Record what changed, what was tested, and whether the hypothesis survived.
9. Commit the change with a clear message.

## Hard rules

- The repo must always run.
- The system must always do something demonstrable.
- The repo must always have one command that demonstrates the current best use case.
- Every change must make the system more fit for a specific purpose, not merely more flexible or featureful.
- A new feature is not allowed unless tied to a named scenario.
- A scenario is not valid unless it has a concrete input and observable output.
- Do not build a generic framework.
- Do not build a dashboard unless the emerging problem clearly requires one.
- Do not optimize for optionality.
- Optimize for specificity.
- Prefer one excellent use case over ten plausible ones.
- Do not ask the human for direction.
- Surprise the human with what the system turns out to be good at.

## Anti-bloat rules

- If two consecutive runs improve different hypotheses, the weaker hypothesis must be killed, demoted, or explicitly marked `weakened`.
- Do not add a second mode when improving the first mode would better test the primary hypothesis.
- Do not add configuration unless a scenario proves the default is wrong.
- Do not add an abstraction until two concrete cases force it.
- Delete dead code, dead data, and dead scenarios aggressively.

## Commitment rule

For the first 24 hours, exploration is allowed.

After 24 hours, the system must choose one primary hypothesis.

After that, every change must either:

- strengthen the primary hypothesis,
- weaken it with evidence,
- replace it with a better hypothesis,
- or remove work that served a dead hypothesis.

## Required files

- `HYPOTHESES.md`
- `SCENARIOS/`
- `JOURNAL.md`
- `WHAT_THIS_IS_FOR.md`

## File update requirements

Every run must update:

- `JOURNAL.md`
- `HYPOTHESES.md` if confidence, status, evidence, next test, or kill criterion changed
- the tested scenario file, or a new scenario file
- `WHAT_THIS_IS_FOR.md` if at least 24 hours have passed since the last rewrite

Machine-readable run records in `RUNS/` are optional but recommended when they clarify what happened.
