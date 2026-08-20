"""Spørgsmålsbank for 3. semester — Distribution og Projektstyring.

Hvorfor filen findes
--------------------
Forsvarstræneren var stadig en 2. semester-træner: dækningskortet viste
30,2 spørgsmål pr. ECTS på SCM-stoffet mod 1,1 på Distribution — som er
prøvens STØRSTE fag (7 af 20 ECTS) — og 0,5 på Projektstyring.

Stoffet her stammer fra fagets egne oplæg (Lean & agil, QRM 1-5, strukturen
på transportmarkedet, søtransport, landevej, luftfragt, distribution,
warehousing, bæredygtighed) og fra projektstyringsbogens kapitel 1-2.

Format = samme som KONCEPT i pakke_spoergsmaal.py:
    type="rigtigt"  → der ER et korrekt svar (alt="")
    type="argument" → flere forsvarlige svar (alt = det modsatte forsvar)

Ingen virksomheds- eller personnavne: værktøjet er et generelt opslagsværk,
ikke et case-referat. Situationer beskrives neutralt.
"""

KONCEPT_3SEM = [

    # =====================================================================
    # DISTRIBUTION — Lean
    # =====================================================================
    {
        "fag": "Distribution", "emne": "De 5 Lean-principper", "type": "rigtigt",
        "sp": "Hvad er de fem Lean-principper, og hvorfor kan man ikke tage dem i vilkårlig rækkefølge?",
        "svar": "Værdi → værdistrøm → flow → pull → perfektion. Først defineres værdi af KUNDEN — ikke af afdelingen eller maskinen. Så kortlægges værdistrømmen, så man kan se hvilke skridt der faktisk tilfører værdi. Derefter skabes flow, så arbejdet glider uden bunker og ventetid. Først når der er flow, indføres pull, hvor der produceres på signal fra næste led. Til sidst gentages det hele i det uendelige — perfektion er en retning, ikke en tilstand. Rækkefølgen er bindende, fordi hvert princip forudsætter det foregående: indfører man pull uden først at have skabt flow, vokser lagrene i stedet for at falde, fordi hvert led lægger buffer ind for at kunne svare på trækket. Pull uden flow er bare et lager med et nyt navn.",
        "alt": "",
        "fisker": "Om du kan de fem i RÆKKEFØLGE og kan forklare konsekvensen af at springe et trin over. Mange kan remse dem op; få kan sige hvorfor rækkefølgen betyder noget.",
        "soeg": ["lean", "værdi", "værdistrøm", "flow", "pull", "perfektion", "womack"],
    },
    {
        "fag": "Distribution", "emne": "Muda, mura og muri", "type": "rigtigt",
        "sp": "Lean taler om tre slags tab. Hvilke, og hvilken af dem angriber de fleste virksomheder — med hvilken konsekvens?",
        "svar": "Muda er spild (arbejde uden værdi for kunden), mura er ujævnhed (svingninger i belastningen) og muri er overbelastning af mennesker og maskiner. De fleste angriber kun muda, fordi spild er det, man kan få øje på: bunker, ventetid, omarbejde. Konsekvensen er, at forbedringen ikke holder. Sammenhængen går nemlig den anden vej: ujævnhed skaber overbelastning, og overbelastning skaber spild. Fjerner man spildet uden at udjævne belastningen, kommer det igen næste gang efterspørgslen svinger. Til et forsvar er pointen, at man skal pege på ÅRSAGEN (mura) og ikke kun på symptomet (muda).",
        "alt": "",
        "fisker": "Om du kender alle tre — og om du kan vende kausaliteten rigtigt: mura → muri → muda, ikke omvendt.",
        "soeg": ["muda", "mura", "muri", "spild", "ujævnhed", "overbelastning"],
    },
    {
        "fag": "Distribution", "emne": "Værdistrømsanalyse (VSM)", "type": "rigtigt",
        "sp": "Hvad viser et nutidskort i en værdistrømsanalyse, som en almindelig procesbeskrivelse ikke viser?",
        "svar": "Nutidskortet tegner HELE flowet for én produktfamilie — fra råvare til kunde — med både materialestrøm og informationsstrøm, og med lagrene omregnet til TID. Det er dét, der er pointen: når lagrene står i dage i stedet for i stykker, bliver forskellen mellem bearbejdningstid og gennemløbstid synlig. Typisk er bearbejdningen minutter, mens gennemløbstiden er uger — resten er venten. En almindelig procesbeskrivelse viser skridtene, men ikke ventetiden mellem dem, og det er netop dér spildet ligger. Fremtidskortet designer så flowet med takt, pull og udjævning.",
        "alt": "",
        "fisker": "Om du nævner informationsstrømmen OG omregningen af lagre til dage. Kortet uden tid er bare et rutediagram.",
        "soeg": ["vsm", "værdistrøm", "nutidskort", "fremtidskort", "learning to see"],
    },
    {
        "fag": "Distribution", "emne": "SMED og batchstørrelse", "type": "rigtigt",
        "sp": "En virksomhed kører store serier, fordi omstilling tager lang tid. Hvad er den rigtige rækkefølge at angribe det i?",
        "svar": "Omstillingstiden først, batchstørrelsen bagefter. Lang omstillingstid er selve ÅRSAGEN til de store serier: jo dyrere det er at skifte, jo mere skal der køres pr. skift for at fordele omkostningen. Angriber man batchstørrelsen først uden at sænke omstillingstiden, stiger omkostningen pr. enhed, og forbedringen ruller tilbage. SMED gør omstillingen kortere ved at skille indre tid (maskinen står stille) fra ydre tid (kan gøres mens den kører), flytte så meget som muligt til ydre, og forenkle resten. Falder omstillingstiden, falder den økonomisk optimale seriestørrelse med — og først dér bliver flow muligt.",
        "alt": "",
        "fisker": "Om du får kausaliteten rigtigt. Mange svarer 'kør mindre batches' — det er konklusionen, ikke vejen.",
        "soeg": ["smed", "omstilling", "indre tid", "ydre tid", "seriestørrelse", "batch"],
    },
    {
        "fag": "Distribution", "emne": "5S", "type": "rigtigt",
        "sp": "Hvad er formålet med 5S — og hvorfor er 'der bliver pænere' et forkert svar?",
        "svar": "5S er sortér, sæt i system, systematisk rengøring, standardisér og selvdisciplin. Formålet er ikke pænhed, men SYNLIGHED: når alt har en fast plads, bliver en afvigelse øjeblikkelig synlig. Mangler et værktøj, ser man det med det samme; hober der sig materiale op et sted, springer det i øjnene. Uden 5S kan man ikke se, om flowet er brudt, for der er ingen normaltilstand at måle imod. Derfor er 5S et fundament under de øvrige Lean-værktøjer og ikke et selvstændigt projekt — og derfor falder rene oprydningskampagner tilbage efter et par måneder.",
        "alt": "",
        "fisker": "Om du siger 'synlighed af afvigelser' og ikke 'orden og ryddelighed'. Det er dér, forståelsen adskiller sig.",
        "soeg": ["5s", "sortér", "standardisér", "visuel styring", "orden"],
    },

    # =====================================================================
    # DISTRIBUTION — QRM
    # =====================================================================
    {
        "fag": "Distribution", "emne": "Lean eller QRM", "type": "argument",
        "sp": "En virksomhed laver mange varianter i små serier og overvejer Lean. Hvad anbefaler du?",
        "svar": "Jeg vil pege på QRM. Lean er bygget til stabile flows med høj volumen og lav variation — takttid, kanban og udjævning forudsætter, at der er noget gentageligt at udjævne. Ved mange varianter i små serier er der ingen stabil takt, kanban-kortene multipliceres med antallet af varenumre, og lagrene vokser i stedet for at falde. QRM angriber i stedet TIDEN: målet er kortest mulig gennemløbstid målt som MCT, organiseret i celler med krydsoplærte medarbejdere, der kan færdiggøre en hel opgavefamilie. Det passer til netop den situation, hvor Lean har svært ved at bide.",
        "alt": "Man kan forsvare at starte med Lean alligevel: værktøjerne 5S, SMED og værdistrømsanalyse er ikke afhængige af høj volumen, og især SMED er direkte relevant, fordi kortere omstilling er forudsætningen for små serier overhovedet. Argumentet er, at man tager Leans grundlæggende værktøjer først og lader QRM's celletankegang komme bagefter — det er billigere at begynde og kræver ikke en omorganisering fra dag ét.",
        "fisker": "Om du kobler valget til VARIABILITET og volumen frem for til hvad der er mest moderne — og om du kender grænsen for din egen anbefaling.",
        "soeg": ["qrm", "lean", "variation", "volumen", "suri"],
    },
    {
        "fag": "Distribution", "emne": "MCT og det hvide rum", "type": "rigtigt",
        "sp": "Hvad er MCT, og hvorfor måles den i kalendertid frem for arbejdstimer?",
        "svar": "MCT (Manufacturing Critical-path Time) er den samlede kalendertid fra en kunde afgiver ordre, til den er leveret — regnet ad den længste vej gennem virksomheden. Den måles i kalendertid netop for at afsløre ventetiden. Regner man i arbejdstimer, forsvinder pointen, for så tæller kun den tid, nogen faktisk rører opgaven. Erfaringen fra QRM er, at langt størstedelen af MCT er 'det hvide rum' — ventetid, kø og liggetid, hvor intet sker. Typisk arbejdes der på opgaven i nogle få procent af den samlede tid. Det er dér, forbedringspotentialet ligger, og det ser man kun, hvis man måler kalendertid.",
        "alt": "",
        "fisker": "Om du siger KALENDERTID og kan forklare hvorfor. Svarer du 'gennemløbstid' uden den nuance, er halvdelen af pointen væk.",
        "soeg": ["mct", "hvide rum", "kalendertid", "kritisk vej", "gennemløbstid"],
    },
    {
        "fag": "Distribution", "emne": "Udnyttelsesgrad og kø", "type": "rigtigt",
        "sp": "Ledelsen vil have maskinerne udnyttet 95 % af tiden, fordi de er dyre. Hvad er dit modargument?",
        "svar": "At sammenhængen mellem udnyttelsesgrad og ventetid ikke er lineær — den er en hockeystav. Op til omkring 80 % stiger køen langsomt; derover eksploderer den, og gennemløbstiden med. Ved 95 % er systemet så følsomt, at den mindste variation — en maskine der står, en hasteordre, en sygemelding — vælter planen. Det økonomiske modargument er, at leveringstid er en konkurrenceparameter: tabt dækningsbidrag på en mistet ordre er større end værdien af en ekstra udnyttet maskintime. Derfor planlægger QRM bevidst med reservekapacitet. Travlhed er et mål for maskinen, ikke for kunden.",
        "alt": "",
        "fisker": "Om du kan forklare at sammenhængen er ikke-lineær, og om du kan oversætte det til KRONER — ikke bare sige at det er uhensigtsmæssigt.",
        "soeg": ["udnyttelsesgrad", "kø", "reservekapacitet", "rho", "hockeystav"],
    },
    {
        "fag": "Distribution", "emne": "POLCA og kanban", "type": "rigtigt",
        "sp": "Hvorfor bruger QRM POLCA-kort i stedet for kanban mellem cellerne?",
        "svar": "Fordi kanban er et LAGERsignal, og POLCA er et KAPACITETSsignal. Kanban forudsætter, at der står færdige beholdere af en kendt vare, som kan fyldes op igen — det virker ved gentagne standardvarer. Ved kundetilpassede varer findes den beholder ikke: hver ordre er unik, så der er intet lager at trække fra. POLCA-kortet siger i stedet noget andet: at den modtagende celle har LEDIG KAPACITET til at tage imod. Arbejdet sendes altså først videre, når næste celle kan nå det, hvilket forhindrer, at der hober sig arbejde op foran en flaskehals. Det er den samme grundidé — træk frem for skub — men på kapacitet i stedet for på lager.",
        "alt": "",
        "fisker": "Om du kan forklare forskellen lager- vs. kapacitetssignal. Det er den nuance, der viser, at du har forstået begge systemer.",
        "soeg": ["polca", "kanban", "qrm", "celler", "kapacitetssignal"],
    },
    {
        "fag": "Distribution", "emne": "QRM-celler og Q-ROC", "type": "rigtigt",
        "sp": "Hvad kendetegner en QRM-celle, og hvad er en Q-ROC?",
        "svar": "En QRM-celle er et lille team med egne, samlokaliserede og dedikerede ressourcer, krydsoplært til at færdiggøre en HEL opgavefamilie uden at opgaven pendler frem og tilbage mellem afdelinger. Nøgleordene er teamejerskab, krydsoplæring og et fælles mål om at sænke MCT. Modsætningen er den funktionsopdelte organisation, hvor hver afdeling optimerer sin egen udnyttelse, og opgaven venter i kø ved hvert skifte — det QRM kalder spaghettiflow. En Q-ROC (Quick Response Office Cell) er samme princip anvendt på kontoret: ordrebehandling, tilbudsgivning og indkøb organiseret som en celle. Pointen er, at ventetiden i administrationen ofte er større end i produktionen.",
        "alt": "",
        "fisker": "Om du nævner Q-ROC og dermed viser, at du har fanget, at QRM er virksomhedsdækkende og ikke kun handler om gulvet.",
        "soeg": ["qrm-celle", "q-roc", "krydsoplæring", "ftms", "spaghettiflow"],
    },

    # =====================================================================
    # DISTRIBUTION — netværk og transport
    # =====================================================================
    {
        "fag": "Distribution", "emne": "Antal faciliteter (U-kurven)", "type": "argument",
        "sp": "Ledelsen vil samle tre regionale lagre i ét. Hvad siger teorien, og hvad anbefaler du?",
        "svar": "Færre lagre giver aggregering: den samlede usikkerhed er mindre end summen af usikkerhederne hvert sted, så det nødvendige sikkerhedslager falder mindre end proportionalt med antallet af lagre. Det er den reelle besparelse, og den er ægte. Men transportomkostningen UD til kunderne stiger, og responstiden bliver længere. Totalomkostningen som funktion af antal faciliteter er derfor en U-kurve med et minimum, der hverken ligger ved ét lager eller ved mange. Jeg vil anbefale centralisering, hvis svartid kun er ordrekvalificerende i branchen — altså hvis kunderne ikke betaler ekstra for den.",
        "alt": "Man kan forsvare at beholde de tre: er kort svartid en ordrevinder, kan det tabte salg overstige besparelsen på lager og faciliteter. Dertil kommer robusthed — ét centrallager er et enkelt fejlpunkt, og en uges nedbrud rammer så hele markedet i stedet for en tredjedel. Argumentet vægter altså sårbarhed og kundeoplevelse højere end kapitalbinding.",
        "fisker": "Om du kender AGGREGERING som den egentlige mekanisme, og om du kobler valget til, om svartid er ordrevinder eller blot ordrekvalificerende.",
        "soeg": ["chopra", "aggregering", "u-kurve", "centralisering", "faciliteter"],
    },
    {
        "fag": "Distribution", "emne": "Chopras distributionsnetværk", "type": "rigtigt",
        "sp": "Hvad er de to størrelser, ethvert distributionsnetværk skal afveje, og hvad er last mile?",
        "svar": "Responstid over for omkostning. De trækker hver sin vej: hurtigere svar kræver lager tættere på kunden, hvilket betyder flere og mindre lagre, højere facilitets- og lageromkostninger og tabt aggregering. Chopras designmuligheder spænder fra producentlager med direkte forsendelse (lavest lageromkostning, længst svartid) over in-transit-samling og distributørlager med transportørlevering til distributørlager med last-mile-levering og de to afhentningsmodeller. Last mile er den sidste strækning hjem til kunden, og den er den DYRESTE del af hele kæden, fordi den ikke kan konsolideres — hver stop er én kunde.",
        "alt": "",
        "fisker": "Om du kan navngive afvejningen (responstid ↔ omkostning) og forklare hvorfor last mile er dyrest.",
        "soeg": ["chopra", "netværk", "last mile", "responstid", "drop shipping"],
    },
    {
        "fag": "Distribution", "emne": "Valg af transportform", "type": "argument",
        "sp": "Hvordan begrunder du et valg af transportform, og hvorfor er 'den billigste' sjældent et godt svar?",
        "svar": "Valget er en afvejning af hastighed, pris, godsets art, frekvens og antal omlastninger. Den billigste form pr. tonkm er som regel den langsomste, og den langsomme transporttid koster andre steder: mere gods bundet undervejs, større sikkerhedslager for at dække den længere leveringstid, og dårligere reaktionsevne. Derfor skal valget regnes som en TOTALomkostning inklusive kapitalbinding og lager — ikke som en fragtrate. Dertil kommer godsets art: er det letfordærveligt, meget værdifuldt eller hastende, kan en dyrere form være den billigste samlet set.",
        "alt": "Man kan forsvare det rene prisvalg, hvis godset er robust, lavværdi og efterspørgslen forudsigelig. Så er kapitalbindingen undervejs lille, sikkerhedslageret billigt, og der er ingen grund til at betale for hastighed, kunden ikke mærker. Argumentet er, at totalomkostningsbetragtningen kun flytter konklusionen, når varens værdi eller hastende karakter er høj nok.",
        "fisker": "Om du inddrager kapitalbinding og sikkerhedslager — altså om du regner på TOTALEN og ikke bare på fragtraten.",
        "soeg": ["transportform", "modal split", "intermodal", "omlastning", "transittid"],
    },
    {
        "fag": "Distribution", "emne": "Volumenvægt (measureton)", "type": "rigtigt",
        "sp": "En sending fylder 3,4 m³ og vejer 750 kg og sendes med skib. Hvad afregnes der efter, og hvorfor?",
        "svar": "Der afregnes efter volumen. Fragtføreren sælger både løfteevne og plads, så grundlaget er det STØRSTE af faktisk vægt og volumenvægt. For søfragt er omregningen 1 m³ = 1.000 kg — den klassiske measureton — så volumenvægten bliver 3,4 × 1.000 = 3.400 kg mod en faktisk vægt på 750 kg. Der betales altså for 3.400 kg, godt fire en halv gang varens egen vægt. Omregningsfaktoren afhænger af transportformen: fly regner typisk omkring 167 kg pr. m³, fordi flyets knappe ressource er løfteevne, mens skibets er plads. Rådgivningen er derfor sjældent 'forhandl raten', men 'ændr densiteten' — bedre pakning kan flytte grundlaget fra volumen til vægt.",
        "alt": "",
        "fisker": "Om du kan regne det og forklare HVORFOR faktoren varierer mellem transportformer. Tallet alene er halvdelen.",
        "soeg": ["measureton", "volumenvægt", "cbm", "fragtgrundlag", "densitet"],
    },
    {
        "fag": "Distribution", "emne": "Luftfartens frihedsrettigheder", "type": "rigtigt",
        "sp": "Hvad er den femte og den sjette frihed, og hvorfor er den sjette særligt interessant?",
        "svar": "Femte frihed er retten til at laste og losse undervejs på en rute mellem to andre lande — man må altså tage gods med på mellemlandingen. Sjette frihed er retten til at flyve mellem to fremmede lande med mellemlanding i sit EGET land; den er reelt tredje og fjerde frihed sat sammen. Den er interessant, fordi den ikke står som en officiel frihed i konventionen, men i praksis er hele forretningsmodellen bag de store omstigningslufthavne: man kobler to lovlige rettigheder og opnår dermed at beflyve en rute, man ellers ikke måtte flyve direkte. De fire første friheder er officielle; femte er officiel, mens sjette til niende bruges i praksis uden samme formelle status.",
        "alt": "",
        "fisker": "Om du kan forklare, at sjette frihed er en KOMBINATION af to andre — og at rettighederne er mellemstatslige aftaler, ikke en global standard.",
        "soeg": ["frihedsrettigheder", "femte frihed", "sjette frihed", "cabotage", "hub"],
    },
    {
        "fag": "Distribution", "emne": "Køre-hviletid og arbejdstid", "type": "rigtigt",
        "sp": "En chauffør overholder køre-hviletidsreglerne. Kan han alligevel bryde loven på arbejdstiden?",
        "svar": "Ja, og det er præcis fælden. Køre-hviletidsreglerne handler om KØRSLEN — hvor længe der må køres, og hvornår der skal holdes pause og hvil. Arbejdstidsreglerne handler om HELE arbejdsdagen: også læsning, losning, kontrol, rengøring og administration tæller med. De to regelsæt gælder samtidig, og man kan sagtens overholde det ene og bryde det andet, fordi en dag med kort kørsel og meget læsning kan holde sig inden for køretiden og alligevel sprænge arbejdstiden. Rådighedstid — planlagt ventetid, hvor man på forhånd ved, hvor længe man venter, fx en færgeoverfart — tæller derimod ikke med i arbejdstiden.",
        "alt": "",
        "fisker": "Om du skelner de to regelsæt og kender rådighedstid. Blander du dem sammen, ryger halvdelen af pointen.",
        "soeg": ["køre-hviletid", "arbejdstid", "rådighedstid", "takograf", "chauffør"],
    },
    {
        "fag": "Distribution", "emne": "Særtransport", "type": "rigtigt",
        "sp": "Hvornår kræver en transport særtilladelse, og hvad er den vigtigste forudsætning for at få den?",
        "svar": "Når transporten overskrider de almindelige grænser for bredde, længde, højde eller vægt. Den vigtigste forudsætning er, at godset IKKE kan deles op — kan det skilles ad og køres i flere almindelige læs, gives der ikke tilladelse, uanset hvor meget besvær det ville spare. Tilladelsen knytter sig desuden til en KONKRET RUTE og ikke til køretøjet, fordi ruten skal undersøges for broer, viadukter, master og rundkørsler. Hastighedsgrænsen falder med vægten, over bestemte mål kræves følgebil med godkendt bil og chauffør, og mange strækninger må kun befares om natten.",
        "alt": "",
        "fisker": "Om du nævner udelelighedskravet og at tilladelsen følger RUTEN. Det er de to, folk glemmer.",
        "soeg": ["særtransport", "blokvogn", "følgebil", "tilladelse", "projektlast"],
    },
    {
        "fag": "Distribution", "emne": "Euro-normer", "type": "rigtigt",
        "sp": "En vognmand siger, at hans nye Euro 6-lastbiler har sænket virksomhedens CO₂-aftryk. Holder påstanden?",
        "svar": "Nej, ikke som den står. Euro-normerne regulerer LUFTFORURENING — især NOx og partikler — og ikke CO₂. CO₂ følger brændstofforbruget og energikilden, og en Euro 6-motor kan sagtens bruge lige så meget diesel som en ældre. Påstanden blander to forskellige miljøproblemer sammen. Det er rigtigt, at nyere biler ofte er mere brændstoføkonomiske, men det skyldes motorteknologi og aerodynamik, ikke normen. Euro-normen har til gengæld reel betydning for adgang: miljøzoner i byerne afviser køretøjer under et bestemt trin, og mange udbud stiller minimumskrav — så en gammel bil kan være lovlig at eje, men lukket ude af de opgaver, der betaler bedst.",
        "alt": "",
        "fisker": "Om du kan skille luftforurening fra klimabelastning. Det er en klassisk sammenblanding, og den er let at teste.",
        "soeg": ["euro-norm", "nox", "partikler", "miljøzone", "co2"],
    },
    {
        "fag": "Distribution", "emne": "Told: T1 og T2", "type": "rigtigt",
        "sp": "Hvad er forskellen på T1 og T2, og hvornår bruges de?",
        "svar": "T1 dækker varer, der IKKE er i fri omsætning i EU — typisk varer fra tredjelande, som endnu ikke er fortoldet. De transporteres under toldkontrol, og tolden er ikke betalt endnu, så myndighederne skal kunne følge dem, indtil de fortoldes eller forlader unionen igen. T2 dækker varer, der ER i fri omsætning i EU, men som transporteres gennem et tredjeland undervejs — proceduren dokumenterer, at varerne beholder deres EU-status. Kort sagt: T1 handler om varer, der endnu ikke er kommet ind, T2 om varer, der allerede er inde, men skal ud og ind igen.",
        "alt": "",
        "fisker": "Om du kan forklare 'fri omsætning' — det er begrebet, forskellen hviler på.",
        "soeg": ["t1", "t2", "told", "fri omsætning", "transit", "taric"],
    },
    {
        "fag": "Distribution", "emne": "Remburs", "type": "rigtigt",
        "sp": "Hvad løser en remburs, og hvad er prisen for den sikkerhed?",
        "svar": "Den løser tillidsproblemet mellem to parter, der ikke kender hinanden og handler over lang afstand: sælger tør ikke sende varen uden betaling, og køber tør ikke betale uden vare. Ved en remburs går bankerne ind imellem — køberens bank forpligter sig til at betale, når sælger fremlægger de aftalte DOKUMENTER, typisk konnossement, faktura og forsikringsbevis. Betalingen udløses altså af dokumenterne, ikke af varen. Prisen er dobbelt: den koster gebyrer i begge banker, og den er formalistisk — mindste uoverensstemmelse i et dokument kan blokere udbetalingen, selvom varen er kommet frem i god stand.",
        "alt": "",
        "fisker": "Om du siger, at banken betaler mod DOKUMENTER og ikke mod varen. Det er hele mekanismen — og også dens svaghed.",
        "soeg": ["remburs", "letter of credit", "konnossement", "dokumenter", "bank"],
    },

    # =====================================================================
    # DISTRIBUTION — lager og bæredygtighed
    # =====================================================================
    {
        "fag": "Distribution", "emne": "Plukning som omkostningsdriver", "type": "rigtigt",
        "sp": "Hvorfor er plukning lagerets dyreste aktivitet, og hvilke greb har man?",
        "svar": "Fordi omkostningen ligger i BEVÆGELSEN, ikke i selve grebet om varen. Plukkeren bruger størstedelen af tiden på at gå eller køre mellem lokationer, og den tid vokser med lagerets størrelse og med hvor spredt varerne ligger. Grebene falder i to grupper: enten går mennesket til varen (og så optimerer man ruten, placerer højfrekvente varer tæt på udgangen, og samler flere ordrer i én tur med batch- eller zonepluk), eller også kommer varen til mennesket (automatiserede systemer, hvor plukkeren står stille). Dertil kommer, hvordan plukkeren får besked — liste, scanner, pick by voice, pick by light — hvor pointen er at få hænder og øjne fri.",
        "alt": "",
        "fisker": "Om du siger BEVÆGELSE som driveren. Svarer du 'fordi det er manuelt', har du ikke fat i mekanismen.",
        "soeg": ["plukning", "batch-pluk", "zone-pluk", "pick by voice", "wms"],
    },
    {
        "fag": "Distribution", "emne": "Tredjepartslogistik", "type": "argument",
        "sp": "Bør en virksomhed outsource lageret til en tredjepart?",
        "svar": "Det taler for, når efterspørgslen svinger, og når lagerdrift ikke er en kernekompetence. En tredjepart kan absorbere sæsonudsving, som egne faste kvadratmeter ikke kan — man betaler for det, man bruger, i stedet for at eje en spidsbelastningskapacitet, der står tom resten af året. Dertil kommer adgang til systemer og netværk, det ikke kan betale sig at bygge selv. Prisen er tab af proceskontrol og af tavs viden om egne varer og kunder, og den skal dækkes ind med målbare serviceniveauer i aftalen og egne KPI'er, man selv måler.",
        "alt": "Man kan forsvare at beholde det i eget hus, hvis lagerhåndteringen ER en del af værditilbuddet — særlig håndtering, kundetilpasning, hurtige undtagelser — eller hvis varerne kræver viden, der er svær at overdrage. Så bliver outsourcing en kilde til fejl og til langsom reaktion, og den tavse viden, man mister, kommer ikke tilbage. Argumentet vægter kontrol og læring højere end fleksibel kapacitet.",
        "fisker": "Om du nævner BÅDE fordelen og prisen. Et svar, der kun ser det ene, lyder som en brochure.",
        "soeg": ["tpl", "3pl", "outsourcing", "kernekompetence", "serviceniveau"],
    },
    {
        "fag": "Distribution", "emne": "Slow steaming", "type": "rigtigt",
        "sp": "Hvorfor giver en beskeden fartnedsættelse på et skib så stor en brændstofbesparelse — og hvad koster det?",
        "svar": "Fordi sammenhængen mellem fart og brændstofforbrug ikke er lineær: modstanden i vandet vokser stærkt med farten, så forbruget stiger langt hurtigere end hastigheden. Derfor kan en fartnedsættelse på omkring 10 % give i størrelsesordenen 20-25 % lavere forbrug. Det er søfartens stærkeste enkeltgreb mod CO₂, og det kræver ingen ny teknologi. Prisen er længere transittid, og den skal absorberes et andet sted i kæden — enten med større lager, tidligere bestilling eller bedre prognoser. Dertil binder den langsommere sejlads mere gods undervejs, hvilket er kapital, der ikke arbejder.",
        "alt": "",
        "fisker": "Om du kan forklare den ikke-lineære sammenhæng OG placere omkostningen: den forsvinder ikke, den flytter til lageret.",
        "soeg": ["slow steaming", "co2", "imo", "brændstof", "transittid"],
    },
    {
        "fag": "Distribution", "emne": "Effektivitet er ikke nok", "type": "rigtigt",
        "sp": "Godstransportens CO₂ pr. tonkm er faldet, men de samlede udledninger stiger. Hvordan forklarer du det?",
        "svar": "Effektiviseringen bliver overhalet af væksten. Intensiteten — gram CO₂ pr. tonkm — falder, fordi køretøjer, skibe og fly bliver bedre, og fordi lastene udnyttes bedre. Men transportarbejdet i tonkm vokser hurtigere, end intensiteten falder, og så stiger det absolutte udslip alligevel. Pointen er, at effektivisering alene ikke kan bringe udledningerne ned; den kan kun bremse stigningen. Logistikerens egne håndtag ligger derfor et andet sted: flytte gods til transportformer med lavere CO₂ (modal shift), udnytte kapaciteten bedre, køre kortere og planlagte ruter — og designe netværket, så der simpelthen skal transporteres mindre.",
        "alt": "",
        "fisker": "Om du kan skelne INTENSITET fra ABSOLUT udslip. Det er dér, argumentet vindes.",
        "soeg": ["co2", "tonkm", "intensitet", "modal shift", "dekarbonisering"],
    },

    # =====================================================================
    # PROJEKTSTYRING
    # =====================================================================
    {
        "fag": "Projektstyring", "emne": "Projekt eller drift", "type": "rigtigt",
        "sp": "Et lager skal flyttes til en ny hal over fire weekender, mens driften kører videre. Lagerchefen mener, det er almindelig drift. Har han ret?",
        "svar": "Nej. Test det på de fire kendetegn: opgaven er TIDSBEGRÆNSET (den har en start og en slutning), TVÆRFAGLIG (den trækker på lager, it, transport og ledelse samtidig), AFGRÆNSET (mål, ramme og ressourcer kan defineres på forhånd) og en ENGANGSOPGAVE (den er ikke løst på samme måde før). Alle fire er opfyldt, så det er et projekt. Konsekvensen af at behandle det som drift er, at der ikke udpeges en projektleder, ikke lægges en plan med milepæle, ikke afsættes ressourcer ud over den daglige bemanding, og ikke tages stilling til risici. Så bliver flytningen noget, der skal klares 'ved siden af', og den kolliderer med driften i første weekend.",
        "alt": "",
        "fisker": "Om du bruger de fire kendetegn SYSTEMATISK som en test frem for at svare på mavefornemmelse — og om du kan sige, hvad fejlen koster.",
        "soeg": ["projekt", "drift", "tidsbegrænset", "tværfagligt", "engangsopgave"],
    },
    {
        "fag": "Projektstyring", "emne": "Kendt og ukendt", "type": "rigtigt",
        "sp": "Hvad afgør, hvor detaljeret et projekt overhovedet kan planlægges?",
        "svar": "Hvor det ligger i kendt/ukendt-matricen, der krydser HVAD der skal laves med HVORDAN det skal laves. Er både hvad og hvordan kendt, er det rutineprojektet, og det kan detailplanlægges fra start — det er vandfaldets hjemmebane. Er målet kendt, men vejen ukendt, hjælper en agil tilgang, fordi man må lære undervejs. Er metoden kendt, men målet ikke, skal målet findes først. Er både hvad og hvordan ukendt, er man i et ægte nybrud — et prejekt — og der er ingen plan at lægge endnu; der skal undersøges. Pointen er, at planlægningsgraden ikke er et spørgsmål om grundighed, men om opgavens karakter.",
        "alt": "",
        "fisker": "Om du kan placere en konkret opgave i matricen og udlede planlægningsformen af placeringen — ikke omvendt.",
        "soeg": ["kendt", "ukendt", "prejekt", "matrix", "planlægning"],
    },
    {
        "fag": "Projektstyring", "emne": "Projektlederens beføjelser", "type": "rigtigt",
        "sp": "Projektlederen har brug for en medarbejder to dage om ugen, men driftschefen siger nej. Hvem har ret, og hvad gør projektlederen?",
        "svar": "Begge har ret inden for hver deres logik, og det er selve pointen. Konflikten er ikke personlig, den er STRUKTUREL: den midlertidige organisation lever inde i den permanente, projektlederen har sjældent formel instruktionsbeføjelse, og deltagerne har to chefer på samme tid. Driftschefen forsvarer sin leveringspræcision, projektlederen sin fremdrift. Vejen frem er STYREGRUPPEN — det er præcis den slags beslutning, projektlederen ikke må træffe selv, og som styregruppen er nedsat til at træffe. Og det, der skulle have været aftalt allerede i opstartsprocessen, er ressourcetrækket: hvor mange timer, fra hvem, og hvem der dækker driften imens.",
        "alt": "",
        "fisker": "Om du kalder konflikten strukturel og henviser til styregruppen. Svarer du 'projektlederen må overtale ham', har du ikke fat i organisationsformen.",
        "soeg": ["projektleder", "instruktionsbeføjelse", "styregruppe", "to chefer", "ressourcer"],
    },
    {
        "fag": "Projektstyring", "emne": "Projektorganisationen", "type": "rigtigt",
        "sp": "Hvem sidder i en projektorganisation, og hvilken gruppe glemmes oftest?",
        "svar": "Opdragsgiveren bestiller projektet og betaler for det. Styregruppen træffer de beslutninger, projektlederen ikke må træffe selv — typisk om ressourcer, ændringer i mål og penge. Projektlederen driver projektet fremad og rapporterer opad. Projektgruppen udfører arbejdet og er typisk udlånt fra driften. Ved siden af står REFERENCEGRUPPERNE, og de er dem, der oftest glemmes: det er dem, der skal BRUGE resultatet bagefter. Konsekvensen af at glemme dem er alvorlig, for det er dem, der afgør, om resultatet overhovedet kan bruges — et teknisk vellykket projekt, ingen vil arbejde i, er ikke vellykket.",
        "alt": "",
        "fisker": "Om du nævner referencegrupperne uopfordret og kan sige, hvorfor de betyder noget.",
        "soeg": ["projektorganisation", "styregruppe", "opdragsgiver", "referencegruppe"],
    },
    {
        "fag": "Projektstyring", "emne": "Vandfald eller agil", "type": "argument",
        "sp": "Et implementeringsprojekt skal i gang. Budgettet skal godkendes på forhånd. Vandfald eller agil?",
        "svar": "Jeg vil pege på den BLANDEDE form, og det er også den, man oftest møder i logistik: rammen og budgettet ligger fast, mens udførelsen er agil. Argumentet er, at agil ikke betyder 'uden styring' — det betyder, at prioriteringen genbesøges mellem korte forløb i stedet for at ligge fast fra start. Et fast budget udelukker altså ikke agil udførelse; det udelukker kun, at man løbende kan udvide scope. Forudsætningen, man skal nævne selv, er, at opdragsgiveren skal være tilgængelig LØBENDE og ikke kun ved milepæle. Kan han ikke det, holder den agile del ikke.",
        "alt": "Man kan forsvare rent vandfald, hvis målet er kendt fra start, metoden er brugt før, og kravene ligger fast — fx i et udbud, hvor kravene er bundet juridisk. Så er der intet at lære undervejs, og den agile overhead med løbende prioritering og hyppige møder koster mere, end den giver. Vandfald knækker først, når kravene ændrer sig undervejs, eller når fejl først opdages efter mange måneder.",
        "fisker": "Om du bruger kendt/ukendt-matricen som begrundelse, og om du nævner den blandede form frem for at vælge en yderlighed.",
        "soeg": ["vandfald", "agil", "blandet", "iterativ", "projektmodel"],
    },
    {
        "fag": "Projektstyring", "emne": "Agilitetens to dele", "type": "rigtigt",
        "sp": "Bogen skiller agilitet i to dele. Hvilke, og hvad sker der, hvis man kun tager den ene?",
        "svar": "Ledelsesdelen og procesdelen. Ledelsesdelen er projektlederens tilgang til medarbejderne og til den udadvendte del af opgaven — hvordan der ledes, faciliteres og rapporteres opad. Procesdelen er selve styringen, hvor det planlagte hele tiden forandres, fordi omverdenen og præmisserne ændrer sig. Tager man kun ledelsesdelen, får man en flad og involverende stil oven på en helt almindelig fast plan — et agilt skilt på noget, der ikke er agilt. Tager man kun procesdelen, får man løbende ændringer uden den ledelsesform, der skal holde teamet sammen om dem, og det ender i kaos. De to forudsætter hinanden.",
        "alt": "",
        "fisker": "Om du kan navngive begge dele og beskrive fejlen ved kun at tage den ene. Det er en klassisk 'agil på papiret'-diskussion.",
        "soeg": ["agil", "ledelsesdel", "procesdel", "projektledelse"],
    },
    {
        "fag": "Projektstyring", "emne": "Scrum: roller, lister og møder", "type": "rigtigt",
        "sp": "Hvad består Scrum af, og hvad er forskellen på sprint review og retrospektiv?",
        "svar": "Tre roller: produktejeren ejer prioriteringen og bestemmer HVAD der er vigtigst (ikke hvordan det løses), scrum masteren sikrer at processen holder og fjerner det, der spærrer for teamet (og er ikke chef), og udviklingsteamet leverer resultatet og planlægger selv sprintets indhold. Tre lister: produkt-backlog (alt det, der kunne laves, prioriteret), sprint-backlog (den bid, teamet har taget ind) og increment (det færdige og brugbare resultat). Fire møder: sprintplanlægning, daglig standup, sprint review og retrospektiv. Forskellen på de to sidste er central: REVIEW handler om PRODUKTET og vises for opdragsgiver og kommende brugere, mens RETROSPEKTIV handler om PROCESSEN og er teamets egen justering af, hvordan de arbejder. De må ikke blandes sammen.",
        "alt": "",
        "fisker": "Om du kan holde review og retrospektiv adskilt — produkt over for proces. Det er den hyppigste sammenblanding.",
        "soeg": ["scrum", "produktejer", "scrum master", "backlog", "sprint", "retrospektiv"],
    },
    {
        "fag": "Projektstyring", "emne": "De fem ting i balance", "type": "rigtigt",
        "sp": "Hvilke fem forhold skal en projektleder holde i balance, og hvad er pointen med at nævne dem samlet?",
        "svar": "Omgivelserne (organisationen omkring projektet ændrer sig undervejs), arbejdsgruppen (folk er udlånt, har to chefer og kan blive trukket tilbage), fremdriften (projektet skal bevæge sig, ikke bare være i gang), produktkvaliteten (det færdige resultat skal kunne bruges) og økonomien (forbruget holdes op mod budgettet hele vejen). Pointen er SAMTIDIGHEDEN: de fem trækker i hver sin retning, og optimerer man én, skrider en anden. Presser man fremdriften, falder kvaliteten eller økonomien; sikrer man kvaliteten, koster det tid. Projektledelse er derfor ikke at maksimere ét forhold, men at holde alle fem inden for det acceptable på samme tid.",
        "alt": "",
        "fisker": "Om du siger SAMTIDIGHED. Kan du kun remse de fem op, mangler du det, der gør dem til en ledelsesopgave.",
        "soeg": ["balance", "fremdrift", "produktkvalitet", "økonomi", "arbejdsgruppe"],
    },
    {
        "fag": "Projektstyring", "emne": "DISC, Adizes og Belbin", "type": "rigtigt",
        "sp": "Hvorfor må man ikke blande DISC, Adizes og Belbin sammen, når man sammensætter en gruppe?",
        "svar": "Fordi de svarer på tre FORSKELLIGE spørgsmål. DISC beskriver adfærdsstil — hvordan personen kommunikerer og reagerer. Adizes PAEI beskriver lederrolle — hvad personen bidrager med ledelsesmæssigt: producent, administrator, entreprenør eller integrator. Belbin beskriver teamrolle — hvordan personen opfører sig i gruppearbejde. Blander man dem, svarer man på et andet spørgsmål end det, der blev stillet: en lav integrator-score i Adizes siger ikke, at personen kommunikerer dårligt, og en høj D i DISC gør ikke nogen til en god leder. Belbin peger desuden på fire roller, der oftest mangler i en gruppe: idémanden, koordinatoren, analysatoren og afslutteren — den, der får de sidste tyve procent færdige.",
        "alt": "",
        "fisker": "Om du kan holde de tre linser adskilt og sige, hvad hver især måler. Det er selve øvelsens pointe.",
        "soeg": ["disc", "adizes", "paei", "belbin", "teamrolle", "gruppedannelse"],
    },
    {
        "fag": "Projektstyring", "emne": "Leadership og management", "type": "rigtigt",
        "sp": "Hvad er Kotters skel mellem leadership og management, og hvorfor har en projektleder brug for begge?",
        "svar": "Leadership sætter retning, motiverer og overbeviser, håndterer forandring og arbejder med MENNESKER. Management planlægger og budgetterer, organiserer og bemander, kontrollerer og løser problemer og arbejder med SYSTEMER. En projektleder har brug for begge, men sjældent i samme mængde. Uden management skrider planen, budgettet og opfølgningen. Uden leadership følger folk ikke med — og det er særligt kritisk i projekter, netop fordi projektlederen ikke har formel instruktionsbeføjelse og derfor må lede gennem retning og overbevisning frem for gennem ordrer. Vægtningen skifter desuden med projektets størrelse og med, hvor kendt opgaven er.",
        "alt": "",
        "fisker": "Om du kobler leadership til den manglende instruktionsbeføjelse. Det er dét, der gør skellet relevant lige her.",
        "soeg": ["kotter", "leadership", "management", "ledelse", "administration"],
    },

    # =====================================================================
    # DISTRIBUTION — transportmarkedet og aktørerne
    # =====================================================================
    {
        "fag": "Distribution", "emne": "Speditør, fragtfører og mægler", "type": "rigtigt",
        "sp": "Hvad er forskellen på en speditør og en fragtfører, og hvorfor betyder den forskel juridisk?",
        "svar": "En fragtfører udfører selv transporten og hæfter derfor for godset efter den konvention, der gælder for transportformen. En speditør formidler transporten: han tilrettelægger og indgår aftaler på kundens vegne, men kører ikke nødvendigvis selv. Forskellen er afgørende, når godset bliver skadet, fordi den afgør, HVEM man har et krav mod og efter hvilket regelsæt. En speditør, der optræder som formidler, hæfter typisk kun for egne fejl i tilrettelæggelsen, mens en speditør der påtager sig transportøransvar reelt agerer fragtfører og hæfter derefter. Derfor er det første spørgsmål i en skadessag ikke 'hvem kørte?', men 'i hvilken rolle handlede modparten ifølge aftalen?'.",
        "alt": "",
        "fisker": "Om du kan se, at rollen — ikke firmanavnet — afgør ansvaret, og at samme virksomhed kan optræde i begge roller.",
        "soeg": ["speditør", "fragtfører", "transportør", "formidler", "ansvar"],
    },
    {
        "fag": "Distribution", "emne": "Trafikstyringens opgaver", "type": "rigtigt",
        "sp": "Hvad er trafikstyringens funktioner i en virksomhed, og hvorfor er valg af transportform kun én af dem?",
        "svar": "Trafikstyring dækker hele styringen af virksomhedens transport: valg af transportform og transportør, forhandling af rater, planlægning og konsolidering af sendinger, dokumenthåndtering, opfølgning på leveringer og behandling af reklamationer og skader. Valget af transportform er kun det ene led, og ofte ikke det, der giver den største gevinst. Konsolidering — at samle flere små sendinger til færre store — flytter typisk mere på omkostningen end at skifte transportør, fordi fragtrater falder med sendingsstørrelsen. Dertil kommer, at dokumenter og told kan stoppe en sending fuldstændigt, uanset hvor godt transportformen er valgt.",
        "alt": "",
        "fisker": "Om du kan opremse flere funktioner end transportvalg — og pege på konsolidering som et stærkt håndtag.",
        "soeg": ["trafikstyring", "konsolidering", "rater", "dokumenter", "reklamation"],
    },
    {
        "fag": "Distribution", "emne": "Serviceklager fra kunder", "type": "rigtigt",
        "sp": "Hvilke hovedtyper af serviceklager møder en transportkøber, og hvad fortæller de om systemet?",
        "svar": "Klagerne falder typisk i fire grupper: forsinkelser (godset kom for sent), skader og svind (godset kom beskadiget eller ufuldstændigt), fejl i dokumenter og fakturering, og manglende information undervejs. Den sidste er værd at hæfte sig ved, fordi den ikke handler om godset overhovedet — kunden kan være utilfreds med en leverance, der ankom til tiden og i god stand, hvis han ikke vidste hvor den var. Klagemønsteret er derfor en diagnose: mange forsinkelser peger på planlægning eller kapacitet, mange skader på emballering og håndtering, og mange informationsklager på manglende sporing og kommunikation.",
        "alt": "",
        "fisker": "Om du behandler klagerne som DATA om systemet frem for som enkeltsager der skal lukkes.",
        "soeg": ["serviceklager", "forsinkelse", "svind", "sporing", "kundeservice"],
    },
    {
        "fag": "Distribution", "emne": "Fragttillæg og ratevarsler", "type": "rigtigt",
        "sp": "Et rederi varsler en ratestigning med kort frist. Hvad kigger du på, før du accepterer?",
        "svar": "Først på hvad der faktisk stiger: grundraten eller et tillæg. Fragtpriser er sjældent ét tal — de består af en grundrate plus tillæg for brændstof, valutaudsving, havneomkostninger og sæsonspidser. Et varsel om tillæg rammer anderledes end en varslet grundrate, fordi tillæg typisk er knyttet til et indeks og derfor kan falde igen. Dernæst på DATOEN: kort varsel er et forhandlingssignal, og fristen afgør, om du kan nå at flytte volumen eller fremrykke sendinger. Endelig på kontrakten: er raten aftalt for en periode, eller er den spot? Er den aftalt, er varslet et oplæg til genforhandling, ikke en meddelelse.",
        "alt": "",
        "fisker": "Om du skiller grundrate fra tillæg og lægger mærke til varslingsfristen. Det er dér, forhandlingsrummet ligger.",
        "soeg": ["rate", "tillæg", "baf", "caf", "varsel", "spot", "kontraktrate"],
    },
    {
        "fag": "Distribution", "emne": "Skader på containergods", "type": "rigtigt",
        "sp": "En container ankommer med væltet og beskadiget gods. Hvad er de typiske årsager, og hvem har ansvaret for stuvningen?",
        "svar": "De typiske årsager er dårlig stuvning og manglende sikring inde i containeren, overbelastning af de nederste kolli, fugt og kondens, og bevægelser i søgang, hvor stakke kan kollapse. Ansvaret afhænger af, hvem der pakkede containeren. Er den stuvet af afsenderen og forseglet, er det som udgangspunkt afsenderens ansvar, at godset er sikret til at tåle en normal rejse — rederiet hæfter ikke for skader, der skyldes mangelfuld stuvning, det ikke kunne se. Derfor er stuvningsinstruks, surring og fugtbeskyttelse ikke en detalje, men en del af risikofordelingen.",
        "alt": "",
        "fisker": "Om du kobler ansvaret til, HVEM der pakkede containeren — det er det spørgsmål, der afgør sagen.",
        "soeg": ["container", "stuvning", "surring", "kondens", "søgang", "skade"],
    },
    {
        "fag": "Distribution", "emne": "Certificeringer i transport", "type": "rigtigt",
        "sp": "Hvorfor kræver kunder certificeringer af deres transportører, og hvordan vælger man den rigtige?",
        "svar": "Fordi certificeringen er et bevis på, at der findes et STYRINGSSYSTEM og ikke bare gode intentioner — en uafhængig part har kontrolleret, at processerne er beskrevet, følges og revideres. Kunden kan ikke selv auditere alle sine leverandører, så certificeringen erstatter den kontrol. Man vælger efter, hvad godset kræver: kvalitetsstyring dækker processer generelt, miljø- og energiledelse dækker klima- og forbrugsforhold, arbejdsmiljø dækker sikkerheden for medarbejderne, og der findes branchespecifikke ordninger for fødevarer, medicin, sikret transport og toldforenkling. Pointen til et forsvar: match certificeringen til godsets risiko — en ordning, der ikke rammer godsets faktiske sårbarhed, er en omkostning uden effekt.",
        "alt": "",
        "fisker": "Om du kan forklare, at certificering dokumenterer et SYSTEM, og at valget skal matche godsets risiko.",
        "soeg": ["certificering", "iso", "aeo", "kvalitetsstyring", "audit", "compliance"],
    },
    {
        "fag": "Distribution", "emne": "Højresving og bløde trafikanter", "type": "rigtigt",
        "sp": "Hvorfor sker der stadig højresvingsulykker mellem lastbiler og cyklister, og hvad kan en transportvirksomhed gøre?",
        "svar": "Fordi risikoen opstår i samspillet mellem to parter, der begge handler rimeligt hver for sig. På lastbilens side er der blinde vinkler, høj førerposition og mange spejle at nå at aflæse i det sekund, svinget tages. På cyklistens side er der en forventning om, at man er set, og en tendens til at køre op langs siden af en holdende lastbil, hvor føreren ikke kan se ned. Virksomhedens greb er derfor både teknik og adfærd: afstandssensorer og kamera til at dække den blinde vinkel, faste rutiner for spejlkontrol før sving, ruteplanlægning der undgår de værste kryds i myldretiden, og træning af chaufførerne i, hvor cyklisten typisk befinder sig.",
        "alt": "",
        "fisker": "Om du behandler det som et SYSTEMproblem med greb på begge sider — ikke som en chaufførfejl.",
        "soeg": ["højresving", "blind vinkel", "cyklist", "spejle", "trafiksikkerhed"],
    },
    {
        "fag": "Distribution", "emne": "Risiko på transportkorridorer", "type": "rigtigt",
        "sp": "Hvorfor indgår vejens og korridorens tilstand i et transportvalg, og hvad gør man ved det?",
        "svar": "Fordi transporttid ikke kun afhænger af afstand og transportform, men af hvor pålidelig strækningen er. En korridor med dårlig vej, ekstreme vejrforhold, grænsekontrol eller politisk ustabilitet har en meget større SPREDNING i transporttiden, selvom gennemsnittet måske ser fornuftigt ud. Og det er spredningen, ikke gennemsnittet, der driver sikkerhedslageret. Greb: planlæg med realistiske og ikke gennemsnitlige transporttider, hav en alternativ rute eller transportform klar, forsikr efter den faktiske risiko, og indregn ventetid ved grænser. Til en case er pointen, at billig transport ad en upålidelig korridor kan blive dyr i lager og tabt salg.",
        "alt": "",
        "fisker": "Om du taler om SPREDNING i transporttiden og kobler den til sikkerhedslageret — ikke bare om at det tager længere tid.",
        "soeg": ["korridor", "risiko", "variabilitet", "alternativ rute", "grænse"],
    },

    # =====================================================================
    # DISTRIBUTION — lager i dybden
    # =====================================================================
    {
        "fag": "Distribution", "emne": "Hvorfor overhovedet lager", "type": "rigtigt",
        "sp": "Lager er kapitalbinding og spild ifølge Lean. Hvorfor har virksomheder alligevel lagre?",
        "svar": "Fordi lageret løser fire problemer, som ellers ville koste mere. Det udligner forskellen mellem indkøbs- eller produktionstakt og salgstakt, så man kan producere i økonomiske serier og alligevel levere løbende. Det dækker usikkerhed i både efterspørgsel og leveringstid — det er sikkerhedslagerets rolle. Det gør konsolidering mulig, så man kan købe og transportere i større og billigere mængder. Og det giver mulighed for at samle, ompakke og kundetilpasse tæt på kunden i stedet for tidligt i kæden. Lean har ret i, at lager skjuler problemer, men konklusionen er ikke nul lager — den er, at lageret skal have en grund, man kan sætte ord på.",
        "alt": "",
        "fisker": "Om du kan give lageret en FUNKTION i stedet for at forsvare det som nødvendigt onde.",
        "soeg": ["lager", "udligning", "usikkerhed", "konsolidering", "postponement"],
    },
    {
        "fag": "Distribution", "emne": "Lagerets arbejdsgang", "type": "rigtigt",
        "sp": "Beskriv lagerets arbejdsgang fra rampe til afsendelse — og hvor ligger omkostningen?",
        "svar": "Modtagelse og kontrol af det indgående, placering på lokation, opbevaring, plukning af ordrer, pakning og forsendelsesklargøring, og endelig afsendelse. Omkostningen er meget ujævnt fordelt: plukningen står typisk for langt den største del af lagerets arbejdstid, fordi den indebærer bevægelse for hver enkelt ordrelinje, mens opbevaring i sig selv koster plads, men næsten ingen arbejdstid. Derfor er det placeringen af varerne — hvad der ligger tæt på plukruten — der har størst effekt på omkostningen, og ikke hvor effektivt der køres på rampen. Til en case: optimér plukket først.",
        "alt": "",
        "fisker": "Om du kan pege på plukningen som den dominerende omkostning og begrunde det med bevægelse pr. ordrelinje.",
        "soeg": ["modtagelse", "placering", "plukning", "pakning", "arbejdsgang"],
    },
    {
        "fag": "Distribution", "emne": "Lagerets KPIer", "type": "rigtigt",
        "sp": "Hvilke nøgletal styrer man et lager efter, og hvad er faren ved at måle på ét af dem alene?",
        "svar": "Typisk måles der på plukkeeffektivitet (linjer eller ordrer pr. time), plukkenøjagtighed (andel fejlfrie plukninger), pladsudnyttelse og leveringspræcision. Faren ved at måle på ét alene er, at de trækker mod hinanden. Presser man udelukkende plukkeeffektiviteten, stiger fejlprocenten, fordi der skæres hjørner — og en plukkefejl er dyr: den udløser returnering, ny forsendelse, administration og en utilfreds kunde, hvilket koster mange gange den sparede tid. Presser man pladsudnyttelsen maksimalt, bliver plukningen langsommere, fordi varerne står tættere og sværere tilgængeligt. Derfor skal nøgletallene læses SAMMEN.",
        "alt": "",
        "fisker": "Om du kan sætte to nøgletal op mod hinanden og forklare, hvorfor en plukkefejl er dyrere end den sparede tid.",
        "soeg": ["kpi", "plukkeeffektivitet", "nøjagtighed", "pladsudnyttelse", "plukkefejl"],
    },
    {
        "fag": "Distribution", "emne": "Hvad et WMS giver", "type": "rigtigt",
        "sp": "Hvad giver et lagerstyringssystem (WMS), som et regneark ikke kan?",
        "svar": "Et WMS styrer lokationer og bevægelser i realtid: det ved, hvor hver enkelt vare står, hvad der er reserveret, og hvad der er på vej ind og ud. Det giver fire ting, et regneark ikke kan. Det kan styre plukruten, så plukkeren går den korteste vej og samler flere ordrer i én tur. Det kan placere varer dynamisk efter omsætningshastighed, så højfrekvente varer flytter tættere på udgangen. Det giver sporbarhed på batch og dato, hvilket er et krav i fødevarer og medicin. Og det giver data til at måle og forbedre, fordi hver bevægelse registreres. Prisen er, at systemet kræver disciplin: registreres en flytning ikke, er varen borte i systemets øjne, selvom den står på hylden.",
        "alt": "",
        "fisker": "Om du nævner både gevinsten OG forudsætningen: et WMS er kun så godt som registreringsdisciplinen.",
        "soeg": ["wms", "lokationsstyring", "plukrute", "sporbarhed", "realtid"],
    },
    {
        "fag": "Distribution", "emne": "Niveauer af logistikoutsourcing", "type": "rigtigt",
        "sp": "Hvad ligger der i 1PL, 2PL, 3PL og 4PL, og hvad afgør, hvor langt man skal gå?",
        "svar": "1PL er, at virksomheden selv udfører transporten med egne biler og eget lager. 2PL er at købe en enkelt ydelse — fx transport — af en leverandør. 3PL er at lægge en samlet pakke ud: lager, plukning, pakning og distribution hos en partner, der driver det som sin kerneforretning. 4PL går et skridt videre, hvor en part styrer og koordinerer hele forsyningskæden på tværs af flere leverandører uden nødvendigvis selv at eje aktiverne. Hvor langt man skal gå afhænger af, om logistikken er en KONKURRENCEPARAMETER: er den en del af værditilbuddet, beholder man kontrollen; er den en støtteproces, kan en specialist ofte gøre det billigere og bedre.",
        "alt": "",
        "fisker": "Om du kan trappen OG kan koble valget til, om logistikken er kernekompetence eller støtteproces.",
        "soeg": ["1pl", "2pl", "3pl", "4pl", "outsourcing", "logistikpartner"],
    },

    # =====================================================================
    # DISTRIBUTION — netværksdesign og bæredygtighed
    # =====================================================================
    {
        "fag": "Distribution", "emne": "Beslutninger i netværksdesign", "type": "rigtigt",
        "sp": "Hvilke beslutninger træffer man i netværksdesign, og i hvilken rækkefølge?",
        "svar": "Fire beslutninger, og rækkefølgen betyder noget. Først faciliteternes ROLLE: hvad skal anlægget lave — produktion, lager, cross-docking, kundetilpasning? Dernæst PLACERINGEN: hvor i verden eller landet skal det ligge. Så KAPACITETEN: hvor stort skal det være. Og til sidst ALLOKERINGEN: hvilke markeder og kunder betjenes fra hvilket anlæg. Rækkefølgen er vigtig, fordi en placering, der er valgt uden at rollen er afklaret, låser fast. Beslutningerne er desuden langsigtede og dyre at rulle tilbage — man flytter ikke et lager, fordi efterspørgslen skifter et halvt år. Derfor arbejder man med scenarier frem for ét punktestimat.",
        "alt": "",
        "fisker": "Om du kender de fire OG kan begrunde rækkefølgen — rolle før placering.",
        "soeg": ["netværksdesign", "facilitetsrolle", "placering", "kapacitet", "allokering"],
    },
    {
        "fag": "Distribution", "emne": "Tyngdepunktsmetodens begrænsning", "type": "argument",
        "sp": "Tyngdepunktsmetoden peger på et bestemt punkt på kortet. Skal lageret ligge dér?",
        "svar": "Nej, ikke uden videre. Metoden minimerer vægtet transportafstand i LUFTLINJE og antager, at fragtraten er ens i alle retninger. Virkeligheden har veje, ikke luftlinjer; den har motorveje, færger og bjerge; og raterne er ikke symmetriske. Dertil kommer alt det, modellen slet ikke kan se: grundpriser, arbejdskraft, adgang til motorvej og havn, byggetilladelser og medarbejdernes pendling. Tyngdepunktet er derfor et kvalificeret UDGANGSPUNKT, som skal holdes op mod konkrete kandidatplaceringer i nærheden — og de kan sagtens vinde, selvom deres beregnede omkostning er lidt højere.",
        "alt": "Man kan forsvare at følge beregningen tættere, hvis transportomkostningen dominerer totalbilledet — mange og tunge sendinger over lange afstande — og hvis de øvrige omkostninger er nogenlunde ens i regionen. Så er modellens forsimplinger små i forhold til den gevinst, den peger på, og at afvige koster reelle penge hver eneste dag.",
        "fisker": "Om du kender modellens ANTAGELSER og kan sige, hvornår de holder. Et svar der bare siger 'ja, dér' viser ingen modelforståelse.",
        "soeg": ["tyngdepunkt", "luftlinje", "antagelser", "kandidatplacering", "lokalisering"],
    },
    {
        "fag": "Distribution", "emne": "Modal shift", "type": "argument",
        "sp": "Skal virksomheden flytte gods fra lastbil til bane eller skib for at sænke CO₂?",
        "svar": "Ja, hvis godset tåler det. Bane og skib har markant lavere udledning pr. tonkm end vej, og for tungt, robust gods over lange afstande er modal shift et af de kraftigste greb, en logistiker selv råder over — det kræver ingen ny teknologi. Forudsætningen er, at godset ikke er hastende, at der er tilstrækkelig volumen til at fylde enheden, og at der findes terminaler i nærheden af begge ender. Dertil skal man regne omlastningerne med: hver omlastning koster tid, penge og en risiko for skade.",
        "alt": "Man kan forsvare at blive på vej: intermodal transport indfører omlastninger, længere transporttid og større spredning i leveringstiden, og den spredning skal dækkes af sikkerhedslager. For gods med høj værdi, kort holdbarhed eller uforudsigelig efterspørgsel kan CO₂-gevinsten være reel, men mindre værd end den fleksibilitet, man mister. Argumentet er, at klimahensynet skal vejes mod kundens servicekrav og ikke stå alene.",
        "fisker": "Om du inddrager omlastninger og spredning i transporttiden — ikke bare sammenligner g CO₂ pr. tonkm.",
        "soeg": ["modal shift", "intermodal", "bane", "omlastning", "tonkm"],
    },
    {
        "fag": "Distribution", "emne": "Elektrificering af godstransport", "type": "rigtigt",
        "sp": "Hvorfor er lokal distribution lettere at elektrificere end langdistancetransport?",
        "svar": "Fordi batteriets vægt og ladetid rammer hårdest, når distancen er lang. I lokal distribution er dagsstrækningen kort og forudsigelig, køretøjet holder stille på et depot om natten, hvor der kan lades, og den ekstra batterivægt går kun fra en lastkapacitet, der sjældent er fuldt udnyttet på bydistribution. Ved langdistance skal batteriet enten være så stort, at det æder nyttelasten, eller også skal der lades undervejs, hvilket koster køretid og kræver en ladeinfrastruktur langs korridorerne. Derfor peger scenarierne på andre løsninger på lange stræk: elektrificering af selve vejen, brintbaserede løsninger eller flytning af godset til bane og skib.",
        "alt": "",
        "fisker": "Om du kan forklare afvejningen batterivægt over for nyttelast, og hvorfor depotladning gør lokal distribution let.",
        "soeg": ["elektrificering", "batteri", "nyttelast", "ladeinfrastruktur", "ers"],
    },

    # =====================================================================
    # PROJEKTSTYRING — de fire processer
    # =====================================================================
    {
        "fag": "Projektstyring", "emne": "De fire processer", "type": "rigtigt",
        "sp": "Hvilke fire processer gennemløber et projekt, og hvad er formålet med hver?",
        "svar": "Opstart, planlægning, gennemførelse og afslutning. I OPSTARTEN bliver en idé til et godkendt projekt: formålet afklares, rammen og mandatet fastlægges, og der tages stilling til, om projektet overhovedet skal sættes i gang. I PLANLÆGNINGEN kortlægges interessenter og risici, og planen lægges — det er her, arbejdet gøres muligt at styre. I GENNEMFØRELSEN udføres og kontrolleres arbejdet løbende, og afvigelser håndteres. I AFSLUTNINGEN afleveres resultatet, og både processen og resultatet evalueres. Pointen med at have en afslutningsproces er, at et projekt ellers har det med at fise ud: uden en formel aflevering ved ingen, hvornår ansvaret går tilbage til driften.",
        "alt": "",
        "fisker": "Om du kan give hver fase et FORMÅL og især kan forsvare, hvorfor afslutningen er en selvstændig proces.",
        "soeg": ["opstart", "planlægning", "gennemførelse", "afslutning", "projektmodel"],
    },
    {
        "fag": "Projektstyring", "emne": "Opstartsprocessen", "type": "rigtigt",
        "sp": "Hvad er projektlederens vigtigste opgave i opstarten, og hvad koster det at springe den over?",
        "svar": "At få rammen og mandatet på plads, før arbejdet går i gang: hvad er formålet, hvad er i og uden for scope, hvilke ressourcer er der, hvem beslutter hvad, og hvornår er projektet lykkedes. Det lyder som formalia, men det er dér, de fleste projekter afgøres. Springer man det over, opdager man først undervejs, at opdragsgiver og projektleder har forskellige billeder af målet, at ressourcerne aldrig blev aftalt med afdelingscheferne, og at ingen ved, hvem der må godkende en ændring. Så bruges gennemførelsen på at forhandle det, der skulle have været aftalt i opstarten — og det er dyrt, fordi der samtidig er en plan, der skrider.",
        "alt": "",
        "fisker": "Om du kan sætte ord på, at opstartens produkt er ENIGHED — ikke dokumenter.",
        "soeg": ["opstart", "mandat", "scope", "formål", "succeskriterier"],
    },
    {
        "fag": "Projektstyring", "emne": "Risikostyring i projektet", "type": "rigtigt",
        "sp": "Hvordan arbejder man med risici i et projekt, og hvorfor er en risikoliste ikke nok?",
        "svar": "Man identificerer risici, vurderer dem på sandsynlighed og konsekvens, prioriterer dem derefter, og beslutter en HANDLING for hver: undgå, reducere, overføre (fx forsikre) eller acceptere bevidst. En ren liste er ikke nok, fordi den ikke ændrer noget — værdien opstår, når hver væsentlig risiko har en ejer, en handling og et tidspunkt, hvor den følges op. Dertil skal listen leve: risici ændrer sig undervejs, nogle forsvinder, og nye kommer til, så den skal genbesøges gennem hele gennemførelsen. En risikoliste, der blev skrevet i planlægningen og aldrig åbnet igen, er dokumentation, ikke styring.",
        "alt": "",
        "fisker": "Om du nævner de fire håndteringsmuligheder OG at listen skal have ejere og følges op løbende.",
        "soeg": ["risiko", "sandsynlighed", "konsekvens", "risikolog", "handling"],
    },
    {
        "fag": "Projektstyring", "emne": "Ændringer i projektplanen", "type": "rigtigt",
        "sp": "Opdragsgiveren beder om en ekstra funktion midt i projektet. Hvordan håndterer du det?",
        "svar": "Ikke ved at sige nej, og ikke ved bare at sige ja. Ændringen skal PRISSÆTTES i tid, penge og risiko og lægges op til den, der har mandat til at beslutte — typisk styregruppen. Pointen er, at et projekt har en fast trekant af scope, tid og ressourcer: udvides scope, må enten tid eller ressourcer følge med, ellers går det ud over kvaliteten. Den klassiske fejl er scope creep, hvor en række små ændringer hver for sig virker rimelige og tilsammen sprænger projektet, fordi ingen af dem blev prissat. Derfor er svaret en ændringsprocedure aftalt på forhånd — ikke en forhandling i hvert enkelt tilfælde.",
        "alt": "",
        "fisker": "Om du nævner scope creep og henviser beslutningen til styregruppen frem for at træffe den selv.",
        "soeg": ["ændring", "scope creep", "styregruppe", "trekant", "prissætning"],
    },
    {
        "fag": "Projektstyring", "emne": "Projektets logbog", "type": "rigtigt",
        "sp": "Hvorfor føres der logbog i et projekt, når man alligevel holder statusmøder?",
        "svar": "Fordi logbogen fastholder BESLUTNINGER og deres begrundelse, og det gør statusmøder ikke. Et halvt år senere kan ingen huske, hvorfor man valgte den ene løsning frem for den anden, hvem der godkendte det, og hvilke forudsætninger der lå til grund. Uden logbog bliver den diskussion taget forfra, ofte med nye deltagere og uden det, man vidste dengang. Logbogen har desuden to andre roller: den er grundlaget for evalueringen i afslutningsprocessen, hvor man skal kunne se, hvad der faktisk skete, og den er dokumentation, hvis der senere opstår uenighed om, hvad der blev aftalt.",
        "alt": "",
        "fisker": "Om du fremhæver BEGRUNDELSEN for beslutninger — ikke bare at det er en dagbog over aktiviteter.",
        "soeg": ["logbog", "beslutninger", "dokumentation", "evaluering", "erfaring"],
    },
    {
        "fag": "Projektstyring", "emne": "Afslutning og evaluering", "type": "rigtigt",
        "sp": "Hvad skal der ske i afslutningsprocessen, og hvad evaluerer man på?",
        "svar": "Resultatet skal formelt AFLEVERES, så ansvaret går fra projektet tilbage til driften — der skal være en modtager, en overdragelse og en accept. Derefter evalueres der på to ting, som ikke må blandes sammen: RESULTATET (nåede vi målet, inden for tid og budget, og kan det bruges?) og PROCESSEN (hvordan arbejdede vi, hvad gik godt, hvad ville vi gøre anderledes?). Resultatevalueringen svarer opdragsgiveren; procesevalueringen er organisationens læring til næste projekt. Springes afslutningen over, sker der typisk to ting: driften føler sig ikke ansvarlig for noget, den ikke har taget imod, og de samme fejl gentages i næste projekt.",
        "alt": "",
        "fisker": "Om du skiller resultat fra proces — og om du nævner den formelle overdragelse til driften.",
        "soeg": ["afslutning", "aflevering", "evaluering", "overdragelse", "læring"],
    },
    {
        "fag": "Projektstyring", "emne": "Fordele ved den agile proces", "type": "rigtigt",
        "sp": "Hvad vinder man konkret ved at arbejde agilt, og hvad er prisen?",
        "svar": "Fire ting. OVERBLIK: alle ved, hvad der foregår, og kan nå at reagere på ændringer, fordi arbejdet er synligt i korte forløb. HURTIGT UDBYTTE: der leveres brugbare bidder løbende i stedet for alt til sidst, så værdien kommer tidligere. EJERSKAB: når man kan se resultatet undervejs, giver arbejdet mening, og teamet planlægger selv sit næste forløb. BRUGERFOKUS: detaljerne fastlægges undervejs, mens produktet tager form, og med brugerne inde over. Prisen er, at det kræver mere af omgivelserne: opdragsgiveren skal være tilgængelig løbende og ikke kun ved milepæle, og organisationen skal kunne leve med, at det præcise slutindhold ikke er kendt fra start.",
        "alt": "",
        "fisker": "Om du kan nævne prisen — især kravet om en løbende tilgængelig opdragsgiver. Uden det lyder agil som gratis.",
        "soeg": ["agil", "overblik", "ejerskab", "brugerfokus", "increment"],
    },
    {
        "fag": "Projektstyring", "emne": "Hvorfor virksomheder vælger agilt", "type": "rigtigt",
        "sp": "Hvilke forretningsmæssige grunde er der til at vælge agil projektstyring?",
        "svar": "Tre, og ingen af dem handler om at slippe for at planlægge. TIME TO MARKET: kortere tid og lavere omkostninger, så løsningen når markedet før konkurrenterne — man leverer noget brugbart tidligt frem for alt sent. PRIORITERING: i projekter, hvor omfang og sluttidspunkt ikke kan overskues fra start, giver det mening at prioritere løbende og tage det vigtigste først, så man altid har leveret det, der betyder mest. STRATEGI: projektets mål kan rettes ind efter virksomhedens overordnede strategi undervejs, i stedet for at være låst fast til det, man troede for et år siden. Bemærk, at alle tre forudsætter styring — bare en anden slags.",
        "alt": "",
        "fisker": "Om du eksplicit afviser, at agil betyder mindre styring. Det er den hyppigste misforståelse.",
        "soeg": ["time to market", "prioritering", "strategi", "agil", "forretning"],
    },
    {
        "fag": "Projektstyring", "emne": "Det agile gennemløb", "type": "rigtigt",
        "sp": "Hvad består ét agilt gennemløb af, og hvad betyder det, at en bid skal være 'færdig'?",
        "svar": "Tre trin, der gentages: PLANLÆG (den næste bid prioriteres sammen med opdragsgiver og brugere), UDARBEJD (bidden laves helt færdig, og kontrollen sker i arbejdsgruppen) og IMPLEMENTÉR (resultatet tages i brug og giver feedback til næste bid). At en bid er færdig betyder BRUGBAR — den kan tages i anvendelse, ikke bare være teknisk fuldført. Halvt lavet arbejde tæller ikke med, og det er en hård regel: en bid, der er 90 % færdig, leverer nul værdi og skjuler samtidig, hvor langt projektet reelt er. Det er dét, der gør, at fremdriften kan måles ærligt i agile forløb.",
        "alt": "",
        "fisker": "Om du kan definere 'færdig' som BRUGBAR og forklare, hvorfor halvt arbejde ikke tælles med.",
        "soeg": ["gennemløb", "increment", "færdig", "feedback", "iteration"],
    },
    {
        "fag": "Projektstyring", "emne": "Projektlederens tre roller", "type": "rigtigt",
        "sp": "Hvilke tre roller har en projektleder, og hvordan skifter vægtningen?",
        "svar": "TEAMLEDER: får gruppen til at fungere — motivation, konflikter og retning. INTEGRATOR: binder fagligheder sammen på tværs af funktioner, så delene passer sammen til en helhed. KOORDINATOR: holder styr på opgaver, tid og afhængigheder. Vægtningen skifter med projektets størrelse og organisationsform. I et lille projekt fylder koordinatorrollen mest, fordi lederen selv er tæt på arbejdet. I et stort, tværfagligt projekt bliver integratorrollen den afgørende, fordi risikoen ikke ligger i de enkelte dele, men i sammenføjningen. Og i et projekt med modstand eller usikkerhed fylder teamlederrollen mest.",
        "alt": "",
        "fisker": "Om du kan sige, hvad der får vægtningen til at skifte — ikke bare remse de tre op.",
        "soeg": ["teamleder", "integrator", "koordinator", "projektleder", "roller"],
    },
]


