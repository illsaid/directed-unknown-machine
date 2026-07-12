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

## Runs 22–33 — Evidence provenance, applicability, and assumptions

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

## Run 34 — Expose a threshold-crossing sensitivity boundary

**What changed:** Added `SCENARIOS/033-sensitivity-range-crosses-gate.md` and tightened the fixed constraint requirement so a supplied sensitivity range that crosses a gate must remain visible as a range with its decision boundary and conditional outcomes. The analyst may not choose a midpoint, best case, or convenient point estimate to resolve the gate.

**Scenario tested:** A production-shadow test measured p95 latency at 430 milliseconds. A canary measured 560 milliseconds and supplied Safari and non-Safari segment measurements. Historical observations supported a Monday Safari share between 20% and 30%, producing a supplied adjusted range of 476–519 milliseconds and a 500-millisecond threshold crossing at approximately 25.6% Safari. Paid conversion was 23%.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario remains valid, maps `partial` to `hold-but-improve`, and recommends addressing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/033-sensitivity-range-crosses-gate.md` preserves all four fields and now requires the 476–519 millisecond range, the supplied 25.6% Safari boundary, and the conditional outcome on each side to remain explicit. Because the supported range crosses the threshold and the actual Monday mix is not narrowed further, the gate remains unresolved and delay is supported.

**What was removed or rejected:** No sensitivity engine, threshold calculator, assumption classifier, source-ranking system, fifth field, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Supported uncertainty is not the same as missing evidence, but a supported range that spans both sides of a decision gate still cannot support one unconditional action. The useful output is the boundary itself: what must be true for the recommendation to change.

**Hypothesis movement:** H2 strengthens from 0.97 to 0.98 and remains primary. The next test is a supported sensitivity range entirely on one side of the threshold, checking that uncertainty does not automatically make a resolvable gate unresolved.
