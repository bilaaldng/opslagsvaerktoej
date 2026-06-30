"""Produktion — regnemaskiner med dynamiske grafer.

Batch 1: POQ · Linjebalancering · Processkort · Knap kapacitet · Produktions-
strategi (5 dim.) · MPS+ATP · Little's Law · OEE · Perfect Order/OTIF ·
Udnyttelsesgrad ρ. (MRP og S&OP = batch 2.)
Notation matcher brugerens danish-produktion-skill + VIDEN §4.
"""
import math
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import produktion as pr  # noqa: E402
from core import indkoeb as ik  # noqa: E402 (POQ genbruges)
from ui_theme import (  # noqa: E402
    inject_css, style_fig,
    C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_A, C_B, C_C, C_MUTED,
)

st.set_page_config(page_title="Produktion", page_icon="🏭", layout="wide")
inject_css()


def num(x, dec=0):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "—"
    s = f"{x:,.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def kr(x, dec=0):
    return num(x, dec) + " kr."


def pct(x, dec=1):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "—"
    return num(x * 100, dec) + " %"


st.title("🏭 Produktion")
st.caption("Regnemaskiner med live-grafer. Tast ind eller træk i skyderne, så opdateres "
           "graf og mellemregninger med det samme.")

(tab_poq, tab_lb, tab_pk, tab_kk, tab_strat, tab_mps, tab_mrp, tab_sop,
 tab_ll, tab_oee, tab_po, tab_rho) = st.tabs([
    "POQ", "Linjebalancering", "Processkort", "Knap kapacitet",
    "Produktionsstrategi", "MPS + ATP", "MRP", "S&OP",
    "Little's Law", "OEE", "Perfect Order / OTIF", "Udnyttelsesgrad ρ",
])


# ===========================================================================
# POQ — produktionsseriestørrelse (genbrug af core.indkoeb)
# ===========================================================================
with tab_poq:
    st.subheader("POQ — optimal produktionsseriestørrelse")
    st.caption("Til in-house produktion: lageret bygges op løbende under produktion. "
               "Forudfyldt med et eksempel. Samme model som under Indkøb.")

    v, h = st.columns([1, 2])
    with v:
        D = st.number_input("Årlig efterspørgsel D (stk.)", min_value=1.0, value=48000.0,
                            step=1000.0, key="p_poq_D",
                            help="Hvor mange stk. der skal bruges/produceres på et år.")
        dage = st.number_input("Arbejdsdage/år", min_value=1.0, value=250.0, step=5.0, key="p_poq_dage",
                            help="Antal dage om året hvor der produceres. Bruges til at regne den "
                                 "årlige efterspørgsel om til et dagligt forbrug.")
        p = st.number_input("Daglig produktionskapacitet p (stk./dag)", min_value=1.0,
                            value=600.0, step=10.0, key="p_poq_p",
                            help="Hvor mange stk. maskinen kan producere pr. dag (skal være > daglig efterspørgsel).")
        S = st.number_input("Igangsætningsomkostning S (kr./serie)", min_value=0.01,
                            value=850.0, step=50.0, key="p_poq_S",
                            help="Omstilling/opstart pr. serie. Udledes ofte som omstillingstid × timeløn.")
        pris = st.number_input("Produktionspris (kr./stk.)", min_value=0.01, value=4.20,
                               step=0.10, key="p_poq_pris",
                               help="Hvad det koster at fremstille ét stk. Bruges sammen med "
                                    "lagerrenten til at finde, hvad det koster at have varen på lager.")
        rente = st.slider("Lagerrente (%)", 1, 60, 22, key="p_poq_rente",
                          help="Hvor meget det koster om året at have penge bundet i lager, i procent "
                               "af varens værdi. Dækker rente, svind og plads. Ganges med "
                               "produktionsprisen for at finde lageromkostningen pr. stk.") / 100
        Q_cur = st.number_input("Nuværende seriestørrelse (stk.)", min_value=1.0, value=8000.0,
                                step=500.0, key="p_poq_Qcur",
                                help="Den seriestørrelse I bruger i dag. Bruges kun til at vise, hvor "
                                     "meget I kan spare ved at skifte til den optimale (POQ).")

    H = ik.holding_cost_per_unit(pris, rente)
    d = D / dage
    s = ik.epq_summary(D, S, H, d, p, Q_current=Q_cur)
    q_star = s["POQ"]

    with h:
        if q_star == q_star:
            q_grid = np.linspace(max(1, q_star * 0.2), q_star * 2.6, 400)
            cur = ik.epq_curve(D, S, H, d, p, q_grid)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=cur["Q"], y=cur["igangsaetning"], name="Igangsætning", line=dict(color=C_ORDER)))
            fig.add_trace(go.Scatter(x=cur["Q"], y=cur["lageromkostning"], name="Lageromkostning", line=dict(color=C_HOLD)))
            fig.add_trace(go.Scatter(x=cur["Q"], y=cur["total"], name="Total", line=dict(color=C_TOTAL, width=3)))
            fig.add_vline(x=q_star, line_dash="dash", line_color=C_OPT)
            fig.add_trace(go.Scatter(x=[q_star], y=[s["total"]], mode="markers+text",
                                     marker=dict(color=C_OPT, size=12),
                                     text=[f"POQ = {num(q_star,0)}"], textposition="top center", name="Optimum"))
            if Q_cur:
                fig.add_vline(x=Q_cur, line_dash="dot", line_color=C_MUTED,
                              annotation_text=f"Nuværende {num(Q_cur,0)}")
            fig.update_layout(xaxis_title="Seriestørrelse Q (stk.)", yaxis_title="Omkostning (kr./år)",
                              height=430, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), use_container_width=True)
        else:
            st.error("p skal være større end daglig efterspørgsel d.")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("POQ", f"{num(q_star,0)} stk.", help="Optimal produktionsseriestørrelse.")
    m2.metric("Antal serier/år", num(s["antal_serier"], 1), help="D delt med POQ.")
    m3.metric("Maks. lager", f"{num(s['maks_lager'],0)} stk.", help="Højeste lagerniveau: Q·(1−d/p).")
    m4.metric("Total omkostning", kr(s["total"], 0), help="Igangsætning + lager pr. år ved POQ.")

    with st.expander("Mellemregninger / formel", expanded=True):
        st.latex(r"POQ = \sqrt{\dfrac{2 \cdot D \cdot S}{H \cdot \left(1 - \frac{d}{p}\right)}}")
        st.markdown(
            f"- H = {num(pris,2)} × {num(rente*100,0)} % = **{num(H,3)} kr./stk./år**\n"
            f"- d = D/arbejdsdage = {num(d,1)} stk./dag · (1 − d/p) = {num(s['andel_til_lager'],3)}\n"
            f"- POQ = **{num(q_star,0)} stk.** · antal serier/år = {num(s['antal_serier'],1)}"
        )
        if "besparelse" in s:
            st.markdown(f"- Nuværende serie ({num(Q_cur,0)}): total {kr(s['total_nuvaerende'],0)}, "
                        f"**besparelse ved POQ = {kr(s['besparelse'],0)}/år**")