# ===========================================================================
# DYBDE-KÆDER — "Eksaminator borer" lag for lag
# ===========================================================================
# Struktur som KÆDER i siden: {emne, fag, lag:[{sp, arg, fisker, alt, snyd, fakta}]}
# snyd=True markerer et lag, hvor præmissen i spørgsmålet er forkert.
KAEDER_3SEM = [
    {"emne": "De 5 Lean-principper", "fag": "Distribution", "lag": [
        {"sp": "Hvad er de fem Lean-principper?",
         "arg": "Værdi, værdistrøm, flow, pull og perfektion — i den rækkefølge. "
                "Værdi defineres af kunden, værdistrømmen kortlægger alle skridt, "
                "flow får arbejdet til at glide, pull producerer på signal, og "
                "perfektion er den løbende gentagelse.",
         "fisker": "Om du kan alle fem og kan holde rækkefølgen.",
         "alt": "", "snyd": False, "fakta": True},
        {"sp": "Hvorfor står værdi først og ikke flow?",
         "arg": "Fordi der ikke er nogen grund til at optimere flowet i noget, "
                "kunden ikke betaler for. Definerer man ikke værdien først, "
                "risikerer man at gøre spild mere effektivt — man kommer hurtigere "
                "frem ad en vej, der ikke fører nogen steder.",
         "fisker": "Om du kan begrunde rækkefølgen frem for bare at gengive den.",
         "alt": "", "snyd": False, "fakta": False},
        {"sp": "En virksomhed indfører kanban for at komme i gang med Lean uden "
               "først at have arbejdet med flow. Er det en god genvej?",
         "arg": "Nej — det er fælden. Pull uden flow får hvert led til at lægge "
                "buffer ind for at kunne svare på trækket, så lagrene VOKSER i "
                "stedet for at falde. Pull uden flow er bare et lager med et nyt "
                "navn. Rækkefølgen er ikke pædagogik, den er årsagssammenhæng.",
         "fisker": "Om du falder for at kanban er et let første skridt, eller om du "
                   "ser, at forudsætningen mangler.",
         "alt": "", "snyd": True, "fakta": False},
        {"sp": "Hvornår er man så færdig med Lean?",
         "arg": "Aldrig — og det er hele femte princip. Perfektion er en retning, "
                "ikke en tilstand. Så snart flowet forbedres, bliver den næste "
                "flaskehals synlig, og værdistrømmen skal kortlægges igen. "
                "Virksomheder, der behandler Lean som et projekt med en slutdato, "
                "ruller typisk tilbage inden for et par år.",
         "fisker": "Om du kan forklare, hvorfor Lean ikke kan afsluttes som et projekt.",
         "alt": "", "snyd": False, "fakta": False},
    ]},

    {"emne": "Udnyttelsesgrad og gennemløbstid", "fag": "Distribution", "lag": [
        {"sp": "Hvad er udnyttelsesgrad, og hvordan regnes den?",
         "arg": "Andelen af den tilgængelige kapacitet, der faktisk bruges — "
                "belastning divideret med kapacitet. Ligger den på 0,8, arbejdes "
                "der 80 % af tiden.",
         "fisker": "Om du kan definitionen og kan skelne belastning fra kapacitet.",
         "alt": "", "snyd": False, "fakta": True},
        {"sp": "Hvad sker der med ventetiden, når udnyttelsesgraden stiger fra "
               "0,80 til 0,95?",
         "arg": "Den eksploderer. Sammenhængen er ikke lineær: køen vokser "
                "voldsomt, når man nærmer sig fuld udnyttelse, fordi der ikke er "
                "luft til at indhente selv små udsving. Kurven er en hockeystav, "
                "og gennemløbstiden følger den.",
         "fisker": "Om du siger IKKE-LINEÆR og kan beskrive kurvens form.",
         "alt": "", "snyd": False, "fakta": False},
        {"sp": "Så høj udnyttelsesgrad er bare dårligt — vi bør sigte lavt?",
         "arg": "Nej, det er den modsatte grøft. Meget lav udnyttelse betyder "
                "dyr, ubrugt kapacitet, og det er heller ikke gratis. Pointen er "
                "ikke at minimere udnyttelsen, men at planlægge BEVIDST med "
                "reservekapacitet, så variationen kan absorberes. QRM sætter et "
                "tal på det og styrer efter det i stedet for at jagte 100 %.",
         "fisker": "Om du kan holde begge grøfter fra dig og lande på en bevidst "
                   "afvejning frem for en tommelfingerregel.",
         "alt": "", "snyd": True, "fakta": False},
        {"sp": "Hvordan oversætter du argumentet til noget, en økonomichef lytter til?",
         "arg": "Ved at regne på tabt dækningsbidrag. Lang gennemløbstid koster "
                "ordrer, fordi leveringstid er en konkurrenceparameter, og en "
                "mistet ordre koster hele dækningsbidraget. Det skal holdes op "
                "mod værdien af en ekstra udnyttet maskintime. Er "
                "dækningsbidraget pr. ordre stort, vinder reservekapaciteten "
                "regnestykket — og det er et argument i kroner, ikke i teori.",
         "fisker": "Om du kan oversætte en produktionsmodel til økonomi. Det er "
                   "dét, en tværfaglig case belønner.",
         "alt": "", "snyd": False, "fakta": False},
    ]},

    {"emne": "Fragtførerens ansvar", "fag": "Jura", "lag": [
        {"sp": "Hvilket regelsæt gælder for fragtførerens ansvar?",
         "arg": "Det følger TRANSPORTFORMEN: CMR for international landevej, "
                "Haag-Visby for sø under konnossement, Montreal for luft og "
                "COTIF/CIM for jernbane. Ikke købeloven og ikke CISG — de "
                "regulerer forholdet mellem køber og sælger.",
         "fisker": "Om du kobler regelsættet til transportformen og ikke til aftalen.",
         "alt": "", "snyd": False, "fakta": True},
        {"sp": "Godset er værd 500.000 kr. og vejer 300 kg. Får afsenderen sit tab "
               "dækket, hvis det ødelægges under vejtransport?",
         "arg": "Nej, langtfra. Ansvarsgrænsen er vægtbaseret — et beløb pr. kilo "
                "opgjort i SDR — så erstatningen regnes på 300 kg og ikke på "
                "værdien. Ved vejtransport er grænsen desuden den laveste af dem "
                "alle. Resultatet bliver typisk en brøkdel af tabet.",
         "fisker": "Om du regner på VÆGTEN og ikke på værdien. Det er hele pointen.",
         "alt": "", "snyd": False, "fakta": False},
        {"sp": "Så er det bare at kræve fuld erstatning, hvis fragtføreren har "
               "været uforsigtig?",
         "arg": "Ikke helt. Grænsen kan gennembrydes, men det kræver FORSÆT eller "
                "GROV uagtsomhed — almindelig uagtsomhed er ikke nok, og "
                "bevisbyrden er tung. Den praktiske vej er en anden: enten "
                "værdideklarere sendingen på forhånd mod tillæg, eller tegne en "
                "vareforsikring, som er væsentligt billigere.",
         "fisker": "Om du kender tærsklen (grov uagtsomhed, ikke almindelig) og kan "
                   "pege på den praktiske løsning.",
         "alt": "", "snyd": True, "fakta": False},
        {"sp": "Sendingen kom med skib og derefter på lastbil. Hvad så?",
         "arg": "Så afhænger det af, HVOR skaden skete. Konventionen følger "
                "transportformen på skadestidspunktet, og grænserne er vidt "
                "forskellige mellem sø og vej. Kan tidspunktet ikke fastslås, "
                "bliver det et bevisspørgsmål — og det er ofte dér, sagen reelt "
                "afgøres. Derfor er dokumentation ved hver omlastning ikke "
                "formalia, men bevissikring.",
         "fisker": "Om du ser det multimodale problem selv, og om du kobler det til "
                   "bevisbyrde frem for at lede efter én rigtig konvention.",
         "alt": "", "snyd": False, "fakta": False},
    ]},

    {"emne": "Projekt eller drift", "fag": "Projektstyring", "lag": [
        {"sp": "Hvad kendetegner et projekt?",
         "arg": "Fire ting: det er tidsbegrænset (har start og slutning), "
                "tværfagligt (trækker på flere funktioner), afgrænset (mål, "
                "rammer og ressourcer er defineret på forhånd) og en "
                "engangsopgave (ikke løst på samme måde før).",
         "fisker": "Om du kan alle fire uden at falde tilbage på 'noget stort og nyt'.",
         "alt": "", "snyd": False, "fakta": True},
        {"sp": "Et lager skal flyttes til en ny hal over fire weekender. "
               "Lagerchefen kalder det drift. Har han ret?",
         "arg": "Nej. Alle fire kendetegn er opfyldt: det har en slutdato, det "
                "trækker på lager, it og transport samtidig, rammen kan "
                "defineres, og flytningen er ikke gjort før. At det er "
                "'bare at flytte noget' gør det ikke til drift.",
         "fisker": "Om du bruger de fire som en TEST frem for som en beskrivelse.",
         "alt": "", "snyd": False, "fakta": False},
        {"sp": "Betyder det så, at alt nyt er et projekt?",
         "arg": "Nej. En tilbagevendende opgave, der bare har et nyt indhold — "
                "fx den årlige lageroptælling eller et nyt sortiment ind i en "
                "kendt proces — er drift, selvom detaljerne skifter. Kriteriet "
                "er, om opgaven er løst på SAMME MÅDE før, ikke om indholdet er "
                "nyt. De fleste fejl handler netop om tilbagevendende opgaver, "
                "der ligner projekter.",
         "fisker": "Om du kan trække grænsen den anden vej og ikke gør alt til projekt.",
         "alt": "", "snyd": True, "fakta": False},
        {"sp": "Hvad koster det konkret at behandle et projekt som drift?",
         "arg": "Der udpeges ingen projektleder, så ingen driver det. Der lægges "
                "ingen plan med milepæle, så afvigelser opdages sent. Der "
                "afsættes ingen ressourcer ud over den daglige bemanding, så "
                "arbejdet skal klares 'ved siden af' og kolliderer med driften "
                "første gang det spidser til. Og der tages ikke stilling til "
                "risici, så den første forhindring bliver en krise i stedet for "
                "en planlagt håndtering.",
         "fisker": "Om du kan sætte KONSEKVENSER på fejlklassifikationen — det er "
                   "dét, der viser, at du forstår hvorfor sondringen findes.",
         "alt": "", "snyd": False, "fakta": False},
    ]},

    {"emne": "Vandfald og agil", "fag": "Projektstyring", "lag": [
        {"sp": "Hvad er forskellen på vandfald og agil?",
         "arg": "Vandfald tager faserne i rækkefølge og lægger hele planen fast "
                "fra start; leveringen sker én gang til sidst. Agil deler "
                "arbejdet i korte forløb med et brugbart resultat i enden af "
                "hvert, og prioriteringen genbesøges mellem forløbene.",
         "fisker": "Om du kan begge og kan beskrive leveringsmønstret, ikke bare tempoet.",
         "alt": "", "snyd": False, "fakta": True},
        {"sp": "Hvornår holder vandfaldsmodellen?",
         "arg": "Når målet er kendt fra start, metoden er brugt før, og kravene "
                "ligger fast — fx i et udbud, hvor kravene er bundet juridisk. "
                "Og når leverancen først kan bruges, når den er hel: et halvt "
                "byggeri er ikke det halve af værdien.",
         "fisker": "Om du kan give BETINGELSER frem for at afvise vandfald som forældet.",
         "alt": "", "snyd": False, "fakta": False},
        {"sp": "Budgettet skal godkendes på forhånd. Så kan man vel ikke arbejde agilt?",
         "arg": "Jo. Agil betyder ikke uden styring — det betyder, at "
                "PRIORITERINGEN genbesøges, ikke at rammen er åben. Rammen og "
                "budgettet kan sagtens ligge fast, mens udførelsen er agil. Det "
                "er den blandede form, og den er den almindelige i logistik. Et "
                "fast budget udelukker kun, at scope udvides løbende.",
         "fisker": "Om du falder for præmissen, eller om du kan skille ramme fra indhold.",
         "alt": "", "snyd": True, "fakta": False},
        {"sp": "Hvad er så den reelle forudsætning for at lykkes med agil?",
         "arg": "At opdragsgiveren er tilgængelig LØBENDE og ikke kun ved "
                "milepæle. Agil flytter beslutninger fra én stor godkendelse til "
                "mange små, og de skal træffes af nogen med mandat. Kan "
                "opdragsgiveren kun mødes hvert kvartal, falder modellen fra "
                "hinanden — så får man ændringer uden beslutninger. Det er den "
                "forudsætning, man skal nævne SELV, før eksaminator gør det.",
         "fisker": "Om du kender modellens forudsætning og ikke kun dens fordele.",
         "alt": "", "snyd": False, "fakta": False},
    ]},

    {"emne": "Volumenvægt og fragtgrundlag", "fag": "Distribution", "lag": [
        {"sp": "Hvad er volumenvægt?",
         "arg": "Godsets rumfang omregnet til kilo med en faktor, der afhænger af "
                "transportformen. Fragtgrundlaget er det største af faktisk vægt "
                "og volumenvægt, fordi fragtføreren sælger både løfteevne og plads.",
         "fisker": "Om du kan definitionen og ved, at det er det STØRSTE der gælder.",
         "alt": "", "snyd": False, "fakta": True},
        {"sp": "Hvorfor er faktoren forskellig for fly og skib?",
         "arg": "Fordi deres knappe ressource er forskellig. Flyet er begrænset af "
                "løfteevne, så et kubikmeter må ikke 'veje' ret meget, før det "
                "bliver dyrt — faktoren er lav. Skibet er begrænset af plads, så "
                "et kubikmeter regnes langt tungere. Derfor straffer søfragten "
                "voluminøst gods hårdere end luftfragten gør relativt set.",
         "fisker": "Om du kan koble faktoren til transportformens flaskehals.",
         "alt": "", "snyd": False, "fakta": False},
        {"sp": "Kunden vil have raten ned. Er forhandling det rigtige greb?",
         "arg": "Ofte ikke det første. Betales der efter volumen, ligger den "
                "største besparelse i at ændre DENSITETEN: bedre pakning, "
                "mindre luft i emballagen, andet kollimål eller adskilt "
                "forsendelse kan flytte grundlaget fra volumen til vægt. Det er "
                "en engangsindsats med varig effekt, hvor en rateforhandling "
                "skal tages igen næste år.",
         "fisker": "Om du vender problemet om fra pris til produkt. Det er "
                   "rådgivningen, opgaven typisk efterspørger.",
         "alt": "", "snyd": True, "fakta": False},
    ]},
]


