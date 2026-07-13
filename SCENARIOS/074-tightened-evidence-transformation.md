# 074 — Tighten evidence transformation without cross-authorizing operations

## Type

structural-regression

## User

A product lead delegating a rollout decision that includes one source-exclusion claim and one adjusted latency estimate.

## Situation

The `Evidence: transform` requirement correctly distinguishes source exclusion from value adjustment, but its wording is denser than necessary. The operator needs a shorter invariant that still requires operation-specific support and prevents evidence for one transformation from authorizing the other.

## Input

Decision: Choose whether to roll out the new checkout.
Evidence: Production report A records paid conversion at 23% and p95 latency at 540 milliseconds for the target customer population. Canary report B records 410 milliseconds for internal employees; supplied environment notes show that employee traffic uses an authentication cache unavailable to customers, so B is not applicable to the target population. A browser table records desktop latency at 450 milliseconds and mobile latency at 525 milliseconds. The team proposes an adjusted production estimate of 480 milliseconds using a 60% desktop and 40% mobile weighting, but no supplied source supports that traffic mix.
Constraints: Conversion must be at least 20% and p95 latency must be below 500 milliseconds. Preserve all original values. Exclude Canary B only from the target-population judgment using the supplied cache mismatch. Treat the 480 millisecond adjustment as conditional because its governing traffic-share assumption is unsupported; do not use the exclusion evidence as support for the adjustment.
Success: Roll out only if every gate is supported as satisfied. Otherwise delay and identify the missing production traffic-share evidence.

## Expected useful outcome

The executable prints a shorter `Evidence: transform` invariant that still preserves original values, requires distinct support for exclusion and adjustment, validates the target population and method, prevents cross-authorization, invalidates unsupported exclusion, and keeps an auditable adjustment conditional while a governing assumption lacks support.

## Actual outcome

Run 75 shortens only the `Evidence: transform` requirement. Canary B may be excluded from the target-population judgment because the supplied cache mismatch explains its non-applicability. The 480 millisecond estimate remains conditional because the 60/40 traffic mix is unsupported, and the valid exclusion evidence cannot authorize that adjustment. Latency therefore does not clear, so the governed recommendation is delay and collect production traffic-share evidence.

## Whether the system helped

yes

## What broke

Before Run 75, the transformation invariant repeated operation-specific support rules through a long nested sentence. The distinction was correct, but the wording made the non-substitution boundary harder to scan.

## What would make the result more useful

Next, test whether `Boundary: reconcile` can be shortened without allowing precedence support and equivalence support to substitute for each other.
