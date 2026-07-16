# 137 — Distinguish a failed rollback branch from one awaiting evidence

## Type

hostile real decision handoff

## User

A release manager delegating a production deployment decision.

## Situation

A canary release violates the supplied continuation boundary and a verified recovery snapshot exists, but the on-call SRE explicitly reports that rollback cannot begin within the required 30-minute window.

## Input

Decision: Decide whether to continue, pause, or roll back production release R-49.
Evidence: The canary error rate is 2.9 percent. The release boundary is at or below 1.0 percent. The recovery service reports that snapshot S-917 passed checksum verification after the canary began. The on-call SRE acknowledged the incident channel and stated that no qualified rollback operator will be available for at least 75 minutes. No Severity 1 incident is open.
Constraints: Continuing the release requires an error rate at or below 1.0 percent and no open Severity 1 incident. Rollback is operationally permitted only when the release error-rate gate is violated, a post-canary recovery snapshot is verified, and an SRE is available to execute rollback within 30 minutes.
Success: Continue the release if both continuation gates are satisfied. If the error-rate gate is violated, roll back to the verified post-canary snapshot only if the snapshot and operator-availability gates are satisfied. Otherwise report that no supplied release branch is authorized. Distinguish a violated branch condition from missing evidence.

## Expected useful outcome

The compiled contract must mark the error-rate gate violated and the no-Severity-1 gate satisfied. It must recognize the violation as the rollback trigger and establish the verified-snapshot gate, but mark the 30-minute operator-availability gate violated because the supplied 75-minute estimate contradicts the required window. It must not authorize rollback, must describe the rollback branch as failed under the supplied evidence rather than merely awaiting confirmation, and must not request evidence that is already supplied.

## Actual outcome

Run 139 exposed that the recommendation obligation required every fallback condition to be established but did not explicitly distinguish a violated fallback gate from an unresolved one. The obligation now requires a violated fallback-specific gate to make the branch unavailable under the supplied evidence, while an unresolved gate leaves it awaiting evidence.

## Whether the system helped

yes

## What broke

The prior wording correctly withheld rollback, but it could still produce the same generic no-authority result used for an unresolved operator gate. That loses an operationally important distinction: this branch is not waiting for confirmation; the supplied confirmation establishes that the timing condition fails.

## What would make the result more useful

Transfer the failed-fallback distinction to a non-software domain before adding any further fallback wording.