"""Kommunikation — interessentanalyse + forhandling.

Blødt fag: interaktiv power-interest-grid, et forhandlingsark (bargaining sheet
med målpunkt/modstandspunkt pr. emne), en ZOPA-visualizer og et forhandlings-
bibliotek (BAPTA, ZOPA, principiel forhandling, kulturelle stile).
Notation matcher brugerens eget bargaining-ark (MDO/LDO) og standard forhandlingsteori.
"""
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_theme import (  # noqa: E402
    inject_css, style_fig, C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_MUTED,
)

st.set_page_config(page_title="Kommunikation", page_icon="💬", layout="wide")
inject_css()


def num(x, dec=0):
    if x is None:
        return "—"
    s = f"{x:,.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


st.title("💬 Kommunikation")
st.caption("Interessentanalyse og forhandling. Placér interessenter efter magt og interesse, "
           "forbered en forhandling med målpunkter, og slå forhandlingsbegreberne op.")

tab_int, tab_forh, tab_bib = st.tabs([
    "🎯 Interessentanalyse", "🤝 Forhandlingsark + ZOPA", "📚 Forhandlingsbibliotek",
])


# ===========================================================================
# INTERESSENTANALYSE (power-interest grid)
# ===========================================================================
with tab_int:
    st.subheader("Interessentanalyse (magt-interesse-model)")
    st.caption("Placér hver interessent efter hvor meget **magt** de har (kan de påvirke "
               "projektet?) og hvor stor **interesse** de har (bliver de berørt?). Hver firkant "
               "har sin egen håndteringsstrategi.")

    c1, c2 = st.columns([1, 2])
    with c1:
        default_i = pd.DataFrame({
            "Interessent": ["Topledelse", "Projektleder", "Slutbrugere", "Leverandør", "Naboafdeling"],
            "Magt": [5, 5, 2, 3, 2],
            "Interesse": [3, 5, 5, 4, 2],
        })
        st.caption("Giv hver interessent en score fra 1 (lav) til 5 (høj) på magt og interesse.")
        idf = st.data_editor(default_i, num_rows="dynamic", hide_index=True,
                             use_container_width=True, key="int_data", height=240)
    with c2:
        idf = idf.copy()
        idf["Magt"] = pd.to_numeric(idf["Magt"], errors="coerce")
        idf["Interesse"] = pd.to_numeric(idf["Interesse"], errors="coerce")
        idf = idf.dropna(subset=["Magt", "Interesse"])
        fig = go.Figure()
        fig.add_shape(type="rect", x0=0.5, y0=3, x1=3, y1=5.5, fillcolor="rgba(245,158,11,0.08)", line_width=0)
        fig.add_shape(type="rect", x0=3, y0=3, x1=5.5, y1=5.5, fillcolor="rgba(239,68,68,0.10)", line_width=0)
        fig.add_shape(type="rect", x0=0.5, y0=0.5, x1=3, y1=3, fillcolor="rgba(100,116,139,0.10)", line_width=0)
        fig.add_shape(type="rect", x0=3, y0=0.5, x1=5.5, y1=3, fillcolor="rgba(16,185,129,0.08)", line_width=0)
        for x, y, t in [(1.75, 5.25, "Hold tilfreds"), (4.25, 5.25, "Samarbejd tæt"),
                        (1.75, 0.75, "Overvåg"), (4.25, 0.75, "Hold informeret")]:
            fig.add_annotation(x=x, y=y, text=t, showarrow=False, font=dict(color="#94a3b8", size=13))
        fig.add_trace(go.Scatter(x=idf["Interesse"], y=idf["Magt"], mode="markers+text",
                                 text=idf["Interessent"], textposition="top center",
                                 marker=dict(color=C_TOTAL, size=13)))
        fig.add_vline(x=3, line_dash="dot", line_color=C_MUTED)
        fig.add_hline(y=3, line_dash="dot", line_color=C_MUTED)
        fig.update_layout(xaxis=dict(title="Interesse", range=[0.5, 5.5]),
                          yaxis=dict(title="Magt", range=[0.5, 5.5]),
                          height=430, margin=dict(t=20, b=10), showlegend=False)
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du den: jo længere mod højre, jo mere berørt er interessenten; "
                   "jo højere op, jo mere magt har de. Firkanten en interessent lander i, fortæller "
                   "hvordan du bør håndtere vedkommende.")

    with st.expander("Strategi for hver firkant", expanded=True):
        st.markdown(
            "- **Samarbejd tæt** (høj magt, høj interesse): de vigtigste. Inddrag dem aktivt, "
            "involvér dem i beslutninger, og hold tæt dialog.\n"
            "- **Hold tilfreds** (høj magt, lav interesse): magtfulde, men ikke så engagerede. "
            "Hold dem tilfredse og orienteret om det vigtige, men undgå at overdænge dem.\n"
            "- **Hold informeret** (lav magt, høj interesse): engagerede uden megen magt. Informér "
            "dem løbende; de kan blive gode ambassadører.\n"
            "- **Overvåg** (lav magt, lav interesse): minimal indsats. Hold øje, men brug ikke "
            "mange ressourcer."
        )


