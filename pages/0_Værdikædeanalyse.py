"""Værdikædeanalyse — sådan bygges en VCA punkt for punkt.

Rammen om hele opslagsværktøjet: Porters værdikæde delt i støtteaktiviteter og
primære aktiviteter. Hver station har et kort hint i hverdagssprog + et link
videre til den regnemaskine eller det modelkatalog i de andre fag der hører til.

Indholdet er bygget 1:1 ud fra undervisernes skabelon "VCA for _.docx" — hvert
punkt og hver rækkefølge er bevaret, inkl. lærerens egne emfaser ("alle 6
punkter!!", "HUSK kun RVL", "Er der harmoni?").
"""
import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_theme import inject_css  # noqa: E402

st.set_page_config(page_title="Værdikædeanalyse", page_icon="🔗", layout="wide")
inject_css()

# Sider der kan linkes til (sti er relativ til Hjem.py)
PAGE_IND = "pages/1_Indkøb.py"
PAGE_PROD = "pages/2_Produktion.py"
PAGE_STAT = "pages/3_Statistik.py"
PAGE_OEKO = "pages/4_Økonomi.py"
PAGE_ORG = "pages/5_Organisation.py"
PAGE_KOMM = "pages/6_Kommunikation.py"

L_IND = (PAGE_IND, "Åbn i Indkøb", "🛒")
L_PROD = (PAGE_PROD, "Åbn i Produktion", "🏭")
L_STAT = (PAGE_STAT, "Åbn i Statistik", "📊")
L_ORG = (PAGE_ORG, "Åbn i Organisation", "🧭")
L_KOMM = (PAGE_KOMM, "Åbn i Kommunikation", "💬")


