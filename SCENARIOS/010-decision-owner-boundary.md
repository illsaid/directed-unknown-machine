# 010 — Decision owner boundary

## Type

contract-boundary

## User

A product lead preparing a release recommendation for an executive approver.

## Situation

The team must decide whether to ship a major update this week or defer it, but the product lead can only recommend; the CTO owns the final release decision.

## Input

Decision: Recommend shipping the major update this week or deferring it.
Owner: The product lead prepares the recommendation; the CTO makes the final decision.
Evidence: The release candidate passed 184 automated tests; two known defects remain; the largest customer begins acceptance testing next Monday.
Constraints: Do not treat the recommendation as authorization to deploy; preserve the CTO approval boundary; do not invent defect severity.
Success: Recommend ship or defer, identify the decisive evidence, and state what the CTO must approve before deployment.

## Expected useful outcome

Do not silently merge the explicit Owner instruction into Decision or claim that the four-field contract is complete. Reject the unsupported field and tell the operator where its meaning belongs without inventing content.

## Actual outcome

Run 11 rejects the unsupported Owner field before shaping the brief and instructs the operator to preserve the approval boundary under Constraints.

## Whether the system helped

yes

## What broke

Before Run 11, the parser treated Owner as part of the Decision value because only the four supported labels ended a field. It then incorrectly reported a complete explicit contract.

## What would make the result more useful

Test another unsupported explicit field to determine whether rejection remains clearer than expanding the contract.