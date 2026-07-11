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

## Runs 22–31 — Evidence provenance and source applicability

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

## Run 32 — Reject opaque adjusted estimates

**What changed:** Added `SCENARIOS/031-opaque-adjusted-estimate.md` and tightened the fixed constraint requirement so a supplied adjusted numeric result cannot resolve a gate unless the notes also supply an auditable adjustment method.

**Scenario tested:** A production-shadow test measured p95 latency at 430 milliseconds. A canary measured 560 milliseconds and had a different Safari mix. The notes reported a favorable 493-millisecond target-population estimate but omitted the browser-segment measurements, weights, calculation, and adjustment procedure. Paid conversion was 23%.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario remains valid, maps `partial` to `hold-but-improve`, and recommends addressing its recorded comparative-test gap. `python decision_brief.py SCENARIOS/031-opaque-adjusted-estimate.md` preserves all four fields and now explicitly requires the opaque 493-millisecond estimate to remain unresolved rather than treating it as sufficient evidence for rollout.

**What was removed or rejected:** No adjustment engine, source-ranking system, applicability classifier, traffic parser, threshold calculator, fifth field, or domain mode was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Preserving the original and adjusted values is not enough. A polished numeric transformation is still only a claim when the supplied notes omit the method needed to reproduce or inspect it. Transparency of the result does not substitute for transparency of the transformation.

**Hypothesis movement:** H2 strengthens from 0.95 to 0.96 and remains primary. The next test is a fully supplied adjustment method that depends on a disputed assumption, checking that auditable arithmetic does not promote an unsupported assumption to fact.
