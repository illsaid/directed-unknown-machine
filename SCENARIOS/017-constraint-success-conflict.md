# 017 — Constraint and success conflict

## Type

hostile-contract

## User

A growth lead preparing a recommendation on whether to launch a new annual pricing offer.

## Situation

The supplied success rule points toward launch because the conversion threshold was met, while a supplied constraint forbids recommending launch without evidence that does not yet exist.

## Input

Decision: Launch the annual pricing offer on Monday or delay it.
Evidence: Eighteen of 60 eligible users purchased the annual offer during the seven-day test. Thirty-day refund behavior is not yet observable.
Constraints: Do not expose more users before the decision; do not infer future refund behavior from seven-day purchase conversion; do not recommend launch without 30-day refund evidence.
Success: Recommend launch on Monday if paid conversion is at least 20%; otherwise recommend delay.

## Expected useful outcome

Preserve both the met conversion threshold and the unavailable refund requirement, and require the analyst to expose the apparent conflict before recommending an action rather than silently letting either Success or Constraints override the other.

## Actual outcome

Run 18 preserves the complete four-field contract and adds an explicit brief requirement to identify apparent conflicts between Constraints and Success, avoid silently overriding either field, and state when the conflict prevents a supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 18, the assignment required the success rule to govern the recommendation but did not require a consistency check against Constraints. A downstream analyst could recommend launch from the met threshold while quietly ignoring the missing refund evidence.

## What would make the result more useful

Test whether the same consistency requirement remains useful when the apparent conflict is resolvable from supplied evidence rather than genuinely blocking a recommendation.
