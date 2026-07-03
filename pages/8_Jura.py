"""Jura — søgbart opslagskatalog for indkøbsjura (ingen regnemaskiner).

Blødt fag: Incoterms med risikoens overgangspunkt, CISG-beføjelser og frister,
vedtagelse af standardvilkår og krav mod transportøren. Hvert opslag følger
jura-mønstret "Hvad den siger" + "Hvorfor her", forklaret generelt med neutrale
eksempler, så det kan bruges til en hvilken som helst opgave eller tvist.
Artikelhenvisningerne er CISG (den internationale købelov); Incoterms er 2020.
"""
import os
import sys

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_theme import inject_css, vis_fig, C_TOTAL, C_ORDER, C_OPT  # noqa: E402

st.set_page_config(page_title="Jura", page_icon="⚖️", layout="wide")
inject_css()

st.title("⚖️ Jura")
st.caption("Indkøbsjura som opslagsværk: Incoterms (hvor går risikoen over?), CISG's "
           "beføjelser og frister, og hvornår standardvilkår overhovedet gælder. "
           "Hvert opslag har **Hvad den siger** (reglen) + **Hvorfor her** (hvornår den "
           "rammer, med et neutralt eksempel). Jura er et argument-fag: censor vil høre "
           "reglen, fakta og din kobling — sjældent bare et facit.")

# ===========================================================================
# DATA — Incoterms 2020 (alle 11) på en fælles transport-tidslinje
# ===========================================================================
# 'risiko_punkt' = hvor RISIKOEN springer fra sælger til køber (det juridisk vigtige).
# 'omk_punkt'    = hvor SÆLGER holder op med at betale (fragt/forsikring).
# For C-gruppen er de to FORSKELLIGE — det er hele fælden.
TRIN = ["Sælgers\nlager", "Overdraget til\nfragtfører", "Langs skibet\n(kaj)",
        "Om bord\npå skibet", "Ankomst-\nhavn", "Hos køber\n(destination)"]