# ===========================================================================
# FORHANDLINGSARK + ZOPA
# ===========================================================================
with tab_forh:
    st.subheader("Forhandlingsark")
    st.caption("Forbered forhandlingen emne for emne. **Målpunkt (MDO)** er det bedste realistiske "
               "resultat du går efter; **modstandspunkt (LDO)** er din smertegrænse, hvor du hellere "
               "går fra forhandlingen. Notér modpartens åbning og hvor vigtigt emnet er.")

    default_b = pd.DataFrame({
        "Emne": ["Pris", "Kreditdage", "Leveringspræcision", "Kvalitet", "Volumen/kontrakt"],
        "Modpartens åbning": ["+10 %", "30 dage", "ingen aftale", "ingen garanti", "—"],
        "Målpunkt (MDO)": ["0 til 2 %", "behold 60 dage", "95 % + bod/bonus", "specifikation + bod", "2-årig aftale"],
        "Modstandspunkt (LDO)": ["maks +4-5 %", "min. 45 dage", "90 % + plan", "skriftlig plan", "kan byttes væk"],
        "Prioritet": ["Høj", "Høj", "Høj", "Middel", "Byttechip"],
    })
    st.data_editor(default_b, num_rows="dynamic", hide_index=True, use_container_width=True,
                   key="forh_data",
                   column_config={"Prioritet": st.column_config.SelectboxColumn(
                       "Prioritet", options=["Høj", "Middel", "Lav", "Byttechip"])})
    st.caption("Tip: emner med lav værdi for dig men høj for modparten er gode **byttechips** "
               "(du giver dem væk for at vinde på dine høj-prioritets-emner).")

    st.divider()
    st.subheader("ZOPA — er der en aftale at lave?")
    st.caption("ZOPA (zonen for mulig enighed) er overlappet mellem hvad køber højst vil betale "
               "og hvad sælger mindst vil acceptere. Er der intet overlap, findes der ingen aftale.")
    c = st.columns(2)
    saelger_min = c[0].number_input("Sælgers mindstepris (sælgers modstandspunkt)", value=100.0,
                                    step=5.0, key="zopa_smin",
                                    help="Det laveste sælger vil gå ned til. Under dette går sælger fra.")
    koeber_max = c[1].number_input("Købers maxpris (købers modstandspunkt)", value=120.0,
                                   step=5.0, key="zopa_kmax",
                                   help="Det højeste køber vil betale. Over dette går køber fra.")

    zopa = koeber_max >= saelger_min
    lav = min(saelger_min, koeber_max)
    hoej = max(saelger_min, koeber_max)
    fig = go.Figure()
    span = max(hoej - lav, 1)
    fig.add_trace(go.Scatter(x=[saelger_min], y=[1], mode="markers+text", text=["Sælgers min"],
                             textposition="bottom center", marker=dict(color=C_OPT, size=14), name="Sælger"))
    fig.add_trace(go.Scatter(x=[koeber_max], y=[1], mode="markers+text", text=["Købers max"],
                             textposition="top center", marker=dict(color=C_TOTAL, size=14), name="Køber"))
    if zopa:
        fig.add_shape(type="rect", x0=saelger_min, y0=0.85, x1=koeber_max, y1=1.15,
                      fillcolor="rgba(16,185,129,0.30)", line_width=0)
    fig.update_layout(height=220, margin=dict(t=20, b=10), showlegend=False,
                      yaxis=dict(visible=False, range=[0.5, 1.5]), xaxis_title="Pris")
    st.plotly_chart(style_fig(fig), use_container_width=True)
    if zopa:
        st.success(f"Der ER en ZOPA: enighed er mulig mellem {num(saelger_min,0)} og "
                   f"{num(koeber_max,0)}. Den endelige pris afgøres af forhandlingsstyrke og BAPTA.",
                   icon="✅")
    else:
        st.error(f"Ingen ZOPA: sælger vil mindst have {num(saelger_min,0)}, men køber vil højst "
                 f"give {num(koeber_max,0)}. Aftalen kræver at en part flytter sit modstandspunkt, "
                 "eller at I finder andre emner at bytte med.", icon="🚫")


