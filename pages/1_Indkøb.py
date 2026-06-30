"""Indkøb — regnemaskiner med dynamiske grafer.

Moduler: EOQ · Make-vs-buy/TCA · ABC/Pareto · Genbestillingspunkt + sikkerheds-
lager · POQ/EPQ. Notation matcher brugerens eget kursusmateriale.
"""
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import indkoeb as ik  # noqa: E402
from ui_theme import (  # noqa: E402
    inject_css, style_fig,
    C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_A, C_B, C_C, C_MUTED,
)

st.set_page_config(page_title="Indkøb", page_icon="🛒", layout="wide")
inject_css()


# --- Danske talformater ----------------------------------------------------
def num(x, dec=0):
    """Tal med dansk format: punktum som tusindtalsskiller, komma som decimal."""
    if x is None or (isinstance(x, float) and (np.isnan(x) or np.isinf(x))):
        return "—"
    s = f"{x:,.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def kr(x, dec=0):
    return num(x, dec) + " kr."


st.title("🛒 Indkøb")
st.caption(
    "Regnemaskiner med live-grafer. Tast ind eller træk i skyderne — "
    "graf og mellemregninger opdateres med det samme."
)

tab_eoq, tab_poq, tab_rop, tab_abc, tab_fc, tab_review, tab_mvb, tab_lev, tab_strat = st.tabs([
    "EOQ", "POQ / EPQ", "Genbestilling + SS", "ABC / Pareto",
    "Forecasting", "Review-systemer", "Make-vs-buy / TCO",
    "Leverandørscore", "Strategi & modeller",
])


# ===========================================================================
# EOQ
# ===========================================================================
with tab_eoq:
    st.subheader("EOQ — optimal ordrestørrelse")
    st.caption("Den ordrestørrelse hvor bestillings- og lageromkostninger er mindst tilsammen. "
               "Også kaldet **Wilsons formel**. (Mængderabat indgår ikke i Wilson og vurderes separat.)")

    venstre, hoejre = st.columns([1, 2])
    with venstre:
        D = st.number_input("Efterspørgsel D (stk./år)", min_value=1.0,
                            value=7800.0, step=100.0, key="eoq_D",
                            help="Årsforbrug: hvor mange stk. du bruger/sælger på et år.")
        S = st.number_input("Ordreomkostning S (kr./ordre)", min_value=0.01,
                            value=450.0, step=10.0, key="eoq_S",
                            help="Hvad det koster at afgive én ordre (adm., håndtering, opstart), "
                                 "uafhængigt af mængden. Kaldes også opstillingsomkostning.")

        h_mode = st.radio(
            "Lageromkostning H", ["Fra pris × lagerrente", "Direkte"],
            horizontal=True, key="eoq_hmode",
            help="H = hvad det koster at have én vare på lager i ét år "
                 "(renter på bunden kapital + plads, forsikring, svind). "
                 "Vælg 'Fra pris × lagerrente' for at beregne H som en procent "
                 "af varens værdi, eller 'Direkte' hvis opgaven allerede giver H i kr.",
        )
        if h_mode == "Fra pris × lagerrente":
            pris = st.number_input("Enhedspris (kr./stk.)", min_value=0.01,
                                   value=148.0, step=1.0, key="eoq_pris")
            rente = st.slider(
                "Lagerrente (%)", 1, 60, 18, key="eoq_rente",
                help="Lageromkostningen udtrykt som procent af varens værdi pr. år. "
                     "Fx 18 % = det koster 18 % af prisen at have varen på lager i et år.",
            ) / 100
            H = ik.holding_cost_per_unit(pris, rente)
            st.caption(f"H = {num(pris,2)} × {num(rente*100,0)} % = **{kr(H,2)}/stk./år**")
        else:
            H = st.number_input("Lageromkostning H (kr./stk./år)", min_value=0.01,
                                value=26.64, step=0.5, key="eoq_H",
                                help="Lageromkostning pr. enhed pr. år, direkte i kroner.")

        vis_nuvaerende = st.checkbox("Sammenlign med nuværende ordrestørrelse",
                                     key="eoq_cmp",
                                     help="Sæt flueben hvis du vil se hvor meget du kan spare "
                                          "ved at skifte fra din nuværende bestillingsmængde "
                                          "til den optimale.")
        Q_cur = None
        if vis_nuvaerende:
            Q_cur = st.number_input("Nuværende ordrestørrelse (stk.)",
                                    min_value=1.0, value=650.0, step=50.0, key="eoq_Qcur",
                                    help="Hvor mange stk. du bestiller pr. gang i dag.")

    s = ik.eoq_summary(D, S, H)
    q_star = s["EOQ"]

    with hoejre:
        # Totalomkostningskurven (U-form)
        q_grid = np.linspace(max(1, q_star * 0.15), q_star * 2.6, 400)
        cur = ik.eoq_curve(D, S, H, q_grid)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=cur["Q"], y=cur["ordreomkostning"],
                                 name="Bestillingsomkostning", line=dict(color=C_ORDER)))
        fig.add_trace(go.Scatter(x=cur["Q"], y=cur["lageromkostning"],
                                 name="Lageromkostning", line=dict(color=C_HOLD)))
        fig.add_trace(go.Scatter(x=cur["Q"], y=cur["total"],
                                 name="Total", line=dict(color=C_TOTAL, width=3)))
        fig.add_vline(x=q_star, line_dash="dash", line_color=C_OPT)
        fig.add_trace(go.Scatter(x=[q_star], y=[s["total"]], mode="markers+text",
                                 marker=dict(color=C_OPT, size=12),
                                 text=[f"EOQ = {num(q_star,0)}"], textposition="top center",
                                 name="Optimum"))
        fig.update_layout(
            xaxis_title="Ordrestørrelse Q (stk.)", yaxis_title="Omkostning (kr./år)",
            height=430, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12),
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption(
            "Sådan læser du grafen: den blå totalkurve er summen af de to andre. "
            "Bestillingsomkostningen falder når du bestiller mere ad gangen, mens "
            "lageromkostningen stiger. Det laveste punkt på totalkurven (den stiplede "
            "streg) er EOQ, som betyder den billigste ordrestørrelse."
        )

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("EOQ", f"{num(q_star,0)} stk.",
              help="Den optimale ordrestørrelse: hvor mange stk. du bør bestille pr. gang.")
    m2.metric("Antal ordrer/år", num(s["antal_ordrer"], 1),
              help="Hvor mange gange om året du bestiller (D delt med EOQ).")
    m3.metric("Cyklustid", f"{num(s['cyklustid_dage'],0)} dage",
              help="Antal dage mellem to bestillinger.")
    m4.metric("Total omkostning", kr(s["total"], 0),
              help="Bestillings- + lageromkostninger pr. år ved EOQ (ekskl. selve varekøbet).")

    with st.expander("Mellemregninger / formel", expanded=True):
        st.latex(r"EOQ = \sqrt{\dfrac{2 \cdot D \cdot S}{H}}")
        st.markdown(
            f"- EOQ = √(2 · {num(D,0)} · {num(S,0)} / {num(H,2)}) = **{num(q_star,1)} stk.**\n"
            f"- Bestillingsomkostning = (D/EOQ)·S = {kr(s['ordreomkostning'],0)}\n"
            f"- Lageromkostning = (EOQ/2)·H = {kr(s['lageromkostning'],0)}\n"
            f"- **Total = {kr(s['total'],0)}/år** (ved optimum er de to lige store)"
        )
        if Q_cur:
            cur_cost = ik.current_policy_cost(D, S, H, Q_cur)
            besp = cur_cost - s["total"]
            st.markdown(
                f"- Nuværende ({num(Q_cur,0)} stk.): total = {kr(cur_cost,0)}, "
                f"som giver en **besparelse ved EOQ = {kr(besp,0)}/år**"
            )


