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

## Runs 22–103 — Evidence, boundaries, sequencing, and repair grammar

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–99:** Simplified unsupported-field repair, deduplicated label variants, and aligned allowed and unsupported labels around same-line horizontal colon spacing.
- **Run 100:** Exposed that `Owner\n:` stayed outside explicit-label detection but was absorbed into Success; H2 confidence dropped to 0.98.
- **Run 101:** Added a narrow malformed unsupported-label preflight, closing the contamination failure and restoring H2 confidence to 0.99.
- **Run 102:** Verified that the preflight excludes allowed labels, preserving the established `Decision\n:` missing-field repair.
- **Run 103:** Added first-occurrence line numbers to malformed unsupported-label repairs and verified the refusal inside a complete contract.

## Run 104 — Collapse repeated malformed unsupported labels

**What changed:** Added `SCENARIOS/102-repeated-line-broken-unsupported-label.md`. No executable change was made because the existing `malformed_unsupported_labels()` implementation already combines case-insensitive deduplication with first-occurrence spelling and line-number retention.

**Scenario tested:** A complete checkout rollout contract contains `Owner` on input line 2 followed by a colon-start value line, then later repeats the same malformed field as lowercase `owner` on input line 5. The executable must refuse before extraction, report exactly one repair item using the first spelling and line number, and leave both ownership meanings outside the four allowed fields.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The decision-contract path was mentally simulated from `scenario_input()` and `malformed_unsupported_labels()`: the first fragment records key `owner` as `(Owner, 2)`; the lowercase repeat matches the same normalized key and is skipped; `main()` exits through `malformed_template()` before unsupported-label detection or field extraction.

**Observable output:** `Malformed explicit fields:\n- Owner (line 2)\nKeep each field label and colon on the same line.` There is no second `owner` item, no replacement with the later spelling or line number, no schema expansion, no normalization of either split label, no absorption into Decision, Evidence, Constraints, or Success, and no complete-contract output.

**What was removed or rejected:** Rejected adding another deduplication pass, changing the malformed-field grammar, reporting every duplicate occurrence, or modifying the allowed-label path. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The Run 103 location improvement composes correctly with the earlier deduplication boundary. A repair list should identify each distinct schema defect once, at its first occurrence, even when the unsupported meaning appears multiple times.

**Hypothesis movement:** H2 remains primary at 0.99. The repeated malformed-label regression passed without new code. The next test is whether two different malformed unsupported labels remain separately visible with their own first occurrence line numbers.