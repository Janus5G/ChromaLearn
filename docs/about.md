---
layout: default
title: ChromaLearn
description: AI som hjælper eleven med at lære – ikke med at springe læringen over
---
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

ChromaLearn er et open source-baseret AI-læringsværktøj udviklet med ét grundlæggende formål:

**Eleven skal bruge kunstig intelligens til at lære, forstå og tænke selv – ikke til at få lavet arbejdet for sig.**

Programmet er udviklet særligt med skoler og undervisningsmiljøer for øje. Det kombinerer pædagogisk styret AI-hjælp med klare roller for elever, lærere og IT-ansvarlige samt en teknisk arkitektur, hvor elevens læringssession er midlertidig og ikke bliver til en permanent elevprofil.

ChromaLearn er ikke tænkt som en erstatning for læreren. Læreren fastlægger fortsat de pædagogiske rammer, undervisningsmålet og graden af hjælp. AI'en fungerer som et værktøj inden for disse rammer.

---

## Hvorfor ChromaLearn?

Generativ AI giver elever adgang til meget stærke værktøjer. Den samme teknologi kan imidlertid bruges på to meget forskellige måder.

En elev kan bede en AI om at skrive en aflevering, løse en ligning eller producere et færdigt svar. Resultatet kan se flot ud, uden at eleven nødvendigvis har lært noget.

Eller AI kan bruges som en tutor, der spørger:

- Hvad ved du allerede?
- Hvad har du prøvet?
- Hvor tror du problemet ligger?
- Hvilken regel kunne være relevant her?
- Kan du forklare, hvorfor dit svar giver mening?
- Kan du bruge samme metode på en ny opgave?

ChromaLearn er bygget omkring den anden tilgang.

Det betyder, at AI'en ikke blot får en generel instruktion om at "være pædagogisk". Selve programmet styrer elevens læringsforløb gennem forskellige trin.

Et typisk forløb kan være:

**Eget forsøg → diagnose → begrænset hint → refleksion → konsolidering**

Eleven forventes derfor at deltage aktivt i problemløsningen.

---

## AI'en skal hjælpe – ikke aflevere

I elevtilstanden er der ikke en almindelig "vis facit"-funktion.

Hvis en elev forsøger at få systemet til at skrive en færdig aflevering eller omgå læringsreglerne, er ChromaLearn designet til i stedet at føre eleven tilbage til læringsprocessen.

AI'en kan eksempelvis:

- stille sokratiske spørgsmål
- forklare et begreb
- give et begrænset hint
- identificere en misforståelse
- vise en tilsvarende metode med et andet eksempel
- bede eleven forklare sin tankegang
- kontrollere elevens forståelse med en ny opgave

Formålet er ikke at forhindre elever i at få hjælp.

Formålet er at gøre hjælpen læringsfremmende.

---

## Forskellige elever – forskellige fag – forskellige metoder

ChromaLearn bygger ikke på idéen om, at et barn permanent er én bestemt "læringstype".

Den samme elev kan have meget forskellige behov i forskellige fag.

En elev kan eksempelvis lære matematik bedst gennem korte logiske trin, mens samme elev i engelsk får større udbytte af dialog og oplæsning. I naturfag kan en praktisk aktivitet være mere effektiv, mens historie kan have gavn af tidslinjer, strukturer og visuelle sammenhænge.

Derfor kan ChromaLearn tilpasse undervisningsformen inden for den aktuelle session.

Systemet kan arbejde med blandt andet:

- tekst og forklaring
- strukturer og diagrammer
- lyd og oplæsning
- spørgsmål og dialog
- praktiske aktiviteter
- eksempler
- repetition
- forståelsestest

Tilpasningen handler ikke om at stemple eleven.

Den handler om at finde en hensigtsmæssig måde at forklare det konkrete stof på.

---

## Test af forståelse

Efter vejledning kan eleven gennemføre en lille forståelses- eller transferopgave.

Det er ikke den oprindelige opgave igen.

AI'en kan i stedet stille en ny, tilsvarende opgave for at undersøge, om eleven kan anvende det lærte i en ny sammenhæng.

Dermed bliver spørgsmålet ikke kun:

**"Fik eleven det rigtige svar?"**

men også:

**"Har eleven forstået metoden godt nok til selv at bruge den igen?"**

