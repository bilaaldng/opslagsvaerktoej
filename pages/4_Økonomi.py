"""Økonomi — regnemaskiner med dynamiske grafer.

Moduler: Investeringskalkule (NPV/IRR/payback/kritisk levetid) · Break-even ·
Priskalkulation (bidrag/fordeling/retrograd) · Prisoptimering (total-/grænse) ·
Nøgletalsanalyse. Notation matcher brugerens danish-okonomi-skill + VIDEN §7.
"""
import math
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import oekonomi as ok  # noqa: E402
from ui_theme import (  # noqa: E402
    inject_css, style_fig, C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_MUTED,
)

st.set_page_config(page_title="Økonomi", page_icon="💰", layout="wide")
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


st.title("💰 Økonomi")
st.caption("Regnemaskiner med live-grafer. Tast ind eller træk i skyderne, så opdateres "
           "graf og mellemregninger med det samme.")

tab_inv, tab_be, tab_kalk, tab_opt, tab_nt, tab_bud = st.tabs([
    "Investeringskalkule", "Break-even", "Priskalkulation",
    "Prisoptimering", "Nøgletalsanalyse", "Budget",
])


# ===========================================================================
# INVESTERINGSKALKULE
# ===========================================================================
with tab_inv:
    st.subheader("Investeringskalkule — kapitalværdi (NPV) og intern rente (IRR)")
    st.caption("Indtast cashflows (år 0 = investeringen, negativ). NPV-profilen viser, "
               "hvordan kapitalværdien falder med renten og krydser nul ved IRR.")

    v, h = st.columns([1, 2])
    with v:
        rente = st.number_input("Kalkulationsrente (%)", min_value=0.5, max_value=40.0,
                                value=10.0, step=0.5, format="%.1f", key="inv_rente",
                                help="Afkastkravet. NPV > 0 betyder investeringen tjener mere end "
                                     "kravet. Kan skrives med decimaler, fx 8,5.") / 100
        default_cf = pd.DataFrame({"År": [0, 1, 2, 3, 4, 5],
                                   "Cashflow": [-100000.0, 30000, 30000, 30000, 30000, 30000]})
        st.caption("Skriv investeringen i år 0 som et negativt tal (fx -100000, fordi du "
                   "betaler det ud). For hvert af de følgende år skriver du det beløb, "
                   "investeringen giver tilbage det år. Du kan tilføje eller slette rækker — "
                   "også med huller i årrækken (fx år 0, 1 og 5).")
        cfdf = st.data_editor(default_cf, num_rows="dynamic", hide_index=True,
                              width="stretch", key="inv_cf", height=260)
        with st.expander("Forudsætninger til kritiske værdier (valgfri)"):
            salgspris_stk = st.number_input(
                "Salgspris pr. stk.", min_value=0.0, value=0.0, step=10.0, key="inv_pris",
                help="Bruges kun til den kritiske omsætning i år 1: hvor lavt salget må falde, "
                     "før investeringen ikke længere er lønsom. Lad den stå på 0, hvis du ikke "
                     "regner i styk.")
            db_stk = st.number_input(
                "Dækningsbidrag (DB) pr. stk.", min_value=0.0, value=0.0, step=10.0, key="inv_db",
                help="Hvad hvert solgt stk. bidrager med (salgspris minus variable omkostninger). "
                     "Bruges til at omregne den kritiske indbetaling i år 1 til styk og omsætning.")
            scrap_inv = st.number_input(
                "Scrapværdi i sidste år", min_value=0.0, value=0.0, step=5000.0, key="inv_scrap",
                help="Det maskinen kan sælges for til sidst. Beløbet skal ALLEREDE være lagt ind "
                     "i sidste års cashflow i tabellen — her bruges det kun til at regne den "
                     "kritiske årlige indbetaling rigtigt (scrappen skal ikke med i annuiteten).")

    cfdf = cfdf.copy()
    cfdf["År"] = pd.to_numeric(cfdf["År"], errors="coerce")
    cfdf["Cashflow"] = pd.to_numeric(cfdf["Cashflow"], errors="coerce")
    cfdf = cfdf.dropna().sort_values("År")
    if cfdf["År"].duplicated().any():
        st.warning("Samme år optræder flere gange i tabellen — beløbene lægges sammen pr. år. "
                   "Tjek at det er meningen.", icon="⚠️")
        cfdf = cfdf.groupby("År", as_index=False)["Cashflow"].sum().sort_values("År")
    years = cfdf["År"].tolist()
    cashflows = cfdf["Cashflow"].tolist()

    if len(cashflows) >= 2:
        if cashflows[0] >= 0:
            st.warning(f"Cashflowet i det første år (år {num(years[0],0)}) er ikke negativt. "
                       "År 0 er normalt selve investeringen — penge UD af kassen — og skal "
                       "skrives med minus. Ellers bliver NPV, payback og de kritiske værdier "
                       "misvisende.", icon="⚠️")
        s = ok.investering_summary(cashflows, rente, years)
        irr_findes = s["IRR"] == s["IRR"]
        r_min = max(-0.95, s["IRR"] * 1.2) if (irr_findes and s["IRR"] < 0) else 0.0
        with h:
            rr = np.linspace(r_min, max(0.4, (s["IRR"] if irr_findes else 0.3) * 1.5), 200)
            prof = ok.npv_profile(cashflows, rr, years)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=rr * 100, y=prof, line=dict(color=C_TOTAL, width=3), name="NPV"))
            fig.add_hline(y=0, line_dash="dash", line_color=C_MUTED)
            if irr_findes and rr[0] <= s["IRR"] <= rr[-1]:
                fig.add_vline(x=s["IRR"] * 100, line_dash="dot", line_color=C_OPT)
                fig.add_trace(go.Scatter(x=[s["IRR"] * 100], y=[0], mode="markers+text",
                                         marker=dict(color=C_OPT, size=12),
                                         text=[f"IRR = {pct(s['IRR'])}"], textposition="top center", name="IRR"))
            fig.add_vline(x=rente * 100, line_dash="dot", line_color=C_HOLD,
                          annotation_text=f"Krav {pct(rente,0)}")
            fig.update_layout(xaxis_title="Rente (%)", yaxis_title="Kapitalværdi (kr.)",
                              height=430, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), width="stretch")
            st.caption("Kurven viser investeringens værdi (NPV) ved forskellige renter. Hvor "
                       "kurven er over den stiplede nul-linje, tjener investeringen sig hjem. "
                       "Den krydser nul præcis ved IRR. Ligger dit afkastkrav (Krav-stregen) "
                       "til venstre for IRR-stregen, er investeringen god.")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Kapitalværdi (NPV)", kr(s["NPV"], 0),
                  help="Nutidsværdi af alle cashflows. Positiv = invester.")
        m2.metric("Intern rente (IRR)", pct(s["IRR"]),
                  help="Renten hvor NPV = 0. Højere end kravet = god investering.")
        m3.metric("Tilbagebetalingstid", f"{num(s['payback'],1)} år",
                  help="Antal år før investeringen er tjent ind (risikomål).")
        m4.metric("Kritisk levetid", f"{num(s['kritisk_levetid'],1)} år",
                  help="Mindste levetid før investeringen er tjent hjem (NPV = 0).")

        # --- Kritiske værdier: hvor meget må hver forudsætning skride? ---
        investering = -cashflows[0]
        levetid = years[-1] - years[0]
        k_inv = ok.kritisk_investeringsbeloeb(cashflows, rente, years)
        k_ind = ok.kritisk_aarlig_indbetaling(investering, rente, levetid, scrap_inv)
        ko = ok.kritisk_omsaetning(cashflows, rente, salgspris_stk, db_stk, years)

        st.markdown("**Kritiske værdier** — hvor langt kan forudsætningerne skride, "
                    "før investeringen ikke længere er lønsom (NPV = 0)?")
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Kritisk investeringsbeløb", kr(k_inv, 0),
                  help="Det mest maskinen må koste, før kapitalværdien bliver negativ. "
                       "= investeringen + NPV.")
        k2.metric("Kritisk årlig indbetaling", kr(k_ind, 0) if k_ind == k_ind else "—",
                  help="Den mindste GENNEMSNITLIGE indbetaling pr. år (samme beløb hvert år), "
                       "der lige akkurat tjener investeringen hjem. Scrapværdien fra "
                       "forudsætningerne holdes ude af annuiteten.")
        k3.metric("Kritisk afsætning (år 1)", f"{num(ko['kritisk_stk'],0)} stk." if ko["kritisk_stk"] == ko["kritisk_stk"] else "—",
                  help="Hvor få stk. der må sælges i år 1, før NPV rammer 0 (alle andre år "
                       "holdes fast). Kræver at DB pr. stk. er udfyldt i forudsætningerne.")
        k4.metric("Kritisk omsætning (år 1)", kr(ko["kritisk_omsaetning"], 0) if ko["kritisk_omsaetning"] == ko["kritisk_omsaetning"] else "—",
                  help="Den kritiske afsætning i år 1 omregnet til kroner (stk. · salgspris). "
                       "Kræver at både salgspris og DB pr. stk. er udfyldt i forudsætningerne.")
        if not (salgspris_stk > 0 and db_stk > 0):
            st.caption("Udfyld *Forudsætninger til kritiske værdier* (salgspris og DB pr. stk.) "
                       "i venstre kolonne for at få kritisk afsætning og omsætning i år 1.")

        beslut = "JA, invester" if s["NPV"] > 0 else "NEJ"
        with st.expander("Mellemregninger / beslutning", expanded=True):
            st.markdown(
                f"- NPV ved {pct(rente,0)} = **{kr(s['NPV'],0)}** ({'positiv' if s['NPV']>0 else 'negativ'})\n"
                f"- IRR = **{pct(s['IRR'])}** {'>' if s['IRR']>rente else '<'} kravet {pct(rente,0)}\n"
                f"- **Beslutning: {beslut}** (NPV > 0 og IRR > kalkulationsrente)"
            )
        with st.expander("Mellemregninger — kritiske værdier"):
            faktor = (1 - (1 + rente) ** -levetid) / rente if rente else float(levetid)
            pv_scrap = scrap_inv / (1 + rente) ** levetid if levetid else 0.0
            linjer = [
                f"- Kritisk investeringsbeløb = investering + NPV = {kr(investering,0)} + "
                f"{kr(s['NPV'],0)} = **{kr(k_inv,0)}** — nutidsværdien af alle fremtidige "
                f"indbetalinger, altså det maskinen højst må koste.",
                f"- Annuitetsfaktor ved {pct(rente,0)} og {num(levetid,0)} år = "
                f"(1 − (1+r)⁻ⁿ)/r = {num(faktor,4)}",
                f"- Kritisk årlig indbetaling = (investering − nutidsværdi af scrap) / annuitetsfaktor = "
                f"({kr(investering,0)} − {kr(pv_scrap,0)}) / {num(faktor,4)} = **{kr(k_ind,0)}/år**",
            ]
            if ko["kritisk_stk"] == ko["kritisk_stk"]:
                linjer.append(
                    f"- Kritisk indbetaling i år 1 = cashflow år 1 − NPV·(1+r)^{num(years[1],0)} = "
                    f"{kr(cashflows[1],0)} − {kr(s['NPV'],0)}·{num((1+rente)**years[1],4)} = "
                    f"**{kr(ko['kritisk_indbetaling'],0)}**")
                linjer.append(
                    f"- Kritisk afsætning = indbetaling / DB pr. stk. = {kr(ko['kritisk_indbetaling'],0)} / "
                    f"{kr(db_stk,0)} = **{num(ko['kritisk_stk'],0)} stk.**"
                    + (f" → kritisk omsætning = {num(ko['kritisk_stk'],0)} · {kr(salgspris_stk,0)} = "
                       f"**{kr(ko['kritisk_omsaetning'],0)}**" if ko["kritisk_omsaetning"] == ko["kritisk_omsaetning"] else ""))
            st.markdown("\n".join(linjer))
            st.caption("Husk eksamensfælden: allerede afholdte omkostninger (fx rejseomkostninger "
                       "til at se på maskinen) er *sunk cost* og må IKKE med i kalkulen.")
    else:
        st.info("Indtast mindst år 0 (investering) og ét år med cashflow.")


