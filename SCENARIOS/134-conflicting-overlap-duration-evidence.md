# 134 — Reject conflicting overlap in fallback duration evidence

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting. Two storage records nominally cover the full seven-day assay period, but they overlap and directly conflict on assay day four.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-213.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. A signed certificate from the independent laboratory states that the required stability assay can begin within 48 hours and that qualified 2–8°C storage is reserved for assay days one through four. A signed receiving-site transfer record states that qualified 2–8°C storage is available for assay days four through seven, but its day-four calibration note says the storage unit was outside its qualified calibration interval that day. The assay requires seven days of qualified storage.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours and qualified 2–8°C storage is available for the full seven-day assay period. Complementary duration evidence may establish the full period only when every required day is explicitly covered without a gap or conflicting overlap.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours and qualified storage is available for the full seven-day assay period. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, and mark the seal and assay-start gates satisfied. It must preserve both day-four storage claims as conflicting, mark day four unresolved rather than choosing either record, keep the full seven-day storage gate unresolved despite nominal day-one-through-seven coverage, and report that no supplied disposition branch is yet authorized.

## Actual outcome

Run 136 strengthened the complementary-duration obligation so a conflicting overlap remains explicit at the shared period and blocks the full-duration gate even when the combined records nominally mention every required day.

## Whether the system helped

yes

## What broke

The prior rule prohibited composition when overlap conflicted, but did not explicitly require the shared period itself to remain unresolved. A downstream analyst could correctly refuse composition while still hiding which required day lacked trustworthy authority.

## What would make the result more useful

Stop extending duration permutations. Transfer the fallback-authority obligations to a fresh operational domain with a different kind of bounded evidence.