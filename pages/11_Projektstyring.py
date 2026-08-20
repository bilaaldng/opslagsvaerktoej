"""Projektstyring — 3. semester: den midlertidige organisation omkring en
engangsopgave.

Moduler: Projekt eller drift · Kendt & ukendt · De fire processer ·
Projektorganisationen · Projektlederen · Projektmodeller · Scrum & Kanban ·
De fem i balance · Personprofiler.

Faget prøves ikke for sig selv: Projektstyring (4 ECTS) afgøres sammen med
Distribution, SCM og transportjura i én tværfaglig prøve. Derfor peger siden
løbende videre til de andre fag frem for at stå alene.

Stoffet følger fagets lærebog (kapitel 1-2) og lektion 1. Ingen
virksomhedsnavne — situationer er formuleret neutralt, så de kan bruges på
en hvilken som helst opgave.
"""
import os
import sys

import pandas as pd
import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_theme import inject_css  # noqa: E402

st.set_page_config(page_title="Projektstyring", page_icon="📋", layout="wide")
inject_css()

st.title("📋 Projektstyring")
st.caption(
    "Hvordan man får en **engangsopgave** i mål, når den hverken er drift "
    "eller kan planlægges færdig fra start. Fagets kerne er den midlertidige "
    "organisation inde i den permanente — og den ubehagelige detalje, at "
    "projektlederen sjældent har formel instruktionsbeføjelse over dem, der "
    "skal udføre arbejdet."
)

# --- Modulvælger (samme deep-link-konvention som de øvrige fagsider) --------
MODULER = [
    "Projekt eller drift", "Kendt & ukendt", "De fire processer",
    "Projektorganisationen", "Projektlederen", "Projektmodeller",
    "Scrum & Kanban", "De fem i balance", "Personprofiler",
]

goto = st.session_state.pop("goto_modul", None)
if goto in MODULER:
    st.session_state["proj_modul"] = goto
elif "proj_modul" not in st.session_state:
    st.session_state["proj_modul"] = MODULER[0]

modul = st.pills("Vælg modul", MODULER, key="proj_modul",
                 label_visibility="collapsed")
if modul is None:
    modul = MODULER[0]


# ===========================================================================
# Projekt eller drift
# ===========================================================================
if modul == "Projekt eller drift":
    st.subheader("Projekt eller drift — testen med de fire kendetegn")
    st.caption(
        "De fleste fejl handler om **tilbagevendende opgaver, der ligner "
        "projekter**. Sæt kryds herunder, så får du svaret — og en begrundelse "
        "du kan bruge ordret.")

    KENDETEGN = [
        ("Tidsbegrænset", "Opgaven har en start og en slutning. Den kører "
         "ikke videre uden slutdato.", "pd_tid"),
        ("Tværfagligt", "Den trækker på folk fra flere funktioner samtidig — "
         "ikke kun én afdeling.", "pd_tvaer"),
        ("Afgrænset", "Mål, rammer og ressourcer kan defineres på forhånd.",
         "pd_afgr"),
        ("Engangsopgave", "Opgaven er ikke løst på samme måde før. Nyt "
         "indhold i en kendt proces tæller ikke.", "pd_engang"),
    ]

    t1, t2 = st.columns([1, 1])
    with t1:
        st.markdown("**Sæt kryds ved det, der passer**")
        svar = []
        for navn, hjaelp, key in KENDETEGN:
            svar.append(st.checkbox(navn, key=key, help=hjaelp))
        antal = sum(svar)
    with t2:
        st.markdown("**Vurdering**")
        st.metric("Kendetegn opfyldt", f"{antal} af 4")
        if antal == 4:
            st.success("**Det er et projekt.** Alle fire kendetegn er opfyldt. "
                       "Så skal der udpeges en projektleder, lægges en plan "
                       "med milepæle, afsættes ressourcer ud over den daglige "
                       "bemanding og tages stilling til risici.")
        elif antal == 0:
            st.info("**Det er drift.** Ingen af kendetegnene er opfyldt — "
                    "opgaven hører til i linjen med en linjechef.")
        else:
            mangler = [n for (n, _h, _k), v in zip(KENDETEGN, svar) if not v]
            st.warning(
                "**Gråzone.** Opgaven mangler: " + " · ".join(mangler) + ". "
                "Til et forsvar er gråzonen ikke et problem — den er et "
                "argument. Sig hvilke kendetegn der er opfyldt, hvilke der "
                "ikke er, og hvad du vælger at gøre med det.")

    st.markdown("#### Projekt over for drift")
    st.markdown(
        "| | Projekt | Drift |\n|---|---|---|\n"
        "| **Opgaven** | Ny hver gang | Tilbagevendende |\n"
        "| **Organisationen** | Midlertidig | Fast |\n"
        "| **Ledelsen** | Egen projektleder | Linjechef |\n"
        "| **Slutningen** | Slutter når målet er nået | Kører videre uden slutdato |\n")

    st.error(
        "**Hvad fejlklassifikationen koster.** Behandles et projekt som drift, "
        "sker der fire ting: ingen driver opgaven, afvigelser opdages sent "
        "(der er ingen plan at måle mod), arbejdet skal klares «ved siden af» "
        "og kolliderer med driften første gang det spidser til, og den første "
        "forhindring bliver en krise i stedet for en planlagt håndtering.")


