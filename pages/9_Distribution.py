"""Distribution — 3. semester: transport, netværksdesign, Lean/QRM, lager.

Moduler: Transportformsvalg · Tyngdepunktsmetoden (gravity) · Distributions-
netværk (Chopra) · Lean & QRM · Kanban-beregner · Lager & plukning ·
Køre-hviletid & vægte · Told & dokumenter · Grøn godstransport.
Tal, notation og modeller matcher fagets eget kursusmateriale (Chopra kap. 4-5,
IOSM kap. 13, QRM 1-5, Warehouse Management 1-3, transport-deckene).
"""
import math
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import distribution as ds  # noqa: E402
from ui_theme import (  # noqa: E402
    inject_css, vis_fig,
    C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_MUTED,
)

st.set_page_config(page_title="Distribution", page_icon="🚚", layout="wide")
inject_css()


def num(x, dec=0):
    """Tal med dansk format: punktum som tusindtalsskiller, komma som decimal."""
    if x is None or (isinstance(x, float) and (np.isnan(x) or np.isinf(x))):
        return "—"
    s = f"{x:,.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


st.title("🚚 Distribution")
st.caption(
    "3. semester: hvordan varer kommer fra fabrik til kunde. Transportformer og "
    "-regler, design af distributionsnetværket, Lean/QRM i produktionen og lagerets "
    "drift. To regnemaskiner (tyngdepunkt og kanban) + opslag med fagets egne tal."
)

# --- Modulvælger (samme deep-link-konvention som Indkøb/Produktion) ---------
MODULER = [
    "Transportformsvalg", "Tyngdepunktsmetoden", "Distributionsnetværk (Chopra)",
    "Lean & QRM", "Kanban-beregner", "Lager & plukning",
    "Køre-hviletid & vægte", "Volumenvægt & fragtgrundlag",
    "Luftfragt & frihedsrettigheder", "Told & dokumenter", "Grøn godstransport",
]

goto = st.session_state.pop("goto_modul", None)
if goto in MODULER:
    st.session_state["dist_modul"] = goto
elif "dist_modul" not in st.session_state:
    st.session_state["dist_modul"] = MODULER[0]

modul = st.pills("Vælg modul", MODULER, key="dist_modul",
                 label_visibility="collapsed")
if modul is None:
    modul = MODULER[0]


# ===========================================================================
# Transportformsvalg
# ===========================================================================
if modul == "Transportformsvalg":
    st.subheader("Valg af transportform")
    st.caption("Ingen transportform vinder på alt — valget er en afvejning af "
               "hastighed, pris, godsets art, frekvens og hvor mange omlastninger "
               "du kan leve med. Til eksamen: argumentér for afvejningen, "
               "ikke kun for konklusionen.")

    styrker = pd.DataFrame([
        ["🚛 Vej", "Hurtig levering · fleksibel · mangfoldigt materiel · hyppige afgange · "
         "praktisk for både afsender og modtager (dør til dør)"],
        ["🚆 Bane", "Massetransport · lave enhedsomkostninger · pålidelig · langdistance · "
         "bred dækning · specialiseret materiel"],
        ["🚢 Vand", "Meget lave enhedsomkostninger · varer med lav enhedsværdi · "
         "langdistance · massetransport af bulk"],
        ["🛢️ Rørledning", "Laveste enhedsomkostninger · flydende/gasformige produkter · "
         "stor kapacitet · den mest pålidelige transportform"],
        ["✈️ Luft", "Den hurtigste af alle · levering fra dag til dag · hyppig betjening "
         "af store markeder"],
        ["📦 Intermodal", "Kombinerer formerne (container) · omkostningsbesparelser · "
         "færre skader pga. containerisering · når flere afsendere/modtagere"],
    ], columns=["Transportform", "Væsentlige fordele (fagets liste)"])
    st.dataframe(styrker, hide_index=True, width="stretch")

    v1, v2 = st.columns([1, 1])
    with v1:
        st.markdown("**Hvem flytter godset i dag?** Modal split fra undervisningen:")
        split = pd.DataFrame(
            {"Danmark (national)": [90, 5, 5, 0], "International": [23, 3, 73, 1]},
            index=["Vej", "Bane", "Skib", "Luft"])
        fig = go.Figure()
        fig.add_bar(name="DK national", x=split.index, y=split["Danmark (national)"],
                    marker_color=C_TOTAL)
        fig.add_bar(name="International", x=split.index, y=split["International"],
                    marker_color=C_ORDER)
        fig.update_layout(barmode="group", yaxis_title="% af transporteret mængde",
                          height=320)
        vis_fig(fig)
        st.caption("Vejen dominerer nationalt (90 %); skibet dominerer internationalt "
                   "(73 %). Luftfragt er næsten intet i mængde — men høj i værdi.")
    with v2:
        st.markdown("**Samme tur, tre former** — fagets eksempel Billund → Milano:")
        st.markdown(
            "- **Vej:** 2 dage (1 chauffør) · **1 dag med 2 chauffører** · ingen "
            "omlastning · høj frekvens\n"
            "- **Bane:** 2–4 dage · daglig fast afgang · men flere led: lastbil til "
            "terminal → tog → rangering → lastbil ud\n"
            "- **Skib:** 3–6 dage · billigst · flest omladninger (havn → havn → lastbil)\n\n"
            "Hvert ekstra led = ekstra tid, ekstra håndtering og ekstra skadesrisiko. "
            "Store containerskibe rummer 4.000–12.000 containere — dét er kilden til "
            "søfragtens lave enhedspris.")
        st.info("**Husk reklamations-vinklen:** de hyppigste serviceklager handler om "
                "beskadigede varer, overskredet transittid og fejl i fragtdokumenter "
                "(konnossement/bill of lading). Transportvalget er også et valg af, "
                "hvor de risici ligger — og ansvaret afgøres af leveringsbetingelsen "
                "(se Incoterms på Jura-siden).")

    st.page_link("pages/8_Jura.py", label="⚖️ Incoterms — hvem bærer risikoen undervejs?")