# ===========================================================================
# MAKE-VS-BUY / TCA
# ===========================================================================
with tab_mvb:
    st.subheader("Make-vs-buy / Total Cost of Ownership (TCO)")
    st.caption("Sammenlign udlicitering mod egenproduktion på den fulde ejeromkostning "
               "(ikke kun stykpris). Forudfyldt med et eksempel "
               "(køb i udlandet vs. egenproduktion).")

    visning = st.radio("Visning", ["Break-even vs. volumen", "Fuld TCO-tabel"],
                       horizontal=True, key="mvb_view")

    if visning == "Break-even vs. volumen":
        st.caption("To totalomkostningslinjer som funktion af volumen — break-even hvor de krydser.")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Køb (outsource)**")
            f_buy = st.number_input("Faste omk. (kr./år)", value=14400.0,
                                    step=1000.0, key="mvb_fbuy",
                                    help="Faste omkostninger ved at lade andre levere: "
                                         "udgifter der er ens uanset hvor meget du køber "
                                         "(fx leje eller abonnement).")
            v_buy = st.number_input("Variabel (kr./stk.)", value=4.23,
                                    step=0.05, key="mvb_vbuy",
                                    help="Udgiften pr. stk. ved køb, som vokser med antallet "
                                         "(typisk selve stykprisen).")
        with c2:
            st.markdown("**Egenproduktion (insource)**")
            f_make = st.number_input("Faste omk. (kr./år)", value=51200.0,
                                     step=1000.0, key="mvb_fmake",
                                     help="Faste omkostninger ved selv at producere: udgifter "
                                          "der er ens uanset antallet (fx maskine eller leje).")
            v_make = st.number_input("Variabel (kr./stk.)", value=3.86,
                                     step=0.05, key="mvb_vmake",
                                     help="Udgiften pr. stk. ved egenproduktion, som vokser "
                                          "med antallet (fx materiale eller løn pr. stk.).")
        with c3:
            st.markdown("**Volumen**")
            vol = st.number_input("Aktuelt forbrug (stk./år)", value=48000.0,
                                  step=1000.0, key="mvb_vol",
                                  help="Hvor mange stk. du regner med at bruge på et år. "
                                       "Tallet bestemmer hvor på grafen du står, og dermed "
                                       "hvilken løsning der er billigst lige nu.")

        be = ik.breakeven_volume(f_buy, v_buy, f_make, v_make)
        vmax = max(vol * 1.6, (be * 1.6 if be == be and be > 0 else vol * 1.6))
        x = np.linspace(0, vmax, 200)
        y_buy = ik.total_cost_linear(f_buy, v_buy, x)
        y_make = ik.total_cost_linear(f_make, v_make, x)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y_buy, name="Køb (outsource)", line=dict(color=C_ORDER, width=3)))
        fig.add_trace(go.Scatter(x=x, y=y_make, name="Egenproduktion (insource)", line=dict(color=C_HOLD, width=3)))
        if be == be and be > 0:
            fig.add_vline(x=be, line_dash="dash", line_color=C_OPT)
            fig.add_trace(go.Scatter(x=[be], y=[ik.total_cost_linear(f_buy, v_buy, be)],
                                     mode="markers+text", marker=dict(color=C_OPT, size=12),
                                     text=[f"Break-even {num(be,0)}"], textposition="top center",
                                     name="Break-even"))
        fig.add_vline(x=vol, line_dash="dot", line_color="#64748b")
        fig.update_layout(xaxis_title="Volumen (stk./år)", yaxis_title="Total omkostning (kr./år)",
                          height=430, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption(
            "Sådan læser du grafen: hvor de to linjer krydser (break-even) koster køb og "
            "egenproduktion det samme. Til venstre for krydset er den ene billigst, til højre "
            "den anden. Den grå prikkede streg viser dit aktuelle forbrug, som fortæller "
            "hvilken side du er på, altså hvilken løsning der er billigst lige nu."
        )

        tb = ik.total_cost_linear(f_buy, v_buy, vol)
        tm = ik.total_cost_linear(f_make, v_make, vol)
        m1, m2, m3 = st.columns(3)
        m1.metric("Køb ved aktuelt forbrug", kr(tb, 0),
                  help="Total årlig omkostning ved at købe (outsource) ved det aktuelle volumen.")
        m2.metric("Egenproduktion ved aktuelt forbrug", kr(tm, 0),
                  help="Total årlig omkostning ved selv at producere (insource) ved aktuelt volumen.")
        billigst = "Køb" if tb < tm else "Egenproduktion"
        m3.metric(f"Billigst ved {num(vol,0)} stk.", billigst,
                  delta=f"sparer {kr(abs(tb - tm), 0)}", delta_color="off",
                  help="Den billigste mulighed ved det aktuelle volumen, og hvor meget den sparer "
                       "i forhold til den anden.")

        with st.expander("Mellemregninger / formel", expanded=True):
            st.markdown(
                f"- Total(køb) = {num(f_buy,0)} + {num(v_buy,2)}·V\n"
                f"- Total(egen) = {num(f_make,0)} + {num(v_make,2)}·V\n"
                f"- Break-even: V = (F_køb − F_egen)/(v_egen − v_køb) = **{num(be,0)} stk./år**\n"
                f"- Over break-even-volumen er den med lavest variabel pr. stk. billigst."
            )

    else:
        st.caption("Komponentopdelt TCO (kr./år). Ret tallene, så opdateres totalerne live. "
                   "Husk de 4 KPI'er nedenfor i den kvalitative vurdering.")
        buy_df = pd.DataFrame({
            "Komponent": ["Indkøbspris (FOB)", "Søfragt + forsikring", "Told (4,5 %)",
                          "Bestilling/adm.", "Lageromkostning", "Kassation (4 %)", "Risiko (valuta)"],
            "Beløb (kr./år)": [134400, 40800, 7884, 14400, 9636, 7480, 2688],
        })
        make_df = pd.DataFrame({
            "Komponent": ["Råmateriale", "Direkte løn", "Maskine (afskr./service/el)",
                          "Igangsætning (6 serier)", "Lageromkostning", "Kassation (1,5 %)",
                          "Engangsomk. (afskr. 5 år)"],
            "Beløb (kr./år)": [86400, 115200, 18000, 5100, 3696, 3024, 5000],
        })
        antal = st.number_input("Årligt forbrug (stk.)", value=48000.0, step=1000.0, key="tca_antal",
                                help="Bruges til at regne den fuldt belastede pris pr. stk. "
                                     "(total delt med antal).")
        st.caption("I tabellerne nedenfor kan du rette hvert beløb eller tilføje rækker. "
                   "Søjlerne og tallene opdateres med det samme.")

        cc1, cc2 = st.columns(2)
        with cc1:
            st.markdown("**Køb (udenlandsk leverandør)**")
            buy_e = st.data_editor(buy_df, num_rows="dynamic", hide_index=True,
                                   use_container_width=True, key="tca_buy")
        with cc2:
            st.markdown("**Egenproduktion (eget anlæg)**")
            make_e = st.data_editor(make_df, num_rows="dynamic", hide_index=True,
                                    use_container_width=True, key="tca_make")

        tot_buy = pd.to_numeric(buy_e["Beløb (kr./år)"], errors="coerce").sum()
        tot_make = pd.to_numeric(make_e["Beløb (kr./år)"], errors="coerce").sum()

        fig = go.Figure(go.Bar(
            x=["Køb (udland)", "Egenproduktion"],
            y=[tot_buy, tot_make], marker_color=[C_ORDER, C_HOLD],
            text=[kr(tot_buy, 0), kr(tot_make, 0)], textposition="outside"))
        fig.update_layout(yaxis_title="Total cost (kr./år)", height=380, margin=dict(t=40, b=10))
        st.plotly_chart(style_fig(fig), use_container_width=True)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total — Køb", kr(tot_buy, 0),
                  help="Summen af alle TCO-komponenter ved køb (kr./år).")
        m2.metric("Total — Egenprod.", kr(tot_make, 0),
                  help="Summen af alle TCO-komponenter ved egenproduktion (kr./år).")
        m3.metric("Pris/stk. — Køb", kr(tot_buy / antal, 2) if antal else "—",
                  help="Total ved køb delt med antal stk. (fuldt belastet stykpris).")
        m4.metric("Pris/stk. — Egenprod.", kr(tot_make / antal, 2) if antal else "—",
                  help="Total ved egenproduktion delt med antal stk. (fuldt belastet stykpris).")
        forskel = tot_make - tot_buy
        st.info(
            f"**{'Køb' if forskel > 0 else 'Egenproduktion'}** er billigst på TCO, "
            f"med en forskel på {kr(abs(forskel),0)}/år ved {num(antal,0)} stk. "
            "Tallet alene afgør det ikke, så vægt de 4 KPI'er nedenfor.",
            icon="⚖️",
        )
        with st.expander("De 4 make-or-buy KPI'er (kvalitativ vurdering)", expanded=False):
            st.markdown(
                "1. **Omkostningseffektivitet** (direkte + indirekte: transport, told, kvalitetstab)\n"
                "2. **Fejlprocent / kvalitet**\n"
                "3. **Leveringssikkerhed** (leveringspræcision, lead time, valutarisiko)\n"
                "4. **Omstillingstid / fleksibilitet**\n\n"
                "Beslutningsheuristik: ren offshoring til Asien er sjældent optimalt, fordi "
                "lange leadtider og risiko ofte opvejer besparelsen. **Nearshoring** "
                "(fx Østeuropa) rammer typisk den bedste balance. Selve investeringsdelen "
                "(egenproduktion vs. køb) regnes som investeringskalkule under Økonomi."
            )


