# 151 — Treat enumerated governance scope as closed

## Type

hostile real decision handoff

## User

A laboratory operations manager delegating disposition of a temperature-exposed specimen batch.

## Situation

A governance rule resolves applicability-authority conflicts for contamination-hold and release-hold status, but does not name quarantine status. The two named dimensions must not be treated as examples that silently include the omitted third dimension.

## Input

Decision: Decide whether to local-reprocess, salvage-ship, or hold specimen batch B-291.
Evidence: Freezer F-31 recorded minus 58 degrees Celsius against a release boundary of at or below minus 70 degrees Celsius. The batch remains sealed. Reprocessing suite R-21 is validated, a qualified technician is available, and local-reprocessing authorization is signed. A validated dry-ice overpack is reserved, salvage-shipment authorization is signed, and a courier confirmed collection within four hours. Policy DP-9 gives local reprocessing precedence when both fallback branches qualify. Policy NT-3 gives salvage shipment precedence when both qualify. Governance rule QG-4 states that DP-9 controls NT-3 except for batches under contamination hold, release hold, or quarantine. For contamination-hold status, CH-32 says B-291 is held and CR-24 says it is cleared; AR-6 selects CR-24 while AR-9 selects CH-32. For release-hold status, RH-12 says B-291 is held and RR-8 says it is cleared; AR-12 selects RR-8 while AR-14 selects RH-12. For quarantine status, QH-5 says B-291 is quarantined and QR-3 says it is cleared; AR-16 selects QR-3 while AR-18 selects QH-5. Governance rule AG-5 states that AR-6 controls AR-9 for contamination-hold status and AR-12 controls AR-14 for release-hold status. AG-5 says nothing about quarantine status, and no other supplied authority selects between AR-16 and AR-18.
Constraints: Local reprocessing requires a violated temperature gate, an intact seal, a validated suite, an available qualified technician, signed authorization, and no applicable exception to QG-4. Salvage shipment requires a violated temperature gate, an intact seal, a reserved validated overpack, signed authorization, confirmed courier collection within four hours, and no applicable exception to QG-4. Preserve all three status dimensions, every status record, every applicability rule, both precedence policies, and AG-5's exact enumerated scope.
Success: Apply AG-5 to contamination-hold and release-hold status only. CR-24 and RR-8 govern those dimensions, while their opposing records and applicability rules remain conflicting but non-governing. Do not treat AG-5's two named dimensions as illustrative or extend it to quarantine status. Because AR-16 and AR-18 conflict and no supplied governance selects between them, quarantine status remains unresolved, QG-4 exception applicability remains unresolved, DP-9 cannot govern, branch authority remains unresolved, and the authorized action is hold pending quarantine-status applicability authority.

## Expected useful outcome

The contract must treat AG-5's enumerated scope as closed: resolve only contamination-hold and release-hold status, preserve quarantine status as a separate unresolved conflict, refuse to extend AG-5 by analogy, leave QG-4 and fallback precedence unresolved, and authorize hold pending authority over quarantine status.

## Actual outcome

Run 153 requires an enumerated governance scope to cover only the dimensions it explicitly lists. AG-5 resolves contamination-hold and release-hold status, but not quarantine status. AR-16 and AR-18 therefore remain conflicting, QG-4 cannot govern, DP-9 and NT-3 remain conflicting, both fallback branches remain satisfied candidates but unauthorized, and hold is authorized pending quarantine-status applicability authority.

## Whether the system helped

yes

## What broke

The contract confined governance to named dimensions but did not explicitly state that a list of named dimensions is closed rather than illustrative.

## What would make the result more useful

Test a governance rule that says "including" before named dimensions, distinguishing an explicitly open list from a closed enumeration.