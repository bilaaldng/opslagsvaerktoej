"""Ren matematik for Statistik-modulet.

Ingen Streamlit-kald herinde. scipy.stats leverer de rigtige tal (korrekthed!).
Notation matcher brugerens danish-statistik-skill + VIDEN §8:

    Kontrolkort:  UCL/LCL = ±3σ.  p-kort, X̄-kort, R-kort.
    Konfidensinterval:  gns ± t·s/√n (middelværdi) · p̂ ± z·√(p̂(1−p̂)/n) (andel)
    Binomialfordeling:  P(X=k) = C(n,k)·p^k·(1−p)^(n−k); normaltilnærmelse ved stor n
"""

from __future__ import annotations

import math
import numpy as np
from scipy import stats


# ---------------------------------------------------------------------------
# Normalfordeling
# ---------------------------------------------------------------------------

def normal_pdf(x, mu=0.0, sigma=1.0):
    return stats.norm.pdf(x, mu, sigma)


def normal_cdf(x, mu=0.0, sigma=1.0) -> float:
    return float(stats.norm.cdf(x, mu, sigma))


def z_score(x: float, mu: float, sigma: float) -> float:
    return (x - mu) / sigma if sigma else float("nan")


def normal_area(lower, upper, mu=0.0, sigma=1.0) -> float:
    """Areal (sandsynlighed) mellem to grænser under normalfordelingen."""
    lo = -np.inf if lower is None else lower
    hi = np.inf if upper is None else upper
    return float(stats.norm.cdf(hi, mu, sigma) - stats.norm.cdf(lo, mu, sigma))


def prob_to_z(p: float) -> float:
    """Sandsynlighed (venstre haleareal) til z-værdi."""
    return float(stats.norm.ppf(min(max(p, 1e-9), 1 - 1e-9)))


# ---------------------------------------------------------------------------
# Konfidensinterval
# ---------------------------------------------------------------------------

def ci_mean(mean: float, s: float, n: int, conf: float = 0.95) -> dict:
    """KI for middelværdi: gns ± t(α/2, n−1)·s/√n (t-fordeling)."""
    alpha = 1 - conf
    t = float(stats.t.ppf(1 - alpha / 2, n - 1))
    me = t * s / math.sqrt(n)
    return {"t": t, "margin": me, "nedre": mean - me, "oevre": mean + me,
            "std_error": s / math.sqrt(n)}


def ci_proportion(phat: float, n: int, conf: float = 0.95) -> dict:
    """KI for andel: p̂ ± z·√(p̂(1−p̂)/n)."""
    alpha = 1 - conf
    z = float(stats.norm.ppf(1 - alpha / 2))
    se = math.sqrt(phat * (1 - phat) / n)
    me = z * se
    return {"z": z, "margin": me, "nedre": max(phat - me, 0.0),
            "oevre": min(phat + me, 1.0), "std_error": se}


# ---------------------------------------------------------------------------
# Binomialfordeling
# ---------------------------------------------------------------------------

def binom_pmf(k: int, n: int, p: float) -> float:
    """P(X = k)."""
    return float(stats.binom.pmf(k, n, p))


def binom_cdf(k: int, n: int, p: float) -> float:
    """P(X ≤ k)."""
    return float(stats.binom.cdf(k, n, p))


def binom_summary(n: int, p: float, k: int) -> dict:
    """Nøgletal for binomialfordeling ved et valgt k."""
    return {
        "P_lig": binom_pmf(k, n, p),
        "P_hoejst": binom_cdf(k, n, p),                       # P(X ≤ k)
        "P_mindst": 1 - binom_cdf(k - 1, n, p) if k >= 1 else 1.0,   # P(X ≥ k)
        "P_flere_end": 1 - binom_cdf(k, n, p),               # P(X > k)
        "middel": n * p,
        "sigma": math.sqrt(n * p * (1 - p)),
    }


