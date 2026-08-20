"""Tværfaglige koblinger og forsvar-dit-valg-cases til Forsvarstræneren.

Hvorfor en ny bank
------------------
De øvrige banker spørger inden for ét fag ad gangen. Men 3. semester prøves
tværfagligt: fire fag afgøres i én prøve, og casen kræver, at transportansvar
og projektstyring kobles på det samme flow som Lean, Chopra og lagerdesign.
Det er præcis dét, ingen af de eksisterende tilstande træner.

To lister:

  KOBLINGER   — en situation, der ikke kan besvares fra ét fag. Kortet siger
                hvilke fag der skal med, og modelsvaret VISER koblingen frem
                for at give et facit. Der er sjældent ét rigtigt svar; der er
                et argument, der hænger sammen på tværs.

  VALG        — «du valgte X, hvorfor ikke Y?». Til det mundtlige forsvar,
                hvor man forsvarer sin EGEN rapport, ikke pensum. Kortene
                træner formen: vælg position, begrund, anerkend afvejningen,
                hold fast. De virker uden at kende den konkrete rapport.

Ingen virksomheds- eller personnavne — værktøjet er et generelt
opslagsværktøj, ikke et case-referat.
"""

# (situation, [fag der skal kobles], [de spørgsmål eksaminator stiller],
#  modelsvar der viser koblingen)
KOBLINGER = [
    (
        "En virksomhed lægger produktionen om til mindre batches og "
        "hyppigere leveringer til kunderne.",
        ["Produktion", "Distribution", "Jura"],
        ["Hvad gør det ved netværksdesignet?",
         "Hvad gør det ved fragtførerens ansvar?",
         "Hvad gør det ved CO₂ pr. leveret enhed?"],
        "Mindre batches er Lean-flow: lagrene falder, og gennemløbstiden "
        "kortes. Men transporten går den modsatte vej — flere og mindre "
        "sendinger betyder dårligere fyldningsgrad, højere omkostning pr. "
        "enhed og mere CO₂ pr. tonkm. **Juridisk** ændrer det også noget: "
        "ansvarsgrænsen er vægtbaseret, så mange små sendinger giver lavere "
        "samlet dækning end én stor, hvis noget går galt. Koblingen er, at en "
        "Lean-gevinst inde i fabrikken kan blive betalt af transporten og "
        "risikoen udenfor — og det er dét, en tværfaglig case vil have dig "
        "til at få øje på.",
    ),
    (
        "Ledelsen vil samle tre regionale lagre i ét centrallager for at "
        "spare omkostninger.",
        ["Distribution", "Økonomi", "Indkøb"],
        ["Hvad siger Chopras U-kurve?",
         "Hvad sker der med responstiden — og med sikkerhedslageret?",
         "Hvornår er besparelsen reel?"],
        "Færre lagre giver **aggregering**: den samlede usikkerhed falder, så "
        "det nødvendige sikkerhedslager falder mindre end proportionalt — det "
        "er den reelle besparelse. Men transportomkostningen ud til kunderne "
        "stiger, og responstiden bliver længere. Chopras U-kurve siger, at "
        "totalomkostningen har et minimum ved et bestemt antal faciliteter — "
        "ikke ved ét og ikke ved mange. Svaret afhænger derfor af, hvad "
        "kunderne betaler for: er svartid en ordrevinder, kan besparelsen "
        "koste mere i tabt salg, end den giver på lageret.",
    ),
    (
        "En Lean-omlægning af lageret skal gennemføres over fire måneder, "
        "mens driften kører videre.",
        ["Produktion", "Projektstyring", "Distribution"],
        ["Er det et projekt eller drift?",
         "Vandfald eller agil?",
         "Hvem skal med i styregruppen, og hvem er referencegruppe?"],
        "Det er et **projekt**: tidsbegrænset, tværfagligt, afgrænset og en "
        "engangsopgave. Målet er kendt (kortere gennemløbstid), men vejen er "
        "det ikke — kendt hvad, ukendt hvordan — og dér peger kendt/ukendt-"
        "matricen på en **agil** eller blandet tilgang: fast ramme og budget, "
        "agil udførelse i korte forløb. **Projektstyringsdelen** er den svære: "
        "medarbejderne er udlånt fra driften og har to chefer, og "
        "driftschefen har en bonus, der afhænger af leveringspræcision. "
        "Plukkerne er referencegruppe — det er dem, der afgør, om den nye "
        "reolopstilling kan bruges.",
    ),
    (
        "Indkøb vil skifte til en billigere leverandør i Asien i stedet for "
        "den nuværende i Europa.",
        ["Indkøb", "Distribution", "Jura", "Økonomi"],
        ["Hvad siger Kraljic om varen?",
         "Hvad gør leveringstiden ved lageret?",
         "Hvilken Incoterm, og hvem bærer risikoen?"],
        "Prisen pr. stk. er kun ét led. **Lead time** går fra dage til uger, "
        "og det hæver både genbestillingspunktet og sikkerhedslageret — "
        "kapitalbindingen spiser en del af besparelsen, og det hører til i en "
        "**TCO**-betragtning, ikke en prissammenligning. **Kraljic** afgør, "
        "hvor meget risiko der overhovedet må tages: er varen strategisk "
        "eller flaskehals, er single sourcing langt væk en dårlig idé. "
        "**Juridisk** skal Incoterm-klausulen aftales bevidst — og husk, at "
        "risikoovergang og hvem der betaler fragten ikke er samme punkt i "
        "C-gruppen.",
    ),
    (
        "Ledelsen kræver, at maskinerne udnyttes mindst 95 % af tiden, fordi "
        "de er dyre.",
        ["Produktion", "Økonomi", "Distribution"],
        ["Hvad sker der med gennemløbstiden?",
         "Hvad er det økonomiske modargument?",
         "Hvad ville QRM gøre i stedet?"],
        "Sammenhængen mellem udnyttelsesgrad og kø er ikke lineær — den er en "
        "hockeystav. Presses udnyttelsen mod 100 %, eksploderer ventetiden, og "
        "**MCT** vokser. Det økonomiske modargument er, at leveringstiden er "
        "en konkurrenceparameter: kortere MCT vinder ordrer, og tabt "
        "dækningsbidrag på en mistet ordre er større end den sparede "
        "maskintime. **QRM** planlægger derfor bevidst med reservekapacitet. "
        "Pointen til forsvaret: høj udnyttelse er et mål for maskinen, ikke "
        "for kunden.",
    ),
    (
        "En sending elektronik bliver beskadiget undervejs. Den kom med skib "
        "og derefter på lastbil, og skaden opdages først på lageret.",
        ["Jura", "Distribution"],
        ["Hvilket regelsæt gælder?",
         "Hvad kan man få erstattet?",
         "Hvad burde have været gjort på forhånd?"],
        "Først: **hvornår** skete skaden? Transportformen på skadestidspunktet "
        "afgør regelsættet — Haag-Visby til søs, CMR på vejen — og "
        "grænserne er vidt forskellige. Kan tidspunktet ikke fastslås, bliver "
        "det et bevisspørgsmål. Dernæst: skaden er **skjult**, så der er en "
        "kort frist efter udlevering, og en kvitteret fragtseddel uden "
        "forbehold vender bevisbyrden. Endelig: ansvarsgrænsen er "
        "**vægtbaseret**, og elektronik er let og dyrt — så erstatningen "
        "dækker en brøkdel. Det, der burde have været gjort, er en "
        "**vareforsikring**; Incoterm-klausulen afgjorde blot, hvem af "
        "parterne der stod med tabet.",
    ),
    (
        "En webshop vil tilbyde levering samme dag i de største byer.",
        ["Distribution", "Økonomi", "Produktion"],
        ["Hvilket af Chopras netværk peger det på?",
         "Hvad koster svartiden?",
         "Hvad gør det ved lagerstrukturen?"],
        "Svartid og omkostning trækker hver sin vej — det er hele "
        "grænsekurven. Samme-dags-levering kræver lager **tæt på kunden**, "
        "altså flere og mindre lagre, hvilket øger både facilitets- og "
        "lageromkostninger og fjerner aggregeringsgevinsten. Chopra peger mod "
        "distributørlager med last-mile-levering, hvor last mile er den "
        "dyreste del af hele kæden. Spørgsmålet til casen er derfor ikke "
        "«kan vi?», men **«er svartid en ordrevinder eller blot "
        "ordrekvalificerende i denne branche?»** — er den kun "
        "kvalificerende, betaler kunden ikke ekstra for den.",
    ),
    (
        "Et nyt lagerstyringssystem skal indføres. Den eneste medarbejder, "
        "der kender både det gamle system og de daglige arbejdsgange, kan "
        "ikke undværes fra driften.",
        ["Projektstyring", "Distribution", "Organisation"],
        ["Hvem har ret — projektlederen eller driftschefen?",
         "Hvad kan projektlederen gøre uden instruktionsbeføjelse?",
         "Hvad skulle have været aftalt på forhånd?"],
        "Begge har ret inden for hver deres logik, og det er selve pointen: "
        "projektlederen har **sjældent formel instruktionsbeføjelse**, og "
        "deltagerne har to chefer. Konflikten er ikke personlig, den er "
        "**strukturel** — den følger af den midlertidige organisation inde i "
        "den permanente. Vejen frem er **styregruppen**: det er præcis den "
        "slags beslutning, projektlederen ikke må træffe selv. Og det, der "
        "skulle have været aftalt i opstartsprocessen, er ressourcetrækket — "
        "hvor mange timer, fra hvem, og hvem der dækker driften imens.",
    ),
]


