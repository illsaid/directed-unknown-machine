# 008 — Social post reuse decision

## Type

decision-support-transfer

## User

A newsletter operator deciding whether to reuse an unused social post.

## Situation

The operator has an unused post from yesterday and fresh account analytics, but wants to avoid repeating the same framing too closely.

## Input

Decision: Reuse the unused post today or write a new post from scratch.
Evidence: Yesterday's post using a concrete FDA contrast earned above-median replies, while broad market-summary posts earned impressions but few interactions.
Constraints: Do not repeat yesterday's wording or the same company pair; preserve the concrete contrast structure; do not claim the analytics prove causation.
Success: Recommend reuse or replacement and provide one defensible reason tied to the observed engagement pattern.

## Expected useful outcome

Preserve the editorial decision, observed evidence, anti-causal constraint, and observable success condition without recasting existing evidence as a request for future evidence.

## Actual outcome

Run 9 preserves all four clauses. Neutral output labels avoid changing the supplied evidence into an evidence requirement.

## Whether the system helped

yes

## What broke

The previous output label `Evidence required` subtly changed supplied observations into a request for additional evidence.

## What would make the result more useful

Test a non-editorial decision while keeping the same explicit four-field contract.
