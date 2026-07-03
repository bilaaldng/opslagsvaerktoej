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

import math
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
# FLERE: økonomi, statistik, indkøb, produktion
# ---------------------------------------------------------------------------

def g_payback():
    inv = random.choice([200, 300, 400, 500]) * 1000
    a = random.choice([80, 100, 120, 150]) * 1000
    cfs = [-inv] + [a] * 8
    svar = oek.payback(cfs)
    return {
        "fag": "Økonomi", "emne": "Payback (tilbagebetalingstid)",
        "sp": f"En investering på {_kr(inv)} kr. giver {_kr(a)} kr. om året. Beregn "
              f"tilbagebetalingstiden (payback) i år (2 decimaler).",
        "svar": svar, "enhed": "år", "dec": 2, "tol": max(abs(svar) * 0.02, 0.05),
        "metode": f"Payback = investering/årligt cashflow = {_kr(inv)}/{_kr(a)} = "
                  f"{_pct(svar, 2)} år (akkumuleret cashflow når 0).",
    }


def g_overskudsgrad():
    oms = random.choice([5, 8, 10, 12, 20]) * 1_000_000
    ebit = random.choice([300, 500, 800, 1200, 2000]) * 1000
    svar = ebit / oms * 100
    return {
        "fag": "Økonomi", "emne": "Overskudsgrad",
        "sp": f"Driftsresultatet (EBIT) er {_kr(ebit)} kr. og omsætningen {_kr(oms)} kr. Beregn "
              f"overskudsgraden i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.2,
        "metode": f"Overskudsgrad = EBIT/omsætning = {_kr(ebit)}/{_kr(oms)} = {_pct(svar)}%.",
    }


def g_likviditetsgrad():
    oa = random.choice([2, 3, 4, 5, 6]) * 1_000_000
    kg = random.choice([2, 3, 4]) * 1_000_000
    svar = oa / kg * 100
    return {
        "fag": "Økonomi", "emne": "Likviditetsgrad",
        "sp": f"Omsætningsaktiverne er {_kr(oa)} kr. og den kortfristede gæld {_kr(kg)} kr. Beregn "
              f"likviditetsgraden i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"Likviditetsgrad = omsætningsaktiver/kortfristet gæld = {_kr(oa)}/{_kr(kg)} = "
                  f"{_pct(svar)}%.",
    }


def g_gearing():
    gaeld = random.choice([2, 3, 4, 6, 8]) * 1_000_000
    ek = random.choice([2, 3, 4, 5]) * 1_000_000
    svar = gaeld / ek
    return {
        "fag": "Økonomi", "emne": "Gearing",
        "sp": f"Den samlede gæld er {_kr(gaeld)} kr. og egenkapitalen {_kr(ek)} kr. Beregn "
              f"gearingen (gæld/egenkapital, 2 decimaler).",
        "svar": svar, "enhed": "", "dec": 2, "tol": max(abs(svar) * 0.02, 0.03),
        "metode": f"Gearing = gæld/egenkapital = {_kr(gaeld)}/{_kr(ek)} = {_pct(svar, 2)}.",
    }


def g_bidrag_salgspris():
    kost = random.choice([100, 150, 200, 300, 400])
    dg = random.choice([0.30, 0.40, 0.50, 0.60])
    res = oek.bidragskalkulation(kost, dg)
    svar = res["salgspris"]
    return {
        "fag": "Økonomi", "emne": "Bidragskalkulation (salgspris)",
        "sp": f"Kostprisen er {kost} kr. og den ønskede dækningsgrad er {_pct(dg*100,0)}%. Beregn "
              f"salgsprisen (afrund til hele kr.).",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": max(abs(svar) * 0.01, 1),
        "metode": f"DB = kostpris·DG/(1−DG) = {kost}·{dg}/{round(1-dg,2)} = {_tal(res['db'],0)} kr. "
                  f"Salgspris = kostpris + DB = {kost} + {_tal(res['db'],0)} = {_tal(svar,0)} kr.",
    }


