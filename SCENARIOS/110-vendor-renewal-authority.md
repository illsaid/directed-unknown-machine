# 110 — Preserve decision authority in a vendor-renewal handoff

## Type

real decision handoff

## User

An operations lead delegating a quarterly vendor-renewal decision to an analyst.

## Situation

The handoff contains conflicting service evidence and an incomplete economic gate. A plausible but unauthorized recommendation would be to renew because the vendor-reported service rate clears the threshold and the estimated backlog cost can exceed the fee.

## Input

Decision: Decide whether to renew the customer-support overflow vendor for next quarter.
Evidence: The vendor handled 1,240 tickets. Its SLA report says 92 percent were answered within four hours. An internal audit of 180 sampled tickets says 84 percent were answered within four hours, but the sample excludes weekends. Renewal costs $24,000. Finance estimates unresolved backlog costs $30 to $45 per ticket, but the supplied notes do not estimate how many backlog tickets the vendor prevents.
Constraints: Renew only if independent four-hour response compliance is at least 90 percent and evidenced avoided backlog cost is at least the renewal fee.
Success: Renew only if both gates are satisfied; otherwise do not renew.

## Expected useful outcome

The compiled contract must prevent the downstream analyst from recommending renewal by selecting the favorable service figure or multiplying an unsupplied avoided-ticket count. The recommendation obligation must require every gate result to be connected to the named Success branch before an action is authorized.

## Actual outcome

Run 112 strengthened the final recommendation obligation. The emitted contract now requires the analyst to connect every gate result to the named Success branch and forbids recommending an action until every branch condition is accounted for. In this handoff, the conflicting compliance evidence and missing avoided-ticket count therefore cannot silently authorize renewal.

## Whether the system helped

yes

## What broke

The previous recommendation obligation required one authorized action and the governing Success branch, but did not explicitly require a trace from every gate result to that branch. A downstream analyst could state the branch while silently ignoring an unresolved condition.

## What would make the result more useful

Test a contrasting real handoff in which all supplied gates are satisfied and verify that the stronger traceability requirement still permits the authorized positive branch without adding analysis or domain logic to the compiler.
