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

## Run 1 — Manual test cycle

**What changed:** Added explicit `Decision:` and `Recommended action:` fields to `machine.py` reports. Updated `SCENARIOS/001-friendly.md` with the manual outcome. Updated H1 evidence and confidence.

**Why it changed:** The friendly scenario expected the report to pressure the agent toward a concrete next implementation step or toward weakening a hypothesis. The starter output had useful structure but its action pressure was still too soft; it could let future runs drift into feature accretion.

**Scenario tested:** `SCENARIOS/001-friendly.md`

**What was removed or rejected:** Rejected adding new modes, dashboard output, scoring, or configuration. The smallest scenario-tied improvement was a clearer decision/action layer on the existing report.

**What was learned:** H1 is alive but not proven. The system is useful as a pressure chamber only if it makes hypothesis movement explicit. The next test should be comparative: can this beat a plain checklist?

**Hypothesis movement:** H1 strengthened slightly from 0.30 to 0.32 because the scenario produced a concrete, fixable improvement. Confidence remains low because the output has not yet beaten a simpler baseline.
