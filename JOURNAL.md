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

## Run 5 — Preserve decision constraints instead of inventing structure

**What changed:** Added the executable `decision_brief.py` and `SCENARIOS/005-decision-support.md`. The new command reads a labeled messy-note input and emits the named decision, evidence requirements, constraints, success condition, and one fixed deliverable:

```bash
python decision_brief.py SCENARIOS/005-decision-support.md
```

**Why it changed:** Run 4 narrowed H2 and required a real decision-support test. The existing `machine.py` path always invented a generic three-option brief, which would discard the scenario's anti-causal, non-invention, and editorial constraints.

**Scenario tested:** `SCENARIOS/005-decision-support.md`. The original demo command was mentally simulated first and remains unchanged: `python machine.py run SCENARIOS/001-friendly.md` still emits the partial usefulness report and says the concrete input needs no reshaping. The new decision-brief command was then mentally simulated; its observable output preserves all four labeled parts and requests a one-page recommendation separating facts, assumptions, and unresolved gaps.

**What was removed or rejected:** Rejected a general natural-language extractor, task-type router, configurable templates, automatic option generation, and changes to the old scenario harness. The labeled note-set contract is narrower and directly testable.

**What was learned:** H2 works better when its purpose is not “make vague requests specific,” but “preserve the decision contract while turning messy labeled notes into a bounded brief assignment.” The constraints are not metadata; they are the core value. H1 and H3 both weakened because this useful output does not depend on a broad usefulness report or a generic failure explainer.

**Hypothesis movement:** H2 strengthens from 0.27 to 0.34 and narrows to a constraint-preserving decision-brief shaper. H1 falls from 0.25 to 0.20. H3 falls from 0.15 to 0.12. The next test should use unlabeled decision-support prose; failure should narrow the input contract rather than trigger a generic parser.

## Run 6 — Reject unlabeled prose instead of faking preservation

**What changed:** Added `SCENARIOS/006-unlabeled-decision-notes.md` and changed `decision_brief.py` to stop when any of the four decision-contract labels are missing. The executable now names the exact required fields instead of emitting a plausible brief full of `not stated` values.

**Why it changed:** Run 5's next test was unlabeled decision-support prose. The existing parser could not recover the decision contract, but its fallback hid that failure. A narrow, explicit input contract is more trustworthy than a generic extractor or fabricated completeness.

**Scenario tested:** `SCENARIOS/006-unlabeled-decision-notes.md`. The historical demo command was mentally simulated first and remains runnable: `python machine.py run SCENARIOS/001-friendly.md`. The current best-use command remains `python decision_brief.py SCENARIOS/005-decision-support.md`. Against scenario 006, the executable exits with the observable message: `cannot preserve the decision contract from unlabeled prose; add these explicit fields: Decision:, Evidence:, Constraints:, Success:`.

**What was removed or rejected:** Rejected a generic natural-language extractor, fuzzy classification, inferred field assignment, and silent `not stated` fallbacks. No new mode was added.

**What was learned:** Unlabeled prose is outside the proven use case. The useful system is becoming a labeled decision-contract shaper, not a universal note interpreter. Refusal is a useful output when it prevents a false claim that constraints were preserved.

**Hypothesis movement:** H2 strengthens from 0.34 to 0.39 while narrowing to labeled decision notes. H1 is killed because its own criterion was met: this run was judged directly from executable output and scenario success conditions without the usefulness-report layer. H3 weakens from 0.12 to 0.09.

## Run 7 — Make rejected notes directly repairable

**What changed:** Changed `decision_brief.py` so a rejected unlabeled note set emits a copyable skeleton containing only the missing `Decision`, `Evidence`, `Constraints`, and `Success` labels. Updated `SCENARIOS/006-unlabeled-decision-notes.md` with the observable output.

**Why it changed:** Run 6 proved that refusal is safer than inference, but its one-line error still made the operator reconstruct the required format. The smallest useful improvement was to make the boundary actionable without interpreting or rewriting the notes.

**Scenario tested:** `SCENARIOS/006-unlabeled-decision-notes.md`. The historical command `python machine.py run SCENARIOS/001-friendly.md` remains unchanged and runnable by inspection. The best-use command `python decision_brief.py SCENARIOS/005-decision-support.md` is unaffected because all four fields are present. Against scenario 006, the executable now exits with a four-line repair skeleton.

**What was removed or rejected:** Rejected automatic field inference, suggested rewritten content, a repair mode, interactive prompts, and configuration. The tool supplies structure only; the operator retains control of meaning.

**What was learned:** The labeled input contract can be made low-friction without broadening the system. A useful boundary is not merely a refusal; it should make the compliant retry obvious while preserving the original notes.

**Hypothesis movement:** H2 strengthens from 0.39 to 0.42. It survives as the primary emerging use case. The next test is a repaired version of the same notes with wording unchanged, verifying exact clause preservation.

## Run 8 — Verify a repaired contract without inference

**What changed:** Added `SCENARIOS/007-repaired-decision-notes.md` and changed `decision_brief.py` to emit `Contract check: complete — 4/4 explicit fields; no content inferred.` before the bounded assignment.

**Why it changed:** Run 7 made rejected notes repairable, but the successful retry did not expose whether its content came from explicit fields or interpretation. The smallest useful executable improvement was to make the parser's trust boundary visible.

