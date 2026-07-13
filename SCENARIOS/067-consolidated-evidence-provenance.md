# 067 — Evidence provenance is one immutable-record invariant

## Type

structural-regression

## User

A product lead delegating a checkout diagnosis assembled from several partially overlapping sources.

## Situation

Evidence provenance currently uses one obligation for source-to-measurement mapping and another for observation, interpretation, assumption, and gap status. The obligations should become one invariant only if the combined wording still prevents source spill, double-counting, conflict erasure, and claim promotion.

## Input

Decision: Choose whether to revise checkout copy, investigate latency, or run another diagnostic before changing the product.
Evidence: Funnel report A observes checkout abandonment at 12% and p95 latency at 540 milliseconds. Export B also observes checkout abandonment at 12% but does not measure latency. Interview summary C interprets confusing copy as the cause. Trace review D interprets latency as the cause. The team assumes returning users will adapt. No step-level abandonment data or response-time correlation is supplied.
Constraints: Preserve which source supplied each measurement and value. Disclose that reports A and B overlap on abandonment without counting the duplicate 12% as independent causal support. Preserve the two causal interpretations, the adaptation assumption, and the missing distinguishing evidence without promoting any of them to fact.
Success: Emit one Evidence provenance requirement that preserves both source mapping and evidence status. Recommend another diagnostic because the supplied observations do not distinguish the competing causes; do not prescribe a copy or latency remedy.

## Expected useful outcome

Evidence provenance appears as one invariant. It maps report A to abandonment and latency, export B only to abandonment, discloses their overlap, preserves both 12% values without double-counting, keeps the copy and latency claims as interpretations, keeps adaptation as an assumption, and names step-level abandonment plus response-time correlation as the unresolved evidence needed to distinguish the causes. The supported action remains another diagnostic.

## Actual outcome

Run 68 consolidates the two Evidence provenance requirements into one immutable-record invariant. The combined requirement still protects source-to-measurement mapping, overlap disclosure, conflicting-value preservation, claim-status separation, and the no-promotion boundary. No parser, field, audit group, decision rule, classifier, or transformation was added.

## Whether the system helped

yes

## What broke

Before Run 68, one audit operation was expressed as two adjacent requirements. That split made source identity and claim status look like separable records even though both must be preserved before any transformation or judgment can be trusted.

## What would make the result more useful

Next, test whether the two Boundary evaluation requirements can be consolidated without weakening full-range handling, explicit equality semantics, or the no-comparator refusal boundary.
