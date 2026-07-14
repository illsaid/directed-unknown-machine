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

## Runs 22–94 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.
- **Runs 88–92:** Split unsupported-field refusal into unsupported labels, a compact allowed schema, and concise operator-directed remapping guidance; then clarified multiple distinct unsupported labels.
- **Run 93:** Added order-preserving, case-insensitive deduplication so repeated occurrences of one unsupported label produce one repair item while all source meanings remain untouched.
- **Run 94:** Verified case variants collapse under that same boundary without an executable change.

## Run 95 — Normalize spacing before an unsupported-label colon

**What changed:** Added `SCENARIOS/094-spaced-unsupported-label.md` and changed `unsupported_labels()` to trim each captured label before case-insensitive comparison and repair output. This is one executable normalization step tied only to the named hostile regression.

**Scenario tested:** A concrete checkout rollout contract supplies all four allowed fields plus `Owner: Growth team owns implementation.` and `Owner : Finance owns final approval.` The observable requirement is one `- Owner` repair item, no whitespace-variant duplicate, preservation of both source lines, no automatic field assignment, no recommendation, and no schema expansion.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The current executable was then simulated with `python decision_brief.py SCENARIOS/094-spaced-unsupported-label.md`: the regex captures `Owner` and `Owner `; trimming makes both keys `owner`; first-seen spelling remains `Owner`; `unsupported_template` emits one repair item and the fixed allowed-field guidance; missing-field checks, complete-contract output, audit requirements, and recommendation are not reached.

**What was removed or rejected:** Removed only insignificant edge whitespace from the internal label identity. Rejected changing the four-field parser, automatically remapping ownership meaning, introducing a fifth field, adding a whitespace mode, or altering the six audit operations. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Pre-colon spacing is presentation variation, not a distinct schema meaning. Trimming at the unsupported-label boundary improves exactness without classifying content or weakening refusal discipline.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether harmless spacing before the colon should also be accepted for an allowed label without weakening explicit-field detection.