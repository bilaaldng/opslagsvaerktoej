"""Verificerede regne-opgaver (rigtige svar) til Forsvarstræner.

Forfattet + adversarielt censureret via workflow (36 items, 2 rettet).
Notation matcher core/*.py. Rør ikke i hånden — regenerér hellere.
"""

REGN = [
 {
  "fag": "Økonomi",
  "emne": "NPV (kapitalværdi)",
  "sp": "En investering koster 500.000 kr. og giver et cashflow på 200.000 kr. om året i 3 år. Afkastkravet (kalkulationsrenten) er 8%. Beregn NPV og fortæl, om virksomheden bør investere.",
  "svar": "NPV ≈ +15.420 kr. (positiv). Konklusion: ja, investér.",
  "metode": "NPV = −500.000 + 200.000/1,08 + 200.000/1,08² + 200.000/1,08³. Diskonteringsfaktorer: 1/1,08 = 0,9259; 1/1,08² = 0,8573; 1/1,08³ = 0,7938. Nutidsværdier: 185.185 + 171.468 + 158.766 = 515.419 kr. NPV = 515.419 − 500.000 = 15.419 ≈ +15.420 kr.",
  "fortolk": "Positiv NPV betyder, at projektet giver mere, end afkastkravet på 8% kræver — altså en merværdi på ca. 15.400 kr. i nutidskroner. Renten er afkastkravet/alternativomkostningen (hvad pengene ellers kunne forrentes til). Forsvar mundtligt: 'NPV > 0 → investér, fordi vi skaber værdi ud over vores afkastkrav'.",
  "faelde": "At lægge de tre cashflows sammen UDEN at diskontere (600.000 − 500.000 = 100.000) og tro, projektet er meget bedre, end det er. Husk altid at dividere med (1+r)^t for hvert år.",
  "soeg": [
   "npv",
   "kapitalværdi",
   "diskontering",
   "afkastkrav",
   "investering"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Payback (tilbagebetalingstid)",
  "sp": "En maskine koster 300.000 kr. og giver årlige (ikke-diskonterede) cashflows: år 1 = 100.000, år 2 = 120.000, år 3 = 150.000, år 4 = 150.000. Beregn tilbagebetalingstiden (payback) med interpolation.",
  "svar": "Payback ≈ 2,53 år (ca. 2 år og 6,5 måned).",
  "metode": "Akkumuleret cashflow: efter år 1 = 100.000; efter år 2 = 220.000; efter år 3 = 370.000. Investeringen (300.000) er tilbagebetalt et stykke inde i år 3. Mangler ved start af år 3: 300.000 − 220.000 = 80.000. År 3 giver 150.000. Andel af år 3 = 80.000/150.000 = 0,533. Payback = 2 + 0,533 = 2,53 år.",
  "fortolk": "Det betyder, at virksomheden har tjent investeringen hjem efter ca. 2,5 år. Jo kortere payback, jo lavere likviditetsrisiko. Forsvar mundtligt: payback måler risiko/likviditet, ikke rentabilitet — den ignorerer både diskontering og indtjening EFTER tilbagebetaling, så den bruges som supplement til NPV.",
  "faelde": "At diskontere cashflowene (det er kritisk levetid/diskonteret payback, ikke almindelig payback) eller at runde op til 3 hele år i stedet for at interpolere inde i året.",
  "soeg": [
   "payback",
   "tilbagebetalingstid",
   "akkumuleret cashflow",
   "interpolation",
   "likviditet"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Kritisk levetid",
  "sp": "En investering på 400.000 kr. giver et konstant årligt cashflow på 120.000 kr. Kalkulationsrenten er 10%. Hvad er den kritiske levetid — altså den mindste levetid, før de DISKONTEREDE cashflows dækker investeringen?",
  "svar": "Kritisk levetid ≈ 4,3 år (mellem 4 og 5 år — først efter ca. 4,3 år er den diskonterede sum ≥ 400.000).",
  "metode": "Diskonteret cashflow pr. år (120.000/1,1^t): år 1 = 109.091; år 2 = 99.174; år 3 = 90.158; år 4 = 81.962; år 5 = 74.511. Akkumuleret diskonteret: år 1 = 109.091; år 2 = 208.265; år 3 = 298.423; år 4 = 380.385; år 5 = 454.896. Investeringen 400.000 nås mellem år 4 og 5. Mangler efter år 4: 400.000 − 380.385 = 19.615. År 5 bidrager 74.511 (diskonteret). Andel = 19.615/74.511 = 0,26. Kritisk levetid = 4 + 0,26 ≈ 4,3 år.",
  "fortolk": "Den kritiske levetid er det minimum af år, projektet skal leve, for at NPV bliver ≥ 0. Lever maskinen længere end ca. 4,3 år, er investeringen rentabel; dør den før, taber man penge. Forsvar mundtligt: det er payback regnet på DISKONTEREDE beløb — det indbygger afkastkravet.",
  "faelde": "At bruge ikke-diskonterede cashflows (så får man 400.000/120.000 = 3,33 år, hvilket er for optimistisk). Husk at diskontere hvert års cashflow før du akkumulerer.",
  "soeg": [
   "kritisk levetid",
   "diskonteret payback",
   "kalkulationsrente",
   "npv nul",
   "rentabilitet"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Dækningsbidrag og dækningsgrad",
  "sp": "En vare sælges for 250 kr. og har variable enhedsomkostninger på 150 kr. Beregn dækningsbidraget pr. stk. og dækningsgraden, og forklar forskellen.",
  "svar": "DB = 100 kr. pr. stk. Dækningsgrad DG = 40%.",
  "metode": "DB = pris − variabel enhedsomkostning = 250 − 150 = 100 kr. DG = DB/pris = 100/250 = 0,40 = 40%.",
  "fortolk": "DB er kroner: hver solgt vare bidrager med 100 kr. til at dække faste omkostninger og derefter overskud. DG er procent: 40% af hver omsætningskrone er dækningsbidrag. Forsvar mundtligt: DB bruges pr. stk. (fx break-even i mængde), DG bruges på omsætning (fx break-even i kroner og sikkerhedsmargin).",
  "faelde": "At forveksle DB og DG — fx at kalde 100 kr. for 'dækningsgraden'. DG er ALTID en procent (DB delt med pris), DB er altid kroner.",
  "soeg": [
   "dækningsbidrag",
   "dækningsgrad",
   "db",
   "dg",
   "variable omkostninger"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Break-even (nulpunkt)",
  "sp": "En virksomhed har faste omkostninger på 600.000 kr. Varen sælges for 200 kr. med variable enhedsomkostninger på 120 kr. Beregn nulpunktsmængden og nulpunktsomsætningen.",
  "svar": "Nulpunktsmængde = 7.500 stk. Nulpunktsomsætning = 1.500.000 kr.",
  "metode": "DB pr. stk. = 200 − 120 = 80 kr. Nulpunktsmængde = faste omk / DB pr. stk. = 600.000/80 = 7.500 stk. DG = 80/200 = 0,40 = 40%. Nulpunktsomsætning = faste omk / DG = 600.000/0,40 = 1.500.000 kr. (tjek: 7.500 × 200 = 1.500.000 kr.).",
  "fortolk": "Ved 7.500 solgte stk. (1,5 mio. kr. omsætning) er resultatet præcis 0 — alle omkostninger er dækket, men der er endnu ikke overskud. Sælger man mere end det, tjenes 80 kr. pr. ekstra stk. Forsvar mundtligt: under nulpunktet er der underskud, over det er der overskud.",
  "faelde": "At dividere de faste omkostninger med PRISEN (200) i stedet for med DB pr. stk. (80). Det er dækningsbidraget, der skal dække de faste omkostninger, ikke hele prisen.",
  "soeg": [
   "break-even",
   "nulpunktsmængde",
   "nulpunktsomsætning",
   "faste omkostninger",
   "dækningsbidrag"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Sikkerhedsmargin",
  "sp": "En virksomhed har en omsætning på 2.000.000 kr. og en nulpunktsomsætning på 1.500.000 kr. Beregn sikkerhedsmarginen i procent og forklar, hvad den siger.",
  "svar": "Sikkerhedsmargin = 25%.",
  "metode": "Sikkerhedsmargin = (omsætning − nulpunktsomsætning)/omsætning = (2.000.000 − 1.500.000)/2.000.000 = 500.000/2.000.000 = 0,25 = 25%.",
  "fortolk": "Omsætningen kan falde med 25%, før virksomheden rammer nulpunktet og begynder at give underskud. Det er et mål for, hvor robust virksomheden er over for et salgsfald. Forsvar mundtligt: høj sikkerhedsmargin = lav risiko/god buffer; lav margin = sårbar over for nedgang.",
  "faelde": "At dividere med nulpunktsomsætningen i stedet for med den faktiske omsætning. Nævneren skal være den faktiske omsætning (det 'sikre' udgangspunkt).",
  "soeg": [
   "sikkerhedsmargin",
   "nulpunktsomsætning",
   "risiko",
   "buffer",
   "omsætning"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Bidragskalkulation (fremad fra kostpris)",
  "sp": "En vare har en kostpris på 600 kr. Virksomheden ønsker en dækningsgrad på 40%. Beregn dækningsbidraget og den salgspris, varen skal sælges til.",
  "svar": "DB = 400 kr. Salgspris = 1.000 kr.",
  "metode": "DB = kostpris·DG/(1−DG) = 600·0,40/(1−0,40) = 240/0,60 = 400 kr. Salgspris = kostpris + DB = 600 + 400 = 1.000 kr. (tjek: DG = DB/pris = 400/1.000 = 40% ✓).",
  "fortolk": "For at opnå en dækningsgrad på 40% skal varen sælges til 1.000 kr., hvoraf 400 kr. er dækningsbidrag. Forsvar mundtligt: bidragskalkulation lægger ud fra kostprisen og 'arbejder fremad' til en salgspris, der sikrer den ønskede DG.",
  "faelde": "At lægge 40% oven på kostprisen direkte (600·1,4 = 840 kr.). Det giver en avance på kostprisen, IKKE en dækningsgrad på 40% af salgsprisen. DG måles af salgsprisen, derfor formlen med /(1−DG).",
  "soeg": [
   "bidragskalkulation",
   "kostpris",
   "dækningsgrad",
   "salgspris",
   "avance"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Retrograd kalkulation (maks. købspris)",
  "sp": "En vare skal sælges for 500 kr. Virksomheden kræver en dækningsgrad på 30%. Der er variable salgsomkostninger på 20 kr. pr. stk. og told på 10% af købsprisen. Hvad er den maksimale pris, virksomheden kan betale for varen?",
  "svar": "Maks. købspris ≈ 300,91 kr. (ca. 301 kr.).",
  "metode": "Maks. købspris = (salgspris·(1−DG) − variable salgsomk)/(1+told%) = (500·(1−0,30) − 20)/(1+0,10) = (500·0,70 − 20)/1,10 = (350 − 20)/1,10 = 330/1,10 = 300,91 kr.",
  "fortolk": "Virksomheden kan højst betale ca. 301 kr. for varen og stadig opnå sin dækningsgrad på 30% efter told og salgsomkostninger. Forsvar mundtligt: retrograd kalkulation regner 'baglæns' fra en fast salgspris og et krav til DG ned til, hvad indkøbet må koste.",
  "faelde": "At glemme at trække de variable salgsomkostninger fra, eller at lægge tolden oven på i stedet for at dividere med (1+told%). Tolden beregnes af købsprisen, så den skal divideres ud, ikke trækkes fra salgsprisen.",
  "soeg": [
   "retrograd",
   "maks købspris",
   "told",
   "dækningsgrad",
   "indkøbspris"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Lineær afskrivning",
  "sp": "En lastbil købes for 900.000 kr. og forventes at have en scrapværdi på 150.000 kr. efter 5 års levetid. Beregn den årlige lineære afskrivning og den bogførte værdi efter 2 år.",
  "svar": "Årlig afskrivning = 150.000 kr. Bogført værdi efter 2 år = 600.000 kr.",
  "metode": "Lineær afskrivning = (nypris − scrapværdi)/levetid = (900.000 − 150.000)/5 = 750.000/5 = 150.000 kr. pr. år. Bogført værdi efter 2 år = 900.000 − 2·150.000 = 900.000 − 300.000 = 600.000 kr.",
  "fortolk": "Lastbilen mister 150.000 kr. i værdi hvert år i regnskabet, og efter 2 år står den bogført til 600.000 kr. Forsvar mundtligt: lineær afskrivning fordeler nettoanskaffelsen (ikke hele nyprisen) jævnt over levetiden; scrapværdien afskrives aldrig, fordi den forventes at være tilbage tilسidst.",
  "faelde": "At afskrive HELE nyprisen (900.000/5 = 180.000) og glemme at trække scrapværdien fra. Det er kun værditabet ned til scrapværdien, der afskrives.",
  "soeg": [
   "lineær afskrivning",
   "scrapværdi",
   "bogført værdi",
   "levetid",
   "anskaffelsessum"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Afkastningsgrad (DuPont)",
  "sp": "En virksomhed har et EBIT (resultat før renter) på 800.000 kr., en omsætning på 8.000.000 kr. og samlede aktiver på 5.000.000 kr. Beregn overskudsgrad, AOH og afkastningsgrad, og vis sammenhængen.",
  "svar": "Overskudsgrad = 10%, AOH = 1,6, afkastningsgrad = 16%.",
  "metode": "Overskudsgrad = EBIT/omsætning = 800.000/8.000.000 = 0,10 = 10%. AOH = omsætning/aktiver = 8.000.000/5.000.000 = 1,6. Afkastningsgrad = EBIT/aktiver = 800.000/5.000.000 = 0,16 = 16%. Sammenhæng (DuPont): afkastningsgrad = overskudsgrad × AOH = 0,10 × 1,6 = 0,16 = 16% ✓.",
  "fortolk": "Virksomheden forrenter sine aktiver med 16% (før renter). Den tjener 10 øre pr. omsætningskrone (overskudsgrad), og aktiverne 'omsættes' 1,6 gange om året (AOH). Forsvar mundtligt: vil man hæve afkastningsgraden, kan man enten øge indtjeningen pr. salg (overskudsgrad) eller udnytte aktiverne bedre (AOH).",
  "faelde": "At forveksle EBIT (resultat FØR renter) med årets resultat (efter renter og skat). Afkastningsgrad bruger driftsresultatet EBIT, fordi den måler aktivernes forrentning uafhængigt af finansiering.",
  "soeg": [
   "afkastningsgrad",
   "overskudsgrad",
   "aoh",
   "dupont",
   "ebit"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Soliditet, likviditet og gearing",
  "sp": "En virksomhed har egenkapital 3.000.000 kr., samlede aktiver 10.000.000 kr., omsætningsaktiver 4.000.000 kr. og kortfristet gæld 2.500.000 kr. Beregn soliditetsgrad, likviditetsgrad og gearing.",
  "svar": "Soliditetsgrad = 30%, likviditetsgrad = 160%, gearing = 2,33.",
  "metode": "Soliditetsgrad = egenkapital/aktiver = 3.000.000/10.000.000 = 0,30 = 30%. Likviditetsgrad = omsætningsaktiver/kortfristet gæld = 4.000.000/2.500.000 = 1,60 = 160%. Gæld i alt = aktiver − egenkapital = 10.000.000 − 3.000.000 = 7.000.000. Gearing = gæld/egenkapital = 7.000.000/3.000.000 = 2,33.",
  "fortolk": "Soliditet på 30% betyder, at 30% af aktiverne er finansieret med egenkapital — en sund buffer mod tab. Likviditetsgrad på 160% betyder, at omsætningsaktiverne mere end dækker den kortfristede gæld (>100% er godt). Gearing 2,33 betyder, at der er 2,33 kr. gæld pr. krone egenkapital — relativt højt. Forsvar mundtligt: soliditet = langsigtet robusthed, likviditet = kortsigtet betalingsevne.",
  "faelde": "Ved gearing at glemme at gælden = aktiver − egenkapital (man får ikke gælden direkte). Og at blande soliditet (egenkapital/aktiver) sammen med likviditetsgrad (omsætningsaktiver/kortfristet gæld) — det er to forskellige ting.",
  "soeg": [
   "soliditetsgrad",
   "likviditetsgrad",
   "gearing",
   "egenkapital",
   "nøgletal"
  ]
 },
 {
  "fag": "Økonomi",
  "emne": "Prisoptimering (monopol)",
  "sp": "En virksomhed har følgende afsætning ved forskellige priser: ved 100 kr. sælges 500 stk., ved 90 kr. sælges 700 stk., ved 80 kr. sælges 850 stk. De variable enhedsomkostninger er 50 kr. og de faste omkostninger 20.000 kr. Hvilken pris giver det største overskud?",
  "svar": "Prisen 90 kr. giver det største overskud (8.000 kr.).",
  "metode": "Overskud = omsætning − variable omk − faste omk, hvor variable omk = 50·mængde. Pris 100: oms = 100·500 = 50.000; var = 50·500 = 25.000; DB i alt = 25.000; overskud = 25.000 − 20.000 = 5.000 kr. Pris 90: oms = 90·700 = 63.000; var = 50·700 = 35.000; DB i alt = 28.000; overskud = 28.000 − 20.000 = 8.000 kr. Pris 80: oms = 80·850 = 68.000; var = 50·850 = 42.500; DB i alt = 25.500; overskud = 25.500 − 20.000 = 5.500 kr. Største overskud: 8.000 kr. ved prisen 90 kr.",
  "fortolk": "Prisen 90 kr. maksimerer overskuddet, fordi det er her det samlede dækningsbidrag (28.000 kr.) er størst. Forsvar mundtligt: man sælger ikke nødvendigvis mest ved laveste pris og heller ikke ved højeste pris — optimum er en balance. I optimum er grænseomsætning = grænseomkostning. De faste omkostninger flytter ikke optimum (de er ens for alle priser), men afgør, om der overhovedet er overskud.",
  "faelde": "At vælge prisen med den højeste omsætning (her 80 kr. med 68.000 kr.) i stedet for det højeste OVERSKUD. Høj omsætning er ikke det samme som høj indtjening, fordi de variable omkostninger stiger med mængden.",
  "soeg": [
   "prisoptimering",
   "monopol",
   "overskud",
   "grænseomsætning",
   "grænseomkostning"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Normalfordeling (z-score)",
  "sp": "En maskine fylder poser med en gennemsnitsvægt på 500 g og en spredning på 40 g. Vægten er normalfordelt. Hvor stor en andel af poserne vejer mere end 520 g? Og hvad betyder det tal?",
  "svar": "Ca. 30,85 % (ca. 31 %) af poserne vejer mere end 520 g.",
  "metode": "z = (x−µ)/σ = (520−500)/40 = 20/40 = 0,5. Slå op i standardnormaltabellen: P(Z<0,5) = 0,6915. Vi vil have P(X>520) = 1 − P(Z<0,5) = 1 − 0,6915 = 0,3085 = 30,85 %.",
  "fortolk": "Næsten hver tredje pose ligger over 520 g. z=0,5 betyder at 520 g ligger en halv spredning over gennemsnittet. Mundtligt: 'Jeg standardiserer værdien til en z-score, så jeg kan bruge den fælles standardnormaltabel uanset hvilke tal opgaven har.' Et positivt z betyder over middel.",
  "faelde": "At svare 0,6915 i stedet for 0,3085 — man glemmer at tabellen giver arealet TIL VENSTRE (P(Z<z)), og at spørgsmålet her er 'mere end', så man skal trække fra 1.",
  "soeg": [
   "normalfordeling",
   "z-score",
   "standardisering",
   "areal",
   "tabel"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Konfidensinterval (middelværdi)",
  "sp": "Du måler leveringstiden på 25 ordrer og får et gennemsnit på 52 timer med en stikprøvespredning s = 6 timer. Beregn et 95 % konfidensinterval for den sande middel-leveringstid (t(0,025; 24) = 2,064), og fortolk det.",
  "svar": "95 % KI = [49,52 ; 54,48] timer (ca. 49,5 til 54,5 timer).",
  "metode": "KI = gns ± t(α/2, n−1)·s/√n. Frihedsgrader = n−1 = 24. s/√n = 6/√25 = 6/5 = 1,2. Margin = 2,064·1,2 = 2,48. KI = 52 ± 2,48 = [49,52 ; 54,48].",
  "fortolk": "Vi er 95 % sikre på at den sande gennemsnitlige leveringstid ligger mellem 49,5 og 54,5 timer. Mundtligt: 'Jeg bruger t-fordelingen, fordi populationens spredning er ukendt og estimeret fra stikprøven, og n er lille. Bredere interval = mere usikkerhed; et større n ville snævre intervallet.'",
  "faelde": "At bruge z=1,96 i stedet for t=2,064, eller at glemme n−1 frihedsgrader. Også: at dividere med n i stedet for √n i standardfejlen.",
  "soeg": [
   "konfidensinterval",
   "middelvaerdi",
   "t-fordeling",
   "frihedsgrader",
   "standardfejl"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Konfidensinterval (andel)",
  "sp": "I en stikprøve på 200 kunder svarer 80, at de er tilfredse. Beregn et 95 % konfidensinterval for den sande andel tilfredse kunder (z = 1,96), og fortolk det.",
  "svar": "95 % KI = [0,332 ; 0,468], altså ca. 33,2 % til 46,8 %.",
  "metode": "p̂ = 80/200 = 0,40. KI = p̂ ± z·√(p̂(1−p̂)/n) = 0,40 ± 1,96·√(0,40·0,60/200). 0,40·0,60 = 0,24; 0,24/200 = 0,0012; √0,0012 = 0,0346. Margin = 1,96·0,0346 = 0,068. KI = 0,40 ± 0,068 = [0,332 ; 0,468].",
  "fortolk": "Vi er 95 % sikre på at den sande andel tilfredse kunder ligger mellem ca. 33 % og 47 %. Mundtligt: 'Andelen bruger z-fordelingen, fordi vi har en stor stikprøve. Bemærk at intervallet er bredt — for at halvere usikkerheden skal n firdobles.'",
  "faelde": "At regne med antallet 80 i formlen i stedet for andelen p̂=0,40. Eller at bruge t-fordeling — for andele bruges z. Husk også at p̂(1−p̂) bruger p̂, ikke n.",
  "soeg": [
   "konfidensinterval",
   "andel",
   "proportion",
   "z-fordeling",
   "stikprove"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Binomialfordeling",
  "sp": "En leverandør har en fejlrate på 15 %. Du udtager 10 enheder. Beregn sandsynligheden for præcis 2 defekte enheder. Hvad er forventet antal defekte og spredningen? Må du bruge normaltilnærmelse her?",
  "svar": "P(X=2) ≈ 0,276 (ca. 27,6 %). Forventet antal µ = 1,5 defekte, spredning σ ≈ 1,13. Nej — normaltilnærmelse må IKKE bruges her.",
  "metode": "P(X=2) = C(10,2)·0,15²·0,85⁸. C(10,2)=45; 0,15²=0,0225; 0,85⁸≈0,2725. 45·0,0225·0,2725 ≈ 0,276. µ = np = 10·0,15 = 1,5. σ = √(np(1−p)) = √(10·0,15·0,85) = √1,275 ≈ 1,13. Tjek normaltilnærmelse: np = 1,5 < 5 → kravet np≥5 er IKKE opfyldt.",
  "fortolk": "Der er ca. 28 % chance for præcis 2 defekte, og man forventer i snit 1,5 defekte pr. 10 enheder. Mundtligt: 'Jeg tjekker altid np≥5 OG n(1−p)≥5 før jeg tilnærmer med normalfordeling. Her er np kun 1,5, så jeg skal blive i den eksakte binomialformel.'",
  "faelde": "At bruge normaltilnærmelse uden at tjekke betingelsen. Også at glemme binomialkoefficienten C(n,k), eller at bytte om på p og (1−p) i potenserne.",
  "soeg": [
   "binomial",
   "sandsynlighed",
   "normaltilnaermelse",
   "forventet",
   "spredning"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "p-kort (styringskort for andel)",
  "sp": "Du laver et p-kort for fejlandele. Den gennemsnitlige fejlandel er p̄ = 0,04, og hver delmængde har n = 150 enheder. Beregn UCL og LCL. Hvad gør du med den negative LCL?",
  "svar": "UCL = 0,088 (8,8 %). LCL beregnes til −0,008, men sættes til 0, fordi en andel ikke kan være negativ.",
  "metode": "UCL/LCL = p̄ ± 3·√(p̄(1−p̄)/n). p̄(1−p̄) = 0,04·0,96 = 0,0384; 0,0384/150 = 0,000256; √ = 0,016. 3·0,016 = 0,048. UCL = 0,04 + 0,048 = 0,088. LCL = 0,04 − 0,048 = −0,008 → sættes til 0.",
  "fortolk": "Så længe fejlandelen i en delmængde ligger mellem 0 og 8,8 %, er processen i statistisk kontrol. Mundtligt: 'En negativ nedre grænse giver ingen mening for en andel, så jeg afrunder LCL til 0. Punkter over UCL signalerer en særlig årsag, der skal undersøges.'",
  "faelde": "At lade LCL stå som −0,008 — en andel kan aldrig være negativ, så LCL sættes altid til 0. Også at bruge ±2 i stedet for ±3 spredninger.",
  "soeg": [
   "p-kort",
   "styringskort",
   "kontrolgraenser",
   "andel",
   "lcl"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "X̄-kort og R-kort",
  "sp": "Du overvåger en proces med delmængder på n = 5. Det samlede gennemsnit er X̿ = 200 og den gennemsnitlige variationsbredde R̄ = 8. Beregn kontrolgrænserne for både X̄-kortet og R-kortet (n=5: A₂=0,577, D₃=0, D₄=2,114).",
  "svar": "X̄-kort: UCL = 204,62, LCL = 195,38. R-kort: UCL = 16,91, LCL = 0.",
  "metode": "X̄-kort: UCL/LCL = X̿ ± A₂·R̄ = 200 ± 0,577·8 = 200 ± 4,616 → UCL = 204,62, LCL = 195,38. R-kort: UCL = D₄·R̄ = 2,114·8 = 16,91; LCL = D₃·R̄ = 0·8 = 0.",
  "fortolk": "X̄-kortet overvåger om procesgennemsnittet skrider; R-kortet overvåger om spredningen/variationen ændrer sig. Mundtligt: 'Begge kort skal være i kontrol — et stabilt gennemsnit hjælper ikke, hvis variationen vokser. A₂, D₃ og D₄ er tabelkonstanter, der afhænger af delmængdestørrelsen n.'",
  "faelde": "At forveksle konstanterne (bruge A₂ på R-kortet) eller at bruge konstanter for forkert n. Husk at LCL på R-kortet er 0 for n=5, fordi D₃=0.",
  "soeg": [
   "x-bar-kort",
   "r-kort",
   "styringskort",
   "kontrolgraenser",
   "variationsbredde"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Lineær regression",
  "sp": "En regression mellem reklameudgift (x) og salg (y) giver ligningen y = 50 + 4·x og R² = 0,81. Hvad er salget forudsagt ved x = 20, hvad betyder hældningen 4, og hvad fortæller R² og korrelationskoefficienten r?",
  "svar": "Forudsagt salg = 130. Hældningen 4 betyder: +1 enhed reklame → +4 enheder salg. R²=0,81 betyder 81 % af variationen i salg forklares af reklame. r = 0,9 (positiv).",
  "metode": "Indsæt x=20 i y = 50 + 4·x = 50 + 4·20 = 50 + 80 = 130. Hældning b = 4 er ændringen i y pr. enhed x. r = √R² = √0,81 = 0,9; positiv fordi hældningen b er positiv.",
  "fortolk": "Modellen forklarer 81 % af salgsvariationen — en stærk sammenhæng. Mundtligt: 'R² er forklaringsgraden: hvor stor en del af y's variation modellen fanger. r er korrelationen og har samme fortegn som hældningen. Husk: stærk sammenhæng er ikke det samme som årsag (korrelation ≠ kausalitet).'",
  "faelde": "At forveksle R² og r (r = √R², ikke R²) eller at glemme at r kan være negativ — fortegnet følger hældningen. Også at tolke korrelation som bevis for årsag.",
  "soeg": [
   "regression",
   "forklaringsgrad",
   "korrelation",
   "r-kvadrat",
   "haeldning"
  ]
 },
 {
  "fag": "Statistik",
  "emne": "Normalfordeling (omvendt — find x)",
  "sp": "Leveringstiden er normalfordelt med middel 500 minutter og spredning 40 minutter. Du vil garantere levering for de hurtigste 90 % af ordrerne. Hvilken leveringstid skal du love (90-percentilen)? z for 90 % er 1,28.",
  "svar": "Ca. 551 minutter (550,8 min).",
  "metode": "Her går vi 'baglæns': vi kender arealet (90 %) og finder x. z = (x−µ)/σ omskrives til x = µ + z·σ. P(Z<z)=0,90 giver z = 1,28. x = 500 + 1,28·40 = 500 + 51,2 = 551,2 ≈ 551 minutter.",
  "fortolk": "90 % af ordrerne leveres inden for ca. 551 minutter, så det er en realistisk garanti. Mundtligt: 'Ved omvendt opslag starter jeg med procentdelen, slår z op i tabellen og ganger op til den oprindelige skala med x = µ + z·σ. Et positivt z, fordi 90-percentilen ligger over middel.'",
  "faelde": "At bruge z=1,28 forkert (trække fra i stedet for at lægge til) eller at forveksle 90-percentilen (z=1,28) med 95 %-grænsen (z=1,645). Husk: percentil over 50 % giver positivt z.",
  "soeg": [
   "normalfordeling",
   "percentil",
   "omvendt",
   "z-vaerdi",
   "leveringstid"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "EOQ",
  "sp": "En vare har et årligt forbrug på D = 10.000 stk. Det koster S = 400 kr. at afgive en ordre, enhedsprisen er 50 kr., og lagerrenten er 20 % om året. Beregn den optimale ordrestørrelse (EOQ) og de samlede relevante årsomkostninger. Hvad fortæller EOQ-tallet dig?",
  "svar": "EOQ ≈ 894 stk. (afrundet til hele stk.). Samlede relevante årsomkostninger ≈ 8.944 kr. Det svarer til ca. 10.000/894 ≈ 11,2 ordrer om året.",
  "metode": "H = enhedspris·lagerrente = 50·0,20 = 10 kr./stk./år. EOQ = √(2·D·S/H) = √(2·10.000·400/10) = √800.000 ≈ 894,4 ≈ 894 stk. Kontrol: ordreomk = (D/Q)·S = (10.000/894)·400 ≈ 4.472 kr.; lageromk = (Q/2)·H = (894/2)·10 ≈ 4.472 kr.; total ≈ 8.944 kr. (kan også beregnes direkte som √(2·D·S·H) = √80.000.000 = 8.944 kr.).",
  "fortolk": "EOQ er den ordrestørrelse, hvor ordreomkostninger og lageromkostninger er lige store, og totalen er mindst. Mundtligt forsvar: 'I optimum er de to omkostningskurver lige store (4.472 = 4.472), derfor er totalkurven flad i bunden — små afvigelser fra 894 koster næsten ingenting.'",
  "faelde": "Glemmer at H er pris·rente og indsætter renten (0,20) direkte som H, eller indsætter hele enhedsprisen (50) som H. Husk: H er KRONER pr. enhed pr. år, ikke en procent.",
  "soeg": [
   "eoq",
   "optimal ordrestørrelse",
   "lagerrente",
   "ordreomkostninger",
   "totalomkostninger"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "POQ / EPQ (produktion)",
  "sp": "En virksomhed producerer selv en komponent. Årligt forbrug D = 24.000 stk., opstillingsomkostning S = 500 kr. pr. serie, lageromkostning H = 4 kr./stk./år. Den daglige efterspørgsel er d = 80 stk., og den daglige produktion er p = 200 stk. Beregn den optimale seriestørrelse (EPQ).",
  "svar": "EPQ ≈ 3.162 stk. pr. produktionsserie.",
  "metode": "Korrektionsfaktor: (1 − d/p) = (1 − 80/200) = 1 − 0,4 = 0,6. EPQ = √(2·D·S/(H·(1−d/p))) = √(2·24.000·500/(4·0,6)) = √(24.000.000/2,4) = √10.000.000 ≈ 3.162 stk.",
  "fortolk": "Fordi varerne fyldes på lageret løbende mens de bruges (ikke alle på én gang som ved indkøb), bliver det gennemsnitlige lager lavere, og man kan derfor køre større serier end ved almindelig EOQ. Mundtligt: 'p > d gør faktoren < 1, hvilket sænker H og dermed hæver den optimale seriestørrelse i forhold til klassisk EOQ.'",
  "faelde": "Bytter om på d og p (sætter p<d, hvilket giver negativ rod) eller glemmer korrektionsfaktoren helt og regner som almindelig EOQ. Faktoren (1−d/p) skal være mellem 0 og 1.",
  "soeg": [
   "poq",
   "epq",
   "seriestørrelse",
   "produktionsmodel",
   "opstillingsomkostning"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "Sikkerhedslager og ROP",
  "sp": "En vare har en daglig efterspørgsel på d = 100 stk., en ledetid på L = 4 dage og en standardafvigelse på efterspørgslen pr. dag på σ = 20 stk. Virksomheden ønsker et serviceniveau på 95 %. Beregn sikkerhedslageret (SS) og genbestillingspunktet (ROP).",
  "svar": "Sikkerhedslager SS = 66 stk. Genbestillingspunkt ROP = 466 stk.",
  "metode": "Ved 95 % serviceniveau er z = 1,65. SS = z·σ·√L = 1,65·20·√4 = 1,65·20·2 = 66 stk. ROP = d·L + SS = 100·4 + 66 = 400 + 66 = 466 stk.",
  "fortolk": "Når lagerbeholdningen rammer 466 stk., afgives en ny ordre. De 400 stk. dækker det forventede forbrug i ledetiden, og de 66 stk. er buffer mod udsving. Mundtligt: 'Højere serviceniveau → højere z → større SS; det koster mere lager, men reducerer risikoen for restordre.'",
  "faelde": "Glemmer kvadratroden af L (ganger med L i stedet for √L), eller bruger forkert z. Husk SS skalerer med √L, mens ledetidsforbruget d·L skalerer lineært med L.",
  "soeg": [
   "sikkerhedslager",
   "rop",
   "genbestillingspunkt",
   "serviceniveau",
   "ledetid"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "ABC-analyse",
  "sp": "Du har 5 varenumre med følgende årlige forbrug (stk.) og stykpris (kr.): V1: 1.000 stk. à 50 kr.; V2: 200 stk. à 20 kr.; V3: 400 stk. à 100 kr.; V4: 2.000 stk. à 5 kr.; V5: 100 stk. à 30 kr. Lav en ABC-analyse og placér hver vare i A, B eller C.",
  "svar": "A: V1. B: V3 og V4. C: V2 og V5. (V1 alene udgør 46,7 % af årsværdien og er under 80 %-grænsen. V3 bringer akkumuleret til 84,1 % og V4 til 93,5 % — beget ≤95 %, altså B. V2 (97,2 %) og V5 (100 %) ligger over 95 % og er C.)",
  "metode": "Trin 1 – årsværdi = forbrug·pris: V1=1.000·50=50.000; V3=400·100=40.000; V4=2.000·5=10.000; V2=200·20=4.000; V5=100·30=3.000. Total = 107.000 kr. Trin 2 – sortér faldende og akkumulér i % af total: V1 50.000 → 46,7 %; V3 40.000 → akk. 90.000 = 84,1 %; V4 10.000 → akk. 100.000 = 93,5 %; V2 4.000 → akk. 104.000 = 97,2 %; V5 3.000 → akk. 107.000 = 100 %. Trin 3 – anvend grænserne (A = akk. ≤80 %, B = akk. ≤95 %, C = akk. >95 %): V1 (46,7 %) → A; V3 (84,1 %) > 80 % → B; V4 (93,5 %) ≤ 95 % → B; V2 (97,2 %) > 95 % → C; V5 (100 %) > 95 % → C. Resultat: A = V1; B = V3 og V4; C = V2 og V5.",
  "fortolk": "A-varer binder mest kapital og skal styres tæt (hyppig optælling, lave sikkerhedslagre, forhandling). C-varer kan styres løst (store ordrer, sjælden optælling). Mundtligt forsvar: pointen er ikke ANTAL varer men VÆRDI — få varer står for hovedparten af kapitalbindingen (Pareto/80-20). Bemærk at klassegrænserne er en konvention: med ≤80 %-reglen falder V3 i B, selv om den er en stor post — vær konsekvent og vis akkumuleringen.",
  "faelde": "Sorterer efter forbrug (antal stk.) i stedet for årsværdi (forbrug·pris) — så ville V4 (2.000 stk.) fejlagtigt blive en A-vare, selv om den kun udgør 9,3 % af kroneværdien. Det er kroneværdien, der bestemmer klassen, ikke mængden. Anden fælde: at tvinge V3 ind i A, fordi den 'føles stor' — den akkumulerede andel (84,1 %) overstiger 80 %-grænsen, så striks anvendelse giver B.",
  "soeg": [
   "abc-analyse",
   "pareto",
   "årsværdi",
   "kapitalbinding",
   "80-20"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "Make-vs-buy (breakeven)",
  "sp": "Virksomheden overvejer at producere selv (make) eller købe (buy). Egenproduktion: faste omkostninger 200.000 kr./år og variable 30 kr./stk. Køb: ingen faste omkostninger og 50 kr./stk. Ved hvilket volumen er de to alternativer lige dyre, og hvilket alternativ skal man vælge ved et forventet forbrug på 12.000 stk.?",
  "svar": "Breakeven-volumen = 10.000 stk. Ved 12.000 stk. (over breakeven) skal man producere selv (make), da egenproduktion her er billigst.",
  "metode": "Sæt make = a (fixed_a=200.000, var_a=30), buy = b (fixed_b=0, var_b=50). Breakeven = (fixed_a − fixed_b)/(var_b − var_a) = (200.000 − 0)/(50 − 30) = 200.000/20 = 10.000 stk. Kontrol ved 12.000: make = 200.000 + 30·12.000 = 560.000 kr.; buy = 0 + 50·12.000 = 600.000 kr. → make er 40.000 kr. billigere.",
  "fortolk": "Under breakeven (lavt volumen) er køb billigst, fordi man slipper for de faste omkostninger. Over breakeven er egenproduktion billigst, fordi den lavere variable omkostning (30<50) opvejer de faste 200.000 kr. Mundtligt: 'De høje faste omkostninger ved make kræver et vist volumen for at 'betale sig hjem' via den lavere stykpris.'",
  "faelde": "Vender brøken om eller bruger (var_a − var_b) i nævneren (giver negativt/forkert volumen), eller glemmer at vurdere HVILKEN side af breakeven det aktuelle forbrug ligger på. Tjek altid med et indsat tal.",
  "soeg": [
   "make or buy",
   "breakeven",
   "faste omkostninger",
   "variable omkostninger",
   "outsourcing"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "Forecast-fejl (MAD og bias)",
  "sp": "Over 4 perioder var den faktiske efterspørgsel D = 100, 120, 110, 130 og prognosen F = 110, 115, 120, 125. Beregn MAD, MFE (bias) og tracking signal. Er prognosen partisk?",
  "svar": "MAD = 7,5. MFE (bias) = −2,5. Tracking signal = −1,33. Prognosen har en svag negativ bias (overvurderer en anelse efterspørgslen), men tracking signal på −1,33 ligger godt inden for normale grænser (typisk ±4), så prognosen er acceptabel.",
  "metode": "Fejl (D−F): 100−110=−10; 120−115=+5; 110−120=−10; 130−125=+5. |D−F|: 10, 5, 10, 5 → MAD = Σ|D−F|/n = 30/4 = 7,5. MFE = Σ(D−F)/n = (−10+5−10+5)/4 = −10/4 = −2,5. Tracking signal = Σ(D−F)/MAD = −10/7,5 ≈ −1,33.",
  "fortolk": "MAD måler den gennemsnitlige fejlstørrelse (uden fortegn) = 7,5 stk. MFE/bias har fortegn: negativ betyder F > D i gennemsnit, altså at prognosen systematisk er sat for højt. Tracking signal sætter den akkumulerede bias i forhold til MAD; ligger den inden for ±4, er prognosen 'under kontrol'. Mundtligt: 'Lille bias, tracking signal langt fra grænsen → ingen grund til at justere modellen.'",
  "faelde": "Glemmer fortegnet i MFE/tracking signal (regner dem som absolutte tal som MAD) — så mister man netop informationen om OVER- eller undervurdering. MAD er altid uden fortegn; bias og tracking signal SKAL have fortegn.",
  "soeg": [
   "mad",
   "bias",
   "mfe",
   "tracking signal",
   "forecast"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "Vægtet leverandørscore",
  "sp": "Tre kriterier vægtes: kvalitet 50 %, pris 30 %, levering 20 %. Leverandør A scorer (på en 1-10 skala): kvalitet 8, pris 6, levering 9. Beregn leverandør A's samlede vægtede score.",
  "svar": "Leverandør A's samlede vægtede score = 7,6 (på 10-skalaen).",
  "metode": "Vægtene summer allerede til 1 (0,50 + 0,30 + 0,20 = 1). Vægtet score = Σ(vægt·score) = 0,50·8 + 0,30·6 + 0,20·9 = 4,0 + 1,8 + 1,8 = 7,6.",
  "fortolk": "Den vægtede score reducerer flere kriterier til ét sammenligneligt tal, hvor de vigtigste kriterier (her kvalitet) tæller mest. Mundtligt: 'A trækkes ned af en svag prisscore (6), men den lave vægt på pris (30 %) og de stærke kvalitets- og leveringsscores holder totalen oppe på 7,6 — man vælger den leverandør med højest samlet score.'",
  "faelde": "Glemmer at normalisere vægtene, hvis de ikke summer til 1 (fx hvis de var givet som 5, 3, 2 — så skal de divideres med 10 først), eller ganger score·score i stedet for vægt·score. Vægtene SKAL summere til 1.",
  "soeg": [
   "leverandørvalg",
   "vægtet score",
   "kriterievægte",
   "leverandørvurdering",
   "normalisering"
  ]
 },
 {
  "fag": "Indkøb (beregning)",
  "emne": "Periodisk review (max-niveau R)",
  "sp": "Et lager styres med periodisk gennemgang. Daglig efterspørgsel d = 50 stk., gennemgangsinterval P = 7 dage, ledetid L = 3 dage, sikkerhedslager SS = 80 stk. Beregn max-niveauet R. Ved en gennemgang er beholdningen 200 stk. — hvor meget skal der bestilles?",
  "svar": "Max-niveau R = 580 stk. Bestillingsmængde Q = R − beholdning = 580 − 200 = 380 stk.",
  "metode": "R = d·(P+L) + SS = 50·(7+3) + 80 = 50·10 + 80 = 500 + 80 = 580 stk. Q = R − beholdning = 580 − 200 = 380 stk.",
  "fortolk": "I et periodisk system bestiller man op til et fast max-niveau R hver gang. R skal dække efterspørgslen i BÅDE gennemgangsintervallet OG den efterfølgende ledetid (P+L), fordi der går (P+L) dage før næste leverance kan nå frem. Mundtligt: 'Derfor er P+L afgørende — man skal kunne klare sig fra nu til varerne fra NÆSTE gennemgang er ankommet.'",
  "faelde": "Bruger kun L (som i et kontinuert ROP-system) i stedet for (P+L), så bufferen mod hele review-perioden mangler. I periodisk review skal man altid dække P+L, ikke bare L.",
  "soeg": [
   "periodisk review",
   "max-niveau",
   "bestil op til",
   "gennemgangsinterval",
   "p+l"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "Udnyttelsesgrad",
  "sp": "En maskine har en kapacitet på 400 enheder pr. dag, og belastningen (ordreindgangen) er 340 enheder pr. dag. Beregn udnyttelsesgraden, og fortolk hvad tallet betyder.",
  "svar": "Udnyttelsesgrad = 85 %. Maskinen bruger 85 % af sin kapacitet; der er 15 % ledig kapacitet (buffer).",
  "metode": "Udnyttelsesgrad = belastning/kapacitet = 340/400 = 0,85 = 85 %.",
  "fortolk": "85 % betyder at 85 % af kapaciteten er beslaglagt af ordrer. Mundtligt: et niveau under 100 % er sundt, fordi en buffer optager udsving i efterspørgsel og forhindrer kødannelse. Hvis vi nærmer os 100 %, vokser ventetider og gennemløbstid eksplosivt (jf. kø-teorien), så 85 % er et fornuftigt driftspunkt.",
  "faelde": "At regne kapacitet/belastning i stedet for belastning/kapacitet (vender brøken om og får 1,18, altså 118 %). Husk: belastning står ØVERST. En udnyttelsesgrad over 100 % betyder overbelastning, ikke en regnefejl man bare lader stå.",
  "soeg": [
   "udnyttelsesgrad",
   "kapacitet",
   "belastning",
   "buffer",
   "flaskehals"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "Little's Law",
  "sp": "En produktionslinje har i gennemsnit 240 enheder i arbejde (WIP), og throughput er 30 enheder pr. time. Brug Little's Law til at finde den gennemsnitlige gennemløbstid, og forklar hvad den siger.",
  "svar": "Gennemløbstid T = 8 timer. En enhed er i gennemsnit 8 timer undervejs gennem systemet.",
  "metode": "Little's Law: WIP = R·T → T = WIP/R = 240/30 = 8 timer.",
  "fortolk": "T = 8 timer betyder at en enhed i gennemsnit tilbringer 8 timer fra start til slut i systemet. Mundtligt forsvar: vil man sænke gennemløbstiden, kan man enten sænke WIP (færre enheder i kø samtidig) eller øge throughput R. Less WIP → kortere ledetid ved samme hastighed — kernen i lean/JIT.",
  "faelde": "At forveksle de tre størrelser eller dividere forkert (fx 30/240). Hold styr på enhederne: WIP er i stk, R i stk/time, så T = stk / (stk/time) = timer. Pas også på at R er throughput (gennemløbshastighed), ikke gennemløbstid.",
  "soeg": [
   "little's law",
   "wip",
   "throughput",
   "gennemløbstid",
   "ledetid"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "OEE",
  "sp": "En maskine er planlagt til at køre 480 minutter på et skift. Der er 60 minutters nedetid. Ideel cyklustid er 0,5 minut pr. stk. Der produceres 700 stk, hvoraf 28 er defekte. Beregn OEE og de tre delfaktorer, og fortolk resultatet.",
  "svar": "Tilgængelighed = 87,5 %, ydelse = 83,33 %, kvalitet = 96 %. OEE = ca. 70,0 % (0,875·0,8333·0,96 = 0,700).",
  "metode": "Køretid = planlagt − nedetid = 480 − 60 = 420 min. Tilgængelighed = 420/480 = 0,875. Ydelse = (ideel cyklustid·antal producerede)/køretid = (0,5·700)/420 = 350/420 = 0,8333. Kvalitet = gode/total = (700−28)/700 = 672/700 = 0,96. OEE = 0,875·0,8333·0,96 = 0,70 = 70,0 %.",
  "fortolk": "OEE på 70 % betyder at kun 70 % af det teoretisk mulige output (i den planlagte tid, ved ideel hastighed og uden fejl) faktisk realiseres. Mundtligt: world-class er ca. 85 %, så her er der tab. Den største synder er ydelsen (83 %), så jeg ville starte med at undersøge hastigheds-/mikrostop-tab. De tre faktorer adskiller om tabet skyldes stilstand, langsom drift eller spild.",
  "faelde": "At blande tæller og nævner i ydelse (skal være ideel tid·producerede divideret med KØRETID, ikke planlagt tid), og at bruge total i stedet for gode i kvalitet. Husk også at nedetid trækkes fra planlagt tid for at finde køretid.",
  "soeg": [
   "oee",
   "tilgængelighed",
   "ydelse",
   "kvalitet",
   "nedetid"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "OTIF",
  "sp": "Af 500 leverancer var 460 til tiden (on time), og 475 var komplette (in full). De to forhold antages uafhængige. Beregn OTIF-raten, og forklar hvad den udtrykker.",
  "svar": "OTIF = 87,4 %. Ca. 87,4 % af leverancerne forventes både at være til tiden OG komplette.",
  "metode": "OTIF ved uafhængighed = (on time-andel)·(in full-andel) = (460/500)·(475/500) = 0,92·0,95 = 0,874 = 87,4 %.",
  "fortolk": "OTIF måler andelen af leverancer der både kom til tiden og var komplette — det er kundens reelle oplevelse af leveringspålidelighed. Mundtligt: bemærk at OTIF (87,4 %) er LAVERE end hver delrate hver for sig (92 % og 95 %), fordi begge krav skal opfyldes samtidigt. Det er hele pointen: kunden er kun tilfreds når alt klapper.",
  "faelde": "At lægge raterne sammen eller tage gennemsnit i stedet for at GANGE dem. Husk også at formlen kun gælder ved uafhængighed; kendes antallet der både var on time og in full, bruges i stedet both/total direkte.",
  "soeg": [
   "otif",
   "on time in full",
   "leveringspålidelighed",
   "uafhængighed",
   "sandsynlighed"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "Takt time og min. antal stationer",
  "sp": "Der er 420 minutter tilgængelig produktionstid pr. dag, og kunden efterspørger 60 enheder pr. dag. Det samlede arbejdsindhold (summen af alle opgavetider) er 42 minutter pr. enhed. Beregn takt time og det minimale antal stationer.",
  "svar": "Takt time = 7 minutter pr. enhed. Minimum antal stationer = 6.",
  "metode": "Takt time = tilgængelig produktionstid/krævet output = 420/60 = 7 min/stk. Min. antal stationer = loft(Σ opgavetider/takt time) = loft(42/7) = loft(6,0) = 6.",
  "fortolk": "Takt time på 7 min er den rytme linjen skal følge: hver 7. minut skal en færdig enhed forlade linjen for præcis at matche efterspørgslen. Mundtligt: takt = efterspørgselens puls. De 6 stationer er det teoretiske minimum; i praksis bliver det ofte flere, fordi opgaver ikke kan deles uendeligt og skal grupperes uden at overskride takt time pr. station.",
  "faelde": "At regne takt time som output/tid i stedet for tid/output, og at glemme at RUNDE OP (loft). Selv 6,01 stationer kræver 7 stationer — man kan ikke have en brøkdel af en station, og man runder altid op, aldrig ned.",
  "soeg": [
   "takt time",
   "stationer",
   "linjebalancering",
   "efterspørgsel",
   "loft"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "Linjebalancering (effektivitet og balancetab)",
  "sp": "En samlelinje har 4 stationer med tiderne 8, 6, 7 og 5 minutter. Beregn cyklustiden, linjens effektivitet (balanceringsgrad) og balancetabet, og fortolk.",
  "svar": "Cyklustid = 8 min. Effektivitet = 81,25 %. Balancetab = 18,75 %.",
  "metode": "Cyklustid = max(stationstider) = max(8,6,7,5) = 8 min. Σ stationstider = 8+6+7+5 = 26 min. Effektivitet = Σ stationstider/(antal stationer·cyklustid) = 26/(4·8) = 26/32 = 0,8125 = 81,25 %. Balancetab = 1 − effektivitet = 1 − 0,8125 = 0,1875 = 18,75 %.",
  "fortolk": "Effektiviteten på 81,25 % betyder at 81,25 % af den samlede stationskapacitet udnyttes til reelt arbejde; de resterende 18,75 % er ventetid fordi de hurtige stationer må vente på den langsomste (flaskehalsen på 8 min). Mundtligt forsvar: linjen er kun så hurtig som sin langsomste station, så vil man hæve effektiviteten, skal arbejde flyttes VÆK fra 8-minutters-stationen så belastningen jævnes ud.",
  "faelde": "At bruge gennemsnittet af stationstiderne som cyklustid i stedet for MAKSIMUM. Cyklustiden bestemmes altid af den langsomste station (flaskehalsen), ikke af gennemsnittet.",
  "soeg": [
   "linjebalancering",
   "cyklustid",
   "effektivitet",
   "balancetab",
   "flaskehals"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "Knap kapacitet (flaskehals-prioritering)",
  "sp": "To produkter konkurrerer om tid på samme flaskehalsmaskine. Produkt A: DB 200 kr/stk, kræver 4 min på flaskehalsen. Produkt B: DB 150 kr/stk, kræver 2,5 min på flaskehalsen. Hvilket produkt bør prioriteres ved knap kapacitet, og hvorfor — vis beregningen.",
  "svar": "Produkt B bør prioriteres. DB pr. flaskehalsminut: A = 50 kr/min, B = 60 kr/min. B tjener mest pr. knap minut.",
  "metode": "DB pr. flaskehalstime (her pr. minut) = DB pr. stk / tid pr. stk på flaskehalsen. A: 200/4 = 50 kr/min. B: 150/2,5 = 60 kr/min. 60 > 50 → prioritér B.",
  "fortolk": "Når flaskehalsen er den knappe ressource, er det IKKE det produkt med højest DB pr. stk der er bedst, men det med højest DB pr. flaskehalsminut. Mundtligt: A har højest DB pr. stk (200 vs 150), men B udnytter flaskehalsen bedre, fordi det binder mindre af den knappe tid. Hver flaskehalsminut er den dyre ressource — den skal forrentes bedst muligt, og det gør B med 60 kr/min.",
  "faelde": "At prioritere efter DB pr. stk (ville fejlagtigt vælge A). Ved knap kapacitet skal man dividere DB med forbruget af den KNAPPE ressource. Først når der ikke er en flaskehals, er DB pr. stk afgørende.",
  "soeg": [
   "flaskehals",
   "knap kapacitet",
   "dækningsbidrag",
   "db pr time",
   "prioritering"
  ]
 },
 {
  "fag": "Produktion (beregning)",
  "emne": "Kø-teori (M/M/1)",
  "sp": "Til en arbejdsstation ankommer der i gennemsnit λ = 8 emner pr. time, og stationen kan betjene µ = 10 emner pr. time. Beregn udnyttelsesgraden (rho) og den gennemsnitlige gennemløbstid i systemet, og fortolk.",
  "svar": "rho = 0,8 (80 %). Gennemløbstid Ts = 0,5 time = 30 minutter. Et emne er i gennemsnit en halv time i systemet (kø + betjening).",
  "metode": "rho = λ/µ = 8/10 = 0,8. Gennemløbstid Ts = 1/(µ−λ) = 1/(10−8) = 1/2 = 0,5 time = 30 min.",
  "fortolk": "rho = 0,8 betyder stationen er optaget 80 % af tiden. Ts = 30 min er den samlede tid et emne bruger (ventetid + selve behandlingen). Mundtligt: pointen er ikke-lineariteten — fordi λ ligger tæt på µ, opstår der kø selv om der er ledig kapacitet. Øges λ mod µ, eksploderer Ts mod uendelig. Derfor holder man bevidst udnyttelsen under 100 %.",
  "faelde": "At regne Ts = 1/µ (kun selve betjeningstiden) og glemme at trække λ fra i nævneren — så mister man ventetiden. Hele kø-pointen er nævneren (µ−λ): jo tættere λ er på µ, jo mindre nævner og jo længere gennemløbstid.",
  "soeg": [
   "kø",
   "m/m/1",
   "rho",
   "gennemløbstid",
   "ventetid"
  ]
 }
]
