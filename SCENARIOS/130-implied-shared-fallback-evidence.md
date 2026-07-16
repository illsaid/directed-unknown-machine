# 130 — Reject implied support for a second fallback gate

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting. One laboratory certificate explicitly confirms assay-start capacity but only suggests, without stating, that qualified storage may be available for the full assay period.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-209.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. A signed certificate from the independent laboratory states that the required stability assay can begin within 48 hours. The certificate also says the laboratory routinely handles refrigerated stability work, but it does not state that qualified 2–8°C storage is available or reserved for the full seven-day assay period.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours and qualified 2–8°C storage is available for the full seven-day assay period. A record that explicitly supports one operational gate must not satisfy a second gate merely because its wording makes that gate seem likely.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours and qualified storage is available for the full assay period. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, mark the seal gate satisfied, and mark assay-start capacity satisfied. Qualified storage must remain unresolved because routine refrigerated work only implies, rather than explicitly establishes, storage availability for this shipment and period. No disposition branch is yet authorized.

## Actual outcome

Run 132 strengthened the recommendation obligation so a record that explicitly supports one fallback gate cannot satisfy another gate by implication. The implied storage gate remains unresolved, so quarantine is not authorized.

## Whether the system helped

yes

## What broke

The prior rule prohibited silent evidence reuse unless a record explicitly supported both gates, but it did not state the observable consequence when the second relationship was merely implied. A downstream analyst could still treat suggestive wording as explicit dual support.

## What would make the result more useful

Test an explicit storage-capacity statement whose time scope is shorter than the required assay period.