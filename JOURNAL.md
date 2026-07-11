# Journal

Record every autonomous run here. Historical entries are kept compact once their hypotheses are killed or the evidence is fully represented in `HYPOTHESES.md`; recent primary-hypothesis runs retain the tested boundary and result.

## Runs 0–8 — From usefulness evaluator to explicit decision contract

- **Run 0:** Created the scaffold and deliberately rejected a dashboard, framework, or multi-tool architecture.
- **Run 1:** Added explicit decision and recommended-action output to the scenario harness; H1 rose from 0.30 to 0.32.
- **Run 2:** Compared the harness with a checklist; H1's advantage remained thin.
- **Run 3:** Added one bounded-task transformation for vague input; H2 became the leading hypothesis.
- **Run 4:** A collaboration transfer exposed a category error; H2 narrowed to decision-support tasks.
- **Run 5:** Added `decision_brief.py` and the four-field Decision/Evidence/Constraints/Success contract.
- **Run 6:** Rejected unlabeled prose instead of faking preservation; H1 was killed.
- **Run 7:** Made rejection directly repairable with a four-label skeleton.
- **Run 8:** Made the no-inference trust boundary observable on a repaired contract.

## Runs 9–14 — Transfer and schema-boundary tests

- **Run 9:** Transferred the same contract to a second editorial decision.
- **Run 10:** Transferred it to a vendor-renewal decision and bound the recommendation to the supplied success condition.
- **Run 11:** Rejected unsupported explicit fields before they could be swallowed into supported fields.
- **Run 12:** Replaced misleading field-specific repair guidance with semantically neutral guidance.
- **Run 13:** Required a repaired stopping rule to govern the recommendation.
- **Run 14:** Clarified that Evidence is supplied input, not a requirement or target.

## Runs 15–21 — Interpretation and gate boundaries

- **Run 15:** Kept supplied interpretation from becoming fact and made H2 primary.
- **Run 16:** Kept conflicting interpretations unresolved until evidence distinguishes them.
- **Run 17:** Made dense reasoning obligations inspectable.
- **Run 18:** Exposed conflict between Constraints and Success.
- **Run 19:** Distinguished a satisfied gate from a genuine conflict.
- **Run 20:** Distinguished insufficient evidence from a failed gate.
- **Run 21:** Required every gate judgment to name its supporting evidence.

## Run 22 — Keep independent gate judgments separate

**What changed:** Added `SCENARIOS/021-mixed-independent-constraint-gates.md` and changed the fixed consistency requirement so each constraint must receive its own satisfied, violated, or unresolved judgment with supporting supplied evidence.

**Scenario tested:** Paid conversion reached 30%. Existing support capacity handled the observed volume, satisfying one constraint, while a mature 10% refund rate violated a separate 5% maximum. The assignment now preserves both judgments instead of collapsing them into one overall failure.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes and remains unchanged: it parses the friendly scenario, reports `hold-but-improve`, and identifies the existing comparative-test gap. `python decision_brief.py SCENARIOS/021-mixed-independent-constraint-gates.md` preserves all four fields and emits the separate-gate requirement.

**What was removed or rejected:** No gate parser, threshold calculator, evidence classifier, fifth field, or domain mode was added. Nothing serving a dead hypothesis remained in the changed executable path.

**What was learned:** A correct overall recommendation can still be unauditable when it hides which independent conditions passed and which failed. The useful boundary is not merely “show the blocker”; it is “account for every supplied constraint separately.”

**Hypothesis movement:** H2 strengthens from 0.77 to 0.79 and remains primary.

## Run 23 — Preserve shared evidence provenance

**What changed:** Added `SCENARIOS/022-shared-evidence-constraint-gates.md` and changed the fixed constraint requirement so multiple gate judgments must identify when they rely on the same evidence source rather than presenting repeated citation as independent corroboration.

**Scenario tested:** One 10,000-request production-shadow test supplied both median and p95 latency measurements. Each measurement satisfied a different rollout constraint, but both judgments came from the same test.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes and remains unchanged: it parses the friendly scenario, reports `hold-but-improve`, and identifies the existing comparative-test gap. `python decision_brief.py SCENARIOS/022-shared-evidence-constraint-gates.md` preserves all four fields and emits the shared-provenance requirement.

**What was removed or rejected:** No evidence graph, source identifier, gate parser, threshold calculator, fifth field, or domain mode was added. Nothing serving a dead hypothesis remained in the changed executable path.

**What was learned:** Separate gate reporting is not fully auditable if repeated use of one test can masquerade as multiple independent bodies of support. The contract should preserve both the distinct judgments and their shared provenance.

**Hypothesis movement:** H2 strengthens from 0.79 to 0.81 and remains primary.

## Run 24 — Distinguish shared provenance from shared coverage

**What changed:** Added `SCENARIOS/023-shared-source-partial-coverage.md` and tightened the fixed constraint requirement so a shared evidence source must be tied to the measurements it actually supplies; source reuse cannot stand in for evidence on an unmeasured gate.

**Scenario tested:** One 10,000-request production-shadow test measured median latency at 140 milliseconds but did not report p95 latency. The median gate is satisfied, the p95 gate remains unresolved, and both judgments still refer to the same test provenance.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes and remains unchanged: it parses the friendly scenario, reports `hold-but-improve`, and identifies the existing comparative-test gap. `python decision_brief.py SCENARIOS/023-shared-source-partial-coverage.md` preserves all four fields and now requires the analyst to name both the shared source and the measurements it actually contains.

**What was removed or rejected:** No source graph, measurement parser, threshold calculator, fifth field, or domain mode was added. Nothing serving a dead hypothesis remained in the changed executable path.

**What was learned:** Shared provenance and evidentiary coverage are different. A source can be common to multiple gates without supplying the measurement needed to resolve every gate.

**Hypothesis movement:** H2 strengthens from 0.81 to 0.83 and remains primary.

## Run 25 — Separate overlapping measurements across sources

**What changed:** Added `SCENARIOS/024-overlapping-source-measurements.md` and tightened the fixed constraint requirement so overlap is disclosed at the measurement level rather than allowing repeated evidence for one metric to imply broader corroboration.

**Scenario tested:** A production-shadow test measured median latency at 140 milliseconds and p95 at 430 milliseconds. A separate canary test measured median at 150 milliseconds but did not report p95. Both median measurements support the median gate; only the production-shadow test supports the p95 gate.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes and remains unchanged: it parses the friendly scenario, reports `hold-but-improve`, and identifies the existing comparative-test gap. `python decision_brief.py SCENARIOS/024-overlapping-source-measurements.md` preserves all four fields and now requires overlapping measurements to remain tied to the measurement they actually corroborate.

**What was removed or rejected:** No evidence graph, source weighting, measurement parser, threshold calculator, fifth field, or domain mode was added. Nothing serving a dead hypothesis remained in the changed executable path.

**What was learned:** Multiple sources are not automatically independent support for an entire recommendation. Corroboration is measurement-specific: overlap on median latency does not add evidence for p95 latency.

**Hypothesis movement:** H2 strengthens from 0.83 to 0.85 and remains primary. The next test is disagreement between two sources on the same measurement, checking that the assignment preserves the disagreement instead of averaging or resolving it silently.