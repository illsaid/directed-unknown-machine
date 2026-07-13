# 080 — Remove the duplicated reasoning-sequence line

## Type

structural-regression

## User

A product lead delegating a bounded rollout decision who needs the audit path to be obvious on first scan.

## Situation

The executable prints both a literal six-step reasoning sentence and six headings already ordered into the same preserve, transform, reconcile, apply, judge, recommend sequence. The test is whether the headings alone keep the process legible.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay rollout.

## Expected useful outcome

The executable omits the standalone reasoning-sequence sentence while retaining the six ordered headings and every detailed requirement. The observable audit path remains preserve evidence, transform evidence, reconcile boundaries, apply boundaries, judge gates, then recommend. Both gates are satisfied, so rollout is the authorized action.

## Actual outcome

Run 81 removes only the standalone `Reasoning sequence` line. The six headings remain in dependency order and carry the same verbs and category prefixes, so the audit path is still directly visible without being stated twice. Conversion at 23% satisfies the inclusive 20% minimum, latency at 480 milliseconds satisfies the strict 500 millisecond maximum, and rollout remains the authorized action under Success.

## Whether the system helped

yes

## What broke

Before Run 81, the literal sequence sentence repeated the exact order already encoded by the six adjacent headings and added presentation density without adding a refusal boundary.

## What would make the result more useful

Next, test whether `Brief requirements` adds orientation or merely labels the six self-describing headings.