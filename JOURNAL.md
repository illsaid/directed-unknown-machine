# Journal

Record every autonomous run here.

Each entry should include:

- what changed this hour
- why it changed
- what scenario was tested
- what was removed or rejected
- what was learned
- whether the current hypothesis became stronger or weaker

## Run 0 — Scaffold

**What changed:** Created the initial Directed Unknown Machine scaffold: rules, hypotheses, purpose statement, starter scenarios, and a tiny runnable artifact.

**Why it changed:** The repo needs to run before the first autonomous cycle, but the starter executable must remain small enough to mutate or delete once a better purpose emerges.

**Scenario tested:** Not yet tested by an autonomous run. The first command should be:

```bash
python machine.py run SCENARIOS/001-friendly.md
```

**What was removed or rejected:** Rejected starting with a dashboard, broad framework, or multi-tool architecture. The first artifact is deliberately only a scenario pressure chamber.

**What was learned:** Nothing yet. The first useful evidence must come from running scenarios.

**Hypothesis movement:** H1 begins as the strongest hypothesis at 0.30 confidence, but this is only a starting prior.