# ===========================================================================
# INDHOLD — bygget punkt for punkt efter undervisernes skabelon
# ===========================================================================
BLOKKE = [
    {
        "titel": "Støtteaktiviteter",
        "ikon": "🧱",
        "intro": "Rygraden der gør de primære aktiviteter mulige: hvordan virksomheden er "
                 "organiseret og ledet, dens folk, dens teknologi og dens indkøb. De skaber "
                 "ikke produktet direkte — men uden dem stopper kæden.",
        "omr": [
            {
                "navn": "Virksomhedens infrastruktur",
                "ikon": "🏛️",
                "intro": "Den overordnede ramme: hvordan virksomheden er bygget op og styret, "
                         "og om struktur og strategi spiller sammen.",
                "punkter": [
                    {
                        "navn": "Organisationsstruktur",
                        "forklar": "Hvordan ansvar og arbejde er fordelt. Tegn organisationen og "
                                   "karaktériser den ud fra:",
                        "under": [
                            "**Organisationsdiagram** — tegningen af hvem der refererer til hvem.",
                            "**Funktion/objekt** — er afdelinger delt efter *funktion* (alt indkøb "
                            "samlet ét sted) eller efter *objekt* (produkt, marked eller kunde)?",
                            "**Linie/Stab** — *linje* har beslutningsmagt; *stab* rådgiver (fx HR, jura).",
                            "**Funktionelle** — funktionsopdeling samler specialister (stordrift), "
                            "men skaber typisk silotænkning på tværs af afdelinger.",
                            "**Kontrolspænd** — hvor mange medarbejdere hver leder har under sig.",
                            "**Niveauer** — hvor mange lag i hierarkiet (flad vs. høj organisation).",
                            "**Afdelingernes placering** — hvor afdelingerne sidder i strukturen.",
                        ],
                        "link": L_ORG,
                        "soeg": ["organisationsstruktur", "organisationsdiagram", "funktion", "objekt",
                                 "linie", "linje", "stab", "kontrolspænd", "niveauer", "silo", "hierarki"],
                    },
                    {
                        "navn": "Strategi",
                        "forklar": "Hvilken strategi kører virksomheden — og passer delene sammen?",
                        "under": [
                            "**Virksomhedsstrategi (Porters generiske konkurrencestrategi)** — "
                            "omkostningsleder, differentiering eller fokus.",
                            "**Supply chain-strategi (generisk SC-strategi)** — lean/efficient "
                            "(billig, til stabil efterspørgsel) vs. responsiv/agil (hurtig, til "
                            "uforudsigelig efterspørgsel).",
                            "**Markedsplacering (Ansoff)** — markedspenetrering, markedsudvikling, "
                            "produktudvikling eller diversifikation.",
                        ],
                        "note": "❓ **Er der harmoni?** Spiller konkurrencestrategi, forsyningskæde "
                                "og vækstretning sammen — eller trækker de i hver sin retning? "
                                "At vurdere harmonien giver point.",
                        "link": L_ORG,
                        "soeg": ["strategi", "porter", "generisk", "konkurrencestrategi", "supply chain",
                                 "sc-strategi", "lean", "agil", "ansoff", "markedsplacering", "harmoni"],
                    },
                ],
            },
            {
                "navn": "HR (Human Resource)",
                "ikon": "👥",
                "intro": "Menneskene: kultur, ledelse, og hvordan folk fastholdes og motiveres.",
                "punkter": [
                    {
                        "navn": "Kultur",
                        "forklar": "Kulturtype, kultur på tværs af landegrænser, organisk/mekanistisk "
                                   "osv. — er kulturen *organisk* (flad, fleksibel) eller "
                                   "*mekanistisk* (regelstyret)? Og er der kulturforskelle mellem "
                                   "lande, der skaber friktion (Hofstede)?",
                        "link": L_ORG,
                        "soeg": ["kultur", "kulturtype", "organisk", "mekanistisk", "hofstede",
                                 "landegrænser", "international"],
                    },
                    {
                        "navn": "Ledelsesstile",
                        "forklar": "X/Y-syn, Scheins menneskesyn, ledergitter, Adizes, ledelsesstile "
                                   "— hvordan ser ledelsen på medarbejderne, og hvordan styrer den dem?",
                        "link": L_ORG,
                        "soeg": ["ledelse", "ledelsesstil", "teori x", "teori y", "mcgregor", "schein",
                                 "menneskesyn", "ledergitter", "blake", "mouton", "adizes", "paei"],
                    },
                    {
                        "navn": "Personaleomsætning",
                        "forklar": "Loyale medarbejdere eller stor udskiftning? Høj personaleomsætning "
                                   "koster penge og oplæring og tyder ofte på mistrivsel eller dårlig "
                                   "ledelse.",
                        "soeg": ["personaleomsætning", "loyale", "udskiftning", "fastholdelse", "trivsel"],
                    },
                    {
                        "navn": "Motivation",
                        "forklar": "Hvad driver medarbejderne — løn, fællesskab, faglig udvikling? "
                                   "Hænger tæt sammen med ledelsens menneskesyn (McGregor, Schein).",
                        "link": L_ORG,
                        "soeg": ["motivation", "drivkraft", "trivsel", "engagement"],
                    },
                    {
                        "navn": "Communication",
                        "forklar": "Hvordan kommunikeres der internt — åben dialog på tværs, eller "
                                   "envejs top-down? Dårlig intern kommunikation forstærker "
                                   "silotænkning.",
                        "link": L_KOMM,
                        "soeg": ["kommunikation", "communication", "intern", "dialog", "information"],
                    },
                ],
            },
            {
                "navn": "Teknologi",
                "ikon": "💻",
                "intro": "Virksomhedens systemer og teknologiniveau.",
                "punkter": [
                    {
                        "navn": "IT-systemer",
                        "forklar": "ERP og andre IT-systemer — har de ét samlet ERP-system, der binder "
                                   "indkøb, lager, produktion og økonomi sammen? Andre systemer som "
                                   "CRM (kunder) eller WMS (lager)?",
                        "soeg": ["it", "it-systemer", "erp", "crm", "wms", "system"],
                    },
                    {
                        "navn": "Teknologi ift. især produktion og lager",
                        "forklar": "Høj eller lav teknologisk — er produktion og lager højt "
                                   "automatiseret (robotter, automatlager) eller manuelt drevet?",
                        "soeg": ["teknologi", "automatisering", "produktion", "lager", "højteknologisk",
                                 "lavteknologisk"],
                    },
                ],
            },
            {
                "navn": "Indkøb",
                "ikon": "🛒",
                "intro": "Hvordan virksomheden køber ind og styrer sine leverandører.",
                "punkter": [
                    {
                        "navn": "Strategi",
                        "forklar": "Den overordnede tilgang til leverandører:",
                        "under": [
                            "**Transaktionsomkostnings-perspektiv (TCE) / netværksperspektiv (N)** — "
                            "ser de indkøb som rene markedshandler (køb billigst, skift frit) eller "
                            "som langvarige relationer og netværk?",
                            "**Relation til leverandør – Bensaou** — placér leverandørerne i Bensaous "
                            "matrix (markedsudveksling, captive buyer, captive supplier, strategisk "
                            "partner) efter hvem der har investeret mest i forholdet (fx en lille "
                            "standardskrue købt af mange = *markedsudveksling*; en skræddersyet "
                            "nøglekomponent fra én leverandør = *strategisk partnerskab*).",
                            "**Exit/voice** — reagerer virksomheden på en dårlig leverandør ved at "
                            "*skifte* (exit) eller ved at *tale og forbedre* forholdet (voice)?",
                        ],
                        "link": L_IND,
                        "soeg": ["indkøb", "strategi", "tce", "transaktionsomkostninger", "netværk",
                                 "bensaou", "relation", "exit", "voice"],
                    },
                    {
                        "navn": "Finde nye leverandører",
                        "forklar": "Gøres dette — og hvordan? Leder virksomheden aktivt efter nye "
                                   "leverandører (udbud, screening, markedsovervågning), eller bliver "
                                   "den hos de gamle?",
                        "link": L_IND,
                        "soeg": ["finde", "nye leverandører", "udbud", "screening", "sourcing"],
                    },
                    {
                        "navn": "Leverandørvalg",
                        "forklar": "Hvordan vælges den enkelte leverandør?",
                        "under": [
                            "**Ordrevinder vs. ordrekvalificerende** — hvilke krav skal en leverandør "
                            "bare opfylde for at komme i betragtning (kvalificerende), og hvad *vinder* "
                            "ordren (fx pris, kvalitet eller leveringstid)?",
                            "**Enkelt / flere / dobbelt / kryds-sourcing** — bruges der én eller flere "
                            "leverandører pr. vare, og hvorfor (sikkerhed vs. pris/stordrift)?",
                        ],
                        "link": L_IND,
                        "soeg": ["leverandørvalg", "ordrevinder", "ordrekvalificerende", "order winner",
                                 "qualifier", "single", "dual", "sourcing", "kryds"],
                    },
                    {
                        "navn": "Evaluering af leverandør",
                        "forklar": "Gøres dette — og hvordan? Måler virksomheden leverandørerne "
                                   "løbende (leveringspræcision, kvalitet, pris) med fx en vægtet "
                                   "leverandørscore?",
                        "link": (PAGE_IND, "Leverandørscore (Indkøb)", "🛒"),
                        "soeg": ["evaluering", "leverandørevaluering", "leverandørscore", "vægtet",
                                 "kriterier", "kpi"],
                    },
                ],
            },
        ],
    },
    {
        "titel": "Primære aktiviteter",
        "ikon": "⚙️",
        "intro": "Selve vejen produktet tager — fra råvaren kommer ind, gennem produktionen, ud "
                 "til kunden, og videre med salg og service. Det er her værdien fysisk skabes.",
        "omr": [
            {
                "navn": "Logistik ind (indgående)",
                "ikon": "📥",
                "intro": "Fra leverandøren til virksomhedens dør.",
                "punkter": [
                    {
                        "navn": "Disponering (materialeflow-opstart)",
                        "forklar": "Hvordan disponeres de råvarer, der er lavet aftale om? "
                                   "(rammeaftale) — altså hvordan udløser/hjemkalder virksomheden "
                                   "varer på en allerede indgået aftale, og hvad styrer hvornår der "
                                   "bestilles.",
                        "link": (PAGE_IND, "Genbestilling & review-systemer (Indkøb)", "🛒"),
                        "soeg": ["disponering", "materialeflow", "rammeaftale", "hjemkald", "genbestilling"],
                    },
                    {
                        "navn": "Transport ind",
                        "forklar": "Transportform/-måde fra leverandør til virksomhed / Incoterms — "
                                   "hvordan fragtes varerne ind, og på hvilke vilkår? Incoterms "
                                   "afgør hvem der bærer risiko og omkostning undervejs — fx *DDP* "
                                   "(leverandøren betaler og bærer risikoen helt til din dør) vs. "
                                   "*EXW* (du henter selv på leverandørens fabrik).",
                        "soeg": ["transport ind", "transportform", "incoterms", "fragt", "indgående"],
                    },
                    {
                        "navn": "Varemodtagelse",
                        "forklar": "Hvordan er ankomsten? Er der kvalitetskontrol ved modtagelse "
                                   "(fx stikprøve af et parti, før det godkendes til lager)?",
                        "link": (PAGE_STAT, "Kontrolkort / stikprøve (Statistik)", "📊"),
                        "soeg": ["varemodtagelse", "ankomst", "kvalitetskontrol", "stikprøve", "modtagekontrol"],
                    },
                    {
                        "navn": "Lager",
                        "forklar": "Styres/ledes lageret? **(HUSK: kun råvarelager, RVL)** — hvordan "
                                   "styres råvarelageret: niveauer, sikkerhedslager, hvor meget "
                                   "kapital der er bundet?",
                        "link": (PAGE_IND, "Lagerstyring & EOQ (Indkøb)", "🛒"),
                        "soeg": ["lager", "råvarelager", "rvl", "sikkerhedslager", "lagerstyring"],
                    },
                ],
            },
            {
                "navn": "Produktion / fremstilling / operations",
                "ikon": "🏭",
                "intro": "⚠️ I skal lave alle 6 punkter!! — beskriv produktionen på alle seks "
                         "dimensioner herunder.",
                "punkter": [
                    {
                        "navn": "Produkttype",
                        "forklar": "Standard ↔ kundetilpasset — er produktet ens for alle, eller "
                                   "skræddersyet til hver kunde?",
                        "link": L_PROD,
                        "soeg": ["produkttype", "standard", "kundetilpasset", "skræddersyet"],
                    },
                    {
                        "navn": "Ordretype",
                        "forklar": "MTS, ATO, MTO, ETO — produceres der til lager (Make-To-Stock, "
                                   "fx mælk på hylden), samles kendte dele til ordre "
                                   "(Assemble-To-Order, fx en computer der konfigureres), laves til "
                                   "ordre (Make-To-Order, fx en specialmaskine) eller udvikles helt "
                                   "fra bunden til ordre (Engineer-To-Order, fx et broprojekt)?",
                        "link": L_PROD,
                        "soeg": ["ordretype", "mts", "ato", "mto", "eto", "make to stock", "make to order"],
                    },
                    {
                        "navn": "Produktionsfilosofi",
                        "forklar": "Lean eller Fordisme — *Lean* fjerner spild og er fleksibel; "
                                   "*Fordisme* er masseproduktion af standardvarer i store mængder.",
                        "link": L_PROD,
                        "soeg": ["produktionsfilosofi", "lean", "fordisme", "masseproduktion", "spild"],
                    },
                    {
                        "navn": "Produktionsstyring",
                        "forklar": "MRP, JIT (Just In Time) — planlægges produktionen ud fra "
                                   "materialebehov (MRP, skub) eller trækkes varer ind lige når der "
                                   "er brug for dem (JIT, træk)?",
                        "link": L_PROD,
                        "soeg": ["produktionsstyring", "mrp", "jit", "just in time", "skub", "træk"],
                    },
                    {
                        "navn": "Produktionsformer",
                        "forklar": "Jobshop, serie, flow/masse, enkeltstyk/projekt — hvor stor og "
                                   "ensartet er produktionen (fra enkeltstykker til løbende masseflow)?",
                        "link": L_PROD,
                        "soeg": ["produktionsform", "jobshop", "serie", "flow", "masse", "enkeltstyk",
                                 "projekt"],
                    },
                    {
                        "navn": "Produktionslayout",
                        "forklar": "Fast plads, linje, funktion, gruppe — hvordan er maskiner og "
                                   "arbejdsstationer fysisk placeret i forhold til hinanden?",
                        "link": L_PROD,
                        "soeg": ["produktionslayout", "fast plads", "linje", "funktion", "gruppe", "layout"],
                    },
                ],
            },
            {
                "navn": "Logistik ud (udgående / outbound)",
                "ikon": "📤",
                "intro": "Fra færdigvare til kundens dør.",
                "punkter": [
                    {
                        "navn": "Kundeordrebehandling",
                        "forklar": "Leveringsserviceniveau, ordre ind, beskæftigelse — hvordan "
                                   "håndteres kundeordrer fra de kommer ind, og hvilket serviceniveau "
                                   "lover virksomheden kunderne?",
                        "link": (PAGE_PROD, "Perfect Order / OTIF (Produktion)", "🏭"),
                        "soeg": ["kundeordrebehandling", "leveringsservice", "ordre ind", "beskæftigelse",
                                 "serviceniveau"],
                    },
                    {
                        "navn": "FVL — færdigvarelager",
                        "forklar": "Lagerservicegraden — hvor stor en del af kundeordrerne kan dækkes "
                                   "direkte fra færdigvarelageret uden ventetid?",
                        "link": (PAGE_IND, "Servicegrad & sikkerhedslager (Indkøb)", "🛒"),
                        "soeg": ["fvl", "færdigvarelager", "lagerservicegrad", "servicegrad", "fyldningsgrad"],
                    },
                    {
                        "navn": "Pluk og pak",
                        "forklar": "Håndteringsomkostninger — hvordan plukkes og pakkes ordrer på "
                                   "lageret, og hvad koster den håndtering?",
                        "soeg": ["pluk", "pak", "plukning", "håndtering", "håndteringsomkostninger"],
                    },
                    {
                        "navn": "Transport ud",
                        "forklar": "Transportform, Incoterms — hvordan og på hvilke vilkår leveres "
                                   "til kunden (hvem bærer risiko og fragt — Incoterms)?",
                        "soeg": ["transport ud", "transportform", "incoterms", "udgående", "levering"],
                    },
                ],
            },
            {
                "navn": "Marketing og salg",
                "ikon": "📣",
                "intro": "Hvordan kunder håndteres, og hvor hurtigt virksomheden kommer til markedet.",
                "punkter": [
                    {
                        "navn": "ABC-klassificering",
                        "forklar": "Behandles store og små kunder ens eller forskelligt? "
                                   "(differentieringsstrategi) — del kunderne (eller varerne) op efter "
                                   "betydning: A er de vigtigste, og de bør have mest opmærksomhed.",
                        "link": (PAGE_IND, "ABC / Pareto (Indkøb)", "🛒"),
                        "soeg": ["abc", "abc-klassificering", "pareto", "80/20", "differentiering",
                                 "store kunder", "små kunder"],
                    },
                    {
                        "navn": "Time to market",
                        "forklar": "Den tid det tager fra idé til et nyt produkt er på markedet. Kort "
                                   "time to market er en fordel i hurtige markeder.",
                        "soeg": ["time to market", "udviklingstid", "lancering", "nyt produkt"],
                    },
                    {
                        "navn": "Tidselementer",
                        "forklar": "Lead time og leveringstid — leveringstiden kunden oplever vs. "
                                   "virksomhedens egen gennemløbstid internt.",
                        "link": (PAGE_PROD, "Little's Law / gennemløbstid (Produktion)", "🏭"),
                        "soeg": ["tidselementer", "lead time", "leveringstid", "gennemløbstid", "leadtime"],
                    },
                ],
            },
            {
                "navn": "Service",
                "ikon": "🛟",
                "intro": "Det der sker efter salget, når varen kommer tilbage.",
                "punkter": [
                    {
                        "navn": "Returvarer",
                        "forklar": "Varen fejler ikke noget — kunden sender en fejlfri vare retur "
                                   "(fortrydelse, forkert bestilling, for mange). Hvordan håndteres "
                                   "returneringen og varen bagefter?",
                        "soeg": ["returvarer", "retur", "returnering", "fortrydelse", "fejler ikke"],
                    },
                    {
                        "navn": "Reklamationer",
                        "forklar": "Varen fejler noget — kunden klager over en defekt. Hvordan "
                                   "håndteres garanti, ombytning eller erstatning, og hvad lærer "
                                   "virksomheden af klagerne?",
                        "soeg": ["reklamationer", "reklamation", "klage", "defekt", "garanti", "fejler noget"],
                    },
                ],
            },
        ],
    },
    {
        "titel": "Rapportens sidste dele",
        "ikon": "📄",
        "intro": "Når kæden er gået igennem, samles trådene og dokumentationen.",
        "omr": [
            {
                "navn": "Afslutning og dokumentation",
                "ikon": "🧩",
                "intro": "",
                "punkter": [
                    {
                        "navn": "Liste af udfordringer",
                        "forklar": "Saml de problemer du fandt undervejs ét sted: en liste over "
                                   "virksomhedens udfordringer (fx silotænkning, høj "
                                   "personaleomsætning, dårlig leveringspræcision, manglende "
                                   "harmoni). Her *identificerer* du problemerne — selve "
                                   "løsningerne og anbefalingerne skrives i en separat del bagefter, "
                                   "**ikke inde i værdikæden**. Listen binder analysen sammen og er "
                                   "afsættet for konklusionen.",
                        "soeg": ["udfordringer", "liste af udfordringer", "problemer", "konklusion"],
                    },
                    {
                        "navn": "Referenceliste",
                        "forklar": "De kilder du har brugt (lærebøger, modeller, virksomhedens eget "
                                   "materiale). Henvis korrekt undervejs i teksten, så analysen er "
                                   "dokumenteret og troværdig.",
                        "soeg": ["referenceliste", "kilder", "litteratur", "henvisning"],
                    },
                    {
                        "navn": "Bilag",
                        "forklar": "Tunge udregninger, store tabeller og figurer lægges bagest som "
                                   "bilag, så selve teksten forbliver læsbar. Henvis til dem fra "
                                   "teksten (fx \"se bilag 3\").",
                        "soeg": ["bilag", "bilagene", "tabeller", "figurer", "appendiks"],
                    },
                ],
            },
        ],
    },
]