---

## Ingen permanent adaptiv elevprofil

Et centralt designprincip i ChromaLearn er, at den adaptive læring foregår inden for den aktive session.

Elevens samtale, checkpoint-svar og adaptive læringsresultater bliver ikke til en permanent profil, der følger eleven fra gang til gang.

Når sessionen afsluttes, udløber eller programmet genstartes, nulstilles den elevspecifikke sessionshukommelse.

Det er et bevidst designvalg.

Eleven skal derfor også kunne se tydeligt, at ChromaLearn ikke forventes at "kende eleven" næste gang.

---

## En vigtig teknisk forskel

Når ChromaLearn beskrives som sessionsbaseret, gælder det ChromaLearns egen behandling.

Skolen skal stadig vurdere hele den tekniske installation.

Hvis AI-modellen eksempelvis drives af:

- en lokal modelserver
- en central kommunal server
- en ekstern AI-leverandør
- en containerplatform
- en reverse proxy

kan disse komponenter have deres egen logning eller databehandling.

IT- og dataansvarlige skal derfor undersøge den valgte samlede installation.

ChromaLearn er bevidst konstrueret, så skolen selv kan vælge denne infrastruktur.

---

## Skolen vælger selv AI'en

ChromaLearn er ikke bundet til én bestemt AI-model eller AI-leverandør.

Programmet kan arbejde mod en kompatibel AI-server, som skolen selv vælger.

Det kan eksempelvis være:

- en lokal AI-model på skolens eget udstyr
- en fælles kommunal eller institutionel modelserver
- en godkendt ekstern tjeneste
- en anden OpenAI-kompatibel inference-server

Dermed kan skolen selv vælge løsning ud fra krav til blandt andet:

- databeskyttelse
- pris
- performance
- faglig kvalitet
- dansk sprog
- lokal drift
- leverandørpolitik

ChromaLearn kan derfor betragtes som det pædagogiske lag mellem eleven og den AI-infrastruktur, skolen vælger.

---

## Tre tydelige roller

### Elev

Eleven arbejder inden for de regler og undervisningsprofiler, som skolen og læreren har fastlagt.

Eleven kan ikke selv ændre centrale sikkerheds- eller administrationsindstillinger.

### Lærer

Læreren bestemmer de pædagogiske rammer.

Det kan blandt andet omfatte:

- fag
- klassetrin
- emne
- hjælpeniveau
- undervisningsform
- om der arbejdes med træning, lektier eller andre opgavetyper
- hvilke typer eksempler AI'en må anvende
- hvilke ressourcer der må benyttes

Læreren behøver ikke være AI-specialist for at anvende de almindelige funktioner.

### IT/EDB-administrator

IT-administratoren håndterer den tekniske installation.

Det kan blandt andet være:

- valg af AI-server
- model
- netværksopsætning
- adgangskontrol
- lokale sikkerhedsindstillinger
- driftsmiljø
- kontrol af logning
- installation og opdatering

Rolleadskillelsen er bevidst. En lærer skal ikke nødvendigvis administrere servere, og en IT-medarbejder skal ikke nødvendigvis bestemme undervisningsmetoden.

---

## Læreren beholder kontrollen

ChromaLearn er ikke designet til selvstændigt at træffe væsentlige beslutninger om en elev.

AI'en skal være et undervisningsværktøj.

I den nuværende ramme er ChromaLearn ikke tiltænkt brug til eksempelvis:

- automatisk karaktergivning
- adgang eller optagelse
- automatisk progression mellem niveauer
- disciplinære afgørelser
- automatisk elevsortering
- eksamensovervågning
- følelsesgenkendelse

Hvis en institution ønsker væsentligt andre anvendelser, skal de vurderes særskilt.

---

## Privacy by design

Databeskyttelse er forsøgt gjort til en del af teknikken frem for alene en tekst i en privatlivspolitik.

ChromaLearn er blandt andet udviklet omkring:

- sessionsbaseret elevhukommelse
- ingen permanent adaptiv elevprofil
- ingen almindelig eksportfunktion til elevens sessionsprofil
- sessionstimeout
- mulighed for eksplicit at afslutte og nulstille sessionen
- begrænset applikationslogning
- rollebaserede rettigheder
- mulighed for lokal AI-drift
- åben kildekode, der kan inspiceres

