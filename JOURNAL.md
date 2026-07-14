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

## Runs 22–98 — Evidence, boundaries, sequencing, and simplification

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

## Run 99 — Detect tabbed unsupported labels before field extraction

**What changed:** Added `SCENARIOS/098-tabbed-unsupported-label.md` and changed the unsupported-label regex from `[A-Za-z ]*` to `[A-Za-z \t]*`. This applies the same horizontal-spacing tolerance already used by allowed-field parsing while continuing to exclude line breaks.

**Scenario tested:** A complete checkout rollout contract supplies the four allowed fields plus `Owner\t: Growth team owns implementation.` The observable requirement is an unsupported-field refusal containing one `- Owner`, the unchanged four-field schema, and operator-directed remapping guidance. Complete-contract output must not be reached and the ownership meaning must not be absorbed into Success.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` still maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. The decision-contract executable was also mentally simulated before and after the change. Before Run 99, `Owner\t:` did not match unsupported-label detection and remained inside the captured Success value. After Run 99, the line matches the horizontally bounded explicit-label grammar, trims to `Owner`, and exits through `unsupported_template` before field extraction.

**What was removed or rejected:** Rejected broad `\s` tolerance, multiline labels, fuzzy repair, automatic assignment of Owner to another field, a fifth schema field, and a new parser mode. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Allowed- and unsupported-label validation must share the same same-line horizontal-spacing boundary. Otherwise an extra labeled meaning can bypass the refusal layer and silently contaminate a supported field value. One character-class change closes that gap without broadening the contract.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether a line break before an unsupported-label colon remains outside the explicit-field grammar rather than being normalized as horizontal spacing.