# ===========================================================================
# LINJEBALANCERING
# ===========================================================================
with tab_lb:
    st.subheader("Linjebalancering")
    st.caption("Fordel opgaver på stationer. Takt time = krav; cyklustid = realiseret "
               "(den langsomste station). Effektivitet = hvor lidt tid der spildes.")

    v, h = st.columns([1, 2])
    with v:
        avail = st.number_input("Tilgængelig tid (min./periode)", min_value=1.0, value=60.0,
                                step=5.0, key="lb_avail",
                                help="Fx 60 min., 480 min. (en vagt) osv.")
        output = st.number_input("Krævet output (stk./periode)", min_value=1.0, value=15.0,
                                 step=1.0, key="lb_output",
                                 help="Hvor mange færdige stk. der skal ud af linjen i samme periode. "
                                      "Sammen med tilgængelig tid giver det takt time (kravet pr. stk.).")
        st.caption("Tildel hver opgave til en station (præcedensrækkefølge):")
        st.caption("Kolonnen Station: skriv hvilken station opgaven hører til (1, 2, 3 ...). "
                   "Opgaver med samme nummer udføres på samme station, og deres tider lægges sammen. "
                   "Du fordeler selv opgaverne for at se, hvordan stationerne bliver belastet.")
        default_tasks = pd.DataFrame({
            "Opgave": ["O1", "O2", "O3", "O4", "O5", "O6"],
            "Tid (min)": [3.0, 1.0, 2.0, 1.5, 2.5, 1.0],
            "Station": [1, 1, 2, 2, 3, 3],
        })
        tasks = st.data_editor(default_tasks, num_rows="dynamic", hide_index=True,
                               use_container_width=True, key="lb_tasks", height=250)

    tasks = tasks.copy()
    tasks["Tid (min)"] = pd.to_numeric(tasks["Tid (min)"], errors="coerce")
    tasks["Station"] = pd.to_numeric(tasks["Station"], errors="coerce")
    tasks = tasks.dropna(subset=["Tid (min)", "Station"])
    takt = pr.takt_time(avail, output)
    min_st = pr.theoretical_min_stations(tasks["Tid (min)"].tolist(), takt)

    if not tasks.empty:
        grp = tasks.groupby("Station")["Tid (min)"].sum().sort_index()
        station_times = grp.tolist()
        r = pr.line_balance(station_times)
        with h:
            colors = [C_OPT if abs(t - r["cyklustid"]) < 1e-9 else C_TOTAL for t in station_times]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=[f"Station {int(s)}" for s in grp.index], y=station_times,
                                 marker_color=colors, name="Stationstid",
                                 text=[num(t, 1) for t in station_times], textposition="outside"))
            fig.add_hline(y=takt, line_dash="dash", line_color=C_HOLD,
                          annotation_text=f"Takt = {num(takt,2)}")
            fig.add_hline(y=r["cyklustid"], line_dash="dot", line_color=C_OPT,
                          annotation_text=f"Cyklustid = {num(r['cyklustid'],2)}")
            fig.update_layout(yaxis_title="Tid pr. station (min)", height=430,
                              margin=dict(t=30, b=10), showlegend=False)
            st.plotly_chart(style_fig(fig), use_container_width=True)
            st.caption("Sådan læser du grafen: hver søjle er en station og dens samlede tid. Den "
                       "stiplede takt-linje er kravet pr. stk., den prikkede cyklustids-linje er den "
                       "langsomste station. Søjler over takt-linjen kan ikke følge med efterspørgslen. "
                       "Den fremhævede søjle er flaskehalsen, som sætter tempoet.")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Takt time", f"{num(takt,2)} min", help="Tilgængelig tid / krævet output. Kravet pr. stk.")
        m2.metric("Min. stationer (teoretisk)", num(min_st, 0), help="loft(Σ opgavetider / takt time).")
        m3.metric("Cyklustid", f"{num(r['cyklustid'],2)} min", help="Den langsomste station. Sætter reelt tempoet.")
        m4.metric("Effektivitet", pct(r["effektivitet"]),
                  help="Hvor stor en del af stationernes tid der faktisk bruges på arbejde "
                       "(Σ opgavetid delt med antal stationer gange cyklustid). Tæt på 100 % betyder "
                       "lidt spildt ventetid og en velbalanceret linje; lavt tal betyder, at nogle "
                       "stationer står og venter.")

        with st.expander("Mellemregninger / formel", expanded=True):
            st.markdown(
                f"- Takt = {num(avail,0)}/{num(output,0)} = **{num(takt,2)} min/stk.**\n"
                f"- Min. stationer = loft({num(sum(station_times),1)}/{num(takt,2)}) = **{num(min_st,0)}**\n"
                f"- Cyklustid = største stationstid = **{num(r['cyklustid'],2)} min**\n"
                f"- Effektivitet = {num(sum(station_times),1)}/({num(r['antal_stationer'],0)}×{num(r['cyklustid'],2)}) "
                f"= **{pct(r['effektivitet'])}** · balancetab = {pct(r['balancetab'])}\n"
                f"- Output/time = 60/{num(r['cyklustid'],2)} = **{num(r['output_pr_time'],1)} stk.**"
            )


