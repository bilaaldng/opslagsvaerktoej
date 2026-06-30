"""Auto-generator af regneopgaver til Forsvarstræner (🧮 Regnetræner).

Ingen API: opgaverne får tilfældige tal, og det KORREKTE svar beregnes med
appens egne core-funktioner (core/*.py). Så er der uendeligt mange friske,
selvrettende opgaver, og svaret er garanteret korrekt (samme matematik som
regnemaskinerne i værktøjet).

lav_opgave(fag=None) -> dict med:
    fag, emne, sp (spørgsmål m. tal), svar (float, korrekt), enhed, dec,
    tol (accepteret afvigelse ved retning), metode (facit-udregning).
"""
from __future__ import annotations

import random

from core import oekonomi as oek
from core import indkoeb as ind
from core import statistik as stat
from core import produktion as prod


def _kr(x: float) -> str:
    s = f"{round(x):,}".replace(",", ".")
    return s


def _pct(x: float, dec: int = 1) -> str:
    return f"{x:.{dec}f}".replace(".", ",")


def _tal(x: float, dec: int = 0) -> str:
    return f"{x:,.{dec}f}".replace(",", "§").replace(".", ",").replace("§", ".")


# ---------------------------------------------------------------------------
# ØKONOMI
# ---------------------------------------------------------------------------

def g_npv():
    inv = random.choice([300, 400, 500, 600, 700, 800]) * 1000
    n = random.choice([3, 4, 5])
    a = random.choice([90, 110, 130, 150, 170, 190, 210]) * 1000
    r = random.choice([6, 7, 8, 9, 10, 12])
    cfs = [-inv] + [a] * n
    svar = oek.npv(r / 100, cfs)
    led = " + ".join(f"{_kr(a)}/{1 + r/100:.2f}^{t}" for t in range(1, n + 1))
    return {
        "fag": "Økonomi", "emne": "NPV",
        "sp": f"En investering koster {_kr(inv)} kr. og giver {_kr(a)} kr. om året i {n} år. "
              f"Kalkulationsrenten er {r}%. Beregn NPV (afrund til hele kr.).",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": max(abs(svar) * 0.012, 100),
        "metode": f"NPV = −{_kr(inv)} + {led} = {_kr(svar)} kr. "
                  f"{'Positiv → investér.' if svar > 0 else 'Negativ → lad være.'}",
    }


def g_break_even():
    faste = random.choice([300, 400, 500, 600, 750, 900]) * 1000
    pris = random.choice([120, 150, 180, 200, 250, 300])
    var = random.choice([60, 70, 80, 90, 100, 120])
    var = min(var, pris - 20)
    db = pris - var
    svar = faste / db
    return {
        "fag": "Økonomi", "emne": "Break-even (nulpunktsmængde)",
        "sp": f"Faste omkostninger er {_kr(faste)} kr. Varen sælges for {pris} kr. med variable "
              f"enhedsomkostninger på {var} kr. Beregn nulpunktsmængden (antal stk.).",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": max(abs(svar) * 0.02, 1),
        "metode": f"DB pr. stk. = {pris} − {var} = {db} kr. Nulpunktsmængde = faste/DB = "
                  f"{_kr(faste)}/{db} = {_tal(svar,0)} stk.",
    }


def g_daekningsgrad():
    pris = random.choice([150, 200, 250, 300, 400, 500])
    var = random.choice([60, 90, 120, 150, 180, 240])
    var = min(var, pris - 20)
    svar = (pris - var) / pris * 100
    return {
        "fag": "Økonomi", "emne": "Dækningsgrad",
        "sp": f"En vare sælges for {pris} kr. med variable enhedsomkostninger på {var} kr. "
              f"Beregn dækningsgraden i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"DG = (pris − variabel)/pris = ({pris} − {var})/{pris} = {_pct(svar)}%.",
    }


def g_afkastningsgrad():
    aktiver = random.choice([4, 5, 6, 8, 10]) * 1_000_000
    ebit = random.choice([300, 400, 500, 600, 800, 1000]) * 1000
    svar = ebit / aktiver * 100
    return {
        "fag": "Økonomi", "emne": "Afkastningsgrad",
        "sp": f"En virksomhed har et driftsresultat (EBIT) på {_kr(ebit)} kr. og samlede aktiver "
              f"på {_kr(aktiver)} kr. Beregn afkastningsgraden i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.2,
        "metode": f"Afkastningsgrad = EBIT/aktiver = {_kr(ebit)}/{_kr(aktiver)} = {_pct(svar)}%.",
    }