# ===========================================================================
# BREAK-EVEN / NULPUNKT
# ===========================================================================
with tab_be:
    st.subheader("Break-even / nulpunktsanalyse")
    st.caption("Hvor omsætning og totalomkostninger krydser. Under nulpunktet giver det "
               "underskud, over giver det overskud.")

    v, h = st.columns([1, 2])
    with v:
        pris = st.number_input("Salgspris pr. stk.", min_value=0.01, value=100.0, step=5.0, key="be_pris",
                               help="Den pris du sælger én vare for (uden moms).")
        variabel = st.number_input("Variable omk. pr. stk.", min_value=0.0, value=60.0, step=5.0, key="be_var",
                                   help="De omkostninger der følger med hver vare, fx indkøb og fragt "
                                        "af selve varen. Stiger når du sælger mere.")
        faste = st.number_input("Faste omkostninger (kr.)", min_value=0.0, value=8000.0, step=500.0, key="be_faste",
                                help="Omkostninger du har uanset hvor meget du sælger, fx husleje og "
                                     "løn. Ændrer sig ikke pr. solgt vare.")
        akt_q = st.number_input("Aktuel afsætning (stk., til sikkerhedsmargin)", min_value=0.0,
                                value=250.0, step=10.0, key="be_q",
                                help="Hvor mange stk. du faktisk sælger (eller forventer at sælge). "
                                     "Bruges kun til at beregne hvor stor en sikkerhedsmargin du har "
                                     "op til nulpunktet.")

    r = ok.break_even(pris, variabel, faste)
    q_be = r["nulpunktsmaengde"]

    with h:
        if q_be == q_be:
            q = np.linspace(0, max(q_be * 2, akt_q * 1.2, 1), 200)
            oms = pris * q
            tot = faste + variabel * q
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=q, y=oms, name="Omsætning", line=dict(color=C_HOLD, width=3)))
            fig.add_trace(go.Scatter(x=q, y=tot, name="Totalomkostninger", line=dict(color=C_OPT, width=3)))
            fig.add_trace(go.Scatter(x=q, y=[faste] * len(q), name="Faste omk.",
                                     line=dict(color=C_MUTED, dash="dot")))
            fig.add_vline(x=q_be, line_dash="dash", line_color=C_TOTAL)
            fig.add_trace(go.Scatter(x=[q_be], y=[pris * q_be], mode="markers+text",
                                     marker=dict(color=C_TOTAL, size=12),
                                     text=[f"Nulpunkt {num(q_be,0)}"], textposition="top center", name="Break-even"))
            fig.update_layout(xaxis_title="Afsætning (stk.)", yaxis_title="Kr.", height=430,
                              margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), width="stretch")
            st.caption("De to linjer krydser i nulpunktet. Til venstre for krydset er "
                       "omkostningerne større end omsætningen, som betyder underskud. Til "
                       "højre tjener du penge. Jo længere til højre din aktuelle afsætning "
                       "ligger, jo mere sikker er du.")
        else:
            st.error("Variable omk. pr. stk. skal være lavere end salgsprisen.")

    sm = ok.safety_margin(akt_q * pris, r["nulpunktsomsaetning"])
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("DB pr. stk.", kr(r["db_stk"], 0), help="Salgspris − variable omk.")
    m2.metric("Dækningsgrad", pct(r["daekningsgrad"]), help="DB / salgspris.")
    m3.metric("Nulpunktsmængde", f"{num(q_be,0)} stk.", help="Faste omk. / DB pr. stk.")
    m4.metric("Sikkerhedsmargin", pct(sm), help="Hvor langt over nulpunktet den aktuelle afsætning ligger.")
    with st.expander("Mellemregninger / formel", expanded=True):
        st.markdown(
            f"- DB/stk = {num(pris,0)} − {num(variabel,0)} = **{kr(r['db_stk'],0)}** · "
            f"DG = {pct(r['daekningsgrad'])}\n"
            f"- Nulpunktsmængde = faste/DB = {num(faste,0)}/{num(r['db_stk'],0)} = **{num(q_be,0)} stk.**\n"
            f"- Nulpunktsomsætning = {kr(r['nulpunktsomsaetning'],0)} · "
            f"sikkerhedsmargin = {pct(sm)}"
        )


