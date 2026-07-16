# 131 — Preserve uncovered fallback duration

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting. The laboratory explicitly confirms assay-start capacity and qualified storage, but the storage reservation covers only five of the seven required assay days.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-210.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. A signed certificate from the independent laboratory states that the required stability assay can begin within 48 hours and that qualified 2–8°C storage is reserved for the first five days of the assay. The assay requires seven days of qualified storage. No evidence addresses storage for days six and seven.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours and qualified 2–8°C storage is available for the full seven-day assay period. Evidence covering only part of a required duration must not establish the uncovered remainder.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours and qualified storage is available for the full seven-day assay period. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, and mark the seal and assay-start gates satisfied. Storage must be separated into an established five-day period and an unresolved two-day remainder. Because the fallback requires qualified storage for all seven days, quarantine is not authorized.

## Actual outcome

Run 133 strengthened the recommendation obligation so evidence covering a shorter duration cannot satisfy a full-duration fallback gate. The first five days remain established, days six and seven remain unresolved, and no disposition branch is authorized.

## Whether the system helped

yes

## What broke

The prior rule rejected implied support but did not explicitly constrain otherwise explicit evidence to its stated duration. A downstream analyst could treat a five-day reservation as satisfying a seven-day storage gate.

## What would make the result more useful

Test two complementary records whose non-overlapping durations jointly cover the full required period.