# familie: E/F/C/D · mode: "alle" (enhver transportform) eller "sø" (kun sø/indre vandvej)
INCOTERMS = [
    {
        "kode": "EXW", "navn": "EXW — Ex Works (ab fabrik)", "familie": "E", "mode": "alle",
        "risiko_punkt": 0, "omk_punkt": 0,
        "risiko": "Risikoen overgår allerede når varen er **stillet til rådighed på sælgers "
                  "adresse** — køber står selv for læsning, transport, eksport og import.",
        "siger": "Sælgers mindste forpligtelse: gøre varen klar på eget lager. Alt derfra — "
                 "læsning, fragt, forsikring, told — er købers problem og risiko.",
        "her": "Modpolen til DDP. Brug EXW/DDP som yderpunkterne når du forklarer, hvor meget "
               "ansvar parterne hver især har taget på sig.",
        "soeg": ["exw", "ex works", "ab fabrik", "afhentning"],
    },
    {
        "kode": "FCA", "navn": "FCA — Free Carrier", "familie": "F", "mode": "alle",
        "risiko_punkt": 1, "omk_punkt": 1,
        "risiko": "Risikoen overgår når varen er **overdraget til den fragtfører, køber har "
                  "udpeget** (på sælgers plads eller et aftalt sted). Enhver transportform.",
        "siger": "Sælger klarer eksport og læsser (hvis afhentning sker hos ham); derfra bærer "
                 "køber fragt og risiko. FCA er 'container-versionen' af FOB — den rigtige at "
                 "bruge, når godset går i container og overdrages i en terminal, ikke om bord.",
        "her": "Til enhver transportform (vej, bane, fly, container). Vælg FCA frem for FOB når "
               "godset overdrages FØR skibet — fx i en containerterminal.",
        "soeg": ["fca", "free carrier", "fragtfører", "container", "terminal", "enhver transportform"],
    },
    {
        "kode": "FAS", "navn": "FAS — Free Alongside Ship", "familie": "F", "mode": "sø",
        "risiko_punkt": 2, "omk_punkt": 2,
        "risiko": "Risikoen overgår når varen er **stillet langs skibets side (på kajen)** i "
                  "afskibningshavnen. Kun sø- og indre vandvejstransport.",
        "siger": "Sælger leverer varen ved skibssiden; derfra betaler og bærer køber lastning, "
                 "søfragt og risiko. Bruges typisk til bulk/stykgods der ikke lastes med kran "
                 "som containere.",
        "her": "Sø-only. Mellemtrin mellem EXW og FOB: sælger når helt ned til kajen, men "
               "lastningen om bord er købers.",
        "soeg": ["fas", "free alongside ship", "kaj", "langs skibet", "søtransport"],
    },
    {
        "kode": "FOB", "navn": "FOB — Free On Board", "familie": "F", "mode": "sø",
        "risiko_punkt": 3, "omk_punkt": 3,
        "risiko": "Risikoen overgår når varen er **om bord på skibet i afskibningshavnen**. "
                  "Kun søtransport.",
        "siger": "Sælger leverer om bord på det skib, køber har udpeget. Fra det øjeblik bærer "
                 "køber risikoen og betaler hovedtransport — forsikring er KØBERS eget valg.",
        "her": "Typisk fælde: 'FOB afskibningshavn', og godset går tabt OVER havet (efter "
               "lastning) → købers risiko. Vil køber sikres bedre, så vælg CIF/CIP eller DAP/DDP.",
        "soeg": ["fob", "free on board", "om bord", "container", "overbord", "søtransport"],
    },
    {
        "kode": "CFR", "navn": "CFR — Cost and Freight", "familie": "C", "mode": "sø",
        "risiko_punkt": 3, "omk_punkt": 4,
        "risiko": "**Split:** risikoen overgår allerede når varen er **om bord** (som FOB) — "
                  "men sælger BETALER fragten helt til **ankomsthavnen**. Kun søtransport.",
        "siger": "Sælger betaler søfragten til ankomsthavnen, men risikoen er købers fra "
                 "lastningen. Ingen forsikring (det er forskellen til CIF).",
        "her": "C-gruppens kerne: omkostning og risiko følges IKKE ad. Sælger betaler langt, "
               "men hæfter ikke for et tab undervejs.",
        "soeg": ["cfr", "cost and freight", "fragt", "split", "søtransport"],
    },
    {
        "kode": "CIF", "navn": "CIF — Cost, Insurance & Freight", "familie": "C", "mode": "sø",
        "risiko_punkt": 3, "omk_punkt": 4,
        "risiko": "**Split (som CFR + forsikring):** risikoen overgår **om bord**, men sælger "
                  "betaler fragt OG tegner søforsikring til **ankomsthavnen**. Kun søtransport.",
        "siger": "Som CFR, men sælger tegner også (minimums-)forsikring til fordel for køber. "
                 "Risikoen er stadig købers fra lastningen — forsikringen dækker bare tabet.",
        "her": "Den klassiske eksamensfælde: 'sælger betaler til ankomst, så bærer sælger vel "
               "risikoen?' Nej — går godset tabt undervejs, er det købers risiko, men køber kan "
               "trække på den forsikring, sælger har tegnet.",
        "soeg": ["cif", "cost insurance freight", "forsikring", "fragt", "split", "søtransport"],
    },
    {
        "kode": "CPT", "navn": "CPT — Carriage Paid To", "familie": "C", "mode": "alle",
        "risiko_punkt": 1, "omk_punkt": 5,
        "risiko": "**Split, ekstra tidligt:** risikoen overgår allerede når varen er "
                  "**overdraget til FØRSTE fragtfører** — men sælger betaler fragten helt til "
                  "**destinationen**. Enhver transportform.",
        "siger": "CPT er FCA + sælger betaler hovedfragten. Men risikoen springer meget tidligt "
                 "(ved første fragtfører), selvom sælger betaler hele vejen frem.",
        "her": "Den største 'gotcha': her er afstanden mellem risiko (tidligt) og omkostning "
               "(destination) størst. Køber bærer risiko på en transport, sælger betaler for.",
        "soeg": ["cpt", "carriage paid to", "fragtfører", "split", "enhver transportform"],
    },
    {
        "kode": "CIP", "navn": "CIP — Carriage & Insurance Paid To", "familie": "C", "mode": "alle",
        "risiko_punkt": 1, "omk_punkt": 5,
        "risiko": "**Som CPT + forsikring:** risikoen overgår ved **første fragtfører**, men "
                  "sælger betaler fragt OG tegner forsikring til **destinationen**. Enhver form.",
        "siger": "CIP er CPT med forsikring — og i Incoterms 2020 skal forsikringen være den "
                 "høje dækning (Institute Cargo Clauses A), modsat CIF's minimumsdækning.",
        "her": "Container-versionen af CIF. Vælg CIP frem for CIF når godset ikke går som "
               "søfragt om bord, men i container/multimodal transport.",
        "soeg": ["cip", "carriage insurance paid", "forsikring", "container", "split"],
    },
    {
        "kode": "DAP", "navn": "DAP — Delivered At Place", "familie": "D", "mode": "alle",
        "risiko_punkt": 5, "omk_punkt": 5,
        "risiko": "Risikoen overgår når varen er **ankommet til det aftalte sted, klar til "
                  "aflæsning** hos køber (køber aflæsser selv). Enhver transportform.",
        "siger": "Sælger bærer transport og risiko hele vejen til destinationen — men køber "
                 "aflæsser og klarer selv importtold og -moms.",
        "her": "Mellemtrin i D-gruppen: mere sælgeransvar end C/F-termerne, men uden DDP's "
               "told-forpligtelse. Forskellen til DPU er kun, hvem der aflæsser.",
        "soeg": ["dap", "delivered at place", "destination", "aflæsning", "told"],
    },
    {
        "kode": "DPU", "navn": "DPU — Delivered At Place Unloaded", "familie": "D", "mode": "alle",
        "risiko_punkt": 5, "omk_punkt": 5,
        "risiko": "Risikoen overgår først når varen er **ankommet OG aflæsset** på det aftalte "
                  "sted. Enhver transportform. (Hed DAT i Incoterms 2010.)",
        "siger": "Den ENESTE Incoterm hvor sælger også skal AFLÆSSE varen på destinationen. "
                 "Ellers som DAP: køber klarer importtold.",
        "her": "Nyt navn i 2020 (tidligere DAT). Vælg DPU frem for DAP når det er vigtigt, at "
               "sælger står for aflæsningen — fx tungt gods der kræver sælgers udstyr.",
        "soeg": ["dpu", "delivered at place unloaded", "dat", "aflæsset", "2020"],
    },
    {
        "kode": "DDP", "navn": "DDP — Delivered Duty Paid ⭐", "familie": "D", "mode": "alle",
        "risiko_punkt": 5, "omk_punkt": 5,
        "risiko": "Risikoen overgår først når varen er **stillet til rådighed hos køber på "
                  "destinationen** — og sælger har også betalt **told og importafgifter**.",
        "siger": "Sælgers STØRSTE forpligtelse: alle omkostninger og al risiko — inkl. told og "
                 "importafgifter — indtil varen står klar hos køber.",
        "her": "Typisk fælde: 'DDP destinationsby', og traileren vælter FØR destinationen → "
               "risikoen er endnu ikke overgået, så SÆLGER bærer tabet og skal omlevere. "
               "'Risikoen overgik da varen forlod lageret' er forkert under DDP.",
        "soeg": ["ddp", "delivered duty paid", "risikoovergang", "told", "omlevering"],
    },
]

