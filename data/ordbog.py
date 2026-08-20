"""Ordbogen — begreberne, der lever PÅ TVÆRS af fagene.

Hvorfor den findes
------------------
Resten af værktøjet er skåret efter fag: Indkøb, Produktion, Distribution …
Det er rart at slå op i, men det snyder ét sted. Mange begreber hører til i
flere fag på én gang, og fag-opdelingen skjuler det:

  * Søger man "lean", vinder modulet «Lean & QRM» på Distribution, fordi det
    matcher på titlen. Intet fortæller, at Produktion også underviser i Lean.
  * "Kanban" betyder to forskellige ting samme semester — et kort der giver
    træk-signal i produktionen, og et board med loft over igangværende
    opgaver i agil projektstyring.

3. semester prøves tværfagligt: fire fag afgøres i én prøve, og casen kræver
at de kobles på det samme flow. Derfor er en ordbog uden for fagene ikke
oprydning — det er den måde, stoffet faktisk bliver eksamineret på.

Sådan er den bygget
-------------------
1. GRUNDLAGET er de faktakort, Forsvarstræneren allerede bruger — 15 i selve
   sidefilen og resten i pakke_fakta.py. De er begreb → definition i forvejen,
   så de skrives ikke om; de læses ind. `pakke_fakta.py` røres ikke.
2. FAG AFLEDES med de samme nøgleord som Forsvarstræneren bruger — men her
   returneres ALLE fag der matcher, ikke kun det første. Det er selve
   rettelsen: et Lean-kort må gerne høre til både Produktion og Distribution.
3. BERIGELSER lægges ovenpå i hånden for de begreber, hvor det betaler sig:
   deep-links til de moduler der underviser i begrebet, flere betydninger,
   engelsk fagterm, og en "hvornår holder det ikke"-linje.

Et begreb behøver ikke stå i faktakortene for at være i ordbogen — står det
kun i BERIGELSER, kommer det med alligevel (se fx Kanban og de 5 Lean-principper).
"""
import ast
import io
import os
import re

from pakke_fakta import EKSTRA_FAKTA

_ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TRÆNER = "pages/7_Forsvarstræner.py"


# ===========================================================================
# Fag-afledning — samme nøgleord som Forsvarstræneren, men LISTE-værdig
# ===========================================================================
# Forsvarstrænerens _fakta_fag() stopper ved første match ("første match
# vinder"), så et begreb altid ender i præcis ét fag. Her samles ALLE der
# rammer. Det er hele pointen med ordbogen.
FAGREGLER = [
    ("Jura", ["incoterm", "told", "duty", "cisg", "købelov", "aftalelov",
              "reklamation", "misligholdelse", "risikoovergang", "force majeure",
              "voldgift", "exw", "fca", "fob", "cif", "cfr", "ddp", "dap", "cpt",
              "cip", "fas", "erstatning", "ansvarsgrænse", "fragtfører"]),
    ("Værdikædeanalyse", ["værdikæde", "primære aktiviteter", "primær aktivitet",
                          "støtteaktivitet", "harmoni", "forsyningskæde"]),
    ("Indkøb", ["kraljic", "bensaou", "eoq", "wilson", "genbestillingspunkt",
                "rop", "sikkerhedslager", "servicegrad", "abc analyse",
                "leverandør", "sourcing", "indkøb", "tco", "total cost",
                "rammeaftale", "mængderabat", "erp", "kravspecifikation",
                "behovsanalyse", "forecast", "prognose", "poq"]),
    ("Kommunikation", ["batna", "zopa", "mdo", "ldo", "distributiv",
                       "integrativ", "forhandling", "byttechips", "målpunkt",
                       "aspirationsniveau", "reservationspunkt",
                       "aktiv lytning", "spørgeteknik", "kropssprog",
                       "kommunikation", "transaktionsanalyse", "gesteland"]),
    # NB: nøgleord matcher som forstavelse, ikke inde i ordet — derfor står
    # danske sammensætninger ("nulhypotese") eksplicit ved siden af roden.
    ("Statistik", ["konfidensinterval", "konfidens", "hypotese", "nulhypotese",
                   "modhypotese", "teststørrelse", "p værdi",
                   "signifikans", "normalfordeling", "normalfordelt",
                   "standardafvigelse", "stikprøve", "varians", "korrelation",
                   "regression", "z værdi", "z score", "t test", "t fordeling",
                   "median", "kvartil", "binomial", "fraktil", "outlier",
                   "kontrolkort", "kontrolgrænse", "ucl", "lcl", "særårsag",
                   "forklaringsgrad", "sandsynlighed"]),
    ("Økonomi", ["npv", "kapitalværdi", "annuitet", "kalkulationsrente",
                 "intern rente", "irr", "afskrivning", "dækningsbidrag",
                 "dækningsgrad", "nulpunkt", "break even", "likviditet",
                 "soliditet", "afkastningsgrad", "overskudsgrad", "egenkapital",
                 "balance", "resultatopgørelse", "investering",
                 "tilbagebetalingstid", "payback", "kritisk levetid",
                 "følsomhed", "kalkulation", "bidragskalkulation", "aoh",
                 "omsætningshastighed", "benzinlampe"]),
    ("Produktion", ["mts", "mto", "ato", "eto", "jit", "just in time", "kanban",
                    "lean", "kaizen", "oee", "smed", "mrp", "stykliste", "bom",
                    "takt", "gennemløbstid", "layout", "5s", "muda", "mura",
                    "muri", "tqm", "flaskehals", "kapacitet", "omstilling",
                    "spild", "otif", "ordrevinder", "ordrekvalificerende",
                    "leveringspræstation", "produktion", "kvalitetsstyring",
                    "seriestørrelse", "fordisme", "wip", "udnyttelsesgrad"]),
    ("Distribution", ["chopra", "distributionsnetværk", "tyngdepunkt", "qrm",
                      "mct", "polca", "transportform", "modal", "intermodal",
                      "container", "søfragt", "luftfragt", "plukning", "pluk",
                      "wms", "tpl", "3pl", "cross dock", "køre hviletid",
                      "takograf", "totalvægt", "lastbil", "kanban", "lean",
                      "spild", "muda", "postponement", "last mile",
                      "slow steaming", "modal shift", "volumenvægt"]),
    ("Organisation", ["mcgregor", "schein", "adizes", "ledergitter", "maslow",
                      "herzberg", "hofstede", "motivation", "kultur", "ansoff",
                      "porter", "swot", "mintzberg", "interessent", "strategi",
                      "stuck in the middle", "differentiering", "diversifikation",
                      "kontrolspænd", "span of control", "ledelseslag",
                      "kommandovej", "menneskesyn", "mekanistisk",
                      "omkostningsleder", "ledelse", "organisation", "paei"]),
    # NB: "agil" står IKKE her alene. Ordet bruges også om agile
    # forsyningskæder (Harmoni, Chopra), og et bart "agil" trak derfor
    # rene SCM-begreber ind i projektstyring. Frasen er entydig.
    ("Projektstyring", ["projekt", "projektleder", "styregruppe", "opdragsgiver",
                        "referencegruppe", "milepæl", "vandfald",
                        "agil projektledelse", "agil projektstyring",
                        "scrum", "sprint", "backlog", "retrospektiv",
                        "increment", "produktejer", "belbin", "teamrolle",
                        "kotter", "gantt", "wbs", "prejekt", "paei", "adizes"]),
]