# ===========================================================================
# PROCESSKORT
# ===========================================================================
with tab_pk:
    st.subheader("Processkort — værdigivende analyse")
    st.caption("Mærk hvert trin som V (værdigivende) eller IV (ikke-værdigivende). "
               "Mål: minimér IV-tid (transport, ventetid, inspektion, lager).")

    default_steps = pd.DataFrame({
        "Trin": ["Modtag materiale", "Transport til maskine", "Bearbejdning",
                 "Ventetid", "Montage", "Inspektion", "Pak"],
        "Tid (min)": [2.0, 4.0, 8.0, 6.0, 5.0, 3.0, 2.0],
        "Type": ["IV", "IV", "V", "IV", "V", "IV", "V"],
    })
    st.caption("Kolonnen Type: vælg V hvis trinnet tilfører produktet værdi, kunden vil betale for "
               "(fx bearbejdning, montage). Vælg IV hvis det ikke gør (transport, ventetid, "
               "inspektion, lager) og helst skal reduceres.")
    steps_df = st.data_editor(
        default_steps, num_rows="dynamic", hide_index=True, use_container_width=True,
        key="pk_steps",
        column_config={"Type": st.column_config.SelectboxColumn("Type", options=["V", "IV"])})

    steps_df = steps_df.copy()
    steps_df["Tid (min)"] = pd.to_numeric(steps_df["Tid (min)"], errors="coerce")
    steps_df = steps_df.dropna(subset=["Tid (min)"])
    steps = [{"tid": t, "type": ty} for t, ty in zip(steps_df["Tid (min)"], steps_df["Type"])]
    r = pr.processkort(steps)

    c1, c2 = st.columns([2, 1])
    with c1:
        fig = go.Figure()
        fig.add_trace(go.Bar(x=["Procestid"], y=[r["vaerdigivende_tid"]], name="Værdigivende (V)",
                             marker_color=C_HOLD, text=[num(r["vaerdigivende_tid"], 1)], textposition="inside"))
        fig.add_trace(go.Bar(x=["Procestid"], y=[r["ikke_vaerdigivende_tid"]], name="Ikke-værdigivende (IV)",
                             marker_color=C_OPT, text=[num(r["ikke_vaerdigivende_tid"], 1)], textposition="inside"))
        fig.update_layout(barmode="stack", yaxis_title="Tid (min)", height=380,
                          margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.15))
        st.plotly_chart(style_fig(fig), use_container_width=True)
    with c2:
        fig2 = go.Figure(go.Pie(values=[r["vaerdigivende_tid"], r["ikke_vaerdigivende_tid"]],
                                labels=["V", "IV"], hole=0.6,
                                marker_colors=[C_HOLD, C_OPT]))
        fig2.update_layout(height=380, margin=dict(t=30, b=10),
                           annotations=[dict(text=pct(r["vaerdigivende_pct"]), x=0.5, y=0.5,
                                             font_size=20, showarrow=False, font_color="#e2e8f0")])
        st.plotly_chart(style_fig(fig2), use_container_width=True)
    st.caption("Tallet i midten af cirklen er den værdigivende andel (V) af den samlede tid. "
               "Jo større den grønne del, jo mindre spild. Den stablede søjle til venstre viser de "
               "samme V- og IV-minutter lagt oven på hinanden.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Cyklustid", f"{num(r['cyklustid'],1)} min", help="Summen af alle trins tider.")
    m2.metric("Værdigivende tid", f"{num(r['vaerdigivende_tid'],1)} min", help="Sum af V-trin.")
    m3.metric("Værdigivende %", pct(r["vaerdigivende_pct"]), help="V-tid / cyklustid. Højere = mindre spild.")