# (dit valg, det oplagte alternativ, [modspørgsmål], hvordan man forsvarer det)
VALG = [
    (
        "Du har anbefalet ét centrallager frem for tre regionale.",
        "tre regionale lagre",
        ["Hvad med responstiden til de fjerneste kunder?",
         "Hvad hvis centrallageret står stille en uge?"],
        "Hold fast i **aggregeringsargumentet**: samlet usikkerhed falder, så "
        "sikkerhedslageret falder mere end proportionalt, og "
        "kapitalbindingen med. Anerkend så prisen ærligt — længere svartid og "
        "højere udgående transport — og vis, at du har regnet på, hvor "
        "grænsekurven vender. Det svageste svar er at benægte ulempen; det "
        "stærkeste er at sige, hvad der skulle til for at ændre din "
        "anbefaling (fx hvis svartid var en ordrevinder).",
    ),
    (
        "Du har anbefalet Lean som forbedringsstrategi.",
        "QRM",
        ["Virksomheden laver mange varianter i små serier — er Lean så det rigtige?",
         "Hvad ville du gøre anderledes, hvis variationen fordobles?"],
        "Det afhænger af **variabiliteten**, ikke af hvad der er mest "
        "moderne. Er efterspørgslen nogenlunde stabil og volumen høj, virker "
        "Lean. Er variationen høj og serierne små, er QRM bygget til netop "
        "det, og Lean-værktøjer som takttid og kanban får svært ved at bide. "
        "Et stærkt svar viser, at du kender **grænsen** for din egen "
        "anbefaling — og at du har kigget på tallene for variation, før du "
        "valgte.",
    ),
    (
        "Du har anbefalet DDP i kontrakten.",
        "FCA eller CPT",
        ["Hvorfor skal sælger bære told og risiko helt frem?",
         "Hvad hvis sælger ikke kan agere importør i modtagerlandet?"],
        "DDP giver køberen maksimal enkelhed — én pris, ingen "
        "toldbehandling. Det er et **salgsargument**, ikke en juridisk "
        "nødvendighed. Forsvar det på kundeforholdet, men anerkend prisen: "
        "sælger bærer risiko og omkostning hele vejen og skal kunne "
        "toldbehandle i modtagerlandet — kan han ikke det, falder klausulen "
        "fra hinanden i praksis. Vis, at du kender alternativet og hvorfor "
        "du fravalgte det.",
    ),
    (
        "Du har anbefalet en agil tilgang til implementeringsprojektet.",
        "en traditionel vandfaldsmodel",
        ["Budgettet skal godkendes på forhånd — hvordan går det sammen med agil?",
         "Hvad hvis opdragsgiveren ikke har tid til at være med løbende?"],
        "Peg på **kendt/ukendt-matricen**: er målet kendt, men vejen ukendt, "
        "er agil det rigtige. Og forklar, at agil ikke betyder «uden "
        "styring» — rammen og budgettet kan sagtens ligge fast, mens "
        "udførelsen er agil. Det er den **blandede form**, og den er den "
        "almindelige i logistik. Den ærlige forudsætning, du skal nævne "
        "selv: agil kræver, at opdragsgiveren er tilgængelig løbende og ikke "
        "kun ved milepæle. Kan han ikke det, holder modellen ikke.",
    ),
    (
        "Du har anbefalet at outsource lageret til en tredjepart.",
        "at beholde det i eget hus",
        ["Hvad sker der med jeres viden om egne processer?",
         "Hvordan sikrer I servicen, når I ikke selv styrer den?"],
        "Argumentér på **kernekompetence og variabel kapacitet**: en "
        "tredjepart kan absorbere sæsonudsving, som egne faste kvadratmeter "
        "ikke kan. Anerkend så tabet af proceskontrol og af tavs viden — det "
        "er en reel omkostning, ikke en detalje — og vis, hvordan du dækker "
        "den: målbare serviceniveauer i aftalen og egne KPI'er, du selv "
        "måler. Et svar, der ikke nævner ulempen, lyder som en brochure.",
    ),
    (
        "Du har anbefalet luftfragt på en hastende sending.",
        "søfragt",
        ["Hvad med CO₂-regnskabet, I selv har opstillet?",
         "Er det en engangsløsning eller en struktur?"],
        "Vær ærlig om, at luftfragt er den dyreste form både i kroner og CO₂. "
        "Forsvar det som et **bevidst engangsvalg** mod et konkret tab — "
        "produktionsstop, kontraktbod, mistet kunde — og sæt tallene op mod "
        "hinanden. Det svage svar er at behandle det som normal drift. Det "
        "stærke er at sige, hvad der skal ændres, for at det ikke sker igen: "
        "det er som regel et planlægnings- eller lagerproblem, ikke et "
        "transportproblem.",
    ),
    (
        "Du har anbefalet at hæve sikkerhedslageret for at nå 98 % servicegrad.",
        "at presse leverandøren til kortere og mere stabil leveringstid",
        ["Hvad koster de sidste procenter?",
         "Hvorfor angriber du symptomet frem for årsagen?"],
        "Det er et godt modspørgsmål, og det skal anerkendes. Sikkerhedslager "
        "dækker **variation**, og de sidste procenter koster "
        "uforholdsmæssigt meget, fordi sammenhængen er eksponentiel. Den "
        "billigere vej er ofte at reducere variationen i leveringstiden — "
        "altså at gå på leverandøren i stedet for på lageret. Forsvar dit "
        "valg som det, der virker **nu**, og peg på det andet som det, der "
        "virker **varigt**. At kunne skelne der viser, at du forstår "
        "formlen og ikke bare kan regne den.",
    ),
]
