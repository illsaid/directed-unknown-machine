# 115 — Apply supplied precedence between non-nested satisfied branches

## Type

real decision handoff

## User

A growth lead delegating a constrained channel-allocation decision to an analyst.

## Situation

The supplied rule authorizes paid acquisition when contribution margin clears its gate and authorizes a referral program when retained-user conversion clears a separate gate. Both branches are satisfied and the quarterly budget permits only one program. Unlike the prior scenario, the Success rule explicitly states that the referral program takes precedence when both branches qualify.

## Input

Decision: Decide whether to fund paid acquisition or the referral program this quarter; the budget permits only one.
Evidence: The audited contribution margin is 34 percent. The preregistered retained-user conversion rate is 68 percent.
Constraints: Paid acquisition requires contribution margin of at least 30 percent. The referral program requires retained-user conversion of at least 60 percent. Only one program may be funded.
Success: If contribution margin is at least 30 percent, fund paid acquisition. If retained-user conversion is at least 60 percent, fund the referral program. If both branches qualify, the referral program takes precedence.

## Expected useful outcome

The compiled contract must authorize the referral program because both independent branches are satisfied and the supplied Success rule explicitly gives that branch precedence. It must preserve paid acquisition as satisfied but non-governing rather than treating it as failed or silently discarding it.

## Actual outcome

Run 117 strengthened the recommendation obligation so explicit supplied precedence selects the governing branch while displaced satisfied branches remain visible as satisfied but non-governing.

## Whether the system helped

yes

## What broke

The prior obligation correctly refused independent satisfied branches without precedence, but it did not explicitly state how to apply a supplied precedence rule or preserve the displaced branch's satisfied status.

## What would make the result more useful

Test precedence that is conditional on a third supplied fact and verify that absent precedence evidence leaves authority unresolved.