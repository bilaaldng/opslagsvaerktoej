"""Statistik — regnemaskiner med dynamiske grafer (scipy for korrekthed).

Moduler: Normalfordeling · Konfidensinterval · Binomialfordeling · Kontrolkort
(p-kort, X̄- og R-kort). Notation matcher brugerens danish-statistik-skill + VIDEN §8.
"""
import math
import os
import sys

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

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

tab_norm, tab_ki, tab_binom, tab_kk, tab_reg = st.tabs([
    "Normalfordeling", "Konfidensinterval", "Binomialfordeling", "Kontrolkort", "Regression",
])


# ===========================================================================
# NORMALFORDELING
# ===========================================================================
with tab_norm:
    st.subheader("Normalfordeling")
    st.caption("Brug denne fane når noget varierer omkring et gennemsnit (fx vægt, højde eller "
               "leveringstid). Du kan regne ud hvor sandsynligt det er at en værdi ligger i et "
               "bestemt interval, eller finde den værdi der svarer til en bestemt procentdel. "
               "Arealet under kurven er sandsynligheden, og skraveringen og tallene opdateres live.")

    v, h = st.columns([1, 2])
    with v:
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
            p_left = st.slider("Venstre haleareal (%)", 1, 99, 95, key="n_pleft",
                               help="Den procentdel der skal ligge til venstre for den værdi du "
                                    "søger. Vælger du 95 %, finder værktøjet den værdi som 95 % af "
                                    "tilfældene ligger under.") / 100

    with h:
        xs = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
        ys = stat.normal_pdf(xs, mu, sigma)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=xs, y=ys, line=dict(color=C_TOTAL, width=3), name="Tæthed"))
        if mode == "Sandsynlighed for interval":
            lo = mu - 4 * sigma if lower is None else lower
            hi = mu + 4 * sigma if upper is None else upper
            mask = (xs >= lo) & (xs <= hi)
            fig.add_trace(go.Scatter(x=xs[mask], y=ys[mask], fill="tozeroy",
                                     fillcolor="rgba(16,185,129,0.35)", line=dict(width=0),
                                     name="Areal"))
            area = stat.normal_area(lower, upper, mu, sigma)
        else:
            xval = mu + stat.prob_to_z(p_left) * sigma
            mask = xs <= xval
            fig.add_trace(go.Scatter(x=xs[mask], y=ys[mask], fill="tozeroy",
                                     fillcolor="rgba(16,185,129,0.35)", line=dict(width=0),
                                     name="Areal"))
            fig.add_vline(x=xval, line_dash="dash", line_color=C_OPT)
        fig.update_layout(xaxis_title="x", yaxis_title="Tæthed", height=420,
                          margin=dict(t=30, b=10), legend=dict(orientation="h", y=1.12))
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: det grønne skraverede område er svaret, og dets "
                   "størrelse i forhold til hele kurven er sandsynligheden. Hele arealet under "
                   "kurven er 100 %. Y-aksen 'Tæthed' er bare kurvens højde, ikke et tal du selv "
                   "skal aflæse.")

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
        st.metric("x ved valgt percentil", num(xval, 2),
                  help="Den x-værdi hvor det valgte haleareal til venstre er nået.")
        st.caption(f"z for {num(p_left*100,0)} % = {num(stat.prob_to_z(p_left),3)}, "
                   f"så x = μ + z·σ = {num(xval,2)}.")


