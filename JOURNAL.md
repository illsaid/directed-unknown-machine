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

## Runs 22–102 — Evidence, boundaries, sequencing, and repair grammar

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

## Run 103 — Locate a malformed unsupported field inside the contract

**What changed:** Added `SCENARIOS/101-mid-contract-line-broken-unsupported-label.md`. Replaced the regex-only malformed-label capture with a same-line scan that retains the first occurrence line number. `malformed_template()` now reports malformed labels as `- <label> (line <n>)` while preserving the existing repair instruction.

**Scenario tested:** A complete checkout rollout contract places `Owner` on one line and `: Growth team owns implementation.` on the next line between Evidence and Constraints. The executable must refuse before extraction, identify `Owner` at input line 3, and avoid contaminating either neighboring allowed field.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The decision-contract path was mentally simulated after the change: `scenario_input()` yields the five input lines; the malformed scan matches `Owner` at zero-based index 2 because the following line begins with a colon; it records `(Owner, 3)`; and `main()` exits through `malformed_template()` before unsupported-label detection or field extraction.

**Observable output:** `Malformed explicit fields:\n- Owner (line 3)\nKeep each field label and colon on the same line.` The executable does not normalize the split label, infer a destination field, append ownership to Evidence, Constraints, or Success, or emit complete-contract output.

**What was removed or rejected:** Rejected broad structural parsing, semantic classification, schema expansion, and reporting neighboring field names. Replaced the narrower regex capture rather than adding a second malformed-label mechanism. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Placement becomes part of a useful repair once malformed structure appears inside a complete handoff. Retaining the first line number improves repairability without changing what counts as a field or asking the executable to interpret the unsupported meaning.

**Hypothesis movement:** H2 remains primary at 0.99. The malformed-label refusal survived the mid-contract placement test and became more actionable without broadening the grammar. The next test is whether repeated malformed occurrences of one unsupported label still collapse to one item while retaining the first occurrence line number.