# ===========================================================================
# KNAP KAPACITET
# ===========================================================================
with tab_kk:
    st.subheader("Knap kapacitet — produktmix på flaskehalsen")
    st.caption("Når én ressource er flaskehals, prioritér produkter efter dækningsbidrag "
               "pr. flaskehalstime (DB/time), ikke pr. stk. Fyld op til efterspørgslen.")

    avail = st.number_input("Tilgængelig flaskehalstid (min.)", min_value=1.0, value=200.0,
                            step=10.0, key="kk_avail")
    default_p = pd.DataFrame({
        "Produkt": ["A", "B", "C"],
        "DB pr. stk": [100.0, 60.0, 40.0],
        "Tid pr. stk (min)": [2.0, 1.0, 2.0],
        "Efterspørgsel": [50, 100, 50],
    })
    st.caption("Kolonner: DB pr. stk = dækningsbidrag (salgspris minus variable omkostninger) for ét "
               "stk. Tid pr. stk = den tid produktet bruger på flaskehals-ressourcen (ikke den samlede "
               "produktionstid). Efterspørgsel = højeste antal der kan sælges, som planen fylder op til.")
    pdf = st.data_editor(default_p, num_rows="dynamic", hide_index=True,
                         use_container_width=True, key="kk_data")

    pdf = pdf.copy()
    for c in ["DB pr. stk", "Tid pr. stk (min)", "Efterspørgsel"]:
        pdf[c] = pd.to_numeric(pdf[c], errors="coerce")
    pdf = pdf.dropna()
    produkter = [{"navn": r["Produkt"], "db_stk": r["DB pr. stk"],
                  "tid_pr_stk": r["Tid pr. stk (min)"], "efterspoergsel": r["Efterspørgsel"]}
                 for _, r in pdf.iterrows()]

    if produkter:
        res = pr.knap_kapacitet(produkter, avail)
        plan = res["plan"]
        fig = go.Figure(go.Bar(
            x=[it["navn"] for it in plan], y=[it["db_pr_time"] for it in plan],
            marker_color=C_TOTAL, text=[num(it["db_pr_time"], 1) for it in plan], textposition="outside"))
        fig.update_layout(yaxis_title="DB pr. flaskehalstime (kr./min)", height=360,
                          margin=dict(t=30, b=10), xaxis_title="Produkt (prioriteret rækkefølge)")
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: jo højere søjle, jo mere tjener produktet pr. minut på "
                   "flaskehalsen. Produkterne står fra venstre i den rækkefølge de bør produceres, "
                   "og planen fylder op til efterspørgslen, indtil tiden er brugt.")

        tab = pd.DataFrame([{
            "Produkt": it["navn"],
            "DB/time": num(it["db_pr_time"], 1),
            "Produceres": int(it["produceres"]),
            "Tid brugt (min)": num(it["tid_brugt"], 0),
            "DB i alt": kr(it["db_i_alt"], 0),
        } for it in plan])
        st.dataframe(tab, hide_index=True, use_container_width=True)
        m1, m2 = st.columns(2)
        m1.metric("Samlet dækningsbidrag", kr(res["samlet_db"], 0), help="Summen af DB for det valgte produktmix.")
        m2.metric("Uudnyttet flaskehalstid", f"{num(res['uudnyttet_tid'],0)} min",
                  help="Flaskehalstid der er tilovers, når alle rentable produkter er fyldt op til "
                       "efterspørgslen. Tid du kan bruge på flere ordrer eller nye produkter.")
        with st.expander("Mellemregninger / metode", expanded=True):
            st.markdown(
                "- **DB pr. time = DB pr. stk / tid pr. stk** på flaskehalsen.\n"
                "- Rangordn produkterne efter DB/time (højest først).\n"
                "- Fyld op til efterspørgslen indtil flaskehalstiden er brugt.\n"
                "- Prioritér på **DB/time**, ikke DB/stk: en vare med højt DB/stk men lang "
                "flaskehalstid kan være dårligere end en hurtig vare med lavere DB/stk."
            )


# ===========================================================================
# PRODUKTIONSSTRATEGI (5 dimensioner) — opslag
# ===========================================================================
with tab_strat:
    st.subheader("Produktionsstrategi — de 5 dimensioner")
    st.caption("Den kvalitative analyseramme til 'foreslå en ny produktionsstrategi'. "
               "Gennemgå hver dimension og vælg den der passer til produkttype, volumen og variation.")

    dims = [
        ("1. Ordretype (afkoblingspunkt)",
         "**MTS** Make-to-Stock (lager, standardvarer) · **ATO** Assemble-to-Order (saml på ordre) · "
         "**MTO** Make-to-Order (producér på ordre) · **ETO** Engineer-to-Order (konstruér på ordre, fx bro).",
         "Standard/høj volumen taler for MTS. Kundetilpasning taler for MTO/ATO/ETO."),
        ("2. Produktionsfilosofi",
         "**Lean** (eliminér spild, flow, pull, løbende forbedring) vs. **Fordisme** "
         "(masseproduktion, faste stationer, lav variation).",
         "Varieret/spildtynget produktion taler for Lean. Meget ensartet høj volumen kan bære Fordisme."),
        ("3. Produktionsstyring",
         "**MRP** (push — planlæg fra forecast/MPS, beregn nettobehov) vs. **JIT** "
         "(pull — producér først ved efterspørgsel). 'Først-til-mølle' er ustyret og typisk et problem.",
         "Afhængig efterspørgsel/komponenter taler for MRP. Stabil takt + tæt leverandør taler for JIT."),
        ("4. Produktionsformer",
         "**Jobshop** (enkeltstyk/varieret, funktionel) · **serie/batch** · **flow/masse** "
         "(standard, høj volumen) · **enkeltstyk/projekt** (unikt, stort).",
         "Match til volumen og variation: høj volumen/lav variation = flow; lav volumen/høj variation = jobshop."),
        ("5. Produktionslayout",
         "**Fast plads** (produktet står stille — skib/bro) · **linjelayout** (produktorienteret, flow) · "
         "**funktionelt layout** (maskiner samlet efter type, jobshop) · **gruppe-/cellelayout** (familier af emner).",
         "Flow taler for linjelayout. Produktfamilier taler for cellelayout. Store anlæg = fast plads."),
    ]
    for titel, hvad, hvornaar in dims:
        with st.expander(titel, expanded=False):
            st.markdown(f"**Muligheder:** {hvad}")
            st.markdown(f"**Valg:** {hvornaar}")

    st.info("Eksamenstip: gennemgå alle 5 dimensioner for casen, beskriv nuværende tilstand, "
            "og anbefal en ændring pr. dimension med begrundelse i produkttype/volumen/variation.",
            icon="🎓")


