"""Jura — søgbart opslagskatalog for indkøbsjura (ingen regnemaskiner).

Blødt fag: Incoterms med risikoens overgangspunkt, CISG-beføjelser og frister,
vedtagelse af standardvilkår og krav mod transportøren. Hvert opslag følger
jura-mønstret "Hvad den siger" + "Hvorfor her", forklaret generelt med neutrale
eksempler, så det kan bruges til en hvilken som helst opgave eller tvist.
Artikelhenvisningerne er CISG (den internationale købelov); Incoterms er 2020.
"""
import os
import sys

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
# DATA — Incoterms (risikoovergangspunkt på en fælles transport-tidslinje)
# ===========================================================================
# 'punkt' er position på tidslinjen 0-5 hvor risikoen springer fra sælger til køber
TRIN = ["Sælgers lager", "Læsset /\nafhentet", "Afskibnings-\nhavn",
        "Om bord\npå skibet", "Ankomst-\nhavn", "Hos køber\n(destination)"]

INCOTERMS = [
    {
        "kode": "EXW", "navn": "EXW — Ex Works (ab fabrik)", "punkt": 0,
        "risiko": "Risikoen overgår allerede når varen er **stillet til rådighed på sælgers "
                  "adresse** — køber står selv for læsning, transport, eksport og import.",
        "siger": "Sælgers mindste forpligtelse: han skal bare gøre varen klar på sit eget lager. "
                 "Alt derfra — læsning, fragt, forsikring, told — er købers problem og risiko.",
        "her": "Modpolen til DDP. Brug EXW/DDP som yderpunkterne når du skal forklare, hvor "
               "meget ansvar parterne hver især har taget på sig i kontrakten.",
        "soeg": ["exw", "ex works", "ab fabrik", "afhentning"],
    },
    {
        "kode": "FOB", "navn": "FOB — Free On Board", "punkt": 3,
        "risiko": "Risikoen overgår når varen er **om bord på skibet i afskibningshavnen**. "
                  "Kun til søtransport.",
        "siger": "Sælger leverer varen om bord på det skib, køber har udpeget. Fra det øjeblik "
                 "bærer køber risikoen og betaler hovedtransport — og forsikring er KØBERS "
                 "eget valg og egen regning.",
        "her": "Eksempel: en køber aftaler 'FOB afskibningshavn', og godset går tabt undervejs "
               "OVER havet — altså efter lastning. Så er det købers risiko, og køber bærer "
               "tabet, medmindre han selv har tegnet transportforsikring. Vil køber sikre sig "
               "bedre, kan han vælge en klausul hvor sælger bærer mere (CIF/CIP eller DAP/DDP).",
        "soeg": ["fob", "free on board", "container", "overbord", "søtransport"],
    },
    {
        "kode": "CIF", "navn": "CIF — Cost, Insurance & Freight", "punkt": 3,
        "risiko": "Risikoen overgår **samme sted som FOB** (om bord i afskibningshavnen) — "
                  "selvom sælger betaler fragt og forsikring helt til ankomsthavnen.",
        "siger": "Sælger betaler fragten OG tegner en søforsikring til ankomsthavnen — men "
                 "risikoen er alligevel købers fra lastningen. Omkostninger og risiko følges "
                 "altså IKKE ad. Kun til søtransport.",
        "her": "Den klassiske eksamensfælde: 'sælger betaler til ankomsthavnen, så sælger "
               "bærer vel risikoen?' Nej — går godset tabt undervejs, er det købers risiko, "
               "men køber kan trække på den forsikring sælger har tegnet. Derfor er CIF et "
               "oplagt svar på, hvordan en køber kan sikre sig mod tab under søtransport uden "
               "selv at skulle tegne forsikringen.",
        "soeg": ["cif", "cost insurance freight", "forsikring", "fragt", "søtransport"],
    },
    {
        "kode": "DAP", "navn": "DAP — Delivered At Place", "punkt": 5,
        "risiko": "Risikoen overgår når varen er **ankommet til det aftalte sted, klar til "
                  "aflæsning** hos køber.",
        "siger": "Sælger bærer transport og risiko hele vejen til destinationen — men køber "
                 "klarer selv importtold og importmoms. Forskellen på DAP og DDP er altså "
                 "kun tolden.",
        "her": "Brug DAP som mellemtrin når du sammenligner: mere sælgeransvar end FOB/CIF, "
               "men uden DDP's told-forpligtelse.",
        "soeg": ["dap", "delivered at place", "destination", "told"],
    },
    {
        "kode": "DDP", "navn": "DDP — Delivered Duty Paid ⭐", "punkt": 5,
        "risiko": "Risikoen overgår først når varen er **stillet til rådighed hos køber på "
                  "destinationen** — og sælger har også betalt told og importafgifter.",
        "siger": "Sælgers STØRSTE forpligtelse: han bærer alle omkostninger og al risiko — "
                 "inkl. told og importafgifter — indtil varen står klar hos køber. "
                 "Transportøren undervejs er bare sælgers hjælper.",
        "her": "Eksempel og typisk fælde: aftalen siger 'DDP destinationsby'. Sker der en "
               "transportskade UNDERVEJS — fx traileren vælter før destinationen — er risikoen "
               "endnu ikke overgået, så SÆLGER bærer tabet og skal omlevere. Argumentet "
               "'risikoen overgik da varen forlod sælgers lager' er forkert: under DDP flytter "
               "selve afsendelsen ikke risikoen.",
        "soeg": ["ddp", "delivered duty paid", "risikoovergang", "told", "omlevering"],
    },
]

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
    st.caption("Én tidslinje fra sælgers lager til købers adresse. Den røde ruder-markør er "
               "**risikoovergangspunktet**: til venstre for den bærer sælger risikoen (blå), "
               "til højre bærer køber den (gul). Hold musen over et punkt for detaljer.")

    fig = go.Figure()
    n = len(INCOTERMS)
    for i, ic in enumerate(INCOTERMS):
        y = n - 1 - i  # EXW øverst, DDP nederst
        p = ic["punkt"]
        hover = (f"<b>{ic['kode']}</b> — risikoen overgår ved: "
                 f"{TRIN[p].replace(chr(10), ' ')}<extra></extra>")
        if p > 0:
            fig.add_trace(go.Scatter(x=[0, p], y=[y, y], mode="lines",
                                     line=dict(color=C_TOTAL, width=7),
                                     hoverinfo="skip", showlegend=False))
        if p < 5:
            fig.add_trace(go.Scatter(x=[p, 5], y=[y, y], mode="lines",
                                     line=dict(color=C_ORDER, width=7),
                                     hoverinfo="skip", showlegend=False))
        fig.add_trace(go.Scatter(x=[p], y=[y], mode="markers",
                                 marker=dict(color=C_OPT, size=15, symbol="diamond"),
                                 hovertemplate=hover, showlegend=False))
    # Legendeforklaring via to usynlige spor
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                             line=dict(color=C_TOTAL, width=7), name="Sælger bærer risikoen"))
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="lines",
                             line=dict(color=C_ORDER, width=7), name="Køber bærer risikoen"))
    fig.add_trace(go.Scatter(x=[None], y=[None], mode="markers",
                             marker=dict(color=C_OPT, size=12, symbol="diamond"),
                             name="Risikoen springer her"))
    fig.update_layout(
        height=340,
        xaxis=dict(tickmode="array", tickvals=list(range(6)), ticktext=TRIN,
                   range=[-0.3, 5.3]),
        yaxis=dict(tickmode="array", tickvals=list(range(n)),
                   ticktext=[ic["kode"] for ic in reversed(INCOTERMS)],
                   range=[-0.6, n - 0.4]),
        legend=dict(orientation="h", y=1.12),
        margin=dict(t=30, b=10),
    )
    vis_fig(fig)
    st.caption("Læg mærke til CIF-fælden: sælger betaler fragt og forsikring helt til "
               "ankomsthavnen, men risikoen er sprunget allerede ved lastningen — omkostninger "
               "og risiko følges ikke ad. Og DAP/DDP deler overgangspunkt: forskellen er kun, "
               "hvem der betaler told og importafgifter (DDP = sælger).")

    st.divider()
    for ic in INCOTERMS:
        with st.expander(ic["navn"], expanded=ic["kode"] == "DDP"):
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
