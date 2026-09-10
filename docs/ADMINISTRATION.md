# Administration

ChromaLearn adskiller tre lokale roller:

- almindelig Linux-bruger: elev
- `chromalearn-teacher`: lærer
- `chromalearn-admin`: IT/EDB-administrator

Undervisningsprofiler er skolekonfiguration og gemmes under `/var/lib/chromalearn/profiles`. De kan definere fag, niveau, hjælpeniveau, vurderingssituation og tilladte undervisningsformer. De er **ikke elevprofiler** og må ikke indeholde elevspecifik læringshistorik.

Elevsamtaler, checkpoint-svar og adaptive læringsdata er sessionsbaserede i 0.4.5. Hver ny session starter uden læringsevidens fra tidligere sessioner.

IT/EDB-administratoren konfigurerer inference-endpoint og sessionsgrænser i `/etc/chromalearn/config.json` eller via den lokale admin-UI. Serveren gennemtvinger `persist_student_chats=false` og `adaptive_learning.session_only=true`, også hvis en håndlavet API-request forsøger andet.

## Anbefalet implementeringsforløb

1. Vælg og dokumentér godkendt inference-backend.
2. Verificér backend-, proxy- og containerlogning samt opbevaring.
3. Konfigurér lærer- og administratorgrupper i Linux.
4. Gennemgå `DATA_PROTECTION_SCREENING.md` med skolens relevante privacy-funktion/DPO.
5. Kør en kontrolleret canary-test for utilsigtet persistens.
6. Start kun en lille, afgrænset og lærer-superviseret pilot, når de nødvendige gates er grønne.

## Sprog

Dansk er referencesproget. Andre sprog bør tilføjes som særskilte oversættelser og menneskegodkendes før officiel brug. Se `OVERSAETTELSE_OG_LOKALISERING.md`.