Det betyder ikke, at installation af programmet automatisk gør enhver anvendelse juridisk godkendt.

Skolen er stadig ansvarlig for at vurdere den konkrete anvendelse, dens tekniske miljø og gældende regler.

---

## Materiale til skoleledelse og dataansvarlige

ChromaLearn leveres ikke kun som program.

Der findes også en dansk School Evaluation Pack, der er beregnet til vurdering før egentlig anvendelse.

Den indeholder blandt andet materiale til:

- skoleledelsen
- lærere
- IT/EDB-ansvarlige
- DPO/dataansvarlige
- pilotafprøvning
- privacy-verifikation
- risikovurdering
- elevinformation
- forældreinformation
- hændelses- og stopprocedurer

Formålet er bevidst ikke at fortælle skolen:

**"Dette produkt er godkendt."**

Tilgangen er i stedet:

> **"Her er programmet, arkitekturen, kildekoden, testværktøjerne og dokumentationen. Undersøg løsningen i jeres eget miljø, og træf en dokumenteret beslutning."**

---

## Test før bred anvendelse

Den anbefalede indførelse af ChromaLearn er en begrænset pilot.

Eksempelvis:

- én eller få lærere
- et afgrænset fag
- en begrænset periode
- en mindre elevgruppe
- involvering af relevant IT- og dataansvarlig
- evaluering før udvidelse

Dermed kan skolen undersøge både den pædagogiske værdi og de tekniske konsekvenser, før løsningen eventuelt udbredes.

---

## Open source

ChromaLearn er udviklet som open source.

Det betyder, at interesserede skoler, kommuner, undervisere, datamatikere og andre udviklere kan undersøge, teste og videreudvikle systemet.

Kildekoden følger med projektet, og Debian-installationspakken indeholder også et developer-repository, der kan kopieres ud som arbejdsgrundlag.

Det kan være særligt relevant på skoler, hvor IT-/EDB-ansvarlige eller undervisere selv har programmeringserfaring.

Åbenheden har også et kontrolmæssigt formål:

Kritiske egenskaber behøver ikke alene accepteres på baggrund af producentens beskrivelse. De kan inspiceres og testes.

---

## Dansk som referencesprog

ChromaLearn er først og fremmest udviklet med danske skoler for øje.

Dansk er derfor programmets og den centrale dokumentations referencesprog.

Projektet understøtter samtidig videre lokalisering.

Der findes et oversættelsesværktøj, som kan hjælpe udviklere eller institutioner med at fremstille oversættelseskladder ved hjælp af deres valgte AI-backend.

Maskinoversat materiale skal gennemgås af et menneske, før det betragtes som godkendt materiale.

Det gælder særligt juridiske, sikkerhedsmæssige, privacy-relaterede og pædagogiske tekster.

---

## Hvad koster ChromaLearn?

Grundprojektet er open source.

Skolens reelle omkostninger afhænger derfor især af den valgte AI-infrastruktur.

Hvis skolen allerede råder over en egnet lokal eller central AI-server, kan ChromaLearn benytte denne.

Hvis der benyttes en ekstern AI-tjeneste, kan der være udgifter til API-kald eller drift hos den valgte leverandør.

ChromaLearn er bevidst udviklet, så programmet ikke kræver et bestemt kommercielt AI-abonnement.

---

## Hvad ChromaLearn ikke forsøger at være

ChromaLearn er ikke:

- en automatisk lærer
- en karakterrobot
- en erstatning for pædagogisk vurdering
- en permanent elevprofil
- et overvågningssystem
- en låst AI-platform
- en tjeneste, hvor udvikleren nødvendigvis modtager elevdata
- et løfte om juridisk compliance alene ved installation

Det er et værktøj til kontrolleret og pædagogisk brug af generativ AI.

---

## Hvad læreren får ud af det

For læreren er målet, at AI bliver lettere at bruge ansvarligt.

I stedet for at hver lærer skal opfinde sin egen systemprompt eller forsøge at kontrollere en almindelig chatbot, giver ChromaLearn en fast ramme omkring brugen.

Læreren kan koncentrere sig om:

