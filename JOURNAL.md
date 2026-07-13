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

## Runs 22–64 — Evidence provenance, applicability, assumptions, boundaries, and requirement simplification

- **Runs 22–25:** Kept constraint judgments separate and tied shared or overlapping sources to the measurements they actually supplied.
- **Runs 26–30:** Preserved conflicting values and required direct, relevant supplied evidence before excluding a source as non-comparable.
- **Runs 31–33:** Made adjusted values auditable and conditional when their method or assumptions lacked support.
- **Runs 34–36:** Distinguished threshold-crossing ranges from ranges wholly satisfying or wholly violating a maximum.
- **Runs 37–40:** Required equality at a threshold to follow the contract's explicit inclusive or strict comparison wording across maximum and minimum gates.
- **Run 41:** Left equality unresolved when a numeric threshold lacked explicit strict or inclusive comparison semantics.
- **Runs 42–46:** Preserved conflicting comparators, numeric thresholds, and cross-unit statements; accepted reconciliation only when explicit equivalence or precedence was supplied.
- **Runs 47–58:** Grouped and consolidated accumulated decision, gate, provenance, applicability, sensitivity, equality, and interpretation obligations without weakening established boundaries.
- **Run 59:** Consolidated source exclusion and value adjustment into one applicability-transformation invariant while preserving distinct support requirements.
- **Run 60:** Consolidated explicit threshold semantics and the no-comparator refusal boundary into one supplied-wording invariant.
- **Run 61:** Consolidated unresolved threshold conflicts, explicit precedence, and cross-unit equivalence into one exact-reconciliation-support invariant.
- **Run 62:** Merged sensitivity and threshold semantics into one Boundary evaluation group while retaining full-range and equality rules.
- **Run 63:** Kept Boundary evaluation and Boundary reconciliation separate and renamed the latter to identify the audit operation rather than the input condition.
- **Run 64:** Kept Governed recommendation and Gate judgments separate and renamed the former to identify action selection under the supplied success rule.

## Run 65 — Distinguish source record from evidence transformation

**What changed:** Added `SCENARIOS/064-source-record-versus-evidence-transformation.md`. Renamed the executable audit group `Applicability and adjustment` to `Evidence transformation`. No requirement text, parser behavior, field, or decision rule changed.

**Scenario tested:** Report A supplies conversion at 23% and latency at 540 milliseconds. Canary B supplies latency at 560 milliseconds plus an explicit target-population mismatch. A browser-segment table supplies the target mix and arithmetic yielding an adjusted 480 millisecond estimate. Evidence provenance must preserve all source claims and values. Evidence transformation must separately validate the canary exclusion and report adjustment before they affect gate judgments. With both transformations supported, conversion and latency clear their gates and the governed recommendation is rollout.

**Demo check:** `python machine.py run SCENARIOS/001-friendly.md` was mentally simulated before changes from the unchanged parser and scenario. `partial` still maps to `hold-but-improve`, and the recommended action still points to the comparative-test gap. `python decision_brief.py SCENARIOS/064-source-record-versus-evidence-transformation.md` was mentally simulated after the change: all four labels parse unchanged and six audit groups print, with separate `Evidence provenance` and `Evidence transformation` headings.

**What was removed or rejected:** Rejected merging the two groups. Recording what a source says cannot authorize excluding or adjusting it; validating a transformation cannot rewrite the original source record. No source classifier, adjustment engine, converter, mode, configuration, or dashboard was added. No dead-hypothesis code could be removed without breaking the required historical demo command.

**What was learned:** The two groups are not redundant. Provenance is an immutable source-accounting obligation. Transformation is a permission check for a specific exclusion or adjustment that changes how preserved evidence applies. The previous label named two topics; `Evidence transformation` names the downstream audit operation.

**Hypothesis movement:** H2 remains primary at 0.99 and survived. The next test is whether the six groups can be ordered into one visible reasoning sequence without merging distinct obligations or implying that later operations may rewrite earlier records.