def _afled_fag(*tekster) -> list:
    """Alle fag hvis nøgleord rammer teksten — ikke kun det første.

    Lange nøgleord matcher som forstavelse ('ansoff' rammer også 'Ansoffs'),
    korte som helt ord (så 'irr' ikke rammer 'irrelevant'). Flerords-nøgler
    matcher som frase. Samme regler som Forsvarstræneren, anden returværdi.
    """
    tokens = re.sub(r"[^a-zæøå0-9]+", " ", " ".join(tekster).lower()).split()
    hay = " " + " ".join(tokens) + " "
    ud = []
    for fag, ord_ in FAGREGLER:
        for o in ord_:
            if " " in o:
                ramt = f" {o} " in hay
            elif len(o) >= 5:
                ramt = any(t.startswith(o) for t in tokens)
            else:
                ramt = f" {o} " in hay
            if ramt:
                ud.append(fag)
                break
    return ud


def _noegle(navn: str) -> str:
    """Opslagsnøgle: små bogstaver, ordstilling ligegyldig, 'Incoterm'-præfiks
    ignoreret — så 'Incoterm DDP' ≡ 'DDP' og 'Duty / told' ≡ 'Told / Duty'.
    Samme regel som Forsvarstrænerens _forside_noegle(), så de to lister
    dedupes ens."""
    tokens = re.sub(r"[^a-zæøå0-9]+", " ", navn.lower()).split()
    tokens = [t for t in tokens if t != "incoterm"]
    return " ".join(sorted(tokens)) or navn.strip().lower()