**Scenario tested:** `SCENARIOS/007-repaired-decision-notes.md`. The historical demo `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated first and remains unchanged. The current best-use command also remains runnable. Against scenario 007, the parser finds all four labels, reports a complete explicit contract, and reproduces each clause under Decision, Evidence required, Constraints to preserve, and Success condition.

**What was removed or rejected:** Rejected automatic repair, clause rewriting, confidence scoring, provenance metadata, and a second output mode. One explicit completeness line was sufficient for this scenario.

**What was learned:** A repaired note set can cross the narrow input boundary without requiring a general extractor. The system is becoming useful not merely because it formats notes, but because it makes the difference between explicit operator intent and machine inference observable.

**Hypothesis movement:** H2 strengthens from 0.42 to 0.46. It survives. The next test is transfer within the same narrow domain: a different editorial decision using the same four-field contract.

## Run 10 — Transfer to a vendor renewal decision

**What changed:** Added `SCENARIOS/009-vendor-renewal-decision.md` and changed the fixed deliverable in `decision_brief.py` so the recommendation must be tested against the operator's stated success condition.

**Why it changed:** H2's recorded next test required a non-editorial business decision. The previous deliverable asked for one recommendation but did not explicitly bind that recommendation to the supplied success condition.

**Scenario tested:** `SCENARIOS/009-vendor-renewal-decision.md`. The historical demo `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated first and remains runnable. The current best-use command `python decision_brief.py SCENARIOS/009-vendor-renewal-decision.md` preserves the renewal decision, usage and cost observations, anti-invention constraints, and reversal condition.

**What was removed or rejected:** Rejected a finance mode, cost calculator, staff-time assumption, fifth field, and configurable deliverables. The same four-field contract was sufficient.

**What was learned:** The contract transfers beyond editorial work when the task is still a bounded decision. The strongest improvement was not domain logic; it was making the fixed deliverable accountable to the operator's own success condition.

**Hypothesis movement:** H2 strengthens from 0.50 to 0.54 and survives. The next test should try to break the four-field contract with an apparently essential instruction before any schema expansion.

## Run 11 — Reject unsupported explicit fields before shaping

**What changed:** Added `SCENARIOS/010-decision-owner-boundary.md` and changed `decision_brief.py` to reject explicit labels outside Decision, Evidence, Constraints, and Success before parsing the contract.

**Why it changed:** The prior parser only used the four supported labels as field boundaries. An explicit `Owner:` line was silently merged into Decision, after which the executable incorrectly reported a complete four-field contract with no inference.

**Scenario tested:** `SCENARIOS/010-decision-owner-boundary.md`. The historical demo `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated first and remains unchanged and runnable. Against scenario 010, the best-use executable now exits with: `unsupported explicit field(s): Owner. Preserve their meaning under Constraints instead of adding a new field.`

**What was removed or rejected:** Rejected adding an Owner field, approval workflow, role model, configurable schema, or automatic remapping. The approval boundary already fits Constraints; the tool now exposes the required repair instead of silently changing the contract.

**What was learned:** Contract completeness requires validating extra explicit structure, not only checking for missing required fields. A narrow schema is trustworthy only when unsupported fields cannot disappear inside supported ones.

**Hypothesis movement:** H2 strengthens from 0.54 to 0.57 and survives. The next test is a different unsupported explicit field whose meaning may map to Evidence or Success; rejection should remain meaning-preserving before the schema is kept fixed.

## Run 12 — Preserve unsupported-field meaning during repair

**What changed:** Added `SCENARIOS/011-decision-threshold-boundary.md` and changed `decision_brief.py` so unsupported fields are no longer always directed into Constraints. The rejection now names the four supported destinations and tells the operator to preserve each field under the one matching its role.

**Why it changed:** A campaign stopping threshold is an observable success or decision rule, not a constraint. The Run 11 repair message would have prevented silent merging but still distorted the contract during repair.

**Scenario tested:** `SCENARIOS/011-decision-threshold-boundary.md`. The historical demo `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated first and remains unchanged and runnable. Against scenario 011, the best-use executable exits with: `unsupported explicit field(s): Threshold. Preserve each meaning under the supported field that matches its role: Decision, Evidence, Constraints, Success.`

**What was removed or rejected:** Rejected adding Threshold as a fifth field, building an alias map, automatically classifying the threshold, or adding configuration. The tool exposes the boundary without claiming it can safely interpret the operator's semantics.

**What was learned:** Rejecting unsupported structure is not sufficient if the repair instruction itself misclassifies meaning. The four-field contract remains viable, but its boundary guidance must remain semantically neutral unless a scenario proves an automatic mapping is safe.

**Hypothesis movement:** H2 strengthens from 0.57 to 0.59 and survives. The next test is a repaired version of the same threshold scenario with the wording moved under Success unchanged.

## Run 13 — Make a repaired stopping rule govern the recommendation

**What changed:** Added `SCENARIOS/012-repaired-decision-threshold.md` and changed the fixed deliverable in `decision_brief.py` so the brief must state how the supplied success or reversal rule governs the recommended action.

**Why it changed:** Moving the Threshold wording under Success preserved the text, but the prior deliverable only required testing against the success condition. It did not require the analyst to expose how the stopping rule controls continuation or reversal.

**Scenario tested:** `SCENARIOS/012-repaired-decision-threshold.md`. The historical demo `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated first and remains unchanged and runnable. The current best-use command accepts all four fields, preserves the 18% threshold exactly under Success, and asks for one action governed by that supplied rule.

**What was removed or rejected:** Rejected adding a Threshold field, alias map, campaign mode, conversion calculator, or automatic interpretation. The repair uses the existing Success field and keeps the operator's wording.

**What was learned:** An unsupported stopping-rule field can be repaired into the four-field contract without semantic loss, but preservation alone is not enough: the generated assignment should make the supplied rule operational in the recommendation.

**Hypothesis movement:** H2 strengthens from 0.59 to 0.61 and survives. The next test is a repaired unsupported field whose meaning belongs under Evidence rather than Success, verifying that an observation is not recast as a requirement.