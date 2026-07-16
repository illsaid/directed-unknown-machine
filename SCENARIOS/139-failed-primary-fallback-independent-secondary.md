# 139 — Preserve an independently authorized second fallback

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A specimen batch fails its release-temperature gate. Emergency transfer is unavailable because the qualified technician cannot meet its timing condition, but Success supplies a separate salvage-shipment fallback whose own conditions are fully established.

## Input

Decision: Decide whether to release, transfer, salvage-ship, or hold specimen batch B-219.
Evidence: Freezer F-12 recorded minus 61 degrees Celsius. The release boundary is at or below minus 70 degrees Celsius. The batch remains sealed. Backup freezer F-19 has validated capacity reserved, but the duty technician stated that the earliest qualified arrival is 45 minutes from now. Validated dry-ice overpack kit D-8 is reserved for batch B-219. Quality officer Mara Chen signed the salvage-shipment authorization. Courier Northline confirmed collection within four hours.
Constraints: Release requires storage at or below minus 70 degrees Celsius and an intact seal. Emergency transfer requires a violated storage-temperature gate, reserved validated backup capacity, and qualified transfer within 20 minutes. Salvage shipment requires a violated storage-temperature gate, an intact seal, a reserved validated dry-ice overpack, signed quality authorization, and confirmed courier collection within four hours. The salvage branch does not depend on emergency-transfer availability.
Success: Release the batch if both release gates are satisfied. Otherwise transfer it only if every emergency-transfer condition is satisfied. If emergency transfer is unavailable, salvage-ship it when every salvage condition is satisfied. Otherwise hold the batch and report why no disposition branch is authorized. Preserve the status of each branch separately.

## Expected useful outcome

The compiled contract must mark the storage-temperature gate violated and the seal gate satisfied. It must mark emergency transfer unavailable because the supplied 45-minute technician estimate violates the 20-minute condition. It must independently establish the dry-ice overpack, quality-authorization, and four-hour courier gates and authorize salvage shipment. Failure of the emergency-transfer branch must not erase or contaminate the independently conditioned salvage branch.

## Actual outcome

Run 141 exposed that the recommendation obligation described branch-local blocking generally but did not explicitly require separate fallback branches to retain independent authority after another fallback fails. The strengthened obligation now evaluates each supplied fallback branch independently, keeps emergency transfer unavailable, and authorizes the fully satisfied salvage-shipment branch.

## Whether the system helped

yes

## What broke

The prior wording could be read as applying the failed fallback's unavailability to the entire fallback stage rather than only to emergency transfer. That ambiguity could suppress the separately authorized salvage branch.

## What would make the result more useful

Test two independently satisfied fallback branches with no supplied precedence, verifying that the existing non-nested branch rule leaves authority unresolved rather than choosing one.