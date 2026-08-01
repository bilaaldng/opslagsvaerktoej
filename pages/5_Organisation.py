"""Organisation — søgbart modelkatalog, modelvælger og visualiseringer.

Blødt fag: ingen regnemaskine, men et opslagsbibliotek. Modelkataloget dækker
det klassiske organisationspensum (Porter,
Ansoff, SC-strategi, struktur, organisk/mekanistisk, McGregor, Schein,
Blake & Mouton, Adizes, Hofstede, Herzberg, klankultur og ESG/CSRD-presset).
Hver model: hvad den er, hvornår man bruger den, og dens kritik/begrænsninger.
Dertil interaktive kvadrant-figurer for Ansoff og ledergitteret (samme
mønster som interessent-grid'et på Kommunikations-siden).
"""
import os
import sys

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_theme import (  # noqa: E402
    inject_css, vis_fig, C_TOTAL, C_OPT, C_MUTED,
)

st.set_page_config(page_title="Organisation", page_icon="🧭", layout="wide")
inject_css()

st.title("🧭 Organisation")
st.caption("Søgbart modelkatalog og en modelvælger. Det svære til eksamen er at vælge "
           "den rigtige model, så start i Modelvælger hvis du har en situation, og slå "
           "detaljerne op i Modelkatalog.")

# Situationer brugt af modelvælgeren (label vist til brugeren)
S_KONK = "Konkurrencestrategi (hvordan vinder vi kunder)"
S_VAEKST = "Vækst (nye produkter eller markeder)"
S_STRUK = "Organisationsstruktur eller silotænkning"
S_LEDELSE = "Ledelsesstil"
S_MOTIV = "Motivation og menneskesyn"
S_KULTUR = "Kultur og internationalt samarbejde"
S_FORANDRING = "Forandring"
S_SC = "Design af forsyningskæden"
S_OMGIV = "Pres fra omgivelserne (ESG, kunder, bank)"