def g_soliditet():
    aktiver = random.choice([5, 6, 8, 10, 12]) * 1_000_000
    ek = random.choice([20, 30, 35, 40, 45, 55]) / 100 * aktiver
    svar = ek / aktiver * 100
    return {
        "fag": "Økonomi", "emne": "Soliditetsgrad",
        "sp": f"Egenkapitalen er {_kr(ek)} kr. og de samlede aktiver {_kr(aktiver)} kr. "
              f"Beregn soliditetsgraden i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.2,
        "metode": f"Soliditetsgrad = egenkapital/aktiver = {_kr(ek)}/{_kr(aktiver)} = {_pct(svar)}%.",
    }


def g_afskrivning():
    ny = random.choice([200, 300, 400, 500, 800]) * 1000
    scrap = random.choice([0, 20, 40, 50]) * 1000
    levetid = random.choice([4, 5, 8, 10])
    res = oek.lineaer_afskrivning(ny, scrap, levetid)
    svar = res["aarlig"]
    return {
        "fag": "Økonomi", "emne": "Lineær afskrivning",
        "sp": f"En maskine koster {_kr(ny)} kr. og forventes at have en scrapværdi på {_kr(scrap)} "
              f"kr. efter {levetid} år. Beregn den årlige lineære afskrivning.",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": max(abs(svar) * 0.01, 1),
        "metode": f"Årlig afskrivning = (nypris − scrap)/levetid = ({_kr(ny)} − {_kr(scrap)})/"
                  f"{levetid} = {_kr(svar)} kr.",
    }


# ---------------------------------------------------------------------------
# STATISTIK
# ---------------------------------------------------------------------------

def g_zscore():
    mu = random.choice([50, 100, 200, 500, 1000])
    sigma = random.choice([5, 10, 20, 25, 50])
    x = round(mu + random.choice([-2, -1.5, -1, 1, 1.5, 2, 2.5]) * sigma)
    svar = stat.z_score(x, mu, sigma)
    return {
        "fag": "Statistik", "emne": "z-score",
        "sp": f"En normalfordeling har middelværdi {mu} og standardafvigelse {sigma}. "
              f"Beregn z-værdien for x = {_tal(x,0)} (2 decimaler).",
        "svar": svar, "enhed": "", "dec": 2, "tol": 0.05,
        "metode": f"z = (x − µ)/σ = ({_tal(x,0)} − {mu})/{sigma} = {_pct(svar,2)}.",
    }


def g_ci_margin():
    mean = random.choice([100, 200, 250, 500])
    s = random.choice([10, 15, 20, 25, 40])
    n = random.choice([16, 25, 36, 49, 100])
    res = stat.ci_mean(mean, s, n, 0.95)
    svar = res["margin"]
    return {
        "fag": "Statistik", "emne": "Konfidensinterval (usikkerhed)",
        "sp": f"En stikprøve på n = {n} har gennemsnit {mean} og standardafvigelse s = {s}. "
              f"Beregn usikkerheden (± margin) i et 95%-konfidensinterval for middelværdien "
              f"(t·s/√n, 2 decimaler).",
        "svar": svar, "enhed": "", "dec": 2, "tol": max(abs(svar) * 0.04, 0.05),
        "metode": f"Margin = t·s/√n med t({n-1} frihedsgrader, 95%) ≈ {res['t']:.3f}. "
                  f"= {res['t']:.3f}·{s}/√{n} = {_pct(svar,2)}. "
                  f"Intervallet er {_tal(res['nedre'],1)} til {_tal(res['oevre'],1)}.",
    }


def g_binom():
    n = random.choice([8, 10, 12, 15, 20])
    p = random.choice([0.1, 0.2, 0.25, 0.3, 0.4, 0.5])
    k = random.randint(max(1, int(n * p) - 1), int(n * p) + 1)
    svar = stat.binom_pmf(k, n, p) * 100
    return {
        "fag": "Statistik", "emne": "Binomialfordeling P(X=k)",
        "sp": f"En proces har p = {_pct(p*100,0)}% sandsynlighed for succes pr. forsøg. Ved n = {n} "
              f"forsøg, beregn P(X = {k}) i procent (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": max(abs(svar) * 0.03, 0.2),
        "metode": f"P(X=k) = C({n},{k})·{p}^{k}·{round(1-p,2)}^{n-k} = {_pct(svar)}%. "
                  f"(µ = n·p = {_tal(n*p,1)}.)",
    }


