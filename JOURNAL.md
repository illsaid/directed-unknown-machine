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

## Run 2 — Comparative baseline check

**What changed:** Recorded the outcome of `SCENARIOS/003-comparative.md`, updated H1 evidence, and added a compact run record.

**Why it changed:** H1 needed a baseline check before confidence could rise.

**Scenario tested:** `SCENARIOS/003-comparative.md`

**What was removed or rejected:** Rejected adding a new mode before proving the existing report is clearly better than a simple checklist.

**What was learned:** The report is somewhat useful because it produces a decision and recommended action, but the advantage is thin. The system needs a vague-input test to see whether task shaping is actually the stronger purpose.

**Hypothesis movement:** H1 remains alive at 0.32 but does not strengthen.

## Run 3 — Hostile vague-input recovery

**What changed:** Added executable vague-input detection and a `Bounded task` field to `machine.py`. The hostile request now becomes one observable decision-brief test rather than a proposal for a flexible platform. Recorded the outcome in `SCENARIOS/002-hostile.md` and updated hypothesis rankings.

**Why it changed:** The prior system could diagnose that the input was vague but could not make it usable. The hostile scenario required recovery without asking the human for direction.

**Scenario tested:** `SCENARIOS/002-hostile.md`. The existing friendly demo was mentally re-run first; because its input is concrete, it retains the previous report behavior and now states that no reshaping is needed.

**What was removed or rejected:** Rejected a generic clarification engine, configuration options, multiple task templates, and a second command. One fixed bounded-task transformation is enough to test whether task shaping is the stronger purpose.

**What was learned:** The system became materially more useful only when it stopped merely evaluating and started producing a bounded task. The decision-brief default works for this hostile scenario but may be too narrow or too opinionated elsewhere.

**Hypothesis movement:** H1 is weakened from 0.32 to 0.25. H2 strengthens from 0.20 to 0.30 and becomes the leading live hypothesis. The next run must test transfer before adding another template.

## Run 4 — Transfer exposes category error

**What changed:** Added `SCENARIOS/004-transfer-collaboration.md` and mentally simulated the current executable against it. Narrowed H2 from a general task-shaping assistant to a decision-brief task shaper; confidence fell from 0.30 to 0.27.

**Why it changed:** Run 3 explicitly required a different-domain transfer test before adding another template. The collaboration scenario tests whether the fixed bounded-task transformation preserves the user's problem or merely forces every vague request into the same shape.

**Scenario tested:** `SCENARIOS/004-transfer-collaboration.md`. Before the test, the current demo command was mentally simulated: `python machine.py run SCENARIOS/001-friendly.md` still emits the existing partial usefulness report and correctly says the concrete friendly input needs no reshaping.

**What was removed or rejected:** Rejected adding a coordination template, task-type router, broader vague-term list, or configurable output modes. Those changes would turn one failed transfer into a generic framework.

**What was learned:** The decision-brief transformation does not transfer to a collaboration problem. It creates apparent specificity by changing the user's problem. The evidence supports a narrower purpose: shaping messy decision-support requests into bounded decision briefs, not shaping arbitrary vague tasks.

**Hypothesis movement:** H2 survives but weakens and narrows from 0.30 to 0.27. Its next test must use a real decision-support input and verify that the bounded task preserves the actual decision and domain constraints.
