"""Bred forsvars-spørgsmålsbank (alle modeller/begreber/VCA-stationer).

Forfattet + censur-verificeret via workflow (68 spørgsmål, 7 fagområder).
type="argument" = bløde fag (flere forsvarlige svar, har "alt");
type="rigtigt" = der ER et korrekt svar (alt="").
"""

KONCEPT = [
 {
  "fag": "Organisation",
  "emne": "Porters generiske strategier",
  "sp": "Hvilken generisk strategi har I valgt for virksomheden, og hvorfor kan man ikke bare gå efter at være både billigst og mest unik?",
  "type": "rigtigt",
  "svar": "Porter opstiller tre generiske strategier: omkostningsleder (være billigst), differentiering (være unik/bedst) og fokus (satse på en smal niche — som så kan køres enten med lave omkostninger eller med differentiering inden for nichen). Pointen er, at man skal vælge én klar retning. Grunden til, at man ikke kan være både billigst OG mest unik på samme tid, er det Porter kalder 'stuck in the middle': differentiering koster penge (bedre kvalitet, service, brand), og de penge gør, at man ikke samtidig kan have de laveste omkostninger. Omvendt kræver lavpris, at man skærer ind til benet, og så bliver man ikke den mest unikke. Sidder man fast i midten, har man hverken den ene eller den anden fordel og taber til konkurrenter, der har valgt klart. Derfor er svaret: man vælger én strategi, fordi de to yderpunkter trækker virksomhedens ressourcer i hver sin retning.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at du kender de tre strategier OG kan forklare 'stuck in the middle' korrekt — altså HVORFOR de to ikke kan kombineres (omkostninger trækker mod lavpris, investeringer trækker mod differentiering).",
  "soeg": [
   "porter",
   "generiske strategier",
   "omkostningsleder",
   "differentiering",
   "stuck in the middle"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Ansoffs vækstmatrix",
  "sp": "I Ansoffs vækstmatrix — hvilken vækstretning har virksomheden valgt, og hvilken af felterne er den farligste at gå efter?",
  "type": "argument",
  "svar": "Ansoffs matrix har fire felter ud fra om man bruger nuværende/nye produkter og nuværende/nye markeder: markedspenetrering (kendt produkt, kendt marked — sælg mere af det vi har), produktudvikling (nyt produkt, kendt marked), markedsudvikling (kendt produkt, nyt marked) og diversifikation (nyt produkt, nyt marked). Jeg vil placere virksomheden i [valgt felt], fordi de bygger videre på noget de allerede mestrer, hvilket holder risikoen nede. Det farligste felt er diversifikation, fordi man dér både skal lære et nyt produkt og et nyt marked at kende på én gang — to ukendte ting samtidig, og dermed dobbelt risiko.",
  "alt": "Man kan forsvare en mere offensiv placering, fx markeds- eller produktudvikling, hvis virksomheden har stærke ressourcer og et modent hjemmemarked, der ikke kan vokse mere — så er det nødvendigt at tage større risiko for overhovedet at vokse. Samme virksomhed kan altså placeres forskelligt alt efter, om man vægter sikkerhed eller vækstpotentiale.",
  "fisker": "Eksaminator er ude efter, at du kan begrunde din placering med risiko/ressourcer — ikke et facit. Vis at du ved diversifikation er den farligste (to ukendte ad gangen), og brug det aktivt i argumentet.",
  "soeg": [
   "ansoff",
   "vækstmatrix",
   "diversifikation",
   "markedspenetrering",
   "risiko"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Generisk SC-strategi (lean vs agil)",
  "sp": "Skal virksomhedens forsyningskæde være lean/efficient eller responsiv/agil — og hvordan hænger det sammen med jeres konkurrencestrategi?",
  "type": "argument",
  "svar": "En lean/efficient kæde er bygget til at presse omkostninger ned: stabil produktion, høj udnyttelse, få spild — den passer til forudsigelig efterspørgsel og standardvarer. En responsiv/agil kæde er bygget til hurtigt at kunne omstille sig og reagere på svingende efterspørgsel — den koster mere, men leverer fleksibilitet og hurtige leveringer. Det vigtige er harmonien med konkurrencestrategien: omkostningsleder hører sammen med en lean kæde (begge handler om lav pris), mens differentiering hører sammen med en responsiv/agil kæde (man betaler for at kunne levere det unikke hurtigt og fleksibelt). Jeg vælger [lean/agil], fordi det matcher vores [omkostning/differentiering]-strategi.",
  "alt": "Mange virksomheder kører en hybrid: lean på de stabile basisvarer og agil på de uforudsigelige eller sæsonbetonede varer (afkoblingspunkt/postponement). Så samme virksomhed kan forsvares som 'både og', hvis produktporteføljen er blandet — det er ikke nødvendigvis enten-eller.",
  "fisker": "Eksaminator vil se, at du kobler kæden til strategien korrekt (omkostningsleder→lean, differentiering→agil) og kan argumentere ud fra efterspørgslens forudsigelighed — ikke at der findes ét rigtigt valg.",
  "soeg": [
   "lean",
   "agil",
   "responsiv",
   "forsyningskæde",
   "efterspørgsel"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Organisationsstruktur (funktion vs objekt)",
  "sp": "Er virksomheden bedst tjent med en funktionsopdelt eller en objektopdelt (fx produkt/marked) struktur?",
  "type": "argument",
  "svar": "Funktionsopdeling samler folk efter fag — indkøb for sig, salg for sig, produktion for sig. Fordelen er stordrift og dyb faglighed, fordi specialisterne sidder sammen. Ulempen er silotænkning: hver afdeling passer sit eget og taber helheden/kunden af syne. Objektopdeling samler i stedet folk omkring et produkt, en kunde eller et marked — så alle fag arbejder mod samme mål, hvilket giver hurtig koordinering og kundefokus, men koster stordriften (samme funktion findes flere steder). Jeg vælger [funktion/objekt], fordi virksomheden er [stabil med få produkter / kompleks med flere markeder].",
  "alt": "Samme virksomhed kan forsvares modsat: en funktionsstruktur kan også begrundes selv ved flere produkter, hvis stordrift og faglig specialisering er det vigtigste konkurrenceparameter (fx ren lavpris). Valget afhænger af, om man vægter effektivitet (funktion) eller koordinering/kundenærhed (objekt).",
  "fisker": "Eksaminator er ude efter, at du kender afvejningen: funktion giver stordrift men silotænkning, objekt giver koordinering men dyrere drift. Argumentet tæller, ikke facit.",
  "soeg": [
   "funktionsopdeling",
   "objektopdeling",
   "stordrift",
   "silotænkning",
   "struktur"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Linje/stab, kontrolspænd, flad vs høj",
  "sp": "Hvad betyder kontrolspænd, og hvordan hænger det sammen med, om en organisation bliver flad eller høj?",
  "type": "rigtigt",
  "svar": "Kontrolspænd er, hvor mange medarbejdere én leder har direkte under sig. Linje er den almindelige kommandovej (chef→medarbejder med beslutningsret), mens stab er støttefunktioner (fx HR, jurist), der rådgiver linjen men ikke har kommando. Sammenhængen med flad/høj: hvis hver leder har et bredt kontrolspænd (mange under sig), skal der bruges færre ledere, og organisationen bliver flad med få niveauer — kort vej fra top til bund, hurtige beslutninger, men hver leder kan ikke følge tæt med. Hvis kontrolspændet er smalt (få under hver leder), skal der bruges flere ledere oven på hinanden, og organisationen bliver høj med mange niveauer — tæt kontrol, men lang og langsom kommandovej. Bredt spænd giver altså flad struktur, smalt spænd giver høj struktur.",
  "alt": "",
  "fisker": "Eksaminator vil have den korrekte mekanik: bredt kontrolspænd → flad organisation, smalt → høj. Og at du kan skille linje (kommando) fra stab (rådgivning uden kommando).",
  "soeg": [
   "kontrolspænd",
   "flad",
   "høj",
   "linje",
   "stab"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Organisk vs mekanistisk",
  "sp": "Er virksomheden mest organisk eller mest mekanistisk organiseret — og passer det til markedet, den opererer på?",
  "type": "argument",
  "svar": "En mekanistisk organisation er stram og regelstyret: faste procedurer, klar hierarkisk kommandovej, snæver specialisering — den er effektiv, når omverdenen er stabil og forudsigelig. En organisk organisation er løs og fleksibel: få regler, meget samarbejde på tværs, beslutninger tæt på opgaven — den fungerer, når markedet er foranderligt og man hurtigt skal tilpasse sig. Hovedreglen er: organisk passer til foranderlige markeder, mekanistisk til stabile. Jeg vurderer virksomheden som [organisk/mekanistisk], fordi den opererer på et [foranderligt/stabilt] marked, og det giver harmoni mellem struktur og omverden.",
  "alt": "Samme virksomhed kan godt være blandet: en stabil produktionskerne kan være mekanistisk for at sikre effektivitet, mens udviklings- eller salgsdelen er organisk for at fange markedets bevægelser. Så placeringen kan forsvares som 'organisk i nogle dele, mekanistisk i andre' afhængigt af, hvilken del man ser på.",
  "fisker": "Eksaminator vil høre koblingen mellem struktur og omgivelser: organisk↔foranderligt marked, mekanistisk↔stabilt marked. Det er argumentet om match, der tæller.",
  "soeg": [
   "organisk",
   "mekanistisk",
   "foranderligt marked",
   "stabilt",
   "fleksibilitet"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "McGregor teori X/Y",
  "sp": "Hvad er forskellen på McGregors teori X og teori Y, og hvilket menneskesyn ligger bag hver?",
  "type": "rigtigt",
  "svar": "McGregor beskriver to modsatte menneskesyn hos ledere. Teori X antager, at mennesker grundlæggende er dovne, undgår ansvar og kun arbejder, hvis de bliver kontrolleret, presset og styret med pisk og gulerod — derfor leder en X-leder med tæt kontrol og detailstyring. Teori Y antager det modsatte: at mennesker gerne vil yde, kan tage ansvar og motiveres af selve arbejdet, hvis rammerne er rigtige — derfor leder en Y-leder med tillid, frihed og ansvar. Det er altså lederens grundsyn på medarbejderen, der afgør ledelsesstilen: X = negativt menneskesyn og kontrol, Y = positivt menneskesyn og uddelegering.",
  "alt": "",
  "fisker": "Eksaminator vil have de to menneskesyn klart skåret op: X = doven, skal kontrolleres; Y = ansvarlig, vil gerne yde. Og pointen at lederens syn styrer ledelsesstilen.",
  "soeg": [
   "mcgregor",
   "teori x",
   "teori y",
   "menneskesyn",
   "motivation"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Scheins menneskesyn",
  "sp": "Schein opdeler menneskesynet i flere typer — redegør for dem og forklar, hvad de betyder for, hvordan man bør motivere medarbejderen.",
  "type": "rigtigt",
  "svar": "Schein opstiller fire menneskesyn, der hver kræver sin motivation. 1) Det rationelt-økonomiske menneske: motiveres af penge og egen vinding — styres bedst med løn og bonus. 2) Det sociale menneske: motiveres af fællesskab, relationer og at høre til — styres bedst gennem et godt arbejdsmiljø og kollegaskab. 3) Det selvrealiserende menneske: motiveres af at udvikle sig, præstere og udnytte sine evner — styres bedst med udfordrende, meningsfuldt arbejde og ansvar. 4) Det komplekse menneske: skifter mellem de andre alt efter situation, alder og opgave — der findes ikke én fast motivationsformel, lederen må aflæse den enkelte. Pointen er, at lederen skal tilpasse motivationen til hvilket menneskesyn medarbejderen handler ud fra; det komplekse menneske er Scheins mest nuancerede og realistiske bud.",
  "alt": "",
  "fisker": "Eksaminator vil have alle fire typer nævnt med den rette motivation til hver, og pointen at det komplekse menneske er det mest nuancerede — at motivation ikke er én størrelse.",
  "soeg": [
   "schein",
   "menneskesyn",
   "rationelt økonomiske",
   "sociale",
   "komplekse menneske"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Ledergitteret (Blake og Mouton)",
  "sp": "Placér jeres leder i Blake og Moutons ledergitter, og forklar hvorfor 9.9 regnes for idealet.",
  "type": "argument",
  "svar": "Ledergitteret måler lederen på to akser fra 1 til 9: omsorg for produktionen/opgaven (vandret) og omsorg for menneskene/medarbejderne (lodret). Det giver kendte typer som 1.1 (laissez-faire, ligeglad med begge), 9.1 (autoritær, kun opgave), 1.9 (country club, kun mennesker) og 5.5 (kompromis, middel på begge). 9.9 — teamledelse — er idealet, fordi lederen her har maksimal omsorg for BÅDE opgaven og menneskene på samme tid: engagerede medarbejdere, der i fællesskab leverer høj præstation. Jeg placerer vores leder på [fx 5.5], fordi [begrundelse i adfærd], men idealet at stræbe mod er 9.9.",
  "alt": "Man kan forsvare, at den 'rigtige' placering afhænger af situationen — i en krise eller ved stærkt tidspres kan en mere opgavestyret (9.1) stil være nødvendig, mens 9.9 forudsætter tid og modne medarbejdere. Så samme leder kan vurderes forskelligt alt efter, om man bedømmer den ideelle eller den situationsbestemte stil.",
  "fisker": "Eksaminator vil høre de to akser (opgave vs mennesker), at du kan placere lederen konkret, og at du ved 9.9/team er idealet fordi det maksimerer begge hensyn samtidig.",
  "soeg": [
   "ledergitteret",
   "blake mouton",
   "9.9",
   "teamledelse",
   "ledelsesstil"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Adizes PAEI-lederroller",
  "sp": "Hvad står PAEI for i Adizes' model, og hvorfor kan én leder sjældent dække alle fire roller?",
  "type": "rigtigt",
  "svar": "Adizes siger, at god ledelse kræver fire roller, forkortet PAEI. P = Producer (producenten): får tingene gjort og skaber resultater her og nu. A = Administrator: skaber orden, systemer og styring, så det kører efterretteligt. E = Entrepreneur (entreprenøren): tænker nyt, ser muligheder og driver forandring fremad. I = Integrator: binder folk sammen, skaber samarbejde og fælles ånd. Pointen er, at rollerne delvist modarbejder hinanden — fx vil Administratoren have orden og regler, mens Entrepreneuren vil bryde reglerne og forandre. Derfor er den perfekte leder, der mestrer alle fire, ifølge Adizes nærmest umulig ('the perfect manager findes ikke'). Løsningen er et team, hvor flere personer tilsammen dækker P, A, E og I.",
  "alt": "",
  "fisker": "Eksaminator vil have alle fire roller forklaret og pointen at de trækker i hver sin retning, så ingen enkelt leder kan rumme dem alle — derfor team. Brug ikke 'det afhænger' her; det er en faktamodel.",
  "soeg": [
   "adizes",
   "paei",
   "lederroller",
   "producer administrator",
   "integrator"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Hofstedes kulturdimensioner",
  "sp": "Vælg én af Hofstedes kulturdimensioner og forklar, hvilken betydning den har for, hvordan man leder eller samarbejder på tværs af lande.",
  "type": "rigtigt",
  "svar": "Hofstede måler nationale kulturer på dimensioner — fx magtdistance, individualisme/kollektivisme, maskulinitet/femininitet og usikkerhedsundvigelse. Tag magtdistance som eksempel: den måler, hvor stor afstand mellem chef og medarbejder en kultur accepterer som naturlig. I lande med HØJ magtdistance (fx mange asiatiske og latinske lande) forventer medarbejderne en tydelig, bestemmende chef, og man stiller ikke spørgsmål opad. I lande med LAV magtdistance (Danmark og Norden) er hierarkiet fladt, chefen er nærmest en kollega, og medarbejdere forventer at blive hørt og inddraget. Betydningen er, at en dansk ledelsesstil med uddelegering og medbestemmelse kan virke svag eller forvirrende i en høj-magtdistance-kultur, og omvendt kan en autoritær stil støde danske medarbejdere. Man må altså tilpasse ledelse og samarbejde til kulturen for at undgå misforståelser.",
  "alt": "",
  "fisker": "Eksaminator vil have, at du kan navngive dimensionerne og forklare ÉN konkret med dansk eksempel — og pointen at ledelse må tilpasses kulturen. Det er en faktamodel, så undgå 'det afhænger'.",
  "soeg": [
   "hofstede",
   "kulturdimensioner",
   "magtdistance",
   "individualisme",
   "national kultur"
  ]
 },
 {
  "fag": "Organisation",
  "emne": "Harmoni mellem strategi, struktur og forsyningskæde",
  "sp": "Hænger virksomhedens strategi, organisationsstruktur og forsyningskæde sammen — eller er der et sted, hvor de trækker i hver sin retning?",
  "type": "argument",
  "svar": "De tre skal spille sammen for at virksomheden performer. En rød tråd kunne være: omkostningsleder-strategi → mekanistisk, funktionsopdelt struktur (stordrift, effektivitet) → lean forsyningskæde (lavt spild, stabil produktion). Eller den modsatte tråd: differentieringsstrategi → organisk, objektopdelt struktur (fleksibilitet, kundefokus) → agil/responsiv kæde (hurtig omstilling). Min vurdering er, at virksomheden har harmoni/disharmoni, fordi [fx strategien siger differentiering, men kæden er kørt lean for at spare — det er en konflikt, der gør, at man ikke kan levere det unikke hurtigt nok]. Pointen er at vise, om de tre elementer peger samme vej.",
  "alt": "Man kan forsvare en bevidst 'uharmonisk' opsætning som en overgangsfase: virksomheden er måske midt i et strategiskift, hvor strukturen og kæden endnu ikke har fulgt med, og det kan være en accepteret prioritering frem for en fejl. Så det, der ligner disharmoni, kan også forsvares som en virksomhed undervejs i en planlagt omstilling.",
  "fisker": "Eksaminator er ude efter, at du kan binde de tre niveauer sammen i én konsistent kæde (strategi→struktur→SC) og selv pege på, hvor harmonien holder eller brister. Det er evnen til at se helheden, der bedømmes.",
  "soeg": [
   "harmoni",
   "strategi struktur",
   "forsyningskæde",
   "fit",
   "sammenhæng"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Kraljic — de 4 typer",
  "sp": "Du har placeret en vare i Kraljics flaskehals-felt. Forklar hvorfor, og hvilken indkøbsstrategi du anbefaler for den type.",
  "type": "argument",
  "svar": "Flaskehalsvarer kendetegnes ved LAV indkøbsværdi (lille beløb i kroner) men HØJ forsyningsrisiko — fx fordi der kun er få leverandører, lange leveringstider eller stor afhængighed af én kilde. Pointen er, at varen er billig, men hvis den udebliver, kan den stoppe hele produktionen. Derfor handler strategien IKKE om at presse prisen, men om at SIKRE FORSYNINGEN: byg sikkerhedslagre, lav rammeaftaler/kontrakter der garanterer levering, find om muligt alternative leverandører eller substitutter, og bind leverandøren til dig. De fire felter er: ikke-kritiske (lav værdi/lav risiko → forenkl og automatisér indkøb), løftestang (høj værdi/lav risiko → udnyt konkurrence og pres pris), flaskehals (lav værdi/høj risiko → sikr forsyning) og strategisk (høj værdi/høj risiko → partnerskab).",
  "alt": "Den samme vare kan placeres i strategisk-feltet, hvis man vurderer forsyningsrisikoen så høj OG værdien vigtigere for kerneforretningen end først antaget — så skifter strategien til tæt partnerskab i stedet for ren forsyningssikring. Placeringen afhænger af hvordan man scorer akserne.",
  "fisker": "Eksaminator vil høre, at du forstår de TO akser (værdi vs. forsyningsrisiko) og kan koble en placering til en konkret strategi. Det vigtige er argumentet for placeringen og at flaskehals = forsyningssikkerhed FREM FOR pris — ikke et bestemt facit.",
  "soeg": [
   "kraljic",
   "flaskehals",
   "forsyningsrisiko",
   "indkøbsstrategi",
   "matrix"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Bensaou-matrix",
  "sp": "I Bensaou-matrixen taler man om specifikke investeringer. Hvad afgør hvilken af de fire relationer der opstår, og giv et eksempel.",
  "type": "rigtigt",
  "svar": "Bensaou-matrixen inddeler køber-leverandør-relationer efter HVEM der har lavet specifikke investeringer — altså investeringer der kun har værdi i lige netop denne relation (specielt værktøj, tilpassede IT-systemer, dedikeret personale, fælles udvikling). De to akser er køberens specifikke investeringer (lav/høj) og leverandørens specifikke investeringer (lav/høj), hvilket giver fire felter: 1) Market exchange — begge investerer lidt; standardvarer, let at skifte, armslængde-relation. 2) Captive buyer — KØBEREN har investeret meget, leverandøren lidt; køberen er låst og afhængig (sårbar position). 3) Captive supplier — LEVERANDØREN har investeret meget, køberen lidt; leverandøren er låst og afhængig af køberen. 4) Strategic partnership — BEGGE har investeret meget; gensidig afhængighed og tæt samarbejde. Pointen er, at det er fordelingen af de specifikke (relationsbundne) investeringer, der bestemmer magtbalancen og dermed relationstypen.",
  "alt": "",
  "fisker": "Eksaminator tjekker, at du ved at det er specifikke investeringer (relationsbundne, ikke generelle) og navnlig FORDELINGEN mellem køber og leverandør, der definerer felterne — og at du kan navngive de fire og hvem der er låst.",
  "soeg": [
   "bensaou",
   "specifikke investeringer",
   "captive buyer",
   "partnerskab",
   "relation"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Sourcing-strategier",
  "sp": "Virksomheden overvejer single sourcing kontra multiple sourcing for en vigtig komponent. Hvad anbefaler du, og hvorfor?",
  "type": "argument",
  "svar": "Single sourcing (én leverandør) giver stordriftsfordele, lavere stykpris ved store mængder, tættere relation, lettere koordinering og bedre mulighed for fælles udvikling — men gør dig SÅRBAR: hvis leverandøren svigter (konkurs, strejke, kvalitetsbrist), står du uden vare, og din forhandlingsmagt svækkes. Multiple sourcing (flere leverandører) giver forsyningssikkerhed, konkurrence på pris og et fald-back hvis én svigter — men er typisk DYRERE pr. enhed, sværere at styre og giver løsere relationer. Dual sourcing (to leverandører) er et kompromis: nok sikkerhed til ikke at stå alene, men stadig volumen til hver til at få gode priser. Cross sourcing betyder, at man bruger forskellige leverandører til forskellige varer/områder og spiller dem op mod hinanden over tid. Anbefalingen afhænger af, hvor kritisk komponenten er: er forsyningsrisikoen høj, vægter jeg sikkerhed (multiple/dual); er den lav og volumen høj, vægter jeg pris og relation (single).",
  "alt": "Den modsatte anbefaling kan forsvares lige så godt: vælger man single sourcing, kan man argumentere for at den tætte relation og lavere pris opvejer sårbarheden, hvis man afdækker risikoen på anden vis (lager, kontraktklausuler). Vælger man multiple, kan man forsvare at sikkerheden er pengene værd. Det er en afvejning af pris mod risiko.",
  "fisker": "Eksaminator vil se, at du kender fordele OG ulemper ved hver strategi og kan afveje pris mod forsyningssikkerhed i forhold til varens kritikalitet — ikke at du vælger 'rigtigt', men at du argumenterer.",
  "soeg": [
   "single sourcing",
   "multiple sourcing",
   "dual sourcing",
   "cross sourcing",
   "forsyningssikkerhed"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Exit vs. voice",
  "sp": "Forklar forskellen på exit og voice som reaktion på en leverandør, der underpræsterer. Hvornår vil du bruge hvad?",
  "type": "rigtigt",
  "svar": "Exit og voice er to måder at reagere på, når en leverandør ikke leverer godt nok. EXIT betyder, at du forlader relationen — du skifter til en anden leverandør og lader markedet/konkurrencen løse problemet. Det passer til markedsbaserede, løse relationer med standardvarer og mange alternativer, hvor det er let og billigt at skifte. VOICE betyder, at du BLIVER i relationen og taler problemet op — du giver feedback, stiller krav, samarbejder om forbedring og forsøger at rette op. Det passer til tætte, langvarige relationer (fx strategiske partnerskaber), hvor du har investeret i forholdet, hvor det er dyrt eller umuligt at skifte, og hvor leverandøren er svær at erstatte. Tommelfingerregel: jo tættere og mere bunden relationen er (få alternativer, specifikke investeringer), jo mere taler det for voice; jo mere markedsagtig og standardiseret, jo mere giver exit mening.",
  "alt": "",
  "fisker": "Eksaminator vil have den klare definition: exit = skift leverandør (markedsløsning), voice = bliv og forbedr (relationsløsning) — og at du kobler valget til hvor tæt/bundet relationen er.",
  "soeg": [
   "exit",
   "voice",
   "leverandørrelation",
   "skift",
   "forbedring"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "TCE vs. netværksperspektiv",
  "sp": "Sammenlign transaktionsomkostningsperspektivet (TCE) og netværksperspektivet på leverandørrelationer. Hvilket syn lægger du til grund i casen?",
  "type": "argument",
  "svar": "Transaktionsomkostningsperspektivet (TCE) ser hver handel som en transaktion, der koster noget at gennemføre ud over selve prisen: at finde leverandører, forhandle, skrive kontrakter, kontrollere og håndhæve. Synet er ret køligt og kontrol-orienteret — man vælger den styreform (marked, kontrakt eller egen produktion) der minimerer de samlede transaktionsomkostninger, og man er på vagt over for at modparten udnytter en (opportunisme), især når der er specifikke investeringer. Netværksperspektivet ser i stedet relationer som langvarige, gensidige og værdiskabende: leverandøren er en partner i et netværk, hvor tillid, fælles udvikling, læring og relationer over tid skaber værdi — ikke kun lavest mulig transaktionsomkostning her og nu. TCE forklarer godt, hvornår man bør lave noget selv vs. købe det, og hvorfor kontrakter findes; netværkssynet forklarer godt, hvorfor virksomheder bliver i tætte samarbejder og investerer i relationer, selv når det ikke er billigst på kort sigt. I casen vælger jeg perspektiv efter relationen: standard/armslængde-køb analyseres bedst med TCE, strategiske partnerskaber bedst med netværkssynet.",
  "alt": "Man kan forsvare at lægge ÉT perspektiv konsekvent til grund: en TCE-tilgang på hele indkøbet (alt vurderes på omkostninger og kontrol) eller en ren netværkstilgang (alt vurderes på relationsværdi). Begge er gyldige analyserammer — valget afhænger af, om casen handler mest om kontrol/pris eller om langsigtet samarbejde.",
  "fisker": "Eksaminator vil høre, at du kan stille de to syn op mod hinanden — kontrol/omkostninger/opportunisme (TCE) vs. tillid/relation/værdiskabelse over tid (netværk) — og begrunde dit valg. Ikke et facit, men en bevidst ramme.",
  "soeg": [
   "transaktionsomkostninger",
   "tce",
   "netværksperspektiv",
   "opportunisme",
   "relationsværdi"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Ordrevinder vs. ordrekvalificerende",
  "sp": "Hvad er forskellen på et ordrevindende og et ordrekvalificerende kriterium, og hvorfor er skellet vigtigt i indkøb og leverandørvalg?",
  "type": "rigtigt",
  "svar": "Et ORDREKVALIFICERENDE kriterium er et minimumskrav, en leverandør (eller et produkt) SKAL opfylde bare for at komme i betragtning — fx en vis kvalitet, en godkendelse, overholdelse af leveringstid eller en grundpris på markedsniveau. Opfylder man det ikke, er man ude med det samme; men at opfylde det giver IKKE i sig selv ordren — det gør dig bare 'kvalificeret'. Et ORDREVINDENDE kriterium er det, der reelt afgør, hvem der vælges blandt de kvalificerede — den faktor hvor du skiller dig ud og vinder handlen, fx den laveste pris, den korteste leveringstid, det bedste serviceniveau eller en unik teknisk egenskab. Skellet er vigtigt, fordi det fortæller, hvor man skal lægge sin indsats: man skal sikre at man passerer alle de kvalificerende krav (ellers er man ude), og derefter konkurrere på det, der faktisk vinder ordren. Et kriterium kan desuden skifte status over tid: noget der før vandt ordrer (fx kort leveringstid), kan blive et minimumskrav alle lever op til.",
  "alt": "",
  "fisker": "Eksaminator vil have den præcise sondring: kvalificerende = adgangsbillet/minimumskrav, vindende = det der afgør valget blandt de kvalificerede — plus pointen om at status kan ændre sig over tid.",
  "soeg": [
   "ordrevinder",
   "ordrekvalificerende",
   "minimumskrav",
   "konkurrenceparameter",
   "leverandørvalg"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Leverandørevaluering (vægtet score)",
  "sp": "Du skal vælge mellem to leverandører med en vægtet scoremodel. Forklar metoden, og hvad du skal være opmærksom på, når du fastsætter vægtene.",
  "type": "argument",
  "svar": "En vægtet scoremodel bruges til at sammenligne leverandører på flere kriterier samtidig på en struktureret måde. Metoden: 1) Vælg de relevante kriterier (fx pris, kvalitet, leveringssikkerhed, service, miljø). 2) Giv hvert kriterium en VÆGT efter hvor vigtigt det er — vægtene summer typisk til 100% (eller 1). 3) Giv hver leverandør en SCORE på hvert kriterium, fx 1-5 eller 1-10. 4) Gang score med vægt for hvert kriterium og læg sammen — leverandøren med den højeste vægtede totalscore vælges. Styrken er, at den gør et ellers diffust valg gennemsigtigt og sammenligneligt og tvinger dig til at prioritere. Det du SKAL være opmærksom på: vægtene er et VALG, ikke en naturlov — flytter du vægt fra pris til kvalitet, kan vinderen skifte, så modellen er kun så god som de vægte og kriterier du har valgt. Vær desuden konsekvent i scoringen, undgå at kriterier overlapper (dobbelttælling), og husk at tal kan give falsk præcision: en lille forskel i totalscore er ikke nødvendigvis afgørende.",
  "alt": "Man kan forsvare et andet udfald ved at vægte anderledes: lægger man mest vægt på pris, vinder den billige leverandør; lægger man mest vægt på leveringssikkerhed/kvalitet, kan den dyrere vinde. Det 'rigtige' valg afhænger derfor af, hvad virksomheden strategisk prioriterer.",
  "fisker": "Eksaminator vil se, at du kan beskrive metoden (vægt × score, summeret) OG forholde dig kritisk til den — at resultatet styres af vægtene, så det er argumentet bag vægtningen, ikke selve totalen, der er pointen.",
  "soeg": [
   "leverandørevaluering",
   "vægtet score",
   "kriterier",
   "vægtning",
   "scoremodel"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Make-vs-buy",
  "sp": "Virksomheden skal beslutte, om en komponent skal produceres selv (make) eller købes eksternt (buy). Hvordan griber du beslutningen an?",
  "type": "argument",
  "svar": "Make-vs-buy handler om afvejningen mellem STRATEGISK KONTROL og PRIS. BUY (køb eksternt) er ofte billigere på kort sigt, fordi en specialiseret leverandør har stordrift og ekspertise; det giver fleksibilitet og frigør kapital og fokus til kerneforretningen — men du afgiver kontrol, bliver afhængig af leverandøren og risikerer at miste vigtig viden og forsyningssikkerhed. MAKE (lav det selv) koster typisk mere og binder kapital og kapacitet, men giver kontrol over kvalitet, leveringstid og fortrolig viden, og beskytter kernekompetencer du ikke vil dele eller blive afhængig af. Tilgangen: 1) Er komponenten en kernekompetence / strategisk vigtig? Så taler det for make uanset prisen. 2) Hvor høj er forsyningsrisikoen og afhængigheden af leverandøren? 3) Sammenlign de SAMLEDE omkostninger (ikke kun stykpris, men også transaktions-, koordinerings- og risikoomkostninger). Konklusionen er en balance: køb det der er standard og ikke-strategisk; lav selv det der er kritisk for konkurrenceevnen.",
  "alt": "Samme komponent kan forsvares som både make og buy: vægter du pris og fleksibilitet højest, anbefaler du buy; vægter du kontrol, viden og forsyningssikkerhed højest, anbefaler du make. Begge er forsvarlige afhængigt af, hvor strategisk komponenten vurderes.",
  "fisker": "Eksaminator vil høre, at du ser det som en afvejning mellem strategisk kontrol og pris — ikke bare 'hvad er billigst' — og at kernekompetence og forsyningsrisiko trækker mod make, mens standardvarer trækker mod buy.",
  "soeg": [
   "make-vs-buy",
   "egenproduktion",
   "outsourcing",
   "kernekompetence",
   "strategisk kontrol"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Rammeaftale og disponering",
  "sp": "Hvad er en rammeaftale, og hvordan hænger den sammen med disponeringen af indkøb?",
  "type": "rigtigt",
  "svar": "En rammeaftale er en aftale, der på forhånd fastlægger de overordnede VILKÅR for fremtidige køb hos en leverandør — typisk pris(er), kvalitet, leveringsbetingelser og en periode — men UDEN at man binder sig til en bestemt samlet mængde eller bestemte leveringstidspunkter på forhånd. Selve købene foretages løbende ved AFKALD/AFRUF (disponering) inden for rammen, efterhånden som behovet opstår. Disponering er netop dét: at man løbende bestiller/hjemkalder de konkrete mængder på de aftalte vilkår, når lageret eller behovet kræver det. Sammenhængen: rammeaftalen SÆTTER vilkårene én gang (sparer forhandling og administration ved hvert køb og sikrer faste priser), og disponeringen er den løbende UDNYTTELSE af aftalen — de enkelte ordrer der trækkes på rammen. Fordelene er lavere transaktionsomkostninger pr. ordre, prissikkerhed, hurtigere genbestilling og ofte bedre priser pga. det forventede samlede volumen; til gengæld binder man sig til leverandøren i aftaleperioden.",
  "alt": "",
  "fisker": "Eksaminator vil have, at du adskiller de to ting: rammeaftalen = vilkårene aftalt på forhånd for en periode; disponering/afkald = de løbende konkrete bestillinger der trækker på rammen — og at rammen sparer administration og sikrer pris.",
  "soeg": [
   "rammeaftale",
   "disponering",
   "afkald",
   "transaktionsomkostninger",
   "genbestilling"
  ]
 },
 {
  "fag": "Indkøb",
  "emne": "Find nye leverandører",
  "sp": "Virksomheden vil finde nye leverandører til et indkøbsområde. Hvordan ville du gribe leverandørsøgningen og -udvælgelsen an?",
  "type": "argument",
  "svar": "En struktureret leverandørsøgning kan gribes an i trin: 1) Afklar BEHOVET og kravene først — hvad skal købes, i hvilken mængde, hvilken kvalitet, hvilke krav til levering, pris, miljø/etik osv. (kravspecifikation). 2) SØG bredt efter mulige leverandører: brancheforeninger, messer, kataloger/databaser, internet, anbefalinger fra netværk, eksisterende kontakter. 3) Lav en FORUNDERSØGELSE/screening, så listen koges ind til de kandidater der overhovedet kan opfylde de kvalificerende minimumskrav. 4) Indhent tilbud / send forespørgsel (fx udbud eller RFQ) til de udvalgte. 5) EVALUÉR systematisk — gerne med en vægtet scoremodel på pris, kvalitet, leveringssikkerhed, kapacitet, økonomi/soliditet og service. 6) Vurdér RISIKO og afhængighed (skal det være single eller flere leverandører?) og evt. besøg/audit. 7) Forhandl og indgå aftale (fx rammeaftale). Pointen er at gå fra mange mulige til få egnede via klare kriterier, så valget bliver gennemsigtigt og ikke tilfældigt — og at man matcher søgemetoden til hvor vigtig og risikofyldt varen er (Kraljic).",
  "alt": "Man kan forsvare at lægge vægten forskelligt: en grundig, ressourcetung proces med audits og besøg er rigtig for strategiske/flaskehalsvarer, mens en let, hurtig søgning (fx blot indhente få tilbud) er rigtig for ikke-kritiske standardvarer. Hvor meget arbejde søgningen skal koste, afhænger af varens betydning.",
  "fisker": "Eksaminator vil se, at du har en systematisk proces (behov → søg → screen → tilbud → evaluér → vælg) frem for tilfældig leverandørjagt, og at du tilpasser dybden efter varens kritikalitet — argumentet og metoden, ikke en bestemt leverandør.",
  "soeg": [
   "leverandørsøgning",
   "udvælgelse",
   "kravspecifikation",
   "screening",
   "rfq"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Ordretyper MTS/ATO/MTO/ETO",
  "sp": "Forklar forskellen på MTS, ATO, MTO og ETO, og giv et eksempel på hver. Hvad er sammenhængen mellem ordretype, færdigvarelager og leveringstid?",
  "type": "rigtigt",
  "svar": "De fire ordretyper beskriver, hvor langt produktet er færdiglavet, før kundens ordre kommer ind — altså hvor 'kundeordre-frakoblingspunktet' ligger. MTS (Make To Stock) = vi producerer til lager på forhånd, kunden køber fra hylden. Eksempel: mælk, sodavand, standard-tøj. ATO (Assemble To Order) = vi har komponenter på lager og samler først ved ordre. Eksempel: en computer eller bil med valgfrie konfigurationer. MTO (Make To Order) = vi starter produktionen først når ordren er der. Eksempel: en specialfremstillet maskine eller møbel efter mål. ETO (Engineer To Order) = vi designer/konstruerer produktet fra bunden til den enkelte kunde. Eksempel: en bro, et skib eller et stort anlæg. Sammenhængen er central: jo længere mod MTS, jo større færdigvarelager men kort leveringstid (kunden venter ikke); jo længere mod ETO, jo lavere/intet færdigvarelager men lang leveringstid. MTS binder kapital i lager og har risiko for kurans; MTO/ETO binder ingen færdigvarer men kunden skal vente.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at du forstår frakoblingspunktet og kan koble det til afvejningen lager versus leveringstid — ikke bare ramse de fire bogstaver op. Pointen er trade-off'et: MTS=højt lager/kort ventetid, ETO=intet lager/lang ventetid.",
  "soeg": [
   "mts",
   "ato",
   "mto",
   "eto",
   "frakoblingspunkt",
   "leveringstid"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Lean vs Fordisme",
  "sp": "Hvad er forskellen på Lean og Fordisme som produktionsfilosofier, og hvorfor opstod Lean som et opgør med Fordismen?",
  "type": "argument",
  "svar": "Fordisme (samlebåndet hos Ford, tidligt 1900-tal) bygger på masseproduktion af standardvarer, store seriestørrelser, høj specialisering og stordriftsfordele — 'enhver farve så længe den er sort'. Målet er lavest mulig stykpris ved at producere meget af det samme. Lean (udviklet hos Toyota) er et opgør med dette: i stedet for at maksimere maskinudnyttelse og store batches fokuserer Lean på at fjerne spild (muda), trække produktionen efter reel efterspørgsel, små seriestørrelser, fleksibilitet og løbende forbedring (kaizen). Lean opstod fordi Fordismens store lagre og store batches skjuler problemer, binder kapital og ikke kan håndtere variation i efterspørgslen. Jeg vil argumentere for, at Lean er bedre, når markedet kræver variation og hurtig omstilling, mens Fordisme stadig er stærk ved meget høj, stabil volumen af ét standardprodukt.",
  "alt": "Man kan også forsvare, at Fordisme og Lean ikke er modsætninger men ligger på et spektrum: moderne fabrikker kombinerer begge — Fords flow-tankegang er faktisk en forløber for Leans flow, og Lean overtog samlebåndets stræben efter flow uden afbrydelser. Så Lean kan ses som en videreudvikling snarere end et brud.",
  "fisker": "Eksaminator er ude efter, at du kan stille de to filosofier op mod hinanden med rigtige begreber (spild, batch-størrelse, push versus pull) og selv tage stilling — ikke at der findes ét facit. Det vigtige er argumentet og forståelsen af hvorfor.",
  "soeg": [
   "lean",
   "fordisme",
   "spild",
   "masseproduktion",
   "toyota",
   "kaizen"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "MRP (skub) vs JIT (træk)",
  "sp": "Forklar forskellen på MRP og JIT som styringsprincipper. Hvad menes med 'skub' versus 'træk', og hvad er den store risiko ved JIT?",
  "type": "rigtigt",
  "svar": "MRP (Material Requirements Planning) er et skubbe-system (push): man planlægger ud fra en prognose og en produktionsplan, beregner hvilke materialer der skal bruges hvornår, og 'skubber' produktionen frem efter planen uanset hvad der lige nu er efterspurgt nedstrøms. JIT (Just In Time) er et trække-system (pull): intet produceres, før det næste led faktisk efterspørger det — efterspørgslen 'trækker' varen gennem systemet, ofte styret med kanban-signaler. JIT sigter mod minimalt lager: man får materialerne lige når man skal bruge dem, hvilket frigør kapital og afslører problemer. Den store risiko ved JIT er netop sårbarheden: fordi der ikke er buffere/lager, kan selv et lille forsyningsbrud (en leverandør der svigter, en strejke, en forsinkelse) stoppe hele produktionen. MRP er mere robust over for udsving fordi den planlægger frem og kan bygge buffer, men risikerer omvendt at producere efter en forkert prognose og dermed opbygge for meget lager.",
  "alt": "",
  "fisker": "Pointen er, at du forstår push versus pull og kan nævne JIT's akilleshæl: minimalt lager giver lav kapitalbinding MEN gør forsyningskæden sårbar over for brud. Sig ikke 'det afhænger' — her er der en klar definition.",
  "soeg": [
   "mrp",
   "jit",
   "push",
   "pull",
   "kanban",
   "forsyningsbrud"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Produktionsformer",
  "sp": "Beskriv de fire produktionsformer jobshop, serieproduktion, flow-/masseproduktion og projekt. Hvordan hænger valg af produktionsform sammen med volumen og variation?",
  "type": "rigtigt",
  "svar": "De fire former adskiller sig ved volumen (hvor meget) og variation (hvor forskelligt): 1) Projekt = ét unikt, stort produkt ad gangen, meget lav volumen, meget høj variation. Eksempel: et byggeri eller et skib. 2) Jobshop (enkeltstyk/styk-produktion) = mange forskellige produkter i små mængder, lav volumen/høj variation. Eksempel: et maskinværksted der laver specialdele. 3) Serieproduktion (batch) = man kører hold/batches af samme vare, derefter omstiller til næste — mellem volumen og variation. Eksempel: et bageri eller medicinalproduktion i partier. 4) Flow-/masseproduktion = meget høj volumen af ensartede produkter på en kontinuerlig linje, lav variation. Eksempel: sodavandsfabrik eller bilfabrik. Sammenhængen følger 'produkt-proces-matricen': høj variation/lav volumen trækker mod projekt og jobshop; lav variation/høj volumen trækker mod flow. Vælger man forkert — fx flow-linje til høj variation — bliver det dyrt og ufleksibelt.",
  "alt": "",
  "fisker": "Eksaminator vil se, at du kan placere de fire former på akserne volumen og variation og forklare logikken (produkt-proces-matricen), ikke bare nævne navnene. Pointen er sammenhængen mellem hvad man laver og hvordan man bør producere det.",
  "soeg": [
   "jobshop",
   "serieproduktion",
   "flowproduktion",
   "projekt",
   "volumen",
   "variation"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Produktionslayout",
  "sp": "Forklar de fire layouttyper: fast position, linjelayout, funktionslayout og gruppelayout. Hvilket layout passer til hvilken produktionsform?",
  "type": "argument",
  "svar": "Layout handler om, hvordan man fysisk placerer maskiner og arbejdsstationer: 1) Fast position (fast plads): produktet står stille, og folk/maskiner kommer til det — bruges når produktet er for stort til at flytte. Passer til projekt (skib, bygning). 2) Linjelayout (produktlayout): maskinerne stilles i den rækkefølge produktet skal igennem, varen flyder ned ad linjen. Passer til flow-/masseproduktion (samlebånd). 3) Funktionslayout (proceslayout): ens maskiner samles i afdelinger (al svejsning ét sted, al maling et andet), og produktet flyttes rundt mellem afdelinger. Passer til jobshop, hvor mange forskellige varer har forskellige ruter. 4) Gruppelayout (cellelayout): man samler de maskiner der skal bruges til en familie af lignende produkter i en celle — en mellemting der giver noget af linjens flow men med fleksibilitet. Passer til serieproduktion. Jeg vil forsvare koblingen: linjelayout til høj volumen/lav variation, funktionslayout til lav volumen/høj variation, gruppelayout som kompromiset midt imellem.",
  "alt": "Man kan også argumentere for, at koblingen ikke er fast: en virksomhed med høj volumen men en vis variation kan med fordel vælge gruppe-/cellelayout frem for ren linje, fordi celler giver kortere omstilling og mere fleksibilitet. Så valget afhænger lige så meget af variation i produktmikset som af ren volumen.",
  "fisker": "Eksaminator er ude efter, at du kan parre layout med produktionsform OG begrunde det med flow versus fleksibilitet — der findes ikke ét rigtigt svar for en given virksomhed, så det er argumentet (volumen/variation, omstilling, transportafstand) der tæller.",
  "soeg": [
   "layout",
   "linjelayout",
   "funktionslayout",
   "gruppelayout",
   "fast position",
   "celle"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "S&OP: Level vs Chase",
  "sp": "Forklar de to grundstrategier i Sales & Operations Planning: Level og Chase. Hvad svinger, og hvad holdes konstant i hver strategi?",
  "type": "argument",
  "svar": "S&OP handler om at matche produktionskapacitet med forventet efterspørgsel over de næste måneder. De to rene strategier: Level-strategi (udjævning): man holder produktionstakt og arbejdsstyrke konstant, og lader lageret svinge — i lavsæson opbygger man lager, i højsæson tærer man på det. Fordel: stabil bemanding, ingen dyre op-/nedjusteringer, god kvalitet/moral. Ulempe: binder kapital i lager og risiko for kurans. Chase-strategi (jagt): man lader arbejdsstyrken/produktionen følge efterspørgslen tæt — ansætter/fyrer, bruger overarbejde eller vikarer, så lageret holdes minimalt. Fordel: lavt lager, lav kapitalbinding. Ulempe: dyre og besværlige justeringer af bemanding, slid på medarbejdere, kvalitetsrisiko ved oplæring. Jeg vil forsvare Level når efterspørgslen er sæsonbetonet men forudsigelig og varen kan lagres, og Chase når varen ikke kan lagres (fx friske varer eller services).",
  "alt": "Man kan også forsvare en hybrid-/blandet strategi som det reelle valg i praksis: rent Level eller rent Chase er ekstremer, og de fleste virksomheder kombinerer — fast kernebemanding (Level) suppleret med vikarer/overarbejde i toppe (Chase). Så svaret kan lige så gyldigt være 'mix' frem for at vælge én.",
  "fisker": "Eksaminator vil høre, at du klart kan sige HVAD der svinger: i Level svinger lageret (bemanding konstant), i Chase svinger bemandingen (lager konstant/minimalt). Det er argumentet for hvornår hver passer, der tæller — ikke et facit.",
  "soeg": [
   "sop",
   "level",
   "chase",
   "kapacitet",
   "efterspoergsel",
   "bemanding"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "OEE og dens tre faktorer",
  "sp": "Hvad står OEE for, og hvilke tre faktorer indgår i beregningen? Vis hvordan de ganges sammen, og forklar hvad hver faktor måler.",
  "type": "rigtigt",
  "svar": "OEE står for Overall Equipment Effectiveness (samlet udstyrseffektivitet) og måler, hvor godt en maskine/produktionslinje udnyttes i forhold til sit fulde potentiale. OEE = Tilgængelighed × Ydelse × Kvalitet. 1) Tilgængelighed (Availability): hvor stor del af den planlagte tid maskinen faktisk kører — tab her er nedbrud, omstilling og ventetid. 2) Ydelse (Performance): hvor hurtigt maskinen kører i forhold til sin maksimale hastighed mens den kører — tab her er smådriftsstop og langsom kørsel. 3) Kvalitet (Quality): hvor stor del af det producerede der er fejlfrit (godt) i forhold til det samlede — tab her er kassation og omarbejde. De tre ganges sammen, så de udtrykkes som decimaler/procenter. Eksempel: 90% tilgængelighed × 95% ydelse × 98% kvalitet = ca. 0,84 = 84% OEE. Fordi de ganges, trækker selv én svag faktor hele resultatet ned — det er pointen ved at gange og ikke lægge sammen.",
  "alt": "",
  "fisker": "Pointen er, at du kan formlen Tilgængelighed × Ydelse × Kvalitet og kan forklare hvad hvert led måler og hvilke tab det fanger. Vis gerne at de ganges (ikke lægges sammen), så én dårlig faktor smitter af på det hele.",
  "soeg": [
   "oee",
   "tilgaengelighed",
   "ydelse",
   "kvalitet",
   "udstyrseffektivitet",
   "tab"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "OTIF / perfect order",
  "sp": "Hvad betyder OTIF, og hvad er en 'perfect order'? Hvorfor bliver tallet ofte lavt, selv når hver enkelt delkrav opfyldes ret godt?",
  "type": "rigtigt",
  "svar": "OTIF står for On Time In Full — altså leveret til tiden OG i fuld mængde. Det er et leveringsservice-mål, der kun tæller en ordre som god, hvis den både kom rettidigt og var komplet. 'Perfect order' (den perfekte ordre) er en udvidelse: ordren skal være til tiden, i fuld mængde, fejlfri (uden skader/defekter) OG med korrekt dokumentation/faktura. Grunden til at tallet ofte bliver overraskende lavt er, at kravene multipliceres: hvis hver delkrav opfyldes 95% af tiden, bliver den samlede andel 0,95 × 0,95 × 0,95 × 0,95 ≈ 0,81, altså kun 81% perfekte ordrer — selvom hvert enkelt led ser flot ud. Det illustrerer, at jo flere krav en 'perfekt' ordre skal opfylde, jo hårdere bliver det samlede mål, fordi en fejl på blot ét krav diskvalificerer hele ordren.",
  "alt": "",
  "fisker": "Eksaminator vil se, at du forstår at OTIF/perfect order er et 'alt-eller-intet' mål pr. ordre, og at delkravene ganges sammen — derfor falder totalen selv ved gode enkelttal. Det er multiplikationseffekten, der er pointen.",
  "soeg": [
   "otif",
   "perfect order",
   "leveringsservice",
   "til tiden",
   "fuld maengde",
   "multiplikation"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Little's Law",
  "sp": "Forklar Little's Law (WIP = R × T). Hvad betyder hver størrelse, og hvordan kan loven bruges til at reducere mængden af igangværende arbejde?",
  "type": "rigtigt",
  "svar": "Little's Law beskriver sammenhængen mellem mængden af igangværende arbejde og gennemløbstiden i et system: WIP = R × T. WIP (Work In Process) = antallet af enheder der er i gang i systemet på et givet tidspunkt. R (Rate / throughput) = den hastighed enheder strømmer igennem med, fx enheder pr. time. T (Throughput time / gennemløbstid) = den tid en enhed i gennemsnit bruger på at komme igennem systemet. Loven læses sådan: mængden af igangværende arbejde er lig med strømningshastigheden ganget med gennemløbstiden. Fortolkningen og det praktiske: hvis man vil reducere WIP (mindre kapitalbinding, mindre rod på gulvet), kan man ved given gennemstrømning (R) gøre det ved at sænke gennemløbstiden T — altså få enhederne hurtigere igennem. Omvendt: meget WIP ved samme hastighed betyder automatisk lang gennemløbstid. Loven kan også omskrives til T = WIP / R, så man kan beregne gennemløbstiden ud fra hvor meget der ligger i systemet og hvor hurtigt der produceres.",
  "alt": "",
  "fisker": "Pointen er, at du kan formlen WIP = R × T, kan forklare de tre størrelser og kan fortolke den: lavere gennemløbstid giver lavere WIP ved samme gennemstrømning. Vis gerne omskrivningen T = WIP/R.",
  "soeg": [
   "littles law",
   "wip",
   "gennemloebstid",
   "throughput",
   "igangvaerende",
   "flow"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "MPS og ATP",
  "sp": "Hvad er forskellen på MPS og ATP? Forklar hvordan ATP beregnes ud fra MPS, og hvad sælgeren kan bruge ATP til.",
  "type": "rigtigt",
  "svar": "MPS (Master Production Schedule / hovedproduktionsplan) er den overordnede plan for, hvad og hvor meget der skal produceres af de færdige produkter i hver periode (fx hver uge). Den oversætter prognoser og kundeordrer til konkrete produktionsmængder. ATP (Available To Promise / disponibel til løfte) er den mængde, sælgeren frit kan love nye kunder uden at vælte planen — altså hvad der er tilbage, når man har trukket allerede indgåede ordrer fra det planlagte/på-lager. ATP beregnes ud fra MPS sådan: man tager det der er på lager plus den planlagte produktion (fra MPS) i perioden og trækker de ordrer fra, der allerede er lovet til kunder frem til næste produktionsbatch. Det der er tilbage = ATP. Sælgeren bruger ATP til at give kunden et realistisk leveringstilsagn: 'ja, vi kan love dig 200 stk i uge 30', fordi der reelt er den mængde udisponeret. Uden ATP risikerer man at love det samme parti til flere kunder (overbooking).",
  "alt": "",
  "fisker": "Eksaminator vil høre, at MPS er produktionsplanen, og ATP er det udisponerede der kan loves væk = lager + planlagt produktion − allerede lovede ordrer. Pointen er, at ATP forhindrer at man lover mere end man kan levere.",
  "soeg": [
   "mps",
   "atp",
   "hovedproduktionsplan",
   "available to promise",
   "leveringstilsagn",
   "ordrer"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Knap kapacitet / flaskehals",
  "sp": "Hvad er en flaskehals, og hvorfor sætter den hele linjens output? Forklar princippet 'dækningsbidrag pr. flaskehalstime' og hvordan det styrer hvilke produkter man bør prioritere.",
  "type": "rigtigt",
  "svar": "En flaskehals er det trin i produktionen, der har lavest kapacitet — den ressource der ikke kan følge med, og som derfor begrænser hvad hele systemet kan producere. Princippet er, at en kæde ikke er stærkere end sit svageste led: uanset hvor hurtigt alle andre stationer kører, kan linjens samlede output aldrig blive større end det flaskehalsen kan klare. Derfor sætter flaskehalsen takten for det hele. 'Dækningsbidrag pr. flaskehalstime' er beslutningsreglen, når kapaciteten på flaskehalsen er knap: man skal IKKE prioritere det produkt, der har størst dækningsbidrag pr. stk, men det der giver størst dækningsbidrag pr. time det lægger beslag på flaskehalsen. Man beregner: DB pr. enhed ÷ den tid enheden bruger på flaskehalsen = DB pr. flaskehalstime. Det produkt med højest DB pr. flaskehalstime producerer man først, for det tjener mest pr. knap time. Pointen: når kapaciteten er knap, er det den knappe ressource, ikke stykfortjenesten, der skal optimeres efter.",
  "alt": "",
  "fisker": "Eksaminator er ude efter to ting: at flaskehalsen styrer det samlede output (svageste led), og at man ved knap kapacitet prioriterer efter DB pr. flaskehalstime — IKKE efter DB pr. stk. Det er den fælde, de tester.",
  "soeg": [
   "flaskehals",
   "kapacitet",
   "daekningsbidrag",
   "flaskehalstime",
   "output",
   "prioritering"
  ]
 },
 {
  "fag": "Produktion",
  "emne": "Takt time",
  "sp": "Hvad er takt time, og hvordan beregnes den? Forklar hvordan takt time bruges til at indrette en produktionslinje.",
  "type": "rigtigt",
  "svar": "Takt time er det tempo, produktionen skal holde for præcis at følge med kundernes efterspørgsel — altså hvor ofte en færdig enhed skal forlade linjen for at matche salget. Den beregnes som: Takt time = tilgængelig produktionstid i en periode ÷ kundeefterspørgslen i samme periode. Eksempel: har man 480 minutter til rådighed på en dag og kunderne efterspørger 240 enheder, er takt time 480/240 = 2 minutter pr. enhed — der skal komme en færdig enhed ud hvert 2. minut. Takt time bruges til at indrette linjen (line balancing): man fordeler arbejdsopgaverne på stationerne, så ingen stations cyklustid overstiger takt time. Hvis en station er langsommere end takt time (cyklustid > takt time), bliver den en flaskehals, og linjen kan ikke følge efterspørgslen. Er en station hurtigere end takt time, opstår der ventetid/spildtid på den station, fordi den må vente på linjens takt — og hvis man lader den løbe i forvejen, fører det til overproduktion og oplager. Målet er, at hver stations cyklustid ligger så tæt på (men ikke over) takt time som muligt, så flowet er jævnt og matcher kundernes efterspørgsel — hverken for hurtigt (oplager) eller for langsomt (manko).",
  "alt": "",
  "fisker": "Pointen er formlen tilgængelig tid ÷ efterspørgsel og forståelsen af at takt time er efterspørgslens 'puls' man balancerer linjen efter — ikke maskinens maks-hastighed. Vis gerne et lille regneeksempel.",
  "soeg": [
   "takt time",
   "efterspoergsel",
   "line balancing",
   "cyklustid",
   "produktionstid",
   "flow"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "Interessentanalyse (magt-interesse)",
  "sp": "Du har placeret en bestemt interessent i feltet 'høj magt + høj interesse' og valgt at samarbejde tæt med dem. Forklar din placering — og overbevis mig om, at den interessent ikke i virkeligheden hører til i et andet felt.",
  "type": "argument",
  "svar": "Magt-interesse-matricen (Mendelow) placerer interessenter efter to akser: hvor meget magt de har til at påvirke projektet, og hvor stor interesse (engagement) de har i det. Den interessent jeg har valgt har høj magt, fordi de kan stoppe eller godkende projektet (fx kan de trække en kontrakt eller blokere en beslutning), og høj interesse, fordi udfaldet rammer dem direkte. Derfor er den rigtige strategi 'samarbejd tæt' (manage closely): jeg involverer dem løbende, inddrager dem i beslutninger og bruger ekstra tid på dem, fordi de både kan og vil påvirke resultatet. Det forsvarer placeringen: det er kombinationen af KAN (magt) og VIL (interesse), der afgør feltet, ikke hvor sympatisk eller synlig interessenten er.",
  "alt": "Samme interessent kan forsvares som 'hold tilfreds' (høj magt, lav interesse), hvis deres interesse i praksis er lav — de har formel magt, men engagerer sig sjældent og vil helst ikke forstyrres. Så ville for tæt involvering irritere dem, og man skulle i stedet holde dem tilfredse uden at overinvolvere. Pointen er, at placeringen kan skifte, hvis man vurderer interessen anderledes.",
  "fisker": "Eksaminator vil høre, om du kan begrunde placeringen ud fra de to akser (magt OG interesse) og koble den til den rette af de fire strategier — ikke om du har ramt det 'rigtige' felt, men om argumentet holder.",
  "soeg": [
   "interessentanalyse",
   "magt",
   "interesse",
   "matrice",
   "strategi"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "De fire strategier",
  "sp": "Nævn de fire strategier i magt-interesse-matricen, og forklar hvilken kombination af magt og interesse der hører til hver. Hvad sker der typisk galt, hvis man bytter om på to af dem?",
  "type": "rigtigt",
  "svar": "De fire strategier er: 1) Samarbejd tæt (manage closely) ved HØJ magt + HØJ interesse — disse inddrages aktivt og løbende. 2) Hold tilfreds (keep satisfied) ved HØJ magt + LAV interesse — de har magt nok til at skade projektet, men gider ikke detaljer, så de holdes tilfredse uden at overlæsses. 3) Hold informeret (keep informed) ved LAV magt + HØJ interesse — de er engagerede og kan være gode ambassadører, så de holdes orienteret. 4) Overvåg (monitor) ved LAV magt + LAV interesse — minimal indsats, hold blot øje med dem. Hvis man bytter om, går det typisk galt sådan: behandler man en 'hold tilfreds' (magtfuld, men uinteresseret) som 'hold informeret', spammer man dem med detaljer, de bliver irriterede og kan vende sig mod projektet. Omvendt, behandler man en 'samarbejd tæt' som 'overvåg', mister man en nøgleperson, der både kan og vil påvirke udfaldet.",
  "alt": "",
  "fisker": "Pointen er, at du kender de fire felter præcist (hvilken magt/interesse-kombination giver hvilken strategi) og forstår konsekvensen af at fejlplacere — det er ren faktaviden om modellen.",
  "soeg": [
   "fire strategier",
   "samarbejd tæt",
   "hold tilfreds",
   "hold informeret",
   "overvåg"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "BATNA",
  "sp": "Hvad betyder BATNA, og hvordan påvirker en stærk BATNA din forhandlingsmagt? Giv et konkret eksempel fra en leverandørforhandling.",
  "type": "rigtigt",
  "svar": "BATNA står for 'Best Alternative To a Negotiated Agreement' — altså dit bedste alternativ, hvis forhandlingen IKKE fører til en aftale. Det er din 'plan B'. Jo stærkere din BATNA er, jo mere forhandlingsmagt har du, fordi du roligt kan gå fra bordet uden at stå tomhændet. Modparten kan ikke presse dig, når du har et godt alternativ. Konkret eksempel: Skal du forhandle pris med leverandør A, og du allerede har et godt, billigt tilbud fra leverandør B liggende, så er tilbuddet fra B din BATNA. Det betyder, at du ikke behøver acceptere en dårlig pris fra A — du kan sige nej og gå til B. Har du derimod ingen alternativer (svag BATNA), er du afhængig af A og må tage, hvad du kan få. Pointen: man styrker sin position ved at forbedre sin BATNA INDEN forhandlingen, fx ved at indhente flere tilbud. (Bemærk: BATNA er det etablerede begreb fra Fisher & Ury; 'BAPTA' er ikke et anerkendt fagudtryk og bør ikke bruges.)",
  "alt": "",
  "fisker": "Eksaminator vil høre, at BATNA = dit alternativ uden for forhandlingen, og at en stærk BATNA = mere magt, fordi du kan gå fra bordet. Det er en definition med en klar årsagssammenhæng — ikke et 'det afhænger'.",
  "soeg": [
   "batna",
   "alternativ",
   "forhandlingsmagt",
   "plan b",
   "fisher ury"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "ZOPA",
  "sp": "Forklar hvad ZOPA er, og hvordan den hænger sammen med parternes modstandspunkter. Hvad betyder det, hvis der ikke findes nogen ZOPA?",
  "type": "rigtigt",
  "svar": "ZOPA står for 'Zone Of Possible Agreement' — forhandlingszonen, hvor en aftale er mulig. Den opstår, hvor de to parters modstandspunkter (deres yderste accepterede grænse) OVERLAPPER. Eksempel: Køber vil maks. betale 100.000 kr. (købers modstandspunkt), sælger vil mindst have 80.000 kr. (sælgers modstandspunkt). Så er ZOPA intervallet mellem 80.000 og 100.000 — enhver pris derimellem kan begge parter acceptere. Findes der INGEN ZOPA, betyder det, at der ikke er noget overlap: hvis køber maks. vil give 70.000, men sælger mindst skal have 80.000, er der et 'gab' på 10.000, og så er der ingen mulig aftale. Parterne kan enten gå fra bordet, eller en af dem må flytte sit modstandspunkt (fx hvis deres BATNA forværres), før en aftale bliver mulig. Pointen: ZOPA er overlappet mellem modstandspunkterne — intet overlap, ingen handel.",
  "alt": "",
  "fisker": "Pointen er, at du kan definere ZOPA som overlappet mellem de to modstandspunkter og forstå konsekvensen af manglende overlap (ingen aftale). Det er en præcis fagdefinition.",
  "soeg": [
   "zopa",
   "forhandlingszone",
   "modstandspunkt",
   "overlap",
   "aftale"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "Målpunkt (MDO) og modstandspunkt (LDO)",
  "sp": "Hvad er forskellen på dit målpunkt (MDO) og dit modstandspunkt (LDO)? Hvorfor er det vigtigt at have fastlagt begge INDEN du går ind i forhandlingen?",
  "type": "rigtigt",
  "svar": "Målpunktet (MDO — Most Desired Outcome) er det bedst tænkelige, men stadig realistiske resultat du sigter efter — det du åbner med og helst vil opnå. Modstandspunktet (LDO — Least Desired Outcome) er din nederste grænse, det dårligste du kan acceptere, før du hellere går fra bordet. Forskellen er altså 'drømmen' (MDO) versus 'smertegrænsen' (LDO). Det er vigtigt at fastlægge BEGGE inden forhandlingen af to grunde: 1) Målpunktet giver dig et ambitiøst sigtepunkt, så du ikke nøjes for tidligt — folk der sigter højt, opnår typisk mere. 2) Modstandspunktet beskytter dig mod at acceptere en dårlig aftale i kampens hede; det er din 'stop'-grænse, ofte fastsat ud fra din BATNA. Uden et forudbestemt modstandspunkt risikerer du at lade dig presse under din egen smertegrænse. Pointen: MDO trækker opad, LDO beskytter nedad, og overlappet mellem dit og modpartens modstandspunkt er det, der danner ZOPA.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at du kan adskille de to punkter (mål = sigtepunkt, modstand = nederste grænse) og forklare hvorfor begge skal fastlægges på forhånd. Klar fagdefinition uden 'det afhænger'.",
  "soeg": [
   "målpunkt",
   "mdo",
   "modstandspunkt",
   "ldo",
   "grænse"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "Principiel forhandling (Harvard)",
  "sp": "Harvard-modellen bygger på fire principper for principiel forhandling. Du har valgt at lægge vægt på ét af dem i din case. Forsvar dit valg — og forklar, hvorfor man ikke bare kunne nøjes med det ene princip.",
  "type": "argument",
  "svar": "Harvards fire principper for principiel forhandling er: 1) Adskil personen fra problemet (vær blød ved mennesket, hård ved sagen). 2) Fokusér på interesser, ikke positioner (spørg HVORFOR de vil noget, ikke kun HVAD de kræver). 3) Find løsninger til fælles fordel (generér flere muligheder, der gavner begge). 4) Brug objektive kriterier (markedspris, standarder, fakta — ikke ren viljestyrke). Jeg har lagt vægt på 'fokusér på interesser, ikke positioner', fordi det ofte er nøglen til at låse en fastlåst forhandling op: når man graver bag modpartens krav og finder den bagvedliggende interesse, opdager man tit, at der er flere veje til at opfylde den. Det forsvarer mit fokus i casen, hvor parterne stod stejlt på hver sin position. Men man kan ikke nøjes med ét princip: finder man fælles interesser uden objektive kriterier, mangler man et fair grundlag at lande prisen på; og glemmer man at adskille person fra problem, kan relationen spænde ben for selv den bedste interesseanalyse. De fire principper virker bedst sammen.",
  "alt": "Man kunne i stedet fremhæve 'objektive kriterier' som det vigtigste — især i en pris- eller leverandørforhandling, hvor en uafhængig markedspris eller en branchestandard hurtigt afgør uenigheden uden personlig magtkamp. Så ville argumentet være, at fakta er stærkere end interessegravning, når talen falder på kroner og øre.",
  "fisker": "Eksaminator er ude efter, om du kender alle fire principper og kan begrunde, hvorfor netop dit fokus passer til casen — samtidig med at du forstår, at principperne supplerer hinanden. Det er argumentet, ikke ét facit.",
  "soeg": [
   "harvard",
   "principiel forhandling",
   "interesser",
   "positioner",
   "objektive kriterier"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "Distributiv vs integrativ forhandling",
  "sp": "Forklar forskellen på distributiv og integrativ forhandling. I din case kunne man have valgt en integrativ tilgang — overbevis mig om, at det var det rigtige, og ikke bare en distributiv kamp om prisen.",
  "type": "argument",
  "svar": "Distributiv forhandling er en 'fast kage', man skal dele: det, den ene vinder, taber den anden (nulsumsspil). Det handler typisk om ét emne, fx prisen, og bliver en tovtrækning om hvem der får den største bid. Integrativ forhandling derimod 'udvider kagen': man forhandler om FLERE emner samtidig (pris, leveringstid, betalingsbetingelser, mængde, service) og bytter på tværs af dem, så begge parter får det, de værdsætter mest. Resultatet kan blive en win-win, hvor begge står bedre. Jeg forsvarer den integrative tilgang i min case, fordi der var flere emner i spil end prisen: ved at give modparten noget, der var billigt for mig men værdifuldt for dem (fx længere kontrakt), og til gengæld få noget, der betød meget for mig (fx hurtigere levering), skabte vi mere samlet værdi end ren prisslagsmål. Det er pointen med integrativ: man leder efter forskelle i, hvad parterne vægter, og bytter sig til en større kage.",
  "alt": "Man kunne forsvare en distributiv tilgang, hvis der reelt KUN var ét emne på bordet — fx en ren spotpris på en standardvare, hvor der ikke er andre håndtag at bytte med. Så ville integrativ 'kage-udvidelse' være kunstig, og en ærlig distributiv forhandling om prisen ville være mest redelig og effektiv.",
  "fisker": "Eksaminator vil høre, at du kender forskellen (fast kage vs. udvid kagen) og kan begrunde tilgangsvalget ud fra antallet af emner og mulighederne for bytte — ikke at integrativ altid er 'bedst'.",
  "soeg": [
   "distributiv",
   "integrativ",
   "fast kage",
   "udvid kagen",
   "win-win"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "Kulturelle forhandlingsstile",
  "sp": "Du skal forhandle med en modpart fra en anden kultur end din egen, og du har valgt at tilpasse din stil. Forsvar dine tilpasninger — hvorfor risikerer det at gå galt, hvis du bare kører din vante danske stil videre?",
  "type": "argument",
  "svar": "Kulturer forhandler forskelligt på flere dimensioner: nogle er direkte og opgavefokuserede (fx dansk/skandinavisk og tysk stil — kom hurtigt til sagen, sig tingene ligeud), andre er indirekte og relationsfokuserede (mange asiatiske og mellemøstlige kulturer — byg tillid og relation FØR forretning, undgå at sige nej direkte). Der er også forskel på tidsopfattelse, hierarki (hvem må træffe beslutninger) og hvor meget man forhandler om prisen. Jeg forsvarer mine tilpasninger sådan: over for en relationsorienteret modpart bruger jeg mere tid på indledende smalltalk og tillidsopbygning, læser mellem linjerne i stedet for at presse på et direkte ja/nej, og respekterer hierarkiet ved at sikre, at den rette beslutningstager er til stede. Kører jeg bare min vante direkte danske stil videre, risikerer jeg at virke kold, utålmodig eller respektløs — modparten kan føle sig presset, miste ansigt, og relationen (og dermed aftalen) lider. Pointen er, at kulturel tilpasning ikke er at opgive sin position, men at vælge en kommunikationsform, modparten kan høre.",
  "alt": "Man kan forsvare at holde fast i en autentisk, direkte stil og blot melde det åbent ud ('jeg er dansker, vi taler ligeud — sig til, hvis noget støder dig'). Argumentet er, at overtilpasning kan virke uægte eller som manipulation, og at ærlighed og forudsigelighed også skaber tillid på tværs af kulturer.",
  "fisker": "Eksaminator er ude efter, om du kan beskrive kulturelle forhandlingsdimensioner (direkte/indirekte, relation/opgave, hierarki) og begrunde dine tilpasninger — ikke et facit på 'den rigtige' stil, men bevidstheden om forskellene.",
  "soeg": [
   "kultur",
   "forhandlingsstil",
   "direkte",
   "indirekte",
   "relation"
  ]
 },
 {
  "fag": "Kommunikation",
  "emne": "Byttechips",
  "sp": "Hvad er byttechips i en forhandling, og hvordan bruger man dem til at skabe værdi? Giv et eksempel på en god byttechip.",
  "type": "rigtigt",
  "svar": "Byttechips (trade-offs / handelsvariable) er de elementer, du kan give eller tage i en forhandling — altså de variable, der er i spil ud over hovedkravet. En god byttechip er noget, der er BILLIGT for dig at give væk, men VÆRDIFULDT for modparten at modtage (eller omvendt). Ved at kortlægge sådanne chips på forhånd kan man bytte på tværs af emner og dermed skabe værdi for begge parter — det er selve motoren i integrativ forhandling. Man giver aldrig noget gratis væk; man bytter det mod noget, man selv vægter højere. Eksempel på en god byttechip: I en leverandørforhandling kan du tilbyde en længere kontraktbinding (3 år i stedet for 1). For dig koster det relativt lidt, men for leverandøren er det meget værd, fordi det giver dem sikker omsætning. Til gengæld beder du om en lavere stykpris eller hurtigere levering, som betyder meget for dig. På den måde flytter man værdi derhen, hvor den vægtes højest, uden at nogen taber. Andre typiske chips: betalingsbetingelser, ordrestørrelse, leveringstid, service/garanti, eksklusivitet.",
  "alt": "",
  "fisker": "Pointen er, at du forstår byttechips som handelsvariable — billigt for dig, dyrt for modparten (eller omvendt) — og kan koble dem til værdiskabelse via bytte. Konkret fagviden, ikke holdning.",
  "soeg": [
   "byttechips",
   "trade-off",
   "indrømmelse",
   "værdiskabelse",
   "bytte"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "Primær vs. støtteaktivitet",
  "sp": "Du har placeret indkøb som en støtteaktivitet og logistik ind som en primær aktivitet. Begge handler jo om at få varer ind i virksomheden — hvad er forskellen, og hvorfor hører de ikke under det samme?",
  "type": "rigtigt",
  "svar": "Forskellen er, OM aktiviteten direkte indgår i den fysiske vare-/produktstrøm, eller om den understøtter den. Primære aktiviteter følger varen gennem virksomheden: logistik ind handler om selve modtagelsen, håndteringen og lagringen af de fysiske varer (varemodtagelse, opbevaring på råvarelageret/RVL, intern transport ind). Indkøb er en støtteaktivitet, fordi det handler om at vælge leverandører, forhandle priser og aftaler og sikre indkøbsbetingelser — altså beslutningerne og relationerne BAG varestrømmen, ikke den fysiske håndtering. Indkøb understøtter desuden hele virksomheden (man indkøber også maskiner, IT og serviceaftaler), ikke kun varestrømmen. Tommelfingerregel: indgår aktiviteten direkte i den fysiske strøm frem mod den vare kunden får (primær), eller gør den de primære aktiviteter mulige (støtte)?",
  "alt": "",
  "fisker": "At du forstår selve sondringen primær/støtte: primære aktiviteter ligger i den fysiske værdistrøm fra råvare til kunde, støtteaktiviteter gør strømmen mulig. Eksaminator vil høre at du kan begrunde placeringen ud fra dette princip og ikke bare har lært en liste udenad.",
  "soeg": [
   "primær",
   "støtte",
   "indkøb",
   "logistik ind",
   "sondring"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "De fem primære aktiviteter",
  "sp": "Nævn de fem primære aktiviteter i værdikæden i rækkefølge, og forklar kort hvad der sker i hver — særligt forskellen på logistik ind og logistik ud.",
  "type": "rigtigt",
  "svar": "De fem primære aktiviteter i rækkefølge er: 1) Logistik ind (indgående logistik) — modtagelse, håndtering og lagring af råvarer/varer, fx varemodtagelse og opbevaring på råvarelageret (RVL). 2) Produktion (operationer) — selve forarbejdningen, hvor råvarer/komponenter bliver til færdige varer. 3) Logistik ud (udgående logistik) — opbevaring af færdigvarer, plukning, pakning og forsendelse ud til kunden. 4) Marketing og salg — at skabe efterspørgsel og få ordren hjem (markedsføring, salgskanaler, prissætning). 5) Service — det der sker efter salget, fx montering, reklamation, reparation og support. Den vigtigste forskel: logistik IND er varer på vej ind til virksomheden (typisk råvarer/komponenter, RVL), logistik UD er færdige varer på vej ud til kunden (færdigvarelager, forsendelse). Produktionen ligger imellem dem og er det punkt, der adskiller de to.",
  "alt": "",
  "fisker": "At du kan rækkefølgen og kan holde logistik ind og logistik ud adskilt — de forveksles tit. Eksaminator vil høre at produktionen er skillelinjen, og at ind = råvarer/RVL, ud = færdigvarer/forsendelse.",
  "soeg": [
   "fem primære",
   "logistik ind",
   "logistik ud",
   "produktion",
   "service"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "De fire støtteaktiviteter",
  "sp": "Hvilke fire støtteaktiviteter arbejder man med, og hvorfor kalder man dem netop 'støtte' frem for primære?",
  "type": "rigtigt",
  "svar": "De fire støtteaktiviteter er: 1) Virksomhedens infrastruktur — ledelse, økonomistyring, planlægning, jura, kvalitetsstyring, altså det overordnede 'apparat' der holder virksomheden kørende. 2) Menneskelige ressourcer (HR) — rekruttering, oplæring, fastholdelse og udvikling af medarbejdere. 3) Teknologiudvikling — IT-systemer, produktudvikling, processer og know-how, fx ERP- og lagerstyringssystemer. 4) Indkøb — valg af leverandører, forhandling og indgåelse af indkøbsaftaler for hele virksomheden. De kaldes 'støtte', fordi de ikke selv indgår i den fysiske strøm fra råvare til færdig vare hos kunden, men gør de primære aktiviteter mulige og mere effektive. De løber typisk på tværs af alle de primære aktiviteter (HR og IT bruges fx både i produktion og i salg) i stedet for at følge varen ét sted i strømmen.",
  "alt": "",
  "fisker": "At du kender de fire støtteaktiviteter OG kan forklare hvorfor de er støtte: de ligger på tværs og muliggør den primære strøm frem for selv at være en del af den. Pas på ikke at forveksle indkøb (støtte) med logistik ind (primær).",
  "soeg": [
   "støtteaktiviteter",
   "infrastruktur",
   "hr",
   "teknologi",
   "indkøb"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "Analyse, ikke løsninger",
  "sp": "Hvorfor må der ikke stå løsningsforslag inde i selve værdikæden — er det ikke bare spild ikke at skrive løsningen lige der, hvor du har fundet problemet?",
  "type": "rigtigt",
  "svar": "Nej, det er et bevidst metodisk princip. Værdikæden er ren BESKRIVELSE og ANALYSE: dens opgave er at kortlægge, hvordan virksomheden faktisk arbejder station for station, og afdække hvor der er styrker, svagheder og udfordringer. Hvis man begynder at skrive løsninger ind i kæden, blander man to ting sammen: diagnosen (hvad er problemet) og behandlingen (hvad gør vi ved det). Det gør analysen rodet og svær at vurdere objektivt, og man risikerer at 'springe til løsninger' før man har overblik over helheden. I stedet samler man de fundne udfordringer op til sidst som en bro til konklusionen, og selve løsningsforslagene hører til i en SEPARAT del bagefter. Så bevarer kæden sin rolle som et neutralt analyseværktøj, og løsningerne kan bygge på det fulde billede frem for på et enkelt punkt.",
  "alt": "",
  "fisker": "At du forstår at værdikæden er et analyseværktøj, ikke et løsningskatalog. Eksaminator tester om du kan holde diagnose og behandling adskilt — løsninger kommer i en selvstændig del efter analysen. Sig ikke 'det afhænger'; her er der et klart korrekt princip.",
  "soeg": [
   "analyse",
   "ikke løsninger",
   "beskrivelse",
   "metode",
   "adskillelse"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "Harmoni",
  "sp": "Du skriver, at der skal være 'harmoni' i værdikæden. Hvad mener du med det, og kan du give et eksempel på manglende harmoni?",
  "type": "rigtigt",
  "svar": "Harmoni betyder, at de enkelte stationer i værdikæden spiller sammen og er afstemt med hinanden og med virksomhedens strategi — så der ikke er ét led, der trækker i en anden retning eller flaskehalser, der ødelægger helheden. En værdikæde skaber kun værdi, hvis leddene hænger sammen; en kæde er ikke stærkere end det svageste led. Eksempel på manglende harmoni: marketing og salg lover kunderne meget korte leveringstider, men logistik ud og produktionen er ikke gearet til det (for små lagre, lang produktionstid). Så opstår der utilfredse kunder og tabte ordrer, selvom hver afdeling for sig 'gør sit arbejde'. Et andet eksempel: indkøb vælger den billigste leverandør, men leverer så ustabilt, at produktionen ofte står stille. Harmoni handler altså om at vurdere kæden som en HELHED, ikke kun station for station.",
  "alt": "",
  "fisker": "At du kan løfte blikket fra de enkelte stationer til samspillet mellem dem. Eksaminator vil høre at du forstår kæden som en helhed, hvor et stærkt led ikke hjælper, hvis et andet led ikke følger med — og gerne et konkret eksempel.",
  "soeg": [
   "harmoni",
   "samspil",
   "helhed",
   "svageste led",
   "flaskehals"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "Udfordringer som bro til konklusion",
  "sp": "Til sidst i din værdikædeanalyse laver du en liste over udfordringer. Hvorfor er det smart at samle dem dér, og hvad er meningen med den liste?",
  "type": "argument",
  "svar": "Listen af udfordringer fungerer som broen mellem analysen og konklusionen/løsningsdelen. Når man har gået kæden igennem station for station og beskrevet, hvad der sker hvert sted, dukker der undervejs en række problemer og svagheder op — fx for store lagre, ustabile leverancer, lange leveringstider, dårligt systemoverblik. I stedet for at skrive løsninger ind i kæden (som man netop ikke må), 'parkerer' man de fundne udfordringer og samler dem i en samlet liste til sidst. Den liste viser klart, HVAD analysen har afdækket, og bliver det naturlige afsæt for konklusionen og for løsningsdelen bagefter: man kan tage udfordringerne ét for ét og adressere dem. Det giver en rød tråd fra beskrivelse → fund → konklusion → løsning, så læseren kan følge, at løsningerne faktisk udspringer af analysen.",
  "alt": "Man kan også forsvare at samle udfordringerne løbende undervejs (fx en kort delkonklusion efter hver station) frem for kun i én liste til sidst — det kan gøre det lettere at huske, hvor hver udfordring kom fra, og fastholde sammenhængen til den enkelte station. Pointen er den samme: udfordringerne skal opsamles og bygge bro, og løsninger holdes ude af selve kæden, uanset om opsamlingen sker løbende eller samlet.",
  "fisker": "At du forstår funktionen: listen er broen fra analyse til konklusion/løsning og holder løsningerne ude af selve kæden. Eksaminator er ude efter den røde tråd (fund → konklusion → løsning), ikke en bestemt placering af listen.",
  "soeg": [
   "udfordringer",
   "bro",
   "konklusion",
   "rød tråd",
   "opsamling"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "Hvad analyserer man på en station (logistik ind)",
  "sp": "Tag stationen 'logistik ind'. Hvad er det egentlig, du analyserer dér — og hvor passer Incoterms ind?",
  "type": "rigtigt",
  "svar": "På logistik ind analyserer man, hvordan virksomheden modtager og håndterer indgående varer: Hvordan foregår varemodtagelsen? Hvordan og hvor opbevares råvarer/komponenter (råvarelageret, RVL)? Hvor store er lagrene, og er der unødig lagerbinding eller pladsmangel? Hvordan er den interne transport fra modtagelse til lager/produktion? Hvordan kommer varerne fysisk frem til virksomheden — transportform og -ansvar? Netop dér passer Incoterms ind: Incoterms er de internationale leveringsbetingelser, der bestemmer, hvem (køber eller sælger) der betaler og bærer risikoen for transporten, og hvor ansvaret skifter fra sælger til køber. På logistik ind ser man på transporten IND til virksomheden (og tilsvarende ud på logistik ud), fordi Incoterms styrer ansvar, risiko og omkostninger i den fysiske transport. Bemærk: man BESKRIVER og analyserer disse forhold — fx at lageret er for stort — men skriver ikke løsningen ('reducér lageret') ind i kæden.",
  "alt": "",
  "fisker": "At du kan koble en konkret station til hvad man rent faktisk kigger på (varemodtagelse, RVL, lager, intern transport) og placere Incoterms korrekt under transport ind. Eksaminator vil høre at Incoterms = ansvar/risiko/omkostning i transporten, ikke noget der hører til produktion eller salg.",
  "soeg": [
   "logistik ind",
   "incoterms",
   "rvl",
   "varemodtagelse",
   "transport"
  ]
 },
 {
  "fag": "Værdikæde",
  "emne": "Placering af leverandørrelation",
  "sp": "Din samarbejdspartner/leverandør optræder flere steder i analysen. Hvilken del af værdikæden hører arbejdet med leverandøren til — og hvorfor kan man argumentere for mere end ét sted?",
  "type": "argument",
  "svar": "Det primære svar er, at selve arbejdet med at vælge leverandør, forhandle priser og indgå aftaler hører under støtteaktiviteten INDKØB. Indkøb er det sted i værdikæden, hvor leverandørrelationen som beslutning og aftale håndteres — det er her man vurderer pris, kvalitet, leveringssikkerhed og betingelser. Det er en støtteaktivitet, fordi det understøtter varestrømmen frem for selv at være den fysiske håndtering af varen.",
  "alt": "Man kan også forsvare, at leverandøren berører LOGISTIK IND: når de aftalte varer fysisk modtages, håndteres og lagres (RVL), og når transportansvaret ind reguleres via Incoterms, er det den primære station logistik ind, der er i spil. Og hvis leverandøren leverer ustabilt, dukker den udfordring op i analysen af logistik ind/produktion. Så: beslutningen og aftalen = indkøb (støtte); den fysiske modtagelse og transport = logistik ind (primær). Begge kan forsvares, så længe man begrunder det ud fra om man taler om aftalen eller den fysiske vare.",
  "fisker": "At du kan skelne mellem leverandøren som AFTALE (indkøb/støtte) og som fysisk VARESTRØM (logistik ind/primær) og begrunde din placering. Eksaminator er ikke ude efter ét facit, men efter at du argumenterer ud fra sondringen primær/støtte og kan se, at samme leverandør optræder forskellige steder afhængigt af vinklen.",
  "soeg": [
   "leverandør",
   "indkøb",
   "logistik ind",
   "relation",
   "placering"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "95% konfidensinterval",
  "sp": "Du har beregnet et 95% konfidensinterval for gennemsnittet. Hvad betyder de 95% — og hvad betyder de IKKE?",
  "type": "rigtigt",
  "svar": "De 95% handler om metoden, ikke om det enkelte interval. Det betyder: hvis vi gentog stikprøven rigtig mange gange og lavede et nyt interval hver gang, så ville cirka 95% af alle de intervaller fange den sande værdi i befolkningen. Det betyder IKKE, at der er 95% sandsynlighed for, at lige netop MIT interval rammer den sande værdi. Den sande værdi er et fast tal — den ligger enten inde i mit interval eller udenfor, så for det enkelte interval er der ikke en sandsynlighed på 95%. Sikkerheden ligger i fremgangsmåden, ikke i det ene resultat. Et bredt interval betyder stor usikkerhed (lille stikprøve eller stor spredning), et smalt interval betyder mere præcis viden.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at du kender den klassiske fælde: 95% er en egenskab ved metoden på tværs af mange gentagelser, ikke en sandsynlighed for det konkrete interval. Kan du skille de to ad, har du forstået det.",
  "soeg": [
   "konfidensinterval",
   "usikkerhed",
   "stikprøve",
   "fortolkning",
   "sand værdi"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "R2 (forklaringsgrad)",
  "sp": "Din regression giver en R2 på 0,80. Hvad fortæller det tal dig?",
  "type": "rigtigt",
  "svar": "R2 (forklaringsgraden) viser, hvor stor en del af variationen i y (det du vil forudsige) der kan forklares af x (det du bruger som forklaring). En R2 på 0,80 betyder, at 80% af udsvingene i y forklares af modellen/x, mens de sidste 20% skyldes andre ting, vi ikke har med. R2 ligger mellem 0 og 1 (eller 0–100%): tæt på 1 betyder, at x forklarer y godt, tæt på 0 betyder, at x næsten intet forklarer. Vigtigt: høj R2 betyder ikke automatisk, at x ER årsag til y — det viser kun, hvor godt sammenhængen passer på data. Den siger heller ikke noget om, hvorvidt selve sammenhængen giver fagligt mening.",
  "alt": "",
  "fisker": "Pointen er, at du kan oversætte tallet til ren tekst: andel af variationen i y forklaret af x. Bonus hvis du tilføjer, at høj forklaringsgrad ikke er det samme som årsagssammenhæng.",
  "soeg": [
   "forklaringsgrad",
   "regression",
   "variation",
   "sammenhæng",
   "model"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Normaltilnærmelse til binomial",
  "sp": "Hvornår må man tilnærme en binomialfordeling med en normalfordeling — og hvorfor er det praktisk?",
  "type": "rigtigt",
  "svar": "Tommelfingerreglen er, at normaltilnærmelsen gælder, når n gange p er mindst 5 OG n gange (1−p) er mindst 5. Altså: både det forventede antal 'succeser' og det forventede antal 'fiaskoer' skal være mindst 5. n er antal forsøg og p er sandsynligheden for succes. Når begge betingelser er opfyldt, ligner binomialfordelingen en pæn klokkeform, og man kan regne videre med den nemmere normalfordeling i stedet for de tunge binomialformler. Hvis p er meget lille eller meget stor, og n samtidig er lille, bliver fordelingen skæv, og så holder tilnærmelsen ikke — da skal man bruge den rigtige binomialfordeling.",
  "alt": "",
  "fisker": "Eksaminator vil have den konkrete regel — np ≥ 5 og n(1−p) ≥ 5 — og at du kan sige hvorfor: begge haler skal være store nok til, at klokkeformen passer.",
  "soeg": [
   "binomial",
   "normaltilnærmelse",
   "np",
   "tommelfingerregel",
   "sandsynlighed"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Punkt uden for kontrolgrænserne",
  "sp": "På dit kontrolkort ligger et punkt uden for kontrolgrænserne. Hvad betyder det, og hvad gør du?",
  "type": "rigtigt",
  "svar": "Et punkt uden for kontrolgrænserne er et signal om en særårsag — altså noget særligt og udefrakommende, der har påvirket processen, så den er ude af kontrol. Det er ikke bare tilfældig variation, som man altid har lidt af. Derfor skal man ikke bare ignorere det: man leder efter den konkrete årsag (fx en maskine der er kommet ud af indstilling, et nyt råvareparti, en fejl i målingen) og retter den, før man kører videre. Kontrolgrænserne er typisk sat ved cirka 3 standardafvigelser fra midten, så det er meget usandsynligt at ryge udenfor ved ren tilfældighed — derfor tolker vi det som et reelt signal og ikke støj.",
  "alt": "",
  "fisker": "Pointen er ordet 'særårsag' og forskellen til almindelig tilfældig variation: et punkt udenfor er et alarmsignal, der kræver en undersøgelse, ikke en justering på må og få.",
  "soeg": [
   "kontrolkort",
   "kontrolgrænser",
   "særårsag",
   "proces",
   "ude af kontrol"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "p-kort vs. X-bar/R-kort",
  "sp": "Hvornår vælger du et p-kort frem for et X-bar/R-kort?",
  "type": "rigtigt",
  "svar": "Det afhænger af, hvad du måler. Et p-kort bruges, når data er en ANDEL af noget, du tæller op — fx andelen af defekte enheder i hver prøve (godkendt/ikke godkendt, ja/nej-data). X-bar/R-kort bruges, når du MÅLER en talstørrelse på en skala — fx længde, vægt eller temperatur. Her følger X-bar-kortet gennemsnittet i hver prøve (er processen centreret rigtigt?), og R-kortet følger variationsbredden inden for prøven (er spredningen stabil?). Kort sagt: tæller du fejl/andele, så p-kort; måler du en kontinuerlig værdi, så X-bar/R-kort. Valget styres altså af datatypen — attributdata (tælledata) mod variabeldata (måledata).",
  "alt": "",
  "fisker": "Eksaminator tjekker, om du kobler korttype til datatype: andele/tælledata → p-kort, måledata på en skala → X-bar/R-kort. Det er ikke et frit valg.",
  "soeg": [
   "p-kort",
   "x-bar",
   "r-kort",
   "tælledata",
   "måledata"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "t- vs. z-fordeling",
  "sp": "Hvornår bruger du t-fordelingen, og hvornår z-fordelingen (normalfordelingen)?",
  "type": "rigtigt",
  "svar": "Det styres af, om du kender den sande spredning (sigma) i befolkningen, og af stikprøvens størrelse. Du bruger t-fordelingen, når du IKKE kender den sande spredning og må bruge stikprøvens egen spredning som skøn — det gælder især ved små stikprøver. t-fordelingen er lidt bredere end normalfordelingen og har 'tykkere haler', netop fordi den indregner den ekstra usikkerhed ved at gætte spredningen ud fra data. Du bruger z-fordelingen (normalfordelingen), når den sande spredning er kendt, eller når stikprøven er stor (en tommelfingerregel er n over ca. 30). Grunden til at stor n tillader z er, at stikprøvens spredning ved mange observationer bliver et pålideligt skøn for den sande spredning, så den ekstra usikkerhed bliver forsvindende lille. Ved store stikprøver nærmer t-fordelingen sig derfor normalfordelingen, og i praksis giver de næsten det samme der.",
  "alt": "",
  "fisker": "Pointen er den ene udløsende faktor: kender du sigma? Ukendt spredning og lille n → t. Kendt spredning eller stor n → z. Vis at du ved, hvorfor t er bredere (ekstra usikkerhed ved at estimere spredningen), og hvorfor stor n alligevel tillader z.",
  "soeg": [
   "t-fordeling",
   "z-fordeling",
   "sigma",
   "stikprøve",
   "usikkerhed"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Signifikansniveau",
  "sp": "Hvad er et signifikansniveau på 5%, og hvad fortæller det dig om dit resultat?",
  "type": "rigtigt",
  "svar": "Signifikansniveauet (ofte kaldt alfa) er den grænse, du på forhånd sætter for, hvor stor en risiko du vil acceptere for at tage fejl ved at forkaste nulhypotesen, når den i virkeligheden er sand (en type 1-fejl). Et niveau på 5% betyder, at du accepterer 5% risiko for fejlagtigt at konkludere, at der er en effekt/forskel, selvom der i virkeligheden ikke er nogen. I praksis sammenligner man p-værdien med de 5%: er p-værdien mindre end 0,05, kalder man resultatet signifikant og forkaster nulhypotesen; er den større, kan man ikke forkaste den. Vigtigt: at et resultat er signifikant betyder, at det næppe skyldes ren tilfældighed — det betyder ikke automatisk, at effekten er stor eller vigtig i praksis.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at signifikansniveauet er en på forhånd valgt fejlrisiko (type 1-fejl), og at du kan koble det til p-værdien. Bonus: signifikant ≠ praktisk vigtigt.",
  "soeg": [
   "signifikansniveau",
   "alfa",
   "p-værdi",
   "nulhypotese",
   "fejlrisiko"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "NPV>0 betydning",
  "sp": "Du har en investering med en positiv nutidsværdi (NPV>0). Hvad betyder det helt konkret, og hvorfor skal vi gå videre med den?",
  "type": "rigtigt",
  "svar": "NPV>0 betyder, at investeringen skaber værdi UD OVER det afkastkrav, vi på forhånd har sat. NPV er summen af alle fremtidige ind- og udbetalinger, omregnet til kroner i dag (diskonteret med kalkulationsrenten), minus den oprindelige investering. Når det tal er positivt, betyder det, at projektet ikke bare tjener pengene hjem og betaler for det afkast, vi kræver (vores kalkulationsrente) — det giver ekstra oveni. Et eksempel: en NPV på +200.000 kr. betyder, at projektet — efter at have leveret det krævede afkast på alle de penge, vi binder — lægger 200.000 kr. ekstra værdi til virksomheden, målt i nutidskroner. Derfor er beslutningsreglen klar: NPV>0 = sig ja, NPV<0 = sig nej, NPV=0 = neutralt (projektet rammer præcis afkastkravet, hverken mere eller mindre).",
  "alt": "",
  "fisker": "Eksaminator vil høre, at du forstår NPV som MERVÆRDI over afkastkravet — ikke bare 'overskud'. Pointen er at vise, at afkastkravet allerede er trukket fra inde i beregningen, så et positivt tal er ægte ekstra værdi.",
  "soeg": [
   "npv",
   "nutidsværdi",
   "afkastkrav",
   "værdiskabelse",
   "investeringsbeslutning"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "NPV vs IRR",
  "sp": "NPV og IRR peger nogle gange på hver sit projekt. Hvornår sker det, og hvilken metode stoler du på?",
  "type": "rigtigt",
  "svar": "NPV og IRR kan rangordne forskelligt, når man skal vælge mellem gensidigt udelukkende projekter — altså hvor man kun kan vælge ét. Det sker typisk, når projekterne har forskellig STØRRELSE (skala) eller forskelligt tidsmønster i betalingerne. IRR er en procent og ignorerer skala: et lille projekt kan have en flot IRR på 40 %, men kun skabe 50.000 kr. i værdi, mens et stort projekt med 20 % IRR skaber 2 mio. kr. IRR'en siger 'vælg det lille', men det store gør virksomheden mest rig. NPV måler værdi i kroner og fanger derfor størrelsen korrekt. Derfor stoler man på NPV ved uenighed: målet er at maksimere kroner-værdi, ikke at jagte den højeste procent. NPV bygger desuden på en mere realistisk antagelse om, at frie pengestrømme geninvesteres til kalkulationsrenten, ikke til den (ofte urealistisk høje) IRR. Bemærk: for ét enkeltstående projekt med normale betalinger giver NPV>0 og IRR>kalkulationsrenten samme ja/nej-konklusion — uenigheden opstår først ved rangordning.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at IRR ignorerer skala/størrelse, og at NPV vinder ved RANGORDNING af gensidigt udelukkende projekter, fordi vi vil maksimere VÆRDI i kroner. Nævn gerne også geninvesteringsantagelsen som ekstra argument.",
  "soeg": [
   "npv",
   "irr",
   "skala",
   "rangordning",
   "gensidigt udelukkende"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Diskontering / kalkulationsrente",
  "sp": "Hvorfor diskonterer du de fremtidige betalinger overhovedet, og hvad er det egentlig, kalkulationsrenten dækker over?",
  "type": "rigtigt",
  "svar": "Man diskonterer, fordi en krone i dag er mere værd end en krone om et år. Det er ikke bare inflation — det handler om alternativomkostning og risiko. Pengene kunne i stedet være sat i arbejde et andet sted og have givet afkast, og fremtidige betalinger er usikre. Diskontering omregner derfor fremtidige kroner til, hvad de er værd i dag, så vi kan sammenligne beløb på tværs af tid på samme grundlag. Kalkulationsrenten (diskonteringsrenten) er virksomhedens AFKASTKRAV — den mindste forrentning vi kræver for at binde pengene. Den kan ses som sammensat af et risikofrit afkast plus et risikotillæg for det konkrete projekt, og den afspejler alternativomkostningen ved at binde kapitalen. Jo højere rente, jo hårdere straffes betalinger langt ude i fremtiden, og jo lavere bliver nutidsværdien.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at renten er et AFKASTKRAV (alternativomkostning + risiko), ikke bare inflation. Pointen er, at diskontering gør beløb fra forskellige år sammenlignelige.",
  "soeg": [
   "diskontering",
   "kalkulationsrente",
   "afkastkrav",
   "alternativomkostning",
   "risiko"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Soliditetsgrad",
  "sp": "Virksomhedens soliditetsgrad er på fx 35 %. Hvordan fortolker du det tal, og hvad fortæller det om virksomheden?",
  "type": "rigtigt",
  "svar": "Soliditetsgraden = egenkapital / samlede aktiver, og den fortæller, hvor stor en del af virksomhedens aktiver der er finansieret med EGENKAPITAL frem for med gæld. En soliditet på 35 % betyder, at 35 % af alt det, virksomheden ejer, er finansieret med egenkapital, mens de resterende 65 % er finansieret med gæld. Tallet er et mål for robusthed og modstandskraft: jo højere soliditet, jo bedre kan virksomheden tåle underskud og dårlige tider uden at gå konkurs, fordi der er en stor egenkapital-stødpude til at absorbere tab, før kreditorerne rammes. Lav soliditet betyder meget gæld og dermed højere risiko, men kan også betyde, at virksomheden gearer sig op for at vokse hurtigere. Hvad der er 'godt' afhænger af branchen — kapitaltunge brancher tåler ofte lavere soliditet, fordi de har stabile aktiver at stille som sikkerhed.",
  "alt": "",
  "fisker": "Eksaminator vil høre formlen (egenkapital/aktiver) OG fortolkningen som robusthed/stødpude mod tab. Pointen er, at høj soliditet = modstandskraft, ikke nødvendigvis 'bedst' i alle brancher.",
  "soeg": [
   "soliditetsgrad",
   "egenkapital",
   "aktiver",
   "robusthed",
   "finansiering"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Likviditetsgrad",
  "sp": "Hvad fortæller likviditetsgraden dig, som soliditetsgraden ikke gør?",
  "type": "rigtigt",
  "svar": "Likviditetsgraden måler, om virksomheden kan betale sine KORTFRISTEDE regninger til tiden — altså den helt nære betalingsevne. Den beregnes typisk som omsætningsaktiver / kortfristet gæld (likviditetsgrad 2, current ratio). En likviditetsgrad på fx 120 % betyder, at virksomheden har 1,20 kr. i omsætningsaktiver (varelager, tilgodehavender, kasse) for hver 1 krone gæld, der skal betales inden for et år. Er den under 100 %, kan virksomheden have svært ved at betale regningerne, når de forfalder. Forskellen til soliditet er tidshorisonten og fokus: soliditet ser på den LANGSIGTEDE kapitalstruktur og robusthed (gæld vs. egenkapital), mens likviditet ser på den KORTSIGTEDE evne til at betale lige nu. En virksomhed kan godt være solid på lang sigt, men stadig komme i akut likviditetsklemme, hvis pengene er bundet og regningerne forfalder.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at likviditet handler om KORTSIGTET betalingsevne (kan vi betale regningerne nu), mens soliditet er den langsigtede kapitalstruktur. Pointen er forskellen i tidshorisont.",
  "soeg": [
   "likviditetsgrad",
   "betalingsevne",
   "omsætningsaktiver",
   "kortfristet gæld",
   "current ratio"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Gearing",
  "sp": "Hvad menes der med, at en virksomhed er højt 'gearet', og hvad er bagsiden af det?",
  "type": "rigtigt",
  "svar": "Gearing beskriver, hvor meget virksomheden bruger GÆLD (fremmedkapital) i forhold til egenkapital til at finansiere sig. Høj gearing = meget lånte penge i forhold til egne. Tanken er, at man kan forstørre afkastet på egenkapitalen: hvis virksomheden tjener mere på de lånte penge, end de koster i renter, går merafkastet til ejerne, og afkastet på den egne kapital løftes — en løftestangseffekt. Bagsiden er, at gearing virker begge veje. Når det går dårligt, forstørrer gælden også tabene på egenkapitalen, fordi renter og afdrag skal betales uanset hvad. Høj gearing øger derfor risikoen og gør virksomheden mere sårbar over for rentestigninger og dårlige år. Gearing er altså et tveægget sværd: den kan løfte afkastet i gode tider, men presse virksomheden hårdt — helt ud i konkurs — i dårlige. Høj gearing hænger sammen med lav soliditet.",
  "alt": "",
  "fisker": "Eksaminator vil høre løftestangseffekten BEGGE veje: gearing forstørrer både gevinst og tab på egenkapitalen. Pointen er afvejningen mellem højere afkast og højere risiko.",
  "soeg": [
   "gearing",
   "fremmedkapital",
   "løftestang",
   "risiko",
   "kapitalstruktur"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Dækningsbidrag vs dækningsgrad",
  "sp": "Hvornår bruger du dækningsbidrag, og hvornår bruger du dækningsgrad — hvad er forskellen?",
  "type": "rigtigt",
  "svar": "Dækningsbidrag (DB) er et KRONE-beløb: salgspris minus de variable omkostninger pr. styk (eller i alt). Det fortæller, hvor mange kroner hvert salg bidrager med til at dække de faste omkostninger og derefter skabe overskud. Dækningsgrad (DG) er en PROCENT: dækningsbidraget i procent af omsætningen (DB/omsætning × 100). Den fortæller, hvor stor en andel af hver salgskrone der bliver til dækningsbidrag. Hvornår bruges hvad: Brug DB pr. styk, når du skal vurdere ét konkret produkt eller en konkret ordre — fx 'tjener vi nok pr. enhed', eller hvilket produkt der bidrager mest i kroner. Brug DG, når du vil SAMMENLIGNE på tværs af produkter med forskellige priser, eller regne på samlet omsætning — fx 'hvor meget omsætning skal vi have for at dække de faste omkostninger' (break-even i kroner = faste omkostninger / DG). DG er god til relativ lønsomhed; DB er god til den absolutte kroneeffekt.",
  "alt": "",
  "fisker": "Eksaminator vil høre, at DB er KRONER pr. stk og DG er PROCENT af omsætningen, og hvornår hver er nyttig (DB til enkeltprodukt/ordre, DG til sammenligning og break-even i kroner).",
  "soeg": [
   "dækningsbidrag",
   "dækningsgrad",
   "variable omkostninger",
   "break-even",
   "lønsomhed"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Paybacks begrænsninger",
  "sp": "Du har brugt payback-metoden til at vurdere en investering. Hvilke svagheder har den, som eksaminator kan angribe?",
  "type": "rigtigt",
  "svar": "Payback fortæller kun, hvor hurtigt investeringen er tjent hjem — antal år, før de samlede indbetalinger har dækket den oprindelige udbetaling. Den har to alvorlige svagheder. For det første ignorerer den (i sin simple form) DISKONTERING: den behandler en krone om fem år som lige så meget værd som en krone i dag, hvilket er forkert, fordi penge har en tidsværdi. For det andet, og vigtigst, ignorerer den ALT, hvad der sker EFTER tilbagebetalingstidspunktet. Et projekt, der er tjent hjem på 3 år og så stopper, ser bedre ud end et, der bruger 4 år men derefter giver kæmpe overskud i 10 år — selvom det sidste klart skaber mere værdi. Payback siger altså intet om den samlede indtjening eller lønsomhed; den måler kun likviditetsrisiko/hvor hurtigt pengene er sikret. Derfor bør den kun bruges som et supplement til NPV, ikke som den afgørende metode.",
  "alt": "",
  "fisker": "Eksaminator vil høre BEGGE begrænsninger: payback ignorerer diskontering OG indtjeningen efter tilbagebetaling. Pointen er, at den måler hastighed/risiko, ikke værdiskabelse.",
  "soeg": [
   "payback",
   "tilbagebetalingstid",
   "diskontering",
   "begrænsninger",
   "indtjening"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "DuPont-modellen",
  "sp": "Forklar DuPont-modellen: hvordan splitter den afkastningsgraden op, og hvad bruger man det til?",
  "type": "rigtigt",
  "svar": "DuPont-modellen splitter afkastningsgraden (resultat før renter i forhold til den investerede kapital/aktiver) op i to drivere: Afkastningsgrad = Overskudsgrad × Aktivernes omsætningshastighed (AOH). Overskudsgraden (resultat før renter / omsætning × 100) viser INDTJENINGEN — hvor stor en del af hver salgskrone der bliver til driftsoverskud. AOH (omsætning / aktiver) viser KAPITALUDNYTTELSEN — hvor mange gange virksomheden 'omsætter' sine aktiver, altså hvor effektivt aktiverne skaber salg. Pointen er, at to virksomheder kan have samme afkastningsgrad, men nå dertil på vidt forskellige måder: en kan tjene meget pr. salg men sælge langsomt (høj overskudsgrad, lav AOH — fx en luksusbutik), en anden tjene lidt pr. salg men sælge i store mængder (lav overskudsgrad, høj AOH — fx en discountkæde). Modellen bruges til at FINDE årsagen, når afkastningsgraden ændrer sig: er det indtjeningen pr. salg eller kapitaludnyttelsen, der driver det? Det peger direkte på, hvor man skal sætte ind.",
  "alt": "",
  "fisker": "Eksaminator vil høre formlen (afkastningsgrad = overskudsgrad × AOH) OG fortolkningen: overskudsgrad = indtjening pr. salg, AOH = hvor effektivt aktiverne udnyttes. Pointen er at finde ÅRSAGEN bag afkastet.",
  "soeg": [
   "dupont",
   "afkastningsgrad",
   "overskudsgrad",
   "aoh",
   "kapitaludnyttelse"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Break-even",
  "sp": "Hvad betyder break-even-punktet, og hvad bruger du det til i en investerings- eller priskalkule?",
  "type": "rigtigt",
  "svar": "Break-even (nulpunktet) er det salg, hvor virksomheden lige akkurat går i nul — hverken overskud eller underskud. På det punkt dækker det samlede dækningsbidrag præcis de faste omkostninger. Den simple formel er: Break-even i styk = Faste omkostninger / Dækningsbidrag pr. styk. (I kroner: Faste omkostninger / Dækningsgrad.) Modellen forudsætter, at salgspris og variable omkostninger pr. styk er konstante (lineære), så DG er den samme uanset mængde. Fortolkningen: sælger man én enhed mere end break-even, begynder man at tjene penge; sælger man mindre, taber man. Man bruger break-even til at vurdere RISIKO og 'sikkerhedsmargin': hvor langt er det forventede salg fra nulpunktet? Ligger break-even tæt på det forventede salg, er projektet skrøbeligt — et lille fald i salget tipper det over i underskud. Ligger break-even langt under forventningen, er der god margin at stå imod med. Det er også et hurtigt værktøj til at teste, om en pris eller et omkostningsniveau overhovedet er realistisk: 'hvor meget SKAL vi sælge, før det her løber rundt?'",
  "alt": "",
  "fisker": "Eksaminator vil høre, at break-even er nulpunktet (DB dækker faste omkostninger) OG at det bruges til at vurdere risiko/sikkerhedsmargin — hvor følsomt projektet er over for salgsudsving.",
  "soeg": [
   "break-even",
   "nulpunkt",
   "faste omkostninger",
   "dækningsbidrag",
   "sikkerhedsmargin"
  ]
 }
]