# ===========================================================================
# MPS + ATP
# ===========================================================================
with tab_mps:
    st.subheader("MPS + ATP — Master Production Schedule")
    st.caption("Projected ending inventory (PEI) og Available-to-Promise (ATP) uge for uge. "
               "Negativ PEI = du mangler dækning og skal planlægge produktion.")

    start_inv = st.number_input("Startlager (stk.)", min_value=0.0, value=50.0, step=10.0, key="mps_start")
    default_mps = pd.DataFrame({
        "Uge": [1, 2, 3, 4, 5, 6],
        "Forecast": [30, 30, 30, 40, 40, 40],
        "Bookede ordrer": [35, 20, 10, 40, 15, 5],
        "MPS (produktion)": [70, 0, 0, 80, 0, 0],
    })
    st.caption("Kolonner: Forecast = forventet salg i ugen. Bookede ordrer = salg kunder allerede "
               "har bestilt. MPS = den mængde I planlægger at producere/færdiggøre i ugen.")
    mdf = st.data_editor(default_mps, num_rows="dynamic", hide_index=True,
                         use_container_width=True, key="mps_data")

    mdf = mdf.copy()
    for c in ["Forecast", "Bookede ordrer", "MPS (produktion)"]:
        mdf[c] = pd.to_numeric(mdf[c], errors="coerce").fillna(0)
    forecast = mdf["Forecast"].tolist()
    booked = mdf["Bookede ordrer"].tolist()
    mps = mdf["MPS (produktion)"].tolist()
    uger = mdf["Uge"].tolist()

    if forecast:
        res = pr.mps_atp(forecast, booked, mps, start_inv)
        pei = res["pei"]
        atp = res["atp"]
        colors = [C_OPT if v < 0 else C_TOTAL for v in pei]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=uger, y=pei, mode="lines+markers", name="PEI",
                                 line=dict(color=C_TOTAL, width=3), marker=dict(color=colors, size=9)))
        fig.add_hline(y=0, line_dash="dash", line_color=C_OPT)
        fig.update_layout(xaxis_title="Uge", yaxis_title="Projected ending inventory (stk.)",
                          height=380, margin=dict(t=30, b=10), showlegend=False)
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: linjen er det forventede slutlager hver uge. Punkter under "
                   "den stiplede nul-linje (markeret med anden farve) betyder, at lageret ikke rækker, "
                   "og at du skal planlægge produktion tidligere.")

        out = pd.DataFrame({
            "Uge": uger,
            "Forecast": [num(x, 0) for x in forecast],
            "Bookede": [num(x, 0) for x in booked],
            "MPS": [num(x, 0) for x in mps],
            "PEI": [num(x, 0) for x in pei],
            "ATP": [num(a, 0) if a is not None else "—" for a in atp],
        })
        st.dataframe(out, hide_index=True, use_container_width=True)
        if any(v < 0 for v in pei):
            uger_neg = [int(u) for u, v in zip(uger, pei) if v < 0]
            st.warning(f"Negativ PEI i uge {uger_neg} — planlæg produktion (MPS) tidligere.", icon="⚠️")
        with st.expander("Mellemregninger / formel", expanded=True):
            st.markdown(
                "- **PEI** = forrige lager + denne uges MPS − **MAX**(forecast, bookede ordrer). "
                "MAX, fordi du skal kunne dække det højeste af forventet og bestilt salg.\n"
                "- **ATP** beregnes kun i uger med MPS > 0 (samt uge 1): "
                "MPS (+ startlager i uge 1) − Σ bookede ordrer frem til næste MPS-uge.\n"
                "- ATP = hvor mange du frit kan love nye kunder uden at bryde eksisterende ordrer."
            )


# ===========================================================================
# LITTLE'S LAW
# ===========================================================================
with tab_ll:
    st.subheader("Little's Law")
    st.caption("WIP = gennemløbshastighed (R) × gennemløbstid (T). Løs for den størrelse du mangler.")

    beregn = st.radio("Hvad vil du beregne?", ["WIP", "Gennemløbshastighed (R)", "Gennemløbstid (T)"],
                      horizontal=True, key="ll_mode",
                      help="Vælg den størrelse du IKKE kender. Du taster de to du kender, så regnes den "
                           "tredje. WIP = igangværende arbejde, R = færdige enheder pr. tid, "
                           "T = tid en enhed er undervejs.")
    v, h = st.columns([1, 1])
    with v:
        if beregn == "WIP":
            R = st.number_input("Gennemløbshastighed R (stk./tidsenhed)", min_value=0.0, value=50.0, step=1.0, key="ll_R1")
            T = st.number_input("Gennemløbstid T (tidsenheder)", min_value=0.0, value=4.0, step=0.5, key="ll_T1")
            res = pr.littles_law(throughput=R, flow_time=T)
        elif beregn == "Gennemløbshastighed (R)":
            WIP = st.number_input("WIP (enheder i systemet)", min_value=0.0, value=200.0, step=10.0, key="ll_W2")
            T = st.number_input("Gennemløbstid T (tidsenheder)", min_value=0.01, value=4.0, step=0.5, key="ll_T2")
            res = pr.littles_law(wip=WIP, flow_time=T)
        else:
            WIP = st.number_input("WIP (enheder i systemet)", min_value=0.0, value=200.0, step=10.0, key="ll_W3")
            R = st.number_input("Gennemløbshastighed R (stk./tidsenhed)", min_value=0.01, value=50.0, step=1.0, key="ll_R3")
            res = pr.littles_law(wip=WIP, throughput=R)
    with h:
        st.metric("WIP", f"{num(res['WIP'],1)} enh.", help="Antal enheder i systemet (igangværende arbejde).")
        st.metric("Gennemløbshastighed R", f"{num(res['R'],2)} stk./tid", help="Hvor mange enheder der færdiggøres pr. tidsenhed.")
        st.metric("Gennemløbstid T", f"{num(res['T'],2)} tid", help="Hvor længe en enhed er i systemet.")
    st.latex(r"WIP = R \cdot T")
    st.caption("OBS: 'gennemløbstid T' her er tiden gennem hele systemet, ikke stations-cyklustiden "
               "fra linjebalancering.")