# ===========================================================================
# ABC / PARETO
# ===========================================================================
with tab_abc:
    st.subheader("ABC / Pareto-analyse")
    st.caption("Sortér varer efter årsværdi (forbrug × pris). A ≤ 80 %, B ≤ 95 %, C > 95 % af akkumuleret værdi.")
    with st.expander("Tommelfingerregler og faldgruber", expanded=False):
        st.markdown(
            "- **A** ≈ 20 % af varerne / 80 % af omsætningen (placeres < 5 m fra ekspedition)\n"
            "- **B** ≈ 30 % af varerne / 15 % af omsætningen\n"
            "- **C** ≈ 50 % af varerne / 5 % af omsætningen (lagerautomat/VLM for at spare plads)\n"
            "- ABC-struktur sparer typisk ~12 % pluktid.\n"
            "- **Excel-faldgrube:** den akkumulerede % skal divideres med den **absolutte total**, "
            "ikke med en kumuleret sum."
        )

    default_abc = pd.DataFrame({
        "Betegnelse": ["Kompas Pro", "Mini Gasbrænder", "Vandfilter Pure",
                       "Karabinhage XL", "Stormkøkken L", "Stormkøkken S",
                       "Powerbank 10k", "Powerbank 20k", "Titanium Spork",
                       "Reparationskit Telt", "First-Aid Micro", "Sovepose -10",
                       "Ultralight Underlag", "Pakkepose 10L", "Pakkepose 30L"],
        "Årligt forbrug": [12000, 9600, 4800, 38000, 3000, 7800, 2400, 1600,
                           26000, 5000, 14000, 600, 1200, 8200, 4200],
        "Enhedspris": [28, 52, 118, 8, 210, 148, 260, 340, 19, 46, 24, 790,
                       540, 64, 96],
    })

    cset = st.columns([2, 1])
    with cset[1]:
        a_cut = st.slider("A-grænse (%)", 50, 90, 80, key="abc_a",
                          help="Varer der tilsammen udgør op til denne procent af den samlede "
                               "værdi bliver A-varer. Træk i skyderen for at flytte grænsen.") / 100
        b_cut = st.slider("B-grænse (%)", int(a_cut*100)+1, 99, 95, key="abc_b",
                          help="Varer op til denne procent bliver B-varer, resten bliver "
                               "C-varer. Træk i skyderen for at flytte grænsen.") / 100
    with cset[0]:
        st.caption("Indtast/ret varer (forbrug og pris):")
        data = st.data_editor(default_abc, num_rows="dynamic", hide_index=True,
                              use_container_width=True, key="abc_data", height=240)

    res = ik.abc_analysis(data, a_cut=a_cut, b_cut=b_cut)

    if not res.empty:
        farver = res["Kategori"].map({"A": C_A, "B": C_B, "C": C_C})
        fig = go.Figure()
        fig.add_trace(go.Bar(x=res["Betegnelse"], y=res["Årsværdi"], name="Årsværdi",
                             marker_color=farver))
        fig.add_trace(go.Scatter(x=res["Betegnelse"], y=res["Akkumuleret %"] * 100,
                                 name="Akkumuleret %", yaxis="y2",
                                 line=dict(color=C_TOTAL, width=3), mode="lines+markers"))
        fig.add_hline(y=a_cut*100, line_dash="dash", line_color=C_A, yref="y2",
                      annotation_text=f"A {int(a_cut*100)} %")
        fig.add_hline(y=b_cut*100, line_dash="dash", line_color=C_B, yref="y2",
                      annotation_text=f"B {int(b_cut*100)} %")
        fig.update_layout(
            height=440, margin=dict(t=30, b=10),
            yaxis=dict(title="Årsværdi (kr.)"),
            yaxis2=dict(title="Akkumuleret %", overlaying="y", side="right", range=[0, 105]),
            legend=dict(orientation="h", y=1.12),
            xaxis=dict(tickangle=-40),
        )
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption(
            "Sådan læser du grafen: søjlerne (venstre akse) viser hver vares årsværdi, "
            "sorteret fra størst til mindst. Den blå kurve (højre akse) lægger værdierne "
            "sammen i procent. Hvor kurven krydser de stiplede grænser, skifter varerne "
            "kategori fra A til B til C."
        )

        summ = ik.abc_summary(res)
        cc = st.columns(3)
        for i, kat in enumerate(["A", "B", "C"]):
            row = summ[summ["Kategori"] == kat].iloc[0]
            kat_help = {
                "A": "Få, dyre varer der binder størstedelen af værdien. Styr dem tæt "
                     "(hyppig opfølgning, lavt lager, tæt på ekspedition).",
                "B": "Mellemgruppe. Almindelig styring.",
                "C": "Mange, billige varer med lille værdiandel. Forenkl styringen "
                     "(store ordrer, lagerautomat/VLM).",
            }
            cc[i].metric(
                f"Kategori {kat}",
                f"{int(row['Antal varer'])} varer",
                f"{num(row['Andel af værdi %']*100,1)} % af værdi",
                delta_color="off",
                help=kat_help[kat],
            )

        with st.expander("Klassifikationstabel", expanded=False):
            vis = res[["Betegnelse", "Årligt forbrug", "Enhedspris", "Årsværdi",
                       "Akkumuleret %", "Kategori"]].copy()
            vis["Årsværdi"] = vis["Årsværdi"].map(lambda v: kr(v, 0))
            vis["Akkumuleret %"] = (res["Akkumuleret %"] * 100).map(lambda v: num(v, 1) + " %")
            st.dataframe(vis, hide_index=True, use_container_width=True)


