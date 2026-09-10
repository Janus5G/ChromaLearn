# Privacy-drift og sessionsbaseret implementering

ChromaLearn 0.4.5 er designet, så elevens samtaleindhold og adaptive læringsevidens kun findes i processens hukommelse under den aktive session. ChromaLearn tilbyder ingen API til eksport af elevsessionen og skriver ikke elevchat eller adaptiv evidens til disk.

Denne egenskab gælder ChromaLearn selv. Skolen kan først beskrive **hele** løsningen som sessionsbaseret, når den komplette implementering er gennemgået.

## Kontrol før pilot

IT/EDB-administratoren bør verificere:

1. At den valgte inference-server ikke logger prompts/svar ud over skolens godkendte opbevaringspolitik. Antag aldrig standardindstillinger - kontrollér konkret produkt og version.
2. At reverse proxies, API-gateways og container-runtimes ikke logger request-/response-body med elevindhold.
3. At systemd/journald/syslog ikke modtager elevindhold. ChromaLearn deaktiverer sin HTTP access-log og skriver ikke bevidst request-body til stdout/stderr.
4. At core dumps er deaktiveret for ChromaLearn og, hvor relevant, inference-tjenesten.
5. At swap og hibernation er vurderet. RAM-data kan blive skrevet til lager af operativsystemet. Brug skolens godkendte krypterede swap-konfiguration eller deaktivér swap/hibernation, hvis trusselsmodellen kræver det.
6. At midlertidige mapper, tracing/APM, browserudvidelser, endpoint-security og debugværktøjer ikke opsamler request-/response-data utilsigtet.
7. At backups og snapshots ikke fastholder midlertidigt elevindhold.
8. At netværkstransport til en fjern inference-server er beskyttet, og at roller/databehandlerforhold er vurderet.

## Sessionslivscyklus

Standardgrænser:

- idle-timeout: 20 minutter
- absolut sessionslevetid: 60 minutter

Den absolutte levetid forlænges ikke af fortsat aktivitet. En baggrundsproces fjerner udløbne sessioner. API-adgang til en udløbet session fejler lukket. Eleven kan desuden vælge **Afslut og nulstil session**.

Lukning af processen fjerner programmets hukommelsestilstand. Browserens side-luk forsøger desuden best-effort at sende et session-end-kald, men serverens hårde timeout er den autoritative oprydningsmekanisme.

## Verifikation af persistens

Brug i et kontrolleret testmiljø en unik canary-sætning uden rigtige elevdata, fx:

`CHROMALEARN-CANARY-7f3c-test-only`

Kør en læringssession med markøren, afslut sessionen, stop ChromaLearn og undersøg godkendte fil-/logområder med `chromalearn-privacy-scan`.

En ren filscan viser, at markøren ikke blev fundet i de scannede almindelige filer. Det beviser ikke fravær fra rå swapblokke, hibernation, fjernservere, hypervisor-snapshots, hardware-caches eller tredjepartstelemetri; de områder skal verificeres særskilt.

## Opgradering fra tidligere testudgaver

ChromaLearn 0.4.5 indeholder ingen automatisk migration eller sletterutine for data, der kan være skabt af tidligere udviklings-/testversioner. Hvis en maskine tidligere har kørt en pre-0.4 testversion, skal administratoren foretage en dokumenteret host-gennemgang og eventuel sletning **uden for ChromaLearn** efter skolens egne procedurer for opbevaring, backup og hændelseshåndtering.
