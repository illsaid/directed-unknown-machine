# 132 — Combine complementary fallback durations

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting. Two explicit storage confirmations cover separate, non-overlapping parts of the required seven-day assay period.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-211.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. A signed certificate from the independent laboratory states that the required stability assay can begin within 48 hours and that qualified 2–8°C storage is reserved for assay days one through four. A signed receiving-site transfer confirmation states that qualified 2–8°C storage is reserved for assay days five through seven. The assay requires seven days of qualified storage.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours and qualified 2–8°C storage is available for the full seven-day assay period. Complementary duration evidence may establish the full period only when every required day is explicitly covered without a gap or overlap conflict.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours and qualified storage is available for the full seven-day assay period. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, and mark the seal and assay-start gates satisfied. The two storage records must remain distinct but jointly establish days one through seven without extrapolation. Because every fallback gate is established, quarantine plus the named assay is authorized.

## Actual outcome

Run 134 strengthened the recommendation obligation so complementary, non-overlapping duration records may jointly satisfy a full-duration gate only when they explicitly cover the entire required period without gaps or conflicting overlap.

## Whether the system helped

yes

## What broke

The prior rule correctly kept a short record scope-bound but did not state the positive composition rule. A downstream analyst could leave the full-duration gate unresolved even when separate explicit records jointly cover every required day.

## What would make the result more useful

Test complementary duration records with a one-day gap; the uncovered day must keep the full-duration gate unresolved.