FAM_NAVN = {"E": "E — afhentning", "F": "F — hovedfragt betales af køber",
            "C": "C — hovedfragt betales af sælger (men risiko tidligt)",
            "D": "D — ankomst (sælger bærer helt frem)"}

# ===========================================================================
# DATA — jurakatalog ("Hvad den siger" + "Hvorfor her")
# ===========================================================================
K_INCO = "Incoterms & transport"
K_FRIST = "CISG: mangler & frister"
K_OPH = "CISG: ophævelse & erstatning"
K_VILKAAR = "Standardvilkår & aftalen"

JURA = [
    {
        "navn": "Incoterms 2020 — hvad de regulerer (og ikke regulerer)",
        "kat": K_INCO,
        "siger": "Standardklausuler der fordeler **omkostninger, risiko og opgaver** (transport, "
                 "forsikring, told) mellem køber og sælger. De regulerer IKKE ejendomsret, "
                 "betaling eller misligholdelse — det gør kontrakten og CISG.",
        "her": "Start altid med at finde Incoterm-klausulen i kontrakten (fx 'DDP destinationsby' "
               "eller 'FOB afskibningshavn') — den afgør, hvem der bærer tabet ved en "
               "transportskade. Uden en klausul falder man tilbage på kontraktens øvrige vilkår "
               "og CISG.",
        "soeg": ["incoterms", "2020", "risiko", "klausul", "leveringsbetingelser"],
    },
    {
        "navn": "Krav mod transportøren under DDP (CMR-loven)",
        "kat": K_INCO,
        "siger": "International landevejstransport er reguleret af **CMR-loven**: fragtføreren "
                 "hæfter for skade på godset undervejs, men med en **vægtbaseret "
                 "ansvarsbegrænsning** — den fulde fakturaværdi dækkes ikke nødvendigvis.",
        "her": "Når en part både bærer risikoen (fx som DDP-sælger) OG har indgået "
               "transportaftalen, er det **den part — ikke modparten — der kravstiller mod "
               "fragtføreren**. Kæden er: sælger hæfter over for køber (fx omlevering) og søger "
               "derefter sit tab dækket hos fragtføreren efter CMR — men den vægtbaserede "
               "begrænsning kan betyde, at han ikke får hele tabet hjem.",
        "soeg": ["cmr", "transportør", "fragtfører", "ansvarsbegrænsning", "kravstille", "ddp"],
    },
    {
        "navn": "CISG — hvornår gælder den?",
        "kat": K_FRIST,
        "siger": "CISG (den internationale købelov) gælder som udgangspunkt for **køb af varer "
                 "mellem erhvervsdrivende i to forskellige konventionslande**, medmindre den "
                 "er gyldigt fravalgt i aftalen.",
        "her": "Ved enhver international handelstvist (fx dansk køber ↔ udenlandsk sælger) bør du "
               "FØRST fastslå, at sagen afgøres efter CISG. Det viser censor, at du har styr på "
               "lovgrundlaget, før du går til den enkelte regel.",
        "soeg": ["cisg", "international købelov", "konvention", "lovgrundlag"],
    },
    {
        "navn": "Undersøgelsespligt — CISG art. 38",
        "kat": K_FRIST,
        "siger": "Køber skal **undersøge varen så hurtigt, som omstændighederne tillader det**. "
                 "Skjulte mangler kan i sagens natur først opdages senere — fx når varen "
                 "tages i brug eller forarbejdes.",
        "her": "Skeln mellem synlige og skjulte mangler. En skjult mangel (fx en afvigelse der "
               "først viser sig, når materialet forarbejdes) starter først fristen, når den "
               "blev — eller burde være — opdaget. En kontrakt kan skærpe pligten, fx til at "
               "kontrollere synlige mangler inden for et bestemt antal hverdage.",
        "soeg": ["undersøgelsespligt", "art 38", "artikel 38", "skjult mangel", "kontrol"],
    },
    {
        "navn": "Reklamation 'inden rimelig tid' — CISG art. 39(1)",
        "kat": K_FRIST,
        "siger": "Køber mister retten til at påberåbe sig manglen, hvis der ikke reklameres "
                 "**inden rimelig tid efter at manglen blev opdaget eller burde være opdaget** — "
                 "og reklamationen skal angive manglens art.",
        "her": "Eksempel: opdages en mangel ved forarbejdningen og reklameres der skriftligt få "
               "dage senere, er det klart 'inden rimelig tid'. Pas på fælden: en kortere frist i "
               "sælgers standardvilkår (fx '8 dage') gælder KUN, hvis vilkårene faktisk er "
               "vedtaget — ellers er det CISG's 'rimelig tid', der tæller (se Standardvilkår).",
        "soeg": ["reklamation", "rimelig tid", "art 39", "artikel 39", "frist"],
    },
    {
        "navn": "2-års-fristen — CISG art. 39(2)",
        "kat": K_FRIST,
        "siger": "Uanset hvornår manglen opdages, mister køber kravet, hvis der ikke er "
                 "reklameret **senest 2 år efter varen faktisk blev overgivet** — medmindre "
                 "det strider mod en garanti, sælger har givet.",
        "her": "Eksempel: opdages en skjult mangel først mere end 2 år efter leveringen, er "
               "kravet som udgangspunkt tabt på den absolutte 2-års-frist. Fælden: en garanti "
               "køber selv har givet VIDERE til sin egen kunde forlænger ikke fristen mod "
               "sælger — kun en garanti FRA sælger kan det.",
        "soeg": ["2 år", "to år", "2-års", "art 39", "absolut frist", "garanti"],
    },
    {
        "navn": "Mangelbeføjelser — overblik",
        "kat": K_FRIST,
        "siger": "Ved mangler kan køber (når reklamationen er i orden) kræve **afhjælpning**, "
                 "**omlevering** (kræver væsentlig misligholdelse), **forholdsmæssigt afslag** "
                 "i prisen, **erstatning** — og ved væsentlig misligholdelse **ophævelse**.",
        "her": "Nævn altid flere beføjelser og vælg begrundet. En rettidig reklamation giver fx "
               "køber ret til omlevering eller afslag i prisen — og erstatning for påregnelige "
               "følgeskader oveni (art. 74).",
        "soeg": ["beføjelser", "afhjælpning", "omlevering", "afslag", "erstatning", "mangler"],
    },
    {
        "navn": "Følgeskader — CISG art. 74 (+ tabsbegrænsning art. 77)",
        "kat": K_OPH,
        "siger": "Erstatningen dækker hele tabet inkl. tabt fortjeneste — men kun det, den "
                 "misligholdende part **kunne forudse ved aftalens indgåelse** "
                 "(påregnelighed). Og skadelidte har pligt til at **begrænse sit tab** "
                 "(art. 77), ellers nedsættes erstatningen.",
        "her": "Eksempel: vidste sælger, at varen skulle bruges til en bestemt produktion, er en "
               "forsinkelse og det følgende tab som udgangspunkt påregneligt. Men kravet skæres "
               "til af tre ting: påregnelighed, dokumentation af tabet og "
               "tabsbegrænsningspligten. En ansvarsfraskrivelse for indirekte tab hjælper kun "
               "sælger, hvis den står i vilkår, der faktisk er vedtaget.",
        "soeg": ["følgeskader", "art 74", "art 77", "erstatning", "påregnelig", "tabt fortjeneste",
                 "tabsbegrænsning", "indirekte tab"],
    },
    {
        "navn": "Ophævelse ved væsentlig misligholdelse — CISG art. 25 + 49",
        "kat": K_OPH,
        "siger": "Køber kan kun hæve købet ved **væsentlig misligholdelse** (art. 25): "
                 "misligholdelsen skal i det væsentlige berøve køber det, han med rimelighed "
                 "kunne forvente af aftalen — og det skal have været påregneligt for sælger. "
                 "Ophævelsen erklæres efter art. 49.",
        "her": "Eksempel: en høj andel defekte emner i en bærende konstruktion er et stærkt "
               "argument for væsentlighed — det gør varen ubrugelig til formålet. Men er en "
               "ordre endnu ikke leveret, skal ophævelsen i stedet begrundes i reglerne om "
               "forventet misligholdelse (art. 71-72).",
        "soeg": ["ophævelse", "væsentlig misligholdelse", "art 25", "art 49", "hæve"],
    },
    {
        "navn": "Forventet (anticiperet) misligholdelse — CISG art. 71-72",
        "kat": K_OPH,
        "siger": "Står det **klart**, at modparten vil begå væsentlig misligholdelse, kan man "
                 "hæve allerede FØR leveringstiden (art. 72) eller stille sin egen opfyldelse "
                 "i bero (art. 71). Normalt skal man varsle, så modparten får chancen for at "
                 "stille betryggende sikkerhed.",
        "her": "Eksempel: en køber vil ophæve en endnu ikke leveret ordre af frygt for, at den "
               "får samme fejl som en tidligere leverance. FOR ophævelse taler en høj defekt-"
               "andel og sælgers nægtelse af at afhjælpe; IMOD taler, at sælger melder "
               "leverancen klar — er det så 'klart', at han VIL misligholde? Argumentér begge "
               "veje og konkludér selv — det er dét, der giver point.",
        "soeg": ["anticiperet", "forventet misligholdelse", "art 71", "art 72",
                 "ophæve før levering", "sikkerhed"],
    },
    {
        "navn": "Vedtagelse af standardvilkår",
        "kat": K_VILKAAR,
        "siger": "Standardbetingelser gælder kun, hvis de er **vedtaget** — altså gjort til en "
                 "del af aftalen VED indgåelsen, så modparten havde rimelig mulighed for at "
                 "kende dem (CISG art. 14-19 om aftalens indgåelse og art. 8 om fortolkning). "
                 "Vilkår der først dukker op bagefter — fx på **bagsiden af fakturaen** — er "
                 "som udgangspunkt ikke vedtaget.",
        "her": "Typisk mønster: aftalen indgås pr. mail, og betingelserne står først på "
               "fakturaens bagside og kommer altså EFTER aftalen — de er aldrig aktivt "
               "accepteret. Falder vedtagelsen, falder ALLE vilkårene på én gang (fx kort "
               "reklamationsfrist, ansvarsfraskrivelse og lovvalg) — og så gælder CISG's egne "
               "regler i stedet.",
        "soeg": ["standardvilkår", "vedtagelse", "bagside", "faktura",
                 "salgs- og leveringsbetingelser", "art 14", "art 19", "accept"],
    },
    {
        "navn": "Fremmedsprog og fast samhandel — CISG art. 8 + 9",
        "kat": K_VILKAAR,
        "siger": "Vilkår på et sprog, modtageren ikke med rimelighed kan forventes at forstå, "
                 "er svære at anse for vedtaget (art. 8 — man ser på hvad en fornuftig person "
                 "i samme situation ville forstå). **Sædvane og praksis mellem parterne** "
                 "(art. 9) kan binde — men kun hvis betingelserne reelt har været en kendt og "
                 "fulgt del af samhandlen.",
        "her": "Eksempel: står vilkårene på et sprog, modtageren ikke forstår, og er de aldrig "
               "aktivt accepteret, er de svære at anse for vedtaget. Selv flere års samhandel "
               "gør ikke i sig selv vilkårene til sædvane, hvis de aldrig er blevet accepteret "
               "eller brugt mellem parterne. Sprog + manglende accept trækker samme vej: ikke "
               "vedtaget.",
        "soeg": ["fremmedsprog", "sædvane", "praksis", "art 8", "art 9", "samhandel"],
    },
    {
        "navn": "Lovvalg og værneting",
        "kat": K_VILKAAR,
        "siger": "Kontrakter vælger ofte hvilket lands ret der gælder (**lovvalg**) og hvilken "
                 "domstol der skal dømme (**værneting**). Står valget i standardvilkår, gælder "
                 "det kun, hvis vilkårene er vedtaget.",
        "her": "Eksempel og kontrast: et lovvalg ('sælgers hjemland, sælgers by') i IKKE-vedtagne "
               "fakturavilkår falder bort. Står det derimod i en underskrevet rammeaftale, "
               "gælder det — så det kan fx blive dansk ret og dansk værneting, selv i en handel "
               "med en udenlandsk part.",
        "soeg": ["lovvalg", "værneting", "domstol", "dansk ret"],
    },
]

