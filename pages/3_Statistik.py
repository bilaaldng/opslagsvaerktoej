"""Statistik — regnemaskiner med dynamiske grafer (scipy for korrekthed).

Moduler: Normalfordeling · Konfidensinterval · Hypotesetest · Binomialfordeling ·
Kontrolkort (p-kort, X̄- og R-kort) · Regression.
Notation matcher brugerens danish-statistik-skill + VIDEN §8.
"""
import math
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from scipy.stats import t as t_dist  # kun til at TEGNE t-kurven (matematik ligger i core)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import statistik as stat  # noqa: E402
from ui_theme import (  # noqa: E402
    inject_css, style_fig, C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_MUTED,
)

st.set_page_config(page_title="Statistik", page_icon="📊", layout="wide")
inject_css()


def num(x, dec=0):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "—"
    s = f"{x:,.{dec}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def pct(x, dec=2):
    if x is None or (isinstance(x, float) and (math.isnan(x) or math.isinf(x))):
        return "—"
    return num(x * 100, dec) + " %"


st.title("📊 Statistik")
st.caption("Regnemaskiner med live-grafer. scipy leverer de rigtige tal, så du kan "
           "stole på resultatet og bruge det direkte i opgaven.")

# 50 målinger (fx vægt-% ved en kvalitetskontrol) — forudfyldt eksempel til
# rå-data-tilstandene. Facit: x̄ = 11,867 · s = 0,179 · 95 % KI [11,82 ; 11,92].
MAALE_EKSEMPEL = (
    "11,69 11,90 11,93 12,03 11,88\n"
    "11,74 11,73 12,08 11,66 12,11\n"
    "11,64 11,98 11,92 11,89 12,30\n"
    "11,98 11,79 11,93 11,87 11,77\n"
    "11,80 11,69 11,97 11,89 12,12\n"
    "11,84 12,12 11,87 11,88 11,94\n"
    "11,63 11,60 11,85 11,93 11,67\n"
    "11,81 12,07 11,85 11,66 11,87\n"
    "11,72 11,71 11,98 12,25 11,33\n"
    "11,73 12,02 11,72 12,05 11,96"
)

RAADATA_HELP = ("Sæt dine målinger ind — adskilt af mellemrum, linjeskift eller "
                "semikolon. Både dansk decimalkomma (11,69) og punktum (11.69) "
                "forstås. Eksemplet er 50 målinger fra en kvalitetskontrol, så "
                "du kan tjekke mod et kendt facit.")


def normalitetsvurdering(d: dict) -> None:
    """Vurdering i hverdagssprog af om målingerne ligner en normalfordeling
    (68-95-99,7-reglen + skævhed). d kommer fra stat.beskrivende()."""
    linjer = (f"- Inden for ±1s: **{pct(d['andel_1s'], 0)}** af målingerne "
              f"(en normalfordeling har ca. 68 %)\n"
              f"- Inden for ±2s: **{pct(d['andel_2s'], 0)}** (normal: ca. 95 %)\n"
              f"- Inden for ±3s: **{pct(d['andel_3s'], 0)}** (normal: ca. 99,7 %)\n"
              f"- Skævhed: **{num(d['skaevhed'], 2)}** — tæt på 0 betyder symmetrisk, "
              f"og gennemsnit ({num(d['gennemsnit'], 2)}) og median "
              f"({num(d['median'], 2)}) ligger da også "
              f"{'tæt på hinanden' if abs(d['gennemsnit'] - d['median']) <= d['s'] * 0.25 else 'et stykke fra hinanden'}.")
    ligner = (abs(d["skaevhed"]) < 0.5
              and abs(d["andel_1s"] - 0.68) <= 0.12
              and d["andel_2s"] >= 0.88)
    if ligner:
        st.success("**Ligner en normalfordeling.** Tommelfingerreglen 68-95-99,7 "
                   "passer pænt, og fordelingen er nogenlunde symmetrisk — du kan "
                   "roligt regne videre med normalfordelingen.")
    else:
        st.warning("**Ligner ikke helt en normalfordeling.** Tallene afviger fra "
                   "68-95-99,7-reglen eller fordelingen er skæv — brug resultater "
                   "der forudsætter normalfordeling med forsigtighed.")
    st.markdown(linjer)


tab_norm, tab_ki, tab_ht, tab_binom, tab_kk, tab_reg = st.tabs([
    "Normalfordeling", "Konfidensinterval", "Hypotesetest",
    "Binomialfordeling", "Kontrolkort", "Regression",
])


