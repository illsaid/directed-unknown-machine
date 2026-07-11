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

## Runs 22–30 — Evidence provenance and source applicability

- **Run 22:** Kept independent constraint judgments separate.
- **Run 23:** Exposed shared provenance across multiple gate judgments.
- **Run 24:** Distinguished shared provenance from actual measurement coverage.
- **Run 25:** Kept overlapping measurements tied to the measurements they corroborate.
- **Run 26:** Preserved incompatible values instead of averaging them.
- **Run 27:** Allowed source exclusion only with an auditable comparability reason and visible excluded value.
- **Run 28:** Required supplied observations behind comparability claims.
- **Run 29:** Required direct observations rather than downstream interpretations.
- **Run 30:** Required evidence that an observed difference actually changes applicability to the target population.

## Run 31 — Preserve original measurements behind reweighting

**What changed:** Added `SCENARIOS/030-reweighted-source-applicability.md` and tightened the fixed constraint requirement so an adjusted or reweighted value used to establish target-population applicability must preserve the original value and name the adjusted value, supplied method, and target population.

**Scenario tested:** A production-shadow test measured p95 latency at 430 milliseconds. A canary measured an unadjusted 560 milliseconds with 38% Safari traffic versus 24% in the Monday target mix. Supplied browser-segment measurements and a supplied reweighting calculation produced a 493-millisecond target-population estimate. Paid conversion was 23%.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes. The friendly scenario remains valid, maps `partial` to `hold-but-improve`, and points to its recorded comparative-test gap. `python decision_brief.py SCENARIOS/030-reweighted-source-applicability.md` preserves all four fields and now requires the original 560-millisecond result, adjusted 493-millisecond estimate, supplied reweighting method, and Monday US web target population to remain visible.

**What was removed or rejected:** No source-ranking system, automatic reweighting, applicability classifier, causal model, traffic parser, threshold calculator, fifth field, or domain mode was added. Historical journal detail already represented in `HYPOTHESES.md` was compacted.

**What was learned:** Relevance evidence must support positive resolution as well as rejection. A supplied adjustment can make a conflicting source applicable to the target population, but only if the original measurement and transformation remain inspectable; otherwise the adjustment becomes a hidden overwrite.

**Hypothesis movement:** H2 strengthens from 0.94 to 0.95 and remains primary. The next test is a supplied adjusted value with an incomplete method, checking that an opaque numeric adjustment cannot resolve the gate.