def g_normalareal():
    mu = random.choice([100, 200, 500, 1000])
    sigma = random.choice([10, 20, 25, 50])
    x = round(mu + random.choice([-1.5, -1, 0.5, 1, 1.5, 2]) * sigma)
    svar = stat.normal_cdf(x, mu, sigma) * 100
    return {
        "fag": "Statistik", "emne": "Normalfordeling (areal)",
        "sp": f"En normalfordeling har µ = {mu} og σ = {sigma}. Beregn P(X < {_tal(x,0)}) i procent "
              f"(1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.6,
        "metode": f"z = ({_tal(x,0)} − {mu})/{sigma} = {_pct((x-mu)/sigma,2)}. "
                  f"P(X < {_tal(x,0)}) = P(Z < z) = {_pct(svar)}%.",
    }


# ---------------------------------------------------------------------------
# INDKØB
# ---------------------------------------------------------------------------

def g_eoq():
    D = random.choice([1200, 2400, 3600, 5000, 8000, 10000])
    S = random.choice([50, 80, 100, 150, 200, 250])
    pris = random.choice([20, 40, 50, 80, 100])
    rente = random.choice([0.10, 0.15, 0.20, 0.25])
    H = ind.holding_cost_per_unit(pris, rente)
    svar = ind.eoq(D, S, H)
    return {
        "fag": "Indkøb", "emne": "EOQ",
        "sp": f"Årligt forbrug D = {_kr(D)} stk., bestillingsomkostning S = {S} kr./ordre, "
              f"enhedspris {pris} kr. og lagerrente {_pct(rente*100,0)}%. Beregn EOQ (afrund til "
              f"hele stk.).",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": max(abs(svar) * 0.02, 1),
        "metode": f"H = pris·rente = {pris}·{rente} = {_tal(H,1)} kr./stk./år. "
                  f"EOQ = √(2·D·S/H) = √(2·{_kr(D)}·{S}/{_tal(H,1)}) = {_tal(svar,0)} stk.",
    }


def g_safety_stock():
    service = random.choice([0.90, 0.95, 0.99])
    z = ind.Z_TABLE[service]
    sigma = random.choice([10, 15, 20, 25, 40, 50])
    L = random.choice([1, 2, 4, 9])
    svar = ind.safety_stock(z, sigma, L)
    return {
        "fag": "Indkøb", "emne": "Sikkerhedslager",
        "sp": f"Efterspørgslens standardafvigelse er {sigma} pr. uge, ledetiden er {L} uger, og "
              f"ønsket serviceniveau er {_pct(service*100,0)}% (z = {_pct(z,2)}). Beregn "
              f"sikkerhedslageret (afrund til hele stk.).",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": max(abs(svar) * 0.02, 1),
        "metode": f"SS = z·σ·√L = {_pct(z,2)}·{sigma}·√{L} = {_tal(svar,0)} stk.",
    }


def g_rop():
    d = random.choice([20, 30, 40, 50, 80, 100])
    L = random.choice([2, 3, 4, 5])
    ss = random.choice([30, 50, 80, 100, 150])
    svar = ind.reorder_point(d, L, ss)
    return {
        "fag": "Indkøb", "emne": "Genbestillingspunkt (ROP)",
        "sp": f"Efterspørgslen er {d} stk./dag, ledetiden {L} dage, og sikkerhedslageret {ss} stk. "
              f"Beregn genbestillingspunktet (ROP).",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": 1,
        "metode": f"ROP = d·L + SS = {d}·{L} + {ss} = {_tal(svar,0)} stk.",
    }


# ---------------------------------------------------------------------------
# PRODUKTION
# ---------------------------------------------------------------------------

