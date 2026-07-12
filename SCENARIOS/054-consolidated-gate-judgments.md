# 054 — Consolidated gate judgment preserves independent blocking gates

## Type

structural-regression

## User

A product lead reviewing a delegated rollout decision before it leaves the team.

## Situation

The Gate judgments requirements separately demand per-gate status and evidence, then prohibit collapsing gates and require failed or unresolved gates to block a recommendation. These may be one invariant if independent visibility and recommendation blocking remain explicit.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Paid conversion was 23%. P95 latency was 540 milliseconds. The fraud-loss measurement was not supplied.
Constraints: Paid conversion must be at least 20%, p95 latency must be below 500 milliseconds, and fraud loss must remain below 0.5%.
Success: Recommend rollout only if every constraint is satisfied from supplied evidence; otherwise recommend delay. Report each gate separately and identify the evidence used.

## Expected useful outcome

Emit one concise gate-judgment rule requiring every constraint to receive its own satisfied, violated, or unresolved status with named supplied evidence, while making any violated or unresolved gate block a supported rollout recommendation. Conversion is satisfied by 23%, latency is violated by 540 milliseconds, fraud loss is unresolved because no measurement was supplied, and delay is recommended without collapsing the three gates into one opaque verdict.

## Actual outcome

Run 55 consolidates the two Gate judgments bullets into one inspectable invariant. The output still requires separate evidence-backed status for conversion, latency, and fraud loss; preserves the violated and unresolved gates; and makes both block rollout, so delay remains the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 55, independent gate status, evidence binding, anti-collapse behavior, and recommendation blocking were split across two bullets even though they form one decision-contract invariant.

## What would make the result more useful

Next, inspect the Evidence provenance requirements for whether conflicting values and source-to-measurement mapping can be expressed more compactly without weakening disagreement visibility.