def g_ci_andel():
    n = random.choice([100, 200, 400, 500])
    x = random.randint(int(n * 0.2), int(n * 0.6))
    phat = x / n
    res = stat.ci_proportion(phat, n, 0.95)
    svar = res["margin"] * 100
    return {
        "fag": "Statistik", "emne": "Konfidensinterval (andel)",
        "sp": f"Af {n} adspurgte svarede {x} ja (andel p̂ = {_pct(phat*100,1)}%). Beregn 95%-"
              f"konfidensintervallets margin i procentpoint (z = 1,96, 2 decimaler).",
        "svar": svar, "enhed": "pp", "dec": 2, "tol": max(abs(svar) * 0.04, 0.05),
        "metode": f"Margin = z·√(p̂(1−p̂)/n) = 1,96·√({round(phat,3)}·{round(1-phat,3)}/{n}) = "
                  f"{_pct(svar,2)} procentpoint. Interval: {_pct(res['nedre']*100,1)}% til "
                  f"{_pct(res['oevre']*100,1)}%.",
    }


def g_p_ucl():
    pbar = random.choice([0.02, 0.03, 0.05, 0.08, 0.10])
    n = random.choice([100, 150, 200, 300])
    svar = (pbar + 3 * math.sqrt(pbar * (1 - pbar) / n)) * 100
    return {
        "fag": "Statistik", "emne": "Kontrolkort (p-kort UCL)",
        "sp": f"Den gennemsnitlige fejlandel er p̄ = {_pct(pbar*100,0)}%, og stikprøvestørrelsen er "
              f"n = {n}. Beregn den øvre kontrolgrænse (UCL) for p-kortet i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": max(abs(svar) * 0.02, 0.1),
        "metode": f"UCL = p̄ + 3·√(p̄(1−p̄)/n) = {pbar} + 3·√({pbar}·{round(1-pbar,2)}/{n}) = "
                  f"{_pct(svar)}%.",
    }


def g_poq():
    D = random.choice([5000, 8000, 10000, 12000, 20000])
    S = random.choice([100, 150, 200, 300])
    pris = random.choice([20, 40, 50, 80])
    rente = random.choice([0.10, 0.15, 0.20, 0.25])
    H = pris * rente
    d = random.choice([20, 30, 40, 50])
    p = d + random.choice([20, 40, 60, 80])
    svar = ind.epq(D, S, H, d, p)
    return {
        "fag": "Indkøb", "emne": "POQ / EPQ (produktionsserie)",
        "sp": f"Årligt forbrug D = {_kr(D)}, igangsætningsomkostning S = {S} kr., enhedspris {pris} "
              f"kr., lagerrente {_pct(rente*100,0)}%. Daglig efterspørgsel d = {d}, daglig "
              f"produktion p = {p}. Beregn POQ (afrund til hele stk.).",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": max(abs(svar) * 0.02, 1),
        "metode": f"H = {pris}·{rente} = {_tal(H,1)}. Korrektion (1−d/p) = (1−{d}/{p}) = "
                  f"{round(1-d/p,3)}. POQ = √(2·D·S/(H·(1−d/p))) = {_tal(svar,0)} stk.",
    }


def g_littles_wip():
    R = random.choice([5, 10, 20, 25, 50, 100])
    T = random.choice([2, 3, 4, 5, 8])
    svar = prod.littles_law(throughput=R, flow_time=T)["WIP"]
    return {
        "fag": "Produktion", "emne": "Little's Law (WIP)",
        "sp": f"Gennemløbshastigheden er {R} enheder/time, og gennemløbstiden er {T} timer. Beregn "
              f"WIP (antal enheder i arbejde).",
        "svar": svar, "enhed": "enheder", "dec": 0, "tol": 1,
        "metode": f"Little's Law: WIP = R·T = {R}·{T} = {_tal(svar,0)} enheder.",
    }


def g_line_balance():
    times = [random.choice([20, 25, 30, 35, 40, 45]) for _ in range(random.choice([4, 5, 6]))]
    res = prod.line_balance(times)
    svar = res["effektivitet"] * 100
    return {
        "fag": "Produktion", "emne": "Linjebalancering (effektivitet)",
        "sp": f"En samlebånds-linje har stationstider {times} sek. Beregn linjens effektivitet i % "
              f"(Σtid / (antal stationer · cyklustid), 1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.5,
        "metode": f"Cyklustid = max = {max(times)} sek. Σtid = {sum(times)} sek. "
                  f"Effektivitet = {sum(times)}/({len(times)}·{max(times)}) = {_pct(svar)}%.",
    }


