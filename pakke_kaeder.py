"""Ekstra dybde-kæder til "Eksaminator borer" (eskalerende forsvars-kæder).

Forfattet + censur-verificeret via workflow. Samme struktur som KÆDER i siden:
hver kæde = {emne, fag, lag:[{sp, arg, fisker, alt, snyd, fakta}]}.
Lægges OVEN PÅ de 8 oprindelige kæder (ingen fjernes).
"""

EKSTRA_KAEDER = [{'emne': 'Ansoffs vækstmatrix',
  'fag': 'Strategi',
  'lag': [{'sp': 'Hvad er Ansoffs vækstmatrix, og hvilke fire vækststrategier indeholder den?',
           'arg': 'Ansoffs matrix viser fire vækstveje ud fra to akser: produkt (eksisterende/nyt) og '
                  'marked (eksisterende/nyt). De fire felter er markedspenetrering (kendt produkt på kendt '
                  'marked), markedsudvikling (kendt produkt på nyt marked), produktudvikling (nyt produkt '
                  'på kendt marked) og diversifikation (nyt produkt på nyt marked).',
           'fisker': 'Om du kan opstille de to akser og placere alle fire felter korrekt.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvis vi vil vokse med lavest mulig risiko, hvilken strategi peger du så på, og hvorfor?',
           'arg': 'Markedspenetrering, fordi vi bliver på kendt produkt og kendt marked. Vi kender '
                  'kunderne, distributionen og produktet, så usikkerheden er mindst. Vi vokser ved at '
                  'sælge mere til eksisterende kunder eller tage markedsandele fra konkurrenter.',
           'fisker': 'Om du forstår at risiko stiger jo længere væk fra det kendte du bevæger dig.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'En virksomhed vil sprede sin risiko ved at gå ind i en helt ny branche med et helt nyt '
                 'produkt. Er det den sikre vej at sprede risikoen?',
           'arg': 'Nej — det er en fælde. Diversifikation lyder som risikospredning, men det er netop den '
                  'FARLIGSTE strategi i Ansoff, fordi både produkt og marked er ukendt på samme tid. Man '
                  'har hverken erfaring med produktet eller kunderne, så to slags usikkerhed rammer '
                  'samtidig. Risikospredning på porteføljeniveau betyder ikke lav risiko i selve trækket.',
           'fisker': "Om du falder for at 'sprede risiko' = sikkert, eller om du ser at diversifikation er "
                     'det mest risikable felt.',
           'alt': 'Man kan nuancere: relateret diversifikation (hvor man kan trække på fælles teknologi '
                  'eller kanaler) er mindre farlig end konglomerat-diversifikation.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvornår kan diversifikation alligevel være det rigtige valg på trods af risikoen?',
           'arg': 'Når det eksisterende marked er mættet eller i tilbagegang, så fortsat penetrering ikke '
                  'giver vækst, eller når der opstår en stærk synergimulighed (fælles teknologi, indkøb '
                  'eller distribution). Høj risiko kan opvejes af høj gevinst og af at man ikke har '
                  'vækstveje tilbage i de tre sikrere felter.',
           'fisker': 'Om du kan forsvare en risikabel strategi situationsbestemt i stedet for at afvise '
                     'den per refleks.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Generisk SC-strategi: lean vs agil',
  'fag': 'Værdikæde',
  'lag': [{'sp': 'Hvad er forskellen på en lean og en agil supply chain-strategi?',
           'arg': 'Lean fokuserer på at fjerne spild og minimere omkostninger gennem stabilt, '
                  'forudsigeligt flow — fx lave lagre og høj kapacitetsudnyttelse. Agil fokuserer på '
                  'hurtig reaktion og fleksibilitet, så kæden kan svare på svingende eller uforudsigelig '
                  'efterspørgsel, fx med buffere og kort omstillingstid.',
           'fisker': 'Om du kender de to grundtyper: lean = effektiv/billig, agil = hurtig/fleksibel.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'En virksomhed har stabil, forudsigelig efterspørgsel på et standardprodukt. Hvilken '
                 'SC-strategi passer, og hvorfor ikke den anden?',
           'arg': 'Lean passer, fordi forudsigelig efterspørgsel gør det muligt at planlægge stramt og '
                  'skære spild væk. Agil ville her give unødige buffere og overkapacitet, altså ekstra '
                  'omkostninger uden gevinst, fordi der ikke er udsving at reagere på. Fleksibilitet '
                  'koster, og man betaler kun for den når efterspørgslen kræver det.',
           'fisker': 'Om du kan koble strategivalget til efterspørgslens karakter, ikke bare ramse '
                     'definitionerne op.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Vi sælger et billigt standardprodukt — bør hele forsyningskæden så være ren lean?',
           'arg': "Ikke nødvendigvis. Det er en fælde at sætte lighedstegn mellem 'billigt produkt' og "
                  "'lean hele vejen'. En hybrid (leagile) er ofte bedst: lean op til et afkoblingspunkt, "
                  'hvor man producerer standardkomponenter effektivt, og agil derefter, hvor man hurtigt '
                  'færdiggør mod den faktiske ordre. Også et billigt produkt kan have uforudsigelig '
                  'efterspørgsel, der kræver agilitet i den sidste del.',
           'fisker': 'Om du ser at lean/agil ikke er enten-eller, men kan kombineres via et '
                     'afkoblingspunkt.',
           'alt': 'Hvis efterspørgslen er helt stabil, kan ren lean stadig forsvares — pointen er at man '
                  'skal vurdere det, ikke antage det.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad afgør grundlæggende, om man skal vælge lean eller agil — produktet eller markedet?',
           'arg': 'Primært efterspørgslens forudsigelighed (markedet), ikke produktet i sig selv. '
                  'Stabil/forudsigelig efterspørgsel trækker mod lean; svingende/uforudsigelig '
                  'efterspørgsel trækker mod agil. Produktets levetid og variantbredde spiller med, men '
                  'det er forudsigeligheden, der er den afgørende variabel.',
           'fisker': 'Om du kan pege på efterspørgselsusikkerhed som den styrende faktor.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Organisationsstruktur: funktion vs objekt',
  'fag': 'Organisation',
  'lag': [{'sp': 'Hvad er forskellen på en funktionsopdelt og en objektopdelt organisationsstruktur?',
           'arg': 'Funktionsopdeling grupperer efter fagområde — fx indkøb, produktion, salg, økonomi — så '
                  'ens specialister samles. Objektopdeling (også kaldet markeds-/divisionsopdeling) '
                  'grupperer efter output — fx produkt, kunde eller geografi — så hver enhed har sine egne '
                  'funktioner samlet om ét objekt.',
           'fisker': 'Om du kender de to grundprincipper og kan give eksempler på akserne.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad er den store fordel ved funktionsopdeling, og hvad er den tilsvarende ulempe?',
           'arg': 'Fordelen er stordriftsfordele og dyb faglig specialisering, fordi alle med samme fag '
                  'samles og deler ressourcer og viden. Ulempen er silo-tænkning: afdelingerne optimerer '
                  'hver for sig, koordinationen på tværs bliver svær, og kunde- eller produktansvaret '
                  'falder mellem stolene.',
           'fisker': 'Om du både kan nævne stordrift som styrken OG silo som den indbyggede svaghed.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'En voksende virksomhed har silo-problemer i sin funktionsstruktur. Løser man det bedst '
                 'ved at skifte til objektopdeling?',
           'arg': 'Det er ikke gratis at skifte — det er en fælde at se objektopdeling som ren forbedring. '
                  'Objektopdeling løser silo på tværs af funktioner og giver klart resultatansvar, men man '
                  'MISTER stordriftsfordelene og får dobbeltfunktioner (hver division har egen indkøb, '
                  'økonomi osv.), hvilket koster ressourcer. Man bytter ét problem ud med et andet. '
                  'Alternativt kan man løse silo med koordinationsmekanismer (tværgående teams, '
                  'projektorganisation) uden at opgive funktionsstrukturen.',
           'fisker': "Om du ser trade-off'et: objektopdeling fjerner silo men ofrer stordrift, og at det "
                     'ikke er et entydigt fremskridt.',
           'alt': 'En matrixstruktur kan forene begge hensyn, men koster til gengæld klare kommandoveje '
                  '(to chefer).',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvornår peger du klart på objektopdeling frem for funktionsopdeling?',
           'arg': 'Når virksomheden er stor med meget forskellige produkter, kunder eller markeder, der '
                  'hver kræver tæt koordination og hurtig tilpasning. Her vejer det klare resultatansvar '
                  'og kundenærheden tungere end de stordriftsfordele, man giver afkald på.',
           'fisker': 'Om du kan koble strukturvalg til virksomhedens størrelse og produktbredde.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Linje/stab, kontrolspænd, flad vs høj',
  'fag': 'Organisation',
  'lag': [{'sp': 'Hvad er forskellen på en linjefunktion og en stabsfunktion?',
           'arg': 'Linjefunktioner indgår direkte i den lodrette kommandovej og har beslutnings- og '
                  'resultatansvar (fx produktionschef ned til medarbejder). Stabsfunktioner er rådgivende '
                  'og understøttende — fx jura, HR eller en analyseafdeling — uden direkte kommandoret '
                  'over linjen; de leverer ekspertise til linjelederne.',
           'fisker': 'Om du kan skille det udførende/besluttende (linje) fra det rådgivende (stab).',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad betyder kontrolspænd, og hvordan hænger det sammen med en flad eller høj '
                 'organisation?',
           'arg': 'Kontrolspænd er antallet af medarbejdere, en leder direkte har under sig. Et bredt '
                  'kontrolspænd betyder mange medarbejdere pr. leder og dermed færre ledelseslag — altså '
                  'en flad organisation. Et smalt kontrolspænd betyder få medarbejdere pr. leder og flere '
                  'lag — en høj organisation.',
           'fisker': 'Om du korrekt kobler bredt kontrolspænd til flad struktur (ikke det modsatte).',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'En leder vil have tættere styring og kontrol med sine folk. Bør han så gøre '
                 'kontrolspændet bredere?',
           'arg': 'Nej — det er en fælde. Tættere kontrol kræver et SMALT kontrolspænd, ikke et bredt. Med '
                  'få medarbejdere pr. leder kan lederen følge tæt med og styre detaljeret. Et bredt '
                  'kontrolspænd tvinger derimod til uddelegering og selvstændighed, fordi lederen ikke kan '
                  'nå at kontrollere alle. Ønsket om kontrol og ønsket om et bredt spænd trækker i hver '
                  'sin retning.',
           'fisker': "Om du gennemskuer at 'mere kontrol' = smalt spænd, så du ikke forveksler bredt spænd "
                     'med stærk styring.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad taler for en flad organisation med brede kontrolspænd, og hvad er prisen?',
           'arg': 'For taler: hurtigere kommunikation (kortere vej op og ned), lavere ledelsesomkostninger '
                  'og mere selvstændige, motiverede medarbejdere. Prisen er, at hver leder har mange folk '
                  'og derfor mindre tid til den enkelte, mindre tæt styring, og at det stiller krav om '
                  'kompetente, selvkørende medarbejdere og standardiserede opgaver.',
           'fisker': 'Om du kan afveje fordele (fart, omkostning) mod ulemper (mindre styring pr. '
                     'medarbejder).',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Organisk vs mekanistisk organisation',
  'fag': 'Organisation',
  'lag': [{'sp': 'Hvad kendetegner en mekanistisk organisation over for en organisk?',
           'arg': 'En mekanistisk organisation er stærkt formaliseret: faste regler, klare hierarkier, '
                  'snæver specialisering og centraliseret beslutning — tænk en velsmurt maskine. En '
                  'organisk organisation er løs og fleksibel: få faste regler, decentral beslutning, brede '
                  'roller og horisontal kommunikation, så den hurtigt kan tilpasse sig.',
           'fisker': 'Om du kender de to idealtyper og deres kendetegn (regelstyret vs fleksibel).',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'En virksomhed opererer på et marked i hastig forandring. Hvilken type passer, og hvorfor '
                 'ikke den anden?',
           'arg': 'Den organiske passer, fordi foranderlige markeder kræver hurtig tilpasning, decentral '
                  'beslutning og fleksibilitet. En mekanistisk struktur ville her være for stiv: de faste '
                  'regler og lange beslutningsveje gør den langsom til at reagere, og den taber til '
                  'konkurrenter, der omstiller sig hurtigere.',
           'fisker': 'Om du kobler organisk til foranderlige markeder og mekanistisk til stabile.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Organisk lyder mest moderne og effektivt. Er en organisk struktur derfor altid at '
                 'foretrække?',
           'arg': 'Nej — det er en fælde at se organisk som per definition bedst. På et STABILT, '
                  'forudsigeligt marked er den mekanistiske struktur ofte overlegen: regler, rutiner og '
                  'specialisering giver effektivitet, lave omkostninger og ensartet kvalitet. Organisk '
                  'fleksibilitet er kun en fordel, når der er forandring at tilpasse sig — ellers er det '
                  'bare uorden og spild. Valget afhænger af omgivelserne, ikke af mode.',
           'fisker': 'Om du undgår at hylde organisk ukritisk og ser at mekanistisk vinder i stabile '
                     'omgivelser.',
           'alt': 'Mange virksomheder er hybride: mekanistisk i drift/produktion og organisk i '
                  'udvikling/innovation.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad er den dybere variabel, der afgør valget mellem mekanistisk og organisk?',
           'arg': 'Omgivelsernes stabilitet og forudsigelighed (og dermed opgavernes karakter). Stabile, '
                  'forudsigelige omgivelser med rutineopgaver favoriserer mekanistisk; turbulente, '
                  'foranderlige omgivelser med nye opgaver favoriserer organisk. Det er '
                  'kontingenstænkning: den rette struktur afhænger af situationen, der er ikke én bedst.',
           'fisker': 'Om du kan formulere kontingensprincippet: strukturen skal matche omgivelserne.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'McGregors X- og Y-teori',
  'fag': 'Ledelse',
  'lag': [{'sp': 'Hvad går McGregors X-teori og Y-teori ud på?',
           'arg': 'De er to modsatte menneskesyn hos lederen. X-teori: mennesket er grundlæggende dovent, '
                  'undgår ansvar og skal styres, kontrolleres og motiveres med pisk og gulerod. Y-teori: '
                  'mennesket vil gerne arbejde, søger ansvar og motiveres indefra, så lederen skal give '
                  'frihed, tillid og udviklingsmuligheder.',
           'fisker': 'Om du kender de to menneskesyn og at de sidder hos LEDEREN.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'En Y-leder uddelegerer og giver frihed. Hvorfor virker det motiverende, og hvad er '
                 'svagheden ved en ren X-tilgang?',
           'arg': 'Y virker, fordi frihed og ansvar tilfredsstiller behov for selvstændighed og udvikling, '
                  'hvilket giver indre motivation og engagement. Ren X-ledelse med kontrol og ydre '
                  'belønning kan skabe modvilje og passivitet — folk gør kun det nødvendige, og lederen '
                  'får selv bekræftet sit negative menneskesyn (selvopfyldende profeti).',
           'fisker': 'Om du forstår motivationsmekanismen og X-tilgangens selvforstærkende faldgrube.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Er Y-teori så altid den rigtige ledelsesstil, fordi den er mest moderne og menneskelig?',
           'arg': 'Nej — det er en fælde. McGregor selv hælder til Y, men det er ikke et facit for alle '
                  'situationer. Ved meget rutineprægede opgaver, nye/uerfarne medarbejdere eller akutte '
                  'situationer kan en mere styrende (X-agtig) tilgang være nødvendig. Pointen er, at '
                  'menneskesynet styrer ledelsesstilen, og at man skal passe på den selvopfyldende profeti '
                  '— ikke at Y altid vinder.',
           'fisker': 'Om du ser at Y ikke er universelt rigtigt, men skal tilpasses opgave og medarbejder.',
           'alt': 'Situationsbestemt ledelse (fx Hersey-Blanchard) supplerer her: styr mere ved lav '
                  'modenhed, deleger mere ved høj.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Scheins menneskesyn',
  'fag': 'Ledelse',
  'lag': [{'sp': 'Hvilke menneskesyn opererer Schein med?',
           'arg': 'Schein beskriver fire menneskesyn, der har udviklet sig over tid: det '
                  'rationelle-økonomiske menneske (motiveres af penge/egennytte), det sociale menneske '
                  '(motiveres af relationer og fællesskab), det selvrealiserende menneske (motiveres af at '
                  'udvikle og udfolde sig) og det komplekse menneske (motiveres skiftende, afhængigt af '
                  'situation og person).',
           'fisker': 'Om du kan nævne de fire menneskesyn og deres motivationsgrundlag.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er det komplekse menneske et vigtigt opgør med de tre foregående menneskesyn?',
           'arg': 'Fordi de tre første hver især antager ÉT fast motiv for alle mennesker, mens det '
                  'komplekse menneske siger, at motivation varierer fra person til person og fra situation '
                  'til situation. Det betyder, at lederen ikke kan bruge én opskrift, men må aflæse den '
                  'enkelte medarbejder og tilpasse sin ledelse — det er et mere realistisk og fleksibelt '
                  'syn.',
           'fisker': 'Om du forstår at det komplekse menneske afviser én-størrelse-passer-alle-motivation.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Det rationelle-økonomiske menneske er det ældste syn. Betyder det, at penge ikke længere '
                 'motiverer, og at synet er forældet?',
           'arg': "Nej — det er en fælde at tro, at et 'ældre' menneskesyn er afløst og ugyldigt. Synene "
                  'supplerer hinanden snarere end at erstatte; penge motiverer stadig, men er sjældent '
                  'ene-motivet. Det komplekse menneske rummer netop, at det økonomiske motiv KAN være det '
                  'dominerende for nogle personer eller i nogle situationer. At et syn kom først betyder '
                  'ikke, at det er forkert i dag.',
           'fisker': "Om du undgår at læse udviklingen som 'det nye afløser det gamle' og ser synene som "
                     'supplerende.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Ledergitteret (Blake og Mouton)',
  'fag': 'Ledelse',
  'lag': [{'sp': 'Hvad viser Blake og Moutons ledergitter?',
           'arg': 'Ledergitteret placerer lederstil i et koordinatsystem med to akser: omsorg for '
                  'produktionen/opgaven (vandret) og omsorg for menneskene/medarbejderne (lodret), hver '
                  'fra 1 til 9. Kombinationen giver fem hovedstile, fx 1.1 (laissez-faire), 9.1 '
                  '(autoritær/opgavestyret), 1.9 (country club/relationsstyret), 5.5 (kompromis) og 9.9 '
                  '(team).',
           'fisker': 'Om du kan opstille de to akser og placere de fem typiske stile.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvilken stil ses som idealet i ledergitteret, og hvorfor?',
           'arg': '9.9 — teamledelse — er idealet, fordi den scorer højt på BÅDE opgave og mennesker '
                  'samtidig. Tanken er, at engagerede, involverede medarbejdere (høj omsorg for mennesker) '
                  'leverer de bedste resultater (høj omsorg for opgaven), så de to hensyn forstærker '
                  'hinanden i stedet for at udelukke hinanden.',
           'fisker': 'Om du ved at 9.9 er idealet og kan begrunde hvorfor begge akser maksimeres.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Er 5.5-stilen — den der ligger midt i gitteret og balancerer begge hensyn — så den '
                 'klogeste, fornuftige mellemvej?',
           'arg': "Nej — det er en fælde. 5.5 lyder fornuftigt, fordi den ligger i midten og 'balancerer', "
                  'men i Blake og Moutons logik er den et KOMPROMIS, hvor man går på akkord med begge '
                  'hensyn og ender middelmådig på begge. Idealet er ikke at gå halvt ind på begge akser '
                  '(5.5), men at maksimere begge samtidig (9.9). Midten er ikke målet — det øverste højre '
                  'hjørne er.',
           'fisker': "Om du gennemskuer at 'midten' (5.5) ikke er idealet, men netop en utilstrækkelig "
                     'mellemvej.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad er den væsentligste kritik af ledergitterets antagelse om, at 9.9 altid er bedst?',
           'arg': "At det er en normativ 'one best way', som overser situationen. Situationsbestemte "
                  'teorier indvender, at den rette stil afhænger af opgaven, medarbejdernes modenhed og '
                  'konteksten — i en krise eller med uerfarne folk kan en mere opgavestyret (9.1-agtig) '
                  'stil være bedre. 9.9 er et stærkt ideal, men ikke universelt korrekt i enhver '
                  'situation.',
           'fisker': 'Om du kan løfte kritikken: gitteret er normativt, virkeligheden er '
                     'situationsbestemt.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Adizes PAEI-roller',
  'fag': 'Ledelse',
  'lag': [{'sp': "Hvad står PAEI for i Adizes' ledelsesteori?",
           'arg': 'PAEI er fire ledelsesroller, der tilsammen skal være til stede for god ledelse: '
                  'Producer (P) — får resultater og løser opgaven nu; Administrator (A) — skaber orden, '
                  'systemer og styring; Entrepreneur (E) — er visionær, nyskabende og fremtidsrettet; '
                  'Integrator (I) — binder folk og holdet sammen.',
           'fisker': 'Om du kan oversætte de fire bogstaver til roller og deres fokus.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Adizes mener, at ingen enkelt leder kan udfylde alle fire roller lige godt. Hvad er '
                 'konsekvensen af det?',
           'arg': 'At god ledelse er en holdpræstation, ikke en solopræstation. Da rollerne delvis '
                  'modarbejder hinanden (fx Entrepreneurens forandring vs Administratorens orden), bliver '
                  'enhver leder stærk på nogle roller og svag på andre. Derfor skal man sammensætte et '
                  'komplementært ledelsesteam, så medlemmernes styrker dækker alle fire roller.',
           'fisker': 'Om du ser pointen: rollerne trækker i forskellige retninger, så ledelse må fordeles '
                     'på et team.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': "Så den ideelle leder er vel den, der mestrer alle fire PAEI-roller på én gang — 'den "
                 "perfekte leder'?",
           'arg': "Nej — det er netop en fælde, og Adizes' hovedpointe er det modsatte. Den perfekte leder "
                  '(PAEI på højt niveau hele vejen) findes IKKE; det er en myte. Rollerne er delvis '
                  'uforenelige, så jagten på supermennesket er forfejlet. Styrken ligger i at acceptere, '
                  'at hver leder er ufuldstændig, og bygge et komplementært team i stedet for at lede '
                  'efter et ledelsesgeni.',
           'fisker': "Om du gennemskuer at 'den alsidige superleder' er præcis det Adizes afviser.",
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad sker der typisk, hvis én rolle helt mangler i ledelsen?',
           'arg': 'Så opstår en bestemt form for fejlledelse. Mangler P, går det ud over resultaterne; '
                  'mangler A, bliver der kaos og manglende styring; mangler E, stivner virksomheden og '
                  'taber fremtiden; mangler I, falder organisationen fra hinanden i fraktioner. Pointen '
                  'er, at alle fire roller skal være dækket et sted i ledelsen, ellers opstår systematiske '
                  'svagheder.',
           'fisker': 'Om du kan koble en manglende rolle til en konkret organisatorisk svaghed.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Hofstedes kulturdimensioner',
  'fag': 'Kommunikation',
  'lag': [{'sp': 'Hvad er Hofstedes kulturdimensioner, og kan du nævne nogle af dem?',
           'arg': 'Hofstede beskriver nationale kulturer på en række dimensioner, bl.a. magtdistance '
                  '(accept af ulige magt), individualisme vs kollektivisme, maskulinitet vs femininitet, '
                  'usikkerhedsundvigelse (tolerance for usikkerhed) samt langtids- vs korttidsorientering. '
                  'Hver kultur scorer forskelligt og kan sammenlignes på akserne.',
           'fisker': 'Om du kan nævne dimensionerne og hvad de måler.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er Hofstedes model nyttig for en logistikøkonom, der arbejder med internationale '
                 'leverandører?',
           'arg': 'Fordi den hjælper med at forudse og forstå forskelle i forhandling, samarbejde og '
                  'kommunikation. Fx betyder høj magtdistance, at beslutninger træffes i toppen og man '
                  'taler til chefen, mens høj usikkerhedsundvigelse betyder krav om detaljerede kontrakter '
                  'og klare aftaler. Det gør samarbejdet på tværs af grænser mere effektivt og forebygger '
                  'misforståelser.',
           'fisker': 'Om du kan omsætte dimensionerne til konkret adfærd i international handel.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hofstede giver hvert land en score på hver dimension. Kan du så bruge en kollegas '
                 'landescore til at forudsige, hvordan netop han vil reagere?',
           'arg': 'Nej — det er en fælde. Hofstedes scorer er GENNEMSNIT for en hel nation, ikke en profil '
                  'af enkeltpersoner. At bruge en landescore på et individ er en økologisk fejlslutning: '
                  'der er stor spredning indenfor ethvert land, og personlighed, branche og erfaring '
                  'tæller. Modellen beskriver tendenser i en gruppe, ikke determinerer den enkelte. Brugt '
                  'på individer bliver den til stereotyper.',
           'fisker': 'Om du gennemskuer niveau-forvekslingen: nationsgennemsnit kan ikke uden videre '
                     'overføres til individet.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad er en væsentlig kritik af Hofstedes model ud over individ-problemet?',
           'arg': 'At den behandler nationer som ensartede og statiske kulturer, selvom lande rummer mange '
                  'subkulturer og forandrer sig over tid. Datagrundlaget (oprindeligt IBM-medarbejdere) er '
                  'også blevet kritiseret for ikke at være repræsentativt, og dimensionerne risikerer at '
                  'fastlåse kulturer i klichéer. Modellen er et nyttigt udgangspunkt, men ikke et facit.',
           'fisker': 'Om du kan løfte en bredere metodisk kritik: national homogenitet, statisk syn, '
                     'datagrundlag.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Bensaou-matrix',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad er det Bensaou-matrixen sætter op imod hinanden på sine to akser?',
           'arg': 'Bensaou måler køberens specifikke investeringer mod leverandørens specifikke '
                  'investeringer i relationen. De fire felter er market exchange (begge lavt), captive '
                  'buyer (køber har investeret meget, leverandør lidt), captive supplier (leverandør '
                  'meget, køber lidt) og strategic partnership (begge meget).',
           'fisker': 'At du kender akserne: hvem har bundet aktiver i relationen, ikke produktets '
                     'værdi/risiko.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor giver det mening at fokusere på hvem der har lavet investeringerne, frem for fx '
                 'hvad varen koster?',
           'arg': 'Fordi specifikke investeringer skaber afhængighed og dermed forhandlingsmagt. Den part '
                  'der har investeret aktiver, der ikke kan bruges andre steder, er bundet og sårbar. Det '
                  'forklarer magtbalancen i relationen bedre end varens pris, fordi det handler om hvem '
                  'der har mest at tabe ved et brud.',
           'fisker': 'At du forstår logikken: specifikke investeringer = lock-in = magtforskydning.',
           'alt': 'Du kan også argumentere med at investeringerne signalerer commitment og gør samarbejdet '
                  'mere stabilt over tid.',
           'snyd': False,
           'fakta': False},
          {'sp': 'En leverandør har investeret tungt i specialudstyr til netop os, mens vi som køber '
                 'næsten intet har bundet. Hvem sidder så stærkest, og hvilket felt er det?',
           'arg': 'Det er captive supplier, og det er KØBER der sidder stærkest, ikke leverandøren. Det '
                  'intuitive er at tro den der har investeret mest har mest magt, men det er omvendt: '
                  'leverandøren er låst fast og kan ikke bruge udstyret andre steder, så han er afhængig '
                  'af os. Vi kan presse pris og vilkår.',
           'fisker': 'Om du falder for at investering = magt. Det er afhængighed der afgør magten, og den '
                     'investerende part er den sårbare.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Er strategic partnership, hvor begge har investeret meget, så altid det bedste felt at '
                 'stræbe efter?',
           'arg': 'Nej. Partnerskab er dyrt og bindende, og det giver kun mening når varen er strategisk '
                  'vigtig og kompleks. For en simpel standardvare ville market exchange (begge lavt '
                  'investeret) være langt mere effektivt. Bensaous pointe er at felterne skal matche '
                  'relationens karakter, ikke at man skal op i partnerskab.',
           'fisker': 'At du ikke ser matrixen som en stige man skal klatre op ad, men som en '
                     'passende-match-model.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Single/dual/multiple/cross sourcing',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad er forskellen på single, dual og multiple sourcing?',
           'arg': 'Single sourcing er én leverandør til en vare (bevidst valg). Dual er to leverandører '
                  'til samme vare. Multiple er flere/mange leverandører til samme vare. Cross sourcing er '
                  'en mellemvej hvor man bruger forskellige leverandører på tværs af varer/regioner, så '
                  'hver leverandør kender produktet og kan træde til hvis en anden falder ud.',
           'fisker': 'At du kan placere antallet af leverandører pr. vare og kende cross som '
                     'backup-strategi.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor vælge single sourcing, når man jo gør sig sårbar ved kun at have én leverandør?',
           'arg': 'Single giver stordriftsfordele: større volumen til én leverandør betyder bedre pris, '
                  'tættere samarbejde, fælles udvikling og lavere transaktionsomkostninger. Man bytter '
                  'robusthed for effektivitet og dybde i relationen. Det er fornuftigt for varer hvor '
                  'samarbejde og kvalitet betyder mere end forsyningssikkerhed.',
           'fisker': 'At du kan forsvare fordelen (stordrift/relation) og er bevidst om prisen '
                     '(sårbarhed).',
           'alt': 'Man kan også vælge single fordi varen er så specialiseret at der reelt kun findes én '
                  'kompetent leverandør.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor så ikke bare altid sprede sig på mange leverandører for at være på den sikre '
                 'side?',
           'arg': 'Fordi multiple sourcing splitter volumen, så man mister mængderabatter og '
                  'forhandlingsstyrke, øger administrative omkostninger og får svagere relationer. '
                  'Spredning køber forsyningssikkerhed, men koster effektivitet. Det rette valg afhænger '
                  'af risiko og varens betydning, ikke af at sikkerhed altid er bedst.',
           'fisker': 'At du ser trade-off begge veje og ikke tror spredning er gratis.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': "En indkøber siger: 'Vi har to leverandører på varen, så vi er dual sourcing og dækket "
                 "mod nedbrud.' Hvad kan være galt i den konklusion?",
           'arg': 'To leverandører beskytter kun hvis de er reelt uafhængige. Hvis begge køber råvaren '
                  'samme sted, ligger i samme region ramt af samme strejke/katastrofe, eller den ene kun '
                  'har 5 procent af volumen, er man reelt single sourcing i forklædning. Dual på papiret '
                  'er ikke robusthed i praksis hvis risikoen er korreleret.',
           'fisker': 'Om du gennemskuer at antallet af kontrakter ikke er det samme som reel '
                     'risikospredning.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Exit vs voice',
  'fag': 'Strategi',
  'lag': [{'sp': 'Hvad betyder exit og voice i en leverandørrelation?',
           'arg': 'Exit er at forlade relationen — skifte til en anden leverandør når noget er galt. Voice '
                  'er at blive og give besked, forhandle og forsøge at forbedre relationen indefra. Det er '
                  'to forskellige reaktioner på utilfredshed.',
           'fisker': 'At du kender de to grundreaktioner: skift væk vs. forbedr.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvornår er voice det rigtige valg frem for bare at skifte leverandør?',
           'arg': 'Voice giver mening når skifteomkostningerne er høje, relationen er strategisk, '
                  'leverandøren er svær at erstatte, eller når problemet kan løses. Så er det billigere og '
                  'klogere at investere i at forbedre samarbejdet end at starte forfra med ny oplæring, '
                  'nye specifikke investeringer og ny tillid.',
           'fisker': 'At du kobler valget til skifteomkostninger og relationens værdi.',
           'alt': 'Voice signalerer også loyalitet og kan styrke relationen langsigtet, hvilket exit '
                  'aldrig gør.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor så ikke altid bruge exit-truslen — den giver jo magt i forhandlingen?',
           'arg': 'Exit-truslen virker kun hvis den er troværdig, altså hvis man faktisk har et alternativ '
                  'og lave skifteomkostninger. Ved høj afhængighed (captive buyer) er truslen tom, og '
                  'overforbrug af exit-trusler ødelægger tilliden og det langsigtede samarbejde. Voice '
                  'bevarer relationen, exit brænder broen.',
           'fisker': 'At du ser at exit-magt forudsætter reelle alternativer og har en pris på relationen.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvis en leverandør konstant svigter, er exit så ikke åbenlyst det eneste rigtige?',
           'arg': 'Ikke nødvendigvis. Hvis vi sidder fast som captive buyer med høje skifteomkostninger og '
                  'store specifikke investeringer, kan exit være dyrere end at fortsætte og bruge voice — '
                  "også selvom leverandøren svigter. Det intuitive 'svigt = skift' ignorerer at vores egen "
                  'indlåsning kan gøre exit til det dyreste valg. Først løses indlåsningen, så bliver exit '
                  'troværdig.',
           'fisker': 'Om du gennemskuer at svigt ikke automatisk gør exit billigst når man er låst inde.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'TCE vs netværksperspektiv',
  'fag': 'Strategi',
  'lag': [{'sp': 'Hvad er kernen i transaktionsomkostningsteorien (TCE) i forhold til indkøb?',
           'arg': 'TCE ser på omkostningerne ved selve transaktionen: at søge, forhandle, kontrollere og '
                  'håndhæve aftaler. Spørgsmålet er om man skal lave selv eller købe (make-vs-buy), og '
                  'svaret afhænger af transaktionsomkostninger, usikkerhed og specifikke investeringer. '
                  'Relationen ses dyadisk, altså mellem to parter.',
           'fisker': 'At du kender TCE som en omkostningsbaseret two-party-betragtning af køb vs. lav '
                     'selv.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad tilføjer netværksperspektivet, som TCE ikke fanger?',
           'arg': 'Netværksperspektivet ser virksomheden som en del af et net af relationer, ikke '
                  'isolerede to-parts-handler. Det fanger at relationer skaber værdi over tid gennem '
                  'tillid, læring, fælles innovation og at en leverandør er forbundet til andre. Værdi og '
                  'afhængigheder opstår i hele nettet, ikke kun i den enkelte transaktion.',
           'fisker': 'At du ser TCE som snæver/omkostningsfokuseret og netværk som '
                     'relationelt/værdiskabende.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor ikke bare nøjes med TCE — det er da mere konkret og målbart?',
           'arg': 'Fordi TCE undervurderer langsigtet relationsværdi: tillid, fælles udvikling og '
                  'indlejring i et netværk er svære at sætte tal på, men afgørende. Hvis man kun minimerer '
                  'transaktionsomkostninger, kan man skære relationer væk, der faktisk skaber strategisk '
                  'værdi. TCE er stærk på det målbare, blind på det relationelle.',
           'fisker': "At du kan kritisere TCE's blinde vinkel uden at forkaste den.",
           'alt': 'Man kan også sige de supplerer hinanden: TCE til struktur-beslutningen, netværk til at '
                  'forstå relationens udvikling.',
           'snyd': False,
           'fakta': False},
          {'sp': 'TCE siger: jo mere specifik en investering er, desto større risiko for opportunisme, så '
                 'lav hellere selv. Følger den anbefaling altid?',
           'arg': 'Nej. Set fra netværksperspektivet kan netop den specifikke, gensidige investering binde '
                  'parterne sammen og skabe et tæt, tillidsfuldt partnerskab i stedet for opportunisme. '
                  'Det TCE ser som en risiko der skal internaliseres, ser netværk som limen i en værdifuld '
                  'relation. Samme faktum, modsat konklusion.',
           'fisker': "Om du kan vende TCE's risikologik om og se specifik investering som relationelt "
                     'aktiv.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Ordervinder vs ordrekvalificerende',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er forskellen på et ordervindende og et ordrekvalificerende kriterium?',
           'arg': 'Ordrekvalificerende kriterier er dem man skal opfylde bare for at komme i betragtning — '
                  'adgangsbilletten. Ordervindende kriterier er dem der får kunden til at vælge netop os '
                  'frem for konkurrenterne. Begreberne stammer fra Terry Hill.',
           'fisker': 'At du kender skellet: kvalificerende = kom med i feltet, vindende = vind ordren.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er det vigtigt at skelne mellem de to, når man lægger sin konkurrencestrategi?',
           'arg': 'Fordi de kræver forskellig indsats. På kvalificerende kriterier skal man nå et '
                  'acceptabelt niveau, ikke mere — at overpræstere her giver ingen ekstra ordrer. På '
                  'vindende kriterier skal man være bedre end konkurrenterne. Skellet fortæller hvor man '
                  'skal lægge sine ressourcer for at vinde frem for bare at deltage.',
           'fisker': 'At du kobler skellet til ressourceallokering: hvor giver ekstra indsats faktisk '
                     'ordrer.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvis pris er det der vinder ordrer i vores marked, skal vi så ikke bare presse prisen så '
                 'langt ned som muligt?',
           'arg': 'Ikke uden videre. Selvom pris er ordervinder, må man stadig opfylde de kvalificerende '
                  'kriterier som kvalitet og leveringstid — skærer man dem væk for at presse prisen, ryger '
                  'man ud af feltet helt. Lav pris vinder kun blandt dem der allerede er kvalificerede.',
           'fisker': 'Om du husker at ordervinderen kun virker når de kvalificerende stadig er opfyldt.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Er et ordervindende kriterium så noget der ligger fast for produktet?',
           'arg': 'Nej, det skifter over tid og mellem markeder. Et kriterium der i dag vinder ordrer (fx '
                  'hurtig levering) kan i morgen blive blot kvalificerende, når konkurrenterne har '
                  'indhentet det — så skal man finde en ny vinder. Det er dynamisk, ikke en fast egenskab, '
                  'og det tvinger til løbende revurdering.',
           'fisker': 'At du ser kriterierne som dynamiske: dagens vinder bliver morgendagens '
                     'adgangsbillet.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Leverandørevaluering (vægtet score)',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvordan fungerer en vægtet scoremodel til at vælge mellem leverandører?',
           'arg': 'Man opstiller en række kriterier (pris, kvalitet, leveringssikkerhed osv.), giver hvert '
                  'kriterium en vægt efter vigtighed (vægtene summerer typisk til 100 procent), scorer '
                  'hver leverandør på hvert kriterium, ganger score med vægt og lægger sammen. '
                  'Leverandøren med højest samlet vægtet score vinder.',
           'fisker': 'At du kan beskrive mekanikken: vægt gange score, summeret pr. leverandør.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor bruge vægte i stedet for bare at lægge scorerne sammen ligeligt?',
           'arg': 'Fordi kriterierne ikke er lige vigtige. For en kritisk komponent vejer '
                  'leveringssikkerhed og kvalitet tungere end pris. Vægtene tvinger os til at gøre '
                  'prioriteringen eksplicit og gennemsigtig, så valget afspejler virksomhedens faktiske '
                  'strategi i stedet for at behandle alt som lige vigtigt.',
           'fisker': 'At du forstår at vægte gør prioritering eksplicit og strategisk.',
           'alt': 'Vægtene gør også beslutningen lettere at forsvare og diskutere bagefter, fordi '
                  'præmisserne er synlige.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Leverandør A får den højeste samlede score. Betyder det automatisk at vi skal vælge A?',
           'arg': 'Ikke nødvendigvis. Modellen kan skjule at A scorer uacceptabelt lavt på et '
                  'must-have-kriterium — fx dumper kvalitetskravet — men reddes op af en høj pris-score. '
                  'En høj totalscore kan dække over et knock-out. Man bør sætte minimumstærskler på '
                  'kritiske kriterier, ikke kun se på totalen.',
           'fisker': 'Om du gennemskuer at en høj sum kan camouflere et fald på et kritisk kriterium.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Er en vægtet scoremodel så en objektiv metode, fordi den giver konkrete tal?',
           'arg': 'Nej, kun tilsyneladende. Både valget af kriterier, vægtene og scorerne er subjektive '
                  'skøn — tallene giver et skin af objektivitet. Modellens styrke er at den gør de '
                  'subjektive valg eksplicitte og diskuterbare, ikke at den fjerner subjektiviteten. '
                  'Ændrer man vægtene lidt, kan vinderen skifte.',
           'fisker': 'At du ikke forveksler tal med objektivitet og kender modellens følsomhed.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Make-vs-buy',
  'fag': 'Værdikæde',
  'lag': [{'sp': 'Hvad er en make-vs-buy-beslutning?',
           'arg': 'Det er beslutningen om virksomheden selv skal producere en vare eller ydelse (make) '
                  'eller købe den udefra hos en leverandør (buy). Det er en grundlæggende afgrænsning af '
                  'hvor virksomhedens egne aktiviteter slutter og markedet begynder.',
           'fisker': 'At du kender beslutningen som grænsedragning mellem egen produktion og indkøb.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvilke argumenter taler for at købe (buy) frem for selv at lave?',
           'arg': 'Buy giver adgang til leverandørens stordrift, specialisering og lavere '
                  'enhedsomkostninger, fjerner behov for egne investeringer i kapacitet, giver '
                  'fleksibilitet og lader os fokusere på vores kernekompetencer. Man køber det andre laver '
                  'bedre og billigere, og holder kapitalen fri.',
           'fisker': 'At du kender buy-fordelene: stordrift, fleksibilitet, fokus på kerne.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor så ikke bare outsource alt der kan købes billigere udefra?',
           'arg': 'Fordi nogle aktiviteter er strategiske kernekompetencer der giver konkurrencefordel, og '
                  'dem mister man kontrol over og opbygger afhængighed af ved at købe. Buy øger også '
                  'transaktionsomkostninger og risiko for opportunisme ved specifikke investeringer. Man '
                  'beholder selv det der er kritisk eller svært at styre via marked.',
           'fisker': 'At du afvejer kerne/kontrol/transaktionsomkostninger mod den umiddelbare '
                     'prisbesparelse.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'En komponent kan købes billigere udefra end vi selv kan lave den. Burde vi så altid '
                 'købe?',
           'arg': 'Ikke nødvendigvis. Sammenligningen skal bygge på relevante omkostninger, ikke fulde '
                  'enhedsomkostninger. Hvis vi har ledig kapacitet, forsvinder de faste omkostninger ikke '
                  'ved at outsource — så skal buy-prisen kun sammenlignes med de variable omkostninger ved '
                  'selv at lave. Desuden tæller transaktionsomkostninger og tab af kompetence med. Den '
                  'lavere indkøbspris kan være en fælde.',
           'fisker': 'Om du skelner relevante/variable omkostninger fra fulde og ikke hopper på den '
                     'billige stykpris.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Genbestillingspunkt / ROP-tankegang',
  'fag': 'Logistik',
  'lag': [{'sp': 'Hvad er et genbestillingspunkt (ROP), og hvad sker der når lageret rammer det?',
           'arg': 'Genbestillingspunktet er det lagerniveau hvor man udløser en ny bestilling. Når '
                  'beholdningen falder til ROP, sender man en ordre, så den nye leverance ankommer netop '
                  'inden lageret slipper op. ROP er typisk forbrug i leveringstiden plus et '
                  'sikkerhedslager.',
           'fisker': 'At du kan definere ROP som triggerniveauet og kende formlen forbrug i leveringstid '
                     'plus buffer.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor bestiller man ved et bestemt lagerniveau frem for fx på en fast dato hver måned?',
           'arg': 'Fordi ROP reagerer på faktisk forbrug. Sælger man hurtigere end ventet, rammer man ROP '
                  'tidligere og bestiller før — det beskytter mod udsolgt. En fast dato ignorerer at '
                  'forbruget svinger. ROP-tankegangen kobler bestillingen til det reelle træk på lageret, '
                  'ikke til kalenderen.',
           'fisker': 'At du ser ROP som forbrugsstyret og dermed mere robust over for udsving end fast '
                     'interval.',
           'alt': 'Et fast interval kan dog være lettere at administrere og samordne med leverandørens '
                  'leveringsplan, så valget afhænger af situationen.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor lægger man et sikkerhedslager oven i forbruget i leveringstiden — er '
                 'gennemsnitsforbruget ikke nok?',
           'arg': 'Nej, fordi både forbrug og leveringstid svinger. Sætter man ROP til præcis '
                  'gennemsnitsforbruget i leveringstiden, løber man tør halvdelen af gangene, hver gang '
                  'efterspørgslen eller leveringstiden er over gennemsnit. Sikkerhedslageret er bufferen '
                  'mod den variation og bestemmer servicegraden.',
           'fisker': 'At du forstår at gennemsnit dækker kun halvdelen af tilfældene, og buffer dækker '
                     'variationen.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvis leverandøren halverer sin leveringstid, kan vi så bare sænke vores '
                 'genbestillingspunkt tilsvarende?',
           'arg': 'Delvist. Den del af ROP der dækker forbrug i leveringstiden falder, ja. Men '
                  'sikkerhedslageret afhænger også af usikkerheden i leveringstiden, og er den nye, '
                  'kortere leveringstid mere upålidelig, kan bufferen skulle op igen. Man kan ikke bare '
                  'skalere hele ROP lineært med leveringstiden — gennemsnit og variation skal behandles '
                  'hver for sig.',
           'fisker': 'Om du adskiller cyklusdelen (skalerer med leveringstid) fra sikkerhedsdelen '
                     '(afhænger af variation).',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'ABC-analyse (logikken bag)',
  'fag': 'Logistik',
  'lag': [{'sp': 'Hvad går en ABC-analyse ud på, og hvad kendetegner en A-vare?',
           'arg': 'ABC-analysen inddeler varer/lager i tre grupper efter deres andel af den samlede værdi '
                  '(typisk forbrugsværdi). A-varer er de få varer der står for den største del af værdien, '
                  'B er mellemgruppen, og C er de mange varer der kun udgør en lille værdiandel. A = få '
                  'varer, stor værdi.',
           'fisker': 'At du kender A = få varer/stor værdi og grundinddelingen efter værdiandel.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad er pointen med at dele varerne op på den måde — hvilken logik ligger bag?',
           'arg': 'Logikken er Pareto-princippet: en lille andel af varerne står for en stor andel af '
                  'værdien. Derfor skal styringsindsatsen koncentreres om A-varerne (tæt kontrol, hyppig '
                  'opfølgning), mens C-varerne kan styres enkelt og billigt. Man bruger sin begrænsede '
                  'styringstid der hvor pengene er.',
           'fisker': 'At du kobler ABC til Pareto og til differentieret styringsindsats.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Bør man så altid skære hårdt ned på lageret af C-varer, siden de næsten ingen værdi '
                 'udgør?',
           'arg': 'Ikke nødvendigvis. C-varer er billige at lægge på lager, så det koster lidt at have '
                  'rigeligt af dem, mens en udsolgt C-vare kan stoppe en hel produktion eller ordre. '
                  'Derfor giver det ofte mening at have generøse buffere på netop C-varer. Lav værdiandel '
                  'betyder ikke lav kritikalitet.',
           'fisker': 'Om du gennemskuer at lav værdi ikke er lig med uvigtig — kritikalitet er en anden '
                     'akse.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Er det altid den dyreste vare der er en A-vare?',
           'arg': 'Nej. ABC bygger normalt på forbrugsværdi, altså stykpris gange forbrug/omsætning — ikke '
                  'stykpris alene. En billig vare der sælges i kæmpe mængder kan sagtens være en A-vare, '
                  'mens en meget dyr vare der næsten aldrig bruges ender som C. Det er den samlede '
                  'værdistrøm, ikke prisskiltet, der afgør gruppen.',
           'fisker': 'At du ved klassificeringen sker på forbrugsværdi (pris gange mængde), ikke på '
                     'stykpris.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Ordretyper: MTS / ATO / MTO / ETO',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er forskellen på MTS og MTO?',
           'arg': 'MTS (Make-to-Stock) producerer mod lager FØR ordren kommer — kunden køber fra hylden. '
                  'MTO (Make-to-Order) starter først produktionen NÅR ordren er modtaget. ATO '
                  '(Assemble-to-Order) ligger imellem: komponenter ligger på lager, men selve samlingen '
                  'sker først ved ordre. ETO (Engineer-to-Order) går længst tilbage: selve '
                  'designet/konstruktionen starter ved ordre.',
           'fisker': 'Om du kender ordre-afkoblingspunktet (hvor i kæden kundeordren rammer ind).',
           'alt': 'Kan også forklares via OPP/decoupling point — hvor langt kundeordren trænger ind i '
                  'værdikæden.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvilken ordretype giver den korteste leveringstid til kunden, og hvilken giver det '
                 'laveste færdigvarelager?',
           'arg': 'De to ting trækker hver sin vej. MTS giver KORTEST leveringstid (varen ligger klar), '
                  'men HØJEST færdigvarelager. MTO giver LAVT (ofte intet) færdigvarelager, men LANG '
                  'leveringstid, fordi produktionen først starter ved ordre. Man kan altså ikke få begge '
                  'dele — det er en afvejning mellem lagerbinding og responstid.',
           'fisker': "At du ser trade-off'et: kort leveringstid og lavt FVL er modsatrettede mål.",
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'En virksomhed med stor produktvariation og uforudsigelig efterspørgsel vil gerne have '
                 'både kort leveringstid OG lavt lager. Hvilken type bør de vælge?',
           'arg': 'Fælden er at vælge enten MTS eller MTO. Det rigtige svar er ofte ATO '
                  '(Assemble-to-Order): man lagerfører standard-komponenter (lavt FVL på FÆRDIGvarer, da '
                  'man kun binder kapital i moduler) og samler først ved ordre. Variationen skabes sent i '
                  'kæden (postponement), så man får mange varianter ud af få komponenter med kort '
                  'samletid. Det løser netop kombinationen af variation, lavt FVL og rimelig leveringstid.',
           'fisker': "Om du kender postponement/ATO som svaret på 'variation + lavt lager + hurtig "
                     "levering'.",
           'alt': 'Kan også begrundes via modularisering: få fælleskomponenter giver mange varianter '
                  '(variantstyring).',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Lean vs. Fordisme',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er kerneforskellen på fordisme og Lean?',
           'arg': 'Fordisme (Henry Ford, samlebånd) handler om masseproduktion af ÉT standardprodukt i '
                  'store serier for at presse stykomkostningen ned via stordriftsfordele. Lean (Toyota) '
                  'handler om at fjerne spild (muda) og producere det kunden faktisk efterspørger, i '
                  'mindre partier, med fokus på flow og kvalitet frem for rå volumen.',
           'fisker': 'At du kender de to produktionsfilosofier og deres tidsånd.',
           'alt': "Kan vinkles som 'economies of scale' (Ford) vs. 'economies of flow/flexibilitet' "
                  '(Lean).',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor gik man fra Ford-tankegangen til Lean — hvad kunne fordismen ikke?',
           'arg': "Fordismen var effektiv så længe kunden ville have det samme produkt (Ford: 'any color "
                  "as long as it's black'). Men markedet krævede variation og hyppige skift, og fordismens "
                  'store serier gav store lagre, lange omstillinger og meget bundet kapital. Lean svarer '
                  'på det med små partier, hurtige omstillinger (SMED) og træk fra kunden, så man kan '
                  'levere variation uden at drukne i lager.',
           'fisker': 'At du forstår markedsændringen (fra standard til variation) som driveren bag '
                     'skiftet.',
           'alt': 'Kan også begrundes med kvalitet: Lean bygger kvalitet ind (Jidoka), mens fordismens '
                  'efterkontrol gav dyr omkald.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Lean betyder altså at man altid skal køre med så lille lager som muligt — er det '
                 'rigtigt?',
           'arg': 'Nej, det er fælden. Lean handler om at fjerne SPILD, ikke om nul lager for enhver pris. '
                  'Et bevidst buffer- eller sikkerhedslager foran en flaskehals eller mod en ustabil '
                  'leverandør er IKKE spild — det beskytter flowet. At skære lageret blindt kan skabe stop '
                  "og leveringssvigt, hvilket er dyrere end lageret. Lean er 'det rigtige lager det "
                  "rigtige sted', ikke 'mindst muligt lager overalt'.",
           'fisker': 'Om du kan skelne spild fra nødvendig buffer — at Lean ikke er lig med '
                     'nul-lager-dogmatik.',
           'alt': 'Kan også begrundes via flaskehalsteori: bufferen foran flaskehalsen beskytter netop det '
                  'dyreste punkt.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'MRP (skub) vs. JIT (træk)',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er forskellen på et skub- og et træk-styret produktionssystem?',
           'arg': "MRP er et SKUB-system: man planlægger ud fra en prognose og en stykliste, og 'skubber' "
                  'materialer ind i produktionen efter planen, uanset om næste led er klar. JIT/Kanban er '
                  'et TRÆK-system: et led producerer først, når det næste led signalerer behov (træk fra '
                  'kunden bagfra). Skub er prognosestyret, træk er forbrugsstyret.',
           'fisker': 'At du kender skub/træk-skellet og hvad der udløser produktion i hver.',
           'alt': 'Kan forklares via Kanban-kort som det fysiske træk-signal.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor ikke bare bruge JIT/træk overalt, hvis det giver lavere lager?',
           'arg': 'Træk forudsætter stabil og nogenlunde jævn efterspørgsel samt pålidelige leverandører — '
                  'ellers tømmes bufferne og produktionen stopper. MRP/skub er stærkere ved svingende '
                  'eller sæsonbetonet efterspørgsel, lange leverandør-ledetider og komplekse styklister, '
                  'hvor man MÅ planlægge frem i tid. Mange bruger derfor en hybrid: MRP til den '
                  'overordnede materialeplan, Kanban/træk på gulvet hvor flowet er stabilt.',
           'fisker': 'At du kender forudsætningerne for træk og hvornår skub er nødvendigt.',
           'alt': 'Kan også begrundes via afkoblingspunktet: skub før punktet (prognose), træk efter '
                  '(kundeordre).',
           'snyd': False,
           'fakta': False},
          {'sp': 'Et træk-system har jo intet centralt overblik — så hvis efterspørgslen pludselig stiger '
                 'kraftigt, reagerer det hurtigere end MRP, ikke?',
           'arg': 'Det intuitive svar er fælden. Et rent træk-system reagerer netop LANGSOMT på et brat, '
                  'vedvarende efterspørgselshop, fordi signalet skal forplante sig led for led bagud '
                  'gennem hele kæden (hvert Kanban-kort skal tømmes før næste led trækker). Et '
                  'MRP/skub-system kan derimod planlægge fremad ud fra en opdateret prognose og opbygge '
                  'kapacitet/lager FØR spidsen rammer. Træk er overlegent ved STABIL efterspørgsel, ikke '
                  'ved brat opskalering. Derfor svigter rene træk-systemer ofte ved store, varige '
                  'efterspørgselsskift.',
           'fisker': 'Om du kan vende intuitionen: træk er ikke pr. definition mest responsivt — ved store '
                     'skift vinder fremadrettet planlægning.',
           'alt': 'Kan også kobles til bullwhip: rent forbrugstræk uden delt prognose kan forstærke '
                  'udsving opstrøms.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Produktionsformer: jobshop / serie / flow / projekt',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvilke grundlæggende produktionsformer findes der, og hvad kendetegner dem?',
           'arg': 'Projektproduktion: ét unikt, stort produkt (bro, skib) — produktet står stille, '
                  'ressourcer kommer til. Jobshop/enkeltstyk: små mængder, høj variation, fleksible '
                  'maskiner grupperet efter funktion. Serieproduktion: gentagne partier af samme vare. '
                  'Flow/procesproduktion: stor, ensartet volumen i en kontinuerlig linje (fx mejeri, '
                  'bryggeri). Variationen falder og volumen stiger fra projekt mod flow.',
           'fisker': 'At du kender de fire former og kan placere dem på volumen/variation-aksen.',
           'alt': 'Kan struktureres via produkt-proces-matricen (Hayes & Wheelwright).',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor vælger en virksomhed jobshop frem for flow, når flow giver lavere '
                 'stykomkostning?',
           'arg': 'Fordi jobshop matcher HØJ variation og LAVE mængder. Flowlinjen er billig pr. stk, men '
                  'kun hvis man kan holde den fyldt med stort set samme produkt; den er stiv og dyr at '
                  'stille om. Med mange varianter i små serier ville en flowlinje stå stille eller kræve '
                  'konstant omstilling. Jobshoppens fleksible, funktionsopdelte maskiner kan håndtere '
                  'variationen — man bytter altså lav stykpris for fleksibilitet.',
           'fisker': 'At du forbinder valget med volumen og variation, ikke kun med stykpris.',
           'alt': 'Kan begrundes via produkt-proces-matricen: man skal ligge på diagonalen for ikke at '
                  'miste enten fleksibilitet eller effektivitet.',
           'snyd': False,
           'fakta': False},
          {'sp': 'En virksomhed ligger i serieproduktion, men efterspørgslen vokser støt mod én '
                 'dominerende vare. De overvejer at blive i serie for at bevare fleksibiliteten. Klog '
                 'beslutning?',
           'arg': "Her er fælden 'fleksibilitet er altid godt'. Hvis volumen er høj og variationen reelt "
                  'er faldet til én dominerende vare, koster det at blive i serie: man betaler for '
                  'fleksibilitet man ikke længere bruger (omstillinger, mellemlagre, lav udnyttelse). '
                  'Produkt-proces-matricen siger man skal følge diagonalen — ved høj volumen/lav variation '
                  'bør man rykke mod flow for at få stykomkostningen ned. At blive i serie er kun klogt, '
                  'hvis variationen forventes at vende tilbage. Ellers binder man unødig kapital og taber '
                  'konkurrenceevne.',
           'fisker': 'Om du tør konkludere at mere fleksibilitet kan være forkert — at man skal følge '
                     'diagonalen i matricen.',
           'alt': 'Kan også begrundes rent økonomisk: tabt skalafordel = højere stykpris end konkurrenter '
                  'på samme vare.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Produktionslayout',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvilke hovedtyper af produktionslayout findes der?',
           'arg': 'Funktionslayout (proceslayout): maskiner grupperet efter funktion — alle drejebænke for '
                  'sig — passer til jobshop/høj variation. Linjelayout (produktlayout): maskiner stillet i '
                  'den rækkefølge produktet bearbejdes — passer til flow/høj volumen. Fast '
                  'position/projektlayout: produktet står stille, ressourcer kommer til (skib, bro). '
                  'Celle-layout: en mellemform, hvor maskiner grupperes om en produktfamilie for at få '
                  'flowfordele ved moderat variation.',
           'fisker': 'At du kender layouttyperne og kan koble dem til produktionsformerne.',
           'alt': 'Cellelayout kan fremhæves som Lean-svaret der kombinerer flow og fleksibilitet.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor vælge funktionslayout, når linjelayout giver kortere gennemløbstid?',
           'arg': 'Fordi funktionslayout passer til høj variation og svingende mængder. Linjelayoutet er '
                  'hurtigt, men låst til én produktsekvens; ved mange forskellige varer ville linjen kræve '
                  'konstant omstilling eller stå tom. Funktionslayoutet er fleksibelt — samme maskingruppe '
                  'kan betjene mange forskellige ordrer — men prisen er længere transportveje, mere '
                  'mellemlager (WIP) og længere gennemløbstid. Man vælger altså fleksibilitet frem for '
                  'hastighed.',
           'fisker': "At du ser trade-off'et mellem fleksibilitet (funktion) og hastighed/lavt WIP "
                     '(linje).',
           'alt': 'Kan begrundes via materialeflow: funktionslayout giver krydsende flow, linje giver lige '
                  'flow.',
           'snyd': False,
           'fakta': False},
          {'sp': 'En virksomhed vil minimere gennemløbstiden og vælger derfor det reneste linjelayout. Er '
                 'det altid den rigtige vej til kort gennemløbstid?',
           'arg': 'Ikke nødvendigvis — det er fælden. Et rent linjelayout er kun hurtigt, hvis '
                  'arbejdsstationerne er BALANCEREDE; er de ikke det, sætter den langsomste station '
                  '(flaskehalsen) takten, og WIP hober sig op foran den. Ved høj produktvariation kan et '
                  'celle-layout faktisk give kortere reel gennemløbstid, fordi man slipper for de '
                  'omstillinger og det krydsende flow, en linje med mange varianter ville kræve. Kort '
                  "gennemløbstid afhænger af balancering og variation, ikke kun af at vælge 'linje'.",
           'fisker': 'Om du kender linjebalancering og flaskehalsen som det der reelt bestemmer linjens '
                     'hastighed.',
           'alt': 'Kan kobles til cellelayout/Lean: flow opnås bedre via produktfamilier end via én lang '
                  'stiv linje.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'S&OP: Level vs. Chase',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er forskellen på en Level- og en Chase-strategi i salgs- og driftsplanlægningen?',
           'arg': 'Level-strategi: man holder produktionen og arbejdsstyrken KONSTANT over perioden, og '
                  'lader lageret svinge — man bygger op i lavsæson og tærer ned i højsæson. '
                  'Chase-strategi: man lader produktionen FØLGE efterspørgslen, så arbejdsstyrke og '
                  'kapacitet skaleres op og ned i takt med behovet, og lageret holdes minimalt.',
           'fisker': 'At du præcist kan sige hvad der holdes konstant (Level = arbejdsstyrke/produktion) '
                     'og hvad der svinger.',
           'alt': 'Kan illustreres på en kurve: Level = flad produktionslinje, Chase = produktion der '
                  'følger efterspørgselskurven.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvornår vælger man Level frem for Chase?',
           'arg': 'Level passer, når det er dyrt eller svært at skalere arbejdsstyrken op og ned (oplærte '
                  'specialister, fagforeningsaftaler, høje hyre/fyre-omkostninger), og når '
                  'lageromkostningen er lav og varen kan lagres. Man betaler så for lager mod at få en '
                  'stabil, effektiv produktion og tilfredse medarbejdere. Chase passer omvendt, når lager '
                  'er dyrt eller umuligt (ferskvarer, services) og arbejdsstyrken er let at skalere '
                  '(sæsonarbejdere, vikarer).',
           'fisker': 'At du kobler valget til omkostningerne ved at skalere arbejdsstyrke vs. ved at holde '
                     'lager.',
           'alt': 'Kan vinkles via varens lagerbarhed: services kan ikke lagres, så de tvinges mod Chase.',
           'snyd': False,
           'fakta': False},
          {'sp': 'En virksomhed med kraftig sæson vil minimere omkostningerne og vælger derfor Chase for '
                 'at undgå dyrt sæsonlager. Er det automatisk det billigste?',
           'arg': 'Ikke nødvendigvis — det er fælden. Chase sparer lager, MEN flytter omkostningen over på '
                  'hyppig op- og nedskalering: overarbejde og indlejring i top, ledig kapacitet og '
                  'afskedigelser i bund, oplæringsomkostninger, kvalitetstab og tabt know-how. Ved store, '
                  'brå sæsonsving kan summen af disse skalerings-omkostninger overstige lageromkostningen '
                  'ved Level. Det billigste er ofte en HYBRID — en stabil grundbemanding (Level) suppleret '
                  "med fleksibel kapacitet i top. Man kan altså ikke konkludere 'Chase = billigst' bare "
                  'fordi lageret forsvinder.',
           'fisker': 'Om du kan se de skjulte omkostninger ved Chase og foreslå en hybrid frem for at '
                     'vælge rent.',
           'alt': 'Kan begrundes via medarbejderperspektiv: konstant hyre/fyre koster goodwill, kvalitet '
                  'og oplæring — bløde omkostninger der sjældent står i regnearket.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'OEE — de tre faktorer',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad står OEE for, og hvordan regnes det?',
           'arg': 'OEE = Overall Equipment Effectiveness, et mål for hvor effektivt en maskine/linje '
                  'udnyttes. Det er produktet af tre faktorer: Tilgængelighed gange Ydelse gange Kvalitet. '
                  'Tilgængelighed = hvor stor del af planlagt tid maskinen faktisk kører (tab: nedbrud, '
                  'omstilling). Ydelse = hvor tæt på maksimal hastighed den kører (tab: småstop, langsom '
                  'drift). Kvalitet = andelen af gode emner (tab: kassation, omarbejde).',
           'fisker': 'At du kan formlen Tilgængelighed x Ydelse x Kvalitet og ved hvad hver faktor måler.',
           'alt': "Kan kobles til 'six big losses' — de seks tabstyper bag de tre faktorer.",
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor gange de tre faktorer sammen i stedet for at lægge dem sammen eller tage et '
                 'gennemsnit?',
           'arg': 'Fordi tabene rammer i kæde — de virker oven i hinanden. Hvis maskinen kun er '
                  'tilgængelig 90 % af tiden, kun kører 90 % hastighed og kun laver 90 % gode emner, så er '
                  'den reelle effektivitet 0,9 x 0,9 x 0,9 = ca. 73 %, ikke 90 %. Et gennemsnit ville '
                  'skjule, at hvert tab æder af resultatet fra det forrige. Multiplikationen viser den '
                  "ærlige, samlede udnyttelse — og at selv 'pæne' enkelttal giver et beskedent samlet OEE.",
           'fisker': 'At du forstår hvorfor det er multiplikativt — tabene forstærker hinanden.',
           'alt': 'Kan illustreres talmæssigt med 90/90/90-eksemplet for at vise effekten.',
           'snyd': False,
           'fakta': False},
          {'sp': 'To forbedringsforslag: hæv tilgængeligheden fra 95 % til 98 %, ELLER hæv kvaliteten fra '
                 '80 % til 88 %. Begge er +3 til +8 procentpoint. Hvilket løfter OEE mest?',
           'arg': 'Fælden er at sammenligne procentpoint direkte. Det der tæller er den RELATIVE '
                  'forbedring, fordi faktorerne ganges. Tilgængelighed 95→98 er en faktorforbedring på '
                  '98/95 ≈ +3,2 %. Kvalitet 80→88 er 88/80 = +10 %. Kvalitetsforslaget løfter OEE ca. tre '
                  "gange så meget, selvom 'kun' den lave faktor flyttes. Pointen: man får mest ved at "
                  'angribe den SVAGESTE faktor, fordi den relative gevinst er størst der. Procentpoint kan '
                  'altså narre — kig på den relative ændring og på hvilken faktor der er lavest.',
           'fisker': 'Om du regner relativt (forholdstal), ikke i rå procentpoint, og angriber den '
                     'svageste faktor.',
           'alt': 'Kan kobles til flaskehalstankegang: forbedr den faktor der er den reelle begrænsning, '
                  'ikke den der allerede er høj.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'OTIF / Perfect Order',
  'fag': 'Værdikæde',
  'lag': [{'sp': "Hvad betyder OTIF, og hvad er en 'perfect order'?",
           'arg': 'OTIF = On Time In Full: andelen af ordrer der leveres både til den aftalte tid (On '
                  "Time) OG i fuld, korrekt mængde (In Full). En 'perfect order' går videre og kræver "
                  'typisk fire ting opfyldt samtidig: rettidig, komplet, ubeskadiget OG med korrekt '
                  'dokumentation/faktura. Begge er leveringsservice-mål, der ser leverancen fra KUNDENS '
                  'side.',
           'fisker': 'At du kender de to dimensioner i OTIF og at perfect order tilføjer skade- og '
                     'dokumentationskrav.',
           'alt': 'Kan kobles til leveringsservice-elementerne (leveringstid, -sikkerhed, -fleksibilitet).',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor måle OTIF samlet i stedet for bare at måle leveringstid alene?',
           'arg': 'Fordi en ordre kun er god for kunden, hvis ALT passer. En leverance der er til tiden, '
                  'men mangler halvdelen af varerne, er ubrugelig — og en komplet leverance der kommer for '
                  'sent kan stoppe kundens produktion. Ved at kræve On Time OG In Full samtidig fanger '
                  'OTIF kundens reelle oplevelse, hvor enkeltmål kan se pæne ud hver for sig og alligevel '
                  'dække over dårlig service.',
           'fisker': 'At du forstår at OTIF måler den samlede kundeoplevelse, ikke et delaspekt.',
           'alt': 'Kan begrundes med at delmål kan optimeres hver for sig uden at kunden får en hel, '
                  'brugbar leverance.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Tre delprocesser har hver 95 % succesrate (tid, mængde, skadefri). Betyder det at '
                 'OTIF/perfect order også er omkring 95 %?',
           'arg': 'Nej — det er fælden. Når en perfekt ordre kræver at ALLE krav er opfyldt samtidig, '
                  'ganges sandsynlighederne: 0,95 x 0,95 x 0,95 ≈ 0,857, altså kun ca. 86 %. Med en fjerde '
                  'dimension (dokumentation) på 95 % bliver det ca. 81 %. Pointen er at sammensatte '
                  'servicemål falder hurtigt, fordi hvert led æder af de andre — ligesom OEE. Derfor '
                  'virker en perfect-order-score altid lavere og hårdere end de enkelte delmål, og man må '
                  'ikke aflæse helheden ud fra ét pænt deltal. (Forudsætter at delprocesserne er '
                  'uafhængige; er fejlene korrelerede, kan tallet være lidt højere.)',
           'fisker': "Om du kan gange delsandsynlighederne og ser at et sammensat 'alt-skal-passe'-mål "
                     'bliver markant lavere.',
           'alt': 'Kan kobles til OEE-logikken: samme multiplikative effekt rammer alle '
                  "'alle-krav-opfyldt'-mål.",
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Knap kapacitet / flaskehals',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er en flaskehals i en produktionslinje?',
           'arg': 'En flaskehals er den arbejdsstation eller ressource med den laveste kapacitet i forhold '
                  'til belastningen — det punkt hvor flowet snævrer ind. Det er flaskehalsen, der sætter '
                  'hele linjens output: linjen kan aldrig producere hurtigere end sit langsomste led, '
                  'uanset hvor hurtigt resten kører.',
           'fisker': "At du kender definitionen og pointen 'flaskehalsen bestemmer linjens samlede "
                     "output'.",
           'alt': 'Kan kobles til Theory of Constraints (Goldratt) og dens fem fokuseringstrin.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Når der er knaphed på flaskehalsens kapacitet og flere produkter slås om den, hvordan '
                 'prioriterer man så, hvad der skal produceres?',
           'arg': 'Man prioriterer ikke efter højeste dækningsbidrag pr. styk, men efter dækningsbidrag '
                  'pr. FLASKEHALSTIME. Det er flaskehalstiden der er den knappe ressource, så man skal '
                  'tjene mest muligt pr. minut på flaskehalsen. Et produkt med lavere DB pr. stk kan '
                  'sagtens være bedre, hvis det belaster flaskehalsen mindre og dermed giver højere DB pr. '
                  'flaskehalstime.',
           'fisker': 'At du prioriterer efter DB pr. flaskehalstime — den knappe ressource — ikke pr. '
                     'styk.',
           'alt': "Kan begrundes via Theory of Constraints: 'exploit the constraint' — få mest muligt ud "
                  'af begrænsningen.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Produkt A har det klart højeste dækningsbidrag pr. styk. Bør virksomheden så fylde '
                 'flaskehalsens tid med produkt A?',
           'arg': 'Ikke nødvendigvis — det er fælden. Højeste DB pr. styk er irrelevant, hvis A også '
                  'sluger meget flaskehalstid. Hvis produkt B har lavere DB pr. styk, men kun belaster '
                  'flaskehalsen halvt så meget, kan B give højere DB pr. flaskehalstime og dermed mere '
                  'samlet dækningsbidrag. Eksempel: A = 300 kr/stk men 30 min på flaskehalsen = 10 kr/min; '
                  'B = 200 kr/stk men 10 min = 20 kr/min. B vinder. Man skal altid omregne til DB pr. '
                  'flaskehalstime — DB pr. styk alene fører til forkert prioritering, når kapaciteten er '
                  'knap.',
           'fisker': "Om du afviser 'højest DB pr. styk' og omregner til DB pr. flaskehalstime med et "
                     'taleksempel.',
           'alt': 'Kan udvides: er flaskehalsen IKKE flaskehals (rigelig kapacitet), gælder DB pr. styk '
                  'igen — så pas på at faldgruben kun gælder ved knaphed.',
           'snyd': True,
           'fakta': False}]},
 {'emne': "Little's Law (fortolkning)",
  'fag': 'Produktion',
  'lag': [{'sp': "Hvad siger Little's Law?",
           'arg': "Little's Law siger at det gennemsnitlige antal enheder i et system (WIP, igangværende "
                  'arbejde) er lig med gennemløbshastigheden (throughput) gange den gennemsnitlige '
                  'gennemløbstid: WIP = throughput x gennemløbstid. Omskrevet: Gennemløbstid = WIP / '
                  'throughput. Det gælder for ethvert stabilt system uanset variation og rækkefølge.',
           'fisker': 'At du kan formlen WIP = gennemløbshastighed x gennemløbstid og kan isolere '
                     'gennemløbstiden.',
           'alt': 'Kan illustreres med en kø: jo flere i køen (WIP) ved samme ekspeditionstakt, jo længere '
                  'ventetid.',
           'snyd': False,
           'fakta': True},
          {'sp': "Hvad kan man bruge Little's Law til i praksis i en produktion?",
           'arg': 'Den kobler de tre størrelser, så man kan beregne den tredje ud fra to. Vil man reducere '
                  'gennemløbstiden (fx for kortere leveringstid), viser loven to veje: enten sænke WIP '
                  '(mindre igangværende arbejde, mindre kø) eller hæve throughput (producere hurtigere). '
                  'Den forklarer netop hvorfor Lean presser WIP ned: lavere WIP giver ved samme throughput '
                  'automatisk kortere gennemløbstid.',
           'fisker': 'At du kan bruge loven til at forklare hvorfor lavt WIP giver kort gennemløbstid.',
           'alt': 'Kan kobles til Lean/flow: reducér kø-WIP for at få varen hurtigere gennem fabrikken.',
           'snyd': False,
           'fakta': False},
          {'sp': 'En leder vil halvere gennemløbstiden og beslutter derfor at fordoble '
                 "produktionshastigheden (throughput). Følger det af Little's Law?",
           'arg': "Nej — her snyder intuitionen. Little's Law siger gennemløbstid = WIP / throughput. Hvis "
                  'man fordobler throughput, men WIP også fordobles (fordi man slipper dobbelt så mange '
                  'ordrer ind i systemet), så er gennemløbstiden UÆNDRET — de to ophæver hinanden. '
                  'Throughput sænker kun gennemløbstiden, hvis WIP holdes konstant eller falder. Den sikre '
                  'vej til kortere gennemløbstid er faktisk at SÆNKE WIP, ikke bare at køre hurtigere. '
                  "Mange tror 'hurtigere maskine = kortere tid', men loven viser at det er forholdet "
                  'WIP/throughput der afgør — slipper man mere arbejde ind, vinder man intet.',
           'fisker': 'Om du ser at throughput-stigning uden WIP-kontrol ikke ændrer gennemløbstiden — '
                     'forholdet er det afgørende.',
           'alt': 'Kan begrundes via Lean: derfor styrer man WIP (fx CONWIP/Kanban-lofter) frem for bare '
                  'at jage hastighed.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Interessentanalyse: magt-interesse-matrix og de 4 strategier',
  'fag': 'Strategi',
  'lag': [{'sp': 'Hvad er en interessentanalyse, og hvilke to akser bruger du til at placere '
                 'interessenterne?',
           'arg': 'En interessentanalyse kortlægger de aktører, der påvirker eller påvirkes af projektet, '
                  'så jeg kan vælge den rigtige håndtering af hver. Jeg placerer dem i en matrix med to '
                  'akser: magt (hvor meget kan de påvirke projektet) og interesse (hvor optaget er de af '
                  'udfaldet).',
           'fisker': 'At du kender modellen og dens to dimensioner: magt og interesse.',
           'alt': "Mendelows matrix er standardnavnet; nogle kalder akserne 'indflydelse' og 'engagement', "
                  'men det er samme idé.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Tag en interessent med høj magt og høj interesse — hvad gør du med dem, og hvorfor netop '
                 'det?',
           'arg': 'Dem samarbejder jeg tæt med (manage closely). De kan både vælte og fremme projektet, og '
                  'de bryder sig om det, så jeg involverer dem aktivt, holder dem løbende orienteret og '
                  'inddrager dem i beslutninger. Gør jeg ikke det, risikerer jeg en magtfuld modstander '
                  'der føler sig forbigået.',
           'fisker': "At høj magt + høj interesse = samarbejd tæt/styr nært, ikke bare 'informer'.",
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor skal du ikke bruge lige så mange ressourcer på dem med høj interesse men lav '
                 'magt?',
           'arg': 'Fordi de ikke kan flytte projektet, selvom de er engagerede. Dem holder jeg informeret '
                  '(keep informed) — de er ofte gode ambassadører og kan levere viden, men jeg bruger ikke '
                  'min knappe tid på tæt forhandling med dem. Ressourcerne skal hen, hvor magten er.',
           'fisker': "At du prioriterer indsats efter magt, ikke efter hvor 'larmende' eller ivrig en "
                     'interessent er.',
           'alt': 'De fire strategier: samarbejd tæt (høj/høj), hold tilfreds (høj magt/lav interesse), '
                  'hold informeret (lav magt/høj interesse), overvåg (lav/lav).',
           'snyd': False,
           'fakta': False},
          {'sp': "En interessent har lige nu lav interesse, men stor magt. Du kategoriserer ham som 'hold "
                 "blot tilfreds'. Er det en sikker placering?",
           'arg': 'Nej — det er fælden. Lav interesse kan vende til høj interesse i det øjeblik projektet '
                  'rammer noget han bryder sig om, og så har jeg pludselig en magtfuld og aktiv '
                  'modstander. Placeringen er ikke statisk: jeg skal overvåge ham og være klar til at '
                  "flytte ham op til 'samarbejd tæt', før han selv opdager at han er berørt. En "
                  'interessentanalyse er et øjebliksbillede, ikke en endelig dom.',
           'fisker': "At du forstår matrixen er dynamisk — placeringer skifter, og 'hold tilfreds' med høj "
                     'magt er den farligste rude at sove i.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'BATNA og BAPTA',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad betyder BATNA, og hvad bruger du det til i en forhandling?',
           'arg': 'BATNA er Best Alternative To a Negotiated Agreement — mit bedste alternativ, hvis denne '
                  'aftale ikke bliver til noget. Det er min plan B uden for forhandlingen. Jeg bruger det '
                  'som målestok: en aftale er kun god, hvis den er bedre end min BATNA.',
           'fisker': 'At du kan oversætte begrebet og ved, det er alternativet UDEN for bordet.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Du har to leverandører, der kan levere det samme. Gør det din forhandlingsposition stærk '
                 'eller svag?',
           'arg': 'Stærk. En god BATNA — her en alternativ leverandør — giver mig magt, fordi jeg '
                  'troværdigt kan gå fra bordet. Modparten ved, jeg ikke er afhængig af netop dem, så de '
                  'må give mig bedre pris og vilkår for at vinde ordren.',
           'fisker': 'At du kobler stærk BATNA direkte til magt og evnen til at gå fra bordet.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvad er så BAPTA, og hvorfor er det relevant at kende modpartens?',
           'arg': 'BAPTA står for modpartens BATNA — altså modpartens bedste alternativ til en forhandlet '
                  'aftale, set fra deres side (Best Alternative to a Potential Agreement bruges som etiket '
                  'for samme idé). Kender jeg den, ved jeg hvor presset de er. Har leverandøren ingen '
                  'andre kunder lige nu (svag BAPTA), kan jeg presse hårdere; har de en kø af købere, må '
                  'jeg være mere imødekommende.',
           'fisker': 'At du forstår BAPTA = modpartens BATNA, og at det afslører deres reelle pres.',
           'alt': "BAPTA og 'modpartens BATNA' bruges synonymt; pointen er at vurdere magtbalancen fra "
                  'begge sider.',
           'snyd': False,
           'fakta': True},
          {'sp': "Din leverandør siger 'vi har masser af andre kunder, vi behøver ikke jer'. Betyder det, "
                 'at deres BAPTA reelt er stærk?',
           'arg': 'Ikke nødvendigvis — det kan være en bluff. Påstanden er en forhandlingstaktik for at få '
                  'mig til at tro, deres BAPTA (modpartens BATNA) er stærk, så jeg giver efter. Jeg skal '
                  'teste den mod fakta: har de ledig kapacitet? Sælger de til mig fordi de mangler '
                  'omsætning? En BATNA er kun magt, hvis den er reel og troværdig — ikke fordi den udtales '
                  'højt. Jeg vurderer deres faktiske alternativer, ikke deres retorik.',
           'fisker': 'At du ikke tager en påstået stærk BAPTA for pålydende — magt afhænger af den REELLE '
                     'og troværdige plan B.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'ZOPA — forhandlingszonen',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad er ZOPA?',
           'arg': 'ZOPA er Zone Of Possible Agreement — det område, hvor en aftale er mulig. Det er '
                  'overlappet mellem købers og sælgers modstandspunkter: det interval af priser, som begge '
                  'parter kan acceptere frem for at gå fra bordet.',
           'fisker': 'At du kender definitionen: zonen hvor aftale er mulig = overlap af modstandspunkter.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Køber vil maks. give 100, sælger vil mindst have 90. Er der en ZOPA, og hvor ligger den?',
           'arg': 'Ja. Køberens modstandspunkt er 100 (det højeste han vil betale), sælgerens er 90 (det '
                  'laveste hun vil tage). De overlapper mellem 90 og 100, så ZOPA er intervallet 90-100. '
                  'Enhver pris derimellem er bedre for begge end ingen aftale.',
           'fisker': 'At du kan udregne zonen som overlappet mellem de to modstandspunkter.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Køber vil maks. give 80, sælger vil mindst have 90. Hvad sker der så?',
           'arg': 'Så er der ingen ZOPA — modstandspunkterne overlapper ikke (køber stopper ved 80, sælger '
                  'starter ved 90). Der er ingen pris, begge kan acceptere, så rationelt set bliver der '
                  'ingen aftale. Enten må en part ændre sit modstandspunkt, eller også må vi udvide kagen '
                  'med andre vilkår end pris.',
           'fisker': 'At intet overlap = ingen ZOPA = ingen aftale (medmindre præmisserne ændres).',
           'alt': 'Man kan skabe en ZOPA ved at lægge værdi til, fx levering, betalingsbetingelser eller '
                  'volumen — altså gå fra distributiv til integrativ.',
           'snyd': False,
           'fakta': False},
          {'sp': "Hvis du kender hele ZOPA'en på forhånd, bør du så bare foreslå midtpunktet som en fair "
                 'aftale?',
           'arg': "Nej — det er fælden. Hele ZOPA'en er acceptabel for mig; jeg vil have så meget af zonen "
                  'som muligt, ikke nøjes med midten. Hvis ZOPA er 90-100 og jeg er køber, vil jeg presse '
                  "mod 90, ikke automatisk lande på 95. Et 'fair' midtpunkt lyder rimeligt, men det "
                  'forærer halvdelen af min mulige gevinst væk. Desuden kender jeg sjældent modpartens '
                  "modstandspunkt præcist — at afsløre at jeg kender ZOPA'en ville svække min forhandling. "
                  'Midtpunktet er en bekvem norm, ikke en optimering.',
           'fisker': "At du ikke forveksler 'der er en ZOPA' med 'del den lige over' — målet er at fange "
                     'mest muligt af zonen.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Målpunkt (MDO) og modstandspunkt (LDO)',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad er forskellen på dit målpunkt og dit modstandspunkt i en forhandling?',
           'arg': 'Målpunktet (MDO — Most Desired Outcome) er det resultat, jeg helst vil opnå — mit '
                  'ambitiøse mål. Modstandspunktet (LDO — Least Desired Outcome) er min smertegrænse: det '
                  'dårligste, jeg vil acceptere, før jeg hellere går fra bordet. Mellem dem ligger mit '
                  'forhandlingsrum.',
           'fisker': 'At du kan adskille det ambitiøse mål (MDO) fra smertegrænsen (LDO).',
           'alt': 'MDO/LDO kaldes også aspirationspunkt og reservationspunkt.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad bestemmer, hvor dit modstandspunkt (LDO) skal ligge?',
           'arg': 'Min BATNA. Modstandspunktet skal sættes der, hvor aftalen lige akkurat er lige så god '
                  'som mit bedste alternativ uden for bordet. Kan en alternativ leverandør levere til 100, '
                  'giver det ingen mening at acceptere mere end 100 her — så LDO bør være 100.',
           'fisker': 'At LDO/modstandspunktet er forankret i BATNA, ikke i ønsketænkning.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Bør du sætte dit målpunkt højt og ambitiøst, eller realistisk og tæt på det forventede?',
           'arg': 'Højt, men begrundet. Forskning viser, at forhandlere med ambitiøse, velargumenterede '
                  'målpunkter opnår bedre resultater — udgangskravet (åbningen) ankrer forhandlingen. '
                  'Sætter jeg målet for lavt, ankrer jeg lavt og lukker selv min øvre gevinst. Det skal '
                  'dog kunne forsvares med argumenter, ellers mister jeg troværdighed.',
           'fisker': 'At ambitiøse, men begrundede målpunkter giver bedre udfald via ankring.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Under forhandlingen viser det sig, at modparten er mere presset end ventet. Bør du holde '
                 'fast i dit forberedte modstandspunkt, fordi det jo er bestemt af din BATNA?',
           'arg': 'Modstandspunktet er bestemt af MIN BATNA og bør ikke flyttes, bare fordi modparten er '
                  'svag — min smertegrænse er stadig min smertegrænse. Men fælden er at tro, jeg så skal '
                  'sigte mod mit modstandspunkt. Modpartens svaghed betyder, at deres modstandspunkt er '
                  'længere væk fra mit, end jeg troede — altså en større ZOPA. Det skal flytte mit '
                  'MÅLPUNKT (jeg sigter højere), ikke mit modstandspunkt. Jeg løsner ikke smertegrænsen; '
                  'jeg hæver ambitionen.',
           'fisker': 'At du adskiller LDO (forankret i egen BATNA, stabil) fra MDO (kan og bør justeres '
                     'med ny info om modparten).',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Principiel forhandling (Harvard-metoden)',
  'fag': 'Kommunikation',
  'lag': [{'sp': 'Hvad er kernen i principiel forhandling efter Harvard-metoden?',
           'arg': 'Principiel forhandling handler om at forhandle ud fra sagens substans i stedet for at '
                  'slås om positioner. De fire principper er: skil personen fra problemet, fokuser på '
                  'interesser frem for positioner, find løsninger til fælles fordel, og brug objektive '
                  'kriterier til at afgøre uenigheder.',
           'fisker': 'At du kender de fire principper i Harvard-modellen (Fisher & Ury).',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad er forskellen på en position og en interesse — giv gerne et eksempel?',
           'arg': "En position er det, man kræver ('jeg vil have 100.000'); en interesse er hvorfor man "
                  "kræver det ('jeg har brug for likviditet nu'). To parter med modsatte positioner kan "
                  'have forenelige interesser. Ser jeg bag positionen til interessen, kan jeg ofte finde '
                  'en løsning, der dækker behovet på en anden måde — fx hurtigere betaling i stedet for '
                  'højere pris.',
           'fisker': 'At du forstår, at interesser kan forenes selv når positioner støder sammen.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor er det vigtigt at bruge objektive kriterier, frem for bare at mødes på midten?',
           'arg': 'Fordi objektive kriterier — markedspris, indeks, ekspertvurdering, branchestandard — '
                  'gør resultatet legitimt og uafhængigt af, hvem der er mest stædig. At mødes på midten '
                  'belønner den, der startede mest ekstremt. Med et objektivt kriterium kan begge parter '
                  'acceptere udfaldet uden at føle, de tabte en magtkamp, og aftalen holder bedre.',
           'fisker': 'At objektive kriterier skaber legitimitet og beskytter mod ren stædighedskamp.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': "Betyder 'skil personen fra problemet' og fokus på fælles fordel, at principiel "
                 'forhandling altid er den blødeste og mest eftergivende stil?',
           'arg': "Nej — det er en udbredt misforståelse. Harvard-metoden er udtrykkeligt 'blød mod "
                  "personen, hård mod sagen'. Jeg er venlig og respektfuld over for mennesket, men benhård "
                  'på substansen og mine interesser. Den har endda en indbygget bagstopper: hvis modparten '
                  'nægter at forhandle principielt, falder jeg tilbage på min BATNA og går fra bordet. At '
                  "være eftergivende ville være positionel 'blød' forhandling — det modsatte af "
                  'principiel. Metoden undgår både den hårde og den bløde grøft.',
           'fisker': "At du afviser ligningen 'principiel = eftergivende' — blød på person, hård på sag, "
                     'med BATNA som værn.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Distributiv vs. integrativ forhandling',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad er forskellen på distributiv og integrativ forhandling?',
           'arg': 'Distributiv forhandling er fordeling af en fast kage — det den ene vinder, taber den '
                  'anden (nulsum), typisk en ren priskamp. Integrativ forhandling handler om at udvide '
                  'kagen ved at finde løsninger, hvor begge parter får mere, fx ved at bytte om på ting, '
                  'vi værdsætter forskelligt.',
           'fisker': 'At du kan adskille fast kage (distributiv/nulsum) fra udvid kagen '
                     '(integrativ/win-win).',
           'alt': 'Kaldes også win-lose (distributiv) vs. win-win (integrativ).',
           'snyd': False,
           'fakta': True},
          {'sp': "Hvordan kan du i praksis 'udvide kagen' i en leverandørforhandling?",
           'arg': 'Ved at bringe flere variabler i spil end prisen — fx leveringstid, '
                  'betalingsbetingelser, ordrevolumen, kontraktlængde eller garanti. Hvis sælger '
                  'værdsætter en lang kontrakt højt og jeg værdsætter lav stykpris højt, kan vi bytte: jeg '
                  'binder mig længere, hun giver rabat. Begge får noget, der er mere værd for dem, end det '
                  'koster den anden.',
           'fisker': 'At du kan skabe værdi ved at handle på flere dimensioner med forskellig '
                     'værdsættelse.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor kan det være risikabelt at gå rent distributivt til værks med en leverandør, du '
                 'skal bruge i mange år?',
           'arg': 'Fordi distributiv hård priskamp skader relationen og tilliden. Presser jeg leverandøren '
                  'til bunds hver gang, mister de incitament til at strække sig for mig, prioritere min '
                  'ordre eller dele information. I et langvarigt samarbejde er den fremtidige relation '
                  'selv en værdi, så integrativ tilgang, der bevarer goodwill, betaler sig ofte mere end '
                  'den sidste krones rabat.',
           'fisker': 'At du vejer relationen og fremtidigt samarbejde mod kortsigtet distributiv gevinst.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Integrativ forhandling er jo win-win. Betyder det, at du i en integrativ forhandling '
                 'ikke behøver bekymre dig om din egen andel?',
           'arg': 'Nej — det er fælden. Selv når kagen er udvidet, skal den stadig fordeles, og det trin '
                  'er distributivt. Integrativ og distributiv er ikke modsætninger, man vælger imellem; '
                  'næsten al reel forhandling har begge faser: først skab værdi sammen, derefter krav på '
                  "din andel. Hvis jeg slapper af i fordelingen, fordi 'det er jo win-win', risikerer jeg "
                  'at udvide kagen og så forære størstedelen væk. Man skal kunne begge dele — skabe OG '
                  'kræve.',
           'fisker': 'At du ikke ser win-win som naivt — værdiskabelse fjerner ikke værdifordelingen '
                     '(forhandlerens dilemma).',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Kulturelle forhandlingsstile',
  'fag': 'Kommunikation',
  'lag': [{'sp': 'Hvorfor er det vigtigt at tage højde for kultur, når du forhandler internationalt?',
           'arg': 'Fordi kultur påvirker, hvordan man kommunikerer, opbygger tillid, opfatter tid og '
                  'træffer beslutninger. Det, der er normal forhandlingsadfærd i én kultur, kan virke '
                  'uhøfligt eller utroværdigt i en anden. Misforstår jeg signalerne, kan jeg ødelægge en '
                  'aftale uden at vide hvorfor — så kulturforståelse er en del af forberedelsen.',
           'fisker': 'At du ser kultur som en reel variabel i forhandlingens kommunikation og tillid.',
           'alt': 'Kan kobles til Hofstedes dimensioner eller Halls høj-/lavkontekst-kommunikation.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad er forskellen på en højkontekst- og en lavkontekstkultur i forhandling?',
           'arg': 'I en lavkontekstkultur (fx Danmark, Tyskland, USA) ligger budskabet i de eksplicitte '
                  'ord — man siger tingene direkte og kontrakten betyder alt. I en højkontekstkultur (fx '
                  'Japan, Kina, Mellemøsten) ligger meget i det usagte: relation, tonefald og sammenhæng. '
                  "Et 'ja' kan betyde 'jeg hører dig', ikke 'jeg er enig'. Så jeg må læse mellem linjerne "
                  'og investere i relationen først.',
           'fisker': 'At du kender Halls høj-/lavkontekst og kan oversætte det til konkret '
                     'forhandlingsadfærd.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'I mange relationsorienterede kulturer bruges lang tid på smalltalk og middage før '
                 'forretningen. Hvorfor skal du ikke bare presse på for at komme til sagen?',
           'arg': 'Fordi relationen ER forretningen i de kulturer. Tilliden bygges først, og uden den får '
                  'man ingen god aftale. Presser jeg på for effektivitet, signalerer jeg, at jeg kun er '
                  'ude efter en transaktion, og det underminerer tilliden. Det, der for mig ligner '
                  'spildtid, er for modparten selve fundamentet for at turde indgå aftale — så tålmodighed '
                  'er en investering, ikke et tab.',
           'fisker': 'At du respekterer relationsbygning som funktionel, ikke som forsinkelse.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': "Du har læst, at en bestemt nationalitet 'altid forhandler hårdt og indirekte'. Er det en "
                 'god forberedelse at planlægge din modpart ud fra den nationale profil?',
           'arg': 'Kun med varsomhed — her er fælden. Nationale kulturprofiler er generaliseringer, ikke '
                  'individer. Min konkrete modpart kan være international, ung, vestligt uddannet eller '
                  'bare have sin egen stil, og virksomhedskultur og personlighed kan veje tungere end '
                  'nationaliteten. Bruger jeg profilen som facit, risikerer jeg stereotypisering og at '
                  'fejllæse personen foran mig. Profilen er en hypotese, jeg tester i mødet — ikke en '
                  'skabelon, jeg presser modparten ned i.',
           'fisker': 'At du bruger kulturmodeller som tendens/hypotese, ikke som deterministisk facit der '
                     'overtrumfer individet.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Værdikæden som analyseværktøj (ikke løsninger)',
  'fag': 'Værdikæde',
  'lag': [{'sp': 'Hvad bruger du værdikæden til i din opgave?',
           'arg': 'Værdikæden er et analyse- og beskrivelsesværktøj. Jeg går igennem virksomhedens '
                  'aktiviteter fra logistik ind, over produktion, til logistik ud og service, og beskriver '
                  'hvordan flowet faktisk ser ud i dag. Formålet er at kortlægge og skabe overblik, så jeg '
                  'kan spotte hvor der er problemer eller spild.',
           'fisker': 'At du forstår at værdikæden er kortlægning/analyse, ikke en plan.',
           'alt': 'Du kan også vinkle det som Porters tankegang: hvor i kæden skabes værdien for kunden, '
                  'og hvor er der primært ressourceforbrug.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor stiller du ikke bare dine løsningsforslag direkte ind i værdikæden, hvor '
                 'problemet er?',
           'arg': 'Fordi værdikæden skal holdes ren som beskrivelse og analyse. Hvis jeg blander løsninger '
                  'ind, kan jeg ikke længere bruge kæden til neutralt at vise nu-situationen og finde '
                  'årsagerne. Løsninger hører til i en separat del bagefter, hvor jeg så kan henvise '
                  'tilbage til præcis det sted i kæden, problemet blev fundet.',
           'fisker': 'Disciplinen: analyse og løsning skal adskilles, ellers bliver analysen utroværdig.',
           'alt': 'Argumentet kan også være metodisk: holder man dem adskilt, kan censor følge den røde '
                  'tråd fra problem til løsning.',
           'snyd': False,
           'fakta': False},
          {'sp': "Du skriver i din kædeanalyse: 'her bør virksomheden indføre stregkoder på "
                 "varemodtagelsen'. Er det fint?",
           'arg': 'Nej, det er en fælde jeg skal undgå. Det er et løsningsforslag, og det hører ikke '
                  "hjemme i selve værdikæden. I kæden må jeg kun konstatere problemet, fx 'varemodtagelsen "
                  "registreres manuelt, hvilket giver fejl og forsinkelser'. Selve forslaget om stregkoder "
                  'flytter jeg ned i løsningsdelen.',
           'fisker': 'Om du kan fange en løsning der er smuglet ind i analysen.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Primær- vs. støtteaktiviteter og harmoni i kæden',
  'fag': 'Værdikæde',
  'lag': [{'sp': 'Hvad er forskellen på en primæraktivitet og en støtteaktivitet?',
           'arg': 'Primæraktiviteterne er dem, der direkte skaber og leverer produktet til kunden: '
                  'indgående logistik, produktion, udgående logistik, markedsføring/salg og service. '
                  'Støtteaktiviteterne understøtter primæraktiviteterne, fx indkøb, teknologi/IT, HR '
                  '(menneskelige ressourcer) og virksomhedens infrastruktur.',
           'fisker': 'Ren definition og at du kan placere de fem primæraktiviteter.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor taler man om harmoni i værdikæden — kan man ikke bare optimere hvert led for '
                 'sig?',
           'arg': 'Nej, fordi leddene hænger sammen. Hvis jeg suboptimerer ét led, fx presser indkøb til '
                  'store billige partier, så vælter jeg lageret og binder kapital længere nede i kæden. '
                  'Harmoni betyder at leddene skal spille sammen, så det samlede flow bliver bedst — ikke '
                  'at hvert led er bedst isoleret.',
           'fisker': 'At du forstår suboptimering: helheden over delene.',
           'alt': 'Kan også forsvares ud fra leveringsservice: et stærkt produktionsled hjælper ikke hvis '
                  'logistik ud svigter — kunden oplever kun helheden.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Indkøb er jo helt centralt for at få varerne hjem — er det så ikke en primæraktivitet?',
           'arg': 'Det er fristende at sige ja, men i Porters model er indkøb (anskaffelse/procurement) en '
                  'støtteaktivitet. Det forveksles ofte med indgående logistik, som er primær. Indkøb '
                  'understøtter hele kæden — man køber jo også ind til produktion, IT og service — mens '
                  'den indgående logistik er selve det fysiske flow af varer ind.',
           'fisker': 'Om du falder for at gøre indkøb primært. Skelnen indkøb (støtte) vs. indgående '
                     'logistik (primær).',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Logistik ind — disponering, varemodtagelse og råvarelager (RVL)',
  'fag': 'Indkøb',
  'lag': [{'sp': 'Hvad sker der i den indgående logistik?',
           'arg': 'Det er flowet af varer ind i virksomheden. Det dækker disponering (at bestille de '
                  'rigtige mængder på de rigtige tidspunkter), varemodtagelse (fysisk modtage, kontrollere '
                  'og registrere) og indlægning på råvarelageret, RVL. Det handler om at sikre at '
                  'produktionen har det den skal bruge, uden at binde for meget kapital.',
           'fisker': 'At du kan navngive trinnene ind og ved at RVL = råvarelager.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er en grundig varemodtagelse vigtig — varerne er jo allerede bestilt og betalt?',
           'arg': 'Fordi fejl der slipper igennem varemodtagelsen, forplanter sig. Hvis vi indlægger '
                  'forkerte eller defekte råvarer på RVL, opdager vi det måske først i produktionen, hvor '
                  'det er meget dyrere at rette. Varemodtagelsen er virksomhedens første kontrolpunkt, og '
                  'en fejl her vælter harmonien længere nede i kæden.',
           'fisker': 'At kontrol tidligt i kæden er billigst — fejl vandrer nedstrøms.',
           'alt': 'Kan også forsvares økonomisk: forkerte leverancer der ikke fanges, giver '
                  'lagerdifferencer og forkert disponeringsgrundlag.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Når I køber råvarer hjem fra udlandet — hvem bærer risikoen for varerne under '
                 'transporten ind?',
           'arg': 'Det afhænger af Incoterms, som aftales i handlen. Det intuitive er at sige '
                  "'leverandøren indtil den står hos os', men det passer ikke altid. Ved fx EXW (Ex Works) "
                  'overgår risikoen allerede hos leverandøren, og så bærer vi risikoen under det meste af '
                  'transporten ind. Ved DDP bærer sælger risikoen helt frem til levering hos os. Så svaret '
                  'er: det står og falder med den valgte Incoterm.',
           'fisker': "Om du kobler transport ind til Incoterms i stedet for at gætte på 'leverandøren'.",
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Produktionsleddet — de 6 punkter',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad kigger du på, når du analyserer selve produktionen i værdikæden?',
           'arg': 'Jeg gennemgår produktionen ud fra de 6 punkter: produktionsform/layout, '
                  'produktionsprincip (fx træk/skub), kapacitet, gennemløbstid, kvalitet og fleksibilitet. '
                  'Jeg beskriver hvordan virksomheden faktisk producerer i dag på hvert punkt, så jeg får '
                  'et fuldt billede af produktionsleddet.',
           'fisker': 'At du har et fast greb om produktionsleddet (de 6 punkter) og kan beskrive det '
                     'struktureret.',
           'alt': 'Hvis din lærebog opdeler punkterne lidt anderledes, så forsvar din egen liste '
                  'konsekvent — det vigtige er systematikken.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor ikke bare køre maskinerne 100 % og holde kapaciteten fuldt udnyttet hele tiden?',
           'arg': 'Fordi fuld kapacitetsudnyttelse lyder effektivt, men kvæler fleksibilitet og forlænger '
                  'gennemløbstiden. Når der ikke er luft, hober ordrer sig op i kø, og leveringsevnen til '
                  'kunden falder. I et trækstyret/JIT-perspektiv vil man hellere have lidt buffer, så man '
                  'kan reagere på efterspørgsel, end at maksimere maskinudnyttelsen.',
           'fisker': 'At høj maskinudnyttelse ikke er det samme som god produktion — sammenhæng '
                     'kapacitet/gennemløbstid/leveringsservice.',
           'alt': 'Kan også forsvares omkostningsmæssigt: høj udnyttelse binder varer i arbejde '
                  '(kapitalbinding) og øger lagre i mellemleddet.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvis du finder en flaskehals i produktionen, skriver du så ind i de 6 punkter, at de '
                 'skal købe en ekstra maskine?',
           'arg': "Nej. I produktionsanalysen konstaterer jeg kun flaskehalsen, fx 'kapaciteten på "
                  "samlestationen er for lav og giver kødannelse og lang gennemløbstid'. At købe en ekstra "
                  'maskine er et løsningsforslag, og det hører til i løsningsdelen bagefter. Også '
                  'produktionsleddet skal holdes som ren beskrivelse.',
           'fisker': 'At reglen om analyse-uden-løsninger også gælder inde i produktionsleddet.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Logistik ud — færdigvarelager (FVL) og leveringsservice',
  'fag': 'Værdikæde',
  'lag': [{'sp': 'Hvad indeholder den udgående logistik?',
           'arg': 'Det er flowet af færdige varer ud til kunden. Det dækker færdigvarelageret (FVL), '
                  'plukning, pakning, forsendelse og transport ud. Et centralt mål her er '
                  'leveringsservice: at kunden får den rigtige vare, i rigtig mængde, til tiden.',
           'fisker': 'At du kender FVL = færdigvarelager og kan navngive trinnene ud.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Leveringsservice består af flere elementer — hvilke?',
           'arg': 'Leveringsservice er bredere end fart. Den består typisk af leveringstid, '
                  'leveringssikkerhed/pålidelighed, lagerservicegrad, fleksibilitet og information. De fem '
                  'dimensioner tilsammen er det kunden oplever; man kan ikke reducere leveringsservice til '
                  'leveringstid alene.',
           'fisker': 'At du kender de flere dimensioner i leveringsservice og ikke reducerer det til '
                     'hastighed.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Et stort færdigvarelager giver vel altid den bedste leveringsservice?',
           'arg': 'Det intuitive ja er en fælde. Et stort FVL hæver godt nok lagerservicegraden, men '
                  'binder meget kapital, øger lageromkostninger og risiko for ukurans. God '
                  'leveringsservice handler om den rette balance, ikke om størst muligt lager. Tit kan '
                  'bedre disponering og kortere gennemløbstid give samme service med mindre lager.',
           'fisker': "Om du gennemskuer at 'mere lager = bedre service' overser kapitalbinding og "
                     'omkostninger.',
           'alt': 'Kan også vinkles som en afvejning: høj lagerservicegrad koster kapitalbinding på FVL — '
                  'leveringsservice er altid en balance mod omkostninger.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Service — returvarer vs. reklamationer',
  'fag': 'Værdikæde',
  'lag': [{'sp': 'Hvad dækker serviceleddet i værdikæden?',
           'arg': 'Service er aktiviteterne efter salget, der vedligeholder eller øger produktets værdi '
                  'for kunden: support, reservedele, garanti, samt håndtering af varer der kommer retur. '
                  'Her hører blandt andet returvarer og reklamationer til.',
           'fisker': 'At du kan placere service som en primæraktivitet efter salget.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad er forskellen på en returvare og en reklamation?',
           'arg': 'En returvare fejler ikke noget — varen er i orden, men sendes retur af andre grunde, fx '
                  'kunden fortrød, bestilte for mange eller forkert. En reklamation er derimod en vare, '
                  'der fejler noget: den er defekt eller mangelfuld. Skellet er afgørende, fordi de '
                  'håndteres og bogføres forskelligt.',
           'fisker': 'Den præcise definition: returvare = fejler intet, reklamation = fejler noget.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'En kunde sender en vare tilbage og siger den er i stykker — så er det vel bare en '
                 'returvare i jeres system?',
           'arg': "Nej, det er fælden. At varen fysisk kommer retur gør den ikke til en 'returvare' i "
                  'fagsproget. Når kunden angiver at den fejler noget, er det en reklamation. Forskellen '
                  'betyder noget for håndteringen: en reklamation skal fejlårsagsbehandles og kan udløse '
                  'omlevering/garanti, mens en ægte returvare blot tages ind igen som kurant vare.',
           'fisker': 'Om du holder fast i definitionen under pres — fysisk retur ≠ returvare.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Fra værdikædeanalyse til løsningsdel — den røde tråd',
  'fag': 'Strategi',
  'lag': [{'sp': 'Hvordan hænger din værdikædeanalyse sammen med resten af din opgave?',
           'arg': 'Værdikæden er mit analysefundament. Jeg kortlægger flowet ind-produktion-ud-service og '
                  'finder de steder, hvor der er problemer eller spild. De fund tager jeg så med over i '
                  'løsningsdelen, hvor jeg foreslår og vurderer konkrete tiltag. Analysen leverer '
                  'problemerne, løsningsdelen leverer svarene — det giver den røde tråd.',
           'fisker': 'At du kan forklare formålet: analysen er midlet til at finde problemerne, ikke målet '
                     'i sig selv.',
           'alt': 'Kan også forsvares som beslutningsgrundlag: ledelsen kan kun prioritere løsninger, hvis '
                  'problemerne først er kortlagt neutralt.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvorfor ikke spare tid og skrive løsningen ind med det samme, hvor du finder problemet?',
           'arg': 'Fordi adskillelsen er hele pointen. Holder jeg analysen ren, kan jeg se alle problemer '
                  'samlet og prioritere hvilke der betyder mest, før jeg vælger løsninger. Blander jeg '
                  'dem, springer jeg fra det første problem til den første idé, og risikerer at overse '
                  'sammenhænge på tværs af kæden. Adskillelsen gør analysen troværdig og løsningerne '
                  'velbegrundede.',
           'fisker': 'At adskillelsen ikke er pedantisk formalia, men giver bedre prioritering og '
                     'helhedssyn.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Du finder fem problemer i kæden — skal du så lave en løsning på alle fem?',
           'arg': 'Nej, det er en fælde at gå completionist. Jeg skal prioritere: hvilke problemer rammer '
                  'forretningen og kunden hårdest, og hvor er der størst effekt for indsatsen. Det er '
                  'bedre at løse de få væsentlige problemer ordentligt end at sprede sig tyndt over alle '
                  'fem. Analysen skal fortjene sin plads ved at pege på det vigtigste, ikke alt.',
           'fisker': 'Om du kan prioritere frem for at behandle alle fund som lige vigtige.',
           'alt': 'Kan også forsvares ud fra væsentlighed/80-20: få årsager står ofte for hovedparten af '
                  'effekten.',
           'snyd': True,
           'fakta': False}]},
 {'emne': 'Konfidensinterval — hvad 95% betyder',
  'fag': 'Statistik',
  'lag': [{'sp': 'Du har regnet et 95% konfidensinterval for gennemsnittet. Hvad fortæller det interval?',
           'arg': 'Det er et interval beregnet ud fra stikprøven, som angiver et plausibelt spænd for den '
                  "sande populationsværdi (fx det rigtige gennemsnit). '95%' er knyttet til metoden: "
                  'gentager man stikprøven mange gange og regner et interval hver gang, vil 95% af de '
                  'intervaller fange den sande værdi. Bredden viser usikkerheden: smalt interval = lille '
                  'usikkerhed, bredt = stor usikkerhed.',
           'fisker': 'Om man overhovedet kan forklare formålet: at udtrykke usikkerhed på et estimat fra '
                     'en stikprøve.',
           'alt': "Man kan også sige: alle værdier i intervallet er 'plausible' værdier for den sande "
                  'parameter givet data.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Du siger 95% sikkerhed. Betyder det så, at der er 95% sandsynlighed for, at den sande '
                 'værdi ligger i netop DETTE interval, du har regnet?',
           'arg': 'Nej — og det er fælden. Når intervallet først er regnet, ligger den sande værdi enten i '
                  "det eller ej; der er ikke længere nogen sandsynlighed på 'netop dette' interval. De 95% "
                  'handler om metoden: gentager man stikprøven mange gange og regner et interval hver '
                  'gang, vil 95% af de intervaller fange den sande værdi.',
           'fisker': 'Den klassiske misforståelse. Eksaminator tester om du forstår, at sandsynligheden '
                     'ligger på proceduren over gentagne stikprøver, ikke på det enkelte færdige interval.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvis du gerne vil have et smallere — altså mere præcist — interval, hvad kan du så gøre?',
           'arg': 'Det sikre svar er at øge stikprøvestørrelsen n: usikkerheden falder med kvadratroden af '
                  'n, så intervallet bliver smallere uden at man snyder. Man kan også acceptere lavere '
                  'sikkerhed (fx 90% i stedet for 95%), men så fanger man den sande værdi sjældnere.',
           'fisker': 'Om du kender de tre håndtag (n, sikkerhedsniveau, spredning) og forstår, at man ikke '
                     'får både højere sikkerhed OG smallere interval gratis.',
           'alt': 'Reducér spredningen i data, fx ved at måle mere ensartet eller stratificere — men det '
                  'ændrer ikke selve fænomenet, kun målestøjen.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Et 99% interval er bredere end et 95% interval. Hvorfor er det bredere, når 99% jo lyder '
                 "'bedre'?",
           'arg': 'Fordi højere sikkerhed kræver, at man fanger den sande værdi oftere, og det kan man kun '
                  'garantere ved at gøre nettet større — altså bredere interval. Der er en afvejning: mere '
                  "sikkerhed koster præcision. 'Bedre' afhænger derfor af, hvad man vil bruge det til.",
           'fisker': 'Forståelsen af trade-off mellem sikkerhedsniveau og intervalbredde — at bredere ikke '
                     'er en fejl men en konsekvens.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'R2 / forklaringsgrad',
  'fag': 'Statistik',
  'lag': [{'sp': 'Din regressionsmodel har en R2 på 0,8. Hvad betyder det tal?',
           'arg': 'R2 er forklaringsgraden: den andel af variationen i den afhængige variabel (y), som '
                  'modellen forklarer. R2 = 0,8 betyder, at 80% af variationen i y forklares af modellen '
                  "(af x'erne), mens de resterende 20% skyldes andet, vi ikke har med.",
           'fisker': 'Den rene definition: andel forklaret variation, mellem 0 og 1.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': "Betyder en høj R2 så, at x'erne forårsager ændringer i y?",
           'arg': 'Nej. R2 måler kun, hvor godt modellen passer til data — hvor meget af variationen den '
                  'fanger. Det siger intet om årsagssammenhæng. To variable kan samvariere (høj R2) uden '
                  'at den ene forårsager den anden; der kan ligge en tredje, bagvedliggende faktor.',
           'fisker': "At du holder sammenhæng (samvariation) og årsag adskilt — det klassiske 'korrelation "
                     "er ikke kausalitet'.",
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Er en model med R2 = 0,95 altid bedre end en med R2 = 0,70?',
           'arg': 'Ikke nødvendigvis. R2 stiger næsten altid, når man tilføjer flere x-variable — også '
                  'ubrugelige. Så en høj R2 kan komme af, at man har proppet for mange variable ind '
                  '(overfitting), hvor modellen passer til støjen i netop dette datasæt og er dårlig til '
                  'nye data. Man bør se på justeret R2, som straffer for antallet af variable.',
           'fisker': 'At du kender svagheden ved R2: den belønner flere variable og kan narre. Kendskab '
                     'til justeret R2 imponerer.',
           'alt': 'Man bør også vurdere modellen fagligt: giver fortegnene mening, og holder den på nye '
                  'data — ikke kun stole på ét tal.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad er R2 i sig selv ikke nok til, når du skal bruge modellen til at forudsige fx '
                 'efterspørgsel?',
           'arg': 'R2 fortæller, hvor godt modellen passer til de data, den er bygget på — ikke '
                  'nødvendigvis hvor godt den rammer fremtiden. En model kan have høj R2 og stadig '
                  'forudsige skævt, hvis sammenhængen ændrer sig, eller hvis den er overfittet. Til '
                  'forudsigelse bør man teste på data, modellen ikke har set, og se på '
                  'forudsigelsesusikkerheden (intervaller), ikke kun R2.',
           'fisker': "At du skelner mellem 'passer til fortiden' og 'forudsiger fremtiden' — modnet brug "
                     'af statistik i en logistik-/forretningskontekst.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Normaltilnærmelse til binomialfordelingen',
  'fag': 'Statistik',
  'lag': [{'sp': 'Hvornår må du tilnærme en binomialfordeling med en normalfordeling?',
           'arg': 'Tommelfingerreglen er, at både np ≥ 5 OG n(1−p) ≥ 5 skal være opfyldt. Altså: det '
                  "forventede antal 'successer' (np) og det forventede antal 'fiaskoer' (n(1−p)) skal "
                  "begge være mindst 5. Er begge opfyldt, er fordelingen tilstrækkelig 'klokkeformet' til, "
                  'at normaltilnærmelsen er rimelig.',
           'fisker': 'At du kender betingelsen præcist — begge dele, ikke kun den ene.',
           'alt': 'Nogle lærebøger bruger grænsen 10 i stedet for 5 for at være mere konservativ; pointen '
                  'er den samme.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Du har n = 1000, så stikprøven er jo stor. Er normaltilnærmelsen så altid i orden?',
           'arg': 'Nej — stort n alene er ikke nok. Hvis p er meget lille (fx en fejlrate på 0,001), '
                  'bliver np = 1000 · 0,001 = 1, altså under 5, og så holder tilnærmelsen ikke, selv om n '
                  'er stort. Det er produktet np (og n(1−p)), der afgør det, ikke n alene.',
           'fisker': "Fælden: at man tror 'stort n' automatisk redder tilnærmelsen. Det er np og n(1−p), "
                     'der tæller.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvorfor er det netop produktet np og ikke n alene, der afgør det?',
           'arg': 'Fordi binomialfordelingen bliver skæv, når p ligger tæt på 0 eller 1. Ved lille p '
                  'klumper sandsynligheden sig op mod nul, og fordelingen har en lang hale til den ene '
                  'side — den ligner ikke en symmetrisk klokke. np og n(1−p) måler, hvor langt fordelingen '
                  "er 'rykket væk' fra kanten; er begge mindst 5, er der nok masse på begge sider til, at "
                  'den er nogenlunde symmetrisk og klokkeformet.',
           'fisker': 'Den dybere forståelse: betingelsen handler om symmetri/skævhed, ikke bare om en '
                     'vilkårlig grænse.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvad kan du gøre, hvis betingelsen ikke er opfyldt, men du stadig skal regne på '
                 'sandsynligheden?',
           'arg': 'Så lader man være med at tilnærme og regner i stedet direkte med binomialfordelingen '
                  '(fx i Excel med BINOMIAL.FORDELING), som er den eksakte fordeling. Ved meget lille p og '
                  'stort n kan man alternativt bruge Poisson-tilnærmelsen, som passer bedre til sjældne '
                  'hændelser end normalfordelingen.',
           'fisker': 'At du ikke tvinger en forkert tilnærmelse igennem, men kender det eksakte alternativ '
                     '(og gerne Poisson).',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Kontrolkort — punkt uden for grænserne',
  'fag': 'Produktion',
  'lag': [{'sp': 'Hvad er et kontrolkort, og hvad bruger man det til?',
           'arg': 'Et kontrolkort er et diagram, hvor man over tid plotter en måling fra processen (fx '
                  'vægt eller mål) sammen med en midterlinje og en øvre og nedre kontrolgrænse. Formålet '
                  "er at overvåge, om processen er stabil og 'under kontrol', eller om der sker noget "
                  'unormalt, man bør reagere på.',
           'fisker': 'Grundforståelsen: løbende processtyring, ikke en engangskontrol.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Et punkt falder uden for kontrolgrænserne. Hvad betyder det?',
           'arg': 'Det signalerer en særårsag (en speciel, udefrakommende årsag) — altså noget unormalt, '
                  'der ikke er en del af processens normale tilfældige variation. Fx en slidt maskine, en '
                  'fejlindstilling, et dårligt råvareparti. Man bør stoppe op og finde årsagen, ikke bare '
                  'ignorere det. (Bemærk: det er et signal, ikke et bevis — ved 3-sigma-grænser kan ca. '
                  '0,3% af punkterne falde udenfor ved ren tilfældighed.)',
           'fisker': 'Den centrale fortolkning: uden for grænserne = særårsag, ikke almindelig støj.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Når alle punkter ligger inden for grænserne, er processen så fejlfri og uden problemer?',
           'arg': 'Nej. Punkter inden for grænserne betyder kun, at processen er statistisk under kontrol '
                  '— den varierer kun pga. almindelige, tilfældige årsager. Den kan stadig producere '
                  'varer, der ikke lever op til kundens krav (tolerancerne), hvis grænserne i sig selv er '
                  'for brede. Kontrolgrænser er ikke det samme som kundens tolerancegrænser.',
           'fisker': "Fælden: at forveksle 'under kontrol' med 'god nok'. Kontrolgrænser ≠ "
                     'tolerancegrænser/specifikationer.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Kan processen være ude af kontrol, selv om INTET enkelt punkt ligger uden for grænserne?',
           'arg': 'Ja. Hvis fx mange punkter i træk ligger på samme side af midterlinjen, eller punkterne '
                  'danner en tydelig stigende eller faldende trend, er det også et signal om en særårsag — '
                  'selv om ingen punkter har krydset grænserne. Et systematisk mønster er i sig selv '
                  'unormalt, fordi ren tilfældig variation skulle svinge jævnt omkring midten.',
           'fisker': 'At du kender mønster-/trendreglerne og ikke kun stirrer på grænseoverskridelser — '
                     'dybere SPC-forståelse.',
           'alt': '',
           'snyd': True,
           'fakta': False}]},
 {'emne': 't- vs z-fordeling',
  'fag': 'Statistik',
  'lag': [{'sp': 'Hvornår bruger du t-fordelingen frem for z-fordelingen (normalfordelingen)?',
           'arg': 'Man bruger t-fordelingen, når man ikke kender populationens spredning og må estimere '
                  'den fra stikprøven — hvilket næsten altid er tilfældet i praksis — især ved små '
                  'stikprøver. z bruges, når den sande spredning er kendt (sjældent), eller når stikprøven '
                  'er stor nok til, at det reelt ikke gør forskel.',
           'fisker': 'Det centrale kriterium: kendt vs. ukendt spredning (og stikprøvestørrelse).',
           'alt': 'I praksis bruger mange t-fordelingen som standard, fordi spredningen næsten aldrig er '
                  'kendt; ved store n giver t og z stort set samme resultat.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor giver t-fordelingen et bredere konfidensinterval end z ved samme '
                 'sikkerhedsniveau?',
           'arg': 'Fordi vi ved t-fordelingen har en ekstra usikkerhed: vi kender ikke den sande '
                  'spredning, men har gættet den ud fra stikprøven. Det gæt kan være forkert, især ved få '
                  "observationer. t-fordelingen er derfor lidt 'fladere' med tungere haler, hvilket giver "
                  'et bredere interval — vi er ærlige om, at vi ved mindre.',
           'fisker': 'At du forstår, at den bredere t-fordeling afspejler ekstra usikkerhed fra det '
                     'estimerede spredningsmål.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Du har en kæmpe stikprøve, n = 5000, men kender ikke spredningen. Bør du så bruge z '
                 'eller t?',
           'arg': 'Korrekt og sikkert er at bruge t, fordi spredningen er ukendt. Men pointen er, at det '
                  'praktisk talt ikke gør forskel: ved så stort n er t-fordelingen næsten identisk med z, '
                  'så de to giver stort set samme interval. At vælge z her er ikke en alvorlig fejl, men '
                  'det rene svar er t, når spredningen er estimeret.',
           'fisker': "Fælden ligger i at tro, at stort n 'kræver' z. Du skal vise, at det rette valg "
                     'styres af kendt/ukendt spredning, og at t→z når n vokser.',
           'alt': 'I mange lærebøger og programmer bruges z ved meget store n af bekvemmelighed — det er '
                  'forsvarligt, så længe man kan begrunde, at forskellen er forsvindende.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad sker der med t-fordelingen, når stikprøven bliver større og større?',
           'arg': 'Den nærmer sig normalfordelingen (z). Jo flere frihedsgrader (jo større n), jo bedre er '
                  'vores estimat af spredningen, så den ekstra usikkerhed forsvinder og halerne bliver '
                  'tyndere. I grænsen er t og z ens. Derfor er z reelt et specialtilfælde af t ved meget '
                  'stor stikprøve.',
           'fisker': 'Den dybe sammenhæng: t konvergerer mod z; forskellen handler om frihedsgrader.',
           'alt': '',
           'snyd': False,
           'fakta': True}]},
 {'emne': 'Signifikansniveau og fejltyper',
  'fag': 'Statistik',
  'lag': [{'sp': 'Hvad betyder et signifikansniveau på 5%, når du tester en hypotese?',
           'arg': 'Det er den grænse, vi sætter for, hvor stor en risiko vi accepterer for at forkaste '
                  'nulhypotesen, selv om den faktisk er sand. 5% betyder, at hvis nulhypotesen er sand, '
                  'vil vi i 5% af tilfældene fejlagtigt komme til at forkaste den. Det er altså vores '
                  'accepterede risiko for en type 1-fejl (falsk alarm).',
           'fisker': 'Definitionen: signifikansniveau = accepteret sandsynlighed for type 1-fejl.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Beskriv forskellen på en type 1- og en type 2-fejl.',
           'arg': 'Type 1-fejl: man forkaster nulhypotesen, selv om den er sand — en falsk alarm (man '
                  "'ser' en effekt, der ikke er der). Type 2-fejl: man fastholder nulhypotesen, selv om "
                  'den er falsk — man overser en effekt, der faktisk findes. Eksempel: type 1 = at dømme '
                  'en uskyldig, type 2 = at frifinde en skyldig.',
           'fisker': 'At du klart kan holde de to fejl adskilt og gerne illustrere med et eksempel.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Så hvis vi bare sætter signifikansniveauet meget lavt, fx 0,1%, undgår vi jo fejl. Er '
                 'det ikke bare bedre?',
           'arg': 'Nej, det er fælden. Et lavere signifikansniveau sænker risikoen for type 1-fejl, men '
                  'øger samtidig risikoen for type 2-fejl: man bliver så forsigtig med at forkaste '
                  'nulhypotesen, at man kommer til at overse virkelige effekter. De to fejltyper trækker i '
                  'hver sin retning — man kan ikke minimere begge på én gang uden at øge stikprøven.',
           'fisker': 'At du forstår afvejningen: type 1 og type 2 er modsatrettede, så at jage den ene ned '
                     'hæver den anden.',
           'alt': 'Vil man sænke begge fejl samtidig, er løsningen at øge stikprøvestørrelsen, ikke bare '
                  'at skrue på signifikansniveauet.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvordan vælger man så, hvilken fejltype man helst vil undgå?',
           'arg': 'Det afhænger af, hvad det koster i den konkrete situation. Hvis en falsk alarm er dyr '
                  'eller farlig (fx at stoppe en hel produktion uden grund), vil man holde type 1-fejl '
                  'lav. Hvis det er værre at overse problemet (fx at sende defekte varer ud til kunden), '
                  'vægter man at undgå type 2-fejl. Man vælger altså signifikansniveau ud fra '
                  'konsekvenserne — det er en forretningsbeslutning, ikke kun en statistisk.',
           'fisker': 'At du kan koble fejltyperne til reelle konsekvenser og se valget som en afvejning af '
                     'omkostninger, ikke en automatregel.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'IRR vs NPV — hvornår de er uenige',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad er forskellen på NPV og IRR som beslutningsmetode?',
           'arg': 'NPV (nutidsværdi/kapitalværdi) viser hvor mange kroner et projekt skaber ud over '
                  'afkastkravet — et absolut kronebeløb. IRR (intern rente) viser den rente hvor NPV netop '
                  "bliver 0, altså projektets egen forrentning i procent. NPV svarer på 'hvor meget "
                  "værdi', IRR på 'hvor god er forrentningen'.",
           'fisker': 'At du kan skelne krone-mål (NPV) fra procent-mål (IRR).',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvis to projekter rangordnes forskelligt af NPV og IRR, hvilket stoler du så på?',
           'arg': 'Stol på NPV. NPV måler den faktiske værdiskabelse i kroner og forudsætter '
                  'geninvestering til kalkulationsrenten, hvilket er realistisk. Vælger man efter IRR, kan '
                  'man vælge et lille projekt med høj procent frem for et stort projekt der skaber flere '
                  'kroner — og kroner er det der gør virksomheden rigere.',
           'fisker': 'At du ved NPV vinder ved uenighed, og kan begrunde det.',
           'alt': 'Hvis virksomheden har skarp kapitalrationering, kan IRR/profitability index bruges til '
                  'at prioritere, men selve beløbsmålet er stadig NPV.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvad er det helt konkret der gør at de bliver uenige?',
           'arg': 'To ting: forskellig skala (et stort og et lille projekt) og forskelligt tidsmønster i '
                  'pengestrømmene. IRR ignorerer skala — den er kun en procent og er ligeglad med om '
                  'projektet er stort eller lille. Derfor kan et lille projekt have høj IRR men lav NPV.',
           'fisker': 'At du forstår årsagen — skala og timing — ikke bare reglen.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Et projekt har en IRR på 25 procent og et andet på 15 procent. Det første må vel være '
                 'bedst?',
           'arg': 'Ikke nødvendigvis — det er en fælde. 25 procent af et lille beløb kan give færre kroner '
                  'end 15 procent af et stort beløb. Hvis projekt 2 er meget større, kan det have højere '
                  'NPV og dermed skabe mest værdi. Man skal regne NPV før man konkluderer; IRR alene '
                  'afslører ikke skalaen.',
           'fisker': "Om du falder for 'højeste procent vinder' eller husker at IRR ignorerer skala.",
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Kan et projekt have flere IRR-værdier?',
           'arg': 'Ja. Hvis pengestrømmene skifter fortegn flere gange (fx en stor udgift midt i forløbet '
                  'til reinvestering eller oprydning), kan der matematisk findes flere renter hvor NPV '
                  'bliver 0. Så bliver IRR ubrugelig som entydigt mål, og man må falde tilbage på NPV.',
           'fisker': 'Om du kender en ægte begrænsning ved IRR ud over skala.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Kalkulationsrenten — hvad og hvorfor',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad er kalkulationsrenten i en investeringsberegning?',
           'arg': 'Kalkulationsrenten er det afkastkrav virksomheden stiller til en investering — den '
                  'rente pengestrømmene tilbagediskonteres med. Den udtrykker hvad pengene mindst skal '
                  'forrentes for at investeringen er værd at lave.',
           'fisker': "At du kan definere renten som et afkastkrav, ikke bare 'en rente'.",
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor diskonterer vi overhovedet fremtidige pengestrømme?',
           'arg': 'Fordi penge har en tidsværdi: en krone i dag er mere værd end en krone om et år, da den '
                  'i dag kan investeres og forrentes. Diskontering gør fremtidige beløb sammenlignelige '
                  'med nutidskroner, så vi ikke lægger æbler og pærer sammen.',
           'fisker': 'At du forstår pengenes tidsværdi som grunden til diskontering.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvad bygger man kalkulationsrenten på — hvorfor netop det niveau?',
           'arg': 'Den afspejler alternativomkostningen: det afkast pengene kunne give i den bedste '
                  'alternative anvendelse med tilsvarende risiko. Den indeholder typisk en risikofri rente '
                  'plus et risikotillæg. Jo større usikkerhed i projektet, jo højere krav.',
           'fisker': 'At du kobler renten til alternativomkostning og risiko, ikke bare bankrenten.',
           'alt': 'Den kan også bygges på virksomhedens vægtede kapitalomkostning (WACC) — hvad det koster '
                  'at skaffe fremmed- og egenkapital.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Renten er bare hvad banken tager for et lån, ikke?',
           'arg': 'Nej, det er for snævert — en fælde. Lånerenten er kun en del. Kalkulationsrenten er '
                  'alternativomkostningen for ALLE pengene i projektet, også egenkapitalen, som ejerne '
                  'kunne have placeret andetsteds. Den indeholder også et risikotillæg, som lånerenten '
                  'ikke nødvendigvis dækker. Derfor er den typisk højere end ren lånerente.',
           'fisker': 'Om du forveksler lånerente med det fulde afkastkrav inkl. egenkapital og risiko.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvad sker der med NPV hvis du sætter renten for højt?',
           'arg': 'En for høj rente diskonterer fremtidige indtægter hårdt ned og kan gøre et i '
                  'virkeligheden sundt projekt til negativ NPV — så afviser man gode investeringer. For '
                  'lav rente gør det modsatte og kan godkende dårlige projekter. Renten er derfor en '
                  'følsom forudsætning man bør lave følsomhedsanalyse på.',
           'fisker': 'At du forstår renten som en kritisk, følsom forudsætning — ikke en neutral konstant.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'DuPont — afkastningsgrad = overskudsgrad × AOH',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad fortæller afkastningsgraden?',
           'arg': 'Afkastningsgraden viser virksomhedens evne til at forrente den samlede investerede '
                  'kapital — altså driftsresultatet sat i forhold til de aktiver der er bundet i driften. '
                  'Den måler hvor effektivt aktiverne skaber overskud, uafhængigt af hvordan de er '
                  'finansieret.',
           'fisker': 'At du kender afkastningsgraden som forrentning af den samlede kapital.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvordan kan afkastningsgraden splittes op i DuPont-modellen?',
           'arg': 'Afkastningsgrad = overskudsgrad × aktivernes omsætningshastighed (AOH). Overskudsgraden '
                  'viser hvor stor en del af omsætningen der bliver til driftsresultat (indtjeningsevnen), '
                  "og AOH viser hvor mange gange kapitalen 'omsættes' gennem omsætningen "
                  '(kapitaltilpasningen). Ganget sammen giver de afkastningsgraden.',
           'fisker': 'At du kan formlen og hvad hver faktor betyder.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er det nyttigt at dele den op i to — hvad lærer man der ikke ses i selve '
                 'afkastningsgraden?',
           'arg': 'Fordi to virksomheder kan have samme afkastningsgrad ad helt forskellige veje. En '
                  'lavpriskæde har lav overskudsgrad men høj AOH (mange varer hurtigt), en luksusbutik høj '
                  'overskudsgrad men lav AOH. Opdelingen viser HVOR problemet eller styrken ligger, så man '
                  'kan sætte ind det rigtige sted.',
           'fisker': 'At du ser opdelingen som et diagnoseværktøj, ikke bare et regnestykke.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Afkastningsgraden er faldet. Så er indtjeningen blevet dårligere, ikke?',
           'arg': 'Ikke nødvendigvis — fælde. Et fald kan skyldes lavere overskudsgrad ELLER lavere AOH. '
                  'Indtjeningen pr. krone omsætning kan være helt uændret, mens AOH er faldet fordi man '
                  'har bundet mere kapital (større lager, flere debitorer). Man skal regne begge faktorer '
                  'for at vide hvad der driver faldet.',
           'fisker': "Om du springer til 'dårligere indtjening' uden at tjekke om det er kapitalbindingen.",
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvis du vil hæve afkastningsgraden, hvad er ofte den hurtigste vej?',
           'arg': 'Ofte er det at hæve AOH ved at frigøre bunden kapital — skære i lager og debitorer — '
                  'fordi det kan gøres uden at ændre priser eller omkostningsstruktur. At hæve '
                  'overskudsgraden kræver enten højere priser eller lavere omkostninger, hvilket typisk er '
                  'sværere og mere konkurrencefølsomt.',
           'fisker': 'At du kan koble modellen til konkret handling, ikke kun analyse.',
           'alt': 'Alternativt kan man hæve overskudsgraden via produktmix mod højmargin-varer, hvis '
                  'markedet tillader det.',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Soliditetsgrad',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad er soliditetsgraden?',
           'arg': 'Soliditetsgraden er egenkapitalen i forhold til de samlede aktiver (passiver), opgjort '
                  'i procent. Den viser hvor stor en del af virksomheden der er finansieret med egne '
                  'midler frem for gæld.',
           'fisker': 'At du kan definitionen: egenkapital i procent af balancesummen.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad bruger man soliditetsgraden til at vurdere?',
           'arg': 'Virksomhedens evne til at modstå tab og dens langsigtede økonomiske robusthed. Høj '
                  'soliditet betyder en stor stødpude: virksomheden kan tabe penge eller møde dårlige '
                  'tider uden at gælden vælter den. Den er et solvens- og risikomål, ikke et '
                  'indtjeningsmål.',
           'fisker': 'At du kobler soliditet til risiko og modstandskraft, ikke til drift.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Er en høj soliditetsgrad altid det bedste?',
           'arg': 'Nej — det er en fælde. Meget høj soliditet kan betyde at virksomheden bruger for lidt '
                  'fremmedkapital og dermed går glip af gearing. Hvis man kan låne billigere end '
                  'afkastningsgraden, hæver gæld faktisk forrentningen af egenkapitalen. Maksimal '
                  'soliditet kan altså give for lav egenkapitalforrentning. Det rette niveau afhænger af '
                  'branche og risiko.',
           'fisker': "Om du falder for 'mere er bedre' eller kender afvejningen mellem sikkerhed og "
                     'gearing.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvorfor kræver en kapitaltung produktionsvirksomhed typisk højere soliditet end en '
                 'konsulentvirksomhed?',
           'arg': 'Fordi produktionsvirksomheden har store, svært omsættelige aktiver og høj operationel '
                  'risiko — den har brug for en større egenkapitalpude til at bære udsving. En '
                  'konsulentvirksomhed binder lidt kapital og kan klare sig med lavere soliditet. Derfor '
                  'skal soliditet altid vurderes mod branche, ikke mod en universel grænse.',
           'fisker': 'At du ikke bruger en fast tommelfingergrænse, men vurderer mod branche og risiko.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Likviditetsgrad',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad måler likviditetsgraden?',
           'arg': 'Likviditetsgraden sætter de likvide og hurtigt omsættelige aktiver (omsætningsaktiver) '
                  'i forhold til den kortfristede gæld. Den viser om virksomheden kan betale sine '
                  'regninger på kort sigt — den korte betalingsevne.',
           'fisker': 'At du kender det som et mål for kortsigtet betalingsevne.',
           'alt': 'Likviditetsgrad 1 (uden lager) er strammere end likviditetsgrad 2 (med lager); nævn '
                  'gerne hvilken man bruger.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er likviditet vigtigere på kort sigt end overskud?',
           'arg': 'Fordi en virksomhed går konkurs af manglende likviditet, ikke af manglende overskud. '
                  'Man kan være overskudsgivende på papiret men stadig mangle kontanter til at betale løn '
                  'og leverandører hvis pengene er bundet i lager og debitorer. Likviditet er evnen til at '
                  'betale her og nu.',
           'fisker': 'At du forstår forskellen på at tjene penge og at HAVE penge.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Virksomheden har en likviditetsgrad på 200 procent. Så er likviditeten i fin form, ikke?',
           'arg': 'Ikke nødvendigvis — fælde. Et højt tal kan skjule at omsætningsaktiverne består af '
                  'ukurant lager eller debitorer der ikke betaler. Pengene er måske bundet og ikke reelt '
                  'likvide. Desuden kan meget høj likviditet betyde uudnyttet kapital der bare ligger død. '
                  'Tallet skal kvalitetsvurderes — hvad består aktiverne af.',
           'fisker': 'Om du tager tallet for pålydende eller graver i kvaliteten af omsætningsaktiverne.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'To virksomheder har samme likviditetsgrad, men den ene klarer sig fint og den anden får '
                 'problemer. Hvordan?',
           'arg': 'Likviditetsgraden er et øjebliksbillede fra balancedagen og siger intet om '
                  'tidspunkterne. Den ene har måske kunder der betaler hurtigt og leverandørkredit der '
                  'løber langsomt — så passer ind- og udbetalinger sammen. Den anden har det modsat og '
                  'løber tør midt i måneden trods samme nøgletal. Pengestrømmenes timing afgør det, ikke '
                  'statusbilledet.',
           'fisker': 'At du ser nøgletallets begrænsning — det fanger ikke timingen i likviditeten.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Dækningsgrad vs dækningsbidrag',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad er forskellen på dækningsbidrag og dækningsgrad?',
           'arg': 'Dækningsbidrag (DB) er salgspris minus de variable omkostninger — opgjort i kroner. '
                  'Dækningsgrad (DG) er dækningsbidraget i procent af salgsprisen. DB er altså et '
                  'kronebeløb, DG den samme størrelse udtrykt som en procentandel af omsætningen.',
           'fisker': 'At du klart skiller kroner (DB) fra procent (DG).',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvad bruger man dækningsbidraget til?',
           'arg': 'Dækningsbidraget er det der er tilbage til at dække de faste omkostninger og derefter '
                  'give overskud. Når de samlede dækningsbidrag overstiger de faste omkostninger, tjener '
                  'virksomheden penge. Det er kernen i bidragstankegangen.',
           'fisker': "At du kender DB's rolle: dækker faste omkostninger og bidrager til overskud.",
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvornår foretrækker du dækningsgraden frem for dækningsbidraget?',
           'arg': 'Når du skal sammenligne produkter med forskellige priser. Et dyrt produkt har naturligt '
                  'højere DB i kroner, men det siger ikke om det er mere lønsomt pr. salgskrone. '
                  'Dækningsgraden gør produkterne sammenlignelige fordi den er relativ — den viser hvor '
                  'effektivt hver omsætningskrone bidrager.',
           'fisker': 'At du ved hvornår det relative mål (DG) slår det absolutte (DB).',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Produkt A har højere dækningsgrad end produkt B. Så skal vi satse på A, ikke?',
           'arg': 'Ikke uden videre — fælde. Høj dækningsgrad pr. styk betyder ikke mest samlet bidrag. '
                  'Hvis B sælges i langt større mængder eller har højere pris, kan B levere flere '
                  'DB-kroner i alt. Det er det samlede dækningsbidrag (DG × omsætning, eller DB pr. styk × '
                  'antal) der betaler de faste omkostninger — ikke procenten alene.',
           'fisker': 'Om du forveksler høj procent med mest værdiskabelse i kroner.',
           'alt': 'Hvis flaskehalsen er begrænset kapacitet, vurderer man i stedet DB pr. flaskehalsenhed '
                  '— ikke ren DG.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvis maskintid er flaskehals, hvilket produkt skal så prioriteres?',
           'arg': 'Det med højest dækningsbidrag pr. flaskehalstime — ikke højest DG eller højest DB pr. '
                  'styk. Når kapaciteten er den begrænsende ressource, handler det om at få mest bidrag ud '
                  'af hver knap maskintime. Et produkt med lavere DG kan vinde hvis det bruger '
                  'flaskehalsen langt mere effektivt.',
           'fisker': 'At du kan løfte bidragstankegangen op til flaskehalsoptimering.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Payback og dens begrænsninger',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad er paybacktiden?',
           'arg': 'Paybacktiden (tilbagebetalingstiden) er den tid det tager før et projekts løbende '
                  'indbetalinger har tjent den oprindelige investering hjem. Man lægger pengestrømmene '
                  'sammen indtil de dækker startinvesteringen.',
           'fisker': 'At du kan definitionen: hvornår investeringen er tjent hjem.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er payback populær trods sine svagheder?',
           'arg': 'Fordi den er enkel at forstå og beregne, og fordi den siger noget om risiko og '
                  'likviditet: jo hurtigere pengene er hjemme, jo mindre er man eksponeret for usikkerhed '
                  'langt ude i fremtiden. Den er et grovt risiko- og likviditetsmål.',
           'fisker': 'At du kan forsvare hvorfor metoden bruges i praksis.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvad er de to store ting payback overser?',
           'arg': 'For det første ignorerer den diskontering — den behandler en krone om fem år som en '
                  'krone i dag og ser bort fra pengenes tidsværdi. For det andet ignorerer den alt der '
                  'sker EFTER tilbagebetalingstidspunktet — al indtjening efter payback tæller ikke med. '
                  'Derfor siger den intet om den samlede lønsomhed.',
           'fisker': 'At du kender begge kerneblindheder: tidsværdi og indtjening efter payback.',
           'alt': 'Diskonteret payback retter den første fejl, men ignorerer stadig indtjeningen efter '
                  'tilbagebetalingstidspunktet.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Projekt A har kortere paybacktid end projekt B. Så er A den bedste investering, ikke?',
           'arg': 'Ikke nødvendigvis — fælde. A kan stoppe med at tjene lige efter payback, mens B '
                  'fortsætter med store indtægter i mange år og samlet skaber langt mere værdi. Payback '
                  'belønner hurtige penge men er blind for den samlede indtjening. Man skal regne NPV for '
                  'at vide hvilket projekt der reelt skaber mest værdi.',
           'fisker': 'Om du tror hurtig payback = bedst, eller husker at den ignorerer indtjening efter.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Kan et projekt med kort payback have negativ NPV?',
           'arg': 'Ja. Hvis pengestrømmene efter tilbagebetalingstidspunktet er små eller projektet kun '
                  'lige tjener investeringen hjem, kan diskonteringen gøre den samlede nutidsværdi negativ '
                  "— selvom investeringen formelt er 'betalt tilbage'. Payback kan altså godkende et "
                  'projekt der ødelægger værdi. Derfor bruges payback bedst som supplement til NPV, ikke '
                  'som hovedkriterium.',
           'fisker': 'At du ser at payback og NPV kan pege modsat, og hvorfor.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'Break-even / nulpunkt',
  'fag': 'Økonomi',
  'lag': [{'sp': 'Hvad er nulpunktet (break-even)?',
           'arg': 'Nulpunktet er den afsætning (i mængde eller omsætning) hvor de samlede dækningsbidrag '
                  'netop dækker de faste omkostninger, så resultatet er nul — hverken overskud eller '
                  'underskud. Under nulpunktet taber man penge, over det tjener man.',
           'fisker': 'At du kan definitionen: hvor totalt DB = faste omkostninger.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvordan beregner du nulpunktsmængden?',
           'arg': 'Nulpunktsmængde = faste omkostninger divideret med dækningsbidraget pr. styk. Hver '
                  'solgt enhed bidrager med sit DB til at dække de faste omkostninger, så man dividerer de '
                  'faste omkostninger med bidraget pr. styk for at finde hvor mange enheder der skal til.',
           'fisker': 'At du kan formlen og kan forklare logikken bag den.',
           'alt': 'I omsætning bruges: faste omkostninger / dækningsgrad.',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor er nulpunktet nyttigt udover bare at vise hvornår man går i nul?',
           'arg': 'Det viser sikkerhedsmarginen — hvor meget afsætningen kan falde før man begynder at '
                  'tabe penge. Det bruges også til at vurdere prisændringer, omkostningsbeslutninger og '
                  'risiko ved en investering: jo lavere nulpunkt i forhold til forventet salg, jo mere '
                  'robust er forretningen.',
           'fisker': 'At du ser break-even som et risiko- og beslutningsværktøj, ikke bare et tal.',
           'alt': '',
           'snyd': False,
           'fakta': False},
          {'sp': 'Hvis vi sænker salgsprisen for at sælge flere stykker, så flytter nulpunktet sig vel ned '
                 'fordi vi sælger mere?',
           'arg': 'Nej — det er en fælde. Lavere pris sænker dækningsbidraget pr. styk, og dermed STIGER '
                  'nulpunktsmængden, fordi hver enhed nu bidrager mindre til at dække de faste '
                  'omkostninger. Man skal altså sælge FLERE stykker for at gå i nul, ikke færre. Større '
                  'mængde retfærdiggør kun prisnedsættelsen hvis det samlede dækningsbidrag faktisk '
                  'stiger.',
           'fisker': "Om du forveksler 'sælge mere' med lavere nulpunkt — DB pr. styk er det afgørende.",
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'En virksomhed har høje faste omkostninger og lave variable. Hvad betyder det for '
                 'nulpunkt og risiko?',
           'arg': 'Højt nulpunkt og høj risiko: der skal sælges meget før de tunge faste omkostninger er '
                  'dækket, så virksomheden er sårbar ved fald i afsætningen. Til gengæld er dækningsgraden '
                  'høj, så når man først er over nulpunktet, vokser overskuddet hurtigt med hvert ekstra '
                  'salg. Det er en høj-gearet omkostningsstruktur — stor opside, men også stor nedside.',
           'fisker': 'At du kobler omkostningsstruktur til nulpunkt, risiko og operationel gearing.',
           'alt': '',
           'snyd': False,
           'fakta': False}]},
 {'emne': 'EXW vs. FOB — hvor langt rækker sælgers ansvar?',
  'fag': 'Jura',
  'lag': [{'sp': 'Hvad betyder EXW, og hvor meget af leveringen står sælger for?',
           'arg': 'EXW (Ex Works / Fra Fabrik) er den klausul, hvor sælger gør mindst. Sælger stiller bare '
                  'varen klar på sin egen adresse (fabrik/lager). Derfra bærer KØBER alt: lastning, '
                  'transport, eksport- og importtold, forsikring og risiko. EXW er sælgers letteste '
                  'forpligtelse og købers tungeste.',
           'fisker': 'Om du kender EXW som yderpunktet hvor køber bærer alt.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor vælge FOB frem for EXW, hvis varen alligevel skal sejles?',
           'arg': 'Ved FOB (Free On Board) flytter sælger varen helt om bord på skibet i afskibningshavnen '
                  'og klarer eksporttolden. Det er en fordel for køber, fordi sælger kender sit eget land, '
                  'sin egen havn og sine egne eksportregler bedst. Ved EXW skulle køber selv arrangere '
                  'transport og eksportklarering i et fremmed land — det er besværligt og risikabelt. FOB '
                  'lægger den lokale del hos den, der har lokal viden.',
           'fisker': 'Om du kan begrunde valget ud fra hvem der har bedst kontrol over hvilket led.',
           'alt': 'Man kan også argumentere prismæssigt: ved EXW betaler køber ofte en lavere varepris men '
                  'højere transportbøvl; FOB samler mere ansvar hos sælger mod en højere pris.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Ved FOB går risikoen over, når varen er om bord. Men hvem betaler søfragten og '
                 'forsikringen under sejladsen?',
           'arg': 'Her er fælden: selvom risikoen går over til køber, når varen er bragt om bord, så er '
                  'det stadig KØBER der betaler søfragt og forsikring under selve sejladsen ved FOB — ikke '
                  "sælger. Mange tror, at fordi sælger 'sætter varen om bord', betaler sælger også "
                  'transporten. Det gør han ikke ved FOB. Vil man have sælger til at betale fragt og '
                  'forsikring, skal man bruge CIF i stedet.',
           'fisker': 'Om du adskiller hvor RISIKOEN går over (om bord) fra hvem der BETALER fragten '
                     '(køber).',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Kan man overhovedet bruge FOB, hvis varen sendes med fly eller lastbil?',
           'arg': 'Nej — og det er en typisk fejl. FOB (og CIF) er kun til sø- og indre vandvejstransport, '
                  "fordi de bygger på 'om bord på skibet'. Sender man med fly, tog eller lastbil, skal man "
                  'bruge alle-transportmiddel-klausuler som FCA, CPT eller CIP. At skrive FOB på en '
                  'flyforsendelse er forkert brug af Incoterms og skaber tvist om, hvornår risikoen reelt '
                  'gik over.',
           'fisker': 'Om du ved at FOB/CIF er transportmiddel-specifikke (kun skib).',
           'alt': '',
           'snyd': False,
           'fakta': True}]},
 {'emne': 'CIF — forsikring, risiko og det dobbelte skæringspunkt',
  'fag': 'Jura',
  'lag': [{'sp': 'Hvad dækker sælger under CIF?',
           'arg': 'CIF står for Cost, Insurance and Freight (Omkostning, Forsikring og Fragt). Sælger '
                  'betaler varen, søfragten frem til bestemmelseshavnen OG tegner en transportforsikring '
                  'til fordel for køber. CIF er altså en sø-klausul, hvor sælger betaler det meste af '
                  'vejen frem.',
           'fisker': 'Om du kan udfolde forkortelsen og se at sælger betaler fragt + forsikring.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor lægger man forsikringspligten hos sælger og ikke hos køber under CIF?',
           'arg': 'Fordi sælger har varen og overblikket på afsendelsestidspunktet og nemt kan tegne '
                  'forsikringen som en del af salget. For køber er CIF bekvemt: han får én samlet pris og '
                  'en forsikret forsendelse uden selv at skulle arrangere noget. Det gør CIF velegnet til '
                  'købere, der vil have det enkelt og overlade logistikken til sælger.',
           'fisker': 'Om du kan forklare bekvemmeligheds- og kontrol-logikken bag pligtfordelingen.',
           'alt': 'Modsat kan en stor, professionel køber foretrække FOB og selv forsikre, hvis han har '
                  'bedre forsikringsaftaler end sælger — så slipper han for sælgers avance på '
                  'forsikringen.',
           'snyd': False,
           'fakta': False},
          {'sp': 'Sælger betaler fragt og forsikring helt frem til bestemmelseshavnen. Bærer han så også '
                 'risikoen for, at varen går tabt undervejs?',
           'arg': "Nej — det er CIF's klassiske fælde. Selvom sælger BETALER fragt og forsikring helt "
                  'frem, går RISIKOEN over til køber allerede ved afskibningshavnen, når varen er om bord. '
                  'Går varen tabt på søen, er det købers risiko — men køber er dækket af den forsikring, '
                  'sælger tegnede. CIF har to forskellige skæringspunkter: omkostning frem til ankomst, '
                  'men risiko fra afgang. Derfor er forsikringen netop til fordel for køber.',
           'fisker': 'Om du holder omkostningens og risikoens skæringspunkter adskilt.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Hvis køber så er dækket af forsikringen, betyder CIF så at køber altid er fuldt sikret '
                 'mod tab på søen?',
           'arg': 'Ikke nødvendigvis. Under CIF er sælger kun forpligtet til at tegne MINIMUMSDÆKNING (den '
                  'laveste forsikringsklasse). Den dækker ikke alle skader. Vil køber have bredere '
                  'dækning, skal han enten selv tegne ekstra eller aftale CIP, hvor kravet til '
                  "dækningsniveauet er højere. Så 'forsikret' under CIF betyder ikke 'fuldt dækket'.",
           'fisker': "Om du kender begrænsningen i CIF's minimumsdækning.",
           'alt': '',
           'snyd': True,
           'fakta': True}]},
 {'emne': 'DAP — levering på destinationen, men hvem klarer importtolden?',
  'fag': 'Jura',
  'lag': [{'sp': 'Hvad betyder DAP, og hvor leverer sælger?',
           'arg': 'DAP står for Delivered At Place (Leveret På Stedet). Sælger bringer varen helt frem til '
                  'den aftalte adresse i købers land og bærer risiko og transportomkostninger hele vejen '
                  'frem. Varen anses for leveret, når den står klar til aflæsning på destinationen — selve '
                  'aflæsningen er købers opgave.',
           'fisker': "Om du ved at DAP er en 'frem til døren'-klausul med risiko hele vejen.",
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor vælger en køber DAP frem for fx EXW eller FOB?',
           'arg': 'Fordi DAP er bekvemt og forudsigeligt for køber: sælger står for transport og risiko '
                  'helt frem til købers adresse. Køber slipper for at arrangere international transport og '
                  "bære risikoen undervejs. Det er attraktivt for købere, der vil have varen leveret 'til "
                  "døren' uden logistikbøvl.",
           'fisker': 'Om du kan se kundevenligheden og risikoaflastningen i DAP.',
           'alt': "En sælger kan også bruge DAP strategisk som konkurrencefordel — at tilbyde 'leveret til "
                  "din adresse' kan vinde ordren over en konkurrent, der kun sælger EXW.",
           'snyd': False,
           'fakta': False},
          {'sp': 'Sælger leverer helt frem til købers adresse under DAP. Så han klarer vel også '
                 'importtolden i købers land?',
           'arg': "Nej — det er DAP's fælde. Under DAP er det KØBER, der står for importtold og "
                  'importklarering, selvom sælger bringer varen helt frem. Det er netop forskellen på DAP '
                  'og DDP: ved DDP betaler sælger også importtolden, ved DAP gør køber. Forveksler man de '
                  'to, kan varen stå fast i tolden, fordi ingen har taget ansvaret for importklareringen.',
           'fisker': 'Om du kender den præcise grænse: DAP = køber tager importtolden, DDP = sælger.',
           'alt': '',
           'snyd': True,
           'fakta': True},
          {'sp': 'Hvis en dansk virksomhed sælger DAP til en kunde i Tyskland, hvor meget importtold skal '
                 'køber så betale?',
           'arg': "Ingen. Tyskland og Danmark er begge i EU's toldunion, og der er ingen told på handel "
                  'INDEN for EU — told opkræves kun ved handel ud af unionen. Så selvom DAP normalt lægger '
                  'importtolden hos køber, er der her ingen told at betale. Spørgsmålet om hvem der bærer '
                  'importtolden bliver først reelt relevant ved handel til et land uden for EU.',
           'fisker': 'Om du kobler Incoterm-pligten sammen med at toldunionen fjerner told internt i EU.',
           'alt': '',
           'snyd': True,
           'fakta': True}]},
 {'emne': 'CISG — erstatning og påregnelige følgeskader ved misligholdelse',
  'fag': 'Jura',
  'lag': [{'sp': 'Hvad er CISG, og hvornår gælder den?',
           'arg': "CISG er FN's konvention om internationale løsørekøb (den internationale købelov). Den "
                  'gælder ved køb af varer MELLEM ERHVERVSDRIVENDE i forskellige lande, der har tiltrådt '
                  'konventionen. Den regulerer bl.a. levering, mangler, risikoens overgang og erstatning. '
                  'Den gælder ikke forbrugerkøb.',
           'fisker': "Om du kender CISG's anvendelsesområde: internationale B2B-køb.",
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor har man en fælles international regel som CISG i stedet for bare at bruge '
                 'sælgers eller købers nationale købelov?',
           'arg': 'Fordi parterne ellers ville skændes om HVILKET lands lov der gælder, hver gang en '
                  'handel går over grænsen. CISG giver et fælles, forudsigeligt regelsæt, så begge parter '
                  'ved hvad de er forpligtet til, uanset hvor de bor. Det sænker '
                  'transaktionsomkostningerne og gør international handel mere sikker.',
           'fisker': 'Om du forstår formålet: ét fælles sæt spilleregler skaber forudsigelighed.',
           'alt': 'Man kan også fremhæve neutralitet: ingen af parterne tvinges til at handle under '
                  "modpartens 'hjemmebane-lov', hvilket gør forhandlingen mere ligeværdig.",
           'snyd': False,
           'fakta': False},
          {'sp': 'En leverandør leverer for sent, og det koster køber en stor tabt videresalgsordre. Kan '
                 'køber få erstattet HELE dette følgetab?',
           'arg': 'Ikke automatisk. Efter CISG kan man kun få erstattet tab, der var PÅREGNELIGT — altså '
                  'tab som sælger på aftaletidspunktet kunne forudse som en mulig følge af '
                  'misligholdelsen. Et usædvanligt stort følgetab, som sælger ikke kendte til og ikke '
                  "kunne forudse, falder uden for. Det intuitive 'jeg fik et tab, så det skal dækkes fuldt "
                  "ud' holder ikke — påregnelighed er bremsen.",
           'fisker': 'Om du kender påregnelighedsbetingelsen som grænse for erstatningens omfang.',
           'alt': 'Køber kan styrke sin sag ved at vise, at han FAKTISK havde oplyst sælger om '
                  'videresalgsordren — så bliver tabet påregneligt, og erstatningen kan omfatte det.',
           'snyd': True,
           'fakta': False},
          {'sp': 'Forudsætter erstatning efter CISG, at sælger har handlet uagtsomt eller groft — altså at '
                 "det er hans 'skyld'?",
           'arg': 'Nej — det er en fælde, hvis man tænker i dansk skadeserstatning. CISG bygger på et '
                  'nærmest objektivt ansvar for kontraktbrud: leverer sælger ikke korrekt, ifalder han '
                  'erstatningsansvar, uanset om han kan bebrejdes noget. Han slipper kun fri ved helt '
                  'særlige, uforudsete hindringer uden for hans kontrol (force majeure-lignende). Det er '
                  'altså kontraktbruddet i sig selv, ikke graden af skyld, der udløser ansvaret.',
           'fisker': 'Om du ved at CISG-ansvaret er kontrolbaseret/objektivt, ikke skyldbaseret.',
           'alt': '',
           'snyd': True,
           'fakta': True}]},
 {'emne': 'Mangler og reklamation — beføjelser og rettidighed',
  'fag': 'Jura',
  'lag': [{'sp': 'Hvad kan en køber kræve, hvis den leverede vare er mangelfuld?',
           'arg': 'Køber har flere beføjelser: han kan kræve afhjælpning (at sælger reparerer fejlen) '
                  'eller omlevering (en ny, fejlfri vare). Alternativt kan han kræve et forholdsmæssigt '
                  'afslag i prisen, og ved en VÆSENTLIG mangel kan han hæve købet. Han kan derudover kræve '
                  'erstatning for sit tab. Beføjelserne afhænger af manglens karakter.',
           'fisker': 'Om du kan remse de centrale mangelsbeføjelser op.',
           'alt': '',
           'snyd': False,
           'fakta': True},
          {'sp': 'Hvorfor må køber ikke bare hæve købet med det samme, men ofte først skal acceptere '
                 'afhjælpning eller omlevering?',
           'arg': 'Fordi loven søger at holde handlen i live frem for at rive den fra hinanden. Ophævelse '
                  'er en hård beføjelse, der ruller hele handlen tilbage og rammer sælger økonomisk. Hvis '
                  'sælger kan rette fejlen billigt og hurtigt, får begge parter det de ville have. Derfor '
                  'er afhjælpning/omlevering det normale første skridt, og ophævelse er reserveret til de '
                  'alvorlige tilfælde.',
           'fisker': 'Om du forstår proportionalitet: mindste indgreb der løser problemet, før man når til '
                     'ophævelse.',
           'alt': 'Man kan også argumentere praktisk: omlevering bevarer leverandørforholdet, hvilket er '
                  'værdifuldt for en virksomhed der vil handle med samme leverandør igen.',
           'snyd': False,
           'fakta': False},
          {'sp': 'En mindre, men irriterende fejl ved varen — kan køber hæve købet på grund af den?',
           'arg': 'Nej, normalt ikke. Ophævelse kræver, at manglen er VÆSENTLIG. En lille, '
                  'udbedringsvenlig fejl giver ret til afhjælpning eller et forholdsmæssigt afslag, men '
                  "ikke til at hæve hele handlen. Det intuitive 'varen er fejlbehæftet, så jeg sender den "
                  "retur og annullerer' holder ikke ved bagateller — væsentlighedskravet er spærren mod at "
                  'hæve på et hvilket som helst grundlag.',
           'fisker': 'Om du kender væsentlighedstærsklen for ophævelse.',
           'alt': '',
           'snyd': True,
           'fakta': False},
          {'sp': 'Køber opdager en klar mangel, men er travlt optaget og reklamerer først flere måneder '
                 'senere. Han har stadig sin ret i behold, ikke?',
           'arg': 'Nej — det er fælden. Køber skal reklamere INDEN FOR RIMELIG TID efter, at han opdagede '
                  'eller burde have opdaget manglen. Venter han for længe, mister han sine beføjelser, '
                  'selvom manglen er reel. Retten til afhjælpning, afslag eller ophævelse forudsætter '
                  'altså rettidig reklamation. At have ret nytter ikke, hvis man sover på den.',
           'fisker': 'Om du ved at for sen reklamation afskærer beføjelserne, uanset at manglen findes.',
           'alt': '',
           'snyd': True,
           'fakta': True}]}]