# ===========================================================================
# Kendt & ukendt
# ===========================================================================
elif modul == "Kendt & ukendt":
    st.subheader("Kendt og ukendt — hvor detaljeret kan projektet planlægges?")
    st.caption(
        "Planlægningsgraden er ikke et spørgsmål om grundighed, men om "
        "opgavens karakter. Matricen krydser **hvad** der skal laves med "
        "**hvordan** det skal laves.")

    k1, k2 = st.columns(2)
    hvad = k1.radio("Er det klart, HVAD der skal laves?", ["Ja", "Nej"],
                    key="ku_hvad", horizontal=True)
    hvordan = k2.radio("Er det klart, HVORDAN det skal laves?", ["Ja", "Nej"],
                       key="ku_hvordan", horizontal=True)

    st.markdown("#### Matricen")
    st.markdown(
        "| | **Kendt hvordan** | **Ukendt hvordan** |\n|---|---|---|\n"
        "| **Kendt hvad** | Rutineprojektet — kan detailplanlægges fra start | "
        "Målet er klart, vejen er ikke. Her hjælper en agil tilgang |\n"
        "| **Ukendt hvad** | Metoden findes, men målet skal findes først | "
        "Ægte nybrud — her er vi i et *prejekt* |\n")

    if hvad == "Ja" and hvordan == "Ja":
        st.success(
            "**Rutineprojektet.** Både mål og metode er kendt, så projektet "
            "kan detailplanlægges fra start. Det er vandfaldsmodellens "
            "hjemmebane — der er ikke meget at lære undervejs, og den agile "
            "overhead med løbende prioritering koster mere, end den giver.")
    elif hvad == "Ja" and hvordan == "Nej":
        st.info(
            "**Kendt mål, ukendt vej.** Her hjælper en agil tilgang: arbejdet "
            "deles i korte forløb med et brugbart resultat i enden af hvert, "
            "og prioriteringen genbesøges undervejs. Rammen og budgettet kan "
            "sagtens ligge fast — det er den blandede form, og den er den "
            "almindelige i logistik.")
    elif hvad == "Nej" and hvordan == "Ja":
        st.info(
            "**Metoden findes, målet skal findes.** Første opgave er ikke at "
            "planlægge udførelsen, men at afklare, hvad der egentlig skal "
            "opnås. Springes det over, planlægger man omhyggeligt mod et mål, "
            "ingen har defineret.")
    else:
        st.warning(
            "**Ægte nybrud — et prejekt.** Både hvad og hvordan er ukendt, og "
            "så er der ingen plan at lægge endnu. Det, der skal ske, er "
            "undersøgelse og afklaring, ikke projektstyring. At kræve en "
            "detaljeret plan på dette stadie giver en plan, der er forkert "
            "fra dag ét.")

    st.caption(
        "**Til forsvaret:** placér opgaven i matricen FØRST, og udled så "
        "projektformen af placeringen. Gør man det omvendt — vælger form "
        "og begrunder bagefter — hører eksaminator det med det samme.")