# ===========================================================================
# KONFIDENSINTERVAL
# ===========================================================================
with tab_ki:
    st.subheader("Konfidensinterval")
    st.caption("Intervallet der med valgt sikkerhed indeholder den sande værdi. "
               "Smallere ved større stikprøve.")

    art = st.radio("Type", ["Middelværdi", "Andel"], horizontal=True, key="ki_art",
                   help="Vælg 'Middelværdi' når du måler noget (fx gennemsnitlig vægt eller tid). "
                        "Vælg 'Andel' når du tæller en procentdel (fx hvor mange procent er "
                        "defekte eller tilfredse).")
    conf = st.select_slider("Konfidensniveau", options=[0.90, 0.95, 0.99], value=0.95,
                            format_func=lambda x: f"{int(x*100)} %", key="ki_conf")

    if art == "Middelværdi":
        c = st.columns(3)
        mean = c[0].number_input("Gennemsnit", value=50.0, step=1.0, key="ki_mean",
                                 help="Gennemsnittet du har målt i din stikprøve. Det bliver "
                                      "midten af konfidensintervallet.")
        s = c[1].number_input("Std.afvigelse s", min_value=0.0, value=10.0, step=0.5, key="ki_s",
                              help="Hvor meget dine målinger spreder sig omkring gennemsnittet i "
                                   "din stikprøve. Det lille s står for stikprøvens "
                                   "standardafvigelse. Får du den oplyst i opgaven, taster du den "
                                   "bare ind.")
        n = c[2].number_input("Stikprøvestørrelse n", min_value=2, value=25, step=1, key="ki_n",
                              help="Antal observationer i din stikprøve, altså hvor mange du har "
                                   "målt eller spurgt. Jo større n, jo smallere bliver intervallet.")
        r = stat.ci_mean(mean, s, int(n), conf)
        est, me = mean, r["margin"]
        formel = (f"- t({int(conf*100)} %, {int(n)-1}) = {num(r['t'],3)} · "
                  f"standardfejl = s/√n = {num(r['std_error'],3)}\n"
                  f"- ME = t·s/√n = **{num(me,3)}**\n"
                  f"- KI = {num(mean,2)} ± {num(me,2)} = **[{num(r['nedre'],2)} ; {num(r['oevre'],2)}]**")
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

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[est], y=[0], mode="markers", marker=dict(color=C_TOTAL, size=14),
                             error_x=dict(type="data", array=[me], color=C_OPT, thickness=3, width=14),
                             name="Estimat ± ME"))
    fig.update_layout(height=200, margin=dict(t=20, b=10), yaxis=dict(visible=False, range=[-1, 1]),
                      xaxis_title=("Andel" if art == "Andel" else "Værdi"), showlegend=False)
    st.plotly_chart(style_fig(fig), use_container_width=True)
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
        p = st.slider("Sandsynlighed p (%)", 1, 99, 30, key="b_p",
                      help="Chancen for succes i et enkelt forsøg, i procent. Er der fx 30 % "
                           "chance for at en vare er defekt, sætter du den til 30 %. En 'succes' "
                           "er bare det udfald du tæller efter.") / 100
        k = st.number_input("Antal succeser k", min_value=0, max_value=int(n), value=min(6, int(n)), step=1, key="b_k",
                            help="Hvor mange af forsøgene du vil regne på, fx præcis 6 defekte ud "
                                 "af de 20. k er altså et bestemt antal succeser blandt de n forsøg.")

    s = stat.binom_summary(int(n), p, int(k))
    with h:
        xs = np.arange(0, int(n) + 1)
        pmf = [stat.binom_pmf(int(x), int(n), p) for x in xs]
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
        st.plotly_chart(style_fig(fig), use_container_width=True)
        st.caption("Sådan læser du grafen: hver søjle viser sandsynligheden for præcis det antal "
                   "succeser. Den fremhævede søjle er dit valgte k. Den stiplede kurve er en glat "
                   "tilnærmelse, der kun er pålidelig når stikprøven er stor nok (se noten i "
                   "Mellemregninger).")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric(f"P(X = {int(k)})", pct(s["P_lig"]), help="Præcis k succeser.")
    m2.metric(f"P(X ≤ {int(k)})", pct(s["P_hoejst"]), help="Højst k succeser (kumuleret).")
    m3.metric(f"P(X ≥ {int(k)})", pct(s["P_mindst"]), help="Mindst k succeser.")
    m4.metric("Middelværdi μ", num(s["middel"], 2),
              help="Det antal succeser du i gennemsnit kan forvente. Med 20 forsøg og 30 % chance "
                   "forventer du 6 succeser. Regnes som μ = n·p, og spredningen er "
                   "σ = √(n·p·(1−p)).")
    with st.expander("Mellemregninger / formel", expanded=True):
        st.latex(r"P(X=k) = \binom{n}{k} p^{k} (1-p)^{n-k}")
        st.markdown(
            f"- P(X = {int(k)}) = **{pct(s['P_lig'])}** · P(X ≤ {int(k)}) = {pct(s['P_hoejst'])} · "
            f"P(X > {int(k)}) = {pct(s['P_flere_end'])}\n"
            f"- μ = n·p = {num(s['middel'],2)} · σ = √(n·p·(1−p)) = {num(s['sigma'],2)}\n"
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
                             use_container_width=True, key="kk_pdata", height=260)
        pdf = pdf.copy()
        pdf["Antal (n)"] = pd.to_numeric(pdf["Antal (n)"], errors="coerce")
        pdf["Antal fejl"] = pd.to_numeric(pdf["Antal fejl"], errors="coerce")
        pdf = pdf.dropna()
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
            st.plotly_chart(style_fig(fig), use_container_width=True)
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
        nsize = st.selectbox("Målinger pr. stikprøve (n)", [2, 3, 4, 5], index=2, key="kk_nsize",
                             help="Vælg hvor mange målinger hver stikprøve indeholder. Tager du "
                                  "fx fire målinger hver gang, vælger du 4. Tabellen får så fire "
                                  "kolonner (M1 til M4).")
        cols = [f"M{i+1}" for i in range(nsize)]
        base = {"Stikprøve": list(range(1, 9))}
        seed = [[10, 12, 11, 13, 12], [9, 11, 10, 10, 11], [12, 13, 11, 12, 14],
                [10, 10, 12, 11, 9], [11, 12, 13, 12, 11], [13, 14, 12, 13, 15],
                [10, 9, 11, 10, 12], [11, 11, 10, 12, 11]]
        for j, cnm in enumerate(cols):
            base[cnm] = [row[j] for row in seed]
        default_x = pd.DataFrame(base)
        st.caption("Skriv dine egne tal i tabellen: en række pr. stikprøve, og en måling i hver "
                   "M-kolonne (M1, M2 og så videre). Eksempeltallene kan bare overskrives, og du "
                   "kan tilføje og slette rækker.")
        xdf = st.data_editor(default_x, num_rows="dynamic", hide_index=True,
                             use_container_width=True, key="kk_xdata", height=280)
        xdf = xdf.copy()
        for cnm in cols:
            xdf[cnm] = pd.to_numeric(xdf[cnm], errors="coerce")
        xdf = xdf.dropna(subset=cols)
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
            st.plotly_chart(style_fig(figx), use_container_width=True)

            figr = go.Figure()
            figr.add_trace(go.Scatter(x=x, y=r["ranges"], mode="lines+markers", name="R",
                                      line=dict(color=C_TOTAL), marker=dict(color=rc, size=10)))
            figr.add_hline(y=r["R_UCL"], line_dash="dash", line_color=C_OPT, annotation_text=f"UCL {num(r['R_UCL'],2)}")
            figr.add_hline(y=r["R_LCL"], line_dash="dash", line_color=C_OPT, annotation_text=f"LCL {num(r['R_LCL'],2)}")
            figr.add_hline(y=r["Rbar"], line_dash="dot", line_color=C_HOLD, annotation_text=f"R̄ {num(r['Rbar'],2)}")
            figr.update_layout(title="R-kort (range)", xaxis_title="Stikprøve", yaxis_title="Range",
                               height=300, margin=dict(t=40, b=10), showlegend=False)
            st.plotly_chart(style_fig(figr), use_container_width=True)
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
                              use_container_width=True, key="reg_data", height=280)

    xydf = xydf.copy()
    xydf["x"] = pd.to_numeric(xydf["x"], errors="coerce")
    xydf["y"] = pd.to_numeric(xydf["y"], errors="coerce")
    xydf = xydf.dropna()

    if len(xydf) >= 2:
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
            st.plotly_chart(style_fig(fig), use_container_width=True)
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
        xpred = cc[0].number_input("Hvis x =", value=float(xydf["x"].mean()), step=1.0, key="reg_xpred")
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