def g_min_stations():
    timer = random.choice([7.0, 7.5, 8.0])
    out = random.choice([400, 500, 600, 700, 800])
    tasks = [random.choice([20, 25, 30, 35, 40]) for _ in range(random.choice([5, 6, 7]))]
    available = timer * 3600
    takt = prod.takt_time(available, out)
    svar = prod.theoretical_min_stations(tasks, takt)
    return {
        "fag": "Produktion", "emne": "Min. antal stationer",
        "sp": f"Der er {int(available)} sek. til rådighed og skal laves {out} stk. Opgavetiderne er "
              f"{tasks} sek. Beregn det teoretiske min. antal stationer.",
        "svar": float(svar), "enhed": "stationer", "dec": 0, "tol": 0.5,
        "metode": f"Takt time = {int(available)}/{out} = {_tal(takt,1)} sek. Σopgavetid = "
                  f"{sum(tasks)} sek. Min. stationer = loft({sum(tasks)}/{_tal(takt,1)}) = {svar}.",
    }


# ---------------------------------------------------------------------------
# UDVIDELSE (2026-07-03): flere opgavetyper — alle facit beregnes via core/*.py
# Hver generator har også statiske 'fortolk'- og 'faelde'-felter (det eksaminator
# spørger om efter tallet). Emnerne er neutrale — casen er kun kilde til metoden.
# ---------------------------------------------------------------------------

def g_irr():
    inv = random.choice([300, 400, 500, 600]) * 1000
    n = random.choice([4, 5, 6])
    faktor = random.choice([1.3, 1.4, 1.5, 1.6])
    a = max(round(inv * faktor / n / 10000) * 10000, 10000)
    cfs = [-inv] + [a] * n
    svar = oek.irr(cfs) * 100
    return {
        "fag": "Økonomi", "emne": "IRR (intern rente)",
        "sp": f"En investering koster {_kr(inv)} kr. og giver {_kr(a)} kr. om året i {n} år. "
              f"Beregn den interne rente (IRR) i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"IRR er renten hvor NPV = 0. Med −{_kr(inv)} kr. og {n} × {_kr(a)} kr. "
                  f"løses NPV(r) = 0 → IRR ≈ {_pct(svar)}%.",
        "fortolk": "IRR holdes op mod kalkulationsrenten (afkastkravet): er IRR højere, tjener "
                   "investeringen mere end kravet og er lønsom.",
        "faelde": "IRR kan ikke stå alene — to projekter med samme IRR kan have vidt forskellig "
                  "NPV i kroner. Ved valg mellem projekter vinder højeste NPV, ikke højeste IRR.",
    }


def g_kritisk_levetid():
    inv = random.choice([300, 400, 500, 600]) * 1000
    n = random.choice([6, 7, 8])
    faktor = random.choice([1.6, 1.8, 2.0])
    a = max(round(inv * faktor / n / 10000) * 10000, 10000)
    r = random.choice([6, 7, 8, 10])
    cfs = [-inv] + [a] * n
    svar = oek.kritisk_levetid(cfs, r / 100)
    return {
        "fag": "Økonomi", "emne": "Kritisk levetid",
        "sp": f"En investering på {_kr(inv)} kr. giver {_kr(a)} kr. om året, kalkulationsrente "
              f"{r}%. Hvor mange år skal den mindst holde, før den er tjent hjem (NPV = 0)? "
              f"(2 decimaler).",
        "svar": svar, "enhed": "år", "dec": 2, "tol": max(abs(svar) * 0.02, 0.05),
        "metode": f"Læg de tilbagediskonterede indbetalinger sammen år for år, til de dækker "
                  f"{_kr(inv)} kr. Grænsen nås efter ≈ {_pct(svar, 2)} år.",
        "fortolk": "Holder investeringen kortere end den kritiske levetid, når den ALDRIG at "
                   "blive tjent hjem — så er den ulønsom.",
        "faelde": "Regn med de TILBAGEDISKONTEREDE beløb, ikke de rå. Uden diskontering får du "
                  "en for kort (for optimistisk) levetid.",
    }


