"""Opslagsværktøj for logistikøkonom — forside med hero, farvekodede fag-kort
og global søgning (tokeniseret, tolerant for æ/ø/å, rangeret og fag-grupperet,
med deep-links direkte til modulerne på Indkøb og Produktion).

Kør med:  streamlit run Hjem.py
"""
import os
import sys

import streamlit as st

st.set_page_config(
    page_title="Opslagsværktøj — Logistikøkonom",
    page_icon="📦",
    layout="wide",
)

_ROD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROD)
from ui_theme import inject_css, FAGFARVER  # noqa: E402

inject_css()

# Sidestier (relativt til denne fil) — bruges af page_link/switch_page
P_VCA = "pages/0_Værdikædeanalyse.py"
P_INDKOEB = "pages/1_Indkøb.py"
P_PROD = "pages/2_Produktion.py"
P_STAT = "pages/3_Statistik.py"
P_OEKO = "pages/4_Økonomi.py"
P_ORG = "pages/5_Organisation.py"
P_KOMM = "pages/6_Kommunikation.py"
P_FORSVAR = "pages/7_Forsvarstræner.py"
P_JURA = "pages/8_Jura.py"
P_DIST = "pages/9_Distribution.py"
HAR_JURA = os.path.exists(os.path.join(_ROD, P_JURA))

# Sider med modulvælger: forsiden kan deep-linke til et konkret modul ved at
# sætte st.session_state['goto_modul'] og skifte side (konvention på tværs).
DEEP_SIDER = {P_INDKOEB, P_PROD, P_DIST}

# Fag-kort: (ikon, navn, side, modulbeskrivelse)
FAG = [
    ("🔗", "Værdikædeanalyse", P_VCA,
     "Rammen om det hele · Porters værdikæde punkt for punkt · Støtteaktiviteter + "
     "primære aktiviteter · hver station forklaret med link videre til faget"),
    ("🛒", "Indkøb", P_INDKOEB,
     "EOQ · POQ/EPQ · Genbestilling+SS · ABC/Pareto · Forecasting · "
     "Review-systemer · Make-vs-buy/TCO · Leverandørscore · Strategi & modeller"),
    ("🏭", "Produktion", P_PROD,
     "POQ · Linjebalancering · Processkort · Knap kapacitet · Produktionsstrategi · "
     "MPS+ATP · MRP · S&OP · Little's Law · OEE · Perfect Order/OTIF · Udnyttelsesgrad ρ"),
    ("📊", "Statistik", P_STAT,
     "Normalfordeling · Konfidensinterval · Binomialfordeling · Hypotesetest · "
     "Kontrolkort (p/X̄/R) · Regression"),
    ("💰", "Økonomi", P_OEKO,
     "Investeringskalkule (NPV/IRR + kritiske værdier) · Break-even · Priskalkulation · "
     "Prisoptimering · Nøgletalsanalyse · Budget"),
    ("🧭", "Organisation", P_ORG,
     "Modelkatalog (Porter, Ansoff, McGregor, Blake & Mouton, Adizes, Hofstede …) · Modelvælger"),
    ("💬", "Kommunikation", P_KOMM,
     "Interessentanalyse · Forhandlingsark (MDO/LDO) · ZOPA · Kulturteorier · "
     "Forhandlingsbibliotek"),
    ("🎓", "Forsvarstræner", P_FORSVAR,
     "Træn det mundtlige forsvar · eksaminator borer dybere · argumentér selv (bløde fag) · "
     "regn & forklar (rigtige svar i økonomi/statistik) · faktatjek"),
]
if HAR_JURA:
    FAG.insert(7, ("⚖️", "Jura", P_JURA,
                   "Alle 11 Incoterms 2020 med risiko- og omkostningsovergang · CISG-beføjelser "
                   "og frister · Standardvilkår · Reklamation · Hvem bærer risikoen?"))
# Distribution (3. semester) — indsættes lige før Forsvarstræner
FAG.insert(len(FAG) - 1, ("🚚", "Distribution", P_DIST,
                          "Transportformsvalg · Tyngdepunktsmetoden · Chopras 6 netværk · "
                          "Lean & QRM · Kanban-beregner · Lager & plukning · "
                          "Køre-hviletid & vægte · Told & dokumenter · Grøn godstransport"))