MODELLER = [
    {
        "navn": "Porters generiske strategier",
        "kat": "Strategi & struktur",
        "hvad": "Tre måder at skabe en konkurrencefordel på: **omkostningsleder** (være "
                "billigst), **differentiering** (være unik og tage en højere pris), og **fokus** "
                "(de samme to, men rettet mod et snævert delmarked).",
        "hvornaar": "Når du skal forklare HVORDAN en virksomhed vil vinde kunder og tjene penge.",
        "kritik": "Hvis man prøver at være både billigst og unik på én gang, ender man ofte "
                  "'stuck in the middle' og taber på forvirringen. Nogle virksomheder kan dog "
                  "godt begge dele via fx teknologi. Modellen siger lidt om selve eksekveringen.",
        "soeg": ["porter", "konkurrence", "pris", "differentiering", "omkostningsleder", "fokus", "strategi"],
        "sit": [S_KONK],
    },
    {
        "navn": "Ansoffs vækstmatrix",
        "kat": "Strategi & struktur",
        "hvad": "Fire vækstretninger ud fra om produktet og markedet er nyt eller eksisterende: "
                "**markedspenetrering** (mere af det samme), **markedsudvikling** (kendt produkt "
                "på nyt marked), **produktudvikling** (nyt produkt til kendte kunder) og "
                "**diversifikation** (nyt produkt på nyt marked, den farligste).",
        "hvornaar": "Når virksomheden vil vokse og skal vælge en retning.",
        "kritik": "Siger intet om HVORDAN væksten gennemføres, og kun lidt om risiko ud over at "
                  "diversifikation er farlig. Det er et øjebliksbillede.",
        "soeg": ["ansoff", "vækst", "marked", "produkt", "ekspansion", "diversifikation"],
        "sit": [S_VAEKST],
    },
    {
        "navn": "Generisk SC-strategi (lean vs. agil)",
        "kat": "Strategi & struktur",
        "hvad": "To grundtyper forsyningskæde: **lean/efficient** (lave omkostninger, passer til "
                "stabil og forudsigelig efterspørgsel) og **responsiv/agil** (hurtig og fleksibel, "
                "passer til uforudsigelig efterspørgsel). Der skal være harmoni mellem "
                "konkurrencestrategien og forsyningskæden.",
        "hvornaar": "Når du skal designe eller vurdere forsyningskæden ud fra produktets efterspørgselsmønster.",
        "kritik": "I praksis er kæder ofte en blanding ('leagile'), og det er svært at skifte "
                  "hurtigt mellem de to.",
        "soeg": ["forsyningskæde", "lean", "agil", "responsiv", "efterspørgsel", "sc"],
        "sit": [S_SC, S_KONK],
    },
    {
        "navn": "Organisationsstruktur",
        "kat": "Strategi & struktur",
        "hvad": "Hvordan virksomheden er bygget op: **funktionsopdelt** (specialister samlet, fx "
                "alt indkøb ét sted, som giver stordrift men silotænkning) eller **objektopdelt** "
                "(efter produkt, marked eller kunde). **Linje** har beslutningsmagt, **stab** "
                "rådgiver. **Kontrolspænd** er antal medarbejdere pr. leder, og **niveauer** er "
                "hvor højt hierarkiet er (flad eller høj organisation).",
        "hvornaar": "Når du skal beskrive eller forbedre, hvordan ansvar og arbejde er fordelt.",
        "kritik": "Ingen struktur er bedst i sig selv. Den skal passe til strategien (harmoni). "
                  "Funktionsopdeling skaber typisk silo-problemer på tværs af afdelinger.",
        "soeg": ["struktur", "silo", "hierarki", "afdeling", "kontrolspænd", "linje", "stab", "funktion", "objekt"],
        "sit": [S_STRUK],
    },
    {
        "navn": "Organisk vs. mekanistisk organisation",
        "kat": "Strategi & struktur",
        "hvad": "**Organisk** er flad, fleksibel og decentral (beslutninger tæt på opgaven) og "
                "passer til foranderlige markeder. **Mekanistisk** er hierarkisk, regelstyret og "
                "central og passer til stabile markeder.",
        "hvornaar": "Når du vurderer, om organisationsformen passer til hvor stabilt eller "
                    "foranderligt markedet er.",
        "kritik": "En forenkling. De fleste virksomheder er en blanding, og 'foranderligt marked' "
                  "er i sig selv en vurdering.",
        "soeg": ["organisk", "mekanistisk", "fleksibel", "hierarki", "decentral", "central"],
        "sit": [S_STRUK, S_FORANDRING],
    },
    {
        "navn": "McGregor Teori X / Teori Y",
        "kat": "Ledelse & kultur",
        "hvad": "To menneskesyn hos lederen. **Teori X**: medarbejdere er dovne og skal "
                "kontrolleres og detailstyres. **Teori Y**: de er ansvarsbevidste, motiverer sig "
                "selv og bør inddrages.",
        "hvornaar": "Når du skal forklare en leders stil og dens effekt på motivation.",
        "kritik": "Meget firkantet (enten/eller). Virkeligheden ligger imellem, og hvad der "
                  "virker afhænger af kultur og situation.",
        "soeg": ["mcgregor", "teori x", "teori y", "menneskesyn", "kontrol", "motivation", "ledelse"],
        "sit": [S_LEDELSE, S_MOTIV],
    },
    {
        "navn": "Scheins menneskesyn",
        "kat": "Ledelse & kultur",
        "hvad": "Fire antagelser om hvad der driver mennesker: **rationel-økonomisk** (penge), "
                "**socialt** (fællesskab), **selvrealiserende** (udvikling) og **komplekst** "
                "(skifter alt efter situationen). Synet styrer, hvordan man bør lede.",
        "hvornaar": "Når du vil nuancere motivation ud over McGregors X/Y.",
        "kritik": "Beskrivende snarere end en opskrift, og det er svært at måle, hvilket syn der "
                  "passer til en konkret medarbejder.",
        "soeg": ["schein", "menneskesyn", "motivation", "rationel", "social", "selvrealiserende"],
        "sit": [S_MOTIV, S_LEDELSE],
    },
    {
        "navn": "Ledergitteret (Blake & Mouton)",
        "kat": "Ledelse & kultur",
        "hvad": "Lederstil på to akser: omsorg for **opgaven/produktionen** og omsorg for "
                "**menneskene**. Yderpunkter: 1.1 (forarmet, ligeglad), 9.1 (autoritær, kun "
                "opgave), 1.9 (country club, kun mennesker), 5.5 (midterpunkt) og **9.9 (team)** "
                "som regnes for idealet.",
        "hvornaar": "Når du skal kortlægge og forbedre en konkret lederstil.",
        "kritik": "Antager at 9.9 altid er bedst og tager ikke højde for situationen — en "
                  "presset deadline eller en uerfaren medarbejder kan kræve mere styring end "
                  "9.9 lægger op til. Brug gitteret som kort, ikke som facitliste.",
        "soeg": ["ledergitter", "blake", "mouton", "lederstil", "opgave", "mennesker", "9.9"],
        "sit": [S_LEDELSE],
    },
    {
        "navn": "Adizes lederroller (PAEI)",
        "kat": "Ledelse & kultur",
        "hvad": "Fire roller en ledelse skal dække: **P**roducer (skaber resultater), "
                "**A**dministrator (system og orden), **E**ntreprenør (vision og forandring) og "
                "**I**ntegrator (mennesker og team). Ingen person kan dække alle fire, så der skal "
                "et komplementært team til.",
        "hvornaar": "Når du skal vurdere, om ledelsen eller teamet mangler en bestemt rolle.",
        "kritik": "Der er ingen klar måling, og man risikerer at sætte folk i bås.",
        "soeg": ["adizes", "paei", "lederroller", "team", "producer", "integrator", "entreprenør"],
        "sit": [S_LEDELSE, S_FORANDRING],
    },
    {
        "navn": "Hofstedes kulturdimensioner",
        "kat": "Ledelse & kultur",
        "hvad": "Seks dimensioner der beskriver national kultur: **magtdistance**, "
                "**individualisme/kollektivisme**, **maskulinitet/femininitet**, "
                "**usikkerhedsundvigelse**, **langtids-/korttidsorientering** og "
                "**eftergivenhed/tilbageholdenhed**. Bruges til at forklare friktion mellem lande.",
        "hvornaar": "Når du skal forklare gnidninger i internationale leverandør- eller "
                    "kunderelationer.",
        "kritik": "Bygger på ældre, generaliserede data, lande er ikke ensartede indeni, og der "
                  "er risiko for at det bliver til stereotyper.",
        "soeg": ["hofstede", "kultur", "international", "magtdistance", "dimensioner", "interkulturel"],
        "sit": [S_KULTUR],
    },
    {
        "navn": "Herzbergs to-faktor-teori",
        "kat": "Ledelse & kultur",
        "hvad": "Trivsel på jobbet har to slags knapper: **hygiejnefaktorer** (løn, bemanding, "
                "arbejdsforhold) der gør folk SURE, hvis de mangler — og **motivationsfaktorer** "
                "(ansvar, anerkendelse, udvikling) der gør folk GLADE og engagerede. Hygiejne "
                "fjerner utilfredshed, men skaber ikke i sig selv motivation.",
        "hvornaar": "Når du skal forklare mistrivsel, stigende sygefravær eller høj personale-"
                    "omsætning — og skelne mellem hvad der slukker branden (hygiejne) og hvad "
                    "der tænder gnisten (motivation). Svigter BEGGE, skal der sættes ind begge "
                    "steder.",
        "kritik": "Skellet er ikke knivskarpt i praksis (løn kan fx også motivere i en periode), "
                  "og hvad der er hygiejne for én, kan være motivation for en anden. Brug den "
                  "som sorteringsværktøj, ikke som facitliste.",
        "soeg": ["herzberg", "to-faktor", "tofaktor", "hygiejne", "motivationsfaktor", "trivsel",
                 "sygefravær", "personaleomsætning", "anerkendelse"],
        "sit": [S_MOTIV],
    },
    {
        "navn": "Klankultur / familiekultur",
        "kat": "Ledelse & kultur",
        "hvad": "En firmakultur der er som en familie — hyggelig og tæt, ofte samlet om én "
                "central person. Bagsiden: man bliver **konfliktsky**, møderne er hyggelige men "
                "sjældent beslutningsdygtige, og uenigheder udskydes i stedet for at blive løst.",
        "hvornaar": "Når du skal sætte ord på en kultur, hvor alt går gennem én person, der ikke "
                    "skrives referat, og de svære beslutninger aldrig bliver taget.",
        "kritik": "En etiket, ikke en forklaring: den beskriver mønstret, men siger ikke hvordan "
                  "man ændrer det. Og en tæt kultur har også styrker (loyalitet, kort vej til "
                  "chefen), som analysen ikke må overse.",
        "soeg": ["klankultur", "familiekultur", "kultur", "konfliktsky", "beslutningsdygtig",
                 "referat", "clan"],
        "sit": [S_KULTUR, S_LEDELSE],
    },
    {
        "navn": "ESG og CSRD — pres fra omgivelserne",
        "kat": "Omgivelser & ESG",
        "hvad": "EU skærper kravene til **dokumenteret** bæredygtighed: **CSRD** "
                "(rapporteringskrav), EU's tekstilforordning og **digitale produktpas fra "
                "2027**. Presset kommer ikke kun fra loven — store kunder kræver dokumentation "
                "for arbejdsforhold og CO2-aftryk, og det koster reelt bemanding at levere den.",
        "hvornaar": "Når du analyserer virksomhedens samspil med omgivelserne: lovkrav, "
                    "kundekrav og bankens blik på risiko trækker samme vej. Pointen er "
                    "rækkefølgen — dokumentationen skal på plads, FØR man markedsfører sig på "
                    "bæredygtighed.",
        "kritik": "En Code of Conduct, der kun er udleveret som bilag uden underskrift og uden "
                  "audits, er ord — ikke dokumentation. At love mere end man kan holde "
                  "(greenwashing) er værre end at love mindre. Og kravene flytter sig: tjek "
                  "altid årstal og omfang i den konkrete opgave.",
        "soeg": ["esg", "csrd", "bæredygtighed", "produktpas", "code of conduct", "audit",
                 "co2", "greenwashing", "omgivelser", "tekstilforordning"],
        "sit": [S_OMGIV],
    },
]