# ===========================================================================
# GENBESTILLINGSPUNKT + SIKKERHEDSLAGER
# ===========================================================================
with tab_rop:
    st.subheader("Genbestillingspunkt (ROP) + sikkerhedslager (SS)")
    st.caption("ROP (\"benzinlampen\") = gns. forbrug i leveringstiden + sikkerhedslager. "
               "SS = z·σ·√L. Ugebaseret.")

    venstre, hoejre = st.columns([1, 2])
    with venstre:
        D = st.number_input("Årligt forbrug D (stk./år)", min_value=1.0,
                            value=7800.0, step=100.0, key="rop_D")
        sigma = st.number_input("Std.afvigelse σ (stk./uge)", min_value=0.0,
                                value=11.0, step=0.5, key="rop_sigma",
                                help="Spredning i ugentligt forbrug. √L ganges på, så det "
                                     "svarer til spredningen i hele leveringstiden (din z·σ-form).")
        L = st.number_input("Ledetid L (uger)", min_value=0.0, value=2.0,
                            step=0.5, key="rop_L")
        z_mode = st.radio("z-værdi", ["Fast tabel", "Frit serviceniveau"],
                          horizontal=True, key="rop_zmode",
                          help="Fast tabel = dine afrundede værdier (90 %=1,28, 95 %=1,65, "
                               "99 %=2,33). Frit = vilkårligt serviceniveau via normalfordelingen.")
        if z_mode == "Fast tabel":
            sv = st.select_slider("Serviceniveau", options=[90, 95, 99], value=95,
                                  format_func=lambda x: f"{x} %", key="rop_svfix")
            service = sv / 100
            z = ik.Z_TABLE[service]
        else:
            service = st.slider("Serviceniveau (%)", 50, 99, 95, key="rop_service") / 100
            z = ik.z_from_service(service)
        Q_ord = st.number_input("Ordrestørrelse Q (til graf)", min_value=1.0,
                                value=520.0, step=20.0, key="rop_Q")

    d = D / 52
    ss = ik.safety_stock(z, sigma, L)
    rop = ik.reorder_point(d, L, ss)
    s = {"d": d, "z": z, "sikkerhedslager": ss, "forbrug_i_ledetid": d * L, "ROP": rop}

    with hoejre:
        # Savtakket lagerprofil over tid
        T = Q_ord / d if d > 0 else 1            # cyklustid (uger)
        n_cyc = 3
        xs, ys = [], []
        top = ss + Q_ord
        for c in range(n_cyc):
            t0 = c * T
            xs += [t0, t0 + T]
            ys += [top, ss]
        weeks = np.linspace(0, n_cyc * T, 400)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=xs, y=ys, name="Lagerniveau",
                                 line=dict(color=C_TOTAL, width=2)))
        fig.add_hline(y=rop, line_dash="dash", line_color=C_ORDER,
                      annotation_text=f"ROP = {num(rop,0)}")
        fig.add_hline(y=ss, line_dash="dot", line_color=C_OPT,
                      annotation_text=f"SS = {num(ss,0)}")
        fig.update_layout(xaxis_title="Tid (uger)", yaxis_title="Lagerniveau (stk.)",
                          height=300, margin=dict(t=20, b=10), legend=dict(orientation="h", y=1.2))
        st.plotly_chart(style_fig(fig), use_container_width=True)

        # SS som funktion af serviceniveau
        sl = np.linspace(0.50, 0.999, 200)
        ss_curve = np.array([ik.safety_stock(ik.z_from_service(p), sigma, L) for p in sl])
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=sl * 100, y=ss_curve, line=dict(color=C_HOLD, width=3),
                                  name="SS"))
        fig2.add_trace(go.Scatter(x=[service * 100], y=[ss], mode="markers+text",
                                  marker=dict(color=C_OPT, size=12),
                                  text=[f"SS = {num(ss,0)}"], textposition="top center", name="Valgt"))
        fig2.update_layout(xaxis_title="Serviceniveau (%)", yaxis_title="Sikkerhedslager (stk.)",
                           height=230, margin=dict(t=10, b=10), showlegend=False)
        st.plotly_chart(style_fig(fig2), use_container_width=True)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("z-værdi", num(z, 3),
              help="Sikkerhedsfaktor for dit valgte serviceniveau (fra normalfordelingen).")
    m2.metric("Sikkerhedslager (SS)", f"{num(ss,0)} stk.",
              help="Ekstra buffer mod udsving i forbrug og leveringstid: SS = z·σ·√L.")
    m3.metric("Forbrug i ledetid", f"{num(s['forbrug_i_ledetid'],0)} stk.",
              help="Forventet forbrug mens du venter på leveringen: d·L.")
    m4.metric("Genbestillingspunkt (ROP)", f"{num(rop,0)} stk.",
              help="Lagerniveau hvor du skal bestille igen (forbrug i ledetid + sikkerhedslager).")

    with st.expander("Mellemregninger / formel", expanded=True):
        st.latex(r"SS = z \cdot \sigma \cdot \sqrt{L} \qquad ROP = d \cdot L + SS")
        sigma_lt = sigma * (L ** 0.5)
        st.markdown(
            f"- d (ugentligt forbrug) = D/52 = {num(D,0)}/52 = **{num(d,1)} stk./uge**\n"
            f"- z ved {num(service*100,0)} % serviceniveau = **{num(z,3)}**\n"
            f"- SS = {num(z,3)} · {num(sigma,1)} · √{num(L,1)} = **{num(ss,1)} stk.**\n"
            f"- ROP = d·L + SS = {num(d,1)}·{num(L,1)} + {num(ss,1)} = **{num(rop,1)} stk.**"
        )
        st.caption(
            f"Samme tal som din z·σ-form: spredning i hele leveringstiden "
            f"σ_LT = σ·√L = {num(sigma,1)}·√{num(L,1)} = {num(sigma_lt,1)}, "
            f"så SS = z·σ_LT = {num(z,3)}·{num(sigma_lt,1)} = {num(ss,1)} stk."
        )