# ===========================================================================
# OEE
# ===========================================================================
with tab_oee:
    st.subheader("OEE — Overall Equipment Effectiveness")
    st.caption("OEE = tilgængelighed × ydelse × kvalitet.")
    st.info("OEE er en industristandard og indgår ikke direkte i jeres pensum/eksamen — "
            "tag den som ekstra hjælper.", icon="ℹ️")

    v, h = st.columns([1, 2])
    with v:
        planned = st.number_input("Planlagt produktionstid (min.)", min_value=1.0, value=480.0, step=10.0, key="oee_pl",
                                  help="Den tid maskinen var planlagt til at køre.")
        downtime = st.number_input("Stilstand (min.)", min_value=0.0, value=80.0, step=5.0, key="oee_dt",
                                   help="Tid maskinen stod stille (nedbrud, omstilling).")
        ideal = st.number_input("Ideel cyklustid (min./stk.)", min_value=0.001, value=0.5, step=0.1, key="oee_ic",
                                help="Den hurtigst mulige tid pr. stk., hvis alt kører perfekt.")
        total = st.number_input("Producerede enheder", min_value=0.0, value=700.0, step=10.0, key="oee_tot",
                                help="Alt der blev fremstillet, både gode og fejlbehæftede.")
        good = st.number_input("Gode enheder", min_value=0.0, value=670.0, step=10.0, key="oee_good",
                               help="De fejlfrie enheder ud af de producerede.")

    r = pr.oee(planned, downtime, ideal, total, good)
    with h:
        fig = go.Figure(go.Bar(
            x=["Tilgængelighed", "Ydelse", "Kvalitet", "OEE"],
            y=[r["tilgaengelighed"], r["ydelse"], r["kvalitet"], r["OEE"]],
            marker_color=[C_TOTAL, C_ORDER, C_HOLD, C_OPT],
            text=[pct(r["tilgaengelighed"]), pct(r["ydelse"]), pct(r["kvalitet"]), pct(r["OEE"])],
            textposition="outside"))
        fig.update_layout(yaxis_title="Andel", yaxis=dict(range=[0, 1.1], tickformat=".0%"),
                          height=400, margin=dict(t=30, b=10))
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: de tre første søjler er hver sin tabskilde (tid, tempo, "
                   "kvalitet). OEE yderst er dem ganget sammen og derfor altid lavere end hver enkelt; "
                   "den viser den samlede effektivitet.")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Tilgængelighed", pct(r["tilgaengelighed"]), help="Køretid / planlagt tid.")
    m2.metric("Ydelse", pct(r["ydelse"]), help="(Ideel cyklustid × producerede) / køretid.")
    m3.metric("Kvalitet", pct(r["kvalitet"]), help="Gode enheder / producerede enheder.")
    m4.metric("OEE", pct(r["OEE"]), help="Tilgængelighed × ydelse × kvalitet.")


# ===========================================================================
# PERFECT ORDER / OTIF
# ===========================================================================
with tab_po:
    st.subheader("Perfect Order / OTIF")
    st.caption("Andel ordrer leveret korrekt: til tiden, komplet, ubeskadiget og korrekt faktureret.")

    metode = st.radio("Metode", ["Fra delrater", "Direkte (antal ordrer)"], horizontal=True, key="po_mode",
                      help="Vælg 'Fra delrater' hvis du kender hver fejltype hver for sig (til tiden, "
                           "komplet osv.). Vælg 'Direkte' hvis du blot kender det samlede antal ordrer "
                           "og hvor mange der havde mindst én fejl.")
    if metode == "Fra delrater":
        c = st.columns(4)
        ot = c[0].slider("Til tiden %", 50, 100, 95, key="po_ot") / 100
        ko = c[1].slider("Komplet %", 50, 100, 98, key="po_ko") / 100
        ub = c[2].slider("Ubeskadiget %", 50, 100, 99, key="po_ub") / 100
        fa = c[3].slider("Korrekt faktura %", 50, 100, 97, key="po_fa") / 100
        r = pr.perfect_order(ot, ko, ub, fa)
        po_rate = r["perfect_order"]
        komp = r["komponenter"]
        fig = go.Figure(go.Bar(
            x=["Til tiden", "Komplet", "Ubeskadiget", "Korrekt faktura", "Perfect Order"],
            y=[komp["til_tiden"], komp["komplet"], komp["ubeskadiget"], komp["korrekt_faktura"], po_rate],
            marker_color=[C_TOTAL, C_TOTAL, C_TOTAL, C_TOTAL, C_OPT],
            text=[pct(v) for v in [komp["til_tiden"], komp["komplet"], komp["ubeskadiget"], komp["korrekt_faktura"], po_rate]],
            textposition="outside"))
        fig.update_layout(yaxis=dict(range=[0, 1.1], tickformat=".0%"), height=380, margin=dict(t=30, b=10))
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.metric("Perfect Order", pct(po_rate),
                  help="Produkt af de fire delrater (antager uafhængighed).")
        st.caption("Perfect Order = til tiden × komplet × ubeskadiget × korrekt faktura "
                   f"= {pct(po_rate)}. De fire fejlkilder ganges sammen.")
    else:
        c = st.columns(2)
        total = c[0].number_input("Antal ordrer i alt", min_value=1.0, value=100.0, step=10.0, key="po_total")
        fejl = c[1].number_input("Ordrer med mindst én fejl", min_value=0.0, value=12.0, step=1.0, key="po_fejl")
        rate = pr.perfect_order_direct(total, fejl)
        st.metric("Perfect Order", pct(rate),
                  help="(Total − ordrer med fejl) / total.")
        st.caption(f"Perfect Order = ({num(total,0)} − {num(fejl,0)}) / {num(total,0)} = {pct(rate)}.")


