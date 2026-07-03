"""Kommunikation — kommunikationsmodel, kultur, interessenter + forhandling.

Blødt fag: kommunikationsmodellen (afsender → budskab/kanal → modtager med
støj og feedback), Gestelands fire kulturdimensioner med en sammenlign-to-
kulturer-widget (forudfyldt med brugerens egen Tyrkiet-profil fra SPM 16),
interaktiv power-interest-grid, et forhandlingsark (bargaining sheet med
MDO/LDO pr. emne + numerisk ZOPA og tekst-eksport) og et forhandlings-
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
    inject_css, vis_fig, C_TOTAL, C_HOLD, C_OPT, C_MUTED,
)

st.set_page_config(page_title="Kommunikation", page_icon="💬", layout="wide")
inject_css()


def num(x, dec=0):
    """Dansk talformat — viser '—' for tomme/ugyldige tal (NaN/inf)."""
    if x is None:
        return "—"
    try:
        if not np.isfinite(x):
            return "—"
    except TypeError:
        return "—"
    s = f"{x:,.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


st.title("💬 Kommunikation")
st.caption("Kommunikationsmodellen, kulturforskelle (Gesteland), interessentanalyse og "
           "forhandling. Placér interessenter efter magt og interesse, forbered en "
           "forhandling med MDO/LDO pr. emne, og slå begreberne op.")

tab_int, tab_model, tab_gest, tab_forh, tab_bib = st.tabs([
    "🎯 Interessentanalyse", "📡 Kommunikationsmodellen", "🌍 Gesteland (kultur)",
    "🤝 Forhandlingsark + ZOPA", "📚 Forhandlingsbibliotek",
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
                             width="stretch", key="int_data", height=240)
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
        # Lille fast forskydning + skiftende tekstplacering når flere
        # interessenter deler samme punkt, så navnene ikke skriver oveni hinanden
        offs = [(0.0, "top center"), (0.14, "bottom center"), (-0.14, "middle right"),
                (0.28, "middle left"), (-0.28, "top center")]
        xs, ys, pos = [], [], []
        taeller = {}
        for _, r in idf.iterrows():
            noegle = (r["Interesse"], r["Magt"])
            k = taeller.get(noegle, 0)
            taeller[noegle] = k + 1
            dx, tp = offs[k % len(offs)]
            xs.append(r["Interesse"] + dx)
            ys.append(r["Magt"])
            pos.append(tp)
        fig.add_trace(go.Scatter(x=xs, y=ys, mode="markers+text",
                                 text=idf["Interessent"], textposition=pos,
                                 marker=dict(color=C_TOTAL, size=13)))
        fig.add_vline(x=3, line_dash="dot", line_color=C_MUTED)
        fig.add_hline(y=3, line_dash="dot", line_color=C_MUTED)
        fig.update_layout(xaxis=dict(title="Interesse", range=[0.5, 5.5]),
                          yaxis=dict(title="Magt", range=[0.5, 5.5]),
                          height=430, margin=dict(t=20, b=10), showlegend=False)
        vis_fig(fig)
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
# KOMMUNIKATIONSMODELLEN (afsender → budskab/kanal → modtager, støj + feedback)
# ===========================================================================
with tab_model:
    st.subheader("Kommunikationsmodellen")
    st.caption("Afsenderen pakker sit budskab ind (indkodning), sender det gennem en kanal, og "
               "modtageren pakker det ud (afkodning). Undervejs kan **støj** forvride budskabet — "
               "og uden **feedback** opdager afsenderen aldrig, om det er landet rigtigt.")

    fig = go.Figure()
    BOKSE = [(0.2, 1.7, "Afsender"), (2.1, 3.6, "Indkodning"),
             (4.0, 6.0, "Budskab<br>+ kanal"), (6.4, 7.9, "Afkodning"),
             (8.3, 9.8, "Modtager")]
    for x0, x1, navn in BOKSE:
        fig.add_shape(type="rect", x0=x0, y0=1.45, x1=x1, y1=2.55,
                      line=dict(color=C_TOTAL, width=2),
                      fillcolor="rgba(59,130,246,0.10)")
        fig.add_annotation(x=(x0 + x1) / 2, y=2.0, text=f"<b>{navn}</b>",
                           showarrow=False, font=dict(color="#e2e8f0", size=13))
    # Pile mellem boksene (venstre → højre)
    for fra, til in [(1.7, 2.1), (3.6, 4.0), (6.0, 6.4), (7.9, 8.3)]:
        fig.add_annotation(x=til, y=2.0, ax=fra, ay=2.0, xref="x", yref="y",
                           axref="x", ayref="y", text="", showarrow=True,
                           arrowhead=3, arrowwidth=2, arrowcolor=C_MUTED)
    # Støj rammer budskabet/kanalen ovenfra
    fig.add_annotation(x=5.0, y=3.55, text="⚡ <b>Støj</b>", showarrow=False,
                       font=dict(color=C_OPT, size=14))
    fig.add_annotation(x=5.0, y=2.6, ax=5.0, ay=3.35, xref="x", yref="y",
                       axref="x", ayref="y", text="", showarrow=True,
                       arrowhead=3, arrowwidth=2, arrowcolor=C_OPT)
    # Feedback løber nedenunder fra modtager tilbage til afsender
    fig.add_shape(type="line", x0=9.05, y0=1.45, x1=9.05, y1=0.8,
                  line=dict(color=C_HOLD, width=2))
    fig.add_annotation(x=0.95, y=0.8, ax=9.05, ay=0.8, xref="x", yref="y",
                       axref="x", ayref="y", text="", showarrow=True,
                       arrowhead=3, arrowwidth=2, arrowcolor=C_HOLD)
    fig.add_shape(type="line", x0=0.95, y0=0.8, x1=0.95, y1=1.45,
                  line=dict(color=C_HOLD, width=2))
    fig.add_annotation(x=5.0, y=0.55, text="Feedback — svaret tilbage",
                       showarrow=False, font=dict(color=C_HOLD, size=13))
    fig.update_layout(height=300, margin=dict(t=10, b=10),
                      xaxis=dict(visible=False, range=[-0.2, 10.2]),
                      yaxis=dict(visible=False, range=[0.1, 4.0]),
                      showlegend=False)
    vis_fig(fig)

    MODEL_OPSLAG = [
        ("Modellens led — fra afsender til modtager",
         "**Afsenderen** har et budskab og **indkoder** det: vælger ord, tal, tone og sprog. "
         "Budskabet sendes gennem en **kanal** (møde, telefon, mail, rapport). **Modtageren "
         "afkoder** det — og forstår ikke nødvendigvis det samme, som afsenderen mente. "
         "**Feedback** er svaret tilbage, der viser om budskabet er landet rigtigt.",
         "Når kommunikation fejler i casen, så gå kæden igennem led for led: var budskabet "
         "uklart pakket ind (indkodning)? Var kanalen forkert? Eller blev det afkodet "
         "anderledes end ment? Uden feedback opdager afsenderen aldrig fejlen."),
        ("Støj — det der forvrider budskabet",
         "Alt det, der forstyrrer budskabet på vejen: **fysisk støj** (larm, dårlig "
         "forbindelse), **sprogstøj** (fagudtryk eller et fremmedsprog modtageren ikke "
         "forstår — som den italienske PDF med salgsbetingelser, der bare blev lagt væk) og "
         "**psykologisk støj** (travlhed, følelser, forudindtagethed).",
         "Peg på den KONKRETE støjkilde i casen og på, hvordan den fjernes: oversæt, forenkl "
         "sproget, vælg et roligere tidspunkt — eller skift kanal."),
        ("Valg af kanal — rig eller fattig",
         "En **rig kanal** (møde ansigt til ansigt) bærer tonefald, kropssprog og øjeblikkelig "
         "feedback — den er bedst til komplekse eller følsomme budskaber. En **fattig kanal** "
         "(mail, rapport, opslag) bærer kun teksten, men er hurtig og giver dokumentation.",
         "Match kanalens rigdom med budskabets kompleksitet: svære budskaber på mail går galt, "
         "og simple beskeder i lange møder spilder tid. I forhandling: byg relationen i den "
         "rige kanal (mødet), og bekræft aftalerne i den fattige (skriftligt)."),
        ("Envejs- eller tovejskommunikation",
         "**Envejs**: budskabet sendes uden mulighed for svar (opslag, ordre, massemail) — "
         "hurtigt, men afsenderen ved ikke om det er forstået. **Tovejs**: modtageren kan "
         "spørge og svare — langsommere, men langt sikrere.",
         "Vælg tovejs når budskabet er vigtigt, nyt eller kan misforstås. Og husk: møder uden "
         "referat er reelt envejs — budskabet forsvinder, og ingen kan holdes fast på det."),
        ("Feedback der ignoreres",
         "Kommunikation kan være tovejs på papiret men envejs i praksis: medarbejderne siger "
         "fra ('vi løber stærkere og stærkere, men ingen lytter'), men ledelsen handler ikke "
         "på det. Feedbacken sendes — men den afkodes aldrig.",
         "Et stærkt eksamenspoint: find stedet i casen hvor feedback faktisk BLEV givet, og "
         "vis at problemet ikke er manglende kommunikation, men at der ikke handles på den. "
         "Koblingen til motivation (Herzberg: manglende anerkendelse) giver ekstra point."),
    ]
    for navn, hvad, brug in MODEL_OPSLAG:
        with st.expander(navn):
            st.markdown(f"**Hvad er det?** {hvad}")
            st.markdown(f"**Sådan bruger du det:** {brug}")

    st.caption("Eksemplerne er dine egne cases: den italienske PDF ingen læste (sprogstøj), "
               "møder uden referat (budskabet forsvinder), og 'ingen lytter' (feedback uden "
               "virkning). Og i 🌍 Gesteland-fanen ser du afkodning i praksis: et tyrkisk "
               "'nej' siges sjældent direkte — det skal læses mellem linjerne.")


# ===========================================================================
# GESTELAND — 4 kulturdimensioner + sammenlign to kulturer
# ===========================================================================
with tab_gest:
    st.subheader("Gestelands kulturdimensioner")
    st.caption("En model der beskriver kulturforskelle i forretning på fire dimensioner: er "
               "folk mest til **relationer eller handler**? **Formelle eller afslappede**? "
               "Holder de **tiden stramt eller løst**? **Rolige eller temperamentsfulde**? "
               "Til eksamen skal du bruge mindst TO kulturteorier — Gesteland her og "
               "Hofstede (under 🧭 Organisation).")

    # (dimension, forklaring, [pol A, pol B], råd når parterne er forskellige)
    GESTELAND = [
        ("Relations-fokus ↔ deal-fokus",
         "Relations-fokuserede kulturer vil kende dig, før de handler med dig — "
         "deal-fokuserede går direkte til sagen og lader kontrakten bære relationen.",
         ["Relations-fokus", "Deal-fokus"],
         "Byg relationen FØR forretningen: brug tid på small talk og fælles måltider, og "
         "send ikke bare en kontrakt. Et 'nej' siges sjældent direkte i relations-kulturer — "
         "læs mellem linjerne og bevar harmonien."),
        ("Formel ↔ uformel",
         "Formelle kulturer vægter titler, hierarki og etikette — uformelle kulturer er "
         "hurtigt på fornavn og flad i omgangstonen.",
         ["Formel", "Uformel"],
         "Respektér titler og hierarki: henvend dig til den rigtige (øverste) "
         "beslutningstager, og vær mere høflig og formel, end du plejer derhjemme."),
        ("Stram tid ↔ flydende tid",
         "I stramme (monokrone) tidskulturer ER mødetidspunktet aftalen — i flydende "
         "tidskulturer er relationen vigtigere end uret, og planer skrider uden drama.",
         ["Stram tid (monokron)", "Flydende tid"],
         "Vær tålmodig: læg buffer i planen og bliv ikke fornærmet over ventetid — men få "
         "selv deadlines og aftaler bekræftet skriftligt."),
        ("Ekspressiv ↔ reserveret",
         "Ekspressive kulturer taler højt, afbryder og bruger store fagter — reserverede "
         "kulturer holder pauser, dæmper stemmen og viser færre følelser.",
         ["Ekspressiv", "Reserveret"],
         "Misforstå ikke temperament som vrede (eller tavshed som afvisning): animeret, "
         "følelsesladet kommunikation er normal stil — hold selv hovedet koldt."),
    ]

    for navn, forklaring, _, _ in GESTELAND:
        with st.expander(navn):
            st.markdown(f"**Hvad er det?** {forklaring}")

    st.divider()
    st.subheader("Sammenlign to kulturer")
    st.caption("Sæt de fire dimensioner for begge parter — så viser værktøjet, hvor "
               "gnidningerne opstår, og hvad du gør ved dem. Forudfyldt med din egen "
               "SPM 16-profil for Tyrkiet: relations-fokuseret, formel, flydende tid og "
               "udtryksfuld (ekspressiv).")

    c1, c2 = st.columns(2)
    with c1:
        navn_a = st.text_input("Kultur A (dig)", value="Danmark",
                               key="gest_navn_a",
                               help="Din egen side af bordet — typisk Danmark.")
    with c2:
        navn_b = st.text_input("Kultur B (modparten)", value="Tyrkiet",
                               key="gest_navn_b",
                               help="Modpartens kultur — fx Tyrkiet, Tyskland eller "
                                    "et andet land du forhandler med.")

    # Forudfyldning: Danmark = deal-fokus, uformel, stram tid, reserveret;
    # Tyrkiet = relations-fokus, formel, flydende tid, ekspressiv (SPM 16)
    DEFAULT_A = ["Deal-fokus", "Uformel", "Stram tid (monokron)", "Reserveret"]
    DEFAULT_B = ["Relations-fokus", "Formel", "Flydende tid", "Ekspressiv"]

    valg_a, valg_b = [], []
    for i, (navn, forklaring, poler, _) in enumerate(GESTELAND):
        cc = st.columns(2)
        valg_a.append(cc[0].selectbox(
            f"{navn_a or 'Kultur A'}: {navn}", poler,
            index=poler.index(DEFAULT_A[i]), key=f"gest_a_{i}",
            help=forklaring))
        valg_b.append(cc[1].selectbox(
            f"{navn_b or 'Kultur B'}: {navn}", poler,
            index=poler.index(DEFAULT_B[i]), key=f"gest_b_{i}",
            help=forklaring))

    st.markdown("#### Hvor opstår gnidningerne?")
    forskelle = 0
    for i, (navn, _, _, raad) in enumerate(GESTELAND):
        if valg_a[i] != valg_b[i]:
            forskelle += 1
            st.warning(f"**{navn}** — {navn_a or 'A'} er *{valg_a[i].lower()}*, "
                       f"{navn_b or 'B'} er *{valg_b[i].lower()}*. {raad}", icon="⚠️")
        else:
            st.success(f"**{navn}** — I matcher ({valg_a[i].lower()}): lav friktion her.",
                       icon="✅")
    if forskelle == 0:
        st.info("Ingen forskelle på de fire dimensioner — kulturen er næppe din største "
                "forhandlingsrisiko. Kig i stedet på BAPTA og magtbalancen.", icon="🤝")
    else:
        st.caption(f"{forskelle} af 4 dimensioner er forskellige. Til eksamen: nævn "
                   "forskellen, forklar hvad den betyder ved bordet, og giv et konkret råd — "
                   "som i din egen SPM 16-besvarelse (byg relation først, respektér titler, "
                   "vær tålmodig, og misforstå ikke temperament som vrede).")


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
    fdf = st.data_editor(default_b, num_rows="dynamic", hide_index=True, width="stretch",
                         key="forh_data",
                         column_config={"Prioritet": st.column_config.SelectboxColumn(
                             "Prioritet", options=["Høj", "Middel", "Lav", "Byttechip"])})
    st.caption("Tip: emner med lav værdi for dig men høj for modparten er gode **byttechips** "
               "(du giver dem væk for at vinde på dine høj-prioritets-emner).")

    # Advar hvis MDO/LDO mangler på høj-prioritetsemner — dem må man ikke
    # gå til bordet uden
    _mdo = fdf["Målpunkt (MDO)"].fillna("").astype(str).str.strip()
    _ldo = fdf["Modstandspunkt (LDO)"].fillna("").astype(str).str.strip()
    _hoej = fdf["Prioritet"].fillna("").astype(str) == "Høj"
    mangler = fdf.loc[_hoej & ((_mdo == "") | (_ldo == "")), "Emne"].fillna("").astype(str)
    mangler = [e for e in mangler if e.strip()]
    if mangler:
        st.warning("Høj-prioritetsemner uden MDO eller LDO: **" + ", ".join(mangler) +
                   "** — udfyld dem, før du går til bordet.", icon="✏️")

    st.divider()
    st.subheader("Numerisk ZOPA pr. emne")
    st.caption("Sæt TAL på MDO og LDO for både dig og modparten (modpartens er dit bedste "
               "skøn) — så finder værktøjet overlappet for hvert emne. ZOPA'en ligger mellem "
               "de to modstandspunkter (LDO'erne); MDO'erne viser hvilken vej hver part "
               "trækker.")

    default_z = pd.DataFrame({
        "Emne": ["Pris pr. stk. (kr.)", "Kreditdage", "Leveringspræcision (%)"],
        "Din MDO": [100.0, 60.0, 95.0],
        "Din LDO": [105.0, 45.0, 90.0],
        "Modpart MDO (skøn)": [112.0, 30.0, 85.0],
        "Modpart LDO (skøn)": [98.0, 50.0, 92.0],
    })
    zdf = st.data_editor(
        default_z, num_rows="dynamic", hide_index=True, width="stretch",
        key="zopa_emner",
        column_config={
            "Din MDO": st.column_config.NumberColumn(
                "Din MDO", help="Dit målpunkt: det bedste realistiske resultat du går efter."),
            "Din LDO": st.column_config.NumberColumn(
                "Din LDO", help="Dit modstandspunkt: din smertegrænse, hvor du hellere går "
                                "fra forhandlingen."),
            "Modpart MDO (skøn)": st.column_config.NumberColumn(
                "Modpart MDO (skøn)", help="Dit bedste skøn over modpartens målpunkt — hvad "
                                           "går DE efter?"),
            "Modpart LDO (skøn)": st.column_config.NumberColumn(
                "Modpart LDO (skøn)", help="Dit bedste skøn over modpartens smertegrænse. "
                                           "ZOPA'en ligger mellem jeres to LDO'er."),
        })

    def zopa_pr_emne(din_mdo, din_ldo, mod_mdo, mod_ldo):
        """ZOPA for ét emne: hver parts LDO er grænsen, og MDO'en afslører
        hvilken retning parten trækker i (MDO < LDO → parten vil NED, så
        LDO er et loft; MDO > LDO → parten vil OP, så LDO er et gulv).
        Returnerer (lav, høj), None (ingen ZOPA) eller 'retning' (begge
        parter trækker samme vej — tallene skal tjekkes)."""
        nedre, oevre = [], []
        for mdo, ldo in ((din_mdo, din_ldo), (mod_mdo, mod_ldo)):
            if mdo < ldo:
                oevre.append(ldo)
            elif mdo > ldo:
                nedre.append(ldo)
            else:                       # MDO = LDO: parten står på ét punkt
                nedre.append(ldo)
                oevre.append(ldo)
        if not nedre or not oevre:
            return "retning"
        lav, hoej = max(nedre), min(oevre)
        return (lav, hoej) if lav <= hoej else None

    zopa_linjer = []      # (emoji-linje til skærm, ren linje til tekstfilen)
    z = zdf.copy()
    for kol in ["Din MDO", "Din LDO", "Modpart MDO (skøn)", "Modpart LDO (skøn)"]:
        z[kol] = pd.to_numeric(z[kol], errors="coerce")
    z = z.dropna(subset=["Din MDO", "Din LDO", "Modpart MDO (skøn)", "Modpart LDO (skøn)"])
    for _, r in z.iterrows():
        emne = str(r.get("Emne") or "").strip() or "(uden navn)"
        res = zopa_pr_emne(r["Din MDO"], r["Din LDO"],
                           r["Modpart MDO (skøn)"], r["Modpart LDO (skøn)"])
        if res == "retning":
            zopa_linjer.append((
                f"⚠️ **{emne}:** MDO og LDO peger samme vej for jer begge — tjek at "
                f"modpartens tal er set fra DERES side af bordet.",
                f"{emne}: tjek tallene (MDO/LDO peger samme vej for begge parter)"))
        elif res is None:
            zopa_linjer.append((
                f"🚫 **{emne}:** ingen ZOPA — en part skal flytte sit modstandspunkt, "
                f"eller emnet skal byttes mod noget andet.",
                f"{emne}: INGEN ZOPA"))
        else:
            lav, hoej = res
            d = 0 if float(lav).is_integer() and float(hoej).is_integer() else 1
            zopa_linjer.append((
                f"✅ **{emne}:** ZOPA fra **{num(lav, d)}** til **{num(hoej, d)}** — "
                f"her er der en aftale at lave.",
                f"{emne}: ZOPA {num(lav, d)} - {num(hoej, d)}"))
    if zopa_linjer:
        for linje, _ in zopa_linjer:
            st.markdown(linje)
    else:
        st.info("Udfyld tallene i tabellen for at få ZOPA pr. emne.", icon="👆")

    # -- Download hele arket som tekst (til print eller at have med til bordet)
    def _celle(v):
        s = "" if v is None else str(v)
        return "—" if s.strip() in ("", "nan", "None") else s.strip()

    linjer = ["FORHANDLINGSARK", "=" * 44, ""]
    for _, r in fdf.iterrows():
        emne = _celle(r.get("Emne"))
        if emne == "—":
            continue
        linjer += [
            f"EMNE: {emne}  [prioritet: {_celle(r.get('Prioritet'))}]",
            f"  Modpartens åbning ...... {_celle(r.get('Modpartens åbning'))}",
            f"  Målpunkt (MDO) ......... {_celle(r.get('Målpunkt (MDO)'))}",
            f"  Modstandspunkt (LDO) ... {_celle(r.get('Modstandspunkt (LDO)'))}",
            "",
        ]
    if zopa_linjer:
        linjer += ["NUMERISK ZOPA PR. EMNE", "-" * 44]
        linjer += [ren for _, ren in zopa_linjer]
        linjer += [""]
    linjer += ["Husk: kend din BAPTA, og vær disciplineret ved dit LDO."]
    st.download_button(
        "📄 Download forhandlingsarket som tekst",
        data="\n".join(linjer).encode("utf-8"),
        file_name="forhandlingsark.txt", mime="text/plain",
        help="Gemmer hele arket (emner, MDO/LDO og ZOPA-resultaterne) som en "
             "tekstfil, du kan printe og have med til forhandlingen.")

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
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[saelger_min], y=[1], mode="markers+text", text=["Sælgers min"],
                             textposition="bottom center", marker=dict(color=C_OPT, size=14), name="Sælger"))
    fig.add_trace(go.Scatter(x=[koeber_max], y=[1], mode="markers+text", text=["Købers max"],
                             textposition="top center", marker=dict(color=C_TOTAL, size=14), name="Køber"))
    if zopa:
        fig.add_shape(type="rect", x0=saelger_min, y0=0.85, x1=koeber_max, y1=1.15,
                      fillcolor="rgba(16,185,129,0.30)", line_width=0)
    fig.update_layout(height=220, margin=dict(t=20, b=10), showlegend=False,
                      yaxis=dict(visible=False, range=[0.5, 1.5]), xaxis_title="Pris")
    vis_fig(fig)
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
            st.caption("🎓 **Sådan scorer du point:** 1) Navngiv begrebet og definér det kort → "
                       "2) anvend det på casens konkrete situation → 3) nævn begrænsningen → "
                       "4) konkludér med DIN egen vurdering.")
    if soeg and vist == 0:
        st.info("Ingen begreber matchede søgningen.")

st.divider()
st.caption("Forhandlingsdelen bygger på standard forhandlingsteori (Harvard-metoden, BATNA "
           "kaldet BAPTA som i dit materiale) samt dit eget bargaining-ark (målpunkt/"
           "modstandspunkt, MDO/LDO). Gesteland-profilen for Tyrkiet er din egen fra SPM 16 — "
           "Hofstedes dimensioner ligger under 🧭 Organisation.")
if st.button("🎓 Træn eksamensspørgsmål i Kommunikation",
             help="Åbner Forsvarstræneren med fag-filteret sat til Kommunikation."):
    st.session_state["ex_fag"] = "Kommunikation"
    st.switch_page("pages/7_Forsvarstræner.py")
