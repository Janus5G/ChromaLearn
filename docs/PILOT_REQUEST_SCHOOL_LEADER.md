# Udkast - anmodning til skoleleder om begrænset ChromaLearn-pilot

**Emne: Anmodning om begrænset og lærer-superviseret pilot af ChromaLearn AI**

Kære [skoleleder]

Jeg vil gerne høre, om skolen kunne være interesseret i at evaluere en begrænset pilot af ChromaLearn AI, et open-source pædagogisk AI-værktøj udviklet til at hjælpe elever med generativ AI som vejledning frem for som en generator af færdige besvarelser.

ChromaLearn adskiller elev-, lærer- og IT/EDB-administratorroller. Læreren kan definere fag, niveau, hjælpeniveau og tilladte læringsformer, mens skolens IT/EDB-ansvarlige selv vælger AI-model og inference-server. Projektet driver ikke en obligatorisk cloudtjeneste, og softwaren indeholder ikke en funktion, der sender elevdata til ChromaLearn-udviklerne.

Den aktuelle version bygger på midlertidige elevsessioner. Elevchat, transfer-/forståelsestests og adaptiv læringsevidens findes kun i hukommelsen under den aktive session og nulstilles, når sessionen afsluttes eller udløber. Der findes ingen elevsessions-eksport-API, og systemet er ikke beregnet til karakterer, optagelse, placering, progression eller disciplinære afgørelser.

Før elevtest foreslås det, at skolens/kommunens dataansvarlige funktion og, hvor relevant, DPO gennemgår den medfølgende screening. IT/EDB-administratoren bør desuden verificere hele infrastrukturen, herunder AI-server, logning, proxy/container-opsætning, swap/hibernation, crash dumps og backups.

En første pilot bør være lille, tidsafgrænset og lærer-superviseret med ikke-følsomt undervisningsmateriale. Formålet er at vurdere pædagogisk nytte, om eleverne bliver hjulpet til selvstændig tænkning, og om de tekniske privacy-kontroller fungerer som dokumenteret.

Kildekode, tests, Debian-pakke, checksums og evalueringsmateriale stilles til rådighed, så skolen selv kan inspicere og verificere løsningen.

Med venlig hilsen

Janus Rokkjær  
ChromaLearn AI - open-source projekt