# ===========================================================================
# PRISKALKULATION
# ===========================================================================
with tab_kalk:
    st.subheader("Priskalkulation")
    st.caption("Tre metoder: bidrag (fremad fra kostpris), fordeling (med andel af faste "
               "omk.), retrograd (baglæns fra markedspris til maks. købspris).")

    metode = st.radio("Metode", ["Bidragskalkulation", "Fordelingskalkulation", "Retrograd kalkulation"],
                      horizontal=True, key="kalk_metode")

    if metode == "Bidragskalkulation":
        c = st.columns(2)
        kostpris = c[0].number_input("Kostpris (indkøb + hjemtagelse)", min_value=0.0, value=100.0, step=5.0, key="bk_kost",
                                     help="Hvad varen koster dig at få ind: indkøbsprisen plus fragt, "
                                          "told og andre udgifter ved at få varen hjem til lageret.")
        dg = c[1].slider("Ønsket dækningsgrad (%)", 1, 95, 75, key="bk_dg",
                         help="Hvor stor en del af salgsprisen der skal være tilbage til at dække "
                              "faste omkostninger og overskud, efter de variable omkostninger er "
                              "trukket fra. Sætter du den højere, fører det til en højere salgspris.") / 100
        r = ok.bidragskalkulation(kostpris, dg)
        m1, m2, m3 = st.columns(3)
        m1.metric("Kostpris", kr(kostpris, 0))
        m2.metric("Dækningsbidrag", kr(r["db"], 0), help="DB = kostpris · DG/(1−DG).")
        m3.metric("Salgspris (ekskl. moms)", kr(r["salgspris"], 0))
        st.caption(f"DB = {num(kostpris,0)} · {pct(dg,0)}/(1−{pct(dg,0)}) = {kr(r['db'],0)}; "
                   f"salgspris = kostpris + DB = {kr(r['salgspris'],0)}. Kontrol: DB/salgspris = {pct(r['db']/r['salgspris'])}.")

    elif metode == "Fordelingskalkulation":
        c = st.columns(2)
        var_e = c[0].number_input("Variable enhedsomk.", min_value=0.0, value=40.0, step=5.0, key="fk_var",
                                  help="Hvad det koster at lave eller håndtere én vare.")
        faste = c[1].number_input("Faste (kapacitets-)omkostninger", min_value=0.0, value=200000.0, step=10000.0, key="fk_faste",
                                  help="De samlede faste omkostninger ved at have kapaciteten klar, fx "
                                       "maskiner og husleje, uanset hvor meget du producerer.")
        c2 = st.columns(2)
        kapacitet = c2[0].number_input("Kapacitet (stk.)", min_value=1.0, value=10000.0, step=500.0, key="fk_kap",
                                       help="Hvor mange stk. du højst kan lave.")
        udnyt = c2[1].slider("Udnyttelse (%)", 1, 100, 80, key="fk_udn",
                             help="Hvor stor en del af kapaciteten du reelt bruger. Lav udnyttelse "
                                  "betyder at de faste omkostninger fordeles på færre stk., som fører "
                                  "til en højere pris pr. stk.") / 100
        fortj = st.slider("Ønsket fortjeneste (% af salgsprisen)", 1, 95, 40, key="fk_dg",
                          help="Den avance der lægges oven på egenprisen, målt som andel af "
                               "salgsprisen. OBS: det er IKKE det samme som dækningsgraden — "
                               "egenprisen indeholder allerede en andel af de faste omkostninger, "
                               "så den faktiske dækningsgrad bliver HØJERE end fortjenesteprocenten. "
                               "Værktøjet viser den faktiske DG som kontrol nedenfor.") / 100
        r = ok.fordelingskalkulation(var_e, faste, kapacitet, udnyt, fortj)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Andel af kapacitetsomk.", kr(r["andel_kapacitetsomk"], 2), help="Faste / (kapacitet · udnyttelse).")
        m2.metric("Egenpris", kr(r["egenpris"], 2), help="Variabel enhedsomk. + andel af faste omk.")
        m3.metric("Fortjeneste (avance)", kr(r["avance"], 2),
                  help="Egenpris · fortjeneste/(1 − fortjeneste), så avancen udgør præcis den "
                       "valgte andel af salgsprisen.")
        m4.metric("Salgspris", kr(r["salgspris"], 2))
        st.caption(f"Kontrol: den FAKTISKE dækningsgrad = (salgspris − variable omk.)/salgspris = "
                   f"{pct(r['faktisk_dg'])} — højere end fortjenesten på {pct(fortj,0)}, fordi "
                   f"egenprisen allerede indeholder en andel af de faste omkostninger. Bland aldrig "
                   f"de to begreber sammen til eksamen.")
        st.caption("Forskellige fordelingsnøgler (omsætning/timer/ABC) kan vende rentabiliteten "
                   "— vis altid nøglen. Her: faste/(kapacitet·udnyttelse).")

    else:
        c = st.columns(2)
        salgspris = c[0].number_input("Markedspris (maks. salgspris)", min_value=0.0, value=500.0, step=10.0, key="rk_pris",
                                      help="Den pris markedet vil betale, og som du regner baglæns ud fra.")
        dg = c[1].slider("Ønsket dækningsgrad (%)", 1, 95, 40, key="rk_dg",
                         help="Hvor stor en del af salgsprisen der skal være tilbage til at dække faste "
                              "omkostninger og overskud. I retrograd kalkulation ligger salgsprisen "
                              "FAST (markedsprisen) — sætter du dækningsgraden højere, bliver der "
                              "mindre tilbage til at købe varen for, så den maksimale købspris "
                              "bliver LAVERE.") / 100
        c2 = st.columns(2)
        var_salg = c2[0].number_input("Variable salgsomk.", min_value=0.0, value=20.0, step=5.0, key="rk_var",
                                      help="Udgifter direkte knyttet til salget, fx provision eller forsendelse.")
        told = c2[1].slider("Told (% af købspris)", 0, 30, 10, key="rk_told",
                            help="En procentdel oven i det varen koster hos leverandøren, som du skal "
                                 "trække fra for at finde den højeste pris du må give for varen.") / 100
        r = ok.retrograd_kalkulation(salgspris, dg, var_salg, told)
        m1, m2, m3 = st.columns(3)
        m1.metric("Dækningsbidrag", kr(r["db"], 0), help="Salgspris · DG.")
        m2.metric("Told", kr(r["told"], 0))
        m3.metric("Maks. købspris", kr(r["maks_koebspris"], 2), help="Det varen højst må koste hos leverandøren.")
        st.caption("Bruges til leverandørforhandling: hvor meget må varen koste, for at du stadig "
                   "rammer din dækningsgrad ved den givne markedspris?")