# ===========================================================================
# NORMALFORDELING
# ===========================================================================
with tab_norm:
    st.subheader("Normalfordeling")
    st.caption("Brug denne fane når noget varierer omkring et gennemsnit (fx vægt, højde eller "
               "leveringstid). Du kan regne ud hvor sandsynligt det er at en værdi ligger i et "
               "bestemt interval, eller finde den værdi der svarer til en bestemt procentdel. "
               "Har du rå målinger (fx fra en kvalitetskontrol), kan du sætte "
               "dem direkte ind og få x̄, s og et normalitets-tjek. Arealet under kurven er "
               "sandsynligheden, og skraveringen og tallene opdateres live.")

    n_kilde = st.radio("Datakilde", ["Indtast μ og σ", "Indsæt dine målinger"],
                       horizontal=True, key="n_kilde",
                       help="Vælg 'Indtast μ og σ' hvis opgaven oplyser gennemsnit og "
                            "standardafvigelse. Vælg 'Indsæt dine målinger' hvis du har de rå "
                            "tal — så beregner værktøjet selv x̄, s og n og tjekker om de "
                            "ligner en normalfordeling.")

    n_data = None
    n_klar = True
    if n_kilde == "Indsæt dine målinger":
        n_txt = st.text_area("Dine målinger", value=MAALE_EKSEMPEL, height=170,
                             key="n_raadata", help=RAADATA_HELP)
        n_parsed = stat.parse_maalinger(n_txt)
        if n_parsed["ignoreret"]:
            vis = ", ".join(n_parsed["ignoreret"][:8])
            st.warning(f"{len(n_parsed['ignoreret'])} stump(er) kunne ikke læses som tal og "
                       f"er IKKE talt med: {vis}"
                       + (" …" if len(n_parsed["ignoreret"]) > 8 else ""))
        if len(n_parsed["vaerdier"]) < 2:
            st.info("Indsæt mindst to tal for at regne videre.")
            n_klar = False
        else:
            n_data = stat.beskrivende(n_parsed["vaerdier"])
            mb = st.columns(4)
            mb[0].metric("Gennemsnit x̄", num(n_data["gennemsnit"], 3),
                         help="Gennemsnittet af dine indsatte målinger — bruges som μ i kurven.")
            mb[1].metric("Std.afvigelse s", num(n_data["s"], 3),
                         help="Stikprøvens standardafvigelse (n−1 i nævneren, som i Excels "
                              "STDEV.S) — bruges som σ i kurven.")
            mb[2].metric("Antal n", num(n_data["n"], 0),
                         help="Hvor mange tal værktøjet fandt i din indsatte tekst.")
            mb[3].metric("Median", num(n_data["median"], 3),
                         help="Den midterste måling. Ligger median og gennemsnit tæt på "
                              "hinanden, taler det for en symmetrisk (normal) fordeling.")

    if n_klar:
        v, h = st.columns([1, 2])
        with v:
            if n_data:
                mu, sigma = n_data["gennemsnit"], n_data["s"]
                st.caption(f"μ og σ er sat fra dine målinger: μ = {num(mu, 3)}, "
                           f"σ = {num(sigma, 3)}.")
            else:
                mu = st.number_input("Middelværdi μ", value=100.0, step=1.0, key="n_mu",
                                     help="Gennemsnittet af dine data, altså den værdi tingene typisk "
                                          "ligger omkring. Det græske bogstav μ (my) står for gennemsnit. "
                                          "Kurven har sit højeste punkt her.")
                sigma = st.number_input("Standardafvigelse σ", min_value=0.01, value=15.0, step=1.0, key="n_sigma",
                                        help="Hvor meget dine data spreder sig omkring gennemsnittet. "
                                             "Bogstavet σ (sigma) står for standardafvigelse. Et lille tal "
                                             "giver en smal, høj kurve, hvor værdierne ligger tæt; et stort "
                                             "tal giver en bred, flad kurve.")
            mode = st.radio("Beregn", ["Sandsynlighed for interval", "Find x fra sandsynlighed"],
                            key="n_mode",
                            help="Vælg 'Sandsynlighed for interval' hvis du kender en værdi og vil "
                                 "vide hvor sandsynlig den er. Vælg 'Find x fra sandsynlighed' hvis du "
                                 "kender en procentdel og vil finde den værdi der hører til.")
            if mode == "Sandsynlighed for interval":
                lo_on = st.checkbox("Nedre grænse", value=True, key="n_loon")
                lower = st.number_input("Nedre x", value=mu - sigma, step=1.0, key="n_lo") if lo_on else None
                hi_on = st.checkbox("Øvre grænse", value=True, key="n_hion")
                upper = st.number_input("Øvre x", value=mu + sigma, step=1.0, key="n_hi") if hi_on else None
            else:
                hale = st.radio("Hale", ["Venstre — find x hvor P(X ≤ x) rammes",
                                         "Højre — find x hvor P(X > x) rammes"],
                                key="n_hale",
                                help="Venstre hale: du kender procentdelen der skal ligge UNDER "
                                     "værdien (fx 'de nederste 95 %'). Højre hale: procentdelen der "
                                     "skal ligge OVER (fx 'de øverste 5 %') — så slipper du for at "
                                     "regne 100 % minus selv.")
                p_pct = st.number_input("Sandsynlighed (%)", min_value=0.1, max_value=99.9,
                                        value=95.0, step=0.1, key="n_ppct",
                                        help="Procentdelen i den valgte hale. Decimaler er tilladt, "
                                             "så eksamensklassikere som 97,5 % og 99,5 % kan tastes "
                                             "direkte.")

        with h:
            xs = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
            ys = stat.normal_pdf(xs, mu, sigma)
            fig = go.Figure()
            if n_data:
                fig.add_trace(go.Histogram(x=n_parsed["vaerdier"], histnorm="probability density",
                                           marker_color="rgba(59,130,246,0.45)",
                                           name="Dine målinger"))
            fig.add_trace(go.Scatter(x=xs, y=ys, line=dict(color=C_TOTAL, width=3),
                                     name="Normalkurve" if n_data else "Tæthed"))
            if mode == "Sandsynlighed for interval":
                lo = mu - 4 * sigma if lower is None else lower
                hi = mu + 4 * sigma if upper is None else upper
                mask = (xs >= lo) & (xs <= hi)
                fig.add_trace(go.Scatter(x=xs[mask], y=ys[mask], fill="tozeroy",
                                         fillcolor="rgba(16,185,129,0.35)", line=dict(width=0),
                                         name="Areal"))
                area = stat.normal_area(lower, upper, mu, sigma)
            else:
                p_hale = p_pct / 100
                if hale.startswith("Venstre"):
                    xval = mu + stat.prob_to_z(p_hale) * sigma
                    mask = xs <= xval
                else:
                    xval = mu + stat.prob_to_z(1 - p_hale) * sigma
                    mask = xs >= xval
                fig.add_trace(go.Scatter(x=xs[mask], y=ys[mask], fill="tozeroy",
                                         fillcolor="rgba(16,185,129,0.35)", line=dict(width=0),
                                         name="Areal"))
                fig.add_vline(x=xval, line_dash="dash", line_color=C_OPT)
            fig.update_layout(xaxis_title="x", yaxis_title="Tæthed", height=420,
                              margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12),
                              barmode="overlay")
            st.plotly_chart(style_fig(fig), width="stretch")
            st.caption("Sådan læser du grafen: det grønne skraverede område er svaret, og dets "
                       "størrelse i forhold til hele kurven er sandsynligheden. Hele arealet under "
                       "kurven er 100 %. Y-aksen 'Tæthed' er bare kurvens højde, ikke et tal du selv "
                       "skal aflæse."
                       + (" Søjlerne er dine egne målinger — jo bedre de følger kurven, jo mere "
                          "normalfordelte er de." if n_data else ""))

        if n_data:
            st.markdown("**Ligner dine målinger en normalfordeling?**")
            normalitetsvurdering(n_data)

        if mode == "Sandsynlighed for interval":
            m1, m2, m3 = st.columns(3)
            m1.metric("Sandsynlighed (areal)", pct(area), help="P for at en værdi falder i intervallet.")
            if lower is not None:
                m2.metric("z (nedre)", num(stat.z_score(lower, mu, sigma), 2),
                          help="z fortæller hvor mange standardafvigelser værdien ligger fra "
                               "gennemsnittet. z = 0 er lige på gennemsnittet, z = 2 ligger to "
                               "standardafvigelser over. Bruges til at slå op i en z-tabel.")
            if upper is not None:
                m3.metric("z (øvre)", num(stat.z_score(upper, mu, sigma), 2),
                          help="z fortæller hvor mange standardafvigelser værdien ligger fra "
                               "gennemsnittet. z = 0 er lige på gennemsnittet, z = 2 ligger to "
                               "standardafvigelser over. Bruges til at slå op i en z-tabel.")
            with st.expander("Mellemregninger", expanded=True):
                lo_t = "−∞" if lower is None else num(lower, 1)
                hi_t = "+∞" if upper is None else num(upper, 1)
                st.markdown(f"- Areal mellem {lo_t} og {hi_t} = **{pct(area)}**\n"
                            f"- z = (x − μ)/σ med μ={num(mu,1)}, σ={num(sigma,1)}")
        else:
            retning = "under" if hale.startswith("Venstre") else "over"
            st.metric("x ved valgt hale", num(xval, 2),
                      help=f"Den x-værdi hvor præcis {num(p_pct, 1)} % af fordelingen ligger "
                           f"{retning}.")
            z_brugt = stat.prob_to_z(p_hale) if hale.startswith("Venstre") else stat.prob_to_z(1 - p_hale)
            st.caption(f"{num(p_pct, 1)} % i {'venstre' if hale.startswith('Venstre') else 'højre'} "
                       f"hale giver z = {num(z_brugt, 3)}, så x = μ + z·σ = {num(xval, 2)}.")


