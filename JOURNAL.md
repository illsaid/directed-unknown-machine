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

## Runs 22–87 — Evidence, boundaries, sequencing, and simplification

- **Runs 22–46:** Established provenance, applicability, adjustment, range, equality, conflict, equivalence, and precedence refusal boundaries.
- **Runs 47–62:** Consolidated those obligations into six audit operations without weakening them.
- **Runs 63–72:** Distinguished and ordered preservation, transformation, reconciliation, application, gate judgment, and recommendation.
- **Runs 73–80:** Tightened each requirement while preserving its tested refusal boundaries.
- **Runs 81–83:** Removed the duplicate sequence line, generic requirements wrapper, and generic opening title.
- **Runs 84–87:** Made complete, partial, wholly unlabeled, and missing-field contract states direct and exact.

## Run 88 — Let unsupported labels lead the refusal

**What changed:** Added `SCENARIOS/087-unsupported-fields-first.md`. Replaced the single-sentence unsupported-field error with a three-part refusal: `Unsupported explicit fields:` plus the actual unsupported labels, `Supported fields:` plus the unchanged four-field schema, and one instruction to preserve each extra meaning under the supported field matching its role. Missing-field handling, parsing, complete-contract output, the six audit operations, and all decision rules remain unchanged.

**Scenario tested:** A concrete checkout rollout contract supplies all four supported fields plus `Owner: Growth team.` The observable requirement is that refusal identify `Owner` first, preserve the four-field schema, retain the ownership meaning through remapping guidance, emit no recommendation, and add no fifth field or repair mode.

**Demo check:** Before changes, `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated from the unchanged historical harness: `partial` maps to `hold-but-improve`, and the recommended action still targets the recorded comparative-test gap. After changes, `python decision_brief.py SCENARIOS/087-unsupported-fields-first.md` was mentally simulated: unsupported-label detection finds `Owner`, exits through `unsupported_template`, and never reaches missing-field checks, complete-contract output, audit requirements, or recommendation.

**What was removed or rejected:** Removed the dense one-line unsupported-field refusal. Rejected automatic role classification, schema expansion, silently dropping ownership, a second repair mode, and changes to the established audit requirements. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** Unsupported-field repair needs three inspectable facts, not one compressed sentence: what is unsupported, what schema remains valid, and how to preserve the extra meaning without expanding that schema.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether the supported-schema line can be shortened without making schema preservation or remapping guidance ambiguous.