# ===========================================================================
# FORHANDLINGSBIBLIOTEK
# ===========================================================================
with tab_bib:
    st.subheader("Forhandlingsbibliotek")
    st.caption("Slå de centrale forhandlingsbegreber op.")

    begreber = [
        ("BAPTA — dit bedste alternativ",
         "BAPTA er dit **bedste alternativ til en forhandlet aftale** (det du gør, hvis "
         "forhandlingen bryder sammen, fx en anden leverandør). Jo stærkere BAPTA, jo mere kan du "
         "forlange, fordi du roligt kan gå fra bordet. Din BAPTA bestemmer dit modstandspunkt.",
         "Kend din egen BAPTA før du forhandler, og prøv at vurdere modpartens. Forbedr din BAPTA "
         "inden du går til bordet (fx ved at finde en alternativ leverandør)."),
        ("Målpunkt (MDO) og modstandspunkt (LDO)",
         "**Målpunkt (MDO)** er det bedste realistiske resultat du sigter efter. "
         "**Modstandspunkt (LDO)** er din smertegrænse, hvor du hellere går fra aftalen. "
         "Du forhandler i feltet mellem din åbning og dit modstandspunkt.",
         "Sæt et ambitiøst men realistisk målpunkt, og vær disciplineret ved dit modstandspunkt. "
         "Notér begge for hvert emne på forhandlingsarket."),
        ("ZOPA — zonen for mulig enighed",
         "ZOPA er **overlappet** mellem parternes modstandspunkter, altså det prisinterval hvor "
         "begge hellere vil sige ja end gå fra aftalen. Findes der intet overlap, er der ingen "
         "ZOPA, og en aftale kræver at nogen flytter sig.",
         "Brug ZOPA til at vurdere om en aftale overhovedet er mulig, og hvor meget der er at "
         "forhandle om."),
        ("Principiel forhandling (Harvard-metoden)",
         "En win-win-tilgang med fire principper: 1) **adskil personen fra problemet**, 2) **fokusér "
         "på interesser, ikke positioner** (hvorfor vil de det?), 3) **find løsninger med fælles "
         "gevinst**, og 4) **brug objektive kriterier** (markedspris, standarder) til at afgøre "
         "uenigheder.",
         "Brug den når relationen skal bevares, og når der er plads til at udvide kagen i stedet "
         "for kun at slås om den."),
        ("Distributiv vs. integrativ forhandling",
         "**Distributiv** forhandling fordeler en fast kage (det den ene vinder, taber den anden, "
         "fx ren pris). **Integrativ** forhandling udvider kagen ved at bytte på tværs af flere "
         "emner, så begge får mest muligt af det de værdsætter mest.",
         "Gør forhandlingen integrativ ved at lægge flere emner på bordet, så du kan bytte "
         "lav-værdi-emner væk for høj-værdi-emner (byttechips)."),
        ("Kulturelle forhandlingsstile",
         "Forhandlingsstil varierer mellem kulturer. Brug **Hofstedes dimensioner**: høj "
         "magtdistance betyder ofte at beslutninger kun tages af toppen; høj usikkerhedsundvigelse "
         "betyder vægt på detaljerede kontrakter; nogle kulturer er relations-orienterede (byg "
         "tillid først), andre opgave-/kontraktorienterede (kom til sagen).",
         "Tilpas tempo, formalitet og forberedelse til modpartens kultur, og forvent at "
         "beslutningsveje og tidsopfattelse kan være anderledes."),
    ]
    soeg = st.text_input("Søg begreb (fx 'bapta', 'zopa', 'harvard', 'kultur')", key="forh_soeg").lower().strip()
    vist = 0
    for navn, hvad, hvornaar in begreber:
        if soeg and soeg not in navn.lower() and soeg not in hvad.lower():
            continue
        vist += 1
        with st.expander(navn, expanded=bool(soeg)):
            st.markdown(f"**Hvad er det?** {hvad}")
            st.markdown(f"**Sådan bruger du det:** {hvornaar}")
    if soeg and vist == 0:
        st.info("Ingen begreber matchede søgningen.")

st.divider()
st.caption("Forhandlingsdelen bygger på standard forhandlingsteori (Harvard-metoden, BATNA "
           "kaldet BAPTA som i dit materiale) samt dit eget bargaining-ark (målpunkt/modstandspunkt). "
           "Sig til, hvis din undervisning bruger en anden notation, så retter jeg den til.")
