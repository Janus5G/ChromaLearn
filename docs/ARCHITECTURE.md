# Arkitektur

ChromaLearn er et lokalt pædagogisk kontrollag mellem eleven og et OpenAI-kompatibelt inference-endpoint, som skolen selv vælger.

## Tillidsgrænser

1. Browser-UI på localhost.
2. ChromaLearn HTTP-service og deterministisk pædagogisk/session-controller.
3. Skolestyrede undervisningsprofiler og IT-konfiguration.
4. Selvstændigt valgt inference-backend.

ChromaLearn-projektet bundler eller driver ikke en obligatorisk cloud-modeltjeneste.

## Midlertidig elevtilstand

Elevsamtaler, original opgavetekst, checkpoint-spørgsmål/-svar og adaptiv modalitetsevidens holdes kun i processens hukommelse. Der findes ingen lagringsfunktion for adaptiv elevdata i 0.4.5 og ingen API, som eksporterer sessionstilstanden.

Hver session har både idle-timeout og en absolut, ikke-forlængelig levetid. Udløbne sessioner fjernes af en baggrundsproces og kontrolleres desuden før adgang til session-API. Eleven kan aktivt afslutte og nulstille sessionen.

## Adaptiv læring

Adaptiv evidens er begrænset til den aktuelle session, fag og emne. Systemet bruger midlertidige tællere/scores for tekst, visuel, lyd og aktivitet til at anbefale en undervisningsform **i samme session**. En ny session starter uden tidligere evidens.

Lyd bruger browserens lokale talesyntese. Visuel tilstand beder den konfigurerede LLM om tilgængelige tabeller, diagrammer og strukturer. Aktivitetstilstand beder om en sikker elevaktivitet. Ekstern billedgenerering ligger uden for grundpakken og må tilføjes eksplicit efter særskilt privacy-vurdering.

## Permanent konfiguration

Kun ikke-elevspecifik driftskonfiguration gemmes af ChromaLearn:

- `/etc/chromalearn/config.json` - IT/EDB-konfiguration
- `/var/lib/chromalearn/profiles/*.json` - læreroprettede undervisningsprofiler

Disse filer må ikke indeholde elevspecifik læringshistorik.
