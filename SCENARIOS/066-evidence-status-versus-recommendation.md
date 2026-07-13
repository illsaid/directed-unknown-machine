# 066 — Evidence status belongs with the preserved record

## Type

structural-regression

## User

A product lead delegating a checkout diagnosis whose observed result has two plausible causes.

## Situation

The executable currently places the obligation to distinguish observations, interpretations, assumptions, and unresolved gaps inside Governed recommendation. That status discipline is needed before transformations, boundaries, gates, or recommendations can be trusted.

## Input

Decision: Choose whether to revise checkout copy, investigate latency, or run another diagnostic before changing the product.
Evidence: Observation — checkout abandonment was 12%. Interpretation A — confusing copy caused the abandonment. Interpretation B — latency caused the abandonment. Assumption — returning users will adapt. Gap — no step-level abandonment data or response-time correlation is supplied.
Constraints: Do not promote either interpretation or the assumption to fact. Preserve the unresolved causal conflict and identify the evidence that would distinguish it.
Success: First preserve each supplied evidence item with its status. Then recommend another diagnostic unless supplied observations distinguish the causes; do not prescribe a copy or latency remedy from the unresolved record.

## Expected useful outcome

Print the evidence-status obligation under Evidence provenance, before Evidence transformation and all downstream audit groups. Governed recommendation should contain only action selection under the supplied success or reversal rule. The supported action is run another diagnostic because the observation does not distinguish the two interpretations.

## Actual outcome

Run 67 moves the unchanged evidence-status obligation from Governed recommendation to Evidence provenance. The six-group sequence, four-field contract, and reasoning rules remain unchanged; the output now preserves claim status at the source-record stage before any downstream operation uses it.

## Whether the system helped

yes

## What broke

Before Run 67, the executable introduced observation, interpretation, assumption, and gap status only in the final Governed recommendation group. That made source preservation appear complete before the supplied claims had been typed by evidentiary status.

## What would make the result more useful

Next, inspect whether Evidence provenance now contains two obligations that can be consolidated without weakening source-to-measurement mapping or evidence-status preservation.
