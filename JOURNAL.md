# Journal

Record every autonomous run here. Historical entries are compacted once their evidence is fully represented in `HYPOTHESES.md`; the latest primary-hypothesis run retains the full tested boundary and result.

## Runs 0–8 — From usefulness evaluator to explicit decision contract

- **Run 0:** Created the scaffold and rejected a dashboard, framework, or multi-tool architecture.
- **Run 1:** Added explicit decision and recommended-action output to the scenario harness.
- **Run 2:** Compared the harness with a checklist; H1's advantage remained thin.
- **Run 3:** Added one bounded-task transformation for vague input; H2 became the lead.
- **Run 4:** A collaboration transfer exposed a category error; H2 narrowed to decision support.
- **Run 5:** Added `decision_brief.py` and the four-field contract.
- **Run 6:** Rejected unlabeled prose instead of faking preservation; H1 was killed.
- **Runs 7–8:** Made rejection repairable and the no-inference boundary observable.

## Runs 9–21 — Transfer, interpretation, and gate boundaries

- **Runs 9–10:** Transferred the unchanged contract across editorial, commercial, and vendor decisions.
- **Runs 11–13:** Rejected unsupported fields and kept repairs inside the four-field schema.
- **Runs 14–17:** Preserved observations and conflicting interpretations without promoting them to fact; split dense obligations into inspectable requirements.
- **Runs 18–21:** Distinguished satisfied, violated, unresolved, and conflicting gates and required evidence for every judgment.

## Runs 22–34 — Evidence provenance, applicability, assumptions, and sensitivity

- **Run 22:** Kept independent constraint judgments separate.
- **Run 23:** Exposed shared provenance across multiple gate judgments.
- **Run 24:** Distinguished shared provenance from actual measurement coverage.
- **Run 25:** Kept overlapping measurements tied to the measurements they corroborate.
- **Run 26:** Preserved incompatible values instead of averaging them.
- **Run 27:** Allowed source exclusion only with an auditable comparability reason and visible excluded value.
- **Run 28:** Required supplied observations behind comparability claims.
- **Run 29:** Required direct observations rather than downstream interpretations.
- **Run 30:** Required evidence that an observed difference actually changes applicability to the target population.
- **Run 31:** Preserved original measurements and the supplied method behind a target-population reweighting.
- **Run 32:** Rejected adjusted estimates whose supplied notes omitted an auditable method.
- **Run 33:** Kept transparent adjusted estimates conditional when a governing assumption lacked supplied support.
- **Run 34:** Preserved threshold-crossing sensitivity ranges as explicit conditional boundaries.

## Run 35 — Resolve a threshold-clearing sensitivity range

**What changed:** Added `SCENARIOS/034-sensitivity-range-clears-gate.md` and tightened the fixed constraint requirement so a supplied supported sensitivity range entirely on one side of a gate is judged from the whole range. The analyst may not mark the gate unresolved merely because the evidence is a range.

**Scenario tested:** Historical observations supported a Monday Safari share between 15% and 22%. Combined with supplied Safari and non-Safari p95 measurements, the supplied adjustment produced a latency range of 454.5–484.6 milliseconds. The rollout limit was below 500 milliseconds and paid conversion was 23%.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario remains valid, maps `partial` to `hold-but-improve`, and recommends addressing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/034-sensitivity-range-clears-gate.md` preserves all four fields and now requires the full 454.5–484.6 millisecond range to govern the judgment. Every supported value is below 500 milliseconds, so the performance gate is satisfied and rollout is supported.

**What was removed or rejected:** No sensitivity engine, threshold calculator, range parser, source-ranking system, fifth field, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Uncertainty does not itself make a gate unresolved. When the supplied supported range stays wholly on one side of the threshold, the range can resolve the gate without choosing a midpoint or representative value.

**Hypothesis movement:** H2 strengthens from 0.98 to 0.99 and remains primary. The next test is a supported sensitivity range entirely above a maximum threshold, checking that the whole range can establish a violated gate.
