"""Ren matematik for Økonomi-modulet.

Ingen Streamlit-kald herinde. Notation matcher brugerens danish-okonomi-skill + VIDEN §7.

    Kapitalværdi (NPV) = Σ cashflow_t / (1+r)^t   (cashflow_0 = −startinvestering)
    Intern rente (IRR) = renten hvor NPV = 0
    Nulpunktsomsætning = kapacitetsomk. / dækningsgrad
    Bidragskalkulation: salgspris = kostpris + DB,  DB = kostpris·DG/(1−DG)
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import brentq


# ---------------------------------------------------------------------------
# Investeringskalkule
# ---------------------------------------------------------------------------

def npv(rate: float, cashflows: list[float]) -> float:
    """Kapitalværdi. cashflows[0] = år 0 (typisk −startinvestering)."""
    return float(sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows)))


def irr(cashflows: list[float]) -> float:
    """Intern rente: renten hvor NPV = 0 (første fortegnsskift fundet)."""
    f = lambda r: npv(r, cashflows)
    rates = np.linspace(-0.99, 10.0, 4000)
    vals = [f(r) for r in rates]
    for i in range(len(rates) - 1):
        if vals[i] == 0:
            return float(rates[i])
        if vals[i] * vals[i + 1] < 0:
            return float(brentq(f, rates[i], rates[i + 1]))
    return float("nan")


def payback(cashflows: list[float]) -> float:
    """Tilbagebetalingstid (år, med interpolation). cashflows[0] = år 0."""
    cum = cashflows[0]
    for t in range(1, len(cashflows)):
        if cum + cashflows[t] >= 0:
            return (t - 1) + (-cum) / cashflows[t] if cashflows[t] else float(t)
        cum += cashflows[t]
    return float("nan")


def kritisk_levetid(cashflows: list[float], rate: float) -> float:
    """Mindste levetid (år) før investeringen er tjent hjem (NPV = 0)."""
    investering = -cashflows[0]
    disc_cum = 0.0
    for t in range(1, len(cashflows)):
        d = cashflows[t] / (1 + rate) ** t
        if disc_cum + d >= investering:
            return (t - 1) + (investering - disc_cum) / d if d else float(t)
        disc_cum += d
    return float("nan")


def npv_profile(cashflows: list[float], rates: np.ndarray) -> np.ndarray:
    """NPV ved hver rente (til NPV-profilen der krydser nul ved IRR)."""
    return np.array([npv(r, cashflows) for r in rates])


def investering_summary(cashflows: list[float], rate: float) -> dict:
    return {
        "NPV": npv(rate, cashflows),
        "IRR": irr(cashflows),
        "payback": payback(cashflows),
        "kritisk_levetid": kritisk_levetid(cashflows, rate),
    }


# ---------------------------------------------------------------------------
# Break-even / nulpunktsanalyse
# ---------------------------------------------------------------------------

def daekningsgrad(pris: float, variabel: float) -> float:
    """Dækningsgrad = DB/salgspris = (pris − variabel)/pris."""
    return (pris - variabel) / pris if pris else float("nan")


def break_even(pris: float, variabel: float, faste: float) -> dict:
    """Nulpunktsanalyse. DB pr. stk, nulpunktsmængde og nulpunktsomsætning."""
    db = pris - variabel
    dg = db / pris if pris else float("nan")
    qty = faste / db if db > 0 else float("nan")
    return {
        "db_stk": db,
        "daekningsgrad": dg,
        "nulpunktsmaengde": qty,
        "nulpunktsomsaetning": qty * pris if qty == qty else float("nan"),
    }


def safety_margin(omsaetning: float, nulpunktsomsaetning: float) -> float:
    """Sikkerhedsmargin = (omsætning − nulpunktsomsætning)/omsætning."""
    return (omsaetning - nulpunktsomsaetning) / omsaetning if omsaetning else float("nan")


# ---------------------------------------------------------------------------
# Priskalkulation
# ---------------------------------------------------------------------------

def bidragskalkulation(kostpris: float, dg: float) -> dict:
    """Fremad fra kostpris: DB = kostpris·DG/(1−DG), salgspris = kostpris + DB."""
    db = kostpris * dg / (1 - dg) if dg < 1 else float("nan")
    salgspris = kostpris + db
    return {"db": db, "salgspris": salgspris}


def fordelingskalkulation(variabel_enhed: float, faste: float, kapacitet: float,
                          udnyttelse: float, dg: float) -> dict:
    """Egenpris = variabel enhedsomk. + andel af kapacitetsomk.; +DB → salgspris."""
    andel = faste / (kapacitet * udnyttelse) if (kapacitet and udnyttelse) else float("nan")
    egenpris = variabel_enhed + andel
    db = egenpris * dg / (1 - dg) if dg < 1 else float("nan")
    return {"andel_kapacitetsomk": andel, "egenpris": egenpris, "db": db,
            "salgspris": egenpris + db}


def retrograd_kalkulation(salgspris: float, dg: float, variable_salgsomk: float,
                          told_pct: float) -> dict:
    """Baglæns fra markedspris til maks. købspris.

    salgspris − DB − variable salgsomk. − told(% af købspris) = købspris.
    Løst: købspris = (salgspris·(1−DG) − variable_salgsomk) / (1 + told_pct).
    """
    db = salgspris * dg
    maks_koeb = (salgspris * (1 - dg) - variable_salgsomk) / (1 + told_pct)
    return {"db": db, "told": maks_koeb * told_pct, "maks_koebspris": maks_koeb}


# ---------------------------------------------------------------------------
# Prisoptimering under monopol
# ---------------------------------------------------------------------------

def prisoptimering(priser: list[float], afsaetning: list[float],
                   variabel_enhed: float, faste: float) -> dict:
    """Total- og grænsemetode ud fra en pris/afsætnings-tabel.

    Returnerer kolonner + optimum (max overskud) og grænse-tabel.
    """
    p = np.asarray(priser, dtype=float)
    q = np.asarray(afsaetning, dtype=float)
    omsaetning = p * q
    vo = variabel_enhed * q
    db = omsaetning - vo
    to = vo + faste
    overskud = omsaetning - to
    idx = int(np.argmax(overskud))
    # grænseomsætning og grænseomkostning (Δ pr. ekstra enhed mellem rækker)
    g_oms = np.full_like(omsaetning, np.nan)
    g_omk = np.full_like(omsaetning, np.nan)
    for i in range(1, len(q)):
        dq = q[i] - q[i - 1]
        if dq != 0:
            g_oms[i] = (omsaetning[i] - omsaetning[i - 1]) / dq
            g_omk[i] = (to[i] - to[i - 1]) / dq
    return {
        "omsaetning": omsaetning, "vo": vo, "db": db, "to": to, "overskud": overskud,
        "graenseomsaetning": g_oms, "graenseomkostning": g_omk,
        "optimum_idx": idx, "optimal_pris": float(p[idx]),
        "optimal_afsaetning": float(q[idx]), "max_overskud": float(overskud[idx]),
    }


# ---------------------------------------------------------------------------
# Regnskabsanalyse / nøgletal
# ---------------------------------------------------------------------------

def lineaer_afskrivning(nypris: float, scrapvaerdi: float, levetid_aar: float) -> dict:
    """Lineær afskrivning = (nypris − scrapværdi) / levetid."""
    aarlig = (nypris - scrapvaerdi) / levetid_aar if levetid_aar else float("nan")
    return {"aarlig": aarlig, "kvartal": aarlig / 4, "maaned": aarlig / 12}


def noegletal(omsaetning: float, ebit: float, aarets_resultat: float,
              renteomk: float, aktiver: float, egenkapital: float,
              gaeld: float, omsaetningsaktiver: float, kortfristet_gaeld: float,
              bruttofortjeneste: float | None = None) -> dict:
    """Centrale nøgletal fra resultatopgørelse + balance (andele 0-1)."""
    def safe(a, b):
        return a / b if b else float("nan")
    overskudsgrad = safe(ebit, omsaetning)
    aoh = safe(omsaetning, aktiver)
    return {
        "afkastningsgrad": safe(ebit, aktiver),
        "overskudsgrad": overskudsgrad,
        "aoh": aoh,                                    # afkastningsgrad = overskudsgrad·AOH
        "egenkapitalforrentning": safe(aarets_resultat, egenkapital),
        "fremmedkapitalforrentning": safe(renteomk, gaeld),
        "soliditetsgrad": safe(egenkapital, aktiver),
        "likviditetsgrad": safe(omsaetningsaktiver, kortfristet_gaeld),
        "gearing": safe(gaeld, egenkapital),
        "bruttoavanceprocent": safe(bruttofortjeneste, omsaetning) if bruttofortjeneste is not None else float("nan"),
    }