# ===========================================================================
# KONFIDENSINTERVAL
# ===========================================================================
with tab_ki:
    st.subheader("Konfidensinterval")
    st.caption("Intervallet der med valgt sikkerhed indeholder den sande værdi. "
               "Smallere ved større stikprøve. Du kan også gå den anden vej og finde "
               "hvor stor en stikprøve du skal bruge for en ønsket præcision.")

    ki_tilstand = st.radio("Hvad vil du beregne?",
                           ["Konfidensinterval", "Find n (stikprøvestørrelse)"],
                           horizontal=True, key="ki_tilstand",
                           help="'Konfidensinterval' regner intervallet ud fra din stikprøve. "
                                "'Find n' vender formlen om: hvor mange skal du måle/spørge for "
                                "at ramme en ønsket fejlmargin?")

    if ki_tilstand == "Find n (stikprøvestørrelse)":
        art_n = st.radio("Type", ["Middelværdi", "Andel"], horizontal=True, key="ki_fart",
                         help="Vælg 'Middelværdi' når du måler noget (fx vægt eller tid). "
                              "Vælg 'Andel' når du tæller en procentdel (fx defekte).")
        conf_n = st.select_slider("Konfidensniveau", options=[0.90, 0.95, 0.99], value=0.95,
                                  format_func=lambda x: f"{int(x*100)} %", key="ki_fconf",
                                  help="Hvor sikker du vil være på at intervallet fanger den "
                                       "sande værdi. 95 % er standarden til eksamen.")
        if art_n == "Middelværdi":
            c = st.columns(2)
            sigma_n = c[0].number_input("Standardafvigelse σ", min_value=0.01, value=15.0,
                                        step=0.5, key="ki_fsigma",
                                        help="Spredningen i det du måler — typisk et skøn fra en "
                                             "tidligere undersøgelse eller oplyst i opgaven.")
            me_n = c[1].number_input("Ønsket fejlmargin ME", min_value=0.01, value=3.0,
                                     step=0.5, key="ki_fme",
                                     help="Hvor tæt på den sande værdi dit gennemsnit skal ramme, "
                                          "altså den halve bredde af intervallet. Mindre ME = "
                                          "flere målinger.")
            rn = stat.sample_size_mean(sigma_n, me_n, conf_n)
            st.metric("Nødvendig stikprøve n", num(rn["n"], 0),
                      help="Antal målinger du mindst skal bruge. Rundes altid OP, for et halvt "
                           "svar tæller ikke.")
            with st.expander("Mellemregninger / formel", expanded=True):
                st.latex(r"n = \left(\frac{z \cdot \sigma}{ME}\right)^{2}")
                st.markdown(f"- z({int(conf_n*100)} %) = {num(rn['z'],3)}\n"
                            f"- n = ({num(rn['z'],3)} · {num(sigma_n,2)} / {num(me_n,2)})² "
                            f"= {num(rn['n_raa'],2)} → rundes op til **{num(rn['n'],0)}**")
        else:
            worst = st.checkbox("Brug p = 50 % (worst case)", value=True, key="ki_fworst",
                                help="Kender du ikke andelen på forhånd, giver p = 50 % den "
                                     "største (sikreste) stikprøve. Slå fra hvis du har et skøn.")
            c = st.columns(2)
            if worst:
                p_forv = 0.5
                c[0].caption("Forventet andel: 50 % (worst case)")
            else:
                p_forv = c[0].number_input("Forventet andel (%)", min_value=0.1, max_value=99.9,
                                           value=40.0, step=0.1, key="ki_fp",
                                           help="Dit bedste skøn på andelen, fx fra en tidligere "
                                                "måling.") / 100
            me_p = c[1].number_input("Ønsket fejlmargin (%-point)", min_value=0.1, max_value=50.0,
                                     value=3.0, step=0.1, key="ki_fmep",
                                     help="Hvor mange procentpoint dit resultat højst må ligge fra "
                                          "den sande andel. ±3 %-point er det klassiske "
                                          "meningsmålings-krav.") / 100
            rn = stat.sample_size_proportion(p_forv, me_p, conf_n)
            st.metric("Nødvendig stikprøve n", num(rn["n"], 0),
                      help="Antal du mindst skal spørge/tjekke. Rundes altid OP.")
            with st.expander("Mellemregninger / formel", expanded=True):
                st.latex(r"n = \frac{z^{2} \cdot p(1-p)}{ME^{2}}")
                st.markdown(f"- z({int(conf_n*100)} %) = {num(rn['z'],3)} · p = {pct(p_forv,1)} · "
                            f"ME = {pct(me_p,1)}\n"
                            f"- n = {num(rn['z'],3)}² · {num(p_forv,2)}·{num(1-p_forv,2)} / "
                            f"{num(me_p,3)}² = {num(rn['n_raa'],2)} → rundes op til "
                            f"**{num(rn['n'],0)}**")
    else:
        art = st.radio("Type", ["Middelværdi", "Andel"], horizontal=True, key="ki_art",
                       help="Vælg 'Middelværdi' når du måler noget (fx gennemsnitlig vægt eller tid). "
                            "Vælg 'Andel' når du tæller en procentdel (fx hvor mange procent er "
                            "defekte eller tilfredse).")
        conf = st.select_slider("Konfidensniveau", options=[0.90, 0.95, 0.99], value=0.95,
                                format_func=lambda x: f"{int(x*100)} %", key="ki_conf")

        ki_klar = True
        ki_data = None
        if art == "Middelværdi":
            ki_kilde = st.radio("Datakilde", ["Nøgletal (x̄, s, n)", "Indsæt dine målinger"],
                                horizontal=True, key="ki_kilde",
                                help="Har du kun opsummerede tal fra opgaven, så vælg 'Nøgletal'. "
                                     "Har du de rå målinger (fx fra en kvalitetskontrol), så sæt "
                                     "dem ind og lad værktøjet regne x̄, s og n.")
            metode = st.radio("Metode", ["σ ukendt — brug s fra stikprøven (t)", "σ kendt (z)"],
                              horizontal=True, key="ki_metode",
                              help="Kender du KUN stikprøvens egen spredning s, bruges "
                                   "t-fordelingen (det typiske til eksamen). Oplyser opgaven den "
                                   "SANDE standardafvigelse σ, bruges z i stedet — det giver et "
                                   "lidt smallere interval.")
            if ki_kilde == "Indsæt dine målinger":
                ki_txt = st.text_area("Dine målinger", value=MAALE_EKSEMPEL, height=150,
                                      key="ki_raadata", help=RAADATA_HELP)
                ki_parsed = stat.parse_maalinger(ki_txt)
                if ki_parsed["ignoreret"]:
                    vis = ", ".join(ki_parsed["ignoreret"][:8])
                    st.warning(f"{len(ki_parsed['ignoreret'])} stump(er) kunne ikke læses som tal "
                               f"og er IKKE talt med: {vis}"
                               + (" …" if len(ki_parsed["ignoreret"]) > 8 else ""))
                if len(ki_parsed["vaerdier"]) < 2:
                    st.info("Indsæt mindst to tal for at regne videre.")
                    ki_klar = False
                else:
                    ki_data = stat.beskrivende(ki_parsed["vaerdier"])
                    mean, s, n = ki_data["gennemsnit"], ki_data["s"], ki_data["n"]
                    mb = st.columns(3)
                    mb[0].metric("Gennemsnit x̄", num(mean, 3),
                                 help="Beregnet af dine indsatte målinger.")
                    mb[1].metric("Std.afvigelse s", num(s, 3),
                                 help="Stikprøvens standardafvigelse (n−1, som Excels STDEV.S).")
                    mb[2].metric("Antal n", num(n, 0),
                                 help="Hvor mange tal værktøjet fandt i din indsatte tekst.")
            else:
                c = st.columns(3)
                mean = c[0].number_input("Gennemsnit", value=50.0, step=1.0, key="ki_mean",
                                         help="Gennemsnittet du har målt i din stikprøve. Det bliver "
                                              "midten af konfidensintervallet.")
                if metode.startswith("σ kendt"):
                    s = c[1].number_input("Kendt σ", min_value=0.01, value=10.0, step=0.5, key="ki_sigma",
                                          help="Den sande standardafvigelse som opgaven oplyser "
                                               "(ikke stikprøvens egen s). Bruges i z-formlen.")
                else:
                    s = c[1].number_input("Std.afvigelse s", min_value=0.0, value=10.0, step=0.5, key="ki_s",
                                          help="Hvor meget dine målinger spreder sig omkring gennemsnittet i "
                                               "din stikprøve. Det lille s står for stikprøvens "
                                               "standardafvigelse. Får du den oplyst i opgaven, taster du den "
                                               "bare ind.")
                n = c[2].number_input("Stikprøvestørrelse n", min_value=2, value=25, step=1, key="ki_n",
                                      help="Antal observationer i din stikprøve, altså hvor mange du har "
                                           "målt eller spurgt. Jo større n, jo smallere bliver intervallet.")
            if ki_klar:
                if metode.startswith("σ kendt"):
                    if ki_kilde == "Indsæt dine målinger":
                        sigma_kendt = st.number_input("Kendt σ", min_value=0.01,
                                                      value=float(s) if s else 10.0,
                                                      step=0.5, key="ki_sigma2",
                                                      help="Den sande standardafvigelse som opgaven "
                                                           "oplyser (ikke stikprøvens s). Bruges i "
                                                           "z-formlen. Forudfyldt med stikprøvens s "
                                                           "som udgangspunkt.")
                    else:
                        sigma_kendt = s
                    r = stat.ci_mean_z(mean, sigma_kendt, int(n), conf)
                    formel = (f"- z({int(conf*100)} %) = {num(r['z'],3)} · "
                              f"standardfejl = σ/√n = {num(r['std_error'],3)}\n"
                              f"- ME = z·σ/√n = **{num(r['margin'],3)}**\n"
                              f"- KI = {num(mean,2)} ± {num(r['margin'],2)} = "
                              f"**[{num(r['nedre'],2)} ; {num(r['oevre'],2)}]**")
                else:
                    r = stat.ci_mean(mean, s, int(n), conf)
                    formel = (f"- t({int(conf*100)} %, {int(n)-1}) = {num(r['t'],3)} · "
                              f"standardfejl = s/√n = {num(r['std_error'],3)}\n"
                              f"- ME = t·s/√n = **{num(r['margin'],3)}**\n"
                              f"- KI = {num(mean,2)} ± {num(r['margin'],2)} = "
                              f"**[{num(r['nedre'],2)} ; {num(r['oevre'],2)}]**")
                est, me = mean, r["margin"]
                # Validitetstjek: lille stikprøve kræver (nogenlunde) normalfordelte data
                if int(n) < 30:
                    if ki_data is not None:
                        skaev = (abs(ki_data["skaevhed"]) >= 0.5
                                 or abs(ki_data["andel_1s"] - 0.68) > 0.12)
                        if skaev:
                            st.warning(f"Pas på: n = {int(n)} er under 30, og dine målinger ligner "
                                       "ikke en normalfordeling (se Normalfordelings-fanen). "
                                       "Intervallet kan være misvisende.")
                        else:
                            st.info(f"n = {int(n)} er under 30, men dine målinger ligner en "
                                    "normalfordeling, så intervallet holder.")
                    else:
                        st.info(f"n = {int(n)} er under 30: intervallet kræver at dine data er "
                                "nogenlunde normalfordelte. Er du i tvivl, så tjek de rå målinger "
                                "under Normalfordelings-fanen først.")
        else:
            c = st.columns(2)
            phat = c[0].slider("Stikprøveandel p̂ (%)", 1, 99, 40, key="ki_phat",
                               help="Den procentdel du fandt i din stikprøve, fx hvor mange procent "
                                    "var defekte eller sagde ja. Tegnet p̂ (kaldes 'p-hat') er den "
                                    "andel du selv har målt. Talte du 40 ud af 100, sætter du den til "
                                    "40 %.") / 100
            n = c[1].number_input("Stikprøvestørrelse n", min_value=2, value=100, step=10, key="ki_np",
                                  help="Antal observationer i din stikprøve, altså hvor mange du har "
                                       "målt eller spurgt. Jo større n, jo smallere bliver intervallet.")
            r = stat.ci_proportion(phat, int(n), conf)
            est, me = phat, r["margin"]
            formel = (f"- z({int(conf*100)} %) = {num(r['z'],3)} · "
                      f"standardfejl = √(p̂(1−p̂)/n) = {num(r['std_error'],4)}\n"
                      f"- ME = z·SE = **{num(me,4)}**\n"
                      f"- KI = {pct(phat,1)} ± {pct(me,1)} = **[{pct(r['nedre'],1)} ; {pct(r['oevre'],1)}]**")
            # Validitetstjek for normaltilnærmelsen
            if int(n) * phat < 5 or int(n) * (1 - phat) < 5:
                st.warning(f"Pas på: n·p̂ = {num(int(n)*phat,1)} eller n·(1−p̂) = "
                           f"{num(int(n)*(1-phat),1)} er under 5, så normaltilnærmelsen (og "
                           "dermed intervallet) er usikker. Få flere observationer, eller brug "
                           "binomialfordelingen direkte.")

        if ki_klar:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=[est], y=[0], mode="markers", marker=dict(color=C_TOTAL, size=14),
                                     error_x=dict(type="data", array=[me], color=C_OPT, thickness=3, width=14),
                                     name="Estimat ± ME"))
            fig.update_layout(height=200, margin=dict(t=20, b=10), yaxis=dict(visible=False, range=[-1, 1]),
                              xaxis_title=("Andel" if art == "Andel" else "Værdi"), showlegend=False)
            st.plotly_chart(style_fig(fig), width="stretch")
            st.caption("Sådan læser du grafen: prikken er dit estimat (midten), og den vandrette streg "
                       "viser hvor langt intervallet strækker sig til hver side. Jo kortere streg, jo mere "
                       "præcist er resultatet. ME står for 'fejlmargin', altså usikkerheden.")

            ki_help = ("De tre tal er dit svar: den sande værdi ligger med den valgte sikkerhed mellem "
                       "nedre og øvre grænse. 'Estimat' er dit bedste bud (midten); grænserne viser "
                       "usikkerheden omkring det.")
            m1, m2, m3 = st.columns(3)
            m1.metric("Nedre grænse", pct(r["nedre"], 1) if art == "Andel" else num(r["nedre"], 2), help=ki_help)
            m2.metric("Estimat", pct(est, 1) if art == "Andel" else num(est, 2), help=ki_help)
            m3.metric("Øvre grænse", pct(r["oevre"], 1) if art == "Andel" else num(r["oevre"], 2), help=ki_help)
            with st.expander("Mellemregninger / formel", expanded=True):
                st.markdown(formel)