# ===========================================================================
# Tyngdepunktsmetoden (gravity location model)
# ===========================================================================
elif modul == "Tyngdepunktsmetoden":
    st.subheader("Tyngdepunktsmetoden — hvor skal lageret ligge?")
    st.caption(
        "Gravity-modellen (Chopra kap. 5, fase III): find det punkt der minimerer den "
        "samlede transportomkostning **TC = Σ Dₙ·Fₙ·dₙ** — mængde × fragtrate × "
        "luftlinjeafstand, summeret over alle kunder/kilder. Indtast koordinater og "
        "mængder (fx fra et kort med gitter), så regnes både tyngdepunktet og det "
        "iterative optimum."
    )

    default = pd.DataFrame({
        "Punkt": ["Kunde A", "Kunde B", "Kunde C", "Kunde D"],
        "x": [2.0, 10.0, 6.0, 12.0],
        "y": [3.0, 8.0, 12.0, 2.0],
        "Mængde D": [1200.0, 900.0, 600.0, 400.0],
        "Fragtrate F": [1.0, 1.0, 1.0, 1.0],
    })
    tabel = st.data_editor(
        default, num_rows="dynamic", hide_index=True, key="dist_tp_tabel",
        column_config={
            "x": st.column_config.NumberColumn(help="Punktets vandrette koordinat på dit gitter/kort."),
            "y": st.column_config.NumberColumn(help="Punktets lodrette koordinat."),
            "Mængde D": st.column_config.NumberColumn(
                help="Hvor meget der skal TIL eller FRA punktet pr. periode "
                     "(stk., paller, ton — bare samme enhed hele vejen)."),
            "Fragtrate F": st.column_config.NumberColumn(
                help="Transportomkostning pr. enhed pr. afstandsenhed. Lad den stå "
                     "på 1 hvis raten er ens overalt — så vægtes kun med mængden. "
                     "Leverandører med dyr indgående fragt kan få højere F."),
        })

    punkter = [
        {"x": float(r["x"]), "y": float(r["y"]),
         "D": float(r["Mængde D"]), "F": float(r["Fragtrate F"])}
        for _, r in tabel.iterrows()
        if pd.notna(r["x"]) and pd.notna(r["y"]) and pd.notna(r["Mængde D"])
        and float(r["Mængde D"]) > 0
    ]

    if len(punkter) < 2:
        st.info("Tilføj mindst to punkter med mængde > 0.")
    else:
        res = ds.optimer_placering(punkter)
        m1, m2, m3 = st.columns(3)
        m1.metric("Tyngdepunkt (startpunkt)",
                  f"({num(res['start_x'], 1)} · {num(res['start_y'], 1)})",
                  help="Vægtet gennemsnit af koordinaterne: x* = Σ(D·F·x)/Σ(D·F). "
                       "Det er metodens startpunkt — godt, men sjældent helt optimalt.")
        m2.metric("Optimum (iterativt)",
                  f"({num(res['x'], 1)} · {num(res['y'], 1)})",
                  help="Punktet der minimerer TC. Findes ved at flytte placeringen "
                       "skridt for skridt mod lavere samlet omkostning, indtil den "
                       "står stille (Chopras gravity-model løses iterativt).")
        bespar = res["start_TC"] - res["TC"]
        m3.metric("TC i optimum", num(res["TC"], 0),
                  delta=f"-{num(bespar, 0)} ift. tyngdepunktet" if bespar > 0.5 else "≈ tyngdepunktet",
                  delta_color="inverse" if bespar > 0.5 else "off",
                  help="Samlet transportarbejde Σ D·F·d i optimum. Enheden er "
                       "'mængde × rate × afstand' — brug den til at SAMMENLIGNE "
                       "placeringer, ikke som kroner i sig selv.")

        # --- kort ---
        fig = go.Figure()
        st_mgd = [p["D"] * p["F"] for p in punkter]
        skala = 40 / max(st_mgd)
        fig.add_scatter(
            x=[p["x"] for p in punkter], y=[p["y"] for p in punkter],
            mode="markers+text",
            text=[r["Punkt"] for _, r in tabel.iterrows()
                  if pd.notna(r["x"]) and pd.notna(r["y"])
                  and pd.notna(r["Mængde D"]) and float(r["Mængde D"]) > 0],
            textposition="top center", name="Kunder/kilder",
            marker=dict(size=[max(10, v * skala) for v in st_mgd],
                        color=C_TOTAL, opacity=0.75),
        )
        fig.add_scatter(x=[res["start_x"]], y=[res["start_y"]],
                        mode="markers", name="Tyngdepunkt",
                        marker=dict(symbol="diamond", size=14, color=C_ORDER))
        fig.add_scatter(x=[res["x"]], y=[res["y"]],
                        mode="markers", name="Optimum",
                        marker=dict(symbol="star", size=18, color=C_OPT))
        fig.update_layout(height=430, xaxis_title="x", yaxis_title="y",
                          yaxis_scaleanchor="x")
        vis_fig(fig)
        st.caption("Boblernes størrelse = vægt (D·F). Optimum trækkes mod de tunge "
                   "punkter — med ét meget dominerende punkt ender det praktisk talt "
                   "oven i det.")

        with st.expander("🧮 Mellemregninger + test din egen placering"):
            st.markdown("**TC-bidrag pr. punkt i optimum** (D · F · afstand):")
            rows = []
            for p, navn in zip(punkter, [r["Punkt"] for _, r in tabel.iterrows()
                                         if pd.notna(r["x"]) and pd.notna(r["y"])
                                         and pd.notna(r["Mængde D"])
                                         and float(r["Mængde D"]) > 0]):
                d = math.hypot(res["x"] - p["x"], res["y"] - p["y"])
                rows.append([navn, num(p["D"], 0), num(p["F"], 2), num(d, 2),
                             num(p["D"] * p["F"] * d, 1)])
            st.dataframe(pd.DataFrame(
                rows, columns=["Punkt", "D", "F", "afstand d", "bidrag D·F·d"]),
                hide_index=True, width="stretch")
            st.caption(f"Sum = TC = {num(res['TC'], 1)}. Til opgaven: vis formlen, "
                       "de vægtede gennemsnit for tyngdepunktet, og at kandidaten med "
                       "lavest TC vælges.")
            k1, k2, k3 = st.columns(3)
            kx = k1.number_input("Kandidat x", value=float(round(res["x"])),
                                 key="dist_tp_kx",
                                 help="Test fx en realistisk adresse i nærheden — "
                                      "optimums koordinater kan sjældent bebygges.")
            ky = k2.number_input("Kandidat y", value=float(round(res["y"])),
                                 key="dist_tp_ky")
            tc_k = ds.total_transportomkostning(kx, ky, punkter)
            k3.metric("TC på kandidaten", num(tc_k, 0),
                      delta=f"+{num(tc_k - res['TC'], 0)} ift. optimum",
                      delta_color="inverse")

        st.info("**Metodens begrænsninger** (nævn dem i opgaven): luftlinjeafstande "
                "(ikke vejnet), lineære omkostninger, kun ét anlæg, og ingen hensyn "
                "til grunde, arbejdskraft eller infrastruktur. Derfor er resultatet et "
                "**udgangspunkt** for fase III i Chopras rammeværk — man leder efter en "
                "egnet, bebyggelig placering i nærheden, ikke på præcis den koordinat.")