# ===========================================================================
# POQ / EPQ
# ===========================================================================
with tab_poq:
    st.subheader("POQ / EPQ — optimal produktionsseriestørrelse")
    st.caption("Brug denne fane når du selv producerer varen i stedet for at købe den. "
               "Den finder den bedste seriestørrelse, altså hvor mange stk. du laver pr. "
               "produktionskørsel. Forskellen fra EOQ er, at lageret bygges op lidt ad gangen "
               "mens du producerer, i stedet for at komme på én gang. Forudfyldt med et eksempel.")

    venstre, hoejre = st.columns([1, 2])
    with venstre:
        D = st.number_input("Årlig efterspørgsel D (stk.)", min_value=1.0,
                            value=48000.0, step=1000.0, key="poq_D")
        dage = st.number_input("Arbejdsdage/år", min_value=1.0, value=250.0,
                               step=5.0, key="poq_dage")
        p = st.number_input("Daglig produktionskapacitet p (stk./dag)", min_value=1.0,
                            value=600.0, step=10.0, key="poq_p",
                            help="Hvor mange stk. du kan producere på én arbejdsdag. Skal være "
                                 "større end det daglige forbrug, ellers kan serien ikke beregnes.")
        S = st.number_input("Igangsætningsomkostning S (kr./serie)", min_value=0.01,
                            value=850.0, step=50.0, key="poq_S",
                            help="Hvad det koster at starte en ny produktionsserie op "
                                 "(omstilling af maskine, opsætning), uafhængigt af antal.")
        pris = st.number_input("Produktionspris (kr./stk.)", min_value=0.01,
                               value=4.20, step=0.10, key="poq_pris")
        rente = st.slider("Lagerrente (%)", 1, 60, 22, key="poq_rente") / 100
        Q_cur = st.number_input("Nuværende seriestørrelse (stk.)", min_value=1.0,
                                value=8000.0, step=500.0, key="poq_Qcur",
                                help="Hvor mange stk. du laver pr. serie i dag, så du kan se "
                                     "besparelsen ved at skifte til den optimale.")

    H = ik.holding_cost_per_unit(pris, rente)
    d = D / dage
    s = ik.epq_summary(D, S, H, d, p, Q_current=Q_cur)
    q_star = s["POQ"]

    with hoejre:
        if q_star == q_star:  # ikke NaN
            q_grid = np.linspace(max(1, q_star * 0.2), q_star * 2.6, 400)
            cur = ik.epq_curve(D, S, H, d, p, q_grid)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=cur["Q"], y=cur["igangsaetning"],
                                     name="Igangsætning", line=dict(color=C_ORDER)))
            fig.add_trace(go.Scatter(x=cur["Q"], y=cur["lageromkostning"],
                                     name="Lageromkostning", line=dict(color=C_HOLD)))
            fig.add_trace(go.Scatter(x=cur["Q"], y=cur["total"],
                                     name="Total", line=dict(color=C_TOTAL, width=3)))
            fig.add_vline(x=q_star, line_dash="dash", line_color=C_OPT)
            fig.add_trace(go.Scatter(x=[q_star], y=[s["total"]], mode="markers+text",
                                     marker=dict(color=C_OPT, size=12),
                                     text=[f"POQ = {num(q_star,0)}"], textposition="top center",
                                     name="Optimum"))
            if Q_cur:
                cur_tot = (D / Q_cur) * S + (Q_cur * s["andel_til_lager"] / 2) * H
                fig.add_vline(x=Q_cur, line_dash="dot", line_color="#64748b",
                              annotation_text=f"Nuværende {num(Q_cur,0)}")
            fig.update_layout(xaxis_title="Seriestørrelse Q (stk.)",
                              yaxis_title="Omkostning (kr./år)", height=430,
                              margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), use_container_width=True)
        else:
            st.error("p skal være større end daglig efterspørgsel d for at POQ kan beregnes.")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("POQ", f"{num(q_star,0)} stk.",
              help="Optimal produktionsseriestørrelse: hvor mange stk. pr. serie.")
    m2.metric("Antal serier/år", num(s["antal_serier"], 1),
              help="Hvor mange produktionsserier om året (D delt med POQ).")
    m3.metric("Maks. lager", f"{num(s['maks_lager'],0)} stk.",
              help="Højeste lagerniveau under serien: Q·(1−d/p). Lavere end Q, fordi der "
                   "forbruges løbende mens der produceres.")
    m4.metric("Total omkostning", kr(s["total"], 0),
              help="Igangsætnings- + lageromkostninger pr. år ved POQ.")

    with st.expander("Mellemregninger / formel", expanded=True):
        st.latex(r"POQ = \sqrt{\dfrac{2 \cdot D \cdot S}{H \cdot \left(1 - \frac{d}{p}\right)}}")
        st.markdown(
            f"- H = {num(pris,2)} × {num(rente*100,0)} % = **{num(H,3)} kr./stk./år**\n"
            f"- d = D/arbejdsdage = {num(D,0)}/{num(dage,0)} = **{num(d,1)} stk./dag**\n"
            f"- (1 − d/p) = (1 − {num(d,1)}/{num(p,0)}) = **{num(s['andel_til_lager'],3)}**\n"
            f"- POQ = √(2·{num(D,0)}·{num(S,0)} / ({num(H,3)}·{num(s['andel_til_lager'],3)})) "
            f"= **{num(q_star,0)} stk.**"
        )
        if "besparelse" in s:
            st.markdown(
                f"- Nuværende serie ({num(Q_cur,0)} stk.): total = {kr(s['total_nuvaerende'],0)}, "
                f"som giver en **besparelse ved POQ = {kr(s['besparelse'],0)}/år**"
            )
        st.markdown(
            f"- Antal serier/år = D/POQ = {num(s['antal_serier'],1)}"
        )