# ===========================================================================
# UDNYTTELSESGRAD ρ
# ===========================================================================
with tab_rho:
    st.subheader("Udnyttelsesgrad ρ = λ/μ")
    st.caption("Hvor hårdt en ressource belastes. Jo tættere på 100 %, jo længere ventetid "
               "(kø) — ventetiden eksploderer når ρ nærmer sig 1.")

    v, h = st.columns([1, 2])
    with v:
        lam = st.number_input("Ankomstrate λ (stk./tidsenhed)", min_value=0.0, value=8.0, step=0.5, key="rho_lam",
                              help="Hvor mange enheder der ankommer/efterspørges pr. tidsenhed.")
        mu = st.number_input("Kapacitetsrate μ (stk./tidsenhed)", min_value=0.01, value=10.0, step=0.5, key="rho_mu",
                             help="Hvor mange enheder ressourcen kan betjene pr. tidsenhed.")
    r = pr.queue_metrics(lam, mu)
    with h:
        rr = np.linspace(0.05, 0.98, 200)
        tw = rr / (mu * (1 - rr))      # Tw som funktion af rho ved fast mu
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=rr * 100, y=tw, line=dict(color=C_TOTAL, width=3), name="Ventetid"))
        if mu > lam:
            fig.add_trace(go.Scatter(x=[r["rho"] * 100], y=[r["Tw"]], mode="markers+text",
                                     marker=dict(color=C_OPT, size=12),
                                     text=[f"ρ = {pct(r['rho'])}"], textposition="top center", name="Valgt"))
        fig.update_layout(xaxis_title="Udnyttelsesgrad ρ (%)", yaxis_title="Ventetid i kø Tw (tid)",
                          height=400, margin=dict(t=30, b=10), showlegend=False)
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: kurven viser ventetiden i kø ved forskellige "
                   "udnyttelsesgrader. Den markerede prik er jeres nuværende ρ (udnyttelsesgrad). "
                   "Jo længere mod højre (tæt på 100 %), jo stejlere stiger ventetiden, derfor undgår "
                   "man at belaste en ressource helt op til kapaciteten.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Udnyttelsesgrad ρ", pct(r["rho"]), help="λ / μ. Over 100 % = systemet er overbelastet.")
    m2.metric("Gennemløbstid Ts", num(r["Ts"], 3) if r["Ts"] != float("inf") else "∞",
              help="Gennemsnitstid i systemet (kø + betjening): 1/(μ−λ).")
    m3.metric("Ventetid i kø Tw", num(r["Tw"], 3) if r["Tw"] != float("inf") else "∞",
              help="Gennemsnitlig ventetid før betjening: λ/(μ(μ−λ)).")
    if mu <= lam:
        st.error("λ ≥ μ: ressourcen er overbelastet, og køen vokser uendeligt.", icon="⚠️")


# ===========================================================================
# MRP (BOM-eksplosion)
# ===========================================================================
with tab_mrp:
    st.subheader("MRP — materialebehovsplanlægning")
    st.caption("Fra slutproduktets behov ned gennem styklisten (BOM). Hver komponents "
               "planlagte ordreafgivelser bliver til børnenes bruttobehov, forskudt med ledetiden.")

    WEEKS = 8
    uger = list(range(1, WEEKS + 1))

    st.markdown("**Bruttobehov for slutproduktet** (pr. uge):")
    default_d = pd.DataFrame({"Uge": uger, "Behov": [0, 0, 0, 0, 0, 0, 0, 100]})
    ddf = st.data_editor(default_d, hide_index=True, use_container_width=True, key="mrp_demand",
                         disabled=["Uge"], height=150)
    demand = pd.to_numeric(ddf["Behov"], errors="coerce").fillna(0).tolist()
    demand = (demand + [0] * WEEKS)[:WEEKS]

    st.markdown("**Stykliste (BOM)** — forælder tom = slutprodukt · lot 0 = lot-for-lot:")
    default_bom = pd.DataFrame({
        "Komponent": ["Produkt", "Del B", "Del C", "Råvare D"],
        "Forælder": ["", "Produkt", "Produkt", "Del B"],
        "Antal pr.": [1, 2, 1, 3],
        "Ledetid": [1, 2, 1, 1],
        "Lotstørrelse": [0, 0, 50, 0],
        "Lager": [0, 10, 0, 20],
    })
    st.caption("Kolonner: Antal pr. = hvor mange af komponenten der skal bruges for at lave én af "
               "forælderen. Ledetid = antal uger fra ordre afgives til den er klar (forskyder "
               "bestillingen tilbage i tid). Lotstørrelse = mindste/faste bestillingsmængde "
               "(0 = bestil præcis det der mangler). Lager = nuværende beholdning.")
    bomdf = st.data_editor(default_bom, num_rows="dynamic", hide_index=True,
                           use_container_width=True, key="mrp_bom", height=200)
    bomdf = bomdf.copy()
    for c in ["Antal pr.", "Ledetid", "Lotstørrelse", "Lager"]:
        bomdf[c] = pd.to_numeric(bomdf[c], errors="coerce").fillna(0)
    bomdf = bomdf[bomdf["Komponent"].astype(str).str.strip() != ""]

    rows = [{"navn": r["Komponent"], "foraelder": (str(r["Forælder"]).strip() or None),
             "antal": r["Antal pr."], "ledetid": int(r["Ledetid"]),
             "lot": r["Lotstørrelse"], "lager": r["Lager"]} for _, r in bomdf.iterrows()]

    if rows:
        res = pr.mrp_explode(rows, demand, WEEKS)
        raekkefoelge = [n for n in res["raekkefoelge"] if n in res["items"]]
        rk = {"gross": "Bruttobehov", "scheduled": "Planlagte modtagelser",
              "pei": "Disponibel beholdning", "net": "Nettobehov",
              "planned_receipts": "Planlagte ordremodtagelser",
              "planned_orders": "Planlagte ordreafgivelser"}
        for i, navn in enumerate(raekkefoelge):
            it = res["items"][navn]
            meta = next((r for r in rows if r["navn"] == navn), {})
            with st.expander(f"📦 {navn}  (ledetid {meta.get('ledetid','?')}, "
                             f"lot {num(meta.get('lot',0),0)}, lager {num(meta.get('lager',0),0)})",
                             expanded=(i == 0)):
                tab = pd.DataFrame({rk[k]: [num(v, 0) for v in it[k]] for k in rk},
                                   index=[f"Uge {u}" for u in uger]).T
                tab.columns = [f"Uge {u}" for u in uger]
                st.dataframe(tab, use_container_width=True)
                if it["overdue"] > 0:
                    st.warning(f"{num(it['overdue'],0)} stk. skulle være afgivet før uge 1 "
                               "(ledetiden er længere end horisonten tillader).", icon="⚠️")
        st.caption("Læsning: 'Planlagte ordreafgivelser' er det du faktisk skal bestille/igangsætte "
                   "den pågældende uge. De forskydes ned til børnene som bruttobehov.")
        st.caption("Rækkerne i tabellerne betyder: Bruttobehov = hvad der skal bruges. Disponibel "
                   "beholdning = hvad der er tilbage på lager. Nettobehov = det der mangler efter "
                   "lager. Planlagte ordremodtagelser = hvornår varen skal være klar. Planlagte "
                   "ordreafgivelser = hvornår du skal bestille/igangsætte (skubbet tilbage med "
                   "ledetiden), og det bliver til børnenes bruttobehov.")


