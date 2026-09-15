# ChromaLearn AI 0.4.5

ChromaLearn er et open-source pædagogisk AI-lag til skoler. Dansk er projektets standardsprog for brugerflade, dokumentation og evalueringsmateriale. Skolen vælger selv en OpenAI-kompatibel inference-server og AI-model, mens ChromaLearn styrer læringsforløb, lokale roller og privacy-grænser.

[📘 Læs den komplette beskrivelse af ChromaLearn](https://janus5g.github.io/ChromaLearn/about.html)

## ChromaLearn stopper ikke ved en .deb-pakke.

ChromaLearn kan bruges sammen med **ChromaPress**, den open-source Linux ISO-builder og verificerings-workbench, som nu er udgivet i en offentlig alpha-version.

Målet er en samlet, kontrollerbar skoleløsning, hvor ChromaLearn kan indgå i en Linux-installation, som skolen selv kan bygge, gennemgå og verificere.

AI til udvikling – ikke afvikling https://x.com/JanusR2022/status/2098309747854209443?s=20

## Komplet pakke til danske skoler

Den samlede løsning består af tre dele:

1. **ChromaLearn AI 0.4.5**
   Det pædagogiske AI-lag til elever, lærere og IT/EDB-administratorer.

2. **ChromaPress v1.0.0a72**
   Værktøj til analyse, tilpasning, opbygning og verificering af Linux-installationsimages.

   - **Windows 11 + WSL2:** [Download ChromaPress.exe](https://github.com/Janus5G/ChromaPress/releases/download/v1.0.0a72/ChromaPress.exe)
   - **Debian / Ubuntu:** [Download chromapress_1.0.0~a72-1_all.deb](https://github.com/Janus5G/ChromaPress/releases/download/v1.0.0a72/chromapress_1.0.0~a72-1_all.deb)
   - [ChromaPress-projektet på GitHub](https://github.com/Janus5G/ChromaPress)

   **SHA-256**
   - `ChromaPress.exe` — `4a7e1edd07b4b0cdeeb53fee0ecc0448ff2047e6d218a4e9a0b228d2ad79f76c`
   - `chromapress_1.0.0~a72-1_all.deb` — `b5fe5c1d96d3f7012666f8a2b07bf0384f562704a671981458ec118780a29d2c`

3. **ChromaLearn Skoleevalueringspakke v1.2.1 DA**
   Dansk test- og verifikationsmateriale til en kontrolleret teknisk, pædagogisk og privacy-/juridisk vurdering før en skolepilot.

   📦 **[Hent ChromaLearn Skoleevalueringspakke v1.2.1 DA](docs/ChromaLearn_Skoleevalueringspakke_v1.2.1_DA.zip)**

> **Vigtigt:** ChromaPress `v1.0.0a72` er en alpha-udgivelse. Skoleevalueringspakken er ikke et compliance-certifikat og er ikke juridisk rådgivning. Den konkrete skole skal selv verificere den faktiske installation, AI-/inference-backend, logging, infrastruktur og driftspraksis før bred anvendelse.

## Roller

Rollerne bestemmes af den Linux-konto, der starter programmet:

- **Elev**: almindelig Linux-bruger. Kan kun bruge aktive læringsprofiler.
- **Lærer**: medlem af `chromalearn-teacher`. Kan oprette og redigere pædagogiske profiler.
- **IT/EDB-administrator**: medlem af `chromalearn-admin`. Kan konfigurere og teste inference-backend. Administratorer bør normalt også være medlem af lærergruppen, hvis de administrerer undervisningsprofiler.

Der findes ingen browserknap, som kan skifte rolle.

## Pædagogisk læringsforløb

`eget forsøg -> diagnose -> hint -> refleksion -> konsolidering`

Undervisningsprofiler kan styre fag, klassetrin/niveau, hjælpeniveau 1-4, træning/lektier/aflevering/prøve, analoge eksempler, kildepolitik og tilladte undervisningsformer.

## Privacy som standard

Elevsamtaler, checkpoint-svar og adaptive læringsdata findes kun i programmets hukommelse under den aktive session. ChromaLearn afviser forsøg på at slå permanent elevlagring til. Der findes ingen elevsessions-eksport-API.

API-nøgler gemmes ikke som almindelige ChromaLearn-konfigurationsværdier. Bearer-autentifikation kan i stedet læse et token fra en navngivet miljøvariabel.

Denne egenskab gælder ChromaLearn selv. Skolen skal særskilt verificere modelserver, proxy/container-logs, journald/syslog, swap/hibernation, crash dumps, backup, snapshots, browser og tredjepartstelemetri.

## AI-backend

Standardendpoint:

`http://127.0.0.1:8000/v1/chat/completions`

Enhver kompatibel server kan konfigureres af IT/EDB-administratoren. AI-modellen er ikke bundlet i pakken.

## Installation

```bash
sudo apt install ./chromalearn_0.4.5_all.deb
```

Tildel roller:

```bash
sudo usermod -aG chromalearn-teacher laererbrugernavn
sudo usermod -aG chromalearn-admin adminbrugernavn
```

Log ud og ind igen efter ændringer i gruppemedlemskab.

## Indbygget developer-repository

`.deb`-pakken installerer et komplet Git-repository i:

`/usr/share/chromalearn/developer-repo`

En EDB-ansvarlig eller udvikler kan lave en skrivbar kopi med:

```bash
chromalearn-export-source ~/chromalearn-dev
cd ~/chromalearn-dev
git status
git log --oneline -1
```

Repositoryet indeholder kildekode, tests, dokumentation, eksempler, Debian-packaging og build-script. Der er ingen remote sat op, så skolen selv bestemmer, hvor en fork offentliggøres.

## Dansk som referencesprog og oversættelser

Dansk er det officielle referencesprog i denne release. Kommandoen `chromalearn-translate` kan hjælpe udviklere med at lave **kladder** til andre sprog ved hjælp af den AI-backend, skolen selv har valgt.

Eksempel:

```bash
chromalearn-translate docs/ARCHITECTURE.md --language English --code en
```

Oversættelsen markeres som maskinoversat kladde og må ikke betragtes som juridisk eller fagligt godkendt, før et menneske har gennemgået den. Brug aldrig elevdata, sessionsudtræk eller andre personoplysninger som input til oversættelsesværktøjet.

Se `docs/OVERSAETTELSE_OG_LOKALISERING.md`.

## Adaptiv multimodal læring

ChromaLearn tildeler **ikke** eleven en fast læringsstil. I den aktive session kan systemet midlertidigt sammenholde læringsudbytte med fag, emne og undervisningsform.

Understøttede former:

- `text`: kort, guidet tekst.
- `visual`: tabeller, strukturer, tidslinjer, flows og tekst/ASCII-diagrammer fra den valgte model.
- `audio`: lytteorienterede svar samt lokal browser-tekst-til-tale uden obligatorisk cloud-tjeneste.
- `activity`: sikre praktiske aktiviteter, hvor eleven selv skal gøre eller observere noget.

Eleven kan få en kort transfer-/forståelsestest med en ny tilsvarende opgave. Midlertidige scores bruges kun inde i den aktive session og skrives ikke til en permanent elevprofil.

## Om billeder

Grundpakken har ingen skjult ekstern billedgenerator. Visuel tilstand bruger modelgenererede tabeller, diagrammer og strukturer. Skoler eller bidragydere kan senere tilføje billedgenerering som en eksplicit integration efter egen privacy- og sikkerhedsvurdering.

## Udvikling og test

```bash
python3 -m unittest discover -s tests -v
./build_deb.sh
```

## Opgradering fra tidligere testudgaver

ChromaLearn 0.4.5 udfører ingen automatisk oprydning af data fra tidligere udviklings-/testudgaver. Hvis en maskine har kørt en pre-0.4 testversion, skal skolens administrator gennemgå værten efter skolens egen dokumenterede slette- og opbevaringsprocedure og håndtere eventuelle historiske testdata uden for ChromaLearn.

Til en kontrolleret canary-test kan `chromalearn-privacy-scan <TEST-MARKØR>` anvendes på godkendte filområder. Brug aldrig rigtige elevoplysninger som testmarkør.

## Evaluering og test for danske skoler

ChromaLearn er udviklet til at blive testet og verificeret i skolens eget miljø, før det tages bredt i brug.

Evalueringspakken indeholder materiale til skoleledelse, lærere, IT/EDB-ansvarlige og DPO/dataansvarlige samt vejledning til pilotafprøvning, databeskyttelse og teknisk verifikation.

📦 **[Hent ChromaLearn Skoleevalueringspakke v1.2.1 DA](docs/ChromaLearn_Skoleevalueringspakke_v1.2.1_DA.zip)**

## Licens

MIT, Copyright (c) 2026 Janus Rokkjær.
