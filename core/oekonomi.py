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

def _aar(cashflows: list[float], years: list[float] | None) -> list[float]:
    """Årstal pr. cashflow. Uden years antages på hinanden følgende år fra 0."""
    if years is None:
        return [float(t) for t in range(len(cashflows))]
    return [float(t) for t in years]


def npv(rate: float, cashflows: list[float], years: list[float] | None = None) -> float:
    """Kapitalværdi. cashflows[0] = år 0 (typisk −startinvestering).

    years: valgfri liste med årstal pr. cashflow (samme længde), så huller i
    årrækken diskonteres korrekt — fx years=[0, 1, 5]. Udelades den, antages
    rækkefølgen at være år 0, 1, 2, ...
    """
    return float(sum(cf / (1 + rate) ** t
                     for t, cf in zip(_aar(cashflows, years), cashflows)))


def irr(cashflows: list[float], years: list[float] | None = None) -> float:
    """Intern rente: renten hvor NPV = 0 (første fortegnsskift fundet)."""
    f = lambda r: npv(r, cashflows, years)
    rates = np.linspace(-0.99, 10.0, 4000)
    vals = [f(r) for r in rates]
    for i in range(len(rates) - 1):
        if vals[i] == 0:
            return float(rates[i])
        if vals[i] * vals[i + 1] < 0:
            return float(brentq(f, rates[i], rates[i + 1]))
    return float("nan")


def payback(cashflows: list[float], years: list[float] | None = None) -> float:
    """Tilbagebetalingstid (år, med interpolation). cashflows[0] = år 0.

    Ved huller i årrækken interpoleres hen over spændet mellem to år.
    """
    ys = _aar(cashflows, years)
    cum = cashflows[0]
    for i in range(1, len(cashflows)):
        if cum + cashflows[i] >= 0:
            span = ys[i] - ys[i - 1]
            return float(ys[i - 1] + span * (-cum) / cashflows[i]) if cashflows[i] else float(ys[i])
        cum += cashflows[i]
    return float("nan")


def kritisk_levetid(cashflows: list[float], rate: float,
                    years: list[float] | None = None) -> float:
    """Mindste levetid (år) før investeringen er tjent hjem (NPV = 0)."""
    ys = _aar(cashflows, years)
    investering = -cashflows[0]
    disc_cum = 0.0
    for i in range(1, len(cashflows)):
        d = cashflows[i] / (1 + rate) ** ys[i]
        if disc_cum + d >= investering:
            span = ys[i] - ys[i - 1]
            return float(ys[i - 1] + span * (investering - disc_cum) / d) if d else float(ys[i])
        disc_cum += d
    return float("nan")


def npv_profile(cashflows: list[float], rates: np.ndarray,
                years: list[float] | None = None) -> np.ndarray:
    """NPV ved hver rente (til NPV-profilen der krydser nul ved IRR)."""
    return np.array([npv(r, cashflows, years) for r in rates])


def investering_summary(cashflows: list[float], rate: float,
                        years: list[float] | None = None) -> dict:
    return {
        "NPV": npv(rate, cashflows, years),
        "IRR": irr(cashflows, years),
        "payback": payback(cashflows, years),
        "kritisk_levetid": kritisk_levetid(cashflows, rate, years),
    }


# --- Kritiske værdier i investeringskalkulen -------------------------------

def kritisk_investeringsbeloeb(cashflows: list[float], rate: float,
                               years: list[float] | None = None) -> float:
    """Det mest investeringen må koste, før NPV rammer 0.

    = nutidsværdien af alle fremtidige indbetalinger = investering + NPV.
    (Fyns Spm 8: Maskine II → 797.627 kr.)
    """
    return -cashflows[0] + npv(rate, cashflows, years)


def kritisk_indkoebspris(cashflows: list[float], rate: float,
                         years: list[float] | None = None) -> float:
    """Kritisk værdi for indkøbsprisen på selve aktivet (DSS Spm 6, svejserobot).

    Samme mekanik som kritisk investeringsbeløb: den maksimale pris aktivet
    må koste, før kapitalværdien bliver negativ.
    """
    return kritisk_investeringsbeloeb(cashflows, rate, years)