ALLE_SIT = [S_KONK, S_VAEKST, S_STRUK, S_LEDELSE, S_MOTIV, S_KULTUR, S_FORANDRING, S_SC, S_OMGIV]

SCORE_TIP = ("🎓 **Sådan scorer du point:** 1) Navngiv modellen og definér den kort → "
             "2) anvend den på casens konkrete situation og tal → 3) nævn kritikken/"
             "begrænsningen → 4) konkludér med DIN egen vurdering.")

# --- Modulvælger (erstatter tabs, så der kan deep-linkes fra andre sider) --
MODULER = ["Modelvælger", "Modelkatalog", "Ansoff & ledergitter"]

# Deep-link-konvention: andre sider sætter st.session_state['goto_modul']
# lige før st.switch_page — læses HER, før modulvælger-widgetten oprettes.
goto = st.session_state.pop("goto_modul", None)
if goto in MODULER:
    st.session_state["org_modul"] = goto
if "org_modul" not in st.session_state:
    st.session_state["org_modul"] = MODULER[0]

modul = st.pills("Vælg modul", MODULER, key="org_modul",
                 label_visibility="collapsed")
if modul is None:          # brugeren har klikket det valgte modul væk
    modul = MODULER[0]


# ===========================================================================
# MODELVÆLGER
# ===========================================================================
if modul == "Modelvælger":
    st.subheader("Modelvælger")
    st.caption("Vælg den eller de situationer din case handler om, så foreslår værktøjet de "
               "modeller der passer. Det er netop modelvalget der giver point til eksamen.")

    valgte = st.multiselect("Hvad handler din situation om?", ALLE_SIT,
                            help="Du kan vælge flere. Hvert valg viser de modeller der typisk "
                                 "bruges til netop den slags problem.")

    if valgte:
        forslag = [m for m in MODELLER if any(s in m["sit"] for s in valgte)]
        st.markdown(f"**{len(forslag)} modeller passer:**")
        for m in forslag:
            with st.container(border=True):
                st.markdown(f"### {m['navn']}")
                st.markdown(m["hvad"])
                st.caption(f"**Hvornår:** {m['hvornaar']}")
                st.markdown(f"**Kritik:** {m['kritik']}")
    else:
        st.info("Vælg mindst én situation ovenfor for at få forslag.", icon="👆")


