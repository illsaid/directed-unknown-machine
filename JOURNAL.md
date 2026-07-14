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

## Runs 22–101 — Evidence, boundaries, sequencing, and simplification

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
- **Run 101:** Added a narrow malformed unsupported-label preflight, closing the contamination failure and restoring H2 confidence to 0.99.

## Run 102 — Preserve the allowed-label missing-field repair

**What changed:** Added `SCENARIOS/100-line-broken-allowed-label-regression.md`. No executable change was made because the existing Run 101 preflight already excludes all four allowed labels and the established same-line field grammar already yields the correct repair.

**Scenario tested:** A checkout rollout contract supplies `Decision` on one line and begins the next line with `: Decide whether...`, followed by canonical Evidence, Constraints, and Success fields. The executable must request `Decision:` as missing rather than classify the fragment as a malformed unsupported field or normalize it into a valid label.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The decision-contract path was mentally simulated against Scenario 100: `malformed_unsupported_labels()` captures the split label text but excludes it because `decision` is allowed; unsupported-label detection finds no same-line extra field; `labeled_value()` does not match `Decision\n:`; and `repair_template()` exits with `Missing explicit fields:\nDecision:`.

**What was removed or rejected:** Rejected changing the malformed preflight to include allowed labels, adding a generic structural-error category, or modifying field extraction. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The malformed-input boundary now has two precise repairs: broken unsupported labels are identified as malformed before extraction, while broken allowed labels remain missing required fields. Keeping those paths separate gives the operator the narrowest actionable correction and avoids parser generalization.

**Hypothesis movement:** H2 remains primary at 0.99. The Run 101 repair survived its immediate regression test. The next test is whether a malformed unsupported label placed between two allowed fields is refused before it can contaminate either neighboring value.
