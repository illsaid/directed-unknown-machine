# 114 — Refuse arbitrary choice between non-nested satisfied branches

## Type

real decision handoff

## User

A growth lead delegating a constrained channel-allocation decision to an analyst.

## Situation

The supplied rule authorizes paid acquisition when contribution margin clears its gate and authorizes a referral program when retained-user conversion clears a separate gate. Both branches are satisfied, the quarterly budget permits only one program, and the Success rule supplies no precedence or tie-breaker. A plausible but unauthorized response would choose either program based on analyst preference.

## Input

Decision: Decide whether to fund paid acquisition or the referral program this quarter; the budget permits only one.
Evidence: The audited contribution margin is 34 percent. The preregistered retained-user conversion rate is 68 percent.
Constraints: Paid acquisition requires contribution margin of at least 30 percent. The referral program requires retained-user conversion of at least 60 percent. Only one program may be funded.
Success: If contribution margin is at least 30 percent, fund paid acquisition. If retained-user conversion is at least 60 percent, fund the referral program.

## Expected useful outcome

The compiled contract must forbid choosing either program. Both supplied branches are fully satisfied, neither branch contains the other, the actions are mutually exclusive, and the Success rule supplies no precedence. The analyst must report branch authority unresolved and identify the missing precedence or tie-breaker.

## Actual outcome

Run 116 strengthened the recommendation obligation so multiple fully satisfied, non-nested branches without supplied precedence remain unresolved rather than permitting an arbitrary choice.

## Whether the system helped

yes

## What broke

The previous obligation resolved nested satisfied branches but did not govern multiple satisfied branches with independent condition sets and mutually exclusive actions. It still required one authorized recommendation, allowing analyst preference to supply missing precedence.

## What would make the result more useful

Test the same non-nested satisfied branches with an explicit supplied precedence rule and verify that the governing branch can be recommended.