SCORE_TIP = ("🎓 **Sådan scorer du point:** 1) Nævn reglen med artikel/klausul → "
             "2) læg sagens fakta ved siden af → 3) argumentér begge veje hvor det er "
             "usikkert → 4) konkludér selv, kort og klart.")

tab_kat, tab_inco, tab_case = st.tabs([
    "📚 Jurakatalog", "🚢 Incoterms & risikoens overgang", "🧭 Tvist-skabeloner",
])


# ===========================================================================
# JURAKATALOG (søgbart, samme mønster som Organisations modelkatalog)
# ===========================================================================
with tab_kat:
    st.subheader("Jurakatalog")
    st.caption("Slå regler og artikler op. Hvert opslag: **Hvad den siger** (reglen i "
               "hverdagssprog) + **Hvorfor her** (hvornår den rammer, med et eksempel).")

    c1, c2 = st.columns([2, 1])
    with c1:
        soeg = st.text_input("Søg (fx 'ddp', 'reklamation', '2 år', 'standardvilkår')",
                             key="jura_soeg",
                             help="Søger i navne, regeltekst, forklaring og nøgleord — "
                                  "så både 'art 39' og 'rimelig tid' rammer.").lower().strip()
    with c2:
        kat = st.selectbox("Kategori", ["Alle"] + sorted({j["kat"] for j in JURA}), key="jura_kat",
                           help="Afgræns til ét område, fx kun frister eller kun standardvilkår.")

    vist = 0
    for j in JURA:
        if kat != "Alle" and j["kat"] != kat:
            continue
        tekst = " ".join([j["navn"], j["siger"], j["her"], " ".join(j["soeg"])]).lower()
        if soeg and soeg not in tekst:
            continue
        vist += 1
        with st.expander(f"{j['navn']}  ·  {j['kat']}", expanded=bool(soeg)):
            st.markdown(f"**Hvad den siger:** {j['siger']}")
            st.markdown(f"**Hvorfor her:** {j['her']}")
            st.caption(SCORE_TIP)
    if vist == 0:
        st.info("Ingen opslag matchede søgningen. Prøv et bredere ord, fx 'frist' eller 'risiko'.")


