# Ændringslog

## 0.4.5 - 2026-09-10

- Dansk gjort til officielt referencesprog for README, developer-dokumentation og skolemateriale.
- Tilføjet `chromalearn-translate` til AI-assisterede oversættelseskladder af statiske dokumentations-/lokaliseringsfiler.
- Oversættelser mærkes som kladder og kræver menneskelig godkendelse før officiel brug.
- Oversættelsesværktøjet er eksplicit afgrænset fra elevsessioner og personoplysninger.
- Ingen ændringer i læringsmotor, roller eller sessionsbaseret privacy-model fra 0.4.4.

## 0.4.4 - 2026-09-10

- Fjernede forældede dokumentationsudsagn om automatisk oprydning ved opgradering.
- Præciserede at oprydning på ældre testværter er administratorstyret uden for ChromaLearn.
- Privacy-tests validerer kun aktuelle privacy-egenskaber og packaging-struktur.
- `.pytest_cache` udelukkes fra det indbyggede developer-repository.

## 0.4.3 - 2026-09-10

- Fjernede tidligere package-side migrationshelper og post-install cleanup-hook.
- Adaptiv elevdata er fortsat RAM-only og sessionsbaseret.

## 0.4.1 - 2026-09-10

- Strammede privacy-audit-klarhed og release-kontroller.

## 0.4.0 - 2026-09-10

- Adaptiv læringsevidens ændret til sessionshukommelse.
- Tilføjede idle-/absolut sessionstimeout og eksplicit reset.
- Tilføjede privacy-hardening, canary-scan, DPO-screening og juridisk/etisk afgrænsning.

## 0.3.0

- Tilføjede rolleopdeling elev/lærer/admin og adaptiv multimodal læring.