# Søgeindeks: (fag, modul, side, ikon, nøgleord, modul-deep-link eller None)
# Deep-link-feltet er modulnavnet EKSAKT som det står i sidens modulvælger.
INDEX = [
    # Værdikædeanalyse (rammen om de øvrige fag)
    ("Værdikædeanalyse", "Sådan bygger du en VCA (punkt for punkt)", P_VCA, "🔗",
     ["vca", "værdikæde", "værdikædeanalyse", "porter", "værdikæden", "støtteaktiviteter",
      "primære aktiviteter", "infrastruktur", "logistik ind", "logistik ud", "produktion",
      "marketing", "salg", "service", "harmoni", "udfordringer", "rammeaftale", "incoterms"],
     None),
    # Indkøb
    ("Indkøb", "EOQ — optimal ordrestørrelse", P_INDKOEB, "🛒",
     ["eoq", "wilson", "wilsons formel", "ordrestørrelse", "økonomisk ordremængde", "bestilling"],
     "EOQ"),
    ("Indkøb", "POQ / EPQ", P_INDKOEB, "🛒",
     ["poq", "epq", "produktionsserie", "seriestørrelse"],
     "POQ / EPQ"),
    ("Indkøb", "Genbestillingspunkt + sikkerhedslager", P_INDKOEB, "🛒",
     ["rop", "genbestilling", "benzinlampen", "sikkerhedslager", "ss", "servicegrad", "z-værdi"],
     "Genbestilling + SS"),
    ("Indkøb", "ABC / Pareto-analyse", P_INDKOEB, "🛒",
     ["abc", "pareto", "80/20", "klassifikation", "årsværdi"],
     "ABC / Pareto"),
    ("Indkøb", "Forecasting", P_INDKOEB, "🛒",
     ["forecast", "forecasting", "prognose", "glidende gennemsnit", "eksponentiel udglatning",
      "mad", "mape", "mfe", "tracking signal"],
     "Forecasting"),
    ("Indkøb", "Review-systemer (lagerstyring)", P_INDKOEB, "🛒",
     ["review", "periodisk", "kontinuert", "lagerstyring", "max-niveau"],
     "Review-systemer"),
    ("Indkøb", "Make-vs-buy / TCO", P_INDKOEB, "🛒",
     ["make or buy", "make-vs-buy", "tco", "tca", "total cost", "outsourcing", "insourcing",
      "break-even", "egenproduktion", "ejeromkostning", "leverandørsammenligning"],
     "Make-vs-buy / TCO"),
    ("Indkøb", "Leverandørscore", P_INDKOEB, "🛒",
     ["leverandør", "leverandørevaluering", "vægtet score", "kriterier", "esg"],
     "Leverandørscore"),
    ("Indkøb", "Strategi & modeller (indkøb)", P_INDKOEB, "🛒",
     ["kraljic", "bensaou", "sourcing", "single", "dual", "exit", "voice", "order winner",
      "qualifier", "tce", "vmi", "esi", "srm", "spend"],
     "Strategi & modeller"),
    # Produktion
    ("Produktion", "POQ (produktionsserie)", P_PROD, "🏭",
     ["poq", "epq", "produktionsserie", "besparelse"], "POQ"),
    ("Produktion", "Linjebalancering", P_PROD, "🏭",
     ["linjebalancering", "takt time", "takttid", "stationer", "effektivitet", "balancetab"],
     "Linjebalancering"),
    ("Produktion", "Processkort", P_PROD, "🏭",
     ["processkort", "værdigivende", "v/iv", "lean", "spild"], "Processkort"),
    ("Produktion", "Knap kapacitet / flaskehals", P_PROD, "🏭",
     ["knap kapacitet", "flaskehals", "dækningsbidrag", "db pr. time", "produktmix"],
     "Knap kapacitet"),
    ("Produktion", "Produktionsstrategi (5 dimensioner)", P_PROD, "🏭",
     ["produktionsstrategi", "mts", "mto", "ato", "eto", "lean", "fordisme", "jit", "layout",
      "ordretype", "make to stock"],
     "Produktionsstrategi"),
    ("Produktion", "MPS + ATP", P_PROD, "🏭",
     ["mps", "atp", "master production schedule", "available to promise", "pei"],
     "MPS + ATP"),
    ("Produktion", "MRP (materialebehovsplanlægning)", P_PROD, "🏭",
     ["mrp", "bom", "stykliste", "materialebehov", "lot-for-lot", "lotstørrelse", "bruttobehov"],
     "MRP"),
    ("Produktion", "S&OP (Level vs. Chase)", P_PROD, "🏭",
     ["s&op", "sop", "aggregeret plan", "level", "chase", "arbejdsstyrke"],
     "S&OP"),
    ("Produktion", "Little's Law", P_PROD, "🏭",
     ["little", "littles law", "wip", "gennemløbstid", "gennemløb"],
     "Little's Law"),
    ("Produktion", "OEE", P_PROD, "🏭",
     ["oee", "tilgængelighed", "ydelse", "kvalitet", "overall equipment"],
     "OEE"),
    ("Produktion", "Perfect Order / OTIF", P_PROD, "🏭",
     ["otif", "perfect order", "leveringspræcision", "til tiden"],
     "Perfect Order / OTIF"),
    ("Produktion", "Udnyttelsesgrad ρ (kø)", P_PROD, "🏭",
     ["udnyttelsesgrad", "rho", "kø", "ventetid", "lambda", "my", "kapacitet"],
     "Udnyttelsesgrad ρ"),
    # Statistik
    ("Statistik", "Normalfordeling", P_STAT, "📊",
     ["normalfordeling", "z", "z-score", "areal", "gauss", "standardafvigelse",
      "rå data", "målinger", "normalitetstjek", "histogram"], None),
    ("Statistik", "Konfidensinterval", P_STAT, "📊",
     ["konfidensinterval", "ki", "middelværdi", "andel", "t-fordeling", "margin of error",
      "stikprøvestørrelse"], None),
    ("Statistik", "Binomialfordeling", P_STAT, "📊",
     ["binomial", "binomialfordeling", "sandsynlighed", "x ud af n", "succeser"], None),
    ("Statistik", "Hypotesetest", P_STAT, "📊",
     ["hypotesetest", "hypotese", "h0", "h1", "nulhypotese", "signifikans", "signifikansniveau",
      "p-værdi", "t-test", "z-test", "teststørrelse", "én stikprøve", "to stikprøver",
      "ensidet", "tosidet", "kritisk værdi"], None),
    ("Statistik", "Kontrolkort (SPC)", P_STAT, "📊",
     ["kontrolkort", "spc", "p-kort", "x-kort", "r-kort", "ucl", "lcl", "proceskontrol",
      "statistisk kvalitetskontrol", "kapabilitet"], None),
    ("Statistik", "Regression (lineær)", P_STAT, "📊",
     ["regression", "lineær regression", "scatter", "scatterplot", "r²", "r2", "fittet linje",
      "korrelation", "hældning", "sammenhæng", "mindste kvadraters"], None),
    # Økonomi
    ("Økonomi", "Investeringskalkule (NPV/IRR + kritiske værdier)", P_OEKO, "💰",
     ["npv", "kapitalværdi", "irr", "intern rente", "payback", "tilbagebetalingstid",
      "kritisk levetid", "kritisk omsætning", "kritisk investeringsbeløb", "kritiske indbetalinger",
      "investering", "cashflow", "nutidsværdi", "sunk cost"], None),
    ("Økonomi", "Break-even / nulpunkt", P_OEKO, "💰",
     ["break-even", "nulpunkt", "dækningsgrad", "dækningsbidrag", "sikkerhedsmargin"], None),
    ("Økonomi", "Priskalkulation", P_OEKO, "💰",
     ["priskalkulation", "bidragskalkulation", "fordelingskalkulation", "retrograd",
      "kostpris", "salgspris", "avance"], None),
    ("Økonomi", "Prisoptimering (monopol)", P_OEKO, "💰",
     ["prisoptimering", "totalmetoden", "grænsemetoden", "grænseomsætning", "monopol"], None),
    ("Økonomi", "Nøgletalsanalyse", P_OEKO, "💰",
     ["nøgletal", "afkastningsgrad", "overskudsgrad", "soliditet", "likviditet", "gearing",
      "dupont", "egenkapitalforrentning", "fremmedkapitalforrentning", "aoh", "regnskab",
      "balance", "passiver", "aktiver", "likviditetsgrad"], None),
    ("Økonomi", "Budget", P_OEKO, "💰",
     ["budget", "resultatbudget", "likviditetsbudget", "afskrivning", "lineær afskrivning",
      "kassekredit"], None),
    # Organisation
    ("Organisation", "Modelkatalog + Modelvælger", P_ORG, "🧭",
     ["porter", "generiske strategier", "ansoff", "vækstmatrix", "lean", "agil", "sc-strategi",
      "organisationsstruktur", "silo", "organisk", "mekanistisk", "mcgregor", "teori x", "teori y",
      "schein", "menneskesyn", "ledergitter", "blake", "mouton", "adizes", "paei", "hofstede",
      "kultur", "ledelse", "ledelsesstil", "motivation", "modelvælger", "esg", "csrd"], None),
    # Kommunikation
    ("Kommunikation", "Interessentanalyse", P_KOMM, "💬",
     ["interessent", "interessentanalyse", "magt", "interesse", "power-interest", "mendelow"],
     None),
    ("Kommunikation", "Forhandlingsark + ZOPA", P_KOMM, "💬",
     ["forhandling", "forhandlingsark", "bargaining", "mdo", "ldo", "målpunkt", "modstandspunkt",
      "zopa", "byttechip"], None),
    ("Kommunikation", "Kommunikationsmodellen", P_KOMM, "💬",
     ["kommunikationsmodel", "kommunikationsmodellen", "afsender", "modtager", "budskab",
      "kanal", "støj", "feedback", "kodning", "afkodning", "envejskommunikation",
      "tovejskommunikation"], None),
    ("Kommunikation", "Kulturteorier (Hofstede + Gesteland)", P_KOMM, "💬",
     ["gesteland", "hofstede", "kultur", "kulturteori", "relationship focus", "deal focus",
      "monokron", "flydende tid", "ekspressiv", "reserveret", "formel", "uformel"], None),
    ("Kommunikation", "Forhandlingsbibliotek", P_KOMM, "💬",
     ["bapta", "batna", "alternativ", "principiel forhandling", "harvard", "distributiv",
      "integrativ", "kulturelle forhandlingsstile", "win-win"], None),
    # Forsvarstræner (mundtligt eksamensforsvar — argumentation)
    ("Forsvarstræner", "Træn det mundtlige forsvar (hvorfor + argumenter)", P_FORSVAR, "🎓",
     ["forsvar", "forsvarstræner", "eksamen", "mundtlig", "argumentation", "argument", "hvorfor",
      "dybde", "snydespørgsmål", "snyd", "fælde", "fældejagt", "prøveeksamen", "flashcards",
      "faktatjek", "det afhænger", "ddp", "erp", "kraljic", "bensaou", "incoterms", "told",
      "duty", "regn", "regneopgaver", "rigtige svar", "npv", "break-even", "konfidensinterval",
      "eoq", "oee", "nøgletal", "eksaminér mig", "eksaminer", "regnetræner", "forklar selv",
      "feynman", "quiz", "selvrating", "eksaminator borer"], None),
]
# Distribution (3. semester) — deep-links til modulvælgeren på siden
INDEX += [
    ("Distribution", "Valg af transportform", P_DIST, "🚚",
     ["transportform", "transportformer", "transportvalg", "vej", "bane", "jernbane",
      "skib", "søtransport", "søfragt", "luftfragt", "rørledning", "intermodal",
      "container", "modal split", "omlastning", "transittid", "transportør"],
     "Transportformsvalg"),
    ("Distribution", "Tyngdepunktsmetoden (gravity model)", P_DIST, "🚚",
     ["tyngdepunkt", "tyngdepunktsmetoden", "gravity", "center of gravity",
      "lagerplacering", "lokalisering", "placering af lager", "koordinater",
      "transportarbejde", "netværksdesign", "hvor skal lageret ligge"],
     "Tyngdepunktsmetoden"),
    ("Distribution", "Distributionsnetværk — Chopras 6 design", P_DIST, "🚚",
     ["chopra", "distributionsnetværk", "netværksdesign", "drop-shipping",
      "dropshipping", "in-transit merge", "last-mile", "kundeafhentning",
      "svartid", "response time", "aggregering", "u-kurve", "antal lagre",
      "distributionskanal", "e-handel", "ferdows"],
     "Distributionsnetværk (Chopra)"),
    ("Distribution", "Lean & QRM", P_DIST, "🚚",
     ["lean", "qrm", "quick response manufacturing", "muda", "spild", "spildtyper",
      "kaizen", "jidoka", "vsm", "værdistrøm", "værdistrømsanalyse", "learning to see",
      "mct", "white space", "qrm-tal", "polca", "ftms", "q-roc", "qrm-celle",
      "responstidsspiral", "christopher", "agil", "postponement", "reservekapacitet"],
     "Lean & QRM"),
    ("Distribution", "Kanban-beregner (antal kort)", P_DIST, "🚚",
     ["kanban", "kanban-kort", "produktionskort", "flyttekort", "beholder",
      "beholderstørrelse", "pull", "træksystem", "to-kort", "jit", "just-in-time",
      "sikkerhedsfaktor"],
     "Kanban-beregner"),
    ("Distribution", "Lager & plukning", P_DIST, "🚚",
     ["lager", "plukning", "pluk", "batch-pluk", "zone-pluk", "wave-pluk",
      "cluster-pluk", "pick by voice", "pick by light", "rfid", "wms", "tpl",
      "tredjepartslogistik", "3pl", "cross-dock", "crossdock", "put away", "fifo",
      "lifo", "konsolidering", "reverse logistics", "fulfilment", "plukkefejl",
      "marshalling", "kaoslager"],
     "Lager & plukning"),
    ("Distribution", "Køre-hviletid & vægtgrænser", P_DIST, "🚚",
     ["køre-hviletid", "kørehviletid", "køretid", "hviletid", "pause", "ugehvil",
      "561/2006", "takograf", "tachograf", "fartskriver", "vejpakke", "totalvægt",
      "vogntogsvægt", "vogntog", "akseltryk", "overlæs", "vægtgrænser", "aksler",
      "chauffør", "bøde"],
     "Køre-hviletid & vægte"),
    ("Distribution", "Told & dokumenter (T1/T2, TIR, remburs)", P_DIST, "🚚",
     ["told", "t1", "t2", "taric", "toldoplag", "tir", "ata-carnet", "carnet", "wto",
      "beskyttelsestold", "finanstold", "remburs", "letter of credit", "cad", "cod",
      "betaling mod dokumenter", "konnossement", "bill of lading", "transit",
      "fri omsætning", "toldstatus", "gældsbevis", "iou"],
     "Told & dokumenter"),
    ("Distribution", "Grøn godstransport (CO2)", P_DIST, "🚚",
     ["co2", "grøn", "decarbonising", "dekarbonisering", "klima", "tonkm",
      "slow steaming", "imo", "net-nul", "bæredygtig", "grøn omstilling",
      "co2-budget", "elektrificering", "modal shift", "70 procent"],
     "Grøn godstransport"),
]
if HAR_JURA:
    INDEX += [
        ("Jura", "Incoterms — risikoens overgang", P_JURA, "⚖️",
         ["incoterms", "exw", "fca", "fas", "fob", "cfr", "cif", "cpt", "cip", "dap", "dpu", "ddp",
          "risikoovergang", "risikoens overgang", "told", "transportør", "fragt", "forsikring",
          "e f c d gruppe"], None),
        ("Jura", "CISG — beføjelser og frister", P_JURA, "⚖️",
         ["cisg", "købelov", "reklamation", "reklamationsfrist", "undersøgelsespligt",
          "misligholdelse", "ophævelse", "erstatning", "følgeskader", "mangler"], None),
        ("Jura", "Standardvilkår og aftaleindgåelse", P_JURA, "⚖️",
         ["standardvilkår", "vedtagelse", "faktura", "fremmedsprog", "lovvalg", "værneting",
          "aftale", "ansvarsfraskrivelse"], None),
    ]


