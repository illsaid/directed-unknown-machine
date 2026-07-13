# 073 — Tighten evidence preservation without weakening refusal boundaries

## Type

structural-regression

## User

A product lead delegating a checkout diagnosis built from overlapping reports, conflicting measurements, and competing causal interpretations.

## Situation

The `Evidence: preserve` requirement protects several distinct refusal boundaries but has accumulated redundant wording. The operator needs a shorter invariant that remains explicit about source scope, overlap, conflicting values, claim status, and unsupported causal promotion.

## Input

Decision: Choose whether to fix checkout copy, investigate latency, or run another diagnostic.
Evidence: Funnel report A records checkout abandonment at 12% and p95 latency at 540 milliseconds. Export B repeats the same 12% abandonment population but contains no latency measurement. Monitor C records p95 latency at 560 milliseconds for the same period. Interview summary D interprets confusing copy as the cause. Trace review E interprets latency as the cause. The team assumes returning users will adapt. Step-level abandonment and response-time correlation are missing.
Constraints: Preserve which source supplied each measurement. Do not count Export B as independent abandonment evidence or as latency evidence. Keep both latency values visible unless supplied applicability evidence resolves them. Keep observations, interpretations, assumptions, and missing evidence distinct; do not promote either causal interpretation to fact.
Success: Produce an audit contract that preserves the source record and leaves the causal conflict unresolved. Name step-level abandonment joined to response time as distinguishing evidence, and recommend another diagnostic rather than a copy or latency remedy.

## Expected useful outcome

The executable prints a shorter `Evidence: preserve` invariant while still requiring source-to-measurement mapping, overlap disclosure without double-counting or spill, conflicting-value retention, distinct evidence statuses, no unsupported promotion, explicit unresolved conflict, and the evidence needed to distinguish competing interpretations.

## Actual outcome

Run 74 shortens only the `Evidence: preserve` requirement. It removes repeated phrasing while retaining every tested refusal boundary: Export B cannot become extra abandonment support or latency evidence; 540 and 560 milliseconds remain visible; causal interpretations and the adaptation assumption remain non-factual; and the missing joined evidence remains the named discriminator.

## Whether the system helped

yes

## What broke

Before Run 74, the invariant repeated the same preservation rule through several nested clauses. The meaning was correct, but the sentence was harder to audit than necessary and obscured the small set of prohibited operations.

## What would make the result more useful

Next, test whether the `Evidence: transform` requirement can be shortened without weakening the distinction between exclusion support and adjustment support.