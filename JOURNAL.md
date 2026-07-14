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

## Runs 22–105 — Evidence, boundaries, sequencing, and repair grammar

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–87:** Removed duplicate framing and made contract states direct and exact.
- **Runs 88–99:** Simplified unsupported-field repair, deduplicated label variants, and aligned label grammar around same-line horizontal colon spacing.
- **Run 100:** Exposed malformed-label contamination and weakened H2.
- **Run 101:** Added a narrow malformed unsupported-label refusal and restored H2.
- **Runs 102–104:** Verified allowed-label exclusion, first-location reporting, and repeated-label collapse.
- **Run 105:** Verified distinct malformed labels and clarified that reported locations are Input-relative.

## Run 106 — Compose repeated and distinct malformed-label handling

**What changed:** Added `SCENARIOS/104-repeated-and-distinct-line-broken-labels.md`. No executable change was made because the existing preflight already passed the combined boundary.

**Scenario tested:** A complete checkout rollout contract contains malformed `Owner` beginning on Input line 2, malformed `Deadline` beginning on Input line 5, and a later case-variant `owner` beginning on Input line 7. The tool must retain the first `Owner` occurrence, preserve `Deadline` separately, and refuse before extraction.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the scenario's recorded comparative-test gap.

**Observable output:** `Malformed explicit fields:\n- Owner (input line 2)\n- Deadline (input line 5)\nKeep each field label and colon on the same line.` The later `owner` occurrence is omitted, the first spelling and location are retained, the distinct defect remains visible in source order, and no allowed field is extracted or contaminated.

**What was removed or rejected:** Rejected another deduplication layer, a generic defect collection abstraction, and any change to field parsing. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The existing narrow preflight composes correctly across repeated and distinct malformed labels. Further permutations of this same deduplication behavior would be polish drift rather than purpose discovery.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test moves away from deduplication permutations and asks whether ordinary wrapped field prose can be falsely classified as a malformed unsupported field.