def fold(s: str) -> str:
    """Normalisér til søgning: småt + æ/ø/å → ae/oe/aa (tolerant tastning)."""
    return (s.lower()
            .replace("æ", "ae").replace("ø", "oe").replace("å", "aa")
            .replace("é", "e").replace("&", " og "))


def soeg(q: str):
    """Tokeniseret OG-søgning med ranking.

    Alle ord i søgningen skal findes i fag+modul+nøgleord. Rangeres:
    eksakt nøgleords-match > modulnavn starter med > alm. forekomst.
    """
    tokens = [t for t in fold(q).split() if t]
    if not tokens:
        return []
    hits = []
    for fag, modul, side, ikon, keys, tab in INDEX:
        hay = fold(" ".join([fag, modul] + keys))
        if not all(t in hay for t in tokens):
            continue
        score = 0
        mf = fold(modul)
        for t in tokens:
            if any(fold(k) == t for k in keys):
                score += 30                    # eksakt nøgleord ("eoq")
            if mf.startswith(t):
                score += 12                    # modulnavnet starter med ordet
            score += hay.count(t)              # alm. forekomst som svag stemme
        hits.append((score, fag, modul, side, ikon, tab))
    hits.sort(key=lambda h: -h[0])
    return hits


def gaa_til(side: str, modul: str | None) -> None:
    """Naviger til en fagside — evt. direkte til et modul (deep-link)."""
    if modul and side in DEEP_SIDER:
        st.session_state["goto_modul"] = modul
    st.switch_page(side)