def g_oee():
    planned = random.choice([400, 420, 450, 480, 600])
    downtime = random.choice([20, 30, 40, 60, 80])
    run = planned - downtime
    ideal = round(random.choice([0.5, 1.0, 1.5, 2.0]), 1)
    total = int(run / ideal * random.choice([0.85, 0.9, 0.95]))
    good = int(total * random.choice([0.92, 0.95, 0.97, 0.99]))
    res = prod.oee(planned, downtime, ideal, total, good)
    svar = res["OEE"] * 100
    return {
        "fag": "Produktion", "emne": "OEE",
        "sp": f"Planlagt tid {planned} min., nedetid {downtime} min., ideel cyklustid {_pct(ideal,1)} "
              f"min./stk. Der blev produceret {total} stk., heraf {good} gode. Beregn OEE i % "
              f"(1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.6,
        "metode": f"Tilgængelighed = ({planned}−{downtime})/{planned} = {_pct(res['tilgaengelighed']*100)}%. "
                  f"Ydelse = ({_pct(ideal,1)}·{total})/{run} = {_pct(res['ydelse']*100)}%. "
                  f"Kvalitet = {good}/{total} = {_pct(res['kvalitet']*100)}%. "
                  f"OEE = produktet = {_pct(svar)}%.",
    }


def g_littles_T():
    R = random.choice([5, 10, 20, 25, 50])
    wip = random.choice([20, 40, 50, 100, 150])
    res = prod.littles_law(wip=wip, throughput=R)
    svar = res["T"]
    return {
        "fag": "Produktion", "emne": "Little's Law (gennemløbstid)",
        "sp": f"Der er i gennemsnit {wip} enheder i arbejde (WIP), og gennemløbshastigheden er {R} "
              f"enheder/time. Beregn gennemløbstiden T i timer (2 decimaler).",
        "svar": svar, "enhed": "timer", "dec": 2, "tol": max(abs(svar) * 0.02, 0.05),
        "metode": f"Little's Law: WIP = R·T → T = WIP/R = {wip}/{R} = {_pct(svar,2)} timer.",
    }


def g_takt():
    timer = random.choice([7, 7.5, 8])
    out = random.choice([240, 300, 360, 480, 600])
    available = timer * 3600
    svar = prod.takt_time(available, out)
    return {
        "fag": "Produktion", "emne": "Takt time",
        "sp": f"Der er {_pct(timer,1)} effektive produktionstimer på en dag, og der skal laves {out} "
              f"enheder. Beregn takt time i sekunder pr. enhed (afrund til hele sek.).",
        "svar": svar, "enhed": "sek.", "dec": 0, "tol": max(abs(svar) * 0.02, 1),
        "metode": f"Takt = tilgængelig tid/output = {int(available)} sek./{out} = {_tal(svar,0)} "
                  f"sek./enhed.",
    }


def g_utilization():
    cap = random.choice([100, 120, 150, 200, 250])
    load = random.choice([60, 70, 80, 90, 95, 110, 130])
    load = min(load, cap)
    svar = prod.utilization(load, cap) * 100
    return {
        "fag": "Produktion", "emne": "Udnyttelsesgrad",
        "sp": f"En maskine har en kapacitet på {cap} enheder/dag og belastes med {load} enheder/dag. "
              f"Beregn udnyttelsesgraden i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"Udnyttelsesgrad = belastning/kapacitet = {load}/{cap} = {_pct(svar)}%.",
    }


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

# (generator, fag) — fag bruges til at filtrere uden at kalde generatoren
_GEN = [
    (g_npv, "Økonomi"), (g_break_even, "Økonomi"), (g_daekningsgrad, "Økonomi"),
    (g_afkastningsgrad, "Økonomi"), (g_soliditet, "Økonomi"), (g_afskrivning, "Økonomi"),
    (g_zscore, "Statistik"), (g_ci_margin, "Statistik"), (g_binom, "Statistik"),
    (g_normalareal, "Statistik"),
    (g_eoq, "Indkøb"), (g_safety_stock, "Indkøb"), (g_rop, "Indkøb"),
    (g_oee, "Produktion"), (g_littles_T, "Produktion"), (g_takt, "Produktion"),
    (g_utilization, "Produktion"),
]

FAG_LISTE = ["Økonomi", "Statistik", "Indkøb", "Produktion"]


def lav_opgave(fag: str | None = None) -> dict:
    """Lav én tilfældig regneopgave (evt. begrænset til ét fag)."""
    if fag and fag != "Alle":
        pulje = [g for g, f in _GEN if f == fag]
    else:
        pulje = [g for g, _ in _GEN]
    return random.choice(pulje)()