# ===========================================================================
# ARGUMENT-CASES — "Argumentér selv" (flere forsvarlige positioner)
# ===========================================================================
# Struktur som ARGUMENTER i siden: {fag, situation, spm, positioner, pointe}
ARGUMENTER_3SEM = [
    {
        "fag": "Distribution",
        "situation": "En producent af kundetilpassede komponenter har lange "
        "leveringstider og mange varianter i små serier. Ledelsen har hørt om "
        "Lean og vil sætte et forbedringsprogram i gang. Produktionen har høj "
        "maskinudnyttelse, og der er ofte hasteordrer, som skubbes forbi køen. "
        "Kunderne klager over uforudsigelige leveringstider frem for over prisen.",
        "spm": "Skal virksomheden gå Lean-vejen, QRM-vejen — eller noget tredje?",
        "positioner": [
            {"navn": "QRM",
             "arg": "Symptomerne peger direkte på QRM: mange varianter i små "
                    "serier, høj udnyttelse, hasteordrer der skubbes forbi, og "
                    "kunder der klager over TID frem for pris. Lean forudsætter "
                    "gentagelse nok til at udjævne, og det findes ikke her. QRM "
                    "angriber gennemløbstiden direkte, måler MCT, organiserer i "
                    "celler og planlægger bevidst med reservekapacitet — det er "
                    "netop hasteordrernes og køernes årsag, der angribes."},
            {"navn": "Lean-værktøjerne først",
             "arg": "Man behøver ikke vælge hele filosofien for at bruge "
                    "værktøjerne. SMED, 5S og værdistrømsanalyse virker uanset "
                    "volumen, og især kortere omstillingstid er forudsætningen "
                    "for overhovedet at kunne køre små serier økonomisk. Det er "
                    "billigere at komme i gang med og kræver ingen "
                    "omorganisering fra dag ét — celletankegangen kan komme "
                    "bagefter, når de basale ting sidder."},
            {"navn": "Start med udnyttelsesgraden",
             "arg": "Det billigste greb er hverken Lean eller QRM som program, "
                    "men en enkelt beslutning: sænk den planlagte udnyttelse. "
                    "Køerne — og dermed de uforudsigelige leveringstider — er en "
                    "direkte følge af, at der planlægges tæt på 100 %. En "
                    "bevidst reservekapacitet giver hurtig og målbar effekt "
                    "uden et forandringsprojekt, og den kan finansieres af de "
                    "hasteomkostninger, der forsvinder."},
        ],
        "pointe": "Alle tre kan forsvares, og de udelukker ikke hinanden. Det "
        "afgørende er, at valget begrundes i VARIABILITET og volumen — ikke i "
        "hvad der er mest udbredt. Det stærke svar peger på, at kundernes klage "
        "handler om tid, ikke pris, og at det derfor er gennemløbstiden og ikke "
        "spildet, der skal angribes først. Det viser samtidig, at man kender "
        "grænsen for Lean og ikke bruger værktøjet, fordi det er kendt.",
    },
    {
        "fag": "Distribution",
        "situation": "En virksomhed sender letvægtsgods med stor volumen til "
        "kunder i udlandet. Fragtregningen er steget markant, selvom mængden i "
        "kilo er uændret. Indkøb vil genforhandle raten med transportøren. "
        "Produktionen mener, emballagen kan gøres mindre, men det kræver en "
        "investering i nyt pakkeudstyr og en ændring af pakkeprocessen.",
        "spm": "Hvor skal virksomheden sætte ind for at få fragtomkostningen ned?",
        "positioner": [
            {"navn": "Ændr emballagen",
             "arg": "Godset betales efter volumen, ikke vægt — derfor er "
                    "densiteten den egentlige omkostningsdriver. En "
                    "emballageændring, der flytter fragtgrundlaget fra volumen "
                    "mod vægt, giver en varig besparelse på hver eneste sending "
                    "og virker uanset, hvilken transportør man bruger. "
                    "Investeringen i pakkeudstyr er engangs; besparelsen er "
                    "løbende."},
            {"navn": "Genforhandl raten",
             "arg": "Rateforhandling kræver ingen investering, kan gennemføres "
                    "på uger og giver effekt med det samme. Virksomheden har "
                    "desuden et stærkt kort: uændret volumen i kilo er et "
                    "argument over for transportøren, og markedet for "
                    "letvægtsgods er konkurrencepræget. En emballageændring "
                    "risikerer at gå ud over produktbeskyttelsen og dermed "
                    "skabe skader, der koster mere end fragten."},
            {"navn": "Skift transportform eller konsolidér",
             "arg": "Omregningsfaktoren afhænger af transportformen, så samme "
                    "kolli kan have et helt andet fragtgrundlag et andet sted. "
                    "Dertil kommer konsolidering: færre og større sendinger "
                    "giver bedre rater pr. enhed. Det kræver hverken "
                    "investering eller forhandling — kun at man planlægger "
                    "afsendelserne anderledes."},
        ],
        "pointe": "Casen tester, om man kan se forbi prisen til MEKANISMEN. "
        "Betales der efter volumen, er densiteten den egentlige driver, og så er "
        "emballagen et strukturelt greb, mens raten er et taktisk. Det stærke "
        "svar rangerer indsatserne efter, hvor varig effekten er, holder "
        "investeringen op mod den løbende besparelse, og nævner risikoen ved at "
        "reducere emballagen — beskyttelsen skal stadig holde, ellers flytter "
        "man bare omkostningen til skader.",
    },
    {
        "fag": "Projektstyring",
        "situation": "Et nyt lagerstyringssystem skal indføres over seks "
        "måneder. Opdragsgiveren er økonomidirektøren, som har fået budgettet "
        "godkendt i bestyrelsen og ønsker en fast plan med milepæle. "
        "Lagermedarbejderne, der skal bruge systemet dagligt, har ikke været "
        "inddraget. It-leverandøren anbefaler korte forløb med løbende "
        "justering, fordi arbejdsgangene først kan afklares undervejs.",
        "spm": "Hvilken projektform bør vælges, og hvordan håndteres modsætningen?",
        "positioner": [
            {"navn": "Blandet form",
             "arg": "Rammen og budgettet ligger fast, som opdragsgiveren "
                    "kræver, mens udførelsen køres i korte forløb, som "
                    "leverandøren anbefaler. Det er den almindelige form i "
                    "logistik, og den løser modsætningen frem for at vælge side: "
                    "økonomidirektøren får sin milepælsrapportering, og "
                    "arbejdsgangene kan afklares undervejs uden at sprænge "
                    "rammen."},
            {"navn": "Traditionel vandfald",
             "arg": "Budgettet er godkendt i bestyrelsen, og opdragsgiveren har "
                    "bundet sig til en plan. Et lagerstyringssystem er desuden "
                    "en velkendt opgave, hvor metoden er brugt før — kendt hvad "
                    "og kendt hvordan. Så er der ikke meget at lære undervejs, "
                    "og den agile overhead med løbende prioritering koster mere, "
                    "end den giver. Uafklarede arbejdsgange løses med en "
                    "grundig analysefase, ikke med en anden projektform."},
            {"navn": "Agil med brugerne inde fra start",
             "arg": "Den reelle risiko i casen er ikke teknikken, men at "
                    "lagermedarbejderne — referencegruppen — ikke er inddraget. "
                    "Det er dem, der afgør, om systemet kan bruges. En agil "
                    "tilgang med brugerne med i hvert forløb er den eneste, der "
                    "opdager problemerne, mens de er billige at rette. Budgettet "
                    "kan stadig være fast; det er scope, der prioriteres."},
        ],
        "pointe": "Casen rummer den klassiske spænding mellem en opdragsgiver, "
        "der vil have forudsigelighed, og en opgave, hvor vejen er ukendt. Det "
        "stærke svar bruger kendt/ukendt-matricen som begrundelse og peger på, at "
        "det er REFERENCEGRUPPEN, der er den oversete risiko — de skal bruge "
        "resultatet, men er ikke spurgt. Uanset hvilken form man vælger, skal "
        "svaret nævne, at et fast budget ikke i sig selv udelukker agil "
        "udførelse; det udelukker kun løbende udvidelse af scope.",
    },
]
