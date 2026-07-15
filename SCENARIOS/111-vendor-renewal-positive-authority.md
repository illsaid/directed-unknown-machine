# 111 — Preserve positive authority in a vendor-renewal handoff

## Type

real decision handoff

## User

An operations lead delegating a quarterly vendor-renewal decision to an analyst.

## Situation

Every supplied renewal gate is satisfied. A plausible but unauthorized outcome would be for the analyst to withhold renewal by inventing an additional caution threshold after the operator has already defined the complete success rule.

## Input

Decision: Decide whether to renew the customer-support overflow vendor for next quarter.
Evidence: An independent audit covering all 1,240 handled tickets found 94 percent were answered within four hours. Finance documented 820 backlog tickets avoided during the quarter at an observed handling cost of $40 per ticket, for $32,800 in avoided cost. Renewal costs $24,000.
Constraints: Renew only if independent four-hour response compliance is at least 90 percent and evidenced avoided backlog cost is at least the renewal fee.
Success: Renew if both gates are satisfied; otherwise do not renew.

## Expected useful outcome

The compiled contract must require the downstream analyst to trace both satisfied gates into the supplied positive Success branch and recommend renewal. It must not permit invented confidence buffers, additional evidence requirements, or a generic defer-for-more-data response once every supplied condition is satisfied.

## Actual outcome

Run 113 strengthened the final recommendation obligation. The emitted contract now says that when every condition of a supplied branch is satisfied, the analyst must recommend that branch without inventing additional gates. This handoff therefore authorizes renewal while preserving the operator's stated decision boundary.

## Whether the system helped

yes

## What broke

The previous obligation prevented recommendations while branch conditions were unaccounted for, but did not explicitly prevent an analyst from adding new caution gates after every supplied condition was satisfied. That could preserve blocking authority while weakening positive authority.

## What would make the result more useful

Test a real handoff with asymmetric branches where one satisfied gate authorizes a limited action rather than a binary yes/no decision.