# ===========================================================================
# PRISOPTIMERING (monopol)
# ===========================================================================
with tab_opt:
    st.subheader("Prisoptimering under monopol")
    st.caption("Find den pris/afsætning der giver størst overskud (totalmetoden), "
               "eller hvor grænseomsætning = grænseomkostning (grænsemetoden).")

    c = st.columns(2)
    var_e = c[0].number_input("Variable enhedsomk. (VE)", min_value=0.0, value=40.0, step=5.0, key="opt_ve",
                              help="Variable enhedsomkostninger (VE): hvad én vare koster at lave. "
                                   "Trækkes fra omsætningen for at finde overskuddet.")
    faste = c[1].number_input("Faste omkostninger (FO)", min_value=0.0, value=500.0, step=100.0, key="opt_fo",
                              help="Faste omkostninger (FO): de omkostninger du har uanset hvor meget "
                                   "du sælger. Trækkes fra omsætningen for at finde overskuddet.")
    default_opt = pd.DataFrame({
        "Pris": [100, 90, 80, 70, 60, 50],
        "Afsætning": [10, 20, 30, 40, 50, 60],
    })
    st.caption("Hver række er en mulig salgspris og den mængde du forventer at sælge ved netop "
               "den pris. Sætter du prisen ned, sælger du typisk flere stk. Værktøjet finder den "
               "kombination der giver størst overskud.")
    odf = st.data_editor(default_opt, num_rows="dynamic", hide_index=True,
                         width="stretch", key="opt_data")
    odf = odf.copy()
    odf["Pris"] = pd.to_numeric(odf["Pris"], errors="coerce")
    odf["Afsætning"] = pd.to_numeric(odf["Afsætning"], errors="coerce")
    odf = odf.dropna()

    if len(odf) >= 2:
        r = ok.prisoptimering(odf["Pris"].tolist(), odf["Afsætning"].tolist(), var_e, faste)
        q = odf["Afsætning"].tolist()
        c1, c2 = st.columns(2)
        with c1:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=q, y=r["overskud"], mode="lines+markers", name="Overskud",
                                     line=dict(color=C_TOTAL, width=3)))
            fig.add_trace(go.Scatter(x=[r["optimal_afsaetning"]], y=[r["max_overskud"]], mode="markers+text",
                                     marker=dict(color=C_OPT, size=13),
                                     text=[f"Maks {kr(r['max_overskud'],0)}"], textposition="top center", name="Optimum"))
            fig.update_layout(title="Totalmetoden (overskud)", xaxis_title="Afsætning", yaxis_title="Overskud (kr.)",
                              height=360, margin=dict(t=40, b=10), showlegend=False)
            st.plotly_chart(style_fig(fig), width="stretch")
        with c2:
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=q, y=r["graenseomsaetning"], mode="lines+markers",
                                      name="Grænseomsætning", line=dict(color=C_HOLD)))
            fig2.add_trace(go.Scatter(x=q, y=r["graenseomkostning"], mode="lines+markers",
                                      name="Grænseomkostning", line=dict(color=C_ORDER)))
            fig2.update_layout(title="Grænsemetoden", xaxis_title="Afsætning", yaxis_title="Kr. pr. enhed",
                               height=360, margin=dict(t=40, b=10), legend=dict(orientation="h", y=1.15))
            st.plotly_chart(style_fig(fig2), width="stretch")
            st.caption("Grænseomsætning er hvad den næste solgte vare giver ekstra i indtægt. "
                       "Grænseomkostning er hvad den næste vare koster ekstra at lave. Så længe "
                       "den ekstra indtægt er større end den ekstra omkostning, kan det betale "
                       "sig at sælge mere. Det optimale punkt er hvor de to kurver krydser.")

        m1, m2, m3 = st.columns(3)
        m1.metric("Optimal pris", kr(r["optimal_pris"], 0))
        m2.metric("Optimal afsætning", f"{num(r['optimal_afsaetning'],0)} stk.")
        m3.metric("Maks. overskud", kr(r["max_overskud"], 0))
        st.caption("De to metoder giver samme optimum: størst overskud er der, hvor "
                   "grænseomsætning og grænseomkostning krydser hinanden.")