# ===========================================================================
# S&OP — aggregeret produktionsplan (Level vs. Chase)
# ===========================================================================
with tab_sop:
    st.subheader("S&OP — aggregeret produktionsplan")
    st.caption("Level holder arbejdsstyrken konstant (lageret svinger). Chase følger "
               "efterspørgslen ved at hyre/fyre (lageret holdes lavt). Sammenlign omkostningerne.")

    c = st.columns(4)
    tpe = c[0].number_input("Timer pr. enhed", min_value=0.01, value=2.0, step=0.5, key="sop_tpe",
                            help="Arbejdstid for at lave ét stk. Bruges sammen med timer pr. md. til "
                                 "at finde, hvor mange arbejdere efterspørgslen kræver.")
    tpm = c[1].number_input("Timer pr. md./arbejder", min_value=1.0, value=160.0, step=10.0, key="sop_tpm",
                            help="Hvor mange timer én ansat arbejder på en måned.")
    start_inv = c[2].number_input("Startlager", value=0.0, step=50.0, key="sop_inv")
    start_w = c[3].number_input("Start-arbejdsstyrke", min_value=0.0, value=12.0, step=1.0, key="sop_w",
                                help="Antal ansatte ved planens start.")
    c2 = st.columns(3)
    hyre = c2[0].number_input("Hyreomkostning pr. ansat", min_value=0.0, value=5000.0, step=500.0, key="sop_hyre")
    fyre = c2[1].number_input("Fyreomkostning pr. ansat", min_value=0.0, value=8000.0, step=500.0, key="sop_fyre")
    lager = c2[2].number_input("Lageromkostning pr. enhed/md.", min_value=0.0, value=10.0, step=1.0, key="sop_lager")

    default_fc = pd.DataFrame({
        "Måned": ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"],
        "Forecast": [1000, 1200, 1400, 1100, 900, 1000],
    })
    fcdf = st.data_editor(default_fc, num_rows="dynamic", hide_index=True,
                          use_container_width=True, key="sop_fc", height=250)
    fcdf = fcdf.copy()
    fcdf["Forecast"] = pd.to_numeric(fcdf["Forecast"], errors="coerce").fillna(0)
    forecast = fcdf["Forecast"].tolist()
    maaneder = fcdf["Måned"].tolist()

    if forecast:
        common = dict(timer_pr_enhed=tpe, timer_pr_md=tpm, startlager=start_inv,
                      start_arbejdere=start_w, hyreomk=hyre, fyreomk=fyre, lageromk=lager)
        lev = pr.sop_plan(forecast, strategi="Level", **common)
        cha = pr.sop_plan(forecast, strategi="Chase", **common)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=maaneder, y=forecast, name="Forecast (efterspørgsel)",
                             marker_color=C_MUTED, opacity=0.6))
        fig.add_trace(go.Scatter(x=maaneder, y=lev["production"], name="Level-produktion",
                                 line=dict(color=C_TOTAL, width=3)))
        fig.add_trace(go.Scatter(x=maaneder, y=cha["production"], name="Chase-produktion",
                                 line=dict(color=C_ORDER, width=3, dash="dash")))
        fig.update_layout(yaxis_title="Enheder", height=380, margin=dict(t=30, b=10),
                          legend=dict(orientation="h", y=1.12))
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: de grå søjler er efterspørgslen. Den flade linje (Level) "
                   "holder produktionen konstant, så lageret svinger. Den svingende, stiplede linje "
                   "(Chase) følger søjlerne tæt ved at hyre og fyre. Sammenlign med "
                   "totalomkostningerne nedenfor for at se hvilken der er billigst.")

        billigst = "Level" if lev["total"] <= cha["total"] else "Chase"
        m1, m2, m3 = st.columns(3)
        m1.metric("Level — total omkostning", kr(lev["total"], 0),
                  help="Konstant arbejdsstyrke. Lageromkostninger dominerer.")
        m2.metric("Chase — total omkostning", kr(cha["total"], 0),
                  help="Følg efterspørgsel. Hyre-/fyreomkostninger dominerer.")
        m3.metric("Billigst", billigst, delta=kr(-abs(lev["total"] - cha["total"]), 0),
                  delta_color="off", help="Den strategi med lavest samlet omkostning.")

        valg = st.radio("Vis månedstabel for", ["Level", "Chase"], horizontal=True, key="sop_valg")
        plan = lev if valg == "Level" else cha
        tab = pd.DataFrame({
            "Måned": maaneder,
            "Forecast": [num(x, 0) for x in forecast],
            "Arbejdere": [num(x, 0) for x in plan["workers"]],
            "Produktion": [num(x, 0) for x in plan["production"]],
            "Hyringer": [num(x, 0) for x in plan["hires"]],
            "Fyringer": [num(x, 0) for x in plan["layoffs"]],
            "Slutlager": [num(x, 0) for x in plan["ending"]],
        })
        st.dataframe(tab, hide_index=True, use_container_width=True)
        with st.expander("Mellemregninger / omkostninger", expanded=True):
            st.markdown(
                f"- **{valg}**: hyre = {kr(plan['hyre_total'],0)} · fyre = {kr(plan['fyre_total'],0)} · "
                f"lager = {kr(plan['lager_total'],0)}\n"
                f"- **Total = {kr(plan['total'],0)}**\n"
                "- Arbejdere krævet = forecast × timer pr. enhed / timer pr. md. "
                "(Level bruger årsgennemsnittet; Chase runder op pr. måned)."
            )