# ===========================================================================
# BERIGELSER — hånd-skrevet ovenpå faktakortene
# ===========================================================================
# Nøglen er _noegle(begrebsnavn). Felter der må sættes:
#   navn         vist titel (ellers bruges faktakortets forside)
#   kort         kort definition (ellers faktakortets bagside)
#   engelsk      fagtermen på engelsk — en væsentlig del af litteraturen er engelsk
#   fag          LISTE af fag; erstatter den afledte liste
#   ekstra_fag   fag der lægges TIL den afledte liste
#   betydninger  [(sammenhæng, forklaring)] når ordet betyder noget forskelligt
#   hvor         [(fag, modul)] deep-links til de moduler der underviser i det
#   holder_ikke  antagelsen bag begrebet, og hvor den knækker
#   soeg         ekstra søgeord
#   se_ogsaa     beslægtede begreber (skal selv findes i ordbogen)
BERIGELSER = {

    # --- Lean-familien: Bilaals oprindelige hul -----------------------------
    _noegle("Lean"): {
        "engelsk": "Lean",
        "ekstra_fag": ["Distribution"],
        "kort": "Fjern alt det, der ikke skaber værdi for kunden. Kommer fra "
                "bilindustrien og hviler på fem principper, der tages i rækkefølge.",
        "hvor": [("Produktion", "Produktionsstrategi"),
                 ("Produktion", "Processkort"),
                 ("Distribution", "Lean & QRM")],
        "holder_ikke": "Lean forudsætter nogenlunde stabil og forudsigelig "
                       "efterspørgsel. Laver man mange varianter i små mængder, "
                       "er svaret ikke mere Lean — det er QRM, som angriber "
                       "tiden i stedet for spildet.",
        "soeg": ["toyota", "tps", "womack", "5 principper", "fem principper"],
        "se_ogsaa": ["De 5 Lean-principper", "Muda · Mura · Muri", "JIT",
                     "Kanban", "QRM", "Værdistrømsanalyse (VSM)"],
    },
    _noegle("De 5 Lean-principper"): {
        "navn": "De 5 Lean-principper",
        "engelsk": "The five Lean principles",
        "fag": ["Produktion", "Distribution"],
        "kort": "Rækkefølgen, Lean skal tages i: 1) **Værdi** — kunden "
                "definerer, hvad der er værd at betale for. 2) **Værdistrøm** — "
                "kortlæg alle skridt og se, hvilke der reelt tilfører værdi. "
                "3) **Flow** — få det til at glide uden stop og bunker. "
                "4) **Pull** — producér først, når der er trukket. "
                "5) **Perfektion** — gentag i det uendelige.",
        "hvor": [("Distribution", "Lean & QRM"),
                 ("Produktion", "Produktionsstrategi")],
        "holder_ikke": "Principperne er en rækkefølge, ikke en menu. Springer "
                       "man til pull uden først at have flow, vokser lagrene i "
                       "stedet for at falde — pull uden flow er bare et lager "
                       "med et nyt navn.",
        "soeg": ["værdi", "værdistrøm", "flow", "pull", "perfektion",
                 "womack", "jones", "lean thinking"],
        "se_ogsaa": ["Lean", "Værdistrømsanalyse (VSM)", "Kanban",
                     "Muda · Mura · Muri", "Takt time"],
    },
    _noegle("Muda · Mura · Muri"): {
        "navn": "Muda · Mura · Muri",
        "engelsk": "Waste · Unevenness · Overburden",
        "fag": ["Produktion", "Distribution"],
        "kort": "Lean har tre slags tab, ikke ét. **Muda** er spild — arbejde "
                "uden værdi for kunden. **Mura** er ujævnhed — svingninger i "
                "belastningen. **Muri** er overbelastning af mennesker og "
                "maskiner. De hænger sammen: ujævnhed skaber overbelastning, "
                "og overbelastning skaber spild.",
        "hvor": [("Distribution", "Lean & QRM"), ("Produktion", "Processkort")],
        "holder_ikke": "De fleste jagter kun muda, fordi spild er lettest at "
                       "få øje på. Men fjerner man spildet uden at udjævne "
                       "belastningen, kommer det igen — mura er ofte årsagen, "
                       "muda kun symptomet.",
        "soeg": ["spild", "ujævnhed", "overbelastning", "8 spildtyper",
                 "syv spildtyper", "7 wastes"],
        "se_ogsaa": ["Lean", "De 5 Lean-principper", "Værdistrømsanalyse (VSM)"],
    },
    _noegle("Værdistrømsanalyse (VSM)"): {
        "navn": "Værdistrømsanalyse (VSM)",
        "engelsk": "Value Stream Mapping",
        "fag": ["Produktion", "Distribution"],
        "kort": "Tegn hele flowet for én produktfamilie — fra råvare til kunde "
                "— med både materiale- og informationsstrøm. Nutidskortet "
                "viser, hvor tiden bliver væk; fremtidskortet viser, hvordan "
                "det skal se ud bagefter.",
        "hvor": [("Distribution", "Lean & QRM"), ("Produktion", "Processkort")],
        "holder_ikke": "Et kort er ikke en forbedring. Værdien opstår først, "
                       "når fremtidskortet bliver til konkrete projekter med "
                       "navn og dato — ellers er det en pæn tegning.",
        "soeg": ["vsm", "value stream", "current state", "future state",
                 "nutidskort", "fremtidskort", "learning to see"],
        "se_ogsaa": ["Lean", "De 5 Lean-principper", "Takt time",
                     "Gennemløbstid (lead time)"],
    },

    # --- Kanban: samme ord, to fag, to betydninger -------------------------
    _noegle("Kanban"): {
        "navn": "Kanban",
        "engelsk": "Kanban",
        "fag": ["Produktion", "Distribution", "Projektstyring"],
        "kort": "Et synligt signal om, at der må laves eller hentes mere. "
                "Ordet bruges om to forskellige ting i dette semester.",
        "betydninger": [
            ("Lean og produktion",
             "Et kort eller en beholder, der udløser genopfyldning. Der "
             "produceres først, når et kort kommer retur — derfor et "
             "træksystem. Antal kort: y = D·T·(1+x)/C."),
            ("Agil projektstyring",
             "Et synligt board med loft over, hvor mange opgaver der må være "
             "i gang på én gang. Styrer flow i stedet for at dele arbejdet i "
             "faste sprint, som Scrum gør."),
        ],
        "hvor": [("Distribution", "Kanban-beregner"),
                 ("Projektstyring", "Scrum & Kanban")],
        "holder_ikke": "Kanban forudsætter nogenlunde jævnt træk. Svinger "
                       "efterspørgslen, vokser antallet af kort — og QRM "
                       "kritiserer netop kanban på det punkt: systemet reagerer "
                       "på forbrug, det forudsiger ikke.",
        "soeg": ["pull", "træksystem", "kort", "beholder", "board", "wip",
                 "loft", "two-bin", "scrum", "sprint", "agil", "opgavetavle"],
        "se_ogsaa": ["JIT", "Lean", "QRM", "De 5 Lean-principper"],
    },

    # --- QRM: Leans modstykke ved høj variation ----------------------------
    _noegle("QRM"): {
        "navn": "QRM (Quick Response Manufacturing)",
        "engelsk": "Quick Response Manufacturing",
        "fag": ["Produktion", "Distribution"],
        "kort": "Angriber **tiden** i stedet for spildet. Målet er kortest "
                "mulig gennemløbstid fra ordre til levering, målt som MCT. "
                "Svaret for virksomheder med mange varianter i små mængder, "
                "hvor Lean har svært ved at få fodfæste.",
        "hvor": [("Distribution", "Lean & QRM")],
        "holder_ikke": "QRM kræver, at man bevidst planlægger med "
                       "reservekapacitet. Det strider mod den udbredte idé om, "
                       "at høj udnyttelsesgrad er god økonomi — og derfor "
                       "falder QRM ofte på gulvet i budgetforhandlingen, ikke "
                       "på fagligheden.",
        "soeg": ["suri", "quick response", "mct", "polca", "q-roc",
                 "det hvide rum", "reservekapacitet"],
        "se_ogsaa": ["Lean", "MCT", "Udnyttelsesgrad", "Kanban",
                     "Gennemløbstid (lead time)"],
    },
    _noegle("MCT"): {
        "navn": "MCT (Manufacturing Critical-path Time)",
        "engelsk": "Manufacturing Critical-path Time",
        "fag": ["Produktion", "Distribution"],
        "kort": "Den kalendertid der går, fra en kunde afgiver ordre, til den "
                "er leveret — regnet ad den længste vej gennem virksomheden, "
                "og målt i kalenderdage, ikke arbejdstimer.",
        "hvor": [("Distribution", "Lean & QRM")],
        "holder_ikke": "MCT måler kalendertid netop for at afsløre ventetiden. "
                       "Regner man i arbejdstimer i stedet, forsvinder pointen: "
                       "det er typisk kun nogle få procent af MCT, hvor der "
                       "faktisk bliver arbejdet på opgaven.",
        "soeg": ["gennemløbstid", "kritisk vej", "kalendertid", "hvide rum"],
        "se_ogsaa": ["QRM", "Gennemløbstid (lead time)", "Littles Law",
                     "Udnyttelsesgrad"],
    },

    # --- Udnyttelsesgrad: fagets bedste fælde ------------------------------
    _noegle("Udnyttelsesgrad"): {
        "engelsk": "Utilisation",
        "ekstra_fag": ["Distribution"],
        "hvor": [("Produktion", "Udnyttelsesgrad ρ"), ("Distribution", "Lean & QRM")],
        "holder_ikke": "Den klassiske fælde: høj udnyttelsesgrad føles "
                       "effektivt, men køen — og dermed gennemløbstiden — "
                       "vokser eksplosivt, når man nærmer sig 100 %. Travlhed "
                       "er ikke det samme som hastighed.",
        "soeg": ["rho", "kø", "ventetid", "kapacitet", "reservekapacitet"],
        "se_ogsaa": ["QRM", "Littles Law", "Flaskehals", "MCT"],
    },
    _noegle("Flaskehals"): {
        "engelsk": "Bottleneck",
        "ekstra_fag": ["Distribution", "Økonomi"],
        "hvor": [("Produktion", "Knap kapacitet")],
        "holder_ikke": "Flaskehalsen flytter sig. Løser man den ét sted, "
                       "opstår en ny et andet — derfor er «find flaskehalsen» "
                       "en løbende opgave, ikke et engangsprojekt.",
        "se_ogsaa": ["Udnyttelsesgrad", "Littles Law", "Dækningsbidrag (DB)"],
    },
    _noegle("Littles Law"): {
        "engelsk": "Little's Law",
        "ekstra_fag": ["Distribution"],
        "hvor": [("Produktion", "Little's Law")],
        "holder_ikke": "Loven gælder kun i et system i ligevægt over tid. "
                       "Måler man midt i en ordrepukkel, giver den et tal, der "
                       "ser rigtigt ud, men ikke beskriver noget stabilt.",
        "se_ogsaa": ["Gennemløbstid (lead time)", "WIP (Work in Process)",
                     "Udnyttelsesgrad", "MCT"],
    },
    _noegle("JIT"): {
        "engelsk": "Just-in-Time",
        "ekstra_fag": ["Distribution"],
        "hvor": [("Produktion", "Produktionsstrategi"), ("Distribution", "Lean & QRM")],
        "holder_ikke": "JIT optimerer omkostninger på bekostning af robusthed. "
                       "Uden buffer rammer enhver forstyrrelse i kæden "
                       "produktionen med det samme.",
        "se_ogsaa": ["Lean", "Kanban", "Sikkerhedslager", "De 5 Lean-principper"],
    },
    _noegle("Takt time"): {
        "engelsk": "Takt time",
        "ekstra_fag": ["Distribution"],
        "hvor": [("Produktion", "Linjebalancering")],
        "holder_ikke": "Takttid er kundens efterspørgsel omsat til tid — ikke "
                       "hvor hurtigt maskinen kan køre. Forveksles de to, "
                       "bygger man kapacitet til et behov, der ikke findes.",
        "se_ogsaa": ["De 5 Lean-principper", "Værdistrømsanalyse (VSM)",
                     "Gennemløbstid (lead time)"],
    },
    _noegle("Gennemløbstid (lead time)"): {
        "engelsk": "Lead time / throughput time",
        "ekstra_fag": ["Distribution", "Indkøb"],
        "hvor": [("Produktion", "Little's Law"), ("Indkøb", "Genbestilling + SS")],
        "se_ogsaa": ["Littles Law", "MCT", "Sikkerhedslager", "QRM"],
    },
    _noegle("WIP (Work in Process)"): {
        "engelsk": "Work in Process",
        "ekstra_fag": ["Distribution", "Projektstyring"],
        "hvor": [("Produktion", "Little's Law"),
                 ("Projektstyring", "Scrum & Kanban")],
        "se_ogsaa": ["Littles Law", "Kanban", "Gennemløbstid (lead time)"],
    },

    # --- Modeller der optræder i to fag ------------------------------------
    _noegle("Adizes PAEI"): {
        "navn": "Adizes PAEI",
        "engelsk": "Adizes PAEI roles",
        "fag": ["Organisation", "Projektstyring"],
        "kort": "Fire lederroller, ingen kan mestre alle fire: **P**roducent "
                "(får tingene gjort), **A**dministrator (systematiserer og "
                "følger op), **E**ntreprenør (ser muligheder, tænker fremad), "
                "**I**ntegrator (får folk til at spille sammen). Stort bogstav "
                "= stærk rolle.",
        "hvor": [("Organisation", "Modelkatalog"),
                 ("Projektstyring", "Personprofiler")],
        "holder_ikke": "Modellen beskriver roller i et team, ikke kvaliteten "
                       "af en person. En lav I betyder ikke «dårlig leder» — "
                       "det betyder, at nogen anden i teamet skal dække "
                       "sammenhængen, ellers falder den på gulvet.",
        "soeg": ["paei", "producent", "administrator", "entreprenør",
                 "integrator", "lederroller"],
        "se_ogsaa": ["Belbins teamroller", "McGregor X/Y", "Ledergitteret (Blake & Mouton)"],
    },
    _noegle("Belbins teamroller"): {
        "navn": "Belbins teamroller",
        "engelsk": "Belbin team roles",
        "fag": ["Organisation", "Projektstyring"],
        "kort": "Ni roller, en gruppe skal dække for at fungere. Et menneske "
                "dækker typisk to-tre af dem, så tre til fem personer kan "
                "dække alle ni. Fire mangler oftest: **idémanden** (de "
                "utraditionelle forslag), **koordinatoren** (holder gruppen på "
                "sporet), **analysatoren** (vurderer nøgternt, om idéen kan "
                "lade sig gøre) og **afslutteren** (får de sidste tyve procent "
                "færdige).",
        "holder_ikke": "Belbin beskriver adfærd i en gruppe — ikke evner og "
                       "ikke lederrolle. Blandes den med Adizes (lederrolle) "
                       "eller DISC (adfærdsstil), svarer man på et andet "
                       "spørgsmål end det, der blev stillet.",
        "hvor": [("Projektstyring", "Personprofiler")],
        "soeg": ["teamrolle", "idémand", "koordinator", "analysator",
                 "afslutter", "completer", "gruppedannelse"],
        "se_ogsaa": ["Adizes PAEI", "Ledergitteret (Blake & Mouton)",
                     "McGregor X/Y"],
    },
    _noegle("Interessentanalyse (magt-interesse)"): {
        "engelsk": "Stakeholder analysis (power–interest grid)",
        # Nøgleordet "interessent" hører under Organisation i reglerne, men
        # modulet ligger på Kommunikation, og projektstyring bruger samme
        # model på opdragsgiver, styregruppe og referencegrupper. Alle tre.
        "fag": ["Kommunikation", "Organisation", "Projektstyring"],
        "hvor": [("Kommunikation", "Interessentanalyse"),
                 ("Projektstyring", "Projektorganisationen")],
        "holder_ikke": "Placeringen i gitteret er ikke fast. En interessent "
                       "med lav interesse kan vågne på et øjeblik, hvis "
                       "projektet pludselig rører noget, der betyder noget for "
                       "dem — analysen skal gentages undervejs.",
        "se_ogsaa": ["Adizes PAEI"],
    },
    _noegle("Harmoni"): {
        "engelsk": "Strategic fit",
        "fag": ["Værdikædeanalyse", "Organisation", "Distribution"],
        "hvor": [("Distribution", "Distributionsnetværk (Chopra)")],
        "holder_ikke": "Harmoni er et krav om, at strategi og forsyningskæde "
                       "peger samme vej — ikke en påstand om, at den ene er "
                       "bedst. En omkostningsleder med agil kæde betaler for "
                       "en fleksibilitet, kunden ikke har bedt om; en "
                       "differentieret virksomhed med lean kæde kan ikke "
                       "levere den variation, den sælger sig på.",
        "soeg": ["strategisk fit", "agil forsyningskæde", "responsiv"],
        "se_ogsaa": ["Lean", "Omkostningsleder (Cost leadership)",
                     "Differentiering"],
    },
    _noegle("Fordisme"): {
        "ekstra_fag": ["Projektstyring"],
        "hvor": [("Produktion", "Produktionsstrategi")],
        "holder_ikke": "Tankegangen om at specialisere og udnytte hver "
                       "ressource maksimalt lever videre i moderne "
                       "afdelingsstruktur — og det er præcis den, QRM peger på "
                       "som årsag til lange gennemløbstider.",
        "se_ogsaa": ["Lean", "QRM", "Udnyttelsesgrad"],
    },

    # --- Transportjura ------------------------------------------------------
    _noegle("Fragtførerens ansvar"): {
        "navn": "Fragtførerens ansvar",
        "engelsk": "Carrier liability",
        "fag": ["Jura", "Distribution"],
        "kort": "Hvad man kan få ud af transportøren, når godset bliver "
                "skadet. Reguleres ikke af købsaftalen, men af en konvention "
                "der følger **transportformen**: CMR (vej), Haag-Visby (sø), "
                "Montreal (luft), COTIF/CIM (bane).",
        "hvor": [("Jura", "Fragtførerens ansvar")],
        "holder_ikke": "Ansvarsgrænsen er **vægtbaseret**, ikke værdibaseret. "
                       "Let og dyrt gods er derfor systematisk underdækket — "
                       "og ved multimodal transport kan skaden endda falde "
                       "ind under et andet regelsæt end det, man regnede med.",
        "soeg": ["cmr", "haag-visby", "hague visby", "montreal", "cotif", "cim",
                 "warszawa", "sdr", "ansvarsgrænse", "ansvarsbegrænsning",
                 "transportør", "godsskade", "konvention"],
        "se_ogsaa": ["Incoterms", "SDR", "Vareforsikring", "CISG"],
    },
    _noegle("SDR"): {
        "navn": "SDR (Special Drawing Rights)",
        "engelsk": "Special Drawing Rights",
        "fag": ["Jura", "Distribution", "Økonomi"],
        "kort": "IMF's regningsenhed — en kurv af valutaer med en dagskurs. "
                "Transportkonventionerne angiver ansvarsgrænser i SDR frem "
                "for i en enkelt valuta, så grænsen ikke udhules af inflation "
                "i ét land.",
        "hvor": [("Jura", "Fragtførerens ansvar")],
        "holder_ikke": "Kursen ændrer sig dagligt, og beløbsgrænserne "
                       "revideres periodisk. Et konkret erstatningsbeløb skal "
                       "regnes på dagskursen og med kildehenvisning — ikke "
                       "huskes.",
        "soeg": ["special drawing rights", "imf", "regningsenhed", "kurs"],
        "se_ogsaa": ["Fragtførerens ansvar"],
    },
    _noegle("Vareforsikring"): {
        "navn": "Vareforsikring",
        "engelsk": "Cargo insurance",
        "fag": ["Jura", "Distribution", "Økonomi"],
        "kort": "Forsikring af godsets **værdi** under transporten. Dækker "
                "det, fragtførerens vægtbaserede ansvarsgrænse ikke rækker "
                "til — og er typisk langt billigere end at værdideklarere "
                "sendingen hos transportøren.",
        "hvor": [("Jura", "Fragtførerens ansvar")],
        "holder_ikke": "Forsikringen erstatter ikke ansvaret — den dækker "
                       "differencen. Man skal stadig reklamere rettidigt over "
                       "for fragtføreren, ellers kan forsikringsselskabet "
                       "miste sit regreskrav og afvise dækning.",
        "soeg": ["cargo insurance", "værdideklaration", "regres", "dækning",
                 "underdækket", "cif", "cip"],
        "se_ogsaa": ["Fragtførerens ansvar", "Incoterms", "SDR"],
    },

    # --- Nyt stof fra fagets oplæg -----------------------------------------
    _noegle("Volumenvægt"): {
        "navn": "Volumenvægt (measureton)",
        "engelsk": "Volumetric weight / measurement ton",
        "fag": ["Distribution", "Økonomi"],
        "kort": "Fragtføreren sælger både løfteevne og plads, så en sending "
                "afregnes efter **det største** af faktisk vægt og volumenvægt. "
                "Volumenvægt = m³ × en omregningsfaktor, der afhænger af "
                "transportformen (fly ≈ 167 kg/m³, søfragt 1.000 kg/m³).",
        "hvor": [("Distribution", "Volumenvægt & fragtgrundlag")],
        "holder_ikke": "Faktoren er ikke en naturlov — den er en aftale, og den "
                       "varierer mellem transportformer og transportører. "
                       "Regner man med flyets faktor på en søfragt, tager man "
                       "fejl med en faktor seks.",
        "soeg": ["measureton", "cbm", "fragtgrundlag", "chargeable weight",
                 "densitet", "w/m", "rumvægt", "volumen"],
        "se_ogsaa": ["Incoterms", "Told / Duty"],
    },
    _noegle("Frihedsrettigheder"): {
        "navn": "Luftfartens frihedsrettigheder",
        "engelsk": "Freedoms of the air",
        "fag": ["Distribution", "Jura"],
        "kort": "Ni trin for, hvad et lands luftfartsselskab må i et andet "
                "lands luftrum — fra blot at flyve henover (1.) til at flyve "
                "rent indenrigs i det fremmede land (9.). De fire første er "
                "officielle; resten bruges i praksis uden samme formelle status.",
        "hvor": [("Distribution", "Luftfragt & frihedsrettigheder")],
        "holder_ikke": "Rettighederne er mellemstatslige aftaler, ikke en "
                       "global standard. To lande kan have vidt forskellige "
                       "aftaler, så «har vi femte frihed?» afhænger af "
                       "landepar — ikke af selskabet.",
        "soeg": ["femte frihed", "cabotage", "overflyvning", "luftrum",
                 "hub", "beflyvning", "luftfart"],
        "se_ogsaa": ["Volumenvægt (measureton)"],
    },
    _noegle("Arbejdstid"): {
        "navn": "Arbejdstid (transport)",
        "engelsk": "Working time (road transport)",
        "fag": ["Distribution", "Jura"],
        "kort": "Reglerne for hele chaufførens arbejdsdag — også læsning, "
                "kontrol og papirarbejde. Et **andet** regelsæt end "
                "køre-/hviletid, som kun handler om selve kørslen. "
                "**Rådighedstid** (planlagt ventetid, fx færge) tæller ikke med.",
        "hvor": [("Distribution", "Køre-hviletid & vægte")],
        "holder_ikke": "De to regelsæt gælder samtidig. En chauffør kan "
                       "overholde køre-/hviletiden og alligevel bryde "
                       "arbejdstidsreglerne, fordi læsning og ventetid tæller "
                       "med dér — så sig hvilket regelsæt du argumenterer ud fra.",
        "soeg": ["rådighedstid", "natarbejde", "48 timer", "chauffør", "pause"],
        "se_ogsaa": ["Særtransport"],
    },
    _noegle("Særtransport"): {
        "navn": "Særtransport",
        "engelsk": "Abnormal / oversize transport",
        "fag": ["Distribution", "Jura"],
        "kort": "Transport der overskrider de almindelige grænser for bredde, "
                "længde, højde eller vægt. Kræver tilladelse til en **konkret "
                "rute**, hastigheden falder med vægten, og over bestemte mål "
                "skal der følgebil med.",
        "hvor": [("Distribution", "Køre-hviletid & vægte")],
        "holder_ikke": "Der gives kun tilladelse, hvis godset ikke kan deles "
                       "op. Kan det skilles ad, er særtransport ikke en "
                       "mulighed — uanset hvor meget besværet det ville spare.",
        "soeg": ["blokvogn", "følgebil", "tilladelse", "projektlast",
                 "overstørrelse", "dispensation"],
        "se_ogsaa": ["Arbejdstid (transport)", "Luftfartens frihedsrettigheder"],
    },
    _noegle("Euro-norm"): {
        "navn": "Euro-norm",
        "engelsk": "Euro emission standard",
        "fag": ["Distribution"],
        "kort": "Fælles europæiske grænser for udstødning fra tunge "
                "dieselkøretøjer, især NOx og partikler. Normen følger "
                "køretøjets registreringsår og er skærpet trinvis.",
        "hvor": [("Distribution", "Køre-hviletid & vægte")],
        "holder_ikke": "Euro-normen regulerer **luftforurening**, ikke CO₂. "
                       "En Euro 6-lastbil er ikke klimavenlig — den er "
                       "renere i byluften. CO₂ afhænger af brændstofforbrug "
                       "og energikilde.",
        "soeg": ["nox", "partikler", "miljøzone", "udstødning", "emission"],
        "se_ogsaa": ["Volumenvægt (measureton)"],
    },
    _noegle("5S"): {
        "navn": "5S",
        "engelsk": "5S",
        "fag": ["Produktion", "Distribution"],
        "kort": "Sortér · Sæt i system · Systematisk rengøring · Standardisér · "
                "Selvdisciplin. Formålet er ikke pænhed, men at **afvigelser "
                "bliver synlige** — mangler et værktøj, ses det med det samme.",
        "hvor": [("Distribution", "Lean & QRM")],
        "holder_ikke": "5S uden de øvrige Lean-principper bliver til "
                       "oprydningskampagner, der falder tilbage efter et par "
                       "måneder. Det er et fundament, ikke et projekt.",
        "soeg": ["sortér", "standardisér", "orden", "visuel styring", "seiri"],
        "se_ogsaa": ["Lean", "De 5 Lean-principper", "SMED"],
    },
    _noegle("POQ"): {
        "navn": "POQ / EPQ",
        "engelsk": "Production Order Quantity / Economic Production Quantity",
        "fag": ["Indkøb", "Produktion"],
        "kort": "EOQ'ens søskende for **egen produktion**. Hvor EOQ antager, "
                "at hele ordren lander på lageret på én gang, tager POQ højde "
                "for, at varerne produceres løbende — og forbruges undervejs. "
                "Derfor bliver det maksimale lager lavere end seriestørrelsen, "
                "og den optimale serie større end EOQ.",
        "hvor": [("Indkøb", "POQ / EPQ"), ("Produktion", "POQ")],
        "holder_ikke": "POQ kræver, at produktionstakten er **højere** end "
                       "forbrugstakten. Er de lige store, løber man aldrig "
                       "foran, og formlen giver ikke mening — så er "
                       "spørgsmålet kapacitet, ikke seriestørrelse.",
        "soeg": ["epq", "seriestørrelse", "produktionsserie", "opbygningstid",
                 "maks lager"],
        "se_ogsaa": ["EOQ (Wilson)", "SMED (omstillingsreduktion)", "Lagerrente"],
    },
    _noegle("SMED"): {
        "navn": "SMED (omstillingsreduktion)",
        "engelsk": "SMED — Single-Minute Exchange of Die",
        "fag": ["Produktion", "Distribution"],
        "kort": "Systematisk nedbringelse af omstillingstid. Skil **indre** tid "
                "(maskinen står stille) fra **ydre** tid (kan gøres mens den "
                "kører), flyt så meget som muligt til ydre, og forenkl resten.",
        "hvor": [("Distribution", "Lean & QRM"), ("Produktion", "POQ")],
        "holder_ikke": "Lang omstillingstid er selve grunden til store "
                       "batches. Angriber man batchstørrelsen uden først at "
                       "sænke omstillingstiden, stiger omkostningen pr. enhed "
                       "— så rækkefølgen er omvendt af, hvad folk tror.",
        "soeg": ["omstilling", "indre tid", "ydre tid", "setup", "seriestørrelse"],
        "se_ogsaa": ["5S", "Lean", "De 5 Lean-principper", "POQ"],
    },

    # --- Jura ↔ Distribution ------------------------------------------------
    _noegle("Incoterms"): {
        "engelsk": "Incoterms 2020",
        "ekstra_fag": ["Distribution"],
        "hvor": [("Jura", "Incoterms & risikoens overgang"),
                 ("Distribution", "Told & dokumenter")],
        "holder_ikke": "Incoterms regulerer risiko og omkostninger mellem "
                       "køber og sælger — ikke ejendomsret, ikke betaling, og "
                       "ikke forholdet til fragtføreren. Det sidste afgøres af "
                       "transportkonventionerne.",
        "se_ogsaa": ["CISG", "Told / Duty"],
    },
    _noegle("Told / Duty"): {
        "engelsk": "Customs duty",
        "ekstra_fag": ["Distribution"],
        "hvor": [("Distribution", "Told & dokumenter"), ("Jura", "Jurakatalog")],
        "se_ogsaa": ["Incoterms", "DDP"],
    },
    _noegle("Servicegrad"): {
        "ekstra_fag": ["Distribution"],
        "hvor": [("Indkøb", "Genbestilling + SS")],
        "holder_ikke": "Servicegrad koster eksponentielt: de sidste par "
                       "procent kræver uforholdsmæssigt meget sikkerhedslager. "
                       "100 % er ikke et mål, det er en regning.",
        "se_ogsaa": ["Sikkerhedslager", "Genbestillingspunkt (ROP)", "OTIF (On Time In Full)"],
    },
    _noegle("OTIF (On Time In Full)"): {
        "ekstra_fag": ["Distribution", "Indkøb"],
        "hvor": [("Produktion", "Perfect Order / OTIF")],
        "holder_ikke": "OTIF er en alt-eller-intet-måling: én forsinket "
                       "varelinje trækker hele ordren ned. Det gør tallet "
                       "hårdt, men også groft — det siger intet om, hvor tæt "
                       "på man var.",
        "se_ogsaa": ["Servicegrad", "Lead time"],
    },
    _noegle("ABC-analyse"): {
        "ekstra_fag": ["Distribution"],
        "hvor": [("Indkøb", "ABC / Pareto")],
        "holder_ikke": "ABC rangerer på værdi alene. En billig C-vare, der "
                       "stopper produktionen når den mangler, er kritisk — "
                       "derfor suppleres ABC ofte med en risikovurdering.",
        "se_ogsaa": ["Kraljic", "Sikkerhedslager"],
    },
    _noegle("Sikkerhedslager"): {
        "ekstra_fag": ["Distribution"],
        "hvor": [("Indkøb", "Genbestilling + SS")],
        "holder_ikke": "Sikkerhedslager dækker variation, ikke fejl. Er "
                       "leveringstiden systematisk undervurderet, hjælper mere "
                       "lager kun indtil det løber tør igen.",
        "se_ogsaa": ["Servicegrad", "Genbestillingspunkt (ROP)", "JIT", "Lead time"],
    },
    _noegle("MRP"): {
        "ekstra_fag": ["Distribution"],
        "hvor": [("Produktion", "MRP")],
        "holder_ikke": "MRP regner med faste, gennemsnitlige leveringstider. "
                       "Svinger de i virkeligheden, planlægger systemet efter "
                       "et tal, der sjældent passer — det er QRM's hovedanke "
                       "mod almindelig MRP.",
        "se_ogsaa": ["Stykliste (BOM – Bill of Materials)", "QRM", "Kanban"],
    },
    _noegle("ERP"): {
        "ekstra_fag": ["Projektstyring"],
        "holder_ikke": "Et ERP-projekt fejler sjældent på teknikken. Det "
                       "fejler på interessenterne — de afdelinger, der skal "
                       "ændre arbejdsgang, og som ikke blev spurgt i tide.",
        "se_ogsaa": ["Interessentanalyse (magt-interesse)", "MRP",
                     "Behovsanalyse / kravspecifikation"],
    },
}


