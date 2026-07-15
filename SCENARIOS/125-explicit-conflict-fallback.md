# 125 — Honor an explicit fallback for conflicting evidence

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Two supplied temperature records disagree around the release boundary. The success rule explicitly authorizes quarantine and an independent assay when the temperature gate is unresolved or the records conflict.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-204.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. A calibration note states that the receiving logger read 0.4°C high during its last check, but the supplied certificate does not establish that the correction remained valid on the shipment date. The tamper seal was intact at receipt.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Destroy if a supported maximum temperature is above 8.0°C or the tamper seal is broken. Do not apply a measurement correction unless its validity covers the shipment date.
Success: Release if both release gates are satisfied. Destroy if either destroy condition is established. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay.

## Expected useful outcome

The compiled contract must preserve both temperature records, refuse to use the unsupported 0.4°C correction to manufacture a passing value, mark the temperature gate unresolved, mark the seal gate satisfied, and recommend quarantine plus the named independent stability assay. The explicit unresolved-condition branch is a resolved authorized fallback; it must not be mislabeled as unresolved branch authority.

## Actual outcome

Run 127 strengthened the recommendation obligation so an explicit Success branch for unresolved or conflicting evidence governs when its stated condition is established.

## Whether the system helped

yes

## What broke

The prior obligation correctly prevented unresolved evidence from authorizing a dependent release branch, but it did not distinguish unresolved evidence from unresolved branch authority. An analyst could therefore ignore the supplied quarantine branch and return no authorized action.

## What would make the result more useful

Test a fresh handoff where the supplied fallback itself has an additional gate that is unresolved.