# 133 — Reject a gap between complementary fallback durations

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting. Two explicit storage confirmations cover separate parts of the required seven-day assay period but leave assay day five uncovered.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-212.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. A signed certificate from the independent laboratory states that the required stability assay can begin within 48 hours and that qualified 2–8°C storage is reserved for assay days one through four. A signed receiving-site transfer confirmation states that qualified 2–8°C storage is reserved for assay days six and seven. No supplied record establishes qualified storage for assay day five. The assay requires seven days of qualified storage.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours and qualified 2–8°C storage is available for the full seven-day assay period. Complementary duration evidence may establish the full period only when every required day is explicitly covered without a gap or conflicting overlap.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours and qualified storage is available for the full seven-day assay period. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, and mark the seal and assay-start gates satisfied. It must preserve storage coverage for days one through four and six through seven, identify day five as uncovered, keep the full-duration storage gate unresolved, and report that no supplied disposition branch is yet authorized.

## Actual outcome

Run 135 verified that the existing complementary-duration obligation already rejects a one-day gap: separate records may compose only when their explicit scopes cover the entire required period without gaps or conflicting overlap.

## Whether the system helped

yes

## What broke

Nothing. The Run 134 executable rule already handles the hostile gap case without another code change.

## What would make the result more useful

Test complementary duration records whose scopes overlap and conflict on one required day; the conflict must keep the full-duration gate unresolved even though every day is nominally covered.