def g_nulpunktsomsaetning():
    pris = random.choice([150, 200, 250, 300, 400])
    var = min(random.choice([60, 90, 120, 150]), pris - 30)
    faste = random.choice([300, 400, 500, 750]) * 1000
    res = oek.break_even(pris, var, faste)
    svar = res["nulpunktsomsaetning"]
    return {
        "fag": "Økonomi", "emne": "Nulpunktsomsætning",
        "sp": f"Faste omkostninger {_kr(faste)} kr., salgspris {pris} kr./stk., variable "
              f"enhedsomkostninger {var} kr. Beregn nulpunktsOMSÆTNINGEN i kr. (afrund).",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": max(abs(svar) * 0.02, 100),
        "metode": f"DB = {pris} − {var} = {pris-var} kr. Nulpunktsmængde = {_kr(faste)}/{pris-var} "
                  f"= {_tal(res['nulpunktsmaengde'],0)} stk. Nulpunktsomsætning = mængde·pris = "
                  f"{_kr(svar)} kr.",
        "fortolk": "Under denne omsætning giver virksomheden underskud; over den, overskud.",
        "faelde": "Nulpunktsomsætning = mængde · SALGSPRIS — ikke mængde · dækningsbidrag.",
    }


def g_sikkerhedsmargin():
    pris = random.choice([150, 200, 250, 300])
    var = min(random.choice([60, 90, 120]), pris - 30)
    faste = random.choice([300, 400, 500]) * 1000
    be = oek.break_even(pris, var, faste)
    faktisk = round(be["nulpunktsomsaetning"] * random.choice([1.2, 1.3, 1.4, 1.5]) / 1000) * 1000
    svar = oek.safety_margin(faktisk, be["nulpunktsomsaetning"]) * 100
    return {
        "fag": "Økonomi", "emne": "Sikkerhedsmargin",
        "sp": f"Den faktiske omsætning er {_kr(faktisk)} kr., og nulpunktsomsætningen er "
              f"{_kr(be['nulpunktsomsaetning'])} kr. Beregn sikkerhedsmarginen i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"Sikkerhedsmargin = (omsætning − nulpunktsomsætning)/omsætning = "
                  f"({_kr(faktisk)} − {_kr(be['nulpunktsomsaetning'])})/{_kr(faktisk)} = {_pct(svar)}%.",
        "fortolk": "Hvor meget omsætningen må falde, før virksomheden rammer nulpunktet. "
                   "Høj margin = mere robust mod nedgang.",
        "faelde": "Marginen måles i forhold til den FAKTISKE omsætning, ikke nulpunktsomsætningen.",
    }


def g_retrograd():
    salgspris = random.choice([200, 250, 300, 400, 500])
    dg = random.choice([0.30, 0.40, 0.50])
    vso = random.choice([10, 20, 30, 40])
    told = random.choice([0.00, 0.05, 0.10])
    res = oek.retrograd_kalkulation(salgspris, dg, vso, told)
    svar = res["maks_koebspris"]
    return {
        "fag": "Økonomi", "emne": "Retrograd kalkulation (maks. købspris)",
        "sp": f"Markedsprisen er fast på {salgspris} kr., den ønskede dækningsgrad er "
              f"{_pct(dg*100,0)}%, variable salgsomkostninger {vso} kr./stk. og told "
              f"{_pct(told*100,0)}% af købsprisen. Hvad er den HØJESTE indkøbspris du må betale? "
              f"(afrund).",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": max(abs(svar) * 0.01, 1),
        "metode": f"Baglæns fra prisen: DB = {salgspris}·{_pct(dg*100,0)}% = {_tal(res['db'],0)} kr. "
                  f"Maks. købspris = (salgspris·(1−DG) − salgsomk.)/(1+told) = "
                  f"({salgspris}·{round(1-dg,2)} − {vso})/{round(1+told,2)} = {_tal(svar,0)} kr.",
        "fortolk": "Retrograd bruges når markedet bestemmer prisen: du regner BAGLÆNS til hvad "
                   "varen højst må koste i indkøb, hvis din avance skal holde.",
        "faelde": "Her er salgsprisen fast — en HØJERE ønsket dækningsgrad giver en LAVERE maks. "
                  "købspris (modsat bidragskalkulation, hvor prisen stiger med DG).",
    }