def binom_normal_approx(n: int, p: float) -> dict:
    """Normaltilnærmelse: µ = n·p, σ = √(n·p·(1−p)). Gyldig når np og n(1−p) ≥ 5."""
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    return {"mu": mu, "sigma": sigma, "gyldig": (n * p >= 5 and n * (1 - p) >= 5)}


# ---------------------------------------------------------------------------
# Kontrolkort (SPC)
# ---------------------------------------------------------------------------

# Tabelkonstanter for X̄- og R-kort (efter stikprøvestørrelse n)
SPC_CONST = {
    2: (1.880, 0.000, 3.267),
    3: (1.023, 0.000, 2.574),
    4: (0.729, 0.000, 2.282),
    5: (0.577, 0.000, 2.114),
    6: (0.483, 0.000, 2.004),
    7: (0.419, 0.076, 1.924),
    8: (0.373, 0.136, 1.864),
    9: (0.337, 0.184, 1.816),
    10: (0.308, 0.223, 1.777),
}


def p_chart(defects: list[float], sizes: list[float]) -> dict:
    """p-kort (andel defekte).

    p̄ = Σfejl/Σn. σ_p = √(p̄(1−p̄)/n) (kan variere pr. punkt). UCL/LCL = p̄ ± 3σ_p.
    """
    defects = np.asarray(defects, dtype=float)
    sizes = np.asarray(sizes, dtype=float)
    pbar = defects.sum() / sizes.sum() if sizes.sum() else float("nan")
    props = defects / sizes
    sigma = np.sqrt(pbar * (1 - pbar) / sizes)
    ucl = pbar + 3 * sigma
    lcl = np.maximum(pbar - 3 * sigma, 0)
    ooc = (props > ucl) | (props < lcl)
    return {"andele": props, "pbar": pbar, "UCL": ucl, "LCL": lcl,
            "ude_af_kontrol": ooc}


def linear_regression(x, y) -> dict:
    """Lineær regression (mindste kvadraters metode) via scipy.

    Returnerer hældning (b), skæring (a), korrelation r og forklaringsgrad R².
    Linjen er y = a + b·x.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    res = stats.linregress(x, y)
    return {
        "haeldning": float(res.slope),
        "skaering": float(res.intercept),
        "r": float(res.rvalue),
        "r2": float(res.rvalue ** 2),
        "p": float(res.pvalue),
        "std_err": float(res.stderr),
    }


def regression_predict(xval: float, haeldning: float, skaering: float) -> float:
    """Forudsig y for en given x ud fra linjen y = a + b·x."""
    return skaering + haeldning * xval


def xbar_r_chart(samples: list[list[float]]) -> dict:
    """X̄- og R-kort ud fra ligestore stikprøver.

    samples: liste af stikprøver (hver en liste af målinger).
    X̿ = gns. af stikprøvegennemsnit. R̄ = gns. af ranges. A₂/D₃/D₄ fra tabel.
    """
    means = [float(np.mean(s)) for s in samples]
    ranges = [float(max(s) - min(s)) for s in samples]
    n = len(samples[0]) if samples else 0
    xbarbar = float(np.mean(means)) if means else float("nan")
    rbar = float(np.mean(ranges)) if ranges else float("nan")
    A2, D3, D4 = SPC_CONST.get(n, (float("nan"),) * 3)
    x_ucl = xbarbar + A2 * rbar
    x_lcl = xbarbar - A2 * rbar
    r_ucl = D4 * rbar
    r_lcl = D3 * rbar
    return {
        "means": means, "ranges": ranges, "n": n,
        "Xbarbar": xbarbar, "Rbar": rbar, "A2": A2, "D3": D3, "D4": D4,
        "X_UCL": x_ucl, "X_LCL": x_lcl, "R_UCL": r_ucl, "R_LCL": r_lcl,
        "X_ooc": [m > x_ucl or m < x_lcl for m in means],
        "R_ooc": [r > r_ucl or r < r_lcl for r in ranges],
    }