# ===========================================================================
# Distributionsnetværk (Chopra)
# ===========================================================================
elif modul == "Distributionsnetværk (Chopra)":
    st.subheader("De seks distributionsnetværk (Chopra kap. 4)")
    st.caption(
        "To spørgsmål definerer designet: **(1)** leveres varen til kunden, eller "
        "henter kunden den? **(2)** går varen gennem et mellemled? Svarene giver seks "
        "netværk med hver deres styrker. Ingen vinder på alt — designet skal passe til "
        "produktet og strategien."
    )

    DESIGNS = [
        ("1 · Producentlager med direkte forsendelse (drop-shipping)",
         "Varen sendes direkte fra producenten til kunden — forhandleren har intet lager.",
         "Bedst til varer med høj værdi, lav og usikker efterspørgsel og stor variation: "
         "lageret samles ét sted (aggregering), så sikkerhedslageret bliver lille.",
         "Høj transportomkostning, lang svartid, delleverancer fra flere producenter, "
         "og returnering/sporing er besværlig."),
        ("2 · Producentlager med sammenlægning undervejs (in-transit merge)",
         "Dele fra flere producenter mødes hos fragtføreren og leveres som ÉN samlet "
         "leverance (fx pc fra én fabrik + skærm fra en anden).",
         "Samme lagerfordele som drop-shipping, men lavere transportomkostning og en "
         "bedre kundeoplevelse (én levering).",
         "Kræver avanceret koordinering — egner sig bedst til få kilder (4-5 steder)."),
        ("3 · Distributørlager med pakkelevering",
         "Varen ligger på et mellemlager tættere på kunden og sendes med pakkedistributør.",
         "Hurtigere svar, lavere transportomkostning, nemmere sporing og returnering. "
         "Passer til varer der sælges jævnt (medium/hurtige).",
         "Mere lager end producentlager (mindre aggregering) og et ekstra led at drive."),
        ("4 · Distributørlager med last-mile-levering",
         "Distributøren kører selv varen helt hjem til kunden (fx dagligvarer).",
         "Hurtigst af leverings-modellerne og bedst til returnering/oplevelse.",
         "Dyrest i transport (ingen stordrift på sidste kilometer) og dyre faciliteter — "
         "kræver tætbefolkede områder, store varer eller et eksisterende net."),
        ("5 · Producent-/distributørlager med kundeafhentning",
         "Lageret bliver opstrøms; kunden henter på et aftalt afhentningssted.",
         "Meget lav transportomkostning (samlede leverancer til punktet) — især oven på "
         "et net af steder man har i forvejen.",
         "Håndteringsomkostning på afhentningsstedet og mindre bekvemt for kunden."),
        ("6 · Butikslager med kundeafhentning",
         "Varen ligger lokalt i butikker; kunden går ind eller bestiller og henter.",
         "Hurtigst svartid af alle og lavest transportomkostning. Bedst til hurtigt "
         "omsættelige varer og kunder der vil have varen NU.",
         "Højeste lager- og facilitetsomkostning (mange decentrale lagre)."),
    ]
    for titel, hvad, styrke, svaghed in DESIGNS:
        with st.expander(titel):
            st.markdown(f"{hvad}\n\n**Styrker:** {styrke}\n\n**Svagheder:** {svaghed}")

    st.markdown("**Sammenligningen fra kompendiet** (placering 1 = bedst på dimensionen):")
    rank = pd.DataFrame(
        {
            "Butik m. afhentning": [1, 4, 4, 5, 1, 1, 4, 1, 6, 1],
            "Direkte forsendelse": [4, 1, 1, 4, 5, 5, 1, 4, 1, 4],
            "In-transit merge": [4, 1, 1, 3, 4, 5, 1, 3, 2, 4],
            "Distributør + pakke": [3, 2, 2, 2, 3, 4, 2, 2, 3, 3],
            "Distributør + last-mile": [2, 3, 3, 1, 2, 3, 3, 5, 4, 2],
            "Producentlager m. afhentning": [4, 1, 1, 5, 6, 2, 1, 1, 5, 5],
        },
        index=["Svartid", "Varesortiment", "Tilgængelighed", "Kundeoplevelse",
               "Ordresynlighed", "Returnering", "Lager", "Transport",
               "Faciliteter & håndtering", "Information"])
    st.dataframe(rank, width="stretch")
    st.caption("Læs kolonnevis: butiks-modellen vinder på tid og transport, men taber på "
               "lager og faciliteter; drop-shipping er det omvendte spejlbillede. "
               "Hybrid er normalen i praksis: hurtige varer lokalt, langsomme centralt, "
               "de langsomste drop-shippes.")

    st.markdown("#### Hvor mange lagre? U-kurven")
    n = np.arange(1, 13)
    lager = 14 * np.sqrt(n)               # illustrativ: lager vokser med antal anlæg
    facil = 6 * n + 8                     # illustrativ: faste omkostninger pr. anlæg
    transport = 150 / n + 3.5 * n         # illustrativ: ud-transport falder, ind-stordrift tabes
    total = lager + facil + transport
    fig = go.Figure()
    fig.add_scatter(x=n, y=lager, name="Lager", line=dict(color=C_ORDER))
    fig.add_scatter(x=n, y=facil, name="Faciliteter", line=dict(color=C_MUTED))
    fig.add_scatter(x=n, y=transport, name="Transport", line=dict(color=C_HOLD))
    fig.add_scatter(x=n, y=total, name="Total logistikomkostning",
                    line=dict(color=C_TOTAL, width=4))
    nmin = int(n[np.argmin(total)])
    fig.add_scatter(x=[nmin], y=[float(total.min())], mode="markers",
                    name="Omkostningsminimum",
                    marker=dict(size=14, color=C_OPT, symbol="star"))
    fig.update_layout(height=380, xaxis_title="Antal lagre/faciliteter →",
                      yaxis_title="Omkostning (illustrativ) →")
    vis_fig(fig)
    st.caption("Principfigur (ikke rigtige tal): flere lagre → kortere svartid og "
               "billigere ud-transport, men mere lager og flere faste omkostninger — "
               "totalen er U-formet. Chopras regel: hold mindst det antal der minimerer "
               "totalomkostningen, og tilføj kun flere hvis den hurtigere svartid "
               "tjener mere ind end den koster.")

    with st.expander("📐 Netværksdesign i praksis (kap. 5): beslutninger, faktorer og faserne"):
        st.markdown(
            "**Fire beslutninger der hænger sammen:** anlæggets **rolle** · "
            "**placering** · **kapacitet** · **hvilke markeder/leverandører** det "
            "kobles til. De er dyre og svære at gøre om — derfor rammeværket:\n\n"
            "1. **Fase I — strategi:** skal kæden være billig eller hurtig? (cost vs. "
            "responsiveness)\n"
            "2. **Fase II — regioner:** hvor mange anlæg, i hvilke regioner, ca.-kapacitet "
            "(efterspørgsel, stordrift, told, skat, risiko — den kapaciterede "
            "placeringsmodel)\n"
            "3. **Fase III — kandidatsteder:** en bruttoliste af egnede steder med hård "
            "infrastruktur (leverandører, transport, forsyning) og blød (arbejdskraft, "
            "kompetencer) — her bruges **tyngdepunktsmetoden**\n"
            "4. **Fase IV — endeligt valg:** præcis placering + fordeling af "
            "efterspørgslen, så samlet profit maksimeres\n\n"
            "**Faktorer der trækker:** strategi (omkostningsleder vs. responsiv) · "
            "teknologi (stordrift vs. lokale anlæg) · makroøkonomi (told, skattefordele, "
            "valutakurs) · politik/stabilitet · infrastruktur · konkurrenter (klynge "
            "eller afstand) · krav til svartid · logistikomkostninger. Husk også "
            "Ferdows' anlægsroller (offshore → source, server → contributor, outpost, "
            "lead) hvis rollen skal begrundes.")
    st.page_link("pages/1_Indkøb.py", label="🛒 Sikkerhedslager og aggregering — se Genbestilling + SS")


