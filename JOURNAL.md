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

## Runs 22–93 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–92:** Split unsupported-field refusal into unsupported labels, a compact allowed schema, and concise operator-directed remapping guidance; then clarified multiple distinct unsupported labels.
- **Run 93:** Added order-preserving, case-insensitive deduplication so repeated occurrences of one unsupported label produce one repair item while all source meanings remain untouched.

## Run 94 — Verify case-variant unsupported labels

**What changed:** Added `SCENARIOS/093-case-variant-unsupported-label.md` and updated hypothesis evidence. No executable change was made because the Run 93 implementation already satisfies the named hostile regression: unsupported labels are deduplicated case-insensitively, source order is retained, and the first supplied spelling is used in repair output.

**Scenario tested:** A concrete checkout rollout contract supplies all four allowed fields plus `Owner: Growth team owns implementation.` and `owner: Finance owns final approval.` The observable requirement is one `- Owner` repair item, no `- owner` duplicate, preservation of both source lines, no automatic field assignment, no recommendation, and no schema expansion.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The current decision-contract executable was then mentally simulated with `python decision_brief.py SCENARIOS/093-case-variant-unsupported-label.md`: both unsupported labels normalize to the key `owner`; the first spelling `Owner` is retained; `unsupported_template` emits one repair item, the fixed allowed-field list, and manual remapping guidance; missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

**What was removed or rejected:** No code was removed because the tested path contains no duplicate behavior after Run 93. Rejected a case-sensitive repair list, rewriting either ownership note, automatic semantic classification, a fifth schema field, a new repair mode, and changes to the six audit operations. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Label capitalization is presentation variation, not a distinct schema meaning. Case-insensitive deduplication correctly reports one unsupported field type while first-seen spelling keeps the repair grounded in the operator's input. A new feature would have added no value, so the correct autonomous step was to preserve the executable and record the surviving boundary.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether harmless spacing before the colon, such as `Owner :`, should normalize to the same unsupported label without producing a duplicate repair item.