# ===========================================================================
# FORECASTING
# ===========================================================================
with tab_fc:
    st.subheader("Forecasting — efterspørgselsprognose")
    st.caption("Glidende gennemsnit og eksponentiel udglatning. Leverer årsforbrug D til "
               "EOQ og gns. forbrug til genbestillingspunktet. Vælg modellen med lavest "
               "MAD/MAPE og MFE tættest på 0.")

    venstre, hoejre = st.columns([1, 2])
    with venstre:
        n_ma = st.slider("Glidende gennemsnit, antal perioder (n)", 2, 6, 3, key="fc_n",
                         help="Antal seneste perioder der midles over. Stort n = glattere, "
                              "mere træg prognose; lille n = følger nyere udsving tættere.")
        st.caption("Glidende gennemsnit: forecast = gennemsnit af de n seneste faktiske perioder.")
        alpha = st.slider("Eksponentiel udglatning α", 0.05, 0.95, 0.30, 0.05, key="fc_alpha",
                          help="Vægt på den nyeste observation. Høj α reagerer hurtigt på nye "
                               "tal; lav α giver en træg, stabil prognose.")
        st.caption("Eksp. udglatning: F(t) = α·D(t−1) + (1−α)·F(t−1). "
                   "Lav α = stabil, høj α = reagerer hurtigt.")

    default_fc = pd.DataFrame({
        "Periode": list(range(1, 13)),
        "Faktisk efterspørgsel": [120, 135, 128, 150, 142, 160, 155, 168, 172, 165, 180, 190],
    })
    with venstre:
        data_fc = st.data_editor(default_fc, num_rows="dynamic", hide_index=True,
                                 use_container_width=True, key="fc_data", height=240)

    serie = pd.to_numeric(data_fc["Faktisk efterspørgsel"], errors="coerce").dropna().tolist()

    if len(serie) >= n_ma:
        ma = ik.moving_average(serie, n_ma)
        es = ik.exp_smoothing(serie, alpha)
        N = len(serie)
        # Fair sammenligning: samme periodevindue (efter glidende gns.' opvarmning)
        start = n_ma
        err_ma = ik.forecast_errors(serie[start:], ma[start:N])
        err_es = ik.forecast_errors(serie[start:], es[start:N])
        x_act = list(range(1, N + 1))

        with hoejre:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_act, y=serie, name="Faktisk",
                                     mode="lines+markers", line=dict(color=C_TOTAL, width=3)))
            fig.add_trace(go.Scatter(x=list(range(1, len(ma) + 1)), y=ma, name=f"Glidende gns. (n={n_ma})",
                                     mode="lines+markers", line=dict(color=C_ORDER, dash="dot"),
                                     connectgaps=False))
            fig.add_trace(go.Scatter(x=list(range(1, len(es) + 1)), y=es, name=f"Eksp. udglatning (α={alpha:.2f})",
                                     mode="lines+markers", line=dict(color=C_HOLD, dash="dash")))
            fig.update_layout(xaxis_title="Periode", yaxis_title="Efterspørgsel (stk.)",
                              height=420, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), use_container_width=True)

        st.markdown(f"**Sammenlign modellerne** (samme vindue fra periode {start+1}; "
                    "vælg lavest MAD/MAPE, MFE tæt på 0):")
        cmp = pd.DataFrame({
            "Model": [f"Glidende gns. (n={n_ma})", f"Eksp. udglatning (α={alpha:.2f})"],
            "MFE (bias)": [err_ma["MFE"], err_es["MFE"]],
            "MAD": [err_ma["MAD"], err_es["MAD"]],
            "MAPE": [err_ma["MAPE"] * 100 if err_ma["MAPE"] == err_ma["MAPE"] else float("nan"),
                     err_es["MAPE"] * 100 if err_es["MAPE"] == err_es["MAPE"] else float("nan")],
            "Tracking signal": [err_ma["tracking_signal"], err_es["tracking_signal"]],
            "Næste periode": [ma[-1], es[-1]],
        })
        visc = cmp.copy()
        visc["MFE (bias)"] = visc["MFE (bias)"].map(lambda v: num(v, 1))
        visc["MAD"] = visc["MAD"].map(lambda v: num(v, 1))
        visc["MAPE"] = visc["MAPE"].map(lambda v: num(v, 1) + " %")
        visc["Tracking signal"] = visc["Tracking signal"].map(lambda v: num(v, 2))
        visc["Næste periode"] = visc["Næste periode"].map(lambda v: num(v, 0) + " stk.")
        st.dataframe(
            visc, hide_index=True, use_container_width=True,
            column_config={
                "MFE (bias)": st.column_config.Column(
                    help="Gennemsnitlig fejl MED fortegn (faktisk − forecast). "
                         "Tæt på 0 = uvildig. Positiv = modellen undervurderer."),
                "MAD": st.column_config.Column(
                    help="Gennemsnitlig fejlstørrelse i stk. (uden fortegn). Lavere = bedre."),
                "MAPE": st.column_config.Column(
                    help="Gennemsnitlig procentvis fejl. Lavere = bedre. God til "
                         "at sammenligne på tværs af varer."),
                "Tracking signal": st.column_config.Column(
                    help="ΣFE / MAD. Driftsalarm: holder den sig ca. mellem −4 og +4, "
                         "er prognosen stabil; løber den væk, er der systematisk skævhed."),
                "Næste periode": st.column_config.Column(
                    help="Modellens forecast for den kommende periode (tallet du bruger videre)."),
            })

        bedst = "Glidende gns." if err_ma["MAD"] <= err_es["MAD"] else "Eksp. udglatning"
        st.success(f"Lavest MAD: **{bedst}**. Brug den som grundlag for D (årsforbrug) og "
                   "det gennemsnitlige forbrug i genbestillingspunktet.", icon="✅")

        with st.expander("Hvad betyder tallene?", expanded=True):
            st.markdown(
                "**Fejlmål** (FE = faktisk − forecast):\n"
                "- **MFE (bias):** gennemsnitlig fejl *med* fortegn. Tæt på 0 = uvildig. "
                "Positiv betyder modellen undervurderer (faktisk ligger over forecast).\n"
                "- **MAD** (mean absolute deviation): gennemsnitlig fejl*størrelse* i stk. "
                "uden fortegn. Lavere = mere præcis.\n"
                "- **MAPE:** gennemsnitlig *procentvis* fejl. Lavere = bedre. God til at "
                "sammenligne præcision på tværs af varer.\n"
                "- **Tracking signal** = ΣFE / MAD: en driftsalarm. Holder den sig typisk "
                "mellem −4 og +4, er prognosen stabil; løber den væk, er der systematisk skævhed.\n"
                "- **Næste periode:** modellens forecast for den kommende periode.\n\n"
                "Tommelfinger: vælg modellen med **lavest MAD/MAPE** og **MFE tættest på 0**."
            )
    else:
        st.info("Indtast mindst lige så mange perioder som n i det glidende gennemsnit.")