def g_prisoptimering():
    p0 = random.choice([80, 100, 120])
    step = random.choice([20, 25, 30])
    q0 = random.choice([1000, 1200, 1400])
    dq = random.choice([150, 200, 250])
    priser = [p0 + step * i for i in range(5)]
    afsaetning = [q0 - dq * i for i in range(5)]
    var = random.choice([30, 40, 50])
    faste = random.choice([20, 30, 40]) * 1000
    res = oek.prisoptimering(priser, afsaetning, var, faste)
    svar = res["optimal_pris"]
    return {
        "fag": "Økonomi", "emne": "Prisoptimering (optimal pris)",
        "sp": f"Priser {priser} kr. giver afsætning {afsaetning} stk. Variable enhedsomkostninger "
              f"{var} kr., faste {_kr(faste)} kr. Ved hvilken pris er overskuddet størst? (kr.).",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": 0.5,
        "metode": f"Regn overskud = pris·mængde − (variabel·mængde + faste) for hver pris. "
                  f"Størst ved {_tal(svar,0)} kr. (afsætning {_tal(res['optimal_afsaetning'],0)} "
                  f"stk., overskud {_kr(res['max_overskud'])} kr.).",
        "fortolk": "Optimum ligger hvor grænseomsætning = grænseomkostning; totalmetoden finder "
                   "samme punkt ved at maksimere overskuddet direkte.",
        "faelde": "Højeste pris giver ikke størst overskud — en høj pris sænker afsætningen. "
                  "Det er overskuddet i kroner, ikke prisen eller omsætningen, der optimeres.",
    }


def g_forecast_mad():
    n = random.choice([4, 5, 6])
    actual = [random.choice([80, 90, 100, 110, 120, 130]) for _ in range(n)]
    forecast = [a + random.choice([-15, -10, -5, 5, 10, 15]) for a in actual]
    res = ind.forecast_errors(actual, forecast)
    svar = res["MAD"]
    return {
        "fag": "Indkøb", "emne": "Forecast-fejl (MAD)",
        "sp": f"Faktisk efterspørgsel var {actual}, forecast var {forecast}. Beregn MAD "
              f"(gennemsnitlig absolut afvigelse, 1 decimal).",
        "svar": svar, "enhed": "", "dec": 1, "tol": max(abs(svar) * 0.02, 0.1),
        "metode": f"Fejl pr. periode = faktisk − forecast. MAD = gennemsnit af de NUMERISKE "
                  f"fejl (fortegn ignoreres) = {_pct(svar,1)}.",
        "fortolk": "MAD viser den typiske fejlstørrelse. Lav MAD = et præcist forecast, du kan "
                   "styre lager og sikkerhedslager efter.",
        "faelde": "MAD bruger de ABSOLUTTE fejl. Bruger du fortegnene (som i bias/MFE), ophæver "
                  "plus og minus hinanden, og du undervurderer fejlen.",
    }


def g_vaegtet_score():
    krit = ["Pris", "Kvalitet", "Levering"]
    vaegte = random.choice([[0.5, 0.3, 0.2], [0.4, 0.4, 0.2], [0.6, 0.2, 0.2]])
    scores = {k: random.choice([2, 3, 4, 5]) for k in krit}
    weights = {k: v for k, v in zip(krit, vaegte)}
    svar = ind.weighted_score(scores, weights)
    dele = " + ".join(f"{scores[k]}·{_pct(weights[k]*100,0)}%" for k in krit)
    return {
        "fag": "Indkøb", "emne": "Vægtet leverandørscore",
        "sp": f"En leverandør scores (1-5): Pris {scores['Pris']}, Kvalitet {scores['Kvalitet']}, "
              f"Levering {scores['Levering']}. Vægtene er Pris {_pct(weights['Pris']*100,0)}%, "
              f"Kvalitet {_pct(weights['Kvalitet']*100,0)}%, Levering "
              f"{_pct(weights['Levering']*100,0)}%. Beregn den samlede vægtede score (2 decimaler).",
        "svar": svar, "enhed": "", "dec": 2, "tol": 0.03,
        "metode": f"Samlet score = Σ(score · vægt) = {dele} = {_pct(svar,2)}.",
        "fortolk": "Den vægtede score gør leverandører sammenlignelige på tværs af bløde og hårde "
                   "kriterier — højeste score vinder, alt andet lige.",
        "faelde": "Vægtene skal summe til 100%. Tag ikke bare et simpelt gennemsnit af scorerne — "
                  "så ignorerer du hvilke kriterier der betyder mest.",
    }


