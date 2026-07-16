# 150 — Keep governed status authority dimension-local

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A governance rule resolves conflicting contamination-hold evidence but says nothing about a separate release-status conflict. The resolved contamination status must not be borrowed to settle release status.

## Input

Decision: Decide whether to local-reprocess, salvage-ship, or hold specimen batch B-286.
Evidence: Freezer F-27 recorded minus 59 degrees Celsius against a release boundary of at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-18 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both fallback branches qualify. Policy NT-3 gives salvage shipment precedence when both qualify. Governance rule QG-4 states that DP-9 controls NT-3 except for batches under contamination hold or release hold. Hold order CH-28 states that B-286 is under contamination hold. Quality release record CR-20 states that B-286 is cleared from contamination hold. Release-status record RH-7 states that B-286 is under release hold. Release-status record RR-4 states that B-286 is cleared from release hold. Applicability rule AR-6 makes the QA-director-signed quality release record govern current contamination-hold status. Applicability rule AR-9 makes the most recent active contamination-hold order govern current contamination-hold status. Governance rule AG-2 states that AR-6 controls AR-9 for current contamination-hold status only. No supplied authority selects between RH-7 and RR-4 for release-hold status.
Constraints: Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, signed authorization, and no applicable exception to QG-4. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, confirmed courier collection within four hours, and no applicable exception to QG-4. Preserve both fallback branches, both precedence policies, all status records, both applicability rules, and AG-2's exact scope.
Success: Apply AG-2 only to the contamination-hold conflict. AR-6 therefore selects CR-20 for contamination-hold status, while AR-9 and CH-28 remain conflicting but non-governing on that dimension. Do not use AG-2 or CR-20 to resolve the separate release-hold conflict. Because RH-7 and RR-4 conflict and no supplied authority selects between them, QG-4 exception applicability remains unresolved, DP-9 cannot govern, branch authority remains unresolved, and the authorized action is hold pending release-status applicability authority.

## Expected useful outcome

The contract must preserve the authority chain AG-2 to AR-6 to CR-20 for contamination-hold status only. It must preserve RH-7 and RR-4 as an independent unresolved release-hold conflict, refuse to borrow AG-2 across status dimensions, leave QG-4 applicability and fallback precedence unresolved, and authorize hold pending authority over release-hold status.

## Actual outcome

Run 152 requires governance over applicability authorities to remain confined to the exact status dimension stated by the governance rule. AG-2 resolves contamination-hold status through AR-6 and CR-20, but RH-7 and RR-4 remain independently conflicting; QG-4 cannot govern; DP-9 and NT-3 remain conflicting; both fallback branches remain satisfied candidates but non-authorized; and hold is authorized pending release-status applicability authority.

## Whether the system helped

yes

## What broke

The contract said applicability evidence is scope-limited, but did not explicitly state that governance selecting an applicability authority is itself limited to the named status dimension and cannot resolve a separate status conflict.

## What would make the result more useful

Test one governance rule that covers two named status dimensions but excludes a third, confirming that enumerated scope remains closed rather than illustrative.