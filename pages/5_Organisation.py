"""Organisation — søgbart modelkatalog + modelvælger.

Blødt fag: ingen regnemaskine, men et opslagsbibliotek. Modeller matcher
brugerens VIDEN_Organisation (Porter, Ansoff, SC-strategi, struktur,
organisk/mekanistisk, McGregor, Schein, Blake & Mouton, Adizes, Hofstede).
Hver model: hvad den er, hvornår man bruger den, og dens kritik/begrænsninger.
"""
import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_theme import inject_css  # noqa: E402

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
        "kritik": "Antager at 9.9 altid er bedst og tager ikke højde for situationen, modsat "
                  "situationsbestemt ledelse.",
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
]

ALLE_SIT = [S_KONK, S_VAEKST, S_STRUK, S_LEDELSE, S_MOTIV, S_KULTUR, S_FORANDRING, S_SC]

tab_vaelger, tab_katalog = st.tabs(["🎯 Modelvælger", "📚 Modelkatalog"])


# ===========================================================================
# MODELVÆLGER
# ===========================================================================
with tab_vaelger:
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
    else:
        st.info("Vælg mindst én situation ovenfor for at få forslag.", icon="👆")


# ===========================================================================
# MODELKATALOG
# ===========================================================================
with tab_katalog:
    st.subheader("Modelkatalog")
    st.caption("Slå hver model op med hvad den er, hvornår man bruger den, og dens "
               "begrænsninger (kritikken giver point til eksamen).")

    c1, c2 = st.columns([2, 1])
    with c1:
        soeg = st.text_input("Søg model (fx 'ansoff', 'kultur', 'lederstil')", key="org_soeg",
                             help="Søger i modelnavne og nøgleord.").lower().strip()
    with c2:
        kat = st.selectbox("Kategori", ["Alle", "Strategi & struktur", "Ledelse & kultur"], key="org_kat")

    vist = 0
    for m in MODELLER:
        if kat != "Alle" and m["kat"] != kat:
            continue
        if soeg and soeg not in m["navn"].lower() and not any(soeg in t for t in m["soeg"]):
            continue
        vist += 1
        with st.expander(f"{m['navn']}  ·  {m['kat']}", expanded=bool(soeg)):
            st.markdown(f"**Hvad er det?** {m['hvad']}")
            st.markdown(f"**Hvornår bruges den?** {m['hvornaar']}")
            st.markdown(f"**Kritik og begrænsninger:** {m['kritik']}")
    if vist == 0:
        st.info("Ingen model matchede søgningen.")

st.divider()
st.caption("Bemærk: Porters værdikæde har sit eget modul (den har en fast analysestruktur) — "
           "se 🔗 Værdikædeanalyse i menuen. Kommunikationsmodellen ligger under faget Kommunikation.")
st.page_link("pages/0_Værdikædeanalyse.py", label="🔗 Åbn Værdikædeanalyse", icon="🔗")
