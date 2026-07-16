# 138 — Transfer failed-fallback handling to cold-chain operations

## Type

transfer real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A specimen freezer exceeds the supplied storage boundary. The Success rule permits emergency transfer to a validated backup freezer only if capacity is reserved and a qualified technician can complete transfer within 20 minutes, but the technician explicitly cannot arrive inside that window.

## Input

Decision: Decide whether to release, transfer, or hold specimen batch B-204.
Evidence: Freezer F-12 recorded minus 61 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. Backup freezer F-19 has validated capacity reserved for batch B-204. The duty technician acknowledged the transfer request and stated that the earliest qualified arrival is 45 minutes from now. The batch remains sealed.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Emergency transfer is permitted only when the storage-temperature gate is violated, validated backup capacity is reserved, and a qualified technician can complete transfer within 20 minutes.
Success: Release the batch if both release gates are satisfied. If the storage-temperature gate is violated, transfer the sealed batch to the validated backup freezer only if the capacity and 20-minute technician gates are satisfied. Otherwise hold the batch and report why no transfer branch is authorized. Distinguish a violated branch condition from missing evidence.

## Expected useful outcome

The compiled contract must mark the storage-temperature gate violated and the seal gate satisfied. It must recognize the violation as the emergency-transfer trigger and establish backup capacity, but mark the 20-minute technician gate violated because the supplied 45-minute estimate exceeds the required window. It must not authorize transfer, must direct the supplied hold action, must describe emergency transfer as unavailable under the supplied evidence rather than awaiting confirmation, and must not request technician evidence that is already supplied.

## Actual outcome

Run 140 verified that the Run 139 failed-fallback wording transfers unchanged outside software operations. The storage violation activates consideration of emergency transfer, backup capacity is satisfied, the technician timing gate is violated, emergency transfer is unavailable under the supplied evidence, and the supplied hold branch governs without requesting evidence already present.

## Whether the system helped

yes

## What broke

Nothing. The existing recommendation obligation is operational rather than deployment-specific: it distinguishes a violated fallback gate from an unresolved one and preserves the supplied alternative action in this cold-chain handoff without new domain logic.

## What would make the result more useful

Test a violated fallback branch when Success supplies a second, independently conditioned fallback, checking that failure of the first does not erase a separately authorized alternative.