# ===========================================================================
# HYPOTESETEST
# ===========================================================================
def ht_graf(vaerdi: float, kritisk: float, sided: str, navn: str = "z", df=None):
    """Tæthedskurve med rødt kritisk område og markør ved teststørrelsen.
    Samme mønster som normalfordelings-fanen (style_fig + skravering)."""
    graense = max(4.0, abs(vaerdi) + 0.8, abs(kritisk) + 0.8)
    xs = np.linspace(-graense, graense, 500)
    ys = t_dist.pdf(xs, df) if df is not None else stat.normal_pdf(xs)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys, line=dict(color=C_TOTAL, width=3), name="Tæthed"))
    if sided == "tosidet":
        masker = [xs <= -abs(kritisk), xs >= abs(kritisk)]
    elif sided == "hoejre":
        masker = [xs >= kritisk]
    else:
        masker = [xs <= kritisk]
    for i, mask in enumerate(masker):
        fig.add_trace(go.Scatter(x=xs[mask], y=ys[mask], fill="tozeroy",
                                 fillcolor="rgba(239,68,68,0.35)", line=dict(width=0),
                                 name="Kritisk område", showlegend=(i == 0)))
    fig.add_vline(x=vaerdi, line_dash="dash", line_color=C_OPT,
                  annotation_text=f"{navn} = {num(vaerdi, 2)}")
    fig.update_layout(xaxis_title=navn, yaxis_title="Tæthed", height=400,
                      margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
    st.plotly_chart(style_fig(fig), width="stretch")
    st.caption("Sådan læser du grafen: det røde område er det kritiske område — lander den "
               "stiplede markør (din teststørrelse) derinde, forkastes H0. Det røde areal "
               "svarer til signifikansniveauet.")


def ht_konklusion(navn: str, vaerdi: float, kritisk: float, p: float, alpha: float,
                  sided: str, forkast: bool, tekst_forkast: str, tekst_behold: str):
    """Konklusion I ORD, fx:
    'z = 2,15 > 1,645 og p = 0,016 < 0,05 → gennemsnittet er signifikant over 75'."""
    if sided == "tosidet":
        smlg = (f"|{navn}| = {num(abs(vaerdi), 2)} "
                f"{'>' if abs(vaerdi) > abs(kritisk) else '≤'} {num(abs(kritisk), 3)}")
    elif sided == "hoejre":
        smlg = f"{navn} = {num(vaerdi, 2)} {'>' if vaerdi > kritisk else '≤'} {num(kritisk, 3)}"
    else:
        smlg = f"{navn} = {num(vaerdi, 2)} {'<' if vaerdi < kritisk else '≥'} {num(kritisk, 3)}"
    p_del = f"p = {num(p, 3)} {'<' if p < alpha else '≥'} {num(alpha, 2)}"
    if forkast:
        st.success(f"**{smlg} og {p_del} → forkast H0:** {tekst_forkast}")
    else:
        st.info(f"**{smlg} og {p_del} → H0 kan IKKE forkastes:** {tekst_behold}")


with tab_ht:
    st.subheader("Hypotesetest")
    st.caption("Test en påstand om et gennemsnit: er det fx SIGNIFIKANT over 75, eller kan "
               "forskellen bare være tilfældighed? H0 er 'ingen forskel'-påstanden, og testen "
               "fortæller om dine data er usandsynlige nok til at forkaste den. To typiske "
               "spørgsmål: 'er tilfredsheden over 75?' (én stikprøve) og 'ligger gruppe A "
               "under gruppe B?' (to stikprøver).")

    ht_type = st.radio("Testtype",
                       ["Én stikprøve (mod en påstået værdi μ₀)",
                        "To stikprøver (sammenlign to grupper)"],
                       horizontal=True, key="ht_type",
                       help="Én stikprøve: du tester ét gennemsnit mod en fast værdi, fx 'er "
                            "tilfredsheden over 75?'. To stikprøver: du sammenligner to gruppers "
                            "gennemsnit, fx afdeling A mod afdeling B.")

    HALE_VALG = ["Tosidet (≠)", "Højre (større end)", "Venstre (mindre end)"]
    HALE_MAP = {"Tosidet (≠)": "tosidet", "Højre (større end)": "hoejre",
                "Venstre (mindre end)": "venstre"}
    HALE_HELP = ("Tosidet: du tester bare om der ER en forskel (begge retninger). Højre: du "
                 "tester om gennemsnittet er STØRRE (fx 'over 75'). Venstre: om det er MINDRE. "
                 "Retningen skal matche opgavens spørgsmål, IKKE dine tal.")
    METODE_HELP = ("z-test: brug når σ er kendt (oplyst i opgaven) eller stikprøven er stor "
                   "(n ≥ 30). t-test: brug når du kun kender stikprøvens egen spredning s og "
                   "n er lille — t-fordelingen tager højde for den ekstra usikkerhed.")

    if ht_type.startswith("Én"):
        v, h = st.columns([1, 2])
        with v:
            ht_mean = st.number_input("Stikprøvens gennemsnit x̄", value=76.97, step=0.1,
                                      key="ht_mean", format="%.2f",
                                      help="Det gennemsnit du har målt i stikprøven — fx et "
                                           "tilfredshedsindeks på 76,97.")
            ht_mu0 = st.number_input("Påstået værdi μ₀", value=75.0, step=0.5, key="ht_mu0",
                                     help="Værdien du tester imod — H0 siger at det sande "
                                          "gennemsnit ER μ₀, fx en målsætning på 75.")
            ht_n = st.number_input("Stikprøvestørrelse n", min_value=2, value=100, step=1,
                                   key="ht_n",
                                   help="Antal observationer i stikprøven. Jo flere, jo mindre "
                                        "skal forskellen være før den bliver signifikant.")
            ht_metode = st.radio("Metode", ["Kendt σ (z-test)", "Ukendt σ — brug s (t-test)"],
                                 key="ht_metode", help=METODE_HELP)
            ht_spread = st.number_input("σ (z-test)" if ht_metode.startswith("Kendt")
                                        else "s fra stikprøven (t-test)",
                                        min_value=0.01, value=9.16, step=0.1, key="ht_s",
                                        help="Spredningen: den kendte σ ved z-test, eller "
                                             "stikprøvens egen standardafvigelse s ved t-test.")
            ht_hale = st.radio("Retning (H1)", HALE_VALG, index=1, key="ht_hale", help=HALE_HELP)
            ht_alpha = st.select_slider("Signifikansniveau α", options=[0.01, 0.05, 0.10],
                                        value=0.05, format_func=lambda x: f"{num(x*100, 0)} %",
                                        key="ht_alpha",
                                        help="Hvor stor risiko du accepterer for at forkaste H0 "
                                             "ved en fejl (type I-fejl). 5 % er standarden til "
                                             "eksamen.")
        sided = HALE_MAP[ht_hale]
        if ht_metode.startswith("Kendt"):
            r = stat.z_test_mean(ht_mean, ht_spread, int(ht_n), ht_mu0, sided, ht_alpha)
            navn, vaerdi, df = "z", r["z"], None
        else:
            r = stat.t_test_mean(ht_mean, ht_spread, int(ht_n), ht_mu0, sided, ht_alpha)
            navn, vaerdi, df = "t", r["t"], r["df"]
        with h:
            ht_graf(vaerdi, r["kritisk"], sided, navn, df)

        m1, m2, m3 = st.columns(3)
        m1.metric(f"Teststørrelse {navn}", num(vaerdi, 2),
                  help="Hvor mange standardfejl dit gennemsnit ligger fra den påståede værdi. "
                       "Jo længere fra 0, jo stærkere taler dine data imod H0.")
        m2.metric("Kritisk værdi", num(r["kritisk"], 3),
                  help="Grænsen for det kritiske område ved det valgte signifikansniveau. "
                       "Er teststørrelsen forbi grænsen, forkastes H0.")
        m3.metric("p-værdi", num(r["p"], 4),
                  help="Sandsynligheden for at se dit resultat (eller noget mere ekstremt) HVIS "
                       "H0 var sand. Under signifikansniveauet → forkast H0.")

        retning_ord = {"hoejre": "over", "venstre": "under", "tosidet": "forskelligt fra"}[sided]
        ht_konklusion(navn, vaerdi, r["kritisk"], r["p"], ht_alpha, sided, r["forkast"],
                      f"gennemsnittet er signifikant {retning_ord} {num(ht_mu0, 2)} "
                      f"på {num(ht_alpha*100, 0)} %-niveau.",
                      f"der er ikke statistisk belæg for at gennemsnittet er {retning_ord} "
                      f"{num(ht_mu0, 2)} — forskellen kan være tilfældighed.")

        with st.expander("Mellemregninger / formel", expanded=True):
            if navn == "z":
                st.latex(r"z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
                st.markdown(
                    f"- H0: μ = {num(ht_mu0,2)} · H1: μ {'≠' if sided=='tosidet' else ('>' if sided=='hoejre' else '<')} {num(ht_mu0,2)}\n"
                    f"- Standardfejl = σ/√n = {num(ht_spread,2)}/√{int(ht_n)} = {num(r['se'],4)}\n"
                    f"- z = ({num(ht_mean,2)} − {num(ht_mu0,2)}) / {num(r['se'],4)} = **{num(vaerdi,2)}**\n"
                    f"- Kritisk værdi ({num(ht_alpha*100,0)} %, {'tosidet' if sided=='tosidet' else 'ensidet'}) = {num(r['kritisk'],3)} · p-værdi = **{num(r['p'],4)}**")
            else:
                st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}")
                st.markdown(
                    f"- H0: μ = {num(ht_mu0,2)} · H1: μ {'≠' if sided=='tosidet' else ('>' if sided=='hoejre' else '<')} {num(ht_mu0,2)}\n"
                    f"- Standardfejl = s/√n = {num(ht_spread,2)}/√{int(ht_n)} = {num(r['se'],4)}\n"
                    f"- t = ({num(ht_mean,2)} − {num(ht_mu0,2)}) / {num(r['se'],4)} = **{num(vaerdi,2)}** med df = {int(r['df'])}\n"
                    f"- Kritisk værdi ({num(ht_alpha*100,0)} %, {'tosidet' if sided=='tosidet' else 'ensidet'}) = {num(r['kritisk'],3)} · p-værdi = **{num(r['p'],4)}**")
    else:
        st.caption("Eksempel: Gruppe 1 = 70,28, Gruppe 2 = 76,97 — test om gruppe 1 ligger "
                   "signifikant UNDER gruppe 2 (venstre hale).")
        v, h = st.columns([1, 2])
        with v:
            g1, g2 = st.columns(2)
            g1.markdown("**Gruppe 1**")
            m1_ = g1.number_input("Gennemsnit x̄₁", value=70.28, step=0.1, key="ht_m1", format="%.2f",
                                  help="Gennemsnittet i den første gruppe, fx afdeling A's "
                                       "tilfredshedsindeks.")
            s1_ = g1.number_input("Spredning (σ₁/s₁)", min_value=0.01, value=9.0, step=0.1, key="ht_s1",
                                  help="Gruppens standardafvigelse: den kendte σ ved z-test "
                                       "eller stikprøvens s ved t-test.")
            n1_ = g1.number_input("Antal n₁", min_value=2, value=100, step=1, key="ht_n1",
                                  help="Antal observationer i gruppe 1.")
            g2.markdown("**Gruppe 2**")
            m2_ = g2.number_input("Gennemsnit x̄₂", value=76.97, step=0.1, key="ht_m2", format="%.2f",
                                  help="Gennemsnittet i den anden gruppe, fx afdeling B's "
                                       "tilfredshedsindeks.")
            s2_ = g2.number_input("Spredning (σ₂/s₂)", min_value=0.01, value=9.16, step=0.1, key="ht_s2",
                                  help="Gruppens standardafvigelse: den kendte σ ved z-test "
                                       "eller stikprøvens s ved t-test.")
            n2_ = g2.number_input("Antal n₂", min_value=2, value=100, step=1, key="ht_n2",
                                  help="Antal observationer i gruppe 2.")
            ht_metode2 = st.radio("Metode", ["Kendte σ'er (z-test)", "Ukendte σ'er — brug s (t-test)"],
                                  key="ht_metode2", help=METODE_HELP)
            ht_hale2 = st.radio("Retning (H1)", HALE_VALG, index=2, key="ht_hale2",
                                help=HALE_HELP + " Her gælder retningen gruppe 1 i forhold til "
                                     "gruppe 2 — 'Venstre' tester om gruppe 1 ligger UNDER "
                                     "gruppe 2.")
            ht_alpha2 = st.select_slider("Signifikansniveau α", options=[0.01, 0.05, 0.10],
                                         value=0.05, format_func=lambda x: f"{num(x*100, 0)} %",
                                         key="ht_alpha2",
                                         help="Hvor stor risiko du accepterer for at forkaste H0 "
                                              "ved en fejl (type I-fejl). 5 % er standarden til "
                                              "eksamen.")
        sided2 = HALE_MAP[ht_hale2]
        if ht_metode2.startswith("Kendte"):
            r2 = stat.z_test_two_means(m1_, s1_, int(n1_), m2_, s2_, int(n2_), sided2, ht_alpha2)
            navn2, vaerdi2, df2 = "z", r2["z"], None
        else:
            r2 = stat.t_test_two_means(m1_, s1_, int(n1_), m2_, s2_, int(n2_), sided2, ht_alpha2)
            navn2, vaerdi2, df2 = "t", r2["t"], r2["df"]
        with h:
            ht_graf(vaerdi2, r2["kritisk"], sided2, navn2, df2)

        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Forskel x̄₁ − x̄₂", num(r2["forskel"], 2),
                  help="Den målte forskel mellem gruppernes gennemsnit. Testen afgør om den er "
                       "signifikant eller kan være tilfældighed.")
        k2.metric(f"Teststørrelse {navn2}", num(vaerdi2, 2),
                  help="Forskellen målt i standardfejl. Jo længere fra 0, jo stærkere taler "
                       "dine data imod H0 (ingen forskel).")
        k3.metric("Kritisk værdi", num(r2["kritisk"], 3),
                  help="Grænsen for det kritiske område ved det valgte signifikansniveau.")
        k4.metric("p-værdi", num(r2["p"], 5),
                  help="Sandsynligheden for at se en så stor forskel HVIS grupperne i "
                       "virkeligheden var ens. Under signifikansniveauet → forkast H0.")

        retning2 = {"hoejre": "højere end", "venstre": "lavere end",
                    "tosidet": "forskelligt fra"}[sided2]
        ht_konklusion(navn2, vaerdi2, r2["kritisk"], r2["p"], ht_alpha2, sided2, r2["forkast"],
                      f"gruppe 1's gennemsnit ({num(m1_, 2)}) er signifikant {retning2} "
                      f"gruppe 2's ({num(m2_, 2)}) på {num(ht_alpha2*100, 0)} %-niveau.",
                      f"der er ikke statistisk belæg for at gruppe 1 ligger {retning2} "
                      f"gruppe 2 — forskellen kan være tilfældighed.")

        with st.expander("Mellemregninger / formel", expanded=True):
            if navn2 == "z":
                st.latex(r"z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}")
            else:
                st.latex(r"t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}")
            df_linje = "" if df2 is None else f" med df ≈ {num(df2, 1)} (Welch)"
            st.markdown(
                f"- H0: μ₁ = μ₂ · H1: μ₁ {'≠' if sided2=='tosidet' else ('>' if sided2=='hoejre' else '<')} μ₂\n"
                f"- Standardfejl = √({num(s1_,2)}²/{int(n1_)} + {num(s2_,2)}²/{int(n2_)}) = {num(r2['se'],4)}\n"
                f"- {navn2} = ({num(m1_,2)} − {num(m2_,2)}) / {num(r2['se'],4)} = **{num(vaerdi2,2)}**{df_linje}\n"
                f"- Kritisk værdi ({num(ht_alpha2*100,0)} %, {'tosidet' if sided2=='tosidet' else 'ensidet'}) = {num(r2['kritisk'],3)} · p-værdi = **{num(r2['p'],5)}**")