# ===========================================================================
# INCOTERMS — tidslinje-figur + kort pr. klausul
# ===========================================================================
with tab_inco:
    st.subheader("Incoterms 2020 — hvor går risikoen over?")
    st.caption("Tidslinjen går fra sælgers lager (venstre) til købers adresse (højre). Den røde "
               "ruder ◆ er **risikoovergangen** — til venstre bærer sælger risikoen (blå), til "
               "højre køber (gul). Den åbne ring ○ viser, **hvor langt sælger BETALER** "
               "(fragt/forsikring). Ligger de to ikke samme sted, er det C-gruppens fælde.")

    fig = go.Figure()
    n = len(INCOTERMS)
    for i, ic in enumerate(INCOTERMS):
        y = n - 1 - i  # EXW øverst, DDP nederst
        rp, op = ic["risiko_punkt"], ic["omk_punkt"]
        mode_txt = "kun søtransport" if ic["mode"] == "sø" else "enhver transportform"
        hover = (f"<b>{ic['kode']}</b> · {mode_txt}<br>"
                 f"◆ Risiko → køber ved: {TRIN[rp].replace(chr(10), ' ')}<br>"
                 f"○ Sælger betaler til: {TRIN[op].replace(chr(10), ' ')}<extra></extra>")
        # risiko-split-bjælke (blå = sælger, gul = køber)
        if rp > 0:
            fig.add_trace(go.Scatter(x=[0, rp], y=[y, y], mode="lines",
                                     line=dict(color=C_TOTAL, width=7),
                                     hoverinfo="skip", showlegend=False))
        if rp < 5:
            fig.add_trace(go.Scatter(x=[rp, 5], y=[y, y], mode="lines",
                                     line=dict(color=C_ORDER, width=7),
                                     hoverinfo="skip", showlegend=False))
        # stiplet forbindelse ring↔ruder når de er adskilt (C-gruppen)
        if op != rp:
            lo, hi = sorted([rp, op])
            fig.add_trace(go.Scatter(x=[lo, hi], y=[y, y], mode="lines",
                                     line=dict(color=C_TOTAL, width=1.5, dash="dot"),
                                     hoverinfo="skip", showlegend=False))
        # omkostnings-markør (hvor langt sælger betaler) — åben ring
        fig.add_trace(go.Scatter(x=[op], y=[y], mode="markers",
                                 marker=dict(color="rgba(0,0,0,0)", size=17, symbol="circle",
                                             line=dict(color=C_TOTAL, width=2.5)),
                                 hovertemplate=hover, showlegend=False))
        # risiko-markør (rød ruder) — ovenpå
        fig.add_trace(go.Scatter(x=[rp], y=[y], mode="markers",
                                 marker=dict(color=C_OPT, size=13, symbol="diamond"),
                                 hovertemplate=hover, showlegend=False))
    # Legende
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                             line=dict(color=C_TOTAL, width=7), name="Sælger bærer risikoen"))
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                             line=dict(color=C_ORDER, width=7), name="Køber bærer risikoen"))
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="markers",
                             marker=dict(color=C_OPT, size=12, symbol="diamond"),
                             name="◆ Risikoen springer"))
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="markers",
                             marker=dict(color="rgba(0,0,0,0)", size=13, symbol="circle",
                                         line=dict(color=C_TOTAL, width=2.5)),
                             name="○ Sælger betaler til"))
    fig.update_layout(
        height=30 * n + 130,
        xaxis=dict(tickmode="array", tickvals=list(range(6)), ticktext=TRIN, range=[-0.3, 5.3]),
        yaxis=dict(tickmode="array", tickvals=list(range(n)),
                   ticktext=[ic["kode"] for ic in reversed(INCOTERMS)],
                   range=[-0.6, n - 0.4]),
        legend=dict(orientation="h", y=1.06),
        margin=dict(t=45, b=10),
    )
    vis_fig(fig)
    st.caption("**C-gruppens fælde (CFR/CIF/CPT/CIP):** ringen ○ ligger til HØJRE for ruden ◆ — "
               "sælger betaler fragten langt frem, men risikoen sprang allerede tidligt. Går "
               "godset tabt undervejs, er det KØBERS tab, selvom sælger betalte transporten. Ved "
               "CPT/CIP er afstanden størst (risiko ved første fragtfører, betaling helt til "
               "destinationen).")

    st.markdown("**Hurtig oversigt (alle 11):**")
    df_inco = pd.DataFrame([{
        "Kode": ic["kode"],
        "Familie": ic["familie"],
        "Transport": "Kun sø" if ic["mode"] == "sø" else "Enhver",
        "Risikoen går over": TRIN[ic["risiko_punkt"]].replace("\n", " "),
        "Sælger betaler til": TRIN[ic["omk_punkt"]].replace("\n", " "),
    } for ic in INCOTERMS])
    st.dataframe(df_inco, hide_index=True, width="stretch")

    st.divider()
    for fam in ["E", "F", "C", "D"]:
        st.markdown(f"**{FAM_NAVN[fam]}**")
        for ic in [x for x in INCOTERMS if x["familie"] == fam]:
            titel = ic["navn"] + (" · kun søtransport" if ic["mode"] == "sø" else "")
            with st.expander(titel, expanded=ic["kode"] == "DDP"):
                st.markdown(f"**Hvad den siger:** {ic['siger']}")
                st.markdown(f"**Risikoen overgår:** {ic['risiko']}")
                st.markdown(f"**Hvorfor her:** {ic['her']}")
    st.caption("⭐ DDP er ofte den eksamensrelevante: en transportskade FØR destinationen ligger "
               "hos sælger — se den fulde argumentationskæde under fanen 🧭 Tvist-skabeloner.")