# ===========================================================================
# De fire processer
# ===========================================================================
elif modul == "De fire processer":
    st.subheader("De fire processer — fra idé til afleveret resultat")
    st.caption("Hele forløbet følger denne figur. Hver fase har et formål, "
               "ikke bare et navn.")

    FASER = [
        ("1 · Opstart", "Idé bliver til godkendt projekt",
         "Formålet afklares, rammen og mandatet fastlægges, og der tages "
         "stilling til, om projektet overhovedet skal sættes i gang.",
         "Opstartens produkt er **enighed** — ikke dokumenter. Springes den "
         "over, bruges gennemførelsen på at forhandle det, der skulle have "
         "været aftalt: mål, ressourcer og hvem der må beslutte hvad."),
        ("2 · Planlægning", "Interessenter, risici og plan",
         "Interessenterne kortlægges, risiciene vurderes og håndteres, og "
         "planen lægges. Det er her, arbejdet gøres muligt at styre.",
         "Bogens største kapitel. En risikoliste uden ejere, handlinger og "
         "opfølgning er dokumentation — ikke styring."),
        ("3 · Gennemførelse", "Styring og kommunikation",
         "Arbejdsopgaver og ressourcer styres, risici overvåges, ændringer "
         "håndteres, gruppen ledes, og resultater og status kommunikeres. "
         "Undervejs føres projektets logbog.",
         "Logbogen fastholder **beslutninger og deres begrundelse** — det "
         "gør statusmøder ikke. Et halvt år senere kan ingen huske hvorfor."),
        ("4 · Afslutning", "Aflevering og evaluering",
         "Resultatet afleveres formelt, så ansvaret går tilbage til driften. "
         "Derefter evalueres både processen og resultatet.",
         "Resultat og proces må ikke blandes: resultatet svarer "
         "opdragsgiveren, processen er organisationens læring til næste gang."),
    ]

    for navn, undertitel, hvad, pointe in FASER:
        with st.expander(f"**{navn}** — {undertitel}", expanded=False):
            st.markdown(hvad)
            st.info(pointe)

    st.warning(
        "**Den fase, der oftest springes over, er afslutningen.** Uden en "
        "formel overdragelse ved driften ikke, at de har fået ansvaret — og "
        "uden evaluering gentages de samme fejl i næste projekt.")


# ===========================================================================
# Projektorganisationen
# ===========================================================================
elif modul == "Projektorganisationen":
    st.subheader("Projektorganisationen — den midlertidige inde i den permanente")

    st.markdown(
        "```\n"
        "        Opdragsgiver          bestiller projektet og betaler for det\n"
        "             │\n"
        "        Styregruppe           træffer de beslutninger, projektlederen\n"
        "             │                ikke må træffe selv\n"
        "        Projektleder ─────── Referencegrupper\n"
        "             │                dem der skal BRUGE resultatet bagefter\n"
        "        Projektgruppe         udfører arbejdet, typisk udlånt fra driften\n"
        "```")

    ROLLER = pd.DataFrame([
        ["Opdragsgiver", "Bestiller projektet og betaler for det"],
        ["Styregruppe", "Træffer de beslutninger, projektlederen ikke må træffe selv"],
        ["Projektleder", "Driver projektet fremad og rapporterer opad"],
        ["Projektgruppe", "Udfører arbejdet. Typisk udlånt fra driften"],
        ["Referencegrupper", "Dem der skal bruge resultatet bagefter"],
    ], columns=["Rolle", "Hvad de gør"])
    st.dataframe(ROLLER, hide_index=True, width="stretch")

    st.error(
        "**Referencegrupperne glemmes oftest — og det er dyrt.** De afgør, om "
        "resultatet overhovedet kan bruges. Et teknisk vellykket projekt, "
        "ingen vil arbejde i, er ikke vellykket. Spørg tidligt: hvem skal "
        "leve med det her bagefter?")

    st.markdown("#### Den strukturelle konflikt")
    st.markdown(
        "Tre forhold følger af, at den midlertidige organisation lever inde i "
        "den permanente:\n\n"
        "- **Projektlederen har sjældent formel instruktionsbeføjelse.** Han "
        "kan ikke beordre — han må forhandle.\n"
        "- **Deltagerne har to chefer på samme tid** — projektlederen og deres "
        "egen linjechef, som har andre mål.\n"
        "- **Ressourcerne kan trækkes tilbage**, når driften spidser til.\n\n"
        "Derfor er en konflikt om en medarbejders tid ikke personlig, men "
        "**strukturel**. Og derfor er vejen frem styregruppen — det er "
        "præcis den slags beslutning, den er nedsat til at træffe.")

    st.page_link("pages/6_Kommunikation.py",
                 label="💬 Interessentanalysen (magt-interesse) ligger på Kommunikation")