# ===========================================================================
# BINOMIALFORDELING
# ===========================================================================
with tab_binom:
    st.subheader("Binomialfordeling")
    st.caption("n uafhængige forsøg, konstant sandsynlighed p, tæl antal succeser X. "
               "Til 'x ud af n'-spørgsmål.")

    v, h = st.columns([1, 2])
    with v:
        n = st.number_input("Antal forsøg n", min_value=1, value=20, step=1, key="b_n",
                            help="Hvor mange gange du prøver, fx 20 varer du tjekker. Et 'forsøg' "
                                 "kan være hvad som helst med to udfald (fx defekt eller ikke "
                                 "defekt).")
        p = st.number_input("Sandsynlighed p (%)", min_value=0.1, max_value=99.9, value=30.0,
                            step=0.1, key="b_p",
                            help="Chancen for succes i et enkelt forsøg, i procent. Decimaler er "
                                 "tilladt, så fx en defektrate på 2,5 % kan tastes direkte. En "
                                 "'succes' er bare det udfald du tæller efter.") / 100
        k = st.number_input("Antal succeser k", min_value=0, max_value=int(n), value=min(6, int(n)), step=1, key="b_k",
                            help="Hvor mange af forsøgene du vil regne på, fx præcis 6 defekte ud "
                                 "af de 20. k er altså et bestemt antal succeser blandt de n forsøg.")
        interval_on = st.checkbox("Beregn P(a ≤ X ≤ b)", value=False, key="b_ivon",
                                  help="Slå til hvis opgaven spørger om et INTERVAL af succeser, "
                                       "fx 'mellem 4 og 8 defekte'. Grænserne a og b tæller selv "
                                       "med.")
        if interval_on:
            ci1, ci2 = st.columns(2)
            iv_a = ci1.number_input("Fra a", min_value=0, max_value=int(n), value=min(4, int(n)),
                                    step=1, key="b_iva",
                                    help="Intervallets nedre grænse — det mindste antal succeser "
                                         "der tæller med.")
            iv_b = ci2.number_input("Til b", min_value=0, max_value=int(n), value=min(8, int(n)),
                                    step=1, key="b_ivb",
                                    help="Intervallets øvre grænse — det største antal succeser "
                                         "der tæller med.")
            if iv_b < iv_a:
                st.warning("Øvre grænse b er mindre end nedre grænse a — byt om på dem, "
                           "ellers er intervallet tomt og P = 0 %.")

    s = stat.binom_summary(int(n), p, int(k))
    with h:
        xs = np.arange(0, int(n) + 1)
        pmf = stat.binom_pmf_array(int(n), p)   # vektoriseret: hurtigt ved stort n
        if interval_on:
            colors = [C_OPT if x == int(k) else (C_ORDER if iv_a <= x <= iv_b else C_TOTAL)
                      for x in xs]
        else:
            colors = [C_OPT if x == int(k) else C_TOTAL for x in xs]
        fig = go.Figure(go.Bar(x=xs, y=pmf, marker_color=colors, name="P(X=x)"))
        ap = stat.binom_normal_approx(int(n), p)
        if ap["gyldig"]:
            xc = np.linspace(0, int(n), 200)
            fig.add_trace(go.Scatter(x=xc, y=stat.normal_pdf(xc, ap["mu"], ap["sigma"]),
                                     line=dict(color=C_HOLD, width=2, dash="dash"),
                                     name="Normaltilnærmelse"))
        fig.update_layout(xaxis_title="Antal succeser X", yaxis_title="Sandsynlighed",
                          height=420, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
        if int(n) > 200:
            # Zoom ind på det interessante vindue (μ ± 4σ) så grafen forbliver læsbar
            fig.update_xaxes(range=[max(0, ap["mu"] - 4 * ap["sigma"]),
                                    min(int(n), ap["mu"] + 4 * ap["sigma"])])
        st.plotly_chart(style_fig(fig), width="stretch")
        st.caption("Sådan læser du grafen: hver søjle viser sandsynligheden for præcis det antal "
                   "succeser. Den fremhævede søjle er dit valgte k"
                   + (", og de orange søjler er dit interval fra a til b" if interval_on else "")
                   + ". Den stiplede kurve er en glat "
                   "tilnærmelse, der kun er pålidelig når stikprøven er stor nok (se noten i "
                   "Mellemregninger)."
                   + (" Ved stort n er x-aksen zoomet ind på μ ± 4σ." if int(n) > 200 else ""))

    m1, m2, m3, m4 = st.columns(4)
    m1.metric(f"P(X = {int(k)})", pct(s["P_lig"]), help="Præcis k succeser.")
    m2.metric(f"P(X ≤ {int(k)})", pct(s["P_hoejst"]), help="Højst k succeser (kumuleret).")
    m3.metric(f"P(X ≥ {int(k)})", pct(s["P_mindst"]), help="Mindst k succeser.")
    m4.metric("Middelværdi μ", num(s["middel"], 2),
              help="Det antal succeser du i gennemsnit kan forvente. Med 20 forsøg og 30 % chance "
                   "forventer du 6 succeser. Regnes som μ = n·p, og spredningen er "
                   "σ = √(n·p·(1−p)).")
    if interval_on:
        p_iv = stat.binom_between(int(iv_a), int(iv_b), int(n), p)
        st.metric(f"P({int(iv_a)} ≤ X ≤ {int(iv_b)})", pct(p_iv),
                  help="Sandsynligheden for at antallet af succeser lander i intervallet — "
                       "begge grænser tæller med. Regnes som P(X ≤ b) − P(X ≤ a−1).")
    with st.expander("Mellemregninger / formel", expanded=True):
        st.latex(r"P(X=k) = \binom{n}{k} p^{k} (1-p)^{n-k}")
        st.markdown(
            f"- P(X = {int(k)}) = **{pct(s['P_lig'])}** · P(X ≤ {int(k)}) = {pct(s['P_hoejst'])} · "
            f"P(X > {int(k)}) = {pct(s['P_flere_end'])}\n"
            f"- μ = n·p = {num(s['middel'],2)} · σ = √(n·p·(1−p)) = {num(s['sigma'],2)}\n"
            + (f"- P({int(iv_a)} ≤ X ≤ {int(iv_b)}) = P(X ≤ {int(iv_b)}) − P(X ≤ {int(iv_a)-1}) "
               f"= **{pct(p_iv)}**\n" if interval_on else "")
            + ("- Normaltilnærmelse gyldig (n·p og n·(1−p) ≥ 5)." if ap["gyldig"]
               else "- Normaltilnærmelse ikke gyldig endnu (kræver n·p og n·(1−p) ≥ 5).")
        )


# ===========================================================================
# KONTROLKORT
# ===========================================================================
with tab_kk:
    st.subheader("Kontrolkort (SPC)")
    st.caption("Et kontrolkort tjekker om en proces (fx en produktion) er stabil over tid. Du "
               "indtaster målinger fra flere stikprøver, og værktøjet tegner en øverste og en "
               "nederste grænse. Ligger alle punkter inden for grænserne, kører processen normalt; "
               "et punkt udenfor (rødt) betyder at noget særligt er gået galt og bør undersøges. "
               "Grænserne kaldes UCL (øverste) og LCL (nederste) og ligger tre standardafvigelser "
               "fra midten, hvilket dækker 99,7 % af en normal proces.")

    korttype = st.radio("Korttype", ["p-kort (andel defekte)", "X̄- og R-kort (måling)"],
                        horizontal=True, key="kk_type",
                        help="Vælg 'p-kort' når du tæller ja/nej (fx antal defekte ud af en "
                             "stikprøve). Vælg 'X̄- og R-kort' når du måler en talværdi (fx længde "
                             "eller vægt) flere gange pr. stikprøve.")

    if korttype.startswith("p-kort"):
        st.caption("Diskret ja/nej: andel defekte pr. stikprøve.")
        default_p = pd.DataFrame({
            "Stikprøve": list(range(1, 11)),
            "Antal (n)": [100] * 10,
            "Antal fejl": [3, 5, 2, 8, 4, 6, 3, 12, 5, 4],
        })
        st.caption("Erstat eksempeltallene med dine egne: en række pr. stikprøve, hvor 'Antal (n)' "
                   "er hvor mange du tjekkede, og 'Antal fejl' er hvor mange af dem der var "
                   "defekte. Du kan tilføje og slette rækker.")
        pdf = st.data_editor(default_p, num_rows="dynamic", hide_index=True,
                             width="stretch", key="kk_pdata", height=260)
        pdf = pdf.copy()
        pdf["Antal (n)"] = pd.to_numeric(pdf["Antal (n)"], errors="coerce")
        pdf["Antal fejl"] = pd.to_numeric(pdf["Antal fejl"], errors="coerce")
        foer = len(pdf)
        pdf = pdf.dropna()
        if len(pdf) < foer:
            st.warning(f"{foer - len(pdf)} række(r) er IKKE talt med, fordi de mangler et tal "
                       "eller indeholder noget der ikke er et tal.")
        if not pdf.empty:
            r = stat.p_chart(pdf["Antal fejl"].tolist(), pdf["Antal (n)"].tolist())
            x = pdf["Stikprøve"].tolist()
            colors = [C_OPT if o else C_TOTAL for o in r["ude_af_kontrol"]]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=r["andele"], mode="lines+markers", name="Andel defekte",
                                     line=dict(color=C_TOTAL), marker=dict(color=colors, size=10)))
            fig.add_trace(go.Scatter(x=x, y=r["UCL"], mode="lines", name="UCL",
                                     line=dict(color=C_OPT, dash="dash")))
            fig.add_trace(go.Scatter(x=x, y=r["LCL"], mode="lines", name="LCL",
                                     line=dict(color=C_OPT, dash="dash")))
            fig.add_hline(y=r["pbar"], line_dash="dot", line_color=C_HOLD,
                          annotation_text=f"p̄ = {pct(r['pbar'])}")
            fig.update_layout(xaxis_title="Stikprøve", yaxis_title="Andel defekte",
                              height=430, margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), width="stretch")
            st.caption("Sådan læser du kortet: den prikkede midterlinje p̄ er den gennemsnitlige "
                       "andel defekte. De to stiplede linjer er øverste (UCL) og nederste (LCL) "
                       "grænse. Ligger alle punkter mellem dem, er processen stabil; et rødt punkt "
                       "udenfor signalerer et problem der bør undersøges.")
            n_ooc = int(np.sum(r["ude_af_kontrol"]))
            m1, m2 = st.columns(2)
            m1.metric("Centerlinje p̄", pct(r["pbar"]),
                      help="Den gennemsnitlige andel defekte på tværs af alle stikprøver. p̄ "
                           "(udtales 'p-streg') regnes som det samlede antal fejl delt med det "
                           "samlede antal tjekkede.")
            m2.metric("Punkter ude af kontrol", num(n_ooc, 0),
                      help="Antallet af stikprøver der ligger uden for grænserne (de røde "
                           "punkter). Hvert af dem peger på at noget særligt er gået galt i "
                           "processen og bør undersøges.")
            with st.expander("Mellemregninger / formel", expanded=True):
                st.markdown(
                    "- p̄ = Σfejl / Σn\n"
                    "- σ_p = √(p̄(1−p̄)/n) (varierer hvis n varierer)\n"
                    "- UCL = p̄ + 3σ_p · LCL = maks(0; p̄ − 3σ_p)"
                )
    else:
        st.caption("Kontinuert måling: hver stikprøve er flere målinger. R-kort bruges sammen med X̄-kort.")
        nsize = st.selectbox("Målinger pr. stikprøve (n)", list(range(2, 11)), index=2, key="kk_nsize",
                             help="Vælg hvor mange målinger hver stikprøve indeholder (2-10 — "
                                  "tabelkonstanterne A₂/D₃/D₄ findes for dem alle). Tager du fx "
                                  "fire målinger hver gang, vælger du 4. Tabellen får så fire "
                                  "kolonner (M1 til M4).")
        cols = [f"M{i+1}" for i in range(nsize)]
        base = {"Stikprøve": list(range(1, 9))}
        seed = [[10, 12, 11, 13, 12, 11, 12, 10, 13, 11],
                [9, 11, 10, 10, 11, 10, 9, 11, 10, 12],
                [12, 13, 11, 12, 14, 12, 13, 11, 12, 13],
                [10, 10, 12, 11, 9, 11, 10, 12, 11, 10],
                [11, 12, 13, 12, 11, 12, 11, 13, 12, 12],
                [13, 14, 12, 13, 15, 13, 12, 14, 13, 14],
                [10, 9, 11, 10, 12, 10, 11, 9, 10, 11],
                [11, 11, 10, 12, 11, 12, 10, 11, 12, 11]]
        for j, cnm in enumerate(cols):
            base[cnm] = [row[j] for row in seed]
        default_x = pd.DataFrame(base)
        st.caption("Skriv dine egne tal i tabellen: en række pr. stikprøve, og en måling i hver "
                   "M-kolonne (M1, M2 og så videre). Eksempeltallene kan bare overskrives, og du "
                   "kan tilføje og slette rækker.")
        xdf = st.data_editor(default_x, num_rows="dynamic", hide_index=True,
                             width="stretch", key="kk_xdata", height=280)
        xdf = xdf.copy()
        for cnm in cols:
            xdf[cnm] = pd.to_numeric(xdf[cnm], errors="coerce")
        foer = len(xdf)
        xdf = xdf.dropna(subset=cols)
        if len(xdf) < foer:
            st.warning(f"{foer - len(xdf)} række(r) er IKKE talt med, fordi de mangler en "
                       "måling eller indeholder noget der ikke er et tal.")
        if not xdf.empty:
            samples = xdf[cols].values.tolist()
            r = stat.xbar_r_chart(samples)
            x = xdf["Stikprøve"].tolist()
            xc = [C_OPT if o else C_TOTAL for o in r["X_ooc"]]
            rc = [C_OPT if o else C_TOTAL for o in r["R_ooc"]]
            figx = go.Figure()
            figx.add_trace(go.Scatter(x=x, y=r["means"], mode="lines+markers", name="X̄",
                                      line=dict(color=C_TOTAL), marker=dict(color=xc, size=10)))
            figx.add_hline(y=r["X_UCL"], line_dash="dash", line_color=C_OPT, annotation_text=f"UCL {num(r['X_UCL'],2)}")
            figx.add_hline(y=r["X_LCL"], line_dash="dash", line_color=C_OPT, annotation_text=f"LCL {num(r['X_LCL'],2)}")
            figx.add_hline(y=r["Xbarbar"], line_dash="dot", line_color=C_HOLD, annotation_text=f"X̿ {num(r['Xbarbar'],2)}")
            figx.update_layout(title="X̄-kort (middelværdi)", xaxis_title="Stikprøve", yaxis_title="Gennemsnit",
                               height=330, margin=dict(t=40, b=10), showlegend=False)
            st.plotly_chart(style_fig(figx), width="stretch")

            figr = go.Figure()
            figr.add_trace(go.Scatter(x=x, y=r["ranges"], mode="lines+markers", name="R",
                                      line=dict(color=C_TOTAL), marker=dict(color=rc, size=10)))
            figr.add_hline(y=r["R_UCL"], line_dash="dash", line_color=C_OPT, annotation_text=f"UCL {num(r['R_UCL'],2)}")
            figr.add_hline(y=r["R_LCL"], line_dash="dash", line_color=C_OPT, annotation_text=f"LCL {num(r['R_LCL'],2)}")
            figr.add_hline(y=r["Rbar"], line_dash="dot", line_color=C_HOLD, annotation_text=f"R̄ {num(r['Rbar'],2)}")
            figr.update_layout(title="R-kort (range)", xaxis_title="Stikprøve", yaxis_title="Range",
                               height=300, margin=dict(t=40, b=10), showlegend=False)
            st.plotly_chart(style_fig(figr), width="stretch")
            st.caption("Sådan læser du de to kort: det øverste (X̄) tjekker om gennemsnittet pr. "
                       "stikprøve er stabilt; det nederste (R, kaldet 'range') tjekker om "
                       "spredningen, altså forskellen mellem største og mindste måling, er stabil. "
                       "Begge skal være inden for grænserne, før processen er stabil. Et rødt "
                       "punkt på et af kortene signalerer et problem der bør undersøges.")

            with st.expander("Mellemregninger / formel", expanded=True):
                st.markdown(
                    f"- X̿ = {num(r['Xbarbar'],2)} · R̄ = {num(r['Rbar'],2)} · "
                    f"n = {r['n']} giver A₂ = {num(r['A2'],3)}, D₃ = {num(r['D3'],3)}, D₄ = {num(r['D4'],3)}\n"
                    f"- X̄-kort: UCL/LCL = X̿ ± A₂·R̄ = [{num(r['X_LCL'],2)} ; {num(r['X_UCL'],2)}]\n"
                    f"- R-kort: UCL = D₄·R̄ = {num(r['R_UCL'],2)} · LCL = D₃·R̄ = {num(r['R_LCL'],2)}"
                )