# --- Hero -------------------------------------------------------------------
n_ord = sum(len(keys) for *_, keys, _tab in ((e[0], e[1], e[2], e[3], e[4], e[5]) for e in INDEX))
kort_css = "\n".join(
    f'[class*="st-key-fagkort_{i}"] {{ --kort-accent: {FAGFARVER.get(navn, "#3b82f6")}; }}'
    for i, (_ikon, navn, _side, _besk) in enumerate(FAG)
)
st.markdown(
    f"""
<style>{kort_css}</style>
<div class="hero-wrap">
  <div class="hero-eyebrow">Logistikøkonom · alle {len(FAG)} fag ét sted</div>
  <div class="hero-title">Opslagsværktøj</div>
  <p class="hero-tag">Tast tal ind, få svaret med det samme, og se mellemregningerne
  du kan skrive direkte ind i opgaven. Korrekthed frem for alt.</p>
  <div class="hero-stats">
    <span class="stat-chip"><b>{len(FAG)}</b> fag</span>
    <span class="stat-chip"><b>{len(INDEX)}</b> moduler</span>
    <span class="stat-chip"><b>{n_ord}</b> søgeord</span>
    <span class="stat-chip"><b>🎓</b> forsvarstræning</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# --- Global søgning ---------------------------------------------------------
q = st.text_input(
    "🔍 Søg i alle moduler og begreber",
    placeholder="fx EOQ, hypotesetest, Kraljic, DDP, ZOPA, kontrolkort, MRP …",
    key="global_soeg",
).strip()

if q:
    hits = soeg(q)
    if hits:
        st.markdown(f"**{len(hits)} resultater** (klik for at gå direkte til modulet):")
        # Gruppér pr. fag i rang-orden (fag rangeres efter deres bedste hit)
        fag_orden, grupper = [], {}
        for h in hits:
            if h[1] not in grupper:
                grupper[h[1]] = []
                fag_orden.append(h[1])
            grupper[h[1]].append(h)
        for fi, fag in enumerate(fag_orden):
            farve = FAGFARVER.get(fag, "#3b82f6")
            st.markdown(
                f'<div class="soeg-fag-h"><span class="prik" '
                f'style="background:{farve}"></span>{fag}</div>',
                unsafe_allow_html=True,
            )
            for hi, (_s, _fag, modul, side, ikon, tab) in enumerate(grupper[fag]):
                if tab and side in DEEP_SIDER:
                    if st.button(f"{ikon}  {modul}", key=f"soeghit_{fi}_{hi}",
                                 width="stretch"):
                        gaa_til(side, tab)
                else:
                    st.page_link(side, label=f"{ikon}  {modul}", width="stretch")
    else:
        st.info("Ingen moduler matchede søgningen. Prøv et andet ord (fx 'lager', 'rente', 'kultur').")
    st.divider()
    st.caption("Ryd søgefeltet for at se alle fag.")
else:
    # Hurtige genveje — de mest brugte opslag med ét klik
    genveje = [
        ("EOQ", P_INDKOEB, "EOQ"),
        ("NPV", P_OEKO, None),
        ("Hypotesetest", P_STAT, None),
        ("MRP", P_PROD, "MRP"),
        ("Kraljic", P_INDKOEB, "Strategi & modeller"),
        ("ZOPA", P_KOMM, None),
    ]
    gcols = st.columns(len(genveje))
    for gi, (navn, side, tab) in enumerate(genveje):
        with gcols[gi]:
            if st.button(navn, key=f"genvej_{gi}", width="stretch"):
                gaa_til(side, tab)

    st.divider()

    cols = st.columns(3, gap="large")
    for i, (ikon, navn, side, indhold) in enumerate(FAG):
        with cols[i % 3]:
            with st.container(border=True, key=f"fagkort_{i}"):
                st.markdown(f'<div class="fag-badge">{ikon}</div>', unsafe_allow_html=True)
                st.page_link(side, label=navn, width="stretch")
                st.caption(indhold)

    st.divider()
    st.caption(
        "Klik på et fag, brug genvejene, eller søg øverst for at hoppe direkte til et modul. "
        "Hold musen over (?)-ikonerne for forklaringer i hverdagssprog."
    )
