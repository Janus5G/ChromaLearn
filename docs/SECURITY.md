# Sikkerheds- og privacy-kontroller

ChromaLearn 0.4.5 bruger fail-closed standarder for elevdata.

- Permanent lagring af elevchat kan ikke aktiveres via applikationens API.
- Adaptiv læringsevidens er kun sessionsbaseret og har ingen disk-writer.
- Der findes ingen elevsessions-eksport-API.
- HTTP access-log er deaktiveret i ChromaLearn.
- Idle- og absolutte sessionsgrænser begrænser levetiden for data i hukommelsen.
- Aktiv afslut/nulstilling fjerner sessionens objekt fra serverens hukommelse.
- Lærer- og administratorfunktioner bestemmes af Linux-grupper og ikke af en browserangivet rolle.
- API-hemmeligheder gemmes ikke som almindelige ChromaLearn JSON-værdier; bearer-konfiguration kan læse token fra en miljøvariabel.

Kontrollerne hærder ikke automatisk den valgte inference-server, reverse proxy, container-runtime, operativsystemets swap/hibernation, core dumps, backups, browser eller tredjepartstelemetri. Disse dele er separate tillidsgrænser og skal vurderes af skolen.

Se `PRIVACY_OPERATIONS.md` for implementeringskontrol og brug kun ikke-personlige canary-markører ved test.