# ===========================================================================
# MODELKATALOG
# ===========================================================================
elif modul == "Modelkatalog":
    st.subheader("Modelkatalog")
    st.caption("Slå hver model op med hvad den er, hvornår man bruger den, og dens "
               "begrænsninger (kritikken giver point til eksamen).")

    c1, c2 = st.columns([2, 1])
    with c1:
        soeg = st.text_input("Søg model (fx 'ansoff', 'kultur', 'silo', 'hygiejne')", key="org_soeg",
                             help="Søger i modelnavne, nøgleord OG selve beskrivelsen/kritikken — "
                                  "så fx 'stuck in the middle' og 'silotænkning' også rammer.").lower().strip()
    with c2:
        kat = st.selectbox("Kategori", ["Alle"] + sorted({m["kat"] for m in MODELLER}),
                           key="org_kat")

    vist = 0
    for m in MODELLER:
        if kat != "Alle" and m["kat"] != kat:
            continue
        # Søg bredt: navn, nøgleord og hele teksten (hvad/hvornår/kritik)
        tekst = " ".join([m["navn"], m["hvad"], m["hvornaar"], m["kritik"],
                          " ".join(m["soeg"])]).lower()
        if soeg and soeg not in tekst:
            continue
        vist += 1
        with st.expander(f"{m['navn']}  ·  {m['kat']}", expanded=bool(soeg)):
            st.markdown(f"**Hvad er det?** {m['hvad']}")
            st.markdown(f"**Hvornår bruges den?** {m['hvornaar']}")
            st.markdown(f"**Kritik og begrænsninger:** {m['kritik']}")
            st.caption(SCORE_TIP)
    if vist == 0:
        st.info("Ingen model matchede søgningen.")