# ===========================================================================
# Opbygning
# ===========================================================================
def _faktakort() -> list:
    """Alle faktakort: de 15 i trænerens egen fil + resten fra pakke_fakta.

    Trænerens fil importerer Streamlit, så den kan ikke importeres her. I
    stedet læses FAKTA-listen med AST — samme greb som data/index.py bruger
    til at læse MODULER ud af fagsiderne uden at køre dem.
    """
    with io.open(os.path.join(_ROD, _TRÆNER), encoding="utf-8") as f:
        træ = ast.parse(f.read())
    base = []
    for n in træ.body:
        if (isinstance(n, ast.Assign)
                and any(getattr(t, "id", "") == "FAKTA" for t in n.targets)
                and isinstance(n.value, ast.List)):
            for e in n.value.elts:
                par = [x.value for x in e.elts if isinstance(x, ast.Constant)]
                if len(par) == 2:
                    base.append(par)
            break
    return base + [list(k) for k in EKSTRA_FAKTA]


def byg_ordbog() -> list:
    """Slå faktakort og berigelser sammen til ét sorteret opslagsværk."""
    poster = {}

    # 1) grundlaget: faktakortene, dedupet på samme nøgle som træneren
    for forside, bagside in _faktakort():
        n = _noegle(forside)
        if n in poster:                    # dublet (fx DDP i to banker)
            continue
        poster[n] = {"begreb": forside, "kort": bagside,
                     "fag": _afled_fag(forside, bagside),
                     "soeg": [], "se_ogsaa": [], "betydninger": [],
                     "hvor": [], "holder_ikke": None, "engelsk": None}

    # 2) berigelserne ovenpå — de må også indføre helt nye begreber
    for n, b in BERIGELSER.items():
        p = poster.get(n)
        if p is None:
            navn = b.get("navn") or n
            p = {"begreb": navn, "kort": b.get("kort", ""),
                 "fag": _afled_fag(navn, b.get("kort", "")),
                 "soeg": [], "se_ogsaa": [], "betydninger": [],
                 "hvor": [], "holder_ikke": None, "engelsk": None}
            poster[n] = p
        # Berigelsens nøgle er tit den korte form ("MCT"), mens det viste navn
        # er den lange ("MCT (Manufacturing Critical-path Time)"). Begge skal
        # kunne slås op, ellers rammer et "se også: MCT" ikke sit eget kort.
        p.setdefault("_nøgler", set()).add(n)
        for felt in ("navn", "kort", "engelsk", "holder_ikke"):
            if b.get(felt):
                p["begreb" if felt == "navn" else felt] = b[felt]
        if b.get("fag"):
            p["fag"] = list(b["fag"])
        for f in b.get("ekstra_fag", []):
            if f not in p["fag"]:
                p["fag"].append(f)
        for felt in ("betydninger", "hvor", "soeg", "se_ogsaa"):
            if b.get(felt):
                p[felt] = list(b[felt])

    # 3) fag i fast visningsrækkefølge, så kortene ser ens ud overalt
    orden = [f for f, _ in FAGREGLER]
    for p in poster.values():
        p["fag"] = sorted(set(p["fag"]), key=lambda f: orden.index(f)
                          if f in orden else 99)

    return sorted(poster.values(), key=lambda p: p["begreb"].lower())


BEGREBER = byg_ordbog()

# Opslag på nøgle — bruges af siden til "se også"-links. Hvert begreb ligger
# både under sit viste navn og under de nøgler, berigelsen brugte.
BEGREB_VED_NOEGLE = {}
for _p in BEGREBER:
    for _n in {_noegle(_p["begreb"])} | _p.get("_nøgler", set()):
        BEGREB_VED_NOEGLE.setdefault(_n, _p)


def slaa_op(navn: str):
    """Find et begreb ud fra et navn eller alias. None hvis det ikke findes."""
    return BEGREB_VED_NOEGLE.get(_noegle(navn))
