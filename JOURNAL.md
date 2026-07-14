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

## Runs 22–100 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–92:** Split unsupported-field refusal into unsupported labels, a compact allowed schema, and concise operator-directed remapping guidance; then clarified multiple distinct unsupported labels.
- **Run 93:** Added order-preserving, case-insensitive deduplication so repeated occurrences of one unsupported label produce one repair item while all source meanings remain untouched.
- **Run 94:** Verified case variants collapse under that same boundary without an executable change.
- **Run 95:** Normalized harmless pre-colon spacing during unsupported-label identity checks, so `Owner:` and `Owner :` produce one repair item without changing the schema or either source meaning.
- **Run 96:** Accepted horizontal spacing before an allowed-label colon and kept next-field boundaries consistent, so `Decision :` reaches complete-contract output rather than a false missing-field refusal.
- **Run 97:** Restricted colon padding to spaces and tabs, so `Decision\n:` is refused as a missing explicit field while same-line spacing remains accepted.
- **Run 98:** Verified that an allowed label followed by a tab and colon remains accepted without reopening the multiline-label boundary.
- **Run 99:** Applied the same horizontal-spacing grammar to unsupported labels, so `Owner\t:` is refused instead of being absorbed into Success.
- **Run 100:** Exposed that `Owner\n:` stayed outside explicit-label detection but was then absorbed into Success; H2 confidence dropped to 0.98 pending a narrow refusal.

## Run 101 — Refuse malformed unsupported labels before extraction

**What changed:** Added `malformed_unsupported_labels()` and a compact malformed-field refusal to `decision_brief.py`. The check matches only an unsupported label-only line immediately followed by a colon-start line. Updated `SCENARIOS/099-line-broken-unsupported-label.md` with the passing observable result.

**Scenario tested:** A complete checkout rollout contract supplies all four allowed fields, followed by `Owner` on one line and `: Growth team owns implementation.` on the next. The executable must refuse this structure before complete-contract output without normalizing it into a valid label, absorbing it into Success, inferring a destination, or expanding the schema.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The new decision-contract path was mentally simulated against Scenario 099: `malformed_unsupported_labels` captures `Owner`, excludes the four allowed labels, and exits with `Malformed explicit fields:\n- Owner\nKeep each field label and colon on the same line.` before unsupported-field detection or field extraction.

**What was removed or rejected:** Rejected broad multiline-label normalization, a generic malformed-input parser, automatic remapping, and changes to `labeled_value`. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The preservation boundary needs a small preflight for malformed unsupported field structure, separate from the valid explicit-label grammar. Keeping allowed labels out of that check closes the contamination failure while preserving the established `Decision\n:` missing-field behavior.

**Hypothesis movement:** H2 remains primary and returns from 0.98 to 0.99 because the specific Run 100 failure is now refused without semantic classification or schema expansion. The next test is to verify that a line-broken allowed label still follows the existing missing-field refusal.