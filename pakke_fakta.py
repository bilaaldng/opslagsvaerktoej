"""Ekstra fakta-flashcards til Forsvarstræner. Workflow-forfattet + censur.
Liste af [forside, bagside]; lægges oven på de oprindelige FAKTA (ingen fjernes).
"""

EKSTRA_FAKTA = [
 [
  "Genbestillingspunkt (ROP)",
  "Den lagerbeholdning, hvor man skal afgive en ny ordre, så varen når frem inden lageret tømmes. ROP = (gennemsnitligt forbrug pr. tidsenhed × leveringstid) + sikkerhedslager."
 ],
 [
  "Lagerrente",
  "Den årlige procentsats, der udtrykker, hvad det koster at have varer på lager — kapitalbinding (rente), lagerplads, forsikring, svind og forældelse lagt sammen. Bruges til at beregne lageromkostningen H i fx EOQ."
 ],
 [
  "ABC-analyse",
  "Opdeling af varer/leverandører efter værdi: A = få varer (ca. 20 %), der står for ca. 80 % af værdien (styres tæt), B = mellemgruppe, C = mange varer med lille værdi (styres enkelt). Bygger på Pareto-princippet (80/20)."
 ],
 [
  "Single/dual sourcing",
  "Single sourcing = køb af en vare hos én leverandør (lavere pris/tættere samarbejde, men højere forsyningsrisiko). Dual/multiple sourcing = brug af to eller flere leverandører for at sprede risiko og skabe konkurrence."
 ],
 [
  "TCO/TCA",
  "TCO (Total Cost of Ownership) = alle omkostninger ved et indkøb over hele levetiden: indkøbspris + transport, lager, kvalitet, drift, vedligehold og bortskaffelse. TCA (Total Cost of Acquisition) dækker kun anskaffelsesomkostningerne frem til varen er på plads (pris + transport, told, modtagelse mv.)."
 ],
 [
  "Rammeaftale",
  "En overordnet aftale med en leverandør, der fastlægger vilkår (pris, kvalitet, levering) for en periode, hvorefter der løbende kan afkaldes/bestilles uden at forhandle hver gang. Giver effektivitet og forudsigelighed."
 ],
 [
  "Servicegrad",
  "Udtrykker, hvor stor en andel af efterspørgslen der kan dækkes direkte fra lager uden mangel — fx 95 % servicegrad. Højere servicegrad kræver større sikkerhedslager og dermed højere lageromkostninger."
 ],
 [
  "Lead time",
  "Leveringstid — tiden fra en ordre afgives, til varen er modtaget og klar til brug. Lang eller usikker lead time øger behovet for sikkerhedslager og hæver genbestillingspunktet."
 ],
 [
  "Ordrevinder",
  "De konkurrenceparametre, der reelt afgør, at kunden vælger netop os frem for konkurrenterne (fx pris, leveringstid eller unik kvalitet). De skaber salget, hvor blot at være på niveau ikke er nok."
 ],
 [
  "Ordrekvalificerende",
  "De minimumskrav en virksomhed skal opfylde for overhovedet at komme i betragtning hos kunden (adgangsbillet). De vinder ikke ordren alene — uden dem er man bare ude."
 ],
 [
  "MTS (Make-to-Stock)",
  "Produktion mod lager ud fra prognose; varen er færdig før kunden bestiller. Kort leveringstid, men risiko for kurans/overlager. Egner sig til standardvarer med stabil efterspørgsel."
 ],
 [
  "ATO (Assemble-to-Order)",
  "Standardkomponenter ligger på lager og samles først, når ordren kommer. Giver variation til kunden uden lang ventetid. Mellemvej mellem MTS og MTO (fx PC-konfiguration)."
 ],
 [
  "MTO (Make-to-Order)",
  "Produktionen starter først, når kundeordren er modtaget. Lavt færdigvarelager og høj fleksibilitet, men længere leveringstid. Bruges ved kundetilpassede varer."
 ],
 [
  "ETO (Engineer-to-Order)",
  "Produktet både konstrueres og fremstilles til den enkelte ordre. Højest kundetilpasning og længst leveringstid (fx skibe, anlæg). Lager af færdigvarer findes reelt ikke."
 ],
 [
  "Lean",
  "Filosofi om at maksimere kundeværdi og fjerne spild (oprindeligt 7 spildtyper, TIMWOOD; ofte udvidet til 8 med uudnyttet medarbejderpotentiale). Mål: flow, træk (pull) og løbende forbedring (kaizen). Stammer fra Toyota Production System."
 ],
 [
  "Fordisme",
  "Masseproduktion på samlebånd med standardvarer og høj specialisering (Henry Ford). Lave stykomkostninger via skalafordele, men ringe fleksibilitet. Modsætning til Lean/kundetilpasning."
 ],
 [
  "Stykliste (BOM – Bill of Materials)",
  "Struktureret liste over alle komponenter, dele og mængder der indgår i et færdigt produkt. Grundlag for MRP-beregning og kalkulation. Kan være flerniveau (træstruktur)."
 ],
 [
  "Takt time",
  "Det tempo produktionen skal følge for at matche efterspørgslen = tilgængelig produktionstid / efterspurgt antal. Angiver hvor ofte én enhed skal være færdig. Synkroniserer flow med kundebehov."
 ],
 [
  "Flaskehals",
  "Den proces/ressource med lavest kapacitet, som begrænser hele systemets output. Bestemmer den maksimale gennemstrømning. Forbedringer uden for flaskehalsen øger ikke kapaciteten."
 ],
 [
  "OEE (Overall Equipment Effectiveness)",
  "Nøgletal for udstyrs effektivitet = Tilgængelighed × Ydelse × Kvalitet. Måler reelt udnyttet kapacitet mod teoretisk maksimum. Afslører tab fra stop, langsom drift og fejlemner."
 ],
 [
  "OTIF (On Time In Full)",
  "Leveringspræstation: andel ordrer leveret både til tiden OG i fuld mængde. Begge krav skal opfyldes for at tælle med. Centralt mål for kundeservice/leveringsevne."
 ],
 [
  "Littles Law",
  "WIP = gennemløbstid × gennemstrømning (throughput). Beskriver sammenhængen mellem igangværende arbejde, tid og output. Mindre WIP giver kortere gennemløbstid ved samme throughput."
 ],
 [
  "S&OP (Sales & Operations Planning)",
  "Taktisk planlægningsproces der typisk månedligt afstemmer salg/efterspørgsel med produktion/kapacitet og økonomi. Skaber én fælles plan på tværs af afdelinger. Mellemlangt sigte (typisk 3–18 mdr.)."
 ],
 [
  "MPS (Master Production Schedule)",
  "Hovedproduktionsplan der fastlægger hvilke færdigvarer der produceres hvornår og i hvilket antal. Bindeled mellem S&OP og MRP. Driver materialebehovsberegningen."
 ],
 [
  "ATP (Available-to-Promise)",
  "Den mængde der reelt kan loves en kunde på en given dato = lager + planlagt produktion − allerede reserverede ordrer. Bruges til realistiske leveringsløfter. Beregnes ud fra MPS."
 ],
 [
  "Gennemløbstid (lead time)",
  "Den samlede tid fra et emne/ordre starter til det er færdigt. Omfatter både værdiskabende tid og ventetid/transport. Kort gennemløbstid forbedrer leveringsevne og binder mindre kapital."
 ],
 [
  "WIP (Work in Process)",
  "Igangværende arbejde: varer der er påbegyndt men ikke færdige i produktionen. Binder kapital og forlænger gennemløbstid (jf. Littles Law). Lean stræber efter lavt WIP."
 ],
 [
  "Udnyttelsesgrad",
  "Hvor stor del af den tilgængelige kapacitet der faktisk bruges = faktisk benyttet tid / tilgængelig kapacitet. Høj grad giver god ressourceudnyttelse, men meget høj (~100 %) skaber kø og lange gennemløbstider."
 ],
 [
  "IRR (intern rente)",
  "Den rente hvor NPV = 0 — altså investeringens effektive forrentning. Investér hvis IRR > kalkulationsrenten."
 ],
 [
  "Payback (tilbagebetalingstid)",
  "Hvor lang tid der går, før investeringen er tjent hjem af de løbende indbetalinger. Kort payback = lav risiko, men ignorerer pengenes tidsværdi."
 ],
 [
  "Dækningsbidrag (DB)",
  "Salgspris minus variable omkostninger pr. enhed (eller omsætning minus variable omkostninger i alt). Det der er tilbage til at dække faste omkostninger og overskud."
 ],
 [
  "Dækningsgrad (DG)",
  "Dækningsbidrag i procent af omsætningen: DG = DB / omsætning × 100. Viser hvor stor en del af hver salgskrone der bidrager til faste omkostninger og overskud."
 ],
 [
  "Break-even (nulpunkt)",
  "Den afsætning hvor dækningsbidraget netop dækker de faste omkostninger, så resultatet er 0. Nulpunktsmængde = faste omkostninger / DB pr. stk."
 ],
 [
  "Sikkerhedsmargin",
  "Hvor meget afsætningen (eller omsætningen) kan falde, før man rammer break-even. Margin = (faktisk omsætning − break-even-omsætning) / faktisk omsætning × 100."
 ],
 [
  "Afkastningsgrad",
  "Resultatet af driften i forhold til den investerede kapital: Afkastningsgrad = driftsresultat (EBIT) / aktiver × 100. Virksomhedens samlede rentabilitet. = overskudsgrad × AOH."
 ],
 [
  "Overskudsgrad",
  "Driftsresultatets andel af omsætningen: Overskudsgrad = driftsresultat (EBIT) / omsætning × 100. Viser indtjeningsevnen pr. solgt krone."
 ],
 [
  "AOH (aktivernes omsætningshastighed)",
  "Hvor mange gange aktiverne 'omsættes' i salg: AOH = omsætning / aktiver. Viser hvor effektivt kapitalen udnyttes til at skabe omsætning."
 ],
 [
  "Soliditetsgrad",
  "Egenkapitalens andel af de samlede aktiver: Soliditetsgrad = egenkapital / aktiver × 100. Viser hvor godt virksomheden kan modstå tab — jo højere, jo mere robust."
 ],
 [
  "Likviditetsgrad",
  "Evnen til at betale kortfristet gæld. Likviditetsgrad 2 = omsætningsaktiver / kortfristet gæld × 100. Over 100 % betyder at omsætningsaktiverne dækker den korte gæld."
 ],
 [
  "Gearing",
  "Forholdet mellem fremmedkapital og egenkapital: Gearing = gæld / egenkapital. Høj gearing øger både mulig forrentning og finansiel risiko."
 ],
 [
  "Egenkapitalforrentning (ROE)",
  "Hvor godt ejernes kapital forrentes: ROE = årets resultat / egenkapital × 100. Påvirkes positivt af gearing, når afkastningsgraden er højere end lånerenten."
 ],
 [
  "DuPont-modellen",
  "Splitter rentabiliteten op i drivere: Afkastningsgrad = overskudsgrad × AOH. Viser om indtjeningen kommer fra høj margin eller hurtig kapitalomsætning."
 ],
 [
  "Lineær afskrivning",
  "Et aktiv afskrives med samme beløb hvert år over levetiden: Årlig afskrivning = (kostpris − scrapværdi) / levetid i år."
 ],
 [
  "Bidragskalkulation",
  "Kalkule der kun fordeler de variable omkostninger til produktet og lader dækningsbidraget dække de faste omkostninger samlet. Bruges til prissætning og kortsigtede beslutninger."
 ],
 [
  "Retrograd kalkulation",
  "Baglæns kalkule der starter med markedets salgspris og trækker avancer og omkostninger fra for at finde, hvad produktet må koste (målkostpris). Modsat den progressive 'fra-kostpris-til-pris'-metode."
 ],
 [
  "Normalfordeling",
  "Symmetrisk, klokkeformet fordeling om middelværdien. Beskrevet ved μ (middel) og σ (standardafvigelse); ca. 68 % af data ligger inden for ±1σ, 95 % inden for ±2σ."
 ],
 [
  "z-score",
  "Antal standardafvigelser en værdi ligger fra middelværdien. z = (x − μ) / σ; bruges til at sammenligne værdier og slå sandsynligheder op i normalfordelingen."
 ],
 [
  "Konfidensinterval",
  "Et interval, der med en given sikkerhed (fx 95 %) indeholder den sande værdi. Bredden afhænger af spredning og stikprøvestørrelse; fx x̄ ± z·(σ/√n) ved kendt σ."
 ],
 [
  "Standardafvigelse (σ / s)",
  "Mål for hvor meget data i gennemsnit afviger fra middelværdien. Kvadratroden af variansen; stor σ = stor spredning."
 ],
 [
  "Binomialfordeling",
  "Sandsynlighedsfordeling for antal succeser i n uafhængige ja/nej-forsøg med samme sandsynlighed p. Middel = n·p."
 ],
 [
  "Signifikansniveau (α)",
  "Grænsen for, hvornår et resultat anses for statistisk sikkert; typisk 5 % (0,05). Er p-værdien < α, forkastes nulhypotesen. α er også risikoen for at forkaste en sand nulhypotese."
 ],
 [
  "R² (forklaringsgrad)",
  "Andelen af variationen i y, som modellen forklarer; ligger mellem 0 og 1. R² = 0,8 betyder, at modellen forklarer 80 % af variationen."
 ],
 [
  "Korrelation (r)",
  "Mål for styrke og retning af en lineær sammenhæng mellem to variable. r ligger mellem −1 og +1; 0 = ingen lineær sammenhæng. Korrelation ≠ årsag."
 ],
 [
  "Lineær regression",
  "Metode der finder den bedste rette linje gennem data: y = a + b·x. b er hældningen (effekten af x), a er skæringen; bruges til at forudsige y ud fra x."
 ],
 [
  "Kontrolkort",
  "Diagram der over tid overvåger en proces mod en midterlinje og kontrolgrænser (UCL/LCL). Punkter inden for grænserne = normal variation; uden for = proces ude af kontrol."
 ],
 [
  "UCL / LCL",
  "Øvre og nedre kontrolgrænse i et kontrolkort, typisk middel ± 3 standardafvigelser. Punkter uden for grænserne signalerer en særårsag, der bør undersøges."
 ],
 [
  "p-kort",
  "Kontrolkort for andelen (p) af defekte enheder pr. stikprøve. Bruges ved tæl-data (godkendt/fejl) til at overvåge, om fejlandelen holder sig stabil."
 ],
 [
  "Særårsag",
  "Variation der skyldes en specifik, identificerbar hændelse (fx maskinfejl), ikke processens normale tilfældige udsving. Signaleres typisk af et punkt uden for kontrolgrænserne (eller af ikke-tilfældige mønstre) og skal undersøges."
 ],
 [
  "t-fordeling",
  "Klokkeformet fordeling med tungere haler end normalfordelingen; bruges ved små stikprøver eller ukendt σ. Nærmer sig normalfordelingen, når stikprøven vokser."
 ],
 [
  "Omkostningsleder (Cost leadership)",
  "Porter-strategi: vær branchens billigste producent og konkurrér på lav pris. Bygger på stordriftsfordele, høj effektivitet og stram omkostningsstyring."
 ],
 [
  "Differentiering",
  "Porter-strategi: tilbyd noget unikt (kvalitet, design, service, brand) som kunden vil betale ekstra for. Konkurrence på værdi frem for pris."
 ],
 [
  "Fokusstrategi (Niche)",
  "Porter-strategi: rettet mod ét snævert markedssegment, enten via lav pris (omkostningsfokus) eller unikhed (differentieringsfokus) i nichen."
 ],
 [
  "Ansoff (vækstmatrix)",
  "Fire vækststrategier ud fra produkt × marked: markedspenetrering (eksist./eksist.), markedsudvikling (eksist. produkt/nyt marked), produktudvikling (nyt produkt/eksist. marked) og diversifikation (nyt/nyt)."
 ],
 [
  "Diversifikation",
  "Ansoffs mest risikable felt: nyt produkt på nyt marked. Kan være beslægtet (synergi med kerneforretning) eller ubeslægtet (helt nyt område)."
 ],
 [
  "Kontrolspænd (Span of control)",
  "Antal medarbejdere en leder har direkte under sig. Smalt spænd = mange ledelseslag og tæt styring; bredt spænd = flad struktur og mere selvledelse."
 ],
 [
  "Linje vs. stab",
  "Linje = den styrende kommandovej med beslutningsret (chef → medarbejder). Stab = rådgivende specialister (fx HR, jura) uden direkte ordreret over linjen."
 ],
 [
  "Organisk vs. mekanistisk",
  "Burns & Stalker. Mekanistisk = stift, hierarkisk, regelstyret — godt i stabile omgivelser. Organisk = fleksibelt, fladt, decentralt — godt i foranderlige omgivelser."
 ],
 [
  "McGregor X/Y",
  "To menneskesyn hos ledere. Teori X: folk er dovne og skal kontrolleres/tvinges. Teori Y: folk er motiverede og ansvarlige og trives med selvstændighed."
 ],
 [
  "Scheins menneskesyn",
  "Fire syn på medarbejderen: det rationelt-økonomiske (motiveres af løn), det sociale (af fællesskab), det selvrealiserende (af udvikling) og det komplekse (skifter alt efter situation)."
 ],
 [
  "Ledergitteret (Blake & Mouton)",
  "Lederstil placeret i et gitter med to akser, hver fra 1 til 9: omsorg for produktion og omsorg for mennesker. Idealet er 9,9 = teamledelse med høj fokus på begge dele."
 ],
 [
  "Adizes PAEI",
  "Fire ledelsesroller der skal dækkes i et team: Producent (resultater), Administrator (orden/systemer), Entreprenør (nytænkning) og Integrator (sammenhold). Ingen kan det hele alene."
 ],
 [
  "Hofstede (kulturdimensioner)",
  "Måler nationale kulturforskelle på dimensioner som magtdistance, individualisme/kollektivisme, maskulinitet/femininitet, usikkerhedsundvigelse og langtids-/korttidsorientering."
 ],
 [
  "Interessentanalyse (magt-interesse)",
  "Værktøj der placerer interessenter i et magt/interesse-gitter (4 felter). Høj magt + høj interesse = styres tæt (key players); høj magt + lav interesse = hold tilfreds; lav magt + høj interesse = hold informeret; lav magt + lav interesse = overvåg minimalt."
 ],
 [
  "BATNA",
  "Best Alternative To a Negotiated Agreement: dit bedste alternativ, hvis forhandlingen bryder sammen. Jo stærkere BATNA, jo bedre forhandlingsmagt — det sætter den reelle bund for, hvad du vil acceptere."
 ],
 [
  "ZOPA",
  "Zone Of Possible Agreement: forhandlingsfeltet hvor parternes acceptområder overlapper, dvs. mellem købers og sælgers modstandspunkter. Findes ingen overlap, er en aftale ikke mulig."
 ],
 [
  "Målpunkt",
  "Det resultat du allerhelst vil opnå (dit ambitiøse mål/aspirationsniveau). Bør være realistisk men ambitiøst; sætter ankeret og styrer dit åbningsudspil."
 ],
 [
  "Modstandspunkt",
  "Walk-away-punkt: den dårligste pris/de dårligste vilkår du lige akkurat vil acceptere. Krydser modparten det, er det bedre at gå fra forhandlingen (brug din BATNA)."
 ],
 [
  "Principiel forhandling",
  "Harvard-metoden: forhandl ud fra interesser, ikke positioner. Adskil person fra sag, fokusér på interesser frem for positioner, find løsninger med gensidig gevinst, og brug objektive kriterier."
 ],
 [
  "Distributiv vs. integrativ forhandling",
  "Distributiv = nulsum (fast kage skal fordeles; den enes gevinst er den andens tab). Integrativ = win-win, hvor parterne udvider kagen ved at samarbejde om fælles interesser."
 ],
 [
  "Incoterms",
  "ICC's internationale leveringsklausuler (fx EXW, FOB, CIF, DDP). Fastlægger hvem der bærer omkostninger, risiko og pligter ved transporten — men IKKE ejendomsrettens overgang eller selve købsaftalen."
 ],
 [
  "EXW",
  "Ex Works (\"ab fabrik\"): sælger stiller blot varen klar på egen adresse. Køber bærer al risiko og alle omkostninger derfra. Mindst ansvar for sælger. Kan bruges ved alle transportformer."
 ],
 [
  "FOB",
  "Free On Board (kun sø-/indre vandvejstransport): sælger leverer og bærer risiko, til varen er om bord på skibet i afskibningshavnen. Derefter overgår risiko og omkostninger til køber."
 ],
 [
  "CIF",
  "Cost, Insurance and Freight (kun sø-/indre vandvejstransport): sælger betaler fragt + (minimums)forsikring til bestemmelseshavnen, men risikoen overgår til køber allerede, når varen er om bord ved afskibning."
 ],
 [
  "DDP",
  "Delivered Duty Paid: sælger leverer helt frem til aftalt sted og betaler ALT — fragt, importtold og afgifter. Maksimalt ansvar for sælger, minimalt for køber. Alle transportformer."
 ],
 [
  "DAP",
  "Delivered At Place: sælger bærer risiko og omkostninger frem til aftalt sted, klar til aflæsning (sælger aflæsser ikke). Køber står for importtold og afgifter. Alle transportformer."
 ],
 [
  "CISG",
  "Den internationale købelov (FN-konventionen CISG om aftaler om internationale løsørekøb). Fælles regelsæt for handelskøb mellem virksomheder i forskellige medlemslande; gælder som udgangspunkt, medmindre parterne fravælger den."
 ],
 [
  "Reklamation",
  "Købers meddelelse til sælger om, at varen er mangelfuld. Skal ske inden for rimelig tid efter, at manglen er eller burde være opdaget — ellers fortabes retten til at gøre manglen gældende."
 ],
 [
  "Mangel",
  "Når varen ikke svarer til det aftalte i mængde, kvalitet, art eller emballering. Udløser købers misligholdelsesbeføjelser: afhjælpning, omlevering, forholdsmæssigt afslag, ophævelse og/eller erstatning."
 ],
 [
  "Told / Duty",
  "Statslig afgift på varer, der importeres over en grænse. Beregnes typisk af varens værdi (toldsats %) ud fra varekode og oprindelsesland; fordyrer importen, og Incoterms afgør hvem der betaler."
 ]
]
