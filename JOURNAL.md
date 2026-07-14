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

## Runs 22–104 — Evidence, boundaries, sequencing, and repair grammar

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–87:** Removed duplicate framing and made contract states direct and exact.
- **Runs 88–99:** Simplified unsupported-field repair, deduplicated label variants, and aligned label grammar around same-line horizontal colon spacing.
- **Run 100:** Exposed malformed-label contamination and weakened H2.
- **Run 101:** Added a narrow malformed unsupported-label refusal and restored H2.
- **Runs 102–104:** Verified allowed-label exclusion, first-location reporting, and repeated-label collapse.

## Run 105 — Clarify distinct malformed-field locations

**What changed:** Added `SCENARIOS/103-distinct-line-broken-unsupported-labels.md`. Changed malformed-field repair items from `(line N)` to `(input line N)`.

**Scenario tested:** A complete checkout rollout contract contains two different malformed unsupported fields: `Owner\n:` beginning on Input line 2 and `Deadline\n:` beginning on Input line 5. The tool must refuse before extraction, preserve source order, and report both locations without implying that the numbers refer to whole-file lines.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness. `partial` still maps to `hold-but-improve`, and the recommended action still targets the scenario's recorded comparative-test gap.

**Observable output:** `Malformed explicit fields:\n- Owner (input line 2)\n- Deadline (input line 5)\nKeep each field label and colon on the same line.` The output contains two distinct repair items in source order, no merging, no schema expansion, no normalization of either split label, no field contamination, and no complete-contract result.

**What was removed or rejected:** Rejected whole-file line-number calculation, a generic source-location abstraction, semantic classification of `Owner` or `Deadline`, and changes to allowed-label parsing. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Distinct malformed schema defects were already preserved correctly. The useful executable improvement was precision: location scope must match the parser's actual coordinate system. A repair that says only `line N` is misleading when numbering begins inside an extracted block.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether one repeated malformed label retains only its first Input-relative location while another distinct malformed label remains separately visible.