# ===========================================================================
# Projektlederen
# ===========================================================================
elif modul == "Projektlederen":
    st.subheader("Projektlederens roller")

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown("**Teamleder**")
        st.caption("Får gruppen til at fungere. Motivation, konflikter og retning.")
    with r2:
        st.markdown("**Integrator**")
        st.caption("Binder fagligheder sammen på tværs af funktioner.")
    with r3:
        st.markdown("**Koordinator**")
        st.caption("Holder styr på opgaver, tid og afhængigheder.")

    st.info(
        "**Vægtningen skifter.** I et lille projekt fylder koordinatorrollen "
        "mest — lederen er tæt på arbejdet. I et stort, tværfagligt projekt "
        "bliver **integratorrollen** afgørende, fordi risikoen ikke ligger i "
        "delene, men i sammenføjningen. Og i et projekt med modstand eller "
        "usikkerhed fylder teamlederrollen mest.")

    st.markdown("#### Leadership og management (Kotter)")
    st.markdown(
        "| | **Leadership** (ledelse) | **Management** (administration) |\n"
        "|---|---|---|\n"
        "| Sætter retning | ✅ | |\n"
        "| Planlægger og budgetterer | | ✅ |\n"
        "| Motiverer og overbeviser | ✅ | |\n"
        "| Organiserer og bemander | | ✅ |\n"
        "| Håndterer forandring | ✅ | |\n"
        "| Kontrollerer og løser problemer | | ✅ |\n"
        "| Arbejder med **mennesker** | ✅ | |\n"
        "| Arbejder med **systemer** | | ✅ |\n")

    st.success(
        "**Hvorfor skellet betyder noget lige her:** uden management skrider "
        "plan, budget og opfølgning. Uden leadership følger folk ikke med — og "
        "det er særligt kritisk i projekter, netop fordi projektlederen ikke "
        "har instruktionsbeføjelse og derfor må lede gennem retning og "
        "overbevisning frem for gennem ordrer. En projektleder har brug for "
        "begge, men sjældent i samme mængde.")