# ===========================================================================
# RENDER
# ===========================================================================
st.title("🔗 Værdikædeanalyse")
st.caption("Hvordan en værdikædeanalyse bygges punkt for punkt — Porters værdikæde, station for "
           "station. Hvert punkt har et hint i hverdagssprog og et link videre til regnemaskinen "
           "eller modelkataloget der hører til.")

st.info("**ALT HERINDE BØR BRUGES** — så længe du har oplysningerne, der er relevante fra den "
        "pågældende virksomhed. Mangler du data til en station, så spring den over; du behøver "
        "ikke presse alle punkter ind for enhver pris.", icon="🧭")

st.warning("**Værdikæden er en *analyse* — ikke løsninger.** Du beskriver og vurderer, hvordan "
           "virksomheden faktisk gør på hver station (styrker, svagheder, og om det passer med "
           "strategien). Skriv **aldrig løsningsforslag ind i selve værdikæden** — fx ikke \"de bør "
           "skifte til JIT\". Problemerne du finder, noteres i **Liste af udfordringer**, og selve "
           "løsningerne/anbefalingerne kommer i en separat del *bagefter*. Hold kæden beskrivende "
           "og analyserende.", icon="⚠️")

with st.expander("🧭 Sådan skriver du en station — metode + eksempel"):
    st.markdown(
        "Hver station skrives i samme rytme:\n"
        "1. **Beskriv** hvad virksomheden gør (fakta fra casen).\n"
        "2. **Kobl til en model/begreb** (fx ordretype = MTO, relation = Bensaou).\n"
        "3. **Vurdér** — er det en styrke eller en svaghed? Passer det med strategien "
        "(*harmoni*)? Hvilken udfordring skaber det?\n"
        "4. **Ingen løsning her.** Udfordringen ryger på listen; anbefalingen skrives bagefter."
    )
    st.markdown("**Eksempel — Produktionsstyring:**")
    st.error("❌ *Løsning i kæden (forkert):* “Virksomheden bør indføre JIT for at nedbringe "
             "lageret.”")
    st.success("✅ *Analyse (rigtigt):* “Produktionen styres efter MRP, hvor der planlægges ud "
               "fra forventet behov. Det binder kapital i råvarelageret og passer dårligt med den "
               "responsive konkurrencestrategi — altså manglende harmoni. Det høje lager er en "
               "svaghed, som noteres i listen af udfordringer.”")

