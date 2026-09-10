# Juridisk og etisk afgrænsning

ChromaLearn er open-source undervisningssoftware. Projektet driver ikke en obligatorisk inference-tjeneste, brugerkontotjeneste eller telemetri-backend, og softwaren indeholder ingen funktion, som sender elevdata til ChromaLearn-udviklerne. Den anvendende organisation vælger og driver eller kontraherer selv sit inference-endpoint.

Denne arkitektur kan begrænse udviklerprojektets involvering i behandling af personoplysninger, især ved fuldt lokal drift. Arkitekturen afgør dog ikke alene, hvem der juridisk er dataansvarlig, fælles dataansvarlig, databehandler, provider eller deployer. Roller afhænger af den faktiske brug, formål, midler, kontrakter og implementering. Skolen/kommunen bør dokumentere vurderingen.

## GDPR-designposition

ChromaLearn 0.4.5 er designet med dataminimering og opbevaringsbegrænsning:

- ingen permanent elevchat
- ingen permanent adaptiv elevprofil
- ingen elevsessions-eksport-API
- hård idle- og absolut sessionstimeout
- eksplicit sessionsnulstilling
- ingen HTTP access-log med requests i ChromaLearn
- lærer-/root-ejede undervisningsprofiler er konfiguration og ikke elevprofiler

Danske skoler skal stadig fastlægge retsgrundlag, opfylde oplysningspligt, beskytte børn som registrerede, dokumentere retention i hele infrastrukturen og vurdere behovet for DPIA.

## EU AI Act-designposition

ChromaLearn er bevidst begrænset væk fra summativ eller konsekvensfuld beslutningsbrug: grundpakken har ingen funktion til karakterer, optagelse, placering, progression eller disciplin. Lærerpolitik og menneskeligt tilsyn er centrale.

Annex III(3)(b) omfatter imidlertid AI-systemer, der er beregnet til at evaluere læringsresultater, herunder når resultater bruges til at styre læringsprocessen. Den valgfrie formative checkpoint-funktion vurderer et transfer-svar og kan anbefale en undervisningsform. Den anvendende organisation skal derfor vurdere den konkrete tilsigtede anvendelse og klassifikation frem for at stole på en generel lavrisiko-påstand.

Kontrollér altid den aktuelle konsoliderede EU-tekst og national vejledning på tidspunktet for implementering.

## Centrale kilder

- Forordning (EU) 2024/1689, konsolideret tekst: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- Datatilsynet - skoler og daginstitutioner: https://www.datatilsynet.dk/regler-og-vejledning/skoler-og-daginstitutioner
- Datatilsynet - databeskyttelse gennem design og standardindstillinger: https://www.datatilsynet.dk/regler-og-vejledning/behandlingssikkerhed/databeskyttelse-gennem-design-og-standardindstillinger