# ===========================================================================
# REVIEW-SYSTEMER
# ===========================================================================
with tab_review:
    st.subheader("Lagerstyringssystemer (review)")
    st.caption("To systemer for uafhængig efterspørgsel: periodisk review (bestil op til "
               "max-niveau ved faste tjek) og kontinuert review (bestil EOQ når lageret "
               "rammer genbestillingspunktet).")

    c1, c2, c3 = st.columns(3)
    with c1:
        d_uge = st.number_input("Forbrug d (stk./uge)", min_value=0.1, value=150.0,
                                step=5.0, key="rev_d",
                                help="Hvor mange stk. du bruger pr. uge (d står for daglig/"
                                     "periodisk forbrug, her pr. uge).")
        L = st.number_input("Ledetid L (uger)", min_value=0.0, value=2.0, step=0.5, key="rev_L",
                            help="Ledetid L: antal uger fra du bestiller til varen er fremme.")
    with c2:
        P = st.number_input("Review-interval P (uger)", min_value=0.5, value=4.0,
                            step=0.5, key="rev_P",
                            help="Hvor ofte du tjekker lageret, fx hver 4. uge.")
        SS = st.number_input("Sikkerhedslager SS (stk.)", min_value=0.0, value=50.0,
                            step=5.0, key="rev_SS",
                            help="Sikkerhedslager SS: ekstra buffer mod udsving i forbrug "
                                 "og leveringstid.")
    with c3:
        I = st.number_input("Nuværende beholdning I (stk.)", min_value=0.0, value=300.0,
                            step=10.0, key="rev_I",
                            help="Beholdning I: hvor mange stk. du har på lager lige nu.")
        EOQ_in = st.number_input("EOQ (til kontinuert)", min_value=1.0, value=520.0,
                                 step=10.0, key="rev_eoq",
                                 help="EOQ: den faste mængde du bestiller hver gang i kontinuert "
                                      "review. EOQ betyder den optimale ordrestørrelse "
                                      "(beregnes på EOQ-fanen).")

    R_level = ik.periodic_max_level(d_uge, P, L, SS)
    Q_per = ik.order_up_to(R_level, I)
    rop = d_uge * L + SS

    k1, k2 = st.columns(2)
    with k1:
        with st.container(border=True):
            st.markdown("### Periodisk review")
            st.caption("Tjek på faste tidspunkter, bestil op til max-niveau.")
            st.latex(r"R = d \cdot (P + L) + SS \qquad Q = R - I")
            st.metric("Max-niveau R", f"{num(R_level,0)} stk.",
                      help="Det niveau du fylder op til ved hvert tjek: R = d·(P+L)+SS.")
            st.metric("Bestil nu (Q = R − I)", f"{num(Q_per,0)} stk.",
                      help="Hvor meget du bestiller nu: max-niveau minus nuværende beholdning.")
            st.markdown(
                f"- R = {num(d_uge,0)}·({num(P,1)}+{num(L,1)}) + {num(SS,0)} = **{num(R_level,0)} stk.**\n"
                f"- Q = {num(R_level,0)} − {num(I,0)} = **{num(Q_per,0)} stk.**"
            )
    with k2:
        with st.container(border=True):
            st.markdown("### Kontinuert review")
            st.caption("Overvåg løbende, bestil fast mængde (EOQ) ved genbestillingspunkt.")
            st.latex(r"ROP = d \cdot L + SS \qquad Q = EOQ")
            st.metric("Genbestillingspunkt ROP", f"{num(rop,0)} stk.",
                      help="Bestil når lageret når dette niveau: ROP = d·L + SS.")
            st.metric("Bestil ved ROP (EOQ)", f"{num(EOQ_in,0)} stk.",
                      help="Du bestiller en fast mængde (EOQ) hver gang lageret rammer ROP.")
            status = "Bestil nu" if I <= rop else "Vent (over ROP)"
            st.markdown(
                f"- ROP = {num(d_uge,0)}·{num(L,1)} + {num(SS,0)} = **{num(rop,0)} stk.**\n"
                f"- Beholdning {num(I,0)} vs. ROP {num(rop,0)}: **{status}**"
            )
            st.caption(
                "Status sammenligner din nuværende beholdning med genbestillingspunktet. "
                "Er beholdningen på eller under ROP, står der Bestil nu; ligger den over, "
                "kan du vente."
            )

    st.caption("Periodisk: enkel administration, men kræver større sikkerhedslager (dækker "
               "P+L). Kontinuert: mindre lager, men kræver løbende overvågning.")


# ===========================================================================
# LEVERANDØRSCORE
# ===========================================================================
with tab_lev:
    st.subheader("Leverandørevaluering — vægtet score")
    st.caption("Scor hver leverandør 1-5 på kriterierne, vægt kriterierne, og få en samlet "
               "score. Vægtene normaliseres automatisk.")

    krit = ["Pris/TCO", "Kvalitet", "Leveringssikkerhed", "Fleksibilitet", "ESG"]
    st.markdown("**Vægte** (behøver ikke summe til 100 — normaliseres):")
    wc = st.columns(len(krit))
    default_w = [30, 25, 25, 10, 10]
    vaegt_basis = ("Vægt: hvor vigtigt kriteriet er i den samlede vurdering. Højere tal vejer "
                   "tungere. Tallene behøver ikke summe til 100, da de regnes om automatisk.")
    krit_help = {
        "Pris/TCO": vaegt_basis + " Pris/TCO er den fulde ejeromkostning, ikke kun stykprisen.",
        "Kvalitet": vaegt_basis,
        "Leveringssikkerhed": vaegt_basis,
        "Fleksibilitet": vaegt_basis,
        "ESG": vaegt_basis + " ESG dækker miljø, sociale forhold og god ledelse hos leverandøren.",
    }
    weights = {}
    for i, k in enumerate(krit):
        weights[k] = wc[i].number_input(k, min_value=0, max_value=100, value=default_w[i],
                                        step=5, key=f"lev_w_{i}",
                                        help=krit_help[k])

    default_lev = pd.DataFrame({
        "Leverandør": ["Leverandør A", "Leverandør B", "Leverandør C"],
        "Pris/TCO": [4, 3, 5],
        "Kvalitet": [2, 5, 2],
        "Leveringssikkerhed": [2, 5, 3],
        "Fleksibilitet": [3, 4, 2],
        "ESG": [2, 4, 2],
    })
    st.caption("Indtast/ret leverandører og scorer (1 = dårligst, 5 = bedst):")
    data_lev = st.data_editor(default_lev, num_rows="dynamic", hide_index=True,
                              use_container_width=True, key="lev_data")

    total_w = sum(weights.values())
    if total_w > 0 and not data_lev.empty:
        res = ik.evaluate_suppliers(data_lev, weights)
        fig = go.Figure(go.Bar(
            x=res["Leverandør"], y=res["Samlet score"],
            marker_color=C_TOTAL,
            text=res["Samlet score"].map(lambda v: num(v, 2)), textposition="outside"))
        fig.update_layout(yaxis_title="Samlet vægtet score (1-5)", height=360,
                          margin=dict(t=30, b=10), yaxis=dict(range=[0, 5.3]))
        st.plotly_chart(style_fig(fig), use_container_width=True)

        vind = res.iloc[0]
        st.success(f"Højest score: **{vind['Leverandør']}** ({num(vind['Samlet score'],2)} / 5)",
                   icon="🏆")
        norm = {k: v / total_w for k, v in weights.items()}
        st.caption("Normaliserede vægte: " +
                   " · ".join(f"{k} {num(v*100,0)} %" for k, v in norm.items()))
        with st.expander("Resultattabel", expanded=False):
            visl = res.copy()
            visl["Samlet score"] = visl["Samlet score"].map(lambda v: num(v, 2))
            st.dataframe(visl, hide_index=True, use_container_width=True)
    else:
        st.info("Tilføj mindst én leverandør og sæt mindst én vægt > 0.")


