# 052 — Consolidated sensitivity rule preserves crossing and same-side boundaries

## Type

structural-regression

## User

A product lead reviewing a delegated rollout assignment before it leaves the team.

## Situation

The executable uses separate sensitivity requirements for ranges that cross a gate and ranges that remain wholly on one side, even though both cases can be judged by one full-range rule.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was 23%. A supported traffic-mix sensitivity analysis places Monday p95 latency between 480 and 520 milliseconds. A supported seven-day refund-rate sensitivity analysis places refunds between 1.4% and 1.8%.
Constraints: Paid conversion must be at least 20%, p95 latency must be below 500 milliseconds, and refunds must be below 2%.
Success: Recommend rollout only if every gate is satisfied from supplied evidence; otherwise recommend delay.

## Expected useful outcome

Emit one inspectable sensitivity rule that judges every supported range against the full boundary. Preserve the 480–520 millisecond latency range and state that its gate is conditional because the range crosses 500 milliseconds. Resolve the 1.4%–1.8% refund range as satisfying the below-2% gate from the whole range without choosing a representative value. Conversion is satisfied, rollout is unsupported because latency remains conditional, and delay is recommended.

## Actual outcome

Run 53 replaces the separate crossing-range and same-side-range requirements with one full-range invariant. The output still requires conditional outcomes on both sides of a crossed threshold, resolves a wholly same-side range from the complete range, and forbids midpoint, best-case, or other convenient point selection.

## Whether the system helped

yes

## What broke

Before Run 53, one range-evaluation invariant was split across two bullets: preserve conditionality when a range crosses a threshold, then separately resolve the gate when the whole range lies on one side.

## What would make the result more useful

Next, inspect the Decision requirements for duplicated wording around separating facts, interpretations, assumptions, and unresolved conflicts without weakening the no-promotion boundary.
