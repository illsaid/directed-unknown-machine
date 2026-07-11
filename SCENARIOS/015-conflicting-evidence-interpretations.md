# 015 — Conflicting evidence interpretations

## Type

hostile-contract

## User

A product lead preparing a recommendation on whether to keep a new onboarding flow.

## Situation

The supplied Evidence field contains the same observations followed by two incompatible operator interpretations.

## Input

Decision: Keep the new onboarding flow for the next release or restore the prior flow.
Evidence: Twelve of 40 test users abandoned the new flow at the permissions screen. Seven of those users completed the prior flow in an earlier test. The abandonment proves users do not trust the permissions request. The abandonment instead shows that the permissions copy is confusing, not that users distrust the request.
Constraints: Do not infer why users abandoned; do not treat the earlier test as a controlled comparison; do not select either supplied interpretation without tying it to an observation that distinguishes them.
Success: Recommend keep or restore, identify both supplied interpretations as unresolved, and name one additional observation that would discriminate between them.

## Expected useful outcome

Preserve both interpretations, but require the analyst to compare them against the supplied observations and identify what evidence would distinguish them instead of choosing one by plausibility.

## Actual outcome

Run 16 preserves the complete Evidence field and requires conflicting interpretations to be adjudicated against supplied observations, with unresolved conflict remaining explicit.

## Whether the system helped

yes

## What broke

Before Run 16, the deliverable prevented interpretations embedded in Evidence from becoming facts, but did not explicitly require conflicting interpretations to be compared against the same observations or left unresolved when the observations could not distinguish them.

## What would make the result more useful

Test whether the same instruction survives a case with three interpretations, or whether densely mixed Evidence should be rejected as outside the narrow contract.