# ===========================================================================
# Lean & QRM
# ===========================================================================
elif modul == "Lean & QRM":
    st.subheader("Lean & QRM — to svar på 'hvordan producerer vi klogt?'")
    st.caption(
        "**Lean** fjerner spild i stabile flows med høj volumen. **QRM** (Quick Response "
        "Manufacturing) angriber TIDEN og er bygget til lav volumen og høj variation. "
        "Faget bruger Christophers matrix til at vise, hvornår hvilken strategi passer."
    )

    v1, v2 = st.columns([1, 1])
    with v1:
        st.markdown("#### Christophers generiske forsyningskædestrategier")
        chr_df = pd.DataFrame(
            {"Forudsigelig efterspørgsel": ["**Lean** — planlæg og optimér",
                                            "**Kanban** — løbende genopfyldning"],
             "Uforudsigelig efterspørgsel": ["**Hybrid** — afkobl med postponement",
                                             "**Agil** — hurtig respons"]},
            index=["Lang gennemløbstid (forsyning)", "Kort gennemløbstid (forsyning)"])
        st.dataframe(chr_df, width="stretch")
        st.caption("Aflæs: stabil efterspørgsel + lang forsyningstid → Lean. Uforudsigelig "
                   "efterspørgsel → agilitet/hurtig respons — det er QRM's hjemmebane.")
    with v2:
        st.markdown("#### Hvornår passer hvad?")
        fit = pd.DataFrame([
            ["Volumen", "Høj, gentagen", "Lav, ordreproduceret"],
            ["Variation i produkter", "Lav (erstatningsvarer)", "Høj (kundetilpasset)"],
            ["Efterspørgsel", "Stabil/forudsigelig", "Svingende/uforudsigelig"],
            ["Kerneværktøjer", "Takttid, kanban, flow", "MCT, celler, POLCA"],
            ["Målestok", "Spild elimineret", "Gennemløbstid (MCT) reduceret"],
        ], columns=["", "Lean/JIT trives ved", "QRM trives ved"])
        st.dataframe(fit, hide_index=True, width="stretch")

    st.markdown("#### Lean: de 5 principper")
    st.markdown(
        "Rammen om alt det andet. Rækkefølgen er ikke tilfældig — hvert princip "
        "forudsætter det foregående:\n\n"
        "1. **Værdi** — kunden definerer, hvad der er værd at betale for. Ikke "
        "afdelingen, ikke maskinen.\n"
        "2. **Værdistrøm** — kortlæg alle skridt fra råvare til kunde, og skil "
        "dem der tilfører værdi fra dem der ikke gør (se værdistrømsanalysen nedenfor).\n"
        "3. **Flow** — få det til at glide uden stop, bunker og ventetid. Ét "
        "stykke ad gangen frem for store batches.\n"
        "4. **Pull** — producér først, når det næste led faktisk trækker. "
        "Signalet er typisk et kanban-kort.\n"
        "5. **Perfektion** — gentag de fire første i det uendelige. Lean er en "
        "retning, ikke en tilstand man når.")
    st.warning(
        "**Fælde til forsvaret:** principperne er en rækkefølge, ikke en menu. "
        "Indfører man pull uden først at have skabt flow, vokser lagrene i "
        "stedet for at falde — pull uden flow er bare et lager med et nyt navn. "
        "Samme pointe gælder omvendt: der er ingen grund til at optimere flow i "
        "et trin, kunden slet ikke betaler for.")

    st.markdown("#### Lean: de 8 former for spild (muda)")
    st.markdown(
        "1. **Overproduktion** — at lave mere/tidligere end der efterspørges (den værste: skaber de andre)\n"
        "2. **Ventetid** — varer eller folk der venter\n"
        "3. **Transport** — unødig flytning af varer\n"
        "4. **Overforædling** — mere bearbejdning end kunden betaler for\n"
        "5. **Lager** — *'lagre er det første tegn på spild'* (fagets formulering)\n"
        "6. **Bevægelse** — unødige menneskelige bevægelser\n"
        "7. **Fejl/omarbejde** — defekte varer og rettearbejde\n"
        "8. **Uudnyttet medarbejderpotentiale** — idéer og evner der ikke bruges\n\n"
        "Værktøjerne omkring dem: **kaizen** (løbende små forbedringer), **jidoka** "
        "(stop ved fejl, byg kvaliteten ind), **pull/kanban** (producér kun det næste "
        "led beder om — se Kanban-beregneren), og **værdistrømsanalyse**:")

    st.markdown("#### Muda er kun den ene af tre")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("**Muda — spild**")
        st.caption("Arbejde uden værdi for kunden. De 8 typer ovenfor. "
                   "Det, alle kan få øje på.")
    with m2:
        st.markdown("**Mura — ujævnhed**")
        st.caption("Svingninger i belastningen: travlt mandag, tomt torsdag. "
                   "Skaber både overbelastning og spild.")
    with m3:
        st.markdown("**Muri — overbelastning**")
        st.caption("Mennesker og maskiner presset ud over det, de kan holde til. "
                   "Giver fejl, nedbrud og sygefravær.")
    st.info(
        "**Rækkefølgen betyder noget:** ujævnhed (mura) skaber overbelastning "
        "(muri), som skaber spild (muda). De fleste jagter kun muda, fordi det "
        "er lettest at se — men fjerner man spildet uden at udjævne "
        "belastningen, kommer det igen. Til forsvaret: peg på årsagen, ikke "
        "kun symptomet.")

    st.markdown("#### To værktøjer, der ofte spørges til")
    s1, s2 = st.columns(2)
    with s1:
        st.markdown("**5S — orden som fundament**")
        st.markdown(
            "Sortér · Sæt i system · Systematisk rengøring · Standardisér · "
            "Selvdisciplin.\n\n"
            "Ikke oprydning for pænhedens skyld: pointen er, at afvigelser "
            "bliver **synlige**. Mangler et værktøj på sin plads, ses det med "
            "det samme. Uden 5S kan man ikke se, om flowet er brudt.")
    with s2:
        st.markdown("**SMED — omstilling som flaskehals**")
        st.markdown(
            "Lang omstillingstid er selve grunden til, at man kører store "
            "batches — og store batches er grunden til lange gennemløbstider.\n\n"
            "Greb: skil **indre** tid (maskinen står stille) fra **ydre** tid "
            "(kan gøres mens den kører), flyt så meget som muligt til ydre, og "
            "forenkl resten. Falder omstillingstiden, falder den økonomiske "
            "seriestørrelse med — og så bliver flow pludselig muligt.")
    st.caption("Regn effekten selv: mindre omstillingstid sænker den optimale "
               "seriestørrelse i **POQ/EPQ** på Indkøb- og Produktion-siderne.")

    st.markdown("#### Værdistrømsanalyse (VSM — 'Learning to See')")
    st.markdown(
        "Tegn HELE flowet for en produktfamilie — fra råvare til kunde — med både "
        "materiale- og informationsstrøm. For hvert trin noteres cyklustid, omstillingstid, "
        "oppetid og lagre. Lagrene omregnes til dage: **lager i dage = lagerantal × "
        "takttid** (fagets eksempel: 7.000 stk. × 60 sek. ≈ 7,6 dage). Så ses det sort på "
        "hvidt: bearbejdningstiden er minutter, men gennemløbstiden er uger — resten er "
        "venten. Nutidskortet (current state) afslører spildet; fremtidskortet (future "
        "state) designer flowet med takt, pull og udjævning.")
    st.page_link("pages/2_Produktion.py",
                 label="🏭 Takttid og linjebalancering ligger på Produktion-siden")

    st.markdown("#### QRM: tidens kraft")
    st.markdown(
        "QRM forfølger **reduktion af gennemløbstid i alle dele af virksomheden** — "
        "eksternt (hurtigt designe og levere til kundens behov) og internt (alle opgaver, "
        "også administration). Kortere tid giver samtidig bedre kvalitet og lavere "
        "omkostninger. De **fire kernebegreber**:\n\n"
        "1. **Tidens kraft** — gennemløbstid betyder langt mere end de fleste tror. "
        "Målestokken er **MCT** (Manufacturing Critical-path Time): den samlede "
        "kalendertid fra ordre til levering ad den kritiske vej. 95 %+ af MCT er "
        "typisk **'det hvide rum'** — ventetid, ikke bearbejdning. Fremdriften følges "
        "med **QRM-tallet = Base-MCT / Aktuel MCT × 100** (starter i 100 og vokser, "
        "når tiden falder — motiverer teams).\n"
        "2. **Organisationsstruktur** — væk fra funktionsopdelte afdelinger, hen til "
        "**QRM-celler**: et lille team med egne, samlokaliserede, dedikerede ressourcer, "
        "krydsoplært til at færdiggøre en hel opgavefamilie for et **FTMS** (fokuseret "
        "målmarkedssegment) uden at opgaven pendler frem og tilbage. Kontorudgaven "
        "hedder en **Q-ROC** (Quick Response Office Cell) — samme princip for "
        "ordrebehandling, tilbud osv.\n"
        "3. **Systemdynamik** — samspillet mellem udnyttelsesgrad og variabilitet: "
        "presses udnyttelsen mod 100 %, **eksploderer køerne og dermed MCT**. QRM "
        "planlægger derfor med **reservekapacitet** (QRM-udnyttelse = 100 % − "
        "reservekapacitet) i stedet for at jagte fuld udnyttelse. Det er også "
        "forklaringen på **responstids-spiralen**: lange lovede leveringstider → mere "
        "der skal hastes igennem → endnu længere tider.\n"
        "4. **Virksomhedsdækkende anvendelse** — QRM er ikke kun for gulvet: "
        "materialestyringen omlægges (HL/MRP på højt niveau) og cellerne kobles med "
        "**POLCA-kort** — et kapacitetssignal mellem celler (i stedet for kanbans "
        "lagersignal), som passer til kundetilpassede varer, hvor man ikke kan have "
        "færdige beholdere stående.")
    st.info("**Eksamensskarp pointe:** høj udnyttelsesgrad LYDER effektivt, men er "
            "gennemløbstidens værste fjende — sammenhængen er ikke lineær, den er en "
            "hockeystav. Regn selv efter med kø-modulet **Udnyttelsesgrad ρ** på "
            "Produktion-siden, og brug argumentet når casen presser kapaciteten.")
    st.page_link("pages/2_Produktion.py", label="🏭 Udnyttelsesgrad ρ (kø) — se kurven selv")


