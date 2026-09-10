# Oversættelse og lokalisering

## Grundprincip

Dansk er ChromaLearns officielle referencesprog for danske skolepiloter. Andre sprog er nyttige for internationale bidragydere og skoler, men de må ikke erstatte den danske reference uden en bevidst beslutning.

## Indbygget AI-assisteret oversættelse

Kommandoen `chromalearn-translate` kan oversætte statiske `.md`, `.txt` og `.json`-filer ved hjælp af den OpenAI-kompatible AI-backend, der allerede er konfigureret i ChromaLearn.

Eksempel:

```bash
chromalearn-translate docs/ARCHITECTURE.md --language English --code en
```

Standardoutput placeres i `translations/<sprogkode>/` og markeres som **MASKINOVERSAT KLADDE - KRÆVER MENNESKELIG GODKENDELSE**.

## Sikkerhedsgrænser

Oversættelsesværktøjet er kun beregnet til statiske projekt-, UI- og dokumentationsfiler. Det må ikke bruges til:

- elevchat eller sessionsdata
- checkpoint-svar
- elevopgaver med personoplysninger
- logs eller incident-data med personoplysninger
- hemmeligheder, API-nøgler eller credentials

Hvis den valgte AI-backend er ekstern, sendes den fil, der oversættes, til denne backend. Det er derfor brugerens/skolens ansvar kun at oversætte materiale, der må sendes til den valgte tjeneste.

## Juridiske og compliance-tekster

AI-oversættelser af juridiske, privacy- eller elev-/forældretekster er kun kladder. De skal gennemgås af en kompetent person før officiel brug. En oversættelse må ikke markeres som officiel alene, fordi AI'en har genereret den.

## Bidrag til Git

Anbefalet struktur:

```text
translations/
  en/
  de/
  sv/
```

En bidragyder bør i commit/PR angive:

- kildesprog og mål­sprog
- om AI blev brugt
- hvilken version af kildeteksten oversættelsen bygger på
- hvem der har menneskegennemgået teksten
- dato for godkendelse