# ===========================================================================
# NØGLETALSANALYSE
# ===========================================================================
with tab_nt:
    st.subheader("Nøgletalsanalyse")
    st.caption("Indtast tal fra resultatopgørelse og balance. Ét år (År 1) er nok — udfylder du "
               "også År 2 og År 3, viser værktøjet udviklingen med indekstal og retning, som "
               "eksamensopgaver i regnskabsanalyse næsten altid spørger til.")

    NT_POSTER = ["Omsætning", "Driftsresultat (EBIT)", "Årets resultat", "Renteomkostninger",
                 "Bruttofortjeneste (valgfri)", "Aktiver i alt", "heraf omsætningsaktiver",
                 "Egenkapital", "Gæld i alt (fremmedkapital)", "heraf kortfristet gæld"]
    default_nt = pd.DataFrame({
        "Post": NT_POSTER,
        "År 1": [1000000.0, 100000.0, 60000.0, 20000.0, 400000.0,
                 800000.0, 300000.0, 400000.0, 400000.0, 150000.0],
        "År 2": [float("nan")] * len(NT_POSTER),
        "År 3": [float("nan")] * len(NT_POSTER),
    })
    ntdf = st.data_editor(
        default_nt, hide_index=True, width="stretch", key="nt_data", height=390,
        column_config={
            "Post": st.column_config.TextColumn("Post", disabled=True,
                                                help="Regnskabsposten. Se forklaringerne i "
                                                     "'Hvad betyder posterne?' nedenfor."),
            "År 1": st.column_config.NumberColumn(
                "År 1", help="Det ældste regnskabsår. Skal altid være udfyldt — det er "
                             "basisåret (indeks 100), som udviklingen måles fra."),
            "År 2": st.column_config.NumberColumn(
                "År 2 (valgfri)", help="Næste regnskabsår. Lad kolonnen stå tom, hvis du kun "
                                       "analyserer ét år."),
            "År 3": st.column_config.NumberColumn(
                "År 3 (valgfri)", help="Det nyeste regnskabsår. Lad kolonnen stå tom, hvis du "
                                       "ikke har tre år."),
        })
    with st.expander("Hvad betyder posterne?"):
        st.markdown(
            "- **Driftsresultat (EBIT):** overskuddet fra selve driften, før renter og skat. "
            "Står ofte som driftsresultat i regnskabet.\n"
            "- **Bruttofortjeneste:** omsætning minus vareforbrug. Bruges kun til "
            "bruttoavanceprocenten — kan stå tom.\n"
            "- **Aktiver i alt:** summen af anlægs- og omsætningsaktiver (det virksomheden ejer).\n"
            "- **heraf omsætningsaktiver:** likvider, varelager, debitorer — bliver til penge "
            "inden for et år.\n"
            "- **Egenkapital:** ejernes andel (aktiver minus gæld).\n"
            "- **heraf kortfristet gæld:** gæld der forfalder inden for et år.")

    # Et år tæller som udfyldt, når omsætningen (første række) er indtastet og > 0
    aars = []  # liste af (kolonnenavn, nøgletals-dict, rå tal-dict)
    for kol in ["År 1", "År 2", "År 3"]:
        v = pd.to_numeric(ntdf[kol], errors="coerce").tolist()
        if len(v) < len(NT_POSTER) or not (v[0] == v[0] and v[0] > 0):
            continue
        tal = {p: (x if x == x else 0.0) for p, x in zip(NT_POSTER, v)}
        brutto = tal["Bruttofortjeneste (valgfri)"] or None
        rn = ok.noegletal(tal["Omsætning"], tal["Driftsresultat (EBIT)"], tal["Årets resultat"],
                          tal["Renteomkostninger"], tal["Aktiver i alt"], tal["Egenkapital"],
                          tal["Gæld i alt (fremmedkapital)"], tal["heraf omsætningsaktiver"],
                          tal["heraf kortfristet gæld"], brutto)
        aars.append((kol, rn, tal))

    if not aars:
        st.info("Udfyld mindst År 1 — omsætningen skal være større end 0.")
    else:
        skaeve = []
        for navn_a, _, tal_a in aars:
            pas = tal_a["Egenkapital"] + tal_a["Gæld i alt (fremmedkapital)"]
            if abs(pas - tal_a["Aktiver i alt"]) > 1:
                skaeve.append(f"{navn_a}: passiver {kr(pas,0)} ≠ aktiver {kr(tal_a['Aktiver i alt'],0)}")
        if skaeve:
            st.warning("Balancen stemmer ikke (egenkapital + gæld skal være lig aktiver) — "
                       + " · ".join(skaeve), icon="⚖️")
        else:
            st.caption("Balancen stemmer i alle udfyldte år: passiver = egenkapital + gæld = aktiver.")

        navn, r, tal = aars[-1]  # nyeste udfyldte år
        if len(aars) > 1:
            st.markdown(f"**Nøgletal for {navn}** (nyeste udfyldte år — udviklingen står nedenfor)")

        st.markdown("**Rentabilitet**")
        m = st.columns(5)
        m[0].metric("Afkastningsgrad", pct(r["afkastningsgrad"]), help="EBIT / aktiver. = overskudsgrad × AOH.")
        m[1].metric("Overskudsgrad", pct(r["overskudsgrad"]), help="EBIT / omsætning.")
        m[2].metric("Aktivernes omsætningshast.", num(r["aoh"], 2), help="Omsætning / aktiver (gange pr. år).")
        m[3].metric("Egenkapitalforrentning", pct(r["egenkapitalforrentning"]), help="Årets resultat / egenkapital.")
        m[4].metric("Fremmedkapitalforrentning", pct(r["fremmedkapitalforrentning"]),
                    help="Renteomkostninger / gæld: den gennemsnitlige rente virksomheden betaler "
                         "på sin fremmedkapital. Sammenlign med afkastningsgraden — se "
                         "gearing-fordelen nedenfor.")

        st.markdown("**Soliditet og likviditet**")
        m2 = st.columns(4)
        m2[0].metric("Soliditetsgrad", pct(r["soliditetsgrad"]), help="Egenkapital / aktiver. Robusthed.")
        m2[1].metric("Likviditetsgrad", pct(r["likviditetsgrad"]), help="Omsætningsaktiver / kortfristet gæld. Bør > 100 %.")
        m2[2].metric("Gearing", num(r["gearing"], 2),
                     help="Gæld i forhold til egenkapital. Et højt tal betyder at virksomheden er "
                          "finansieret meget med lån, som fører til større risiko.")
        m2[3].metric("Bruttoavanceprocent", pct(r["bruttoavanceprocent"]), help="Bruttofortjeneste / omsætning.")

        with st.expander("DuPont-sammenhæng og gearing-fordelen", expanded=True):
            ag, fkf = r["afkastningsgrad"], r["fremmedkapitalforrentning"]
            if ag == ag and fkf == fkf:
                gearing_ord = ("afkastningsgraden er HØJERE end lånerenten (AG > FKF), så hver lånt "
                               "krone tjener mere end den koster — gælden gearer egenkapitalens "
                               "forrentning OP." if ag > fkf else
                               "afkastningsgraden er LAVERE end lånerenten (AG < FKF), så lånte "
                               "penge koster mere end de tjener — gælden trækker egenkapitalens "
                               "forrentning NED.")
            else:
                gearing_ord = "udfyld renteomkostninger og gæld for at se gearing-fordelen."
            st.markdown(
                f"- **Afkastningsgrad = Overskudsgrad × AOH** = {pct(r['overskudsgrad'])} × "
                f"{num(r['aoh'],2)} = **{pct(r['afkastningsgrad'])}**\n"
                "- Du kan altså forbedre afkastningsgraden enten ved højere indtjening pr. krone "
                "(overskudsgrad) eller ved at omsætte aktiverne hurtigere (AOH).\n"
                f"- **Gearing-fordelen: EKF (før skat) = AG + (AG − FKF) · gæld/EK** = "
                f"{pct(ag)} + ({pct(ag)} − {pct(fkf)}) · {num(r['gearing'],2)} = "
                f"**{pct(r['ekf_foer_skat'])}**\n"
                f"- I ord: {gearing_ord}"
            )
            st.caption("Identiteten gælder, når balancen stemmer (aktiver = egenkapital + gæld). "
                       "EKF før skat = (EBIT − renter)/egenkapital. Egenkapitalforrentningen i "
                       "metricen ovenfor bruger årets resultat (efter skat) og er derfor lavere.")

        if len(aars) >= 2:
            st.markdown("**Udvikling over årene**")
            NT_VIS = [("Afkastningsgrad", "afkastningsgrad", "pct"),
                      ("Overskudsgrad", "overskudsgrad", "pct"),
                      ("Aktivernes omsætningshast.", "aoh", "tal"),
                      ("Egenkapitalforrentning", "egenkapitalforrentning", "pct"),
                      ("Fremmedkapitalforrentning", "fremmedkapitalforrentning", "pct"),
                      ("Soliditetsgrad", "soliditetsgrad", "pct"),
                      ("Likviditetsgrad", "likviditetsgrad", "pct"),
                      ("Gearing", "gearing", "tal"),
                      ("Bruttoavanceprocent", "bruttoavanceprocent", "pct")]
            udv_rows = []
            for label, key, fmt in NT_VIS:
                vals = [a[1][key] for a in aars]
                idx = ok.indekstal(vals)
                sidste_idx = idx[-1]
                if sidste_idx != sidste_idx:
                    retning = "—"
                elif sidste_idx > 100.5:
                    retning = "▲ stiger"
                elif sidste_idx < 99.5:
                    retning = "▼ falder"
                else:
                    retning = "→ uændret"
                row = {"Nøgletal": label}
                for (navn_a, ra, _), v in zip(aars, vals):
                    row[navn_a] = pct(v) if fmt == "pct" else num(v, 2)
                row["Indeks (sidste år)"] = num(sidste_idx, 0) if sidste_idx == sidste_idx else "—"
                row["Retning"] = retning
                udv_rows.append(row)
            st.dataframe(pd.DataFrame(udv_rows), hide_index=True, width="stretch")
            st.caption("Indeks: første udfyldte år = 100, så indeks 120 betyder at nøgletallet er "
                       "steget 20 % siden basisåret. Til eksamen: nævn retningen OG forklar "
                       "hvorfor den er som den er (fx faldende overskudsgrad = omkostningerne "
                       "vokser hurtigere end omsætningen).")

            fig_nt = go.Figure()
            x_aar = [a[0] for a in aars]
            for label, key, farve in [("Afkastningsgrad", "afkastningsgrad", C_TOTAL),
                                      ("Overskudsgrad", "overskudsgrad", C_ORDER),
                                      ("Egenkapitalforrentning", "egenkapitalforrentning", C_HOLD),
                                      ("Fremmedkapitalforrentning", "fremmedkapitalforrentning", C_OPT)]:
                ys_nt = [a[1][key] * 100 for a in aars]
                fig_nt.add_trace(go.Scatter(x=x_aar, y=ys_nt, mode="lines+markers",
                                            name=label, line=dict(color=farve, width=3)))
            fig_nt.update_layout(yaxis_title="%", height=340, margin=dict(t=30, b=10),
                                 title="Rentabilitetens udvikling",
                                 legend=dict(orientation="h", y=1.18))
            st.plotly_chart(style_fig(fig_nt), width="stretch")
            st.caption("Ligger afkastningsgraden (blå) over fremmedkapitalforrentningen (rød), "
                       "tjener virksomheden på sine lånte penge i det år.")