# ===========================================================================
# Projektmodeller
# ===========================================================================
elif modul == "Projektmodeller":
    st.subheader("Tre projektformer")

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("**Traditionel (vandfald)**")
        st.caption("Faser i rækkefølge. Virker når opgaven er kendt.")
    with p2:
        st.markdown("**Blandet**")
        st.caption("Fast ramme, agil udførelse. Det man møder i praksis.")
    with p3:
        st.markdown("**Agil**")
        st.caption("Korte forløb og løbende justering. Virker når vejen er ukendt.")

    st.markdown("#### Vandfaldsmodellen")
    st.markdown(
        "Opstart → Planlægning → Gennemførelse → Afslutning. Hele planen "
        "lægges, før arbejdet går i gang, og leveringen sker **én gang til "
        "sidst**. Tilbageløb findes, men de koster.")

    v1, v2 = st.columns(2)
    with v1:
        st.success("**Den holder når**\n\n"
                   "- Målet er kendt fra start\n"
                   "- Metoden er brugt før\n"
                   "- Kravene ligger fast, fx i et udbud\n"
                   "- Leverancen kan først bruges, når den er hel")
    with v2:
        st.error("**Den knækker når**\n\n"
                 "- Kravene ændrer sig undervejs\n"
                 "- Brugerne først ser resultatet til sidst\n"
                 "- Fejl opdages efter mange måneder\n"
                 "- En sen ændring river hele planen fra hinanden")

    st.markdown("#### Agilitet har to dele")
    a1, a2 = st.columns(2)
    a1.info("**Ledelsesdelen**\n\nProjektlederens tilgang til medarbejderne og "
            "til den udadvendte del af opgaven, fx rapportering opad.")
    a2.info("**Procesdelen**\n\nStyringen, hvor det planlagte hele tiden "
            "forandres, fordi omverdenen og præmisserne ændrer sig.")
    st.warning(
        "**Vælger man kun den ene halvdel**, får man enten kaos (proces uden "
        "ledelse) eller et agilt skilt på en helt almindelig plan (ledelse "
        "uden proces). De to forudsætter hinanden.")

    st.markdown("#### Projektlederens rolle skifter")
    st.markdown(
        "| | **Traditionel** | **Agil** |\n|---|---|---|\n"
        "| Retningen | Teamet arbejder for projektlederen | Projektlederen arbejder for teamet |\n"
        "| Planen | Projektlederens ansvar | Teamet planlægger selv næste forløb |\n"
        "| Kontrollen | Projektleder og styregruppe | Gruppen og brugeren |\n"
        "| Beslutninger | Går opad | Faciliteres og forhindringer fjernes |\n")
    st.caption("Rollen forsvinder ikke — den bliver konsulterende i stedet for "
               "instruerende.")

    st.markdown("#### Vandfald og Scrum side om side")
    st.markdown(
        "| | **Vandfald** | **Scrum** |\n|---|---|---|\n"
        "| Planen | Lægges fast fra start | Genbesøges hvert sprint |\n"
        "| Kravene | Låses tidligt | Prioriteres løbende |\n"
        "| Leveringen | Én gang til sidst | Lidt ad gangen |\n"
        "| Kontrollen | Projektleder og styregruppe | Team og bruger |\n"
        "| Opdragsgiver | Med ved milepæle | Med hele vejen |\n")
    st.info("**Den blandede form tager en kolonne fra hver** — og det er den, "
            "man møder i logistik: rammen og budgettet er fast, udførelsen er agil.")

    st.markdown("#### Hvorfor virksomheder vælger agilt")
    st.markdown(
        "- **Time to market** — kortere tid og lavere omkostninger, så "
        "løsningen når markedet før konkurrenterne\n"
        "- **Prioritering** — projekter hvor omfang og sluttidspunkt ikke kan "
        "overskues fra start\n"
        "- **Strategi** — projektets mål rettes ind efter virksomhedens "
        "overordnede strategi undervejs")
    st.caption("Læg mærke til, at **ingen** af de tre handler om at slippe for "
               "at planlægge. Agil projektstyring er forandringsdrevet — ikke "
               "det samme som at være uden styring.")


