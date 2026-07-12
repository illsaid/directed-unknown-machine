# 055 — Consolidated provenance preserves overlap and disagreement

## Type

structural-regression

## User

A product lead reviewing a delegated rollout decision before it leaves the team.

## Situation

The Evidence provenance group separately maps sources to measurements and preserves conflicting values. These may be one invariant if shared coverage, measurement boundaries, and disagreement remain explicit.

## Input

Decision: Roll out the checkout change to US web users on Monday or delay it.
Evidence: Report A measured paid conversion at 23% and p95 latency at 480 milliseconds. Export B also measured paid conversion at 23% but measured p95 latency at 540 milliseconds. No supplied evidence establishes that either latency source is more applicable.
Constraints: Paid conversion must be at least 20%, and p95 latency must be below 500 milliseconds.
Success: Recommend rollout only if every constraint is satisfied from supplied evidence; otherwise recommend delay. Preserve which source supplied each measurement, disclose overlapping conversion coverage without treating it as independent corroboration, and leave the conflicting latency values unresolved.

## Expected useful outcome

Emit one concise provenance rule that maps every source to the measurements and values it supplies, discloses overlap without letting it spill across measurements or count as extra independent evidence, and preserves conflicting values unless supplied applicability evidence resolves them. Conversion is satisfied by the shared 23% measurement, latency remains unresolved because Report A says 480 milliseconds while Export B says 540 milliseconds, and delay is recommended.

## Actual outcome

Run 56 consolidates the two Evidence provenance bullets into one inspectable invariant. The output still maps Report A and Export B to their actual measurements, treats their matching 23% conversion values as overlapping coverage rather than extra independent support, preserves the 480- and 540-millisecond latency disagreement, and leaves latency unresolved, so delay remains the supported recommendation.

## Whether the system helped

yes

## What broke

Before Run 56, source-to-measurement mapping, overlap handling, and conflicting-value preservation were split across two bullets even though they form one provenance invariant.

## What would make the result more useful

Next, inspect the Decision requirements for whether recommendation and governing fallback wording can be expressed more compactly without weakening the operator-supplied reversal rule.