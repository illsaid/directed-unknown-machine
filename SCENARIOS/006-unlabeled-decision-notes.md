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

The system should refuse to generate a bounded brief from this unlabeled prose and provide a minimal copyable repair skeleton containing only the missing contract labels. It should not infer fields, rewrite the notes, or add a generic extractor.

## Actual outcome

Run 7 exits with a four-line repair skeleton:

```text
cannot preserve the decision contract from unlabeled prose; add these explicit fields without rewriting the notes:
Decision:
Evidence:
Constraints:
Success:
```

The operator can now place the existing clauses under the four labels without changing their substance.

## Whether the system helped

yes

## What broke

Run 6 named the missing labels in one sentence, but the operator still had to reconstruct the required format before retrying.

## What would make the result more useful

Next, test one repaired version of these same notes and verify that the output preserves every clause without adding interpretation.