# ===========================================================================
# Kanban-beregner
# ===========================================================================
elif modul == "Kanban-beregner":
    st.subheader("Kanban-kort — hvor mange beholdere skal cirkulere?")
    st.caption(
        "To-korts kanban (IOSM kap. 13): produktionskortet siger 'lav en beholder til', "
        "flyttekortet siger 'hent en beholder'. Antallet af kort sætter loftet for "
        "lageret mellem to led — pull-systemets kerne. Formlen: **y = D·T·(1+x) / C**, "
        "rundet **op**."
    )

    venstre, hoejre = st.columns([1, 2])
    with venstre:
        D = st.number_input("Efterspørgsel D (stk. pr. tidsenhed)", min_value=1.0,
                            value=300.0, step=10.0, key="dist_kb_D",
                            help="Hvor meget det NÆSTE led trækker pr. tidsenhed — "
                                 "fx 300 emner i timen fra slutmontagen.")
        T = st.number_input("Tid T for én beholder", min_value=0.01,
                            value=2.6, step=0.1, key="dist_kb_T",
                            help="Tiden fra beholderen sættes i produktion til den står "
                                 "fyldt hos det næste led (producere + flytte). SAMME "
                                 "tidsenhed som D — er D pr. time, er T i timer.")
        x = st.slider("Sikkerhedsfaktor x (%)", 0, 50, 15, key="dist_kb_x",
                      help="Buffer for udsving i D eller T. 15 % betyder at der regnes "
                           "med 15 % ekstra behov. Lean-ambitionen: sænk den over tid.") / 100
        C = st.number_input("Beholderstørrelse C (stk.)", min_value=1.0,
                            value=45.0, step=1.0, key="dist_kb_C",
                            help="Hvor mange emner én beholder rummer. Mindre beholdere "
                                 "= mindre bundet lager, men hyppigere håndtering.")

    r = ds.kanban_kort(D, T, x, C)
    with hoejre:
        if "fejl" in r:
            st.error(r["fejl"])
        else:
            m1, m2, m3 = st.columns(3)
            m1.metric("Rå værdi y", num(r["y_raa"], 2),
                      help="D·T·(1+x)/C før oprunding.")
            m2.metric("Antal kort/beholdere", f"{r['y']}",
                      help="Rundes ALTID op — rundes der ned, kan systemet ikke dække "
                           "efterspørgslen, og næste led løber tør.")
            m3.metric("Maks. lager mellem leddene", f"{num(r['maks_lager'])} stk.",
                      delta=None,
                      help="y × C. Kanban-systemets pointe: lageret kan aldrig vokse ud "
                           "over antallet af beholdere i omløb.")
            st.markdown(
                f"**Mellemregning:** y = ({num(D)} × {num(T, 2)} × {num(1 + x, 2)}) / "
                f"{num(C)} = {num(r['taeller'], 1)} / {num(C)} = "
                f"**{num(r['y_raa'], 2)} → {r['y']} kort**")

            cs = np.arange(max(5, int(C * 0.3)), int(C * 2.2) + 1)
            ys = [math.ceil(D * T * (1 + x) / c - 1e-9) for c in cs]
            lag = [yv * c for yv, c in zip(ys, cs)]
            fig = go.Figure()
            fig.add_scatter(x=cs, y=lag, name="Maks. lager (y·C)",
                            line=dict(color=C_ORDER, width=3))
            fig.add_scatter(x=cs, y=ys, name="Antal kort y", yaxis="y2",
                            line=dict(color=C_TOTAL, width=3, shape="hv"))
            fig.add_vline(x=C, line_dash="dot", line_color=C_OPT)
            fig.update_layout(
                height=360, xaxis_title="Beholderstørrelse C →",
                yaxis=dict(title="Maks. lager (stk.)"),
                yaxis2=dict(title="Antal kort", overlaying="y", side="right",
                            showgrid=False),
            )
            vis_fig(fig)
            st.caption("Træk i C og se pointen fra kursets eksempel: mindre, "
                       "standardiserede beholdere ændrer måske ikke antallet af kort "
                       "ret meget — men det bundne lager falder markant. Kombinér med "
                       "kortere T (hurtigere celle) for den store gevinst.")

    st.info("**Typiske fælder:** (1) D og T i hver sin tidsenhed — omregn først. "
            "(2) At runde NED 'fordi 19,93 er tættest på 20'... det ER 20; men 19,2 "
            "skal også blive 20 — aldrig 19. (3) At glemme at et kanban-loft kræver "
            "et jævnt flow — ved dramatiske udsving i efterspørgslen skal x op, eller "
            "systemet skal suppleres med planlægning (jf. QRM-kritikken af kanban ved "
            "høj variation).")
    st.page_link("pages/2_Produktion.py", label="🏭 MRP — push-modstykket, når behovet beregnes frem")


# ===========================================================================
# Lager & plukning
# ===========================================================================
elif modul == "Lager & plukning":
    st.subheader("Lageret: roller, drift og plukning")
    st.caption(
        "Warehouse Management 1-3: hvad lageret SKAL kunne (modtage → placere → plukke "
        "→ pakke → forsende), hvorfor lageret overhovedet findes, og hvor pengene "
        "ligger — i plukningen."
    )

    v1, v2 = st.columns([1, 1])
    with v1:
        st.markdown("#### Lagerets roller")
        st.markdown(
            "- **Opbevaring:** råvare-, halvfabrikata- og færdigvarelager\n"
            "- **Konsolidering:** samle små strømme til fulde læs\n"
            "- **Transshipment / cross-dock:** varen krydser lageret uden at blive "
            "lagt på hylde — omfordeles direkte fra ind- til udgående port\n"
            "- **Sortering** og **fulfilment** (ordreekspedition, ofte e-handel)\n"
            "- **Reverse logistics:** returvarer, emballage, reparationer")
        st.markdown("#### Hvorfor har vi lager?")
        st.markdown(
            "Cyklisk lager (seriestørrelser) · sikkerhedslager (usikkerhed) · "
            "transportomkostninger (fulde læs) · mængderabat · produktionsrytme · "
            "sæsonlager · varer i arbejde · investeringslager (spekulativt indkøb). "
            "Hver grund har en modpost i bunden kapital — lagerets berettigelse skal "
            "kunne argumenteres, ikke antages.")
    with v2:
        st.markdown("#### Driftsflowet (fagets tjekliste)")
        st.markdown(
            "1. **Modtagelse:** aflæs → kontrollér mod BÅDE fragtbrev og indkøbsordre → "
            "kvalitet (godkend / godkend med note på fragtbrevet / afvis) → indtast i ERP\n"
            "2. **Placering (put away):** fast plads (nemt at huske) eller **flydende/"
            "kaos** (bedre pladsudnyttelse — kræver system) + reserveplads\n"
            "3. **Frempluk:** FIFO, LIFO eller random — FIFO hvor holdbarhed/ælde betyder noget\n"
            "4. **Pluk → pak** (evt. værditilførsel: mærkning, kitting)\n"
            "5. **Marshalling & forsendelse:** klargør pr. transportør, meld færdig i ERP, "
            "varen afgangsføres (goods issue)")

    st.markdown("#### Plukning — dér ligger omkostningen")
    st.markdown("Fagets nøglesætning: **den største omkostning stammer fra bevægelsen "
                "mellem de enkelte pluk.** Strategierne handler derfor om at få flere "
                "ordrelinjer ud af hver meter:")
    pluk = pd.DataFrame([
        ["Pluk til ordre", "Én ordre ad gangen, hele ruten", "Få, store ordrer; enkelt overblik"],
        ["Cluster-pluk", "Flere ordrer med på samme runde (vogn med rum)", "Mange små ordrer"],
        ["Batch-pluk", "Samme vare til mange ordrer plukkes samlet, fordeles bagefter", "Få varenumre der går igen"],
        ["Zone-pluk", "Hver plukker ejer sit område; ordren samles på tværs", "Store lagre; korte gåafstande"],
        ["Wave-pluk", "Pluk frigives i bølger timet efter afgange/ruter", "Faste afgangstider"],
        ["Vare-til-plukker", "Automatik bringer varen til stationen (miniload, shuttle)", "Høj volumen; ergonomi og tæt lager"],
    ], columns=["Strategi", "Sådan virker den", "Egner sig til"])
    st.dataframe(pluk, hide_index=True, width="stretch")
    st.markdown(
        "**Teknologier** (stigende styring): plukliste → pluk-til-label → **pick by "
        "voice** → stregkode → RFID → **pick by light**. Et **WMS** binder det sammen: "
        "gennemsigtigt og nøjagtigt lager, sporbarhed, færre fejlpluk, automatisk "
        "genopfyldning, hurtigere reaktion.\n\n"
        "**Hvad koster en plukkefejl?** Hele kæden: administration af returen → "
        "returtransport → modtagelse → udpakning/kontrol/lagring → kreditnota + ny "
        "plukordre → nyt pluk og pakning → ny transport. Én fejl udløser syv processer — "
        "derfor betaler fejlsikring (voice/light/stregkode) sig hurtigt.\n\n"
        "**KPI'erne:** pålidelighed · fleksibilitet · omkostninger · udnyttelse.")

    st.markdown("#### TPL — tredjepartslogistik i niveauer")
    st.markdown(
        "Fagets pointe: *'der er ingen tredjepart — der er forskellige niveauer af "
        "samarbejde'* med logistikpartneren:\n\n"
        "0. **Basis:** læsning, transport & losning\n"
        "1. **+ opbevaring**\n"
        "2. **+ materiale- & informationsstyring**\n"
        "3. **+ indkøb & EDI** (partneren kobles på systemerne)\n"
        "4. **+ investering, korrektioner & udvikling** (partneren investerer og "
        "udvikler løsningen med dig)\n\n"
        "Jo højere niveau, desto større afhængighed — vurdér det som et make-vs-buy-"
        "spørgsmål med exit-omkostninger, ikke kun en fragtpris.")
    st.page_link("pages/1_Indkøb.py", label="🛒 Make-vs-buy / TCO — regn på outsourcing-beslutningen")