# ===========================================================================
# BUDGET (resultatbudget + afskrivning + simpel likviditet)
# ===========================================================================
with tab_bud:
    st.subheader("Budget")
    st.caption("Overordnet resultatbudget pr. kvartal, lineær afskrivning og en simpel "
               "likviditetsoversigt. Ret tallene i tabellen, så opdateres alt live.")

    with st.expander("Lineær afskrivning (hjælper)", expanded=False):
        c = st.columns(3)
        nypris = c[0].number_input("Nypris", min_value=0.0, value=120000.0, step=5000.0, key="bud_ny")
        scrap = c[1].number_input("Scrapværdi", min_value=0.0, value=20000.0, step=1000.0, key="bud_scrap")
        levetid = c[2].number_input("Levetid (år)", min_value=1.0, value=5.0, step=1.0, key="bud_lev")
        a = ok.lineaer_afskrivning(nypris, scrap, levetid)
        st.markdown(f"Årlig afskrivning = (nypris − scrap)/levetid = "
                    f"({num(nypris,0)} − {num(scrap,0)})/{num(levetid,0)} = **{kr(a['aarlig'],0)}/år** "
                    f"({kr(a['kvartal'],0)}/kvartal). Indsæt den i budgettet nedenfor.")

    perioder = ["Q1", "Q2", "Q3", "Q4"]
    default_bud = pd.DataFrame({
        "Post": ["Omsætning", "Vareforbrug", "Løn", "Husleje", "Markedsføring", "Afskrivning"],
        "Type": ["Indtægt", "Omkostning", "Omkostning", "Omkostning", "Omkostning", "Omkostning"],
        "Q1": [250000.0, 100000, 60000, 20000, 15000, 5000],
        "Q2": [260000.0, 104000, 60000, 20000, 15000, 5000],
        "Q3": [240000.0, 96000, 60000, 20000, 12000, 5000],
        "Q4": [300000.0, 120000, 65000, 20000, 20000, 5000],
    })
    bdf = st.data_editor(
        default_bud, num_rows="dynamic", hide_index=True, width="stretch", key="bud_data",
        column_config={"Type": st.column_config.SelectboxColumn("Type", options=["Indtægt", "Omkostning"])})

    bdf = bdf.copy()
    for q in perioder:
        bdf[q] = pd.to_numeric(bdf[q], errors="coerce").fillna(0)

    ind = bdf[bdf["Type"] == "Indtægt"]
    omk = bdf[bdf["Type"] == "Omkostning"]
    resultat = [ind[q].sum() - omk[q].sum() for q in perioder]
    aar = sum(resultat)

    fig = go.Figure(go.Bar(x=perioder, y=resultat,
                           marker_color=[C_HOLD if r >= 0 else C_OPT for r in resultat],
                           text=[kr(r, 0) for r in resultat], textposition="outside"))
    fig.update_layout(yaxis_title="Resultat (kr.)", height=340, margin=dict(t=30, b=10),
                      title="Resultatbudget pr. kvartal")
    st.plotly_chart(style_fig(fig), width="stretch")
    st.caption("Hver søjle er kvartalets resultat (indtægter minus omkostninger). En søjle over "
               "nul betyder overskud i kvartalet; en søjle under nul (rød) betyder underskud.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Indtægter (år)", kr(sum(ind[q].sum() for q in perioder), 0))
    m2.metric("Omkostninger (år)", kr(sum(omk[q].sum() for q in perioder), 0))
    m3.metric("Årets resultat", kr(aar, 0), help="Indtægter minus omkostninger for hele året.")

    st.markdown("**Simpel likviditet** (kassebevægelse = periodens resultat + afskrivninger)")
    primo = st.number_input("Kassebeholdning primo (start)", value=50000.0, step=10000.0, key="bud_primo",
                            help="De penge der er i kassen ved årets/periodens start, før kvartalernes "
                                 "bevægelser lægges til.")
    # Afskrivninger er en omkostning i resultatet, men IKKE penge ud af kassen —
    # de lægges tilbage, ellers ser likviditeten kunstigt dårlig ud.
    afskriv_mask = (bdf["Type"] == "Omkostning") & bdf["Post"].astype(str).str.lower().str.contains("afskriv")
    afskr = [bdf[afskriv_mask][q].sum() for q in perioder]
    saldo = primo
    rows = []
    ultimos = []
    for q, res_q, af_q in zip(perioder, resultat, afskr):
        bev = res_q + af_q
        ultimo = saldo + bev
        ultimos.append(ultimo)
        rows.append({"Periode": q, "Primo": kr(saldo, 0), "Resultat": kr(res_q, 0),
                     "Afskrivninger lagt tilbage": "+" + kr(af_q, 0),
                     "Kassebevægelse": kr(bev, 0), "Ultimo": kr(ultimo, 0)})
        saldo = ultimo
    st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch")
    st.caption("Primo er kassen ved kvartalets start, Kassebevægelse er kvartalets resultat plus "
               "afskrivningerne, og Ultimo er kassen ved kvartalets slut. Ultimo bliver primo i "
               "næste kvartal. Bliver Ultimo negativ, mangler der penge i kassen.")
    st.caption("⚠️ Klassisk eksamensfælde: afskrivninger er en omkostning i resultatbudgettet, men "
               "de er IKKE penge ud af kassen — pengene forlod kassen dengang maskinen blev købt. "
               "Derfor lægges afskrivningerne tilbage, når resultatet oversættes til likviditet. "
               "Rækker med 'afskriv' i navnet findes automatisk.")
    if any(u < 0 for u in ultimos):
        st.warning("Kassebeholdningen bliver negativ i en periode — der mangler likviditet.", icon="⚠️")
    st.caption("Forenklet: et rigtigt likviditetsbudget justerer også for moms, kredittid og "
               "investeringer, der betales når de sker (ikke når de bogføres).")
