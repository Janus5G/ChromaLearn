# ChromaLearn - screening til dataansvarlig/DPO før anvendelse

**Formål:** kort screeningshjælp før implementering. Dokumentet er ikke juridisk rådgivning og er ikke en færdig DPIA. Den skole/kommune, der anvender løsningen, skal selv fastlægge retsgrundlag, roller, risici og behovet for DPIA eller andre formelle vurderinger.

## 1. Tilsigtet undervisningsbrug

- Skole/organisation:
- Ansvarlig beslutningsejer:
- DPO/privacy-kontakt:
- Pilotklasser/aldersgruppe:
- Fag:
- Konkret pædagogisk formål:
- Bruges ChromaLearn kun til formativ vejledning? Ja / Nej
- Kan output påvirke karakter, optagelse, placering, progression, disciplinær afgørelse eller anden beslutning om eleven? Ja / Nej
- Hvis ja, beskriv præcist hvordan:

## 2. Datavej

Dokumentér alle komponenter i den faktiske implementering:

`Elevens enhed -> ChromaLearn -> inference-endpoint -> eventuel proxy/gateway -> modelserver -> svar`

For hver komponent dokumenteres, hvor relevant:

- operatør/dataansvarlig/databehandler
- land/fysisk eller juridisk lokation
- datakategorier
- om prompts/svar logges
- opbevaringsperiode
- backup/snapshot
- underdatabehandlere
- eventuelle tredjelandsoverførsler

## 3. Dataminimering

- Er navn/elev-ID nødvendigt? Som udgangspunkt bør pilot kunne gennemføres uden.
- Kan følsomme eller private oplysninger undgås?
- Kan opgaver anonymiseres/pseudonymiseres før brug?
- Er lyd/billeder nødvendige i den konkrete pilot?

## 4. Retsgrundlag og transparens

Skolen dokumenterer:

- retsgrundlag for behandlingen
- information til elever og forældre/værger, hvor relevant
- kontaktvej for registreredes rettigheder
- databehandleraftaler/kontrakter, hvor relevant
- konkret opbevarings- og slettepolitik for hele infrastrukturen

## 5. Børn og risiko

Vurder især elevens alder, forventninger, magtforholdet i skolen, risiko for overafhængighed af AI, fejl/hallucinationer, diskrimination, utilsigtet profilering og påvirkning af elevens muligheder.

## 6. DPIA-screening

- Er behandlingen sandsynligvis forbundet med høj risiko for de registreredes rettigheder og frihedsrettigheder? Ja / Nej / Kræver vurdering
- Er DPO inddraget? Ja / Nej / Ikke relevant
- Kræves en DPIA? Ja / Nej / Kræver juridisk vurdering
- Begrundelse og dato:

## 7. AI Act-screening

Sessionsbaseret data gør ikke i sig selv en uddannelsesanvendelse lavrisiko. Vurder den konkrete tilsigtede anvendelse, herunder om systemet evaluerer læringsresultater og bruger resultatet til at styre læringsprocessen, eller anvendes til andre Annex III-formål.

Dokumentér særskilt klassifikation og begrundelse. Kontrollér altid gældende konsolideret EU-tekst og dansk vejledning ved deployment.

## 8. GO / NO-GO

- [ ] Formål og nødvendighed er dokumenteret.
- [ ] Roller og leverandører er afklaret.
- [ ] Datavej og logning er verificeret.
- [ ] Retsgrundlag og transparens er afklaret.
- [ ] DPIA-behov er vurderet.
- [ ] AI Act-anvendelse/klassifikation er vurderet.
- [ ] Menneskeligt tilsyn og stopprocedure er på plads.

**Konklusion:** GO / NO-GO / GO med betingelser  
**Ansvarlig:**  
**Dato:**  
**Begrundelse:**