def g_periodisk_R():
    d = random.choice([20, 30, 40, 50, 80])
    P = random.choice([2, 3, 4])
    L = random.choice([1, 2, 3])
    ss = random.choice([30, 50, 80, 100])
    svar = ind.periodic_max_level(d, P, L, ss)
    return {
        "fag": "Indkøb", "emne": "Periodisk review (max-niveau R)",
        "sp": f"Efterspørgslen er {d} stk./uge, review-intervallet P = {P} uger, ledetiden "
              f"L = {L} uger og sikkerhedslageret {ss} stk. Beregn max-niveauet R.",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": 1,
        "metode": f"R = d·(P+L) + SS = {d}·({P}+{L}) + {ss} = {_tal(svar,0)} stk.",
        "fortolk": "Ved hvert tjek bestilles op til R. Dækker både review-intervallet OG ledetiden, "
                   "fordi du først kan reagere igen næste periode.",
        "faelde": "Perioden skal være P+L, ikke kun L. Glemmer du review-intervallet, løber du tør, "
                  "inden næste bestilling når frem.",
    }


def g_makebuy_breakeven():
    koeb_var = random.choice([80, 100, 120, 150])
    egen_fast = random.choice([100, 150, 200, 300]) * 1000
    egen_var = koeb_var - random.choice([20, 30, 40, 50])
    svar = ind.breakeven_volume(0, koeb_var, egen_fast, egen_var)
    return {
        "fag": "Indkøb", "emne": "Make-vs-buy (breakeven-volumen)",
        "sp": f"KØB koster {koeb_var} kr./stk. (ingen faste). EGENPRODUKTION koster {_kr(egen_fast)} "
              f"kr. i faste + {egen_var} kr./stk. Ved hvilket årligt volumen koster de to lige "
              f"meget? (afrund til stk.).",
        "svar": svar, "enhed": "stk.", "dec": 0, "tol": max(abs(svar) * 0.02, 1),
        "metode": f"Sæt totalerne lig: {koeb_var}·x = {_kr(egen_fast)} + {egen_var}·x → "
                  f"x = {_kr(egen_fast)}/({koeb_var}−{egen_var}) = {_tal(svar,0)} stk.",
        "fortolk": "Over dette volumen kan egenproduktion betale sig (de faste fordeles på flere "
                   "stk.); under det er køb billigst.",
        "faelde": "Breakeven alene afgør ikke valget — kvalitet, leveringstid, kapacitet og "
                  "risiko skal med. Billigst på papiret er ikke altid bedst.",
    }


def g_otif():
    ot = random.choice([90, 92, 94, 95, 96, 98])
    iff = random.choice([88, 90, 92, 95, 97])
    res = prod.otif(ot, iff, total=100)
    svar = res["OTIF"] * 100
    return {
        "fag": "Produktion", "emne": "OTIF (On Time In Full)",
        "sp": f"{ot}% af ordrerne kom til tiden, og {iff}% kom komplet. Hvis de to ting er "
              f"uafhængige, hvad er OTIF (til tiden OG komplet) i % (1 decimal)?",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"OTIF = andel til tiden · andel komplet = {ot/100:.2f}·{iff/100:.2f} = "
                  f"{_pct(svar)}%.",
        "fortolk": "OTIF straffer hårdt: begge krav skal være opfyldt samtidig, så tallet er "
                   "altid lavere end hver enkelt andel.",
        "faelde": "Tag IKKE gennemsnittet af de to andele — de ganges (ved uafhængighed). "
                  "Gennemsnit overvurderer leveringsevnen.",
    }


