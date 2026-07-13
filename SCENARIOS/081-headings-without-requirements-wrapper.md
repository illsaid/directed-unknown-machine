# 081 — Let the audit headings stand without a wrapper

## Type

structural-regression

## User

A product lead delegating a bounded rollout decision who needs the audit path to be obvious without presentation-only labels.

## Situation

The executable prints six adjacent, self-describing audit headings beneath a generic `Brief requirements` line. The test is whether removing that wrapper reduces density while leaving the purpose and order of every operation clear.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Paid conversion is 23%. P95 latency is 480 milliseconds.
Constraints: Conversion must be at least 20%. Latency must be below 500 milliseconds.
Success: Roll out only if every gate is satisfied; otherwise delay rollout.

## Expected useful outcome

The executable omits the generic `Brief requirements` line while retaining the six ordered headings and every detailed requirement. The output still moves visibly from evidence preservation through governed recommendation. Both gates are satisfied, so rollout is the authorized action.

## Actual outcome

Run 82 removes only the `Brief requirements` wrapper. The first audit heading, `Evidence: preserve`, now follows the intact four-field contract directly; the six headings remain in dependency order and identify both domain and operation. Conversion at 23% satisfies the inclusive 20% minimum, latency at 480 milliseconds satisfies the strict 500 millisecond maximum, and rollout remains authorized under Success.

## Whether the system helped

yes

## What broke

Before Run 82, `Brief requirements` named no additional operation, rule, or refusal boundary. It inserted a generic label between the contract and six headings that already state exactly what follows.

## What would make the result more useful

Next, test whether the opening `Bounded decision brief task` title adds necessary orientation or duplicates the immediately following contract check and fields.