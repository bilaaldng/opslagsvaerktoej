"""Opslagsværktøj for logistikøkonom — forside med klikbar navigation og søgning.

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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ui_theme import inject_css  # noqa: E402

inject_css()

# Sidestier (relativt til denne fil) — bruges af page_link
P_VCA = "pages/0_Værdikædeanalyse.py"
P_INDKOEB = "pages/1_Indkøb.py"
P_PROD = "pages/2_Produktion.py"
P_STAT = "pages/3_Statistik.py"
P_OEKO = "pages/4_Økonomi.py"
P_ORG = "pages/5_Organisation.py"
P_KOMM = "pages/6_Kommunikation.py"

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
     "Normalfordeling · Konfidensinterval · Binomialfordeling · Kontrolkort (p/X̄/R) · Regression"),
    ("💰", "Økonomi", P_OEKO,
     "Investeringskalkule (NPV/IRR) · Break-even · Priskalkulation · "
     "Prisoptimering · Nøgletalsanalyse · Budget"),
    ("🧭", "Organisation", P_ORG,
     "Modelkatalog (Porter, Ansoff, McGregor, Blake & Mouton, Adizes, Hofstede …) · Modelvælger"),
    ("💬", "Kommunikation", P_KOMM,
     "Interessentanalyse · Forhandlingsark (MDO/LDO) · ZOPA · Forhandlingsbibliotek"),
]

# Søgeindeks: hvert modul/begreb med nøgleord og hvilken side det ligger på
INDEX = [
    # Værdikædeanalyse (rammen om de øvrige fag)
    ("Værdikædeanalyse", "Sådan bygger du en VCA (punkt for punkt)", P_VCA, "🔗",
     ["vca", "værdikæde", "værdikædeanalyse", "porter", "værdikæden", "støtteaktiviteter",
      "primære aktiviteter", "infrastruktur", "logistik ind", "logistik ud", "produktion",
      "marketing", "salg", "service", "harmoni", "udfordringer", "rammeaftale", "incoterms"]),
    # Indkøb
    ("Indkøb", "EOQ — optimal ordrestørrelse", P_INDKOEB, "🛒",
     ["eoq", "wilson", "wilsons formel", "ordrestørrelse", "økonomisk ordremængde", "bestilling"]),
    ("Indkøb", "POQ / EPQ", P_INDKOEB, "🛒",
     ["poq", "epq", "produktionsserie", "seriestørrelse"]),
    ("Indkøb", "Genbestillingspunkt + sikkerhedslager", P_INDKOEB, "🛒",
     ["rop", "genbestilling", "benzinlampen", "sikkerhedslager", "ss", "servicegrad", "z-værdi"]),
    ("Indkøb", "ABC / Pareto-analyse", P_INDKOEB, "🛒",
     ["abc", "pareto", "80/20", "klassifikation", "årsværdi"]),
    ("Indkøb", "Forecasting", P_INDKOEB, "🛒",
     ["forecast", "forecasting", "prognose", "glidende gennemsnit", "eksponentiel udglatning",
      "mad", "mape", "mfe", "tracking signal"]),
    ("Indkøb", "Review-systemer (lagerstyring)", P_INDKOEB, "🛒",
     ["review", "periodisk", "kontinuert", "lagerstyring", "max-niveau"]),
    ("Indkøb", "Make-vs-buy / TCO", P_INDKOEB, "🛒",
     ["make or buy", "make-vs-buy", "tco", "total cost", "outsourcing", "insourcing",
      "break-even", "egenproduktion", "ejeromkostning"]),
    ("Indkøb", "Leverandørscore", P_INDKOEB, "🛒",
     ["leverandør", "leverandørevaluering", "vægtet score", "kriterier", "esg"]),
    ("Indkøb", "Strategi & modeller (indkøb)", P_INDKOEB, "🛒",
     ["kraljic", "bensaou", "sourcing", "single", "dual", "exit", "voice", "order winner",
      "qualifier", "tce", "vmi", "esi", "srm", "spend"]),
    # Produktion
    ("Produktion", "POQ (produktionsserie)", P_PROD, "🏭", ["poq", "epq", "produktionsserie"]),
    ("Produktion", "Linjebalancering", P_PROD, "🏭",
     ["linjebalancering", "takt time", "takttid", "stationer", "effektivitet", "balancetab"]),
    ("Produktion", "Processkort", P_PROD, "🏭",
     ["processkort", "værdigivende", "v/iv", "lean", "spild"]),
    ("Produktion", "Knap kapacitet / flaskehals", P_PROD, "🏭",
     ["knap kapacitet", "flaskehals", "dækningsbidrag", "db pr. time", "produktmix"]),
    ("Produktion", "Produktionsstrategi (5 dimensioner)", P_PROD, "🏭",
     ["produktionsstrategi", "mts", "mto", "ato", "eto", "lean", "fordisme", "jit", "layout",
      "ordretype", "make to stock"]),
    ("Produktion", "MPS + ATP", P_PROD, "🏭",
     ["mps", "atp", "master production schedule", "available to promise", "pei"]),
    ("Produktion", "MRP (materialebehovsplanlægning)", P_PROD, "🏭",
     ["mrp", "bom", "stykliste", "materialebehov", "lot-for-lot", "lotstørrelse", "bruttobehov"]),
    ("Produktion", "S&OP (Level vs. Chase)", P_PROD, "🏭",
     ["s&op", "sop", "aggregeret plan", "level", "chase", "arbejdsstyrke"]),
    ("Produktion", "Little's Law", P_PROD, "🏭",
     ["little", "littles law", "wip", "gennemløbstid", "gennemløb"]),
    ("Produktion", "OEE", P_PROD, "🏭",
     ["oee", "tilgængelighed", "ydelse", "kvalitet", "overall equipment"]),
    ("Produktion", "Perfect Order / OTIF", P_PROD, "🏭",
     ["otif", "perfect order", "leveringspræcision", "til tiden"]),
    ("Produktion", "Udnyttelsesgrad ρ (kø)", P_PROD, "🏭",
     ["udnyttelsesgrad", "rho", "kø", "ventetid", "lambda", "my", "kapacitet"]),
    # Statistik
    ("Statistik", "Normalfordeling", P_STAT, "📊",
     ["normalfordeling", "z", "z-score", "areal", "gauss", "standardafvigelse"]),
    ("Statistik", "Konfidensinterval", P_STAT, "📊",
     ["konfidensinterval", "ki", "middelværdi", "andel", "t-fordeling", "margin of error"]),
    ("Statistik", "Binomialfordeling", P_STAT, "📊",
     ["binomial", "binomialfordeling", "sandsynlighed", "x ud af n", "succeser"]),
    ("Statistik", "Kontrolkort (SPC)", P_STAT, "📊",
     ["kontrolkort", "spc", "p-kort", "x-kort", "r-kort", "ucl", "lcl", "proceskontrol",
      "statistisk kvalitetskontrol", "kapabilitet"]),
    ("Statistik", "Regression (lineær)", P_STAT, "📊",
     ["regression", "lineær regression", "scatter", "scatterplot", "r²", "r2", "fittet linje",
      "korrelation", "hældning", "sammenhæng", "mindste kvadraters"]),
    # Økonomi
    ("Økonomi", "Investeringskalkule (NPV/IRR)", P_OEKO, "💰",
     ["npv", "kapitalværdi", "irr", "intern rente", "payback", "tilbagebetalingstid",
      "kritisk levetid", "investering", "cashflow", "nutidsværdi"]),
    ("Økonomi", "Break-even / nulpunkt", P_OEKO, "💰",
     ["break-even", "nulpunkt", "dækningsgrad", "dækningsbidrag", "sikkerhedsmargin"]),
    ("Økonomi", "Priskalkulation", P_OEKO, "💰",
     ["priskalkulation", "bidragskalkulation", "fordelingskalkulation", "retrograd",
      "kostpris", "salgspris"]),
    ("Økonomi", "Prisoptimering (monopol)", P_OEKO, "💰",
     ["prisoptimering", "totalmetoden", "grænsemetoden", "grænseomsætning", "monopol"]),
    ("Økonomi", "Nøgletalsanalyse", P_OEKO, "💰",
     ["nøgletal", "afkastningsgrad", "overskudsgrad", "soliditet", "likviditet", "gearing",
      "dupont", "egenkapitalforrentning", "aoh", "regnskab", "balance", "passiver", "aktiver"]),
    ("Økonomi", "Budget", P_OEKO, "💰",
     ["budget", "resultatbudget", "likviditetsbudget", "afskrivning", "lineær afskrivning"]),
    # Organisation
    ("Organisation", "Modelkatalog + Modelvælger", P_ORG, "🧭",
     ["porter", "generiske strategier", "ansoff", "vækstmatrix", "lean", "agil", "sc-strategi",
      "organisationsstruktur", "silo", "organisk", "mekanistisk", "mcgregor", "teori x", "teori y",
      "schein", "menneskesyn", "ledergitter", "blake", "mouton", "adizes", "paei", "hofstede",
      "kultur", "ledelse", "ledelsesstil", "motivation", "modelvælger"]),
    # Kommunikation
    ("Kommunikation", "Interessentanalyse", P_KOMM, "💬",
     ["interessent", "interessentanalyse", "magt", "interesse", "power-interest", "mendelow"]),
    ("Kommunikation", "Forhandlingsark + ZOPA", P_KOMM, "💬",
     ["forhandling", "forhandlingsark", "bargaining", "mdo", "ldo", "målpunkt", "modstandspunkt",
      "zopa", "byttechip"]),
    ("Kommunikation", "Forhandlingsbibliotek", P_KOMM, "💬",
     ["bapta", "batna", "alternativ", "principiel forhandling", "harvard", "distributiv",
      "integrativ", "kulturelle forhandlingsstile", "win-win"]),
]


st.title("📦 Opslagsværktøj")
st.caption(
    "Hurtigt opslag og anvendelse under opgaveskrivning og eksamen. "
    "Tast tal ind, få svar, og se grafen reagere. Korrekthed frem for alt."
)

# --- Global søgning --------------------------------------------------------
q = st.text_input(
    "🔍 Søg i alle moduler og begreber",
    placeholder="fx EOQ, Kraljic, NPV, ZOPA, kontrolkort, MRP, Hofstede …",
    key="global_soeg",
).lower().strip()

if q:
    hits = []
    for fag, modul, side, ikon, keys in INDEX:
        if (q in fag.lower() or q in modul.lower() or any(q in k for k in keys)):
            hits.append((fag, modul, side, ikon))
    if hits:
        st.markdown(f"**{len(hits)} resultater** (klik for at gå til faget):")
        for fag, modul, side, ikon in hits:
            st.page_link(side, label=f"{ikon}  {fag}  ·  {modul}", use_container_width=True)
    else:
        st.info("Ingen moduler matchede søgningen. Prøv et andet ord (fx 'lager', 'rente', 'kultur').")
    st.divider()
    st.caption("Ryd søgefeltet for at se alle fag.")
else:
    st.markdown(
        "Klik på et fag herunder eller i menuen til venstre. Hvert regnetungt modul er en "
        "regnemaskine med **dynamisk graf** og **mellemregninger**, og de bløde fag har "
        "søgbare modelbiblioteker."
    )
    st.divider()

    cols = st.columns(3, gap="large")
    for i, (ikon, navn, side, indhold) in enumerate(FAG):
        with cols[i % 3]:
            with st.container(border=True):
                st.page_link(side, label=f"{ikon} {navn}", use_container_width=True)
                st.caption(indhold)

    st.divider()
    st.success(
        "Alle seks fag er klar. Brug søgefeltet øverst til at hoppe direkte til et emne, "
        "eller klik et fag. Hold musen over (?)-ikonerne for forklaringer.",
        icon="✅",
    )