def g_knap_kapacitet():
    a_db, a_tid, a_eft = random.choice([160, 200, 240]), random.choice([4, 5]), random.choice([300, 400])
    b_db, b_tid, b_eft = random.choice([180, 220, 260]), random.choice([6, 8]), random.choice([250, 350])
    tid = random.choice([1800, 2000, 2400, 3000])
    produkter = [
        {"navn": "A", "db_stk": a_db, "tid_pr_stk": a_tid, "efterspoergsel": a_eft},
        {"navn": "B", "db_stk": b_db, "tid_pr_stk": b_tid, "efterspoergsel": b_eft},
    ]
    res = prod.knap_kapacitet(produkter, tid)
    svar = res["samlet_db"]
    ap, bp = a_db / a_tid, b_db / b_tid
    foerst = "A" if ap >= bp else "B"
    return {
        "fag": "Produktion", "emne": "Knap kapacitet (DB pr. flaskehalstime)",
        "sp": f"Flaskehalsen har {tid} min. til rådighed. Produkt A: DB {a_db} kr./stk., {a_tid} "
              f"min./stk., efterspørgsel {a_eft} stk. Produkt B: DB {b_db} kr./stk., {b_tid} "
              f"min./stk., efterspørgsel {b_eft} stk. Hvad er det størst mulige samlede "
              f"dækningsbidrag? (afrund til kr.).",
        "svar": svar, "enhed": "kr.", "dec": 0, "tol": max(abs(svar) * 0.02, 100),
        "metode": f"Prioritér efter DB pr. flaskehalstime: A = {a_db}/{a_tid} = {_tal(ap,0)} "
                  f"kr./min., B = {b_db}/{b_tid} = {_tal(bp,0)} kr./min. Producér {foerst} først "
                  f"op til efterspørgsel, fyld resten med det andet → samlet DB {_kr(svar)} kr.",
        "fortolk": "Når en ressource er knap, er det DB pr. FLASKEHALSTIME der tæller — ikke DB "
                   "pr. stk. Det produkt der tjener mest pr. knap minut, laves først.",
        "faelde": "Ranger IKKE efter DB pr. stk. Et produkt med højt DB/stk. kan være en dårlig "
                  "forretning, hvis det bruger uforholdsmæssigt meget flaskehalstid.",
    }


def g_mm1():
    my = random.choice([12, 15, 20, 25, 30])
    lam = random.choice([v for v in [6, 8, 10, 12, 16, 18] if v < my])
    res = prod.queue_metrics(lam, my)
    svar = res["rho"] * 100
    return {
        "fag": "Produktion", "emne": "Udnyttelsesgrad ρ (kø)",
        "sp": f"En ressource får {lam} enheder/time (λ) og kan behandle {my} enheder/time (μ). "
              f"Beregn udnyttelsesgraden ρ i % (1 decimal).",
        "svar": svar, "enhed": "%", "dec": 1, "tol": 0.3,
        "metode": f"ρ = λ/μ = {lam}/{my} = {_pct(svar)}%.",
        "fortolk": "ρ er hvor stor en andel af tiden ressourcen er optaget. Jo tættere på 100%, "
                   "jo længere køer og ventetider — de eksploderer, når ρ nærmer sig 1.",
        "faelde": "Fuld udnyttelse (ρ ≈ 100%) er ikke et mål: ventetiden går mod uendelig. "
                  "Lidt luft i kapaciteten holder køen nede.",
    }


def g_omvendt_normal():
    mu = random.choice([100, 200, 500, 1000])
    sigma = random.choice([10, 20, 25, 50])
    p = random.choice([0.05, 0.10, 0.90, 0.95, 0.975])
    z = stat.prob_to_z(p)
    svar = mu + z * sigma
    p_vis = _pct(p * 100, 1).rstrip("0").rstrip(",")
    return {
        "fag": "Statistik", "emne": "Omvendt normalfordeling (find x)",
        "sp": f"En normalfordeling har µ = {mu} og σ = {sigma}. Find den værdi x, hvor "
              f"P(X < x) = {p_vis}% (1 decimal).",
        "svar": svar, "enhed": "", "dec": 1, "tol": max(abs(svar) * 0.01, 0.3),
        "metode": f"Find først z ud fra sandsynligheden: z = {_pct(z,2)}. "
                  f"x = µ + z·σ = {mu} + {_pct(z,2)}·{sigma} = {_pct(svar,1)}.",
        "fortolk": "Den omvendte vej: fra en ønsket sandsynlighed/percentil tilbage til en "
                   "konkret grænseværdi — fx serviceniveau → nødvendigt lagerniveau.",
        "faelde": "Ved sandsynligheder under 50% er z NEGATIV, så x ligger under middelværdien. "
                  "Tjek fortegnet på z, før du regner videre.",
    }


