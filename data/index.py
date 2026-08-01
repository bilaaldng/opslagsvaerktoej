"""Søgeindekset — ét sted, bygget ud fra siderne selv.

To lag:

  1. NAVIGATIONSLAGET — ét opslag pr. modul. Modulnavnene LÆSES ud af
     fagsidernes egne MODULER-lister (via AST, uden at køre Streamlit), så
     indekset aldrig kan komme ud af trit med virkeligheden. Tilføjer du et
     modul på en fagside, dukker det op i søgningen af sig selv.

  2. INDHOLDSLAGET — de enkelte modeller, regler og Incoterms inde i
     modulerne, så man kan søge "Ansoff" eller "DDP" og lande det rigtige
     sted i stedet for kun at kunne finde overskrifter.

Nøgleordene nedenfor er det eneste der vedligeholdes i hånden; alt andet
udledes. Mangler et modul nøgleord, kan det stadig findes på sit navn.
"""
import ast
import io
import os

_ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fagene i visningsrækkefølge: (fag, sidesti)
SIDER = [
    ("Værdikædeanalyse", "pages/0_Værdikædeanalyse.py"),
    ("Indkøb", "pages/1_Indkøb.py"),
    ("Produktion", "pages/2_Produktion.py"),
    ("Statistik", "pages/3_Statistik.py"),
    ("Økonomi", "pages/4_Økonomi.py"),
    ("Organisation", "pages/5_Organisation.py"),
    ("Kommunikation", "pages/6_Kommunikation.py"),
    ("Distribution", "pages/9_Distribution.py"),
    ("Jura", "pages/8_Jura.py"),
    ("Forsvarstræner", "pages/7_Forsvarstræner.py"),
]