# ===========================================================================
# STRATEGI & MODELLER (bibliotek)
# ===========================================================================
with tab_strat:
    st.subheader("Strategi & modeller — indkøbsbibliotek")
    st.caption("Opslag på de kvalitative indkøbsmodeller. Kraljic-placeringen er interaktiv; "
               "resten er hurtige opslag med forklaring og anvendelse.")

    # --- Kraljic interaktiv placering ---
    st.markdown("### Kraljic-matrix (interaktiv)")
    st.caption("Placér varer efter økonomisk betydning (y) og forsyningsrisiko (x), 1-5. "
               "Antal mulige leverandører afgør risikoen (få leverandører giver høj risiko).")

    kc1, kc2 = st.columns([1, 2])
    with kc1:
        default_k = pd.DataFrame({
            "Vare": ["Skruer", "Råstål", "Sensorer", "Specialstål"],
            "Økonomisk betydning": [2, 4, 2, 5],
            "Forsyningsrisiko": [1, 2, 4, 5],
        })
        data_k = st.data_editor(default_k, num_rows="dynamic", hide_index=True,
                                use_container_width=True, key="k_data", height=200)
    with kc2:
        fig = go.Figure()
        # kvadrant-baggrund
        fig.add_shape(type="rect", x0=0.5, y0=3, x1=3, y1=5.5, fillcolor="rgba(167,139,250,0.06)", line_width=0)
        fig.add_shape(type="rect", x0=3, y0=3, x1=5.5, y1=5.5, fillcolor="rgba(244,114,182,0.08)", line_width=0)
        fig.add_shape(type="rect", x0=0.5, y0=0.5, x1=3, y1=3, fillcolor="rgba(52,211,153,0.06)", line_width=0)
        fig.add_shape(type="rect", x0=3, y0=0.5, x1=5.5, y1=3, fillcolor="rgba(251,191,36,0.08)", line_width=0)
        for x, y, t in [(1.75, 5.2, "Vægtstang"), (4.25, 5.2, "Strategisk"),
                        (1.75, 0.8, "Rutine"), (4.25, 0.8, "Flaskehals")]:
            fig.add_annotation(x=x, y=y, text=t, showarrow=False,
                               font=dict(color="#94a3b8", size=13))
        kd = data_k.copy()
        kd["Økonomisk betydning"] = pd.to_numeric(kd["Økonomisk betydning"], errors="coerce")
        kd["Forsyningsrisiko"] = pd.to_numeric(kd["Forsyningsrisiko"], errors="coerce")
        kd = kd.dropna()
        fig.add_trace(go.Scatter(
            x=kd["Forsyningsrisiko"], y=kd["Økonomisk betydning"], mode="markers+text",
            text=kd["Vare"], textposition="top center",
            marker=dict(color=C_OPT, size=13), name="Varer"))
        fig.add_vline(x=3, line_dash="dot", line_color=C_MUTED)
        fig.add_hline(y=3, line_dash="dot", line_color=C_MUTED)
        fig.update_layout(xaxis=dict(title="Forsyningsrisiko", range=[0.5, 5.5]),
                          yaxis=dict(title="Økonomisk betydning", range=[0.5, 5.5]),
                          height=400, margin=dict(t=20, b=10), showlegend=False)
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption(
            "Sådan læser du grafen: hver vare lander i en af de fire kvadranter alt efter "
            "hvor vigtig (op ad) og hvor risikabel (til højre) den er. Kvadrantens navn, "
            "fx Strategisk eller Rutine, fortæller hvilken indkøbsstrategi der passer. "
            "Se forklaringen i feltet Strategi pr. Kraljic-kvadrant nedenunder."
        )

    with st.expander("Strategi pr. Kraljic-kvadrant", expanded=False):
        st.markdown(
            "- **Rutinevarer** (lav/lav): mange udbydere. Automatisér, rammeaftaler, e-indkøb, "
            "VMI. Minimer transaktionsomkostninger. (Skruer, emballage.)\n"
            "- **Vægtstang/leverage** (lav risiko/høj værdi): mange leverandører. Udnyt købekraft, "
            "konkurrenceudsæt via udbud, pres pris. Armslængde. (Råstål, lakering.)\n"
            "- **Flaskehals** (høj risiko/lav værdi): få leverandører, kan stoppe produktion. "
            "Sikr forsyning, sikkerhedslager, accepter højere pris, søg alternativer. (Sensorer.)\n"
            "- **Strategisk** (høj/høj): få specialiserede leverandører, kritisk for kvalitet. "
            "Langsigtet partnerskab, fælles produktudvikling, forsyningssikkerhed. (Specialstål.)"
        )

    st.divider()
    st.markdown("### Modelopslag")
    soeg = st.text_input("Søg model (fx 'sourcing', 'bensaou', 'voice')", key="strat_soeg").lower()

    modeller = [
        ("Bensaous leverandørmatrix",
         ["bensaou", "leverandør", "relation", "partnerskab", "market"],
         "Relationstype via køber-investering × leverandør-investering: **Market exchange** "
         "(lav/lav, ren markedshandel, fx Kina pga. pris, intet partnerskab, ofte dårlig "
         "kvalitet/lange leadtider), **Captive buyer**, **Captive supplier**, **Strategisk "
         "partnerskab** (høj/høj).",
         "Når du skal klassificere en konkret leverandørrelation og udlede en handlingsstrategi."),
        ("Sourcing-typer",
         ["sourcing", "single", "dual", "multiple", "cross", "parallel"],
         "**Single** (én leverandør, risiko) · **Multiple** (flere, konkurrence/sikkerhed) · "
         "**Dual** (to, backup) · **Cross/parallel** (samme vare fra flere markeder).",
         "Når du vælger forsyningsstruktur ud fra risiko og ønsket konkurrence/sikkerhed."),
        ("Hirschmans Exit / Voice",
         ["exit", "voice", "hirschman", "skift", "forhandl"],
         "**Exit** = afbryd og skift leverandør. **Voice** = bliv i relationen og "
         "forhandl/forbedr. Langt stabilt samarbejde taler for voice, med dual sourcing som backup.",
         "Når en leverandør underpræsterer og du skal vælge mellem at skifte eller forbedre."),
        ("TCE vs. netværksperspektiv",
         ["tce", "transaktion", "netværk", "perspektiv"],
         "**Transaktionsomkostningsøkonomi (TCE):** minimer kontrakt-/transaktionsomkostninger, "
         "armslængde, make-or-buy. **Netværk:** relationer og værdiskabelse over tid.",
         "Når du argumenterer for en ny indkøbsstrategi (Spm 5: TCE-fokus vs. netværksrelation)."),
        ("Order winner vs. qualifier (Terry Hill)",
         ["order", "winner", "qualifier", "hill"],
         "**Qualifier** = minimumskrav for at komme i betragtning. **Winner** = den faktor der "
         "vinder ordren. (Standardvare: pris = winner. Specialvare: tilpasning = winner, men "
         "for lang leadtid kan fejle på qualifier.)",
         "Når du skal forklare hvad der reelt vinder ordren vs. hvad der blot kvalificerer."),
        ("Indkøbsniveauer",
         ["niveau", "strategisk", "taktisk", "operationel"],
         "**Strategisk** (3-5 år: partnerskaber, make-or-buy, strategi) · **Taktisk** (6-18 mdr.: "
         "leverandørudvælgelse, kontraktforhandling, procesoptimering, bindeled) · "
         "**Operationelt** (dag-til-dag: ordrer, lagerstyring, fakturabehandling).",
         "Når du skal forankre en analyse på rette niveau. TCO og spend analysis er taktiske."),
        ("Relationsformer (VMI / ESI)",
         ["vmi", "esi", "armslængde", "relation", "partnerskab"],
         "**Armslængde** (rutine/leverage) vs. **tæt samarbejde/strategisk partnerskab** "
         "(flaskehals/strategisk). **VMI** = leverandør fylder selv op. **ESI** = leverandør "
         "med tidligt i produktudvikling.",
         "Når du foreslår at op- eller nedgradere et leverandørsamarbejde (matchet til Kraljic)."),
        ("Best practice (SRM, Category Mgmt, TCO, spend)",
         ["srm", "category", "tco", "spend", "best practice"],
         "**SRM** (Supplier Relationship Management) · **Category Management** · **TCO** (Total "
         "Cost of Ownership, ikke kun stykpris) · KPI/performance · **spend analysis**.",
         "Når du anbefaler professionalisering af indkøbsfunktionen."),
    ]

    vist = 0
    for navn, tags, forklaring, hvornaar in modeller:
        if soeg and soeg not in navn.lower() and not any(soeg in t for t in tags):
            continue
        vist += 1
        with st.expander(navn, expanded=bool(soeg)):
            st.markdown(f"**Hvad:** {forklaring}")
            st.markdown(f"**Hvornår:** {hvornaar}")
    if soeg and vist == 0:
        st.info("Ingen model matchede søgningen.")