# ===========================================================================
# Scrum & Kanban
# ===========================================================================
elif modul == "Scrum & Kanban":
    st.subheader("To kendte rammeværk")
    st.caption("Vælg værktøj efter projektet, ikke efter hvad der er på mode.")

    st.markdown("### Scrum")
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("**De tre roller**")
        st.markdown(
            "- **Produktejeren** — ejer prioriteringen og bestemmer hvad der "
            "er vigtigst. Ikke hvordan det løses.\n"
            "- **Scrum Master** — sikrer at processen holder og fjerner det, "
            "der spærrer for teamet. Er ikke chef.\n"
            "- **Udviklingsteamet** — leverer resultatet, er selvorganiserende "
            "og planlægger selv sprintets indhold.")
    with s2:
        st.markdown("**De tre lister**")
        st.markdown(
            "- **Produkt-backlog** — alt det, der kunne laves, prioriteret af "
            "produktejeren\n"
            "- **Sprint-backlog** — den bid, teamet har taget ind i det "
            "aktuelle sprint\n"
            "- **Increment** — det færdige og brugbare resultat i enden af "
            "sprintet")
    with s3:
        st.markdown("**De fire møder**")
        st.markdown(
            "- **Sprintplanlægning** — teamet vælger, hvad der kan nås\n"
            "- **Daglig standup** — kort møde om fremdrift og forhindringer\n"
            "- **Sprint review** — resultatet vises for opdragsgiver og brugere\n"
            "- **Retrospektiv** — teamet retter på sin egen måde at arbejde på")

    st.warning(
        "**Bland ikke review og retrospektiv sammen.** Review handler om "
        "**produktet** og vises udad. Retrospektiv handler om **processen** og "
        "er teamets egen justering. Det er den hyppigste sammenblanding til "
        "eksamen.")

    st.markdown("#### Sprintet fra ende til anden")
    st.markdown(
        "`Backlog` → `Planlægning` → **`Sprint`** → `Review` → `Retrospektiv` "
        "→ og så forfra")
    st.caption("Pilen går tilbage til **backloggen**, ikke til starten af "
               "projektet. Rammen står fast, indholdet gør ikke.")

    st.info(
        "**«Færdig» betyder brugbar.** Halvt lavet arbejde tæller ikke med. "
        "En bid, der er 90 % færdig, leverer nul værdi og skjuler samtidig, "
        "hvor langt projektet reelt er. Det er dét, der gør, at fremdrift kan "
        "måles ærligt i agile forløb.")

    st.markdown("### Kanban")
    st.markdown(
        "Synligt board med **loft over igangværende opgaver**. Styrer flow i "
        "stedet for at dele arbejdet i faste sprint.")
    st.error(
        "**Pas på ordet.** Kanban betyder to forskellige ting i dette "
        "semester: her er det en opgavetavle med et WIP-loft, og i "
        "Lean/produktionen er det et kort eller en beholder, der giver "
        "træk-signal (`y = D·T·(1+x)/C`). Samme oprindelse, forskellig brug — "
        "og en oplagt eksamensfælde.")
    st.page_link("pages/9_Distribution.py",
                 label="🚚 Kanban som træk-signal — se Kanban-beregneren på Distribution")


# ===========================================================================
# De fem i balance
# ===========================================================================
elif modul == "De fem i balance":
    st.subheader("Fem ting der skal holdes i balance")
    st.caption("Pointen er **samtidigheden**. Optimerer du én, skrider en anden.")

    BALANCE = [
        ("Omgivelserne", "Organisationen omkring projektet ændrer sig undervejs",
         "Ny chef, ny strategi eller en omorganisering kan ændre projektets "
         "grundlag, uden at nogen fortæller projektlederen det."),
        ("Arbejdsgruppen", "Folk er udlånt, har to chefer og bliver trukket tilbage",
         "Den mest almindelige årsag til forsinkelse. Ressourcen var aftalt, "
         "men driften spidsede til."),
        ("Fremdrift", "Projektet skal bevæge sig, ikke bare være i gang",
         "Aktivitet er ikke fremdrift. Uden milepæle med et konkret resultat "
         "kan et projekt være travlt i måneder uden at nærme sig målet."),
        ("Produktkvalitet", "Det færdige resultat skal kunne bruges",
         "Her er referencegrupperne afgørende — det er dem, der afgør, om "
         "resultatet duer i praksis."),
        ("Økonomi", "Forbruget holdes op mod budgettet hele vejen",
         "Ikke kun til sidst. Opdages overforbruget ved afslutningen, er der "
         "ingen handlemuligheder tilbage."),
    ]
    for navn, kort, uddyb in BALANCE:
        with st.expander(f"**{navn}** — {kort}"):
            st.markdown(uddyb)

    st.warning(
        "**Sådan bruges de til et forsvar.** Bliver du spurgt «hvad ville du "
        "gøre?», så svar ikke med ét greb. Sig hvilket af de fem forhold du "
        "prioriterer, og **hvad det koster på de andre**. Presser du "
        "fremdriften, falder kvaliteten eller økonomien. Det er dét, der "
        "adskiller en projektleder fra en, der bare vil have opgaven færdig.")