# ===========================================================================
# Køre-hviletid & vægte
# ===========================================================================
elif modul == "Køre-hviletid & vægte":
    st.subheader("Køre-hviletid (EF 561/2006) og danske vægtgrænser")
    st.caption(
        "Reglerne der afgør om en transportplan overhovedet er LOVLIG — brug dem som "
        "tjek i enhver vejtransport-case. Gælder godskøretøjer over 3,5 t tilladt "
        "totalvægt (inkl. trailer) og busser til flere end 9 personer."
    )

    t1, t2 = st.tabs(["⏱️ Køre-hviletid", "⚖️ Vægtgrænser i DK"])

    with t1:
        v1, v2 = st.columns([1, 1])
        with v1:
            st.markdown("#### Køretid")
            st.markdown(
                "- **Daglig:** maks. **9 timer** — må forlænges til **10 timer højst "
                "2 gange om ugen**\n"
                "- **Ugentlig:** maks. **56 timer**\n"
                "- **To uger i træk:** maks. **90 timer** tilsammen\n"
                "- En uge = mandag kl. 00.00 til søndag kl. 24.00")
            st.markdown("#### Pauser")
            st.markdown(
                "- Efter **4½ times kørsel**: pause på mindst **45 min.**\n"
                "- Kan deles i **15 min. + 30 min.** — i DEN rækkefølge, og begge "
                "inden for de 4½ time\n"
                "- En pause er enhver periode på 15 min.+ uden arbejde")
            st.markdown("#### To chauffører / færge")
            st.markdown(
                "- **2 chauffører:** hver mindst **9 timers hvil inden for 30 timer** "
                "(og turen kan køres på ét døgn, jf. Billund-Milano-eksemplet)\n"
                "- **Færge/tog:** det daglige hvil må afbrydes **2 gange, højst 1 time "
                "i alt**, hvis chaufføren har adgang til en seng — hvilet skal så være "
                "mindst 11 timer")
        with v2:
            st.markdown("#### Hviletid")
            st.markdown(
                "- **Dagligt hvil** (inden for hver 24-timers periode): **11 timer** "
                "uafbrudt — eller **9 timer op til 3 gange mellem to ugehvil** "
                "(reduceret), eller delt **12 timer i 2 perioder** hvor den sidste er "
                "mindst 9 timer\n"
                "- **Ugentligt hvil:** senest efter **6 × 24 timer**: **45 timer** "
                "(regulært) eller **24 timer** (reduceret, hver anden uge) — "
                "afkortningen skal kompenseres samlet **inden 3 uger**")
            st.markdown("#### Vejpakken (2020)")
            st.markdown(
                "- Ved **international** transport: **to reducerede ugehvil i træk** "
                "er muligt uden for hjemlandet — mod fuldt + kompenseret hvil hjemme "
                "i uge 3\n"
                "- Chaufføren skal kunne **komme hjem** (hjemsted/bopæl) — som "
                "hovedregel senest hver 4. uge (hver 3. ved to reducerede i træk)\n"
                "- **Nå-hjem-reglen:** køretiden må overskrides med op til **1 time** "
                "for at nå hjem til ugehvil — eller **2 timer**, hvis der holdes 30 "
                "min. pause først. Årsagen SKAL noteres manuelt på takografen")
        st.info("**Kontrol og bøder:** takografen registrerer alt (distance, fart, køre-, "
                "rådigheds- og hviletid) og skiverne gemmes mindst 1 år. Bøderne "
                "beregnes pr. overtrædelse i %, lægges sammen og rundes op til nærmeste "
                "500 kr. — fx koster en daglig køretid på 13 timer (30 % over) 3.000 kr. "
                "til chaufføren og 6.000 kr. til vognmanden. Manipulation med takografen "
                "→ ubetinget frakendelse af førerretten. Ansvaret ligger ikke kun hos "
                "chaufføren: virksomheder og speditører skal planlægge, så reglerne KAN "
                "overholdes.")

    with t2:
        v1, v2 = st.columns([1, 1])
        with v1:
            st.markdown("#### Sololastbiler (tilladt totalvægt)")
            solo = pd.DataFrame([
                ["2 aksler", "18 t"], ["3 aksler", "26 t"],
                ["4 aksler", "32 t"],
            ], columns=["Lastbil", "Maks. totalvægt"])
            st.dataframe(solo, hide_index=True, width="stretch")
            st.markdown("#### Vogntog (bil + kærre/hænger/trailer)")
            tog = pd.DataFrame([
                ["3 aksler", "28 t"], ["4 aksler", "36–38 t"],
                ["5 aksler", "42–44 t"], ["6 aksler", "45–50 t"],
                ["7 aksler", "54–56 t"],
            ], columns=["Vogntog i alt", "Maks. totalvægt"])
            st.dataframe(tog, hide_index=True, width="stretch")
            st.caption("Pr. maj 2018, national kørsel. Intervallet afhænger af "
                       "kombinationen og akselafstandene — fx kræver 56 t på 7 aksler "
                       "mindst 4 m mellem bilens bageste og kærrens/traileren første "
                       "aksel, ellers 54 t. Slå den konkrete kombination op i fagets "
                       "ITD-oversigt.")
        with v2:
            st.markdown("#### Grundregler ved læsning")
            st.markdown(
                "- Aldrig læsse over det køretøjet er **godkendt og registreret** til\n"
                "- **20 %** af bilens faktiske vægt skal hvile på de **styrende** forhjul\n"
                "- **20 %** af vogntogets faktiske vægt skal hvile på de **drivende** hjul\n"
                "- Sættevognens tilladte kongebolttryk skal kunne bære udnyttelsen")
            st.markdown("#### Politiets tolerancegrænser (tiltale ved overlæs)")
            st.markdown(
                "- **Akseltryk:** over **7 %** ELLER mere end **500 kg** over\n"
                "- **Totalvægt** (køretøj > 3.500 kg): over **6 %** ELLER mere end "
                "**2.000 kg** over")
            st.markdown("#### Hurtigt overlæs-tjek")
            o1, o2 = st.columns(2)
            till = o1.number_input("Tilladt totalvægt (kg)", min_value=1000.0,
                                   value=40000.0, step=500.0, key="dist_ov_till")
            fakt = o2.number_input("Faktisk vægt ved kontrol (kg)", min_value=0.0,
                                   value=42000.0, step=100.0, key="dist_ov_fakt")
            over_kg = fakt - till
            over_pct = over_kg / till * 100
            if over_kg <= 0:
                st.success(f"Ingen overskridelse ({num(over_pct, 1)} %).")
            else:
                tiltale = over_pct > 6.0 or over_kg > 2000
                tekst = (f"Overlæs: **{num(over_kg)} kg = {num(over_pct, 1)} %** — "
                         + ("**over tiltalegrænsen** (6 % eller 2.000 kg)."
                            if tiltale else "under tiltalegrænsen, men stadig ulovligt."))
                (st.error if tiltale else st.warning)(tekst)

    st.markdown("---")
    st.markdown("#### Tre regelsæt, der let forveksles med køre-/hviletid")

    with st.expander("⏱️ Arbejdstid — et ANDET regelsæt end køre-/hviletid"):
        st.markdown(
            "Køre-/hviletidsreglerne handler om **kørslen**. Arbejdstidsreglerne "
            "handler om **hele arbejdsdagen** — også læsning, papirarbejde og "
            "ventetid. De gælder samtidig, og man kan overholde det ene og "
            "bryde det andet.\n\n"
            "- **Arbejdstid** er al tid i tjeneste: kørsel, læsning/losning, "
            "kontrol, rengøring og administration.\n"
            "- **Rådighedstid** er ventetid, hvor man på forhånd ved, hvor "
            "længe man venter, og ikke skal stå til rådighed for opgaver — "
            "fx færgeoverfart eller ventetid ved grænse. Den tæller **ikke** "
            "med i arbejdstiden.\n"
            "- **Maksimal ugentlig arbejdstid:** 48 timer i gennemsnit, med "
            "60 timer som absolut loft i en enkelt uge.\n"
            "- **Pause:** der skal holdes pause, inden der er arbejdet 6 timer "
            "i træk.\n"
            "- **Natarbejde** udløser en lavere grænse for den daglige "
            "arbejdstid.")
        st.info("**Fælde:** en chauffør kan sagtens holde sig inden for "
                "køre-/hviletiden og alligevel bryde arbejdstidsreglerne, "
                "fordi læsning og ventetid tæller med dér. Til eksamen: "
                "nævn hvilket regelsæt du argumenterer ud fra.")

    with st.expander("🚛 Særtransport — når godset sprænger rammerne"):
        st.markdown(
            "En **særtransport** er en transport, der overskrider de "
            "almindelige grænser for bredde, længde, højde eller vægt. Så "
            "skifter spillereglerne:\n\n"
            "- **Tilladelse** skal indhentes på forhånd hos myndigheden, og "
            "den er knyttet til en **konkret rute** — ikke til køretøjet.\n"
            "- **Forudsætning** for tilladelse er, at godset ikke kan deles op. "
            "Kan det skilles ad, gives der ikke tilladelse.\n"
            "- **Hastighedsgrænsen falder med vægten** — jo tungere "
            "vogntoget er, desto lavere må der køres.\n"
            "- **Følgebil** kræves over bestemte mål, og både bil og "
            "chauffør skal være godkendt til opgaven.\n"
            "- **Ruten undersøges** for broer, viadukter, master og "
            "rundkørsler, inden turen planlægges — og mange strækninger må "
            "kun befares om natten.")
        st.caption("Projektlast — vindmøllevinger, transformere, anlægsdele — "
                   "ender næsten altid som særtransport på det sidste stykke. "
                   "Se **Luftfragt & frihedsrettigheder** for planlægningen.")

    with st.expander("🌫️ Euro-normer — hvad lastbilen må slippe ud"):
        st.markdown(
            "Fælles europæiske grænser for udstødning fra tunge "
            "dieselkøretøjer. Normen følger køretøjets **registreringsår**, "
            "ikke ejeren, og trinene er blevet skærpet kraftigt over tid — "
            "især for **NOx** (kvælstofilter) og **partikler**.\n\n"
            "Hvorfor det rager en logistiker:\n"
            "- **Miljøzoner** i byerne afviser køretøjer under et bestemt trin. "
            "En gammel bil kan altså være lovlig at eje, men ulovlig at køre "
            "ind i byen med.\n"
            "- **Udbud og kundekrav** stiller ofte minimumskrav til flådens "
            "Euro-norm.\n"
            "- **Vognmandens investeringsbeslutning**: en ældre bil er "
            "billigere at købe, men lukket ude af de opgaver, der betaler bedst.")
        st.info("**Skil dem ad:** Euro-normen begrænser luftforurening "
                "(NOx, partikler) — ikke CO₂. CO₂ afhænger af brændstofforbrug "
                "og energikilde, og hører til under **Grøn godstransport**.")

    st.page_link("pages/8_Jura.py",
                 label="⚖️ Hvem bærer ansvaret for godset undervejs? Se Incoterms/CISG")


