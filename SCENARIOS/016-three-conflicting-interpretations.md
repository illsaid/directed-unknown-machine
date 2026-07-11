# 016 — Three conflicting evidence interpretations

## Type

hostile-contract

## User

A product lead preparing a recommendation on whether to keep a new onboarding flow.

## Situation

The supplied Evidence field contains direct observations followed by three incompatible operator interpretations, making the generated assignment harder to inspect as one dense sentence.

## Input

Decision: Keep the new onboarding flow for the next release or restore the prior flow.
Evidence: Twelve of 40 test users abandoned the new flow at the permissions screen. Seven of those users completed the prior flow in an earlier test. One interpretation is that users do not trust the permissions request. A second interpretation is that the permissions copy is confusing. A third interpretation is that users were willing to grant permission but did not understand why it was requested at that point in the flow.
Constraints: Do not infer why users abandoned; do not treat the earlier test as a controlled comparison; do not select any supplied interpretation without tying it to an observation that distinguishes it from the others.
Success: Recommend keep or restore, keep all three interpretations unresolved unless supplied observations distinguish them, and name the smallest additional observation that would separate the leading explanations.

## Expected useful outcome

Preserve all three interpretations while making the downstream reasoning requirements individually inspectable rather than burying them in one accumulated deliverable sentence.

## Actual outcome

Run 17 preserves the complete four-field contract and emits five separate brief requirements, including an explicit requirement to compare interpretations only against supplied observations and leave unresolved conflict visible.

## Whether the system helped

yes

## What broke

Before Run 17, the semantic boundary was present, but the fixed deliverable had accumulated into one long sentence. With three interpretations, an operator could no longer quickly verify each reasoning obligation.

## What would make the result more useful

Test a contract where Constraints and Success appear to conflict, to determine whether structural preservation without consistency checking is still trustworthy.