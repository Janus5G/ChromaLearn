# ChromaLearn AI 0.4.5

ChromaLearn er et open-source pædagogisk AI-lag til skoler. Dansk er projektets standardsprog for brugerflade, dokumentation og evalueringsmateriale. Skolen vælger selv en OpenAI-kompatibel inference-server og AI-model, mens ChromaLearn styrer læringsforløb, lokale roller og privacy-grænser.

[📘 Læs den komplette beskrivelse af ChromaLearn](https://janus5g.github.io/ChromaLearn/about.html)
<blockquote class="twitter-tweet"><p lang="da" dir="ltr">ChromaLearn stopper ikke ved en .deb-pakke.<br><br>Det bliver også en del af ChromaPress – min custom Linux ISO-builder under udvikling.<br><br>Målet: Muligheden for at bygge en komplet, kontrolleret skoleinstallation med ChromaLearn integreret fra starten.<br><br>AI til udvikling – ikke afvikling</p>&mdash; Janus Rokkjær - Github-Janus5G (@JanusR2022) <a href="https://x.com/JanusR2022/status/2098309747854209443?ref_src=twsrc%5Etfw">September 11, 2026</a></blockquote> <script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>

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

📦 **[Hent ChromaLearn Skoleevalueringspakke v1.2.1 DA](docs/ChromaLearn_Skoleevalueringspakke_v1.2.1_DA.zip)**

Evalueringspakken indeholder materiale til skoleledelse, lærere, IT/EDB-ansvarlige og DPO/dataansvarlige samt vejledning til pilotafprøvning, databeskyttelse og teknisk verifikation.

## Licens

MIT, Copyright (c) 2026 Janus Rokkjær.