# Ekstra søgeord pr. modul — det man taster i stedet for det officielle navn.
NOEGLEORD = {
    ("Indkøb", "EOQ"): ["wilson", "wilsons formel", "ordrestørrelse", "økonomisk ordremængde", "bestilling", "optimal ordre"],
    ("Indkøb", "POQ / EPQ"): ["produktionsserie", "seriestørrelse"],
    ("Indkøb", "Genbestilling + SS"): ["rop", "genbestillingspunkt", "benzinlampen", "sikkerhedslager", "servicegrad", "z-værdi"],
    ("Indkøb", "ABC / Pareto"): ["80/20", "klassifikation", "årsværdi", "abc-analyse"],
    ("Indkøb", "Forecasting"): ["prognose", "glidende gennemsnit", "eksponentiel udglatning", "mad", "mape", "mfe", "tracking signal"],
    ("Indkøb", "Review-systemer"): ["periodisk", "kontinuert", "lagerstyring", "max-niveau"],
    ("Indkøb", "Make-vs-buy / TCO"): ["make or buy", "tco", "total cost", "outsourcing", "insourcing", "egenproduktion", "ejeromkostning"],
    ("Indkøb", "Leverandørscore"): ["leverandørevaluering", "vægtet score", "kriterier", "esg"],
    ("Indkøb", "Strategi & modeller"): ["kraljic", "bensaou", "sourcing", "single", "dual", "order winner", "qualifier", "vmi", "esi", "srm", "spend"],
    ("Produktion", "POQ"): ["epq", "produktionsserie", "besparelse"],
    ("Produktion", "Linjebalancering"): ["takt time", "takttid", "stationer", "balancetab", "effektivitet"],
    ("Produktion", "Processkort"): ["værdigivende", "lean", "spild"],
    ("Produktion", "Knap kapacitet"): ["flaskehals", "dækningsbidrag", "db pr. time", "produktmix"],
    ("Produktion", "Produktionsstrategi"): ["mts", "mto", "ato", "eto", "lean", "fordisme", "jit", "layout", "make to stock"],
    ("Produktion", "MPS + ATP"): ["master production schedule", "available to promise", "pei"],
    ("Produktion", "MRP"): ["bom", "stykliste", "materialebehov", "lot-for-lot", "bruttobehov"],
    ("Produktion", "S&OP"): ["sop", "aggregeret plan", "level", "chase", "arbejdsstyrke"],
    ("Produktion", "Little's Law"): ["little", "wip", "gennemløbstid"],
    ("Produktion", "OEE"): ["tilgængelighed", "ydelse", "kvalitet", "overall equipment"],
    ("Produktion", "Perfect Order / OTIF"): ["otif", "leveringspræcision", "til tiden"],
    ("Produktion", "Udnyttelsesgrad ρ"): ["rho", "kø", "ventetid", "lambda", "kapacitet"],
    ("Statistik", "Normalfordeling"): ["z", "z-score", "areal", "gauss", "standardafvigelse", "målinger", "histogram"],
    ("Statistik", "Konfidensinterval"): ["ki", "middelværdi", "andel", "t-fordeling", "margin of error", "stikprøvestørrelse"],
    ("Statistik", "Hypotesetest"): ["h0", "h1", "nulhypotese", "signifikans", "p-værdi", "t-test", "z-test", "ensidet", "tosidet", "kritisk værdi"],
    ("Statistik", "Binomialfordeling"): ["sandsynlighed", "succeser", "x ud af n"],
    ("Statistik", "Kontrolkort"): ["spc", "p-kort", "x-kort", "r-kort", "ucl", "lcl", "proceskontrol", "kapabilitet"],
    ("Statistik", "Regression"): ["scatter", "r²", "korrelation", "hældning", "sammenhæng", "mindste kvadraters", "lineær"],
    ("Økonomi", "Investeringskalkule"): ["npv", "kapitalværdi", "irr", "intern rente", "payback", "tilbagebetalingstid", "kritisk levetid", "nutidsværdi", "cashflow", "sunk cost", "investering"],
    ("Økonomi", "Break-even"): ["nulpunkt", "dækningsgrad", "dækningsbidrag", "sikkerhedsmargin"],
    ("Økonomi", "Priskalkulation"): ["bidragskalkulation", "fordelingskalkulation", "retrograd", "kostpris", "salgspris", "avance"],
    ("Økonomi", "Prisoptimering"): ["totalmetoden", "grænsemetoden", "grænseomsætning", "monopol"],
    ("Økonomi", "Nøgletalsanalyse"): ["afkastningsgrad", "overskudsgrad", "soliditet", "likviditet", "gearing", "dupont", "regnskab", "balance", "aoh"],
    ("Økonomi", "Budget"): ["resultatbudget", "likviditetsbudget", "afskrivning", "kassekredit"],
    ("Organisation", "Modelvælger"): ["hvilken model", "vælg model", "situation"],
    ("Organisation", "Modelkatalog"): ["modeller", "opslag", "kritik"],
    ("Organisation", "Ansoff & ledergitter"): ["vækstmatrix", "blake", "mouton", "kvadrant", "diversifikation"],
    ("Kommunikation", "Interessentanalyse"): ["magt", "interesse", "power-interest", "mendelow", "interessent"],
    ("Kommunikation", "Kommunikationsmodellen"): ["afsender", "modtager", "budskab", "kanal", "støj", "feedback", "kodning", "afkodning"],
    ("Kommunikation", "Gesteland (kultur)"): ["kultur", "relationship focus", "deal focus", "monokron", "ekspressiv", "reserveret", "formel"],
    ("Kommunikation", "Forhandlingsark + ZOPA"): ["forhandling", "mdo", "ldo", "målpunkt", "modstandspunkt", "zopa", "byttechip"],
    ("Kommunikation", "Forhandlingsbibliotek"): ["bapta", "batna", "principiel forhandling", "harvard", "distributiv", "integrativ", "win-win"],
    ("Distribution", "Transportformsvalg"): ["transportform", "vej", "bane", "jernbane", "skib", "søfragt", "luftfragt", "intermodal", "container", "modal split", "omlastning", "transittid"],
    ("Distribution", "Tyngdepunktsmetoden"): ["tyngdepunkt", "gravity", "center of gravity", "lagerplacering", "lokalisering", "koordinater", "hvor skal lageret ligge"],
    ("Distribution", "Distributionsnetværk (Chopra)"): ["chopra", "drop-shipping", "in-transit merge", "last-mile", "kundeafhentning", "svartid", "aggregering", "u-kurve", "e-handel"],
    ("Distribution", "Lean & QRM"): ["qrm", "quick response", "muda", "spild", "kaizen", "jidoka", "vsm", "værdistrøm", "mct", "polca", "postponement"],
    ("Distribution", "Kanban-beregner"): ["kanban", "kort", "beholder", "pull", "træksystem", "jit", "just-in-time"],
    ("Distribution", "Lager & plukning"): ["pluk", "batch-pluk", "zone-pluk", "pick by voice", "rfid", "wms", "tpl", "3pl", "cross-dock", "fifo", "reverse logistics", "kaoslager"],
    ("Distribution", "Køre-hviletid & vægte"): ["køretid", "hviletid", "pause", "takograf", "fartskriver", "totalvægt", "vogntog", "akseltryk", "overlæs", "chauffør"],
    ("Distribution", "Told & dokumenter"): ["told", "t1", "t2", "taric", "tir", "ata-carnet", "remburs", "letter of credit", "konnossement", "bill of lading", "transit"],
    ("Distribution", "Grøn godstransport"): ["co2", "grøn", "klima", "tonkm", "slow steaming", "imo", "bæredygtig", "modal shift"],
    ("Jura", "Jurakatalog"): ["cisg", "købelov", "reklamation", "frist", "misligholdelse", "ophævelse", "erstatning", "standardvilkår", "lovvalg", "værneting"],
    ("Jura", "Incoterms & risikoens overgang"): ["incoterms", "risikoovergang", "leveringsbetingelse", "fragt", "forsikring"],
    ("Jura", "Tvist-skabeloner"): ["tvist", "argumentationskæde", "konflikt", "uenighed"],
    ("Forsvarstræner", "Eksaminér mig"): ["quiz", "tilfældigt", "genkaldelse", "selvrating", "eksaminer"],
    ("Forsvarstræner", "Fælde-jagt"): ["snydespørgsmål", "fælde", "forkert præmis"],
    ("Forsvarstræner", "Eksaminator borer"): ["dybde", "drill", "lag", "eksaminator"],
    ("Forsvarstræner", "Argumentér selv"): ["argument", "flere forsvar", "hvorfor", "det afhænger"],
    ("Forsvarstræner", "Forklar selv"): ["feynman", "forklar", "egne ord"],
    ("Forsvarstræner", "Regn"): ["regnetræner", "regneopgaver", "træn med nye tal"],
    ("Forsvarstræner", "Faktatjek"): ["flashcards", "fakta", "begreber", "definition"],
    ("Forsvarstræner", "Prøveeksamen"): ["generalprøve", "10 spørgsmål", "timer", "pres"],
}