# ===========================================================================
# Told & dokumenter
# ===========================================================================
elif modul == "Told & dokumenter":
    st.subheader("Told, transitdokumenter og betaling")
    st.caption(
        "Transportmarkedets papirarbejde: hvornår er varen 'fri', hvilke dokumenter "
        "får den over grænserne, og hvordan sikres betalingen mellem parter der ikke "
        "kender hinanden."
    )

    v1, v2 = st.columns([1, 1])
    with v1:
        st.markdown("#### T1 vs. T2 — varens toldstatus")
        st.markdown(
            "- **T1 (ikke-fællesskabsvarer):** varen er endnu **under toldkontrol** — "
            "formaliteter (fx importafgift) er ikke opfyldt. T1-dokumentet fortæller "
            "tolden i transitlandet, at varen ikke er frigivet: den må transporteres "
            "mellem grænser eller ligge på **toldoplag**, og først ved slutdestinationen "
            "afregnes dokumentet, afgifterne betales, og varen overgår til fri omsætning.\n"
            "- **T2 (fællesskabsvarer):** varen stammer fra EU, er købt i EU — eller er "
            "importeret og **fortoldet til fri omsætning**. Den kan bevæge sig frit.\n\n"
            "**TARIC:** EU's toldtarif. Vejen i praksis: skat.dk → Erhverv → Told → "
            "varekoder → TARIC → hent foranstaltninger (satser, restriktioner, "
            "antidumping) for den konkrete varekode.")
        st.markdown("#### Toldens formål")
        st.markdown(
            "- **Beskyttelsestold:** gøre udenlandske varer dyrere for at skærme egen "
            "produktion (jf. toldkrigene i undervisningen: USA/Kina, stål, Rusland)\n"
            "- **Finanstold:** rent provenu til statskassen\n"
            "- **WTO** sætter rammerne: bundne toldsatser og tvistbilæggelse — et land "
            "kan ikke frit lægge ny told på hvad som helst uden at møde sager eller "
            "gengældelse. Præferenceaftaler (fx EU's) giver lavere satser mellem "
            "parterne.")
    with v2:
        st.markdown("#### TIR og ATA-carnet")
        st.markdown(
            "- **TIR** (Transports Internationaux Routiers): plomberet international "
            "vejtransport — tolden forsegler lastrummet ved afgang, og godset kan "
            "krydse mellemliggende toldområder uden at blive åbnet og fortoldet "
            "undervejs. Garantikæden bag carnetet dækker afgifterne, hvis noget går galt.\n"
            "- **ATA-carnet:** pas til **midlertidig** indførsel — vareprøver, "
            "messeudstyr, professionelt udstyr — ind og ud igen uden told og moms, "
            "mod at varen føres ud inden fristen.")
        st.markdown("#### Betalingsformer ved eksport")
        st.markdown(
            "- **COD** (Cash on Delivery): betaling ved levering — kræver tillid til, "
            "at køber betaler, når varen står der.\n"
            "- **CAD** (Cash Against Documents): køber får først **dokumenterne** "
            "(og dermed varen ud af havnen), når der er betalt via bankerne.\n"
            "- **Remburs** (Letter of Credit): købers bank **garanterer** betalingen, "
            "mod at sælger fremlægger nøjagtigt de aftalte dokumenter (konnossement, "
            "faktura, forsikring) inden fristen. Bankerne kontrollerer KUN dokumenter — "
            "derfor: skriv dokumentkravene præcist, og levér dem fejlfrit. Sælgers "
            "stærkeste sikkerhed ved nye eller usikre modparter og markeder.\n"
            "- **IOU** (gældsbevis): skriftlig anerkendelse af gæld — ingen "
            "banksikkerhed, kun bevis.\n\n"
            "**Transportaftalen:** husk fagets tjekliste (International Transport "
            "Planning s. 23) for hvad aftalen kan indeholde — ydelse, tider, ansvar, "
            "rater, reguleringer, dokumentkrav.")

    st.page_link("pages/8_Jura.py",
                 label="⚖️ Incoterms + CISG — leveringsbetingelser og misligholdelse")


# ===========================================================================
# Volumenvægt & fragtgrundlag
# ===========================================================================
elif modul == "Volumenvægt & fragtgrundlag":
    st.subheader("Volumenvægt — hvad betaler du egentlig fragt for?")
    st.caption(
        "Fragtføreren sælger to ting på én gang: **løfteevne** og **plads**. "
        "Derfor afregnes en sending efter det største af faktisk vægt og "
        "volumenvægt. Let, voluminøst gods betaler for pladsen — også selvom "
        "det næsten intet vejer.")

    vv1, vv2 = st.columns([1, 1])
    with vv1:
        st.markdown("**Målene pr. kolli**")
        v_l = st.number_input("Længde (cm)", 1.0, 2000.0, 120.0, 1.0, key="vv_l")
        v_b = st.number_input("Bredde (cm)", 1.0, 2000.0, 80.0, 1.0, key="vv_b")
        v_h = st.number_input("Højde (cm)", 1.0, 2000.0, 100.0, 1.0, key="vv_h")
        v_kg = st.number_input("Vægt pr. kolli (kg)", 0.1, 50000.0, 90.0, 0.5,
                               key="vv_kg")
        v_n = st.number_input("Antal kolli", 1, 5000, 1, 1, key="vv_n")
    with vv2:
        st.markdown("**Transportform**")
        v_form = st.selectbox("Omregningsfaktor", list(ds.OMREGNING.keys()),
                              key="vv_form",
                              help="Hvor mange kg ét kubikmeter 'vejer' i "
                                   "fragtberegningen. Flyet har løfteproblemet, "
                                   "skibet har pladsproblemet — derfor er "
                                   "faktorerne så forskellige.")
        v_faktor = st.number_input(
            "kg pr. m³", 1.0, 2000.0, float(ds.OMREGNING[v_form]), 1.0,
            key="vv_faktor",
            help="Rediger frit, hvis din case oplyser en anden faktor.")

    r_vv = ds.volumenvaegt(v_l, v_b, v_h, v_kg, int(v_n), v_faktor)
    if "fejl" in r_vv:
        st.error(r_vv["fejl"])
    else:
        k1, k2, k3 = st.columns(3)
        k1.metric("Rumfang", f"{num(r_vv['m3'], 3)} m³")
        k2.metric("Faktisk vægt", f"{num(r_vv['faktisk_vaegt'], 1)} kg")
        k3.metric("Volumenvægt", f"{num(r_vv['volumenvaegt'], 1)} kg")

        st.metric(f"Fragtgrundlag — betales efter {r_vv['betales_efter']}",
                  f"{num(r_vv['fragtgrundlag'], 1)} kg",
                  delta=f"{num(r_vv['overskydende_kg'], 1)} kg mere end det andet mål")

        st.markdown(
            f"**Mellemregning:** {num(v_l, 0)} × {num(v_b, 0)} × {num(v_h, 0)} cm "
            f"= {num(r_vv['m3_pr_kolli'], 4)} m³ pr. kolli × {int(v_n)} stk. "
            f"= **{num(r_vv['m3'], 3)} m³**.  \n"
            f"Volumenvægt = {num(r_vv['m3'], 3)} m³ × {num(v_faktor, 0)} kg/m³ "
            f"= **{num(r_vv['volumenvaegt'], 1)} kg**.  \n"
            f"Fragtgrundlag = største af {num(r_vv['faktisk_vaegt'], 1)} kg og "
            f"{num(r_vv['volumenvaegt'], 1)} kg = **{num(r_vv['fragtgrundlag'], 1)} kg**.")

        st.caption(f"Godsets densitet er {num(r_vv['densitet_kg_pr_m3'], 1)} kg/m³. "
                   f"Ligger den under omregningsfaktoren ({num(v_faktor, 0)} kg/m³), "
                   "betaler du for luft.")

    st.info(
        "**Til forsvaret:** vend den om. Skal du *rådgive*, er spørgsmålet ikke "
        "«hvad koster det?», men «kan vi ændre densiteten?» — bedre pakning, "
        "adskilt forsendelse eller et andet kollimål kan flytte grundlaget fra "
        "volumen til vægt. Det er en billigere besparelse end at forhandle raten.")
    st.caption("Søfragtens 1 m³ = 1.000 kg er den klassiske **measureton** "
               "(w/m — weight or measurement).")


