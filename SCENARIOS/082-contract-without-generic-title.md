# 082 — Let the contract identify itself

## Type

structural-regression

## User

A product lead delegating a bounded rollout decision who needs the output to begin with the enforceable contract rather than a generic document title.

## Situation

The executable opens with `Bounded decision brief task`, immediately followed by a complete contract check and the four explicit fields. The test is whether removing the generic title reduces presentation density while leaving the artifact's purpose, completeness, and audit sequence clear.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay rollout.

## Expected useful outcome

The executable begins with the contract check, preserves all four supplied fields, and retains the six ordered audit headings and every detailed requirement. Both gates are satisfied, so rollout is the authorized action. No generic title is needed to identify the output.

## Actual outcome

Run 83 removes only `Bounded decision brief task`. The output now begins with `Contract check: complete — 4/4 explicit fields; no content inferred`, followed by the intact Decision, Evidence, Constraints, and Success fields and all six audit operations. Conversion at 23% satisfies the inclusive 20% minimum, latency at 480 milliseconds satisfies the strict 500 millisecond maximum, and rollout remains authorized under Success.

## Whether the system helped

yes

## What broke

Before Run 83, the title named the artifact generically but contributed no contract field, audit operation, decision rule, or refusal boundary. The contract check and explicit fields already identify what the executable produced.

## What would make the result more useful

Next, test the contract-check line against an incomplete-field scenario before deciding whether any part of it is redundant; unlike the removed title, it may carry the observable no-inference boundary.