def kritisk_aarlig_indbetaling(investering: float, rate: float, levetid_aar: float,
                               scrapvaerdi: float = 0.0) -> float:
    """Mindste gennemsnitlige årlige indbetaling (annuitet) der giver NPV = 0.

    Scrapværdien (modtages i sidste år) trækkes fra som nutidsværdi, før der
    deles med annuitetsfaktoren. (Fyns Spm 8: Maskine II → 177.615 kr./år.)
    """
    if levetid_aar <= 0:
        return float("nan")
    pv_scrap = scrapvaerdi / (1 + rate) ** levetid_aar
    faktor = (1 - (1 + rate) ** -levetid_aar) / rate if rate else float(levetid_aar)
    return (investering - pv_scrap) / faktor if faktor else float("nan")


def kritisk_omsaetning(cashflows: list[float], rate: float, salgspris_pr_stk: float,
                       db_pr_stk: float, years: list[float] | None = None) -> dict:
    """Kritisk omsætning i år 1: hvor lavt salget i år 1 kan falde, før NPV = 0.

    Kun år 1 varieres: kritisk indbetaling år 1 = cashflow år 1 − NPV·(1+r)^t1.
    Derfra: kritisk stk = indbetaling/DB pr. stk; kritisk omsætning = stk·pris.
    (Fyns Spm 7: Maskine I → ca. 369.000 kr. = 924 stk.)
    """
    ys = _aar(cashflows, years)
    if len(cashflows) < 2:
        return {"kritisk_indbetaling": float("nan"), "kritisk_stk": float("nan"),
                "kritisk_omsaetning": float("nan")}
    n = npv(rate, cashflows, years)
    krit_ind = cashflows[1] - n * (1 + rate) ** ys[1]
    krit_stk = krit_ind / db_pr_stk if db_pr_stk else float("nan")
    return {
        "kritisk_indbetaling": float(krit_ind),
        "kritisk_stk": float(krit_stk),
        "kritisk_omsaetning": float(krit_stk * salgspris_pr_stk) if krit_stk == krit_stk else float("nan"),
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
                          udnyttelse: float, fortjeneste: float) -> dict:
    """Egenpris = variabel enhedsomk. + andel af kapacitetsomk.; +avance → salgspris.

    fortjeneste er avancen som andel af salgsprisen (0-1). OBS: det er IKKE
    dækningsgraden — egenprisen indeholder allerede en andel af de faste
    omkostninger, så den faktiske DG (= (salgspris − variable)/salgspris)
    bliver højere end fortjenesteprocenten. Returneres som 'faktisk_dg'.
    """
    andel = faste / (kapacitet * udnyttelse) if (kapacitet and udnyttelse) else float("nan")
    egenpris = variabel_enhed + andel
    avance = egenpris * fortjeneste / (1 - fortjeneste) if fortjeneste < 1 else float("nan")
    salgspris = egenpris + avance
    faktisk_dg = (salgspris - variabel_enhed) / salgspris if salgspris else float("nan")
    return {"andel_kapacitetsomk": andel, "egenpris": egenpris, "avance": avance,
            "salgspris": salgspris, "faktisk_dg": faktisk_dg}


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


def indekstal(vaerdier: list[float]) -> list[float]:
    """Indekstal med første værdi som basis (= 100). NaN hvis basis er 0/NaN."""
    if not vaerdier:
        return []
    basis = float(vaerdier[0])
    if basis != basis or basis == 0:
        return [float("nan")] * len(vaerdier)
    return [float(v) / basis * 100 for v in vaerdier]


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
        # Gearing-identiteten: EKF før skat = AG + (AG − FKF)·gæld/EK
        "ekf_foer_skat": safe(ebit - renteomk, egenkapital),
        "soliditetsgrad": safe(egenkapital, aktiver),
        "likviditetsgrad": safe(omsaetningsaktiver, kortfristet_gaeld),
        "gearing": safe(gaeld, egenkapital),
        "bruttoavanceprocent": safe(bruttofortjeneste, omsaetning) if bruttofortjeneste is not None else float("nan"),
    }