# ===========================================================================
# Luftfragt & frihedsrettigheder
# ===========================================================================
elif modul == "Luftfragt & frihedsrettigheder":
    st.subheader("Luftfartens frihedsrettigheder")
    st.caption(
        "Et fly må ikke bare flyve, hvorhen det vil. Retten til at krydse, "
        "lande og laste i et andet land forhandles mellem stater, og de ni "
        "friheder er trappen fra «flyve henover» til «flyve frit indenrigs i "
        "et fremmed land». De fire første er officielle; resten bruges i "
        "praksis, men er ikke formelt anerkendte på samme måde.")

    # Markdown frem for st.dataframe: forklaringerne er hele sætninger, og et
    # datagrid klipper dem af ved kolonnekanten i stedet for at ombryde.
    st.markdown(
        "| # | Status | Kort sagt | Hvad den giver ret til |\n"
        "|---|---|---|---|\n"
        "| **1** | Officiel | Overflyvning | Flyve gennem et andet lands "
        "luftrum uden at lande. |\n"
        "| **2** | Officiel | Teknisk landing | Lande i et andet land for at "
        "tanke eller reparere — men ikke for at laste. |\n"
        "| **3** | Officiel | Sætte af ude | Flyve passagerer og gods **fra** "
        "sit hjemland **til** et andet land. |\n"
        "| **4** | Officiel | Tage med hjem | Flyve passagerer og gods **fra** "
        "et andet land **til** sit hjemland. |\n"
        "| **5** | Officiel | Mellemlanding med last | På vej mellem to andre "
        "lande må man laste og losse undervejs. |\n"
        "| **6** | Uofficiel | Over eget hub | Flyve mellem to fremmede lande "
        "med mellemlanding i sit eget — 3. og 4. frihed sat sammen. |\n"
        "| **7** | Uofficiel | Rute uden hjemland | Drive en rute, der slet "
        "ikke berører hjemlandet. |\n"
        "| **8** | Uofficiel | Cabotage i forlængelse | Flyve indenrigs i et "
        "fremmed land som forlængelse af en rute hjemmefra. |\n"
        "| **9** | Uofficiel | Ren cabotage | Flyve rent indenrigs i et "
        "fremmed land uden forbindelse til hjemlandet. |\n")

    st.info(
        "**Den der oftest spørges til:** 6. frihed. Den står ikke i "
        "konventionen, men er i praksis hele forretningsmodellen bag de store "
        "omstignings-lufthavne — man kobler 4. og 3. frihed og flyver dermed "
        "mellem to lande, man ellers ikke måtte beflyve direkte.")

    st.markdown("#### Projektlast — når godset ikke passer i noget")
    st.markdown(
        "Projektlast er sendinger, der er for tunge, for lange eller for "
        "uhåndterlige til almindelig stykgods: anlægsdele, transformere, "
        "vindmøllevinger. Det ændrer hele planlægningen:\n\n"
        "- **Ruten planlægges baglæns** fra modtagerens adgangsforhold — ikke "
        "fremad fra fabrikken. Kan svinget ikke tages, er ruten ligegyldig.\n"
        "- **Det sidste stykke går altid på vej.** Uanset om hovedturen er sø "
        "eller bane, ender godset på et blokvogntog — og dermed i "
        "særtransport-reglerne (tilladelse, følgebil, hastighedsgrænse).\n"
        "- **Forundersøgelse** af broer, viadukter, master og rundkørsler er "
        "en del af opgaven, ikke en formalitet.\n"
        "- **Tidsvinduer**: mange strækninger må kun befares om natten.")
    st.caption("Reglerne for selve særtransporten ligger under "
               "**Køre-hviletid & vægte**.")


# ===========================================================================
# Grøn godstransport
# ===========================================================================
elif modul == "Grøn godstransport":
    st.subheader("Grøn godstransport — fagets tal og virkemidler")
    st.caption(
        "Fra 'Decarbonising the Movement of Freight': hvor stor er godstransportens "
        "klimabelastning, hvor er den på vej hen, og hvilke håndtag findes. Tallene "
        "her er deckets egne — brug dem som belæg i opgaver."
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("Logistiks andel af global CO2", "10–11 %",
              help="Godstransport ca. 8 % + lagre og terminaler 1–2 %.")
    m2.metric("Basisfremskrivning mod 2050", "+118 %",
              help="Forventet vækst i CO2 fra godstransport globalt uden nye tiltag.")
    m3.metric("Vejgodsets CO2-intensitet", "24 → 9 g/tonkm",
              help="Forventet forbedring pr. tonkm mod 2050 — men den opvejes i vidt "
                   "omfang af 3,3× vækst i transportarbejdet, så udledningen stiger "
                   "alligevel ca. 21 %.")

    st.markdown(
        "- **Rammen:** 77 lande har forpligtet sig til net-nul senest 2050. Det "
        "resterende CO2-budget for 1,5° (67 % sandsynlighed) var ca. **420 Gton** "
        "(jan. 2018) mod udledninger på ca. **42 Gton/år** — dvs. opbrugt på ~10 år i "
        "samme tempo. Danmark: 70 %-reduktionsmålet, som transportsektoren skal "
        "bidrage til.\n"
        "- **Effektivitets-paradokset:** intensiteten pr. tonkm falder, men "
        "transportarbejdet vokser hurtigere — derfor er effektivisering alene ikke nok "
        "(+21 % trods 24→9 g/tonkm).\n"
        "- **Søfart:** IMO-målene (50 % reduktion 2008→2050; 70 % pr. transportarbejde). "
        "Stærkeste enkeltgreb: **slow steaming — 10 % lavere fart giver ca. 23 % mindre "
        "brændstof**.\n"
        "- **Scenariet for CO2-fri godstransport** i decket bygger på: elektrificér "
        "de logistiske aktiviteter + sørg for nok **CO2-fri elektricitet** + "
        "CO2-opsamling (lagring/anvendelse) for resten — og **CO2-budgettering** "
        "indarbejdet i logistikstrategien.\n"
        "- **Logistikerens egne håndtag** (før teknologien): flyt gods til billigere "
        "CO2-former (modal shift, jf. Transportformsvalg), udnyt kapaciteten (fyldte "
        "læs, færre tomkørsler), kortere/planlagte ruter, og design af netværket så "
        "transportarbejdet falder (jf. tyngdepunktsmetoden)."
    )
    st.info("**Eksamens-kobling:** grøn omstilling er sjældent sit eget spørgsmål — "
            "den er et VURDERINGSKRITERIE oveni transportvalg, netværksdesign og "
            "lagerstruktur. Nævn CO2-konsekvensen af din anbefaling, og brug deckets "
            "tal som belæg.")
    st.page_link("pages/9_Distribution.py", label="🚚 Transportformsvalg — modal shift starter dér")
