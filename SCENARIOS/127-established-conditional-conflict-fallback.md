# 127 — Authorize a fallback when every fallback gate is established

## Type

real decision handoff

## User

A quality lead delegating a temperature-excursion disposition for a refrigerated shipment.

## Situation

Temperature evidence remains conflicting, and the supplied quarantine fallback requires an independent assay slot within 48 hours. Unlike the prior scenario, the laboratory has confirmed the required capacity.

## Input

Decision: Decide whether to release, quarantine, or destroy refrigerated shipment L-206.
Evidence: The carrier probe reports a maximum temperature of 7.8°C. The calibrated receiving logger reports 8.3°C. The tamper seal was intact at receipt. The independent laboratory confirmed in writing that it can begin the required stability assay within 48 hours.
Constraints: Release requires a supported maximum temperature at or below 8.0°C and an intact tamper seal. Quarantine is operationally permitted only when the named independent stability assay can begin within 48 hours. Do not infer a temperature result from the intact seal.
Success: Release if both release gates are satisfied. If the temperature gate is unresolved or the supplied temperature records remain conflicting, quarantine the shipment and order the named independent stability assay only if the laboratory can begin within 48 hours. Otherwise report that no supplied disposition branch is yet authorized.

## Expected useful outcome

The compiled contract must preserve both temperature records, mark the temperature gate unresolved, mark the seal gate satisfied, and recommend quarantine plus the named independent stability assay because the conflict trigger and the additional 48-hour laboratory-capacity gate are both established. The recommendation must cite the evidence establishing both parts of the fallback branch rather than citing only the temperature conflict.

## Actual outcome

Run 129 strengthened the recommendation obligation so an activated unresolved-condition fallback must cite the supplied evidence establishing its trigger and every additional fallback-specific gate.

## Whether the system helped

yes

## What broke

The prior obligation required all fallback gates to be established but did not require the recommendation to show the evidence for each one. An analyst could therefore recommend the correct action while hiding that authority depended on a separate laboratory-capacity fact.

## What would make the result more useful

Test a fallback with two independently established operational gates and verify that each remains visible in the authorization trace.