- hvad eleven skal lære
- hvor meget hjælp der er passende
- hvordan undervisningen skal tilrettelægges
- om eleven faktisk forstår stoffet

AI-teknikken ligger i baggrunden.

---

## Hvad skoleledelsen får ud af det

For skoleledelsen er ChromaLearn først og fremmest tænkt som en mere kontrollerbar måde at undersøge AI i undervisningen.

Løsningen giver mulighed for:

- afgrænset pilotafprøvning
- eget valg af AI-infrastruktur
- teknisk inspektion
- åben kildekode
- rollefordeling
- dokumenteret privacy-tilgang
- materiale til intern vurdering
- mulighed for at stoppe eller ændre anvendelsen

Det giver et bedre grundlag for en ledelsesmæssig beslutning end blot at åbne adgang til en almindelig offentlig chatbot.

---

## Hvad IT/EDB-ansvarlige får ud af det

IT-medarbejdere får adgang til både det installerbare program og kildekoden.

De kan derfor:

- undersøge arkitekturen
- kontrollere konfiguration
- tilslutte institutionens valgte AI-model
- efterprøve privacy-egenskaber
- gennemgå kode og tests
- bygge pakken selv
- bidrage med forbedringer
- tilpasse installationen til lokale krav

Projektet er bevidst lavet, så teknisk kompetente skoler ikke bliver låst ude af deres eget system.

---

## Fremtidig mulighed: kontrolleret AI-udvidelse

Efter en længere evalueringsperiode kan der senere udvikles et særskilt AI-baseret udviklingsmodul.

**Denne funktion findes ikke som en del af den nuværende ChromaLearn-release.**

Tanken er, at en lærer i fremtiden kan beskrive en ønsket funktion i almindeligt sprog.

AI'en skal derefter ikke bare "kode løs".

En sikker proces kan eksempelvis være:

**Lærerønske → pædagogisk kontrol → præcis AI-specifikation → sikkerheds- og privacykontrol → minimal kodeændring → automatiske tests → ændringslog → pædagogisk evaluering → menneskelig godkendelse → frigivelse**

AI'en må således være kreativ omkring løsningen, men ikke omkring de regler, den skal overholde.

Centrale krav som privacy, rollebeskyttelse, sikkerhed, pædagogiske rammer og obligatoriske tests kan senere defineres som maskinlæsbare regler, som AI'en ikke selv har adgang til at ændre.

Alle foreslåede ændringer skal kunne spores.

Loggen kan blandt andet dokumentere:

- hvad læreren bad om
- AI'ens specifikation
- hvorfor løsningen blev valgt
- hvilke filer der blev ændret
- den præcise kodeforskel
- hvilke tests der blev udført
- resultatet af sikkerheds- og privacykontrol
- den pædagogiske vurdering
- hvem der godkendte ændringen
- hvilken programversion ændringen indgår i

En AI-genereret funktion må aldrig gå direkte ud til elever.

Den skal først gennemgå alle krævede kontroller og menneskelig godkendelse.

Hvis skolen allerede har en egnet AI-model eller AI-tjeneste, er målet, at samme infrastruktur kan anvendes. En eventuel betaling for en sådan fremtidig udvidelse behøver derfor primært at dække reelle AI-/API- eller driftsomkostninger frem for at skabe en unødvendig ekstra abonnementsbarriere.

---

## Grundprincippet

ChromaLearn bygger i sidste ende på en enkel idé:

> **AI i skolen bør ikke vurderes på, hvor meget arbejde den kan udføre for eleven, men på hvor godt den kan hjælpe eleven med selv at lære at udføre arbejdet.**

Teknologien skal understøtte læreren.

Læreren skal bevare den pædagogiske kontrol.

Eleven skal bevare sin aktive rolle i læringen.

Og skolen skal bevare kontrollen over teknologi, data og anvendelse.

---

## Kort fortalt

**ChromaLearn er open source AI til undervisning, hvor eleven stadig skal tænke selv.**

Det kombinerer pædagogisk styret AI-hjælp, sessionsbaseret elevdata, skolekontrolleret AI-infrastruktur, lærer- og administratorroller, adaptiv hjælp uden permanent elevprofil samt en evalueringsramme, der gør det muligt for skolen selv at teste og vurdere løsningen før bred anvendelse.

**Test. Verificér. Lær.**