soeg = st.text_input(
    "🔍 Søg i værdikæden",
    placeholder="fx Bensaou, Ansoff, MRP, Incoterms, ABC, lager, harmoni …",
    key="vca_soeg",
).lower().strip()


def punkt_match(p):
    if not soeg:
        return True
    dele = [p["navn"], p.get("forklar", ""), p.get("note", "")]
    dele += p.get("under", [])
    dele += p.get("soeg", [])
    return soeg in " ".join(dele).lower()


def vis_punkt(p):
    st.markdown(f"**{p['navn']}**")
    if p.get("forklar"):
        st.markdown(p["forklar"])
    if p.get("under"):
        st.markdown("\n".join(f"- {u}" for u in p["under"]))
    if p.get("note"):
        st.markdown(p["note"])
    if p.get("link"):
        sti, label, ikon = p["link"]
        st.page_link(sti, label=label, icon=ikon)


total = 0
for blok in BLOKKE:
    synlige = []
    for omr in blok["omr"]:
        pk = [p for p in omr["punkter"] if punkt_match(p)]
        if pk:
            synlige.append((omr, pk))
    if not synlige:
        continue

    st.header(f"{blok['ikon']} {blok['titel']}")
    if not soeg and blok.get("intro"):
        st.caption(blok["intro"])

    for omr, pk in synlige:
        with st.container(border=True):
            st.markdown(f"#### {omr['ikon']} {omr['navn']}")
            if not soeg and omr.get("intro"):
                st.caption(omr["intro"])
            for i, p in enumerate(pk):
                total += 1
                vis_punkt(p)
                if i < len(pk) - 1:
                    st.markdown("")

if soeg and total == 0:
    st.info("Ingen stationer matchede søgningen. Prøv et andet ord (fx 'leverandør', 'lager', "
            "'ordretype').")
elif soeg:
    st.caption(f"{total} station"
               f"{'er' if total != 1 else ''} matcher. Ryd søgefeltet for at se hele kæden.")

st.divider()
st.caption("🤖 Bygget med Claude ud fra dit eget dokument *VCA for _.docx* (undervisernes "
           "skabelon). Hvert punkt fra dokumentet er med, i samme rækkefølge, og lærerens "
           "emfaser er bevaret. Links fører videre til regnemaskinerne og modelkatalogerne i de "
           "andre fag.")
