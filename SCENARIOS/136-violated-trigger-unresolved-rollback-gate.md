# 136 — Keep rollback unauthorized when one rollback gate is unresolved

## Type

hostile real decision handoff

## User

A release manager delegating a production deployment decision.

## Situation

A canary release violates the supplied continuation boundary and a verified recovery snapshot exists, but no supplied evidence establishes whether an operator can execute rollback within the required 30-minute window.

## Input

Decision: Decide whether to continue, pause, or roll back production release R-48.
Evidence: The canary error rate is 2.6 percent. The release boundary is at or below 1.0 percent. The recovery service reports that snapshot S-901 passed checksum verification after the canary began. The incident channel shows that the on-call SRE was paged, but contains no acknowledgement or availability estimate. No Severity 1 incident is open.
Constraints: Continuing the release requires an error rate at or below 1.0 percent and no open Severity 1 incident. Rollback is operationally permitted only when the release error-rate gate is violated, a post-canary recovery snapshot is verified, and an SRE is available to execute rollback within 30 minutes.
Success: Continue the release if both continuation gates are satisfied. If the error-rate gate is violated, roll back to the verified post-canary snapshot only if the snapshot and operator-availability gates are satisfied. Otherwise report that no supplied release branch is yet authorized and identify the missing evidence.

## Expected useful outcome

The compiled contract must mark the error-rate gate violated and the no-Severity-1 gate satisfied. It must recognize the violation as the rollback trigger and establish the verified-snapshot gate, but leave operator availability unresolved because a page is not an acknowledgement or a 30-minute availability commitment. It must not authorize rollback and must identify operator confirmation as the missing evidence.

## Actual outcome

Run 138 verified that the existing fallback obligation already preserves this boundary. The violated trigger activates consideration of rollback but does not satisfy the separate operator-availability gate; no supplied branch is authorized until an SRE confirms availability within 30 minutes.

## Whether the system helped

yes

## What broke

Nothing. The Run 137 wording still requires every additional fallback-specific condition to be established and cited, so expanding fallback triggers to include violated conditions did not bypass an unresolved rollback gate.

## What would make the result more useful

Test the same violated trigger with a fallback-specific gate that is explicitly violated rather than unresolved, confirming that the output distinguishes a failed fallback branch from one awaiting evidence.