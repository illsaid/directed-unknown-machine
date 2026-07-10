# 006 — Unlabeled decision notes: refuse false preservation

## Type

decision-support-boundary

## User

A newsletter operator handing rough notes to an agent before a publish-or-hold decision.

## Situation

The notes contain a real decision, evidence, caveats, and a success condition, but none are explicitly labeled. The system must not pretend it preserved a decision contract that it cannot reliably identify.

## Input

We need to decide whether to publish the approval forecast this week or hold it until the inspection uncertainty is resolved. The trial hit its primary endpoint, but the sponsor has disclosed an unresolved manufacturing observation and we do not have the underlying FDA correspondence. Priority Review should not be treated as proof that approval is more likely. The useful result is one recommendation the editor can defend in two sentences while naming the largest unresolved uncertainty.

## Expected useful outcome

The system should refuse to generate a bounded brief from this unlabeled prose and state exactly which explicit fields are required. It should not add a generic natural-language extractor or silently emit missing values.

## Actual outcome

Run 6 makes the contract explicit. The command exits with: `cannot preserve the decision contract from unlabeled prose; add these explicit fields: Decision:, Evidence:, Constraints:, Success:`.

## Whether the system helped

yes

## What broke

The Run 5 executable previously emitted a plausible-looking brief with all four fields set to `not stated`. That hid the fact that preservation had failed.

## What would make the result more useful

Keep the labeled note-set requirement. Next, test whether a user can repair a rejected input quickly by adding the four labels without rewriting the underlying notes.