# Sider uden modulvælger (ét sammenhængende forløb)
UDEN_MODULER = {
    "Værdikædeanalyse": (["vca", "værdikæde", "porter", "støtteaktiviteter",
                          "primære aktiviteter", "logistik ind", "logistik ud",
                          "analyse ikke løsning"], "Sådan bygger du en VCA"),
}


def _kilde(sti: str) -> ast.Module:
    with io.open(os.path.join(_ROD, sti), encoding="utf-8") as f:
        return ast.parse(f.read())


def moduler_paa(sti: str) -> list:
    """Læs sidens MODULER-liste uden at køre den (siden importerer Streamlit)."""
    for n in _kilde(sti).body:
        if isinstance(n, ast.Assign) and any(getattr(t, "id", "") == "MODULER" for t in n.targets):
            return [e.value for e in n.value.elts]
    return []


def _tekstfelter(sti: str, variabel: str, felter: tuple) -> list:
    """Træk enkelte tekstfelter ud af en liste-af-ordbøger i en sidefil.

    Bruges til indholdslaget. Vi kan ikke literal_eval hele strukturen (nogle
    felter peger på variabler), men de felter vi skal bruge er ren tekst.
    """
    ud = []
    for n in _kilde(sti).body:
        if not (isinstance(n, ast.Assign)
                and any(getattr(t, "id", "") == variabel for t in n.targets)):
            continue
        for e in n.value.elts:
            if not isinstance(e, ast.Dict):
                continue
            post = {}
            for k, v in zip(e.keys, e.values):
                navn = getattr(k, "value", None)
                if navn not in felter:
                    continue
                if isinstance(v, ast.Constant):
                    post[navn] = v.value
                elif isinstance(v, ast.List):
                    post[navn] = [x.value for x in v.elts if isinstance(x, ast.Constant)]
            ud.append(post)
    return ud


def byg_indeks() -> list:
    """Alle opslag: (fag, titel, sidesti, modul-til-deep-link, nøgleord)."""
    ud = []

    # --- lag 1: ét opslag pr. modul, læst fra siderne selv ---------------
    for fag, sti in SIDER:
        mods = moduler_paa(sti)
        if not mods:                                  # side uden modulvælger
            ord_, titel = UDEN_MODULER.get(fag, ([], fag))
            ud.append((fag, titel, sti, None, ord_))
            continue
        for m in mods:
            ud.append((fag, m, sti, m, NOEGLEORD.get((fag, m), [])))

    # --- lag 2: indholdet inde i modulerne --------------------------------
    for post in _tekstfelter("pages/5_Organisation.py", "MODELLER", ("navn", "soeg")):
        ud.append(("Organisation", post["navn"], "pages/5_Organisation.py",
                   "Modelkatalog", post.get("soeg", []) + ["model"]))
    for post in _tekstfelter("pages/8_Jura.py", "JURA", ("navn", "soeg")):
        ud.append(("Jura", post["navn"], "pages/8_Jura.py",
                   "Jurakatalog", post.get("soeg", []) + ["regel"]))
    for post in _tekstfelter("pages/8_Jura.py", "INCOTERMS", ("kode", "navn", "soeg")):
        kode, navn = post["kode"], post["navn"]
        titel = navn if navn.startswith(kode) else f"{kode} — {navn}"
        ud.append(("Jura", titel, "pages/8_Jura.py",
                   "Incoterms & risikoens overgang",
                   post.get("soeg", []) + [kode.lower(), "incoterms"]))
    return ud


INDEKS = byg_indeks()