def g_regression_forudsig():
    b = random.choice([2, 3, 4, 5])
    a = random.choice([10, 20, 30, 50])
    xs = [1, 2, 3, 4, 5]
    ys = [a + b * x + random.choice([-2, -1, 0, 1, 2]) for x in xs]
    reg = stat.linear_regression(xs, ys)
    xny = random.choice([6, 7, 8])
    svar = stat.regression_predict(xny, reg["haeldning"], reg["skaering"])
    return {
        "fag": "Statistik", "emne": "Regression (forudsigelse)",
        "sp": f"Datapunkter (x, y): {list(zip(xs, ys))}. Find regressionslinjen og forudsig y "
              f"for x = {xny} (1 decimal).",
        "svar": svar, "enhed": "", "dec": 1, "tol": max(abs(svar) * 0.05, 0.5),
        "metode": f"Mindste kvadraters linje: hældning b ≈ {_pct(reg['haeldning'],2)}, skæring "
                  f"a ≈ {_pct(reg['skaering'],2)} (R² = {_pct(reg['r2'],2)}). "
                  f"ŷ = a + b·x = {_pct(reg['skaering'],1)} + {_pct(reg['haeldning'],2)}·{xny} = "
                  f"{_pct(svar,1)}.",
        "fortolk": "Regression bruger den historiske sammenhæng til at forudsige. R² tæt på 1 "
                   "betyder, at x forklarer y godt — så forudsigelsen er mere pålidelig.",
        "faelde": "Forudsig kun inden for (eller nær) dataområdet. Ekstrapolerer du langt uden "
                  "for x-værdierne, kan sammenhængen være brudt sammen.",
    }


def g_hypotesetest_z():
    mu0 = random.choice([50, 75, 100, 200])
    sigma = random.choice([8, 10, 12, 15])
    n = random.choice([25, 36, 100])
    diff = random.choice([-3, -2, 2, 3, 4]) * (sigma / math.sqrt(n))
    mean = round(mu0 + diff, 2)
    res = stat.z_test_mean(mean, sigma, n, mu0, "hoejre")
    svar = res["z"]
    return {
        "fag": "Statistik", "emne": "Hypotesetest (teststørrelse z)",
        "sp": f"Du tester H0: µ = {mu0} mod H1: µ > {mu0}. Stikprøven har gennemsnit {_pct(mean,2)}, "
              f"σ = {sigma} og n = {n}. Beregn teststørrelsen z (2 decimaler).",
        "svar": svar, "enhed": "", "dec": 2, "tol": 0.05,
        "metode": f"Standardfejl = σ/√n = {sigma}/√{n} = {_pct(res['se'],3)}. "
                  f"z = (x̄ − µ0)/standardfejl = ({_pct(mean,2)} − {mu0})/{_pct(res['se'],3)} = "
                  f"{_pct(svar,2)}. Kritisk værdi (5%, ensidet) = 1,645.",
        "fortolk": "Er z større end den kritiske værdi (1,645 ved 5% ensidet), forkastes H0 — "
                   "gennemsnittet er så signifikant større end påstanden.",
        "faelde": "p-værdien er IKKE sandsynligheden for at H0 er sand. Den er sandsynligheden "
                  "for at se dette resultat (eller mere ekstremt), HVIS H0 var sand.",
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
    # Tilføjet senere
    (g_payback, "Økonomi"), (g_overskudsgrad, "Økonomi"), (g_likviditetsgrad, "Økonomi"),
    (g_gearing, "Økonomi"), (g_bidrag_salgspris, "Økonomi"),
    (g_ci_andel, "Statistik"), (g_p_ucl, "Statistik"),
    (g_poq, "Indkøb"),
    (g_littles_wip, "Produktion"), (g_line_balance, "Produktion"), (g_min_stations, "Produktion"),
    # Udvidelse 2026-07-03 — dækker de tidligere manglende opgavetyper
    (g_irr, "Økonomi"), (g_kritisk_levetid, "Økonomi"), (g_nulpunktsomsaetning, "Økonomi"),
    (g_sikkerhedsmargin, "Økonomi"), (g_retrograd, "Økonomi"), (g_prisoptimering, "Økonomi"),
    (g_forecast_mad, "Indkøb"), (g_vaegtet_score, "Indkøb"), (g_periodisk_R, "Indkøb"),
    (g_makebuy_breakeven, "Indkøb"),
    (g_otif, "Produktion"), (g_knap_kapacitet, "Produktion"), (g_mm1, "Produktion"),
    (g_omvendt_normal, "Statistik"), (g_regression_forudsig, "Statistik"),
    (g_hypotesetest_z, "Statistik"),
]

FAG_LISTE = ["Økonomi", "Statistik", "Indkøb", "Produktion"]


def lav_opgave(fag: str | None = None) -> dict:
    """Lav én tilfældig regneopgave (evt. begrænset til ét fag)."""
    if fag and fag != "Alle":
        pulje = [g for g, f in _GEN if f == fag]
    else:
        pulje = [g for g, _ in _GEN]
    return random.choice(pulje)()
