# 129 — Permit one record to support two named fallback gates

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting. One signed facility certificate explicitly confirms both required operational capabilities for the quarantine fallback.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-208.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. A signed certificate from the independent laboratory states both that the required stability assay can begin within 48 hours and that its qualified 2–8°C chamber is reserved for the full seven-day assay period.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours and qualified 2–8°C storage is available for the full seven-day assay period. A single record may support multiple operational gates only when it explicitly states each supported capability.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours and qualified storage is available for the full assay period. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, mark the seal gate satisfied, and recommend quarantine plus the named independent stability assay. The authorization trace may cite the signed laboratory certificate for both operational gates only because the record explicitly supports assay start within 48 hours and qualified storage for seven days.

## Actual outcome

Run 131 verified that the existing recommendation obligation permits one supplied record to support multiple fallback gates only when the record explicitly supports both. The compiled contract reaches complete-contract output without weakening the independent-evidence boundary added in Run 130. No executable change was justified.

## Whether the system helped

yes

## What broke

Nothing. The Run 130 rule already distinguishes explicit dual support from silent evidence reuse.

## What would make the result more useful

Test one record that supports one fallback gate explicitly and a second only by implication; the implied gate must remain unresolved.