# ===========================================================================
# Personprofiler
# ===========================================================================
elif modul == "Personprofiler":
    st.subheader("Tre måder at se en gruppe på")
    st.error(
        "**De svarer på tre forskellige spørgsmål — bland dem ikke sammen.** "
        "Det er selve pointen med øvelsen, og en klassisk fælde til eksamen.")

    pp1, pp2, pp3 = st.columns(3)
    with pp1:
        st.markdown("**DISC**")
        st.caption("**Adfærdsstil** — hvordan personen kommunikerer og reagerer.")
        st.markdown(
            "- **D**ominance — måden man går til problemer og tager kontrol\n"
            "- **I**nfluence — måden man omgås og påvirker andre\n"
            "- **S**teadiness — tålmodighed, vedholdenhed, eftertænksomhed\n"
            "- **C**ompliance — måden man organiserer og følger procedurer")
    with pp2:
        st.markdown("**Adizes PAEI**")
        st.caption("**Lederrolle** — hvad personen bidrager med ledelsesmæssigt.")
        st.markdown(
            "- **P**roducent — får tingene gjort her og nu\n"
            "- **A**dministrator — systematiserer, følger op, holder styr\n"
            "- **E**ntreprenør — ser muligheder, skaber nyt, tænker fremad\n"
            "- **I**ntegrator — får folk til at arbejde sammen, skaber sammenhæng")
        st.caption("Stort bogstav = stærk rolle. Ingen mestrer alle fire.")
    with pp3:
        st.markdown("**Belbin**")
        st.caption("**Teamrolle** — hvordan personen opfører sig i gruppearbejde.")
        st.markdown(
            "Ni roller. Et menneske dækker typisk to-tre, så tre til fem "
            "personer kan dække alle ni.")

    st.markdown("#### Belbin: de fire der oftest mangler")
    st.markdown(
        "| Rolle | Hvad den bidrager med |\n|---|---|\n"
        "| **Idémanden** | Kommer med de utraditionelle forslag. Kan være svær at styre |\n"
        "| **Koordinatoren** | Holder gruppen på sporet og får de andre til at bidrage |\n"
        "| **Analysatoren** | Vurderer nøgternt, om idéen faktisk kan lade sig gøre |\n"
        "| **Afslutteren** | Får de sidste tyve procent færdige. Ofte den der mangler |\n")

    st.info(
        "**Brug det som et gruppe-værktøj, ikke en dom over personer.** En lav "
        "integrator-score siger ikke «dårlig leder» — den siger, at nogen "
        "anden i gruppen skal dække sammenhængen, ellers falder den på gulvet. "
        "Samme med afslutteren: mangler rollen helt, bliver de sidste tyve "
        "procent af opgaven det, der skrider.")

    st.caption(
        "Modellerne findes også i modelkataloget på Organisation-siden, hvor "
        "Adizes står sammen med de øvrige ledelsesmodeller.")
    st.page_link("pages/5_Organisation.py",
                 label="🧭 Adizes og de øvrige ledelsesmodeller på Organisation")


st.divider()
st.caption(
    "📋 Projektstyring vejer **4 ECTS** af den tværfaglige prøve og har ingen "
    "selvstændig eksamen — det afgøres sammen med Distribution, SCM og "
    "transportjura i én prøve. Casen kræver, at projektstyringen kobles på "
    "det samme flow som Lean, Chopra og lagerdesign. Træn koblingen i "
    "**Kobl fagene** på Forsvarstræneren.")
