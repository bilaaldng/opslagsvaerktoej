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
from components.forside import vis_forside  # noqa: E402
from data.index import INDEKS  # noqa: E402

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
P_ORDBOG = "pages/10_Ordbog.py"
P_PROJ = "pages/11_Projektstyring.py"
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
# Projektstyring (3. semester, 4 ECTS af den tværfaglige prøve) — samme plads
FAG.insert(len(FAG) - 1, ("📋", "Projektstyring", P_PROJ,
                          "Projekt eller drift · Kendt & ukendt · De fire processer · "
                          "Projektorganisationen · Projektlederen · Projektmodeller · "
                          "Scrum & Kanban · De fem i balance · Personprofiler"))
# Ordbogen er ikke et fag — den samler begreberne på tværs, så den ligger sidst.
FAG.append(("📖", "Ordbog", P_ORDBOG,
            "131 begreber på tværs af fagene · 47 af dem lever i flere fag · "
            "hvert begreb linker direkte til det modul der underviser i det"))

def gaa_til(side: str, modul: str | None) -> None:
    """Naviger til en fagside — evt. direkte til et modul (deep-link).

    Alle fagsider har nu en modulvælger, så deep-link virker overalt
    (tidligere kun på de tre sider i DEEP_SIDER).
    """
    if modul:
        st.session_state["goto_modul"] = modul
    st.switch_page(side)


# --- 3D-forsiden ------------------------------------------------------------
# Forsiden er ikke Streamlit-widgets, men rigtig HTML/WebGL — se
# components/forside.py for hvorfor og for de tre srcdoc-fælder den omgår.
#
# Navigationen: rammen må ikke selv skifte side, men den må klikke på
# Streamlits egne elementer. Derfor lægger vi en skjult knap pr. opslag her,
# som rammen udløser. Python gør resten via gaa_til().
st.markdown(
    '<style>[class*="st-key-skjulte_hop"]{display:none !important}</style>',
    unsafe_allow_html=True,
)
with st.container(key="skjulte_hop"):
    for _i, (_fag, _titel, _side, _modul, _ord) in enumerate(INDEKS):
        if st.button("hop", key=f"hop_{_i}"):
            gaa_til(_side, _modul)

vis_forside(
    fag=[(navn, side, besk, FAGFARVER.get(navn, "#3b82f6"))
         for _ikon, navn, side, besk in FAG],
    opslag=[(fag, titel, side, FAGFARVER.get(fag, "#3b82f6"), i, ord_)
            for i, (fag, titel, side, _modul, ord_) in enumerate(INDEKS)],
)
