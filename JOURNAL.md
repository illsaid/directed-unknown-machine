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

## Runs 22–92 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–92:** Split unsupported-field refusal into unsupported labels, a compact allowed schema, and concise operator-directed remapping guidance; then clarified multiple distinct unsupported labels.

## Run 93 — Collapse repeated unsupported labels

**What changed:** Added `SCENARIOS/092-repeated-unsupported-label.md`. In `unsupported_labels`, added order-preserving, case-insensitive deduplication so repeated occurrences of the same unsupported label produce one repair item. The first supplied spelling is retained. The scenario source, allowed schema, remapping instruction, missing-field repair, parsing of supported fields, complete-contract output, six audit operations, and decision rules remain unchanged.

**Scenario tested:** A concrete checkout rollout contract supplies all four allowed fields plus `Owner: Growth team owns implementation.` and `Owner: Finance owns final approval.` The observable requirement is that refusal report `Owner` once, preserve both source meanings in the untouched notes, require manual remapping, emit no recommendation, add no fifth field, and perform no automatic assignment.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/092-repeated-unsupported-label.md` was mentally simulated: unsupported-label detection sees both `Owner` occurrences, keeps the first spelling, collapses the duplicate key, exits through `unsupported_template`, and emits one `- Owner`, the unchanged allowed-field list, and the unchanged remapping instruction. It never reaches missing-field checks, complete-contract output, audit requirements, or recommendation.

**What was removed or rejected:** Removed duplicate reporting of the same schema violation. Rejected collapsing distinct unsupported labels, deleting or rewriting either ownership meaning, automatic semantic classification, schema expansion, a second repair mode, and any change to the audit requirements. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Repeated label bullets do not preserve repeated meanings; the original notes do. Reporting the unsupported label once is therefore more exact: it identifies the schema defect without implying that identical label names are separate field types. Order-preserving deduplication retains the operator's original spelling and leaves all source meanings available for manual remapping.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether case variants such as `Owner:` and `owner:` should collapse while preserving the first supplied spelling.