# ===========================================================================
# TVIST-SKABELONER — generiske argumentationskæder pr. tvist-type
# ===========================================================================
with tab_case:
    st.subheader("Tvist-skabeloner — sådan griber du en tvist an")
    st.caption("Tre almindelige tvist-typer som færdige argumentationskæder med neutrale "
               "parter. Brug dem som skabelon på din egen opgave: lovgrundlag → fakta → regel "
               "→ konklusion. Sæt selv casens navne og tal ind.")

    with st.container(border=True):
        st.markdown("### 🧾 Skjult mangel + er standardvilkårene vedtaget?")
        st.markdown(
            "*Situation: en dansk køber opdager en skjult mangel efter forarbejdning; "
            "sælgers standardvilkår stod på fakturaens bagside.*\n\n"
            "1. **Lovgrundlag:** internationalt køb mellem erhvervsdrivende i to "
            "konventionslande → sagen afgøres efter **CISG**.\n"
            "2. **Er sælgers egne vilkår vedtaget?** Hvis aftalen blev indgået pr. mail, og "
            "betingelserne først kom på fakturaens bagside (evt. på et fremmedsprog), er de "
            "aldrig aktivt accepteret (art. 8 + 14-19). Selv års samhandel ændrer ikke det "
            "(art. 9). → en kort reklamationsfrist, ansvarsfraskrivelse og lovvalg i vilkårene "
            "**falder alle bort**.\n"
            "3. **Er reklamationen rettidig efter CISG?** En skjult mangel opdaget ved "
            "forarbejdningen og reklameret skriftligt få dage senere er 'inden rimelig tid' "
            "(art. 38-39).\n"
            "4. **Beføjelser:** omlevering eller forholdsmæssigt afslag + erstatning.\n"
            "5. **Følgeskader (art. 74):** vidste sælger, hvad varen skulle bruges til, er en "
            "følgende forsinkelse påregnelig. Kravet begrænses af påregnelighed, dokumentation "
            "og tabsbegrænsningspligten (art. 77)."
        )

    with st.container(border=True):
        st.markdown("### 🚚 DDP og en transportskade undervejs")
        st.markdown(
            "*Situation: aftalen siger 'DDP destinationsby', og godset beskadiges under "
            "transporten før destinationen.*\n\n"
            "1. **Lovgrundlag:** Incoterm-klausulen i kontrakten (**DDP, Incoterms 2020**) + "
            "et evt. lovvalg/værneting i en underskrevet aftale.\n"
            "2. **Risikoen:** under DDP bærer sælger AL risiko, til varen er stillet til "
            "rådighed på destinationen. Sker skaden før destinationen → risikoen lå stadig hos "
            "**sælger**.\n"
            "3. **Konklusion mod køber:** sælger skal omlevere. Argumentet 'risikoen overgik da "
            "varen forlod sælgers lager' holder ikke: transportøren er bare sælgers led i "
            "leveringen.\n"
            "4. **Kravet mod transportøren:** har sælger både risikoen og transportaftalen → "
            "**sælger kravstiller mod fragtføreren efter CMR-loven** (ikke købeloven). CMR's "
            "vægtbaserede ansvarsbegrænsning betyder, at hele tabet ikke nødvendigvis dækkes."
        )

    with st.container(border=True):
        st.markdown("### ⏳ Frister, ophævelse og FOB-risiko")
        st.markdown(
            "*Situation: en gammel leverance viser sig defekt lang tid efter; en ny ordre "
            "ønskes ophævet; og et parti kom hjem FOB.*\n\n"
            "**Krav for en gammel leverance:** opdages manglen mere end 2 år efter leveringen, "
            "støder kravet på **2-års-fristen i art. 39(2)**. Har sælger ikke givet en garanti, "
            "der forlænger fristen, er kravet som udgangspunkt tabt. Fælde: en garanti køber selv "
            "har givet videre til sin egen kunde binder kun køber — den smitter ikke af på "
            "sælger.\n\n"
            "**Ophævelse af en endnu ikke leveret ordre:** her handler det om **forventet "
            "misligholdelse (art. 71-72)**: FOR taler en høj defekt-andel og sælgers nægtelse af "
            "at afhjælpe; IMOD taler, at sælger melder leverancen klar — er det 'klart', at han "
            "vil misligholde væsentligt (art. 25)? Argumentér begge veje og konkludér selv.\n\n"
            "**Et parti leveret FOB:** risikoen overgik, da godset var om bord. Går det tabt "
            "undervejs → **købers eget tab**. Fremtidig sikring: tegn transportforsikring, eller "
            "aftal CIF/CIP (sælger forsikrer) eller DAP/DDP (sælger bærer risikoen længere)."
        )

    st.caption(SCORE_TIP)

st.divider()
st.caption("Opslagene forklarer reglerne generelt med neutrale eksempler — "
           "artikelhenvisningerne er CISG, og Incoterms er 2020-udgaven. "
           "Incoterms-detaljer ud over risikoovergangen (fx præcise omkostningslister) bør "
           "slås efter i undervisningsmaterialet.")