# ===========================================================================
# ANSOFF & LEDERGITTER — interaktive kvadrant-figurer
# ===========================================================================
elif modul == "Ansoff & ledergitter":
    st.subheader("Ansoffs vækstmatrix — placér casens tiltag")
    st.caption("Skriv casens vækst-tiltag i tabellen og vælg, om produktet og markedet er nyt "
               "eller eksisterende — så lander tiltaget i den rigtige kvadrant. Til eksamen: "
               "navngiv kvadranten og argumentér ud fra risikoen (diversifikation er farligst).")

    c1, c2 = st.columns([1, 2])
    with c1:
        default_a = pd.DataFrame({
            "Tiltag": ["Sælg mere til nuværende kunder", "Kendt produkt til nyt land",
                       "Ny produktlinje til kendte kunder"],
            "Produkt": ["Eksisterende", "Eksisterende", "Nyt"],
            "Marked": ["Eksisterende", "Nyt", "Eksisterende"],
        })
        adf = st.data_editor(
            default_a, num_rows="dynamic", hide_index=True, width="stretch",
            key="org_ansoff", height=220,
            column_config={
                "Produkt": st.column_config.SelectboxColumn(
                    "Produkt", options=["Eksisterende", "Nyt"],
                    help="Er det et produkt virksomheden allerede har, eller noget nyt?"),
                "Marked": st.column_config.SelectboxColumn(
                    "Marked", options=["Eksisterende", "Nyt"],
                    help="Sælges der til de kunder man har i dag, eller til et nyt "
                         "marked/segment/land?"),
            })
        st.caption("Tilføj selv rækker med casens tiltag — fx et nyt brand, et nyt "
                   "eksportmarked eller mersalg til de nuværende forhandlere.")
    with c2:
        KVAD = {
            ("Eksisterende", "Eksisterende"): ("Markedspenetrering", "mere af det samme — laveste risiko"),
            ("Eksisterende", "Nyt"): ("Markedsudvikling", "kendt produkt på nyt marked"),
            ("Nyt", "Eksisterende"): ("Produktudvikling", "nyt produkt til kendte kunder"),
            ("Nyt", "Nyt"): ("Diversifikation", "nyt produkt på nyt marked — den farligste"),
        }
        fig = go.Figure()
        # Kvadrantfarver: grøn (lav risiko) nederst tv., rød (høj risiko) øverst th.
        fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1, fillcolor="rgba(16,185,129,0.08)", line_width=0)
        fig.add_shape(type="rect", x0=1, y0=0, x1=2, y1=1, fillcolor="rgba(245,158,11,0.08)", line_width=0)
        fig.add_shape(type="rect", x0=0, y0=1, x1=1, y1=2, fillcolor="rgba(245,158,11,0.08)", line_width=0)
        fig.add_shape(type="rect", x0=1, y0=1, x1=2, y1=2, fillcolor="rgba(239,68,68,0.10)", line_width=0)
        for x, y, t in [(0.5, 0.06, "Markedspenetrering"), (1.5, 0.06, "Produktudvikling"),
                        (0.5, 1.94, "Markedsudvikling"), (1.5, 1.94, "Diversifikation")]:
            fig.add_annotation(x=x, y=y, text=t, showarrow=False,
                               font=dict(color="#94a3b8", size=13))
        # Placér tiltagene med en lille fast forskydning, så flere i samme
        # kvadrant ikke skriver oven i hinanden
        offs = [(0.0, 0.12), (-0.26, -0.06), (0.26, -0.06), (-0.26, 0.28), (0.26, 0.28), (0.0, -0.24)]
        taeller = {}
        for _, r in adf.iterrows():
            navn = str(r.get("Tiltag") or "").strip()
            p, m = r.get("Produkt"), r.get("Marked")
            if not navn or p not in ("Eksisterende", "Nyt") or m not in ("Eksisterende", "Nyt"):
                continue
            bx = 0.5 if p == "Eksisterende" else 1.5
            by = 0.5 if m == "Eksisterende" else 1.5
            k = taeller.get((bx, by), 0)
            taeller[(bx, by)] = k + 1
            dx, dy = offs[k % len(offs)]
            kv_navn, kv_tekst = KVAD[(p, m)]
            fig.add_trace(go.Scatter(
                x=[bx + dx], y=[by + dy], mode="markers+text", text=[navn],
                textposition="top center", marker=dict(color=C_TOTAL, size=13),
                hovertemplate=f"<b>{navn}</b><br>{kv_navn}: {kv_tekst}<extra></extra>",
                showlegend=False))
        fig.add_vline(x=1, line_dash="dot", line_color=C_MUTED)
        fig.add_hline(y=1, line_dash="dot", line_color=C_MUTED)
        fig.update_layout(
            xaxis=dict(tickvals=[0.5, 1.5], ticktext=["Eksisterende", "Nyt"],
                       title="Produkt", range=[0, 2]),
            yaxis=dict(tickvals=[0.5, 1.5], ticktext=["Eksisterende", "Nyt"],
                       title="Marked", range=[0, 2]),
            height=430, margin=dict(t=20, b=10), showlegend=False)
        vis_fig(fig)

    st.divider()
    st.subheader("Ledergitteret (Blake & Mouton) — plot lederstilen")
    st.caption("Giv hver leder en score fra 1 til 9 på **omsorg for opgaven** og **omsorg for "
               "menneskene** — så ser du hvilken arketype stilen ligger tættest på. "
               "Notationen er (opgave.mennesker), fx 9.1 = fuld fokus på opgaven.")

    c1, c2 = st.columns([1, 2])
    with c1:
        default_l = pd.DataFrame({
            "Leder": ["Leder A", "Leder B"],
            "Opgave (1-9)": [8, 5],
            "Mennesker (1-9)": [3, 8],
        })
        ldf = st.data_editor(
            default_l, num_rows="dynamic", hide_index=True, width="stretch",
            key="org_gitter", height=180,
            column_config={
                "Opgave (1-9)": st.column_config.NumberColumn(
                    "Opgave (1-9)", min_value=1, max_value=9, step=1,
                    help="Hvor optaget er lederen af resultater, deadlines og produktion? "
                         "1 = slet ikke, 9 = meget."),
                "Mennesker (1-9)": st.column_config.NumberColumn(
                    "Mennesker (1-9)", min_value=1, max_value=9, step=1,
                    help="Hvor optaget er lederen af trivsel, relationer og medarbejdernes "
                         "behov? 1 = slet ikke, 9 = meget."),
            })
        st.caption("Skriv fx casens ledere ind og sammenlign — hvor langt er stilen fra 9.9?")
    with c2:
        ARKETYPER = [
            (1, 1, "1.1 Forarmet", "ligeglad med både opgave og mennesker"),
            (9, 1, "9.1 Autoritær", "kun opgaven tæller — mennesker er et middel"),
            (1, 9, "1.9 Country club", "kun menneskene tæller — hyggeligt, men lav ydelse"),
            (5, 5, "5.5 Midterpunkt", "kompromis: middel på begge dele"),
            (9, 9, "9.9 Team", "høj på begge — regnes for idealet"),
        ]
        fig = go.Figure()
        fig.add_vline(x=5, line_dash="dot", line_color=C_MUTED)
        fig.add_hline(y=5, line_dash="dot", line_color=C_MUTED)
        for x, y, navn, tekst in ARKETYPER:
            fig.add_trace(go.Scatter(
                x=[x], y=[y], mode="markers", marker=dict(color=C_MUTED, size=11, symbol="diamond"),
                hovertemplate=f"<b>{navn}</b>: {tekst}<extra></extra>", showlegend=False))
            fig.add_annotation(x=x, y=y + 0.45 if y < 9 else y - 0.5, text=navn,
                               showarrow=False, font=dict(color="#94a3b8", size=12))
        ldf = ldf.copy()
        ldf["Opgave (1-9)"] = pd.to_numeric(ldf["Opgave (1-9)"], errors="coerce").clip(1, 9)
        ldf["Mennesker (1-9)"] = pd.to_numeric(ldf["Mennesker (1-9)"], errors="coerce").clip(1, 9)
        ldf = ldf.dropna(subset=["Opgave (1-9)", "Mennesker (1-9)"])
        if not ldf.empty:
            fig.add_trace(go.Scatter(
                x=ldf["Opgave (1-9)"], y=ldf["Mennesker (1-9)"], mode="markers+text",
                text=ldf["Leder"].fillna("").astype(str), textposition="bottom center",
                marker=dict(color=C_OPT, size=14),
                hovertemplate="<b>%{text}</b>: %{x:.0f}.%{y:.0f}<extra></extra>",
                showlegend=False))
        fig.update_layout(
            xaxis=dict(title="Omsorg for opgaven/produktionen", range=[0.4, 9.6],
                       tickvals=list(range(1, 10))),
            yaxis=dict(title="Omsorg for menneskene", range=[0.4, 9.9],
                       tickvals=list(range(1, 10))),
            height=430, margin=dict(t=20, b=10), showlegend=False)
        vis_fig(fig)
    st.caption("Husk kritikken, når du bruger gitteret til eksamen: 9.9 er ikke altid det "
               "rigtige svar — situationen (tidspres, erfaring) kan kræve en anden stil. "
               "Se kritikfeltet under modellen i 📚 Modelkatalog.")

st.divider()
st.caption("Bemærk: Porters værdikæde har sit eget modul (den har en fast analysestruktur) — "
           "se 🔗 Værdikædeanalyse i menuen. Kommunikationsmodellen ligger under faget Kommunikation.")
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/0_Værdikædeanalyse.py", label="🔗 Åbn Værdikædeanalyse", icon="🔗")
with c2:
    if st.button("🎓 Træn eksamensspørgsmål i Organisation",
                 help="Åbner Forsvarstræneren med fag-filteret sat til Organisation."):
        st.session_state["ex_fag"] = "Organisation"
        st.switch_page("pages/7_Forsvarstræner.py")