# ===========================================================================
# REGRESSION
# ===========================================================================
with tab_reg:
    st.subheader("Lineær regression")
    st.caption("Finder den rette linje der passer bedst til en sky af punkter, så du kan se "
               "sammenhængen mellem to tal og forudsige det ene ud fra det andet. Ret punkterne "
               "i tabellen, så reagerer linjen med det samme.")

    v, h = st.columns([1, 2])
    with v:
        st.caption("Hvert punkt har en x-værdi (det du kender) og en y-værdi (det du vil forklare). "
                   "Du kan rette tallene eller tilføje rækker.")
        default_xy = pd.DataFrame({
            "x": [10, 20, 30, 40, 50, 60, 70],
            "y": [22, 28, 41, 46, 52, 61, 68],
        })
        xydf = st.data_editor(default_xy, num_rows="dynamic", hide_index=True,
                              width="stretch", key="reg_data", height=280)

    xydf = xydf.copy()
    xydf["x"] = pd.to_numeric(xydf["x"], errors="coerce")
    xydf["y"] = pd.to_numeric(xydf["y"], errors="coerce")
    foer = len(xydf)
    xydf = xydf.dropna()
    if len(xydf) < foer:
        st.warning(f"{foer - len(xydf)} række(r) er IKKE talt med, fordi de mangler x eller y "
                   "eller indeholder noget der ikke er et tal.")

    if len(xydf) >= 2 and xydf["x"].nunique() < 2:
        # Guard: linregress crasher hvis alle x-værdier er ens
        st.warning("Alle x-værdier er ens, så der findes ingen entydig linje (den ville stå "
                   "lodret). Ret mindst ét punkt, så x-værdierne er forskellige.")
    elif len(xydf) >= 2:
        r = stat.linear_regression(xydf["x"].tolist(), xydf["y"].tolist())
        xs = np.linspace(xydf["x"].min(), xydf["x"].max(), 100)
        ys = stat.regression_predict(xs, r["haeldning"], r["skaering"])
        with h:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=xydf["x"], y=xydf["y"], mode="markers", name="Datapunkter",
                                     marker=dict(color=C_TOTAL, size=11)))
            fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name="Fittet linje",
                                     line=dict(color=C_OPT, width=3)))
            fig.update_layout(xaxis_title="x", yaxis_title="y", height=420,
                              margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
            st.plotly_chart(style_fig(fig), width="stretch")
            st.caption("Sådan læser du grafen: prikkerne er dine data, og den røde linje er den "
                       "bedste rette linje gennem dem. Jo tættere prikkerne ligger på linjen, jo "
                       "bedre passer modellen (det er det R² måler).")

        m1, m2, m3 = st.columns(3)
        m1.metric("Hældning (b)", num(r["haeldning"], 3),
                  help="Hvor meget y ændrer sig, hver gang x stiger med 1. Linjens stejlhed.")
        m2.metric("Skæring (a)", num(r["skaering"], 2),
                  help="Linjens værdi når x = 0 (hvor den skærer y-aksen).")
        m3.metric("Forklaringsgrad R²", num(r["r2"], 3),
                  help="Mellem 0 og 1. Hvor stor en del af variationen i y som x forklarer. "
                       "Tæt på 1 = linjen passer godt; tæt på 0 = svag sammenhæng.")

        st.markdown("**Forudsig en værdi**")
        cc = st.columns([1, 2])
        xpred = cc[0].number_input("Hvis x =", value=float(xydf["x"].mean()), step=1.0, key="reg_xpred",
                                   help="Den x-værdi du vil forudsige y for. Forudsigelsen er "
                                        "mest pålidelig inden for dine datapunkters område — "
                                        "længere ude er linjen ren gætteri.")
        ypred = stat.regression_predict(xpred, r["haeldning"], r["skaering"])
        cc[1].metric(f"så forudsiges y ≈", num(ypred, 2),
                     help="Sat ind i linjens ligning y = a + b·x.")

        with st.expander("Mellemregninger / formel", expanded=True):
            fortegn = "+" if r["skaering"] >= 0 else "−"
            st.latex(r"y = a + b \cdot x")
            st.markdown(
                f"- Linjen: **y = {num(r['skaering'],2)} {fortegn} {num(abs(r['haeldning']),3)}·x**\n"
                f"- Hældning b = {num(r['haeldning'],3)} · skæring a = {num(r['skaering'],2)}\n"
                f"- Korrelation r = {num(r['r'],3)} · R² = {num(r['r2'],3)} "
                f"(x forklarer {pct(r['r2'],0)} af variationen i y)"
            )
    else:
        st.info("Indtast mindst to punkter for at beregne en linje.")
