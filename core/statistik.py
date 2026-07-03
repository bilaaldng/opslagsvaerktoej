"""Ren matematik for Statistik-modulet.

Ingen Streamlit-kald herinde. scipy.stats leverer de rigtige tal (korrekthed!).
Notation matcher brugerens danish-statistik-skill + VIDEN §8:

    Kontrolkort:  UCL/LCL = ±3σ.  p-kort, X̄-kort, R-kort.
    Konfidensinterval:  gns ± t·s/√n (middelværdi) · p̂ ± z·√(p̂(1−p̂)/n) (andel)
    Binomialfordeling:  P(X=k) = C(n,k)·p^k·(1−p)^(n−k); normaltilnærmelse ved stor n
"""

from __future__ import annotations

import math
import re

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
# Rå data: parsning og beskrivende statistik
# ---------------------------------------------------------------------------

def parse_maalinger(text: str) -> dict:
    """Parser rå målinger fra fritekst.

    Accepterer tal adskilt af mellemrum, linjeskift eller semikolon.
    Dansk decimalkomma (11,69) OG punktum (11.69) accepteres. Indeholder et
    tal både punktum og komma (1.234,5), tolkes punktum som tusindtalsseparator.
    Returnerer {'vaerdier': [...], 'ignoreret': [tokens der ikke var tal]}.
    """
    vaerdier: list[float] = []
    ignoreret: list[str] = []
    for token in re.split(r"[\s;]+", text or ""):
        t = token.strip().strip(",.;:")
        if not t:
            continue
        if "." in t and "," in t:
            t = t.replace(".", "").replace(",", ".")   # 1.234,5 -> 1234.5
        else:
            t = t.replace(",", ".")                    # 11,69 -> 11.69
        try:
            vaerdier.append(float(t))
        except ValueError:
            ignoreret.append(token.strip())
    return {"vaerdier": vaerdier, "ignoreret": ignoreret}


def beskrivende(vaerdier) -> dict:
    """Beskrivende statistik + 68-95-99,7-tjek for en liste af målinger.

    andel_1s/2s/3s = andelen af målinger inden for gns ± 1/2/3 standardafvigelser.
    I en normalfordeling er facit ca. 68 % / 95 % / 99,7 %.
    """
    a = np.asarray(vaerdier, dtype=float)
    n = a.size
    if n < 2:
        return {"n": int(n), "gennemsnit": float(a.mean()) if n else float("nan"),
                "s": float("nan"), "median": float(np.median(a)) if n else float("nan"),
                "min": float(a.min()) if n else float("nan"),
                "maks": float(a.max()) if n else float("nan"),
                "skaevhed": float("nan"),
                "andel_1s": float("nan"), "andel_2s": float("nan"), "andel_3s": float("nan")}
    gns = float(a.mean())
    s = float(a.std(ddof=1))
    def _andel(k):
        if not s:
            return float("nan")
        return float(np.mean(np.abs(a - gns) <= k * s))
    return {
        "n": int(n), "gennemsnit": gns, "s": s,
        "median": float(np.median(a)), "min": float(a.min()), "maks": float(a.max()),
        "skaevhed": float(stats.skew(a)),
        "andel_1s": _andel(1), "andel_2s": _andel(2), "andel_3s": _andel(3),
    }


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


def ci_mean_z(mean: float, sigma: float, n: int, conf: float = 0.95) -> dict:
    """KI for middelværdi ved KENDT σ: gns ± z(α/2)·σ/√n (normalfordeling)."""
    alpha = 1 - conf
    z = float(stats.norm.ppf(1 - alpha / 2))
    se = sigma / math.sqrt(n)
    me = z * se
    return {"z": z, "margin": me, "nedre": mean - me, "oevre": mean + me,
            "std_error": se}


def ci_proportion(phat: float, n: int, conf: float = 0.95) -> dict:
    """KI for andel: p̂ ± z·√(p̂(1−p̂)/n)."""
    alpha = 1 - conf
    z = float(stats.norm.ppf(1 - alpha / 2))
    se = math.sqrt(phat * (1 - phat) / n)
    me = z * se
    return {"z": z, "margin": me, "nedre": max(phat - me, 0.0),
            "oevre": min(phat + me, 1.0), "std_error": se}


def sample_size_mean(sigma: float, me: float, conf: float = 0.95) -> dict:
    """Stikprøvestørrelse for middelværdi: n = (z·σ/ME)², rundet OP."""
    alpha = 1 - conf
    z = float(stats.norm.ppf(1 - alpha / 2))
    n_raa = (z * sigma / me) ** 2 if me else float("inf")
    return {"z": z, "n_raa": n_raa,
            "n": int(math.ceil(n_raa)) if math.isfinite(n_raa) else 0}


def sample_size_proportion(p: float, me: float, conf: float = 0.95) -> dict:
    """Stikprøvestørrelse for andel: n = z²·p(1−p)/ME², rundet OP.

    p = forventet andel; p = 0,5 er 'worst case' (giver størst n).
    """
    alpha = 1 - conf
    z = float(stats.norm.ppf(1 - alpha / 2))
    n_raa = z ** 2 * p * (1 - p) / me ** 2 if me else float("inf")
    return {"z": z, "n_raa": n_raa,
            "n": int(math.ceil(n_raa)) if math.isfinite(n_raa) else 0}


# ---------------------------------------------------------------------------
# Hypotesetest
# ---------------------------------------------------------------------------
# sided: 'tosidet' (μ ≠ μ0) · 'hoejre' (μ > μ0) · 'venstre' (μ < μ0)

def _hale(teststoerrelse: float, sided: str, cdf, ppf, alpha: float) -> tuple:
    """Fælles hale-logik: (p-værdi, kritisk værdi) for valgt hale."""
    if sided == "hoejre":
        return 1 - cdf(teststoerrelse), float(ppf(1 - alpha))
    if sided == "venstre":
        return cdf(teststoerrelse), float(-ppf(1 - alpha))
    return 2 * (1 - cdf(abs(teststoerrelse))), float(ppf(1 - alpha / 2))


def z_test_mean(mean: float, sigma: float, n: int, mu0: float,
                sided: str = "tosidet", alpha: float = 0.05) -> dict:
    """Én-stikprøve z-test for middelværdi (KENDT σ eller stor stikprøve).

    z = (x̄ − μ0) / (σ/√n). Verifikations-facit: x̄=76,97, μ0=75, σ=9,16, n=100
    → z=2,15, p=0,016 < 0,05 → gennemsnittet er signifikant over 75.
    """
    se = sigma / math.sqrt(n)
    z = (mean - mu0) / se if se else float("nan")
    p, kritisk = _hale(z, sided, lambda v: float(stats.norm.cdf(v)),
                       stats.norm.ppf, alpha)
    return {"z": z, "se": se, "kritisk": kritisk, "p": float(p),
            "forkast": bool(p < alpha), "alpha": alpha}


def t_test_mean(mean: float, s: float, n: int, mu0: float,
                sided: str = "tosidet", alpha: float = 0.05) -> dict:
    """Én-stikprøve t-test for middelværdi (σ UKENDT, s fra stikprøven).

    t = (x̄ − μ0) / (s/√n) med df = n − 1 frihedsgrader.
    """
    df = n - 1
    se = s / math.sqrt(n)
    t = (mean - mu0) / se if se else float("nan")
    p, kritisk = _hale(t, sided, lambda v: float(stats.t.cdf(v, df)),
                       lambda q: stats.t.ppf(q, df), alpha)
    return {"t": t, "df": df, "se": se, "kritisk": kritisk, "p": float(p),
            "forkast": bool(p < alpha), "alpha": alpha}


def z_test_two_means(mean1: float, sigma1: float, n1: int,
                     mean2: float, sigma2: float, n2: int,
                     sided: str = "tosidet", alpha: float = 0.05) -> dict:
    """To-stikprøve z-test: H0: μ1 = μ2 (kendte σ'er eller store stikprøver).

    z = (x̄1 − x̄2) / √(σ1²/n1 + σ2²/n2). Verifikations-facit: 70,28 vs 76,97.
    """
    se = math.sqrt(sigma1 ** 2 / n1 + sigma2 ** 2 / n2)
    z = (mean1 - mean2) / se if se else float("nan")
    p, kritisk = _hale(z, sided, lambda v: float(stats.norm.cdf(v)),
                       stats.norm.ppf, alpha)
    return {"z": z, "se": se, "kritisk": kritisk, "p": float(p),
            "forkast": bool(p < alpha), "alpha": alpha,
            "forskel": mean1 - mean2}


def t_test_two_means(mean1: float, s1: float, n1: int,
                     mean2: float, s2: float, n2: int,
                     sided: str = "tosidet", alpha: float = 0.05) -> dict:
    """To-stikprøve t-test (Welch, ulige varianser): H0: μ1 = μ2.

    t = (x̄1 − x̄2) / √(s1²/n1 + s2²/n2); df efter Welch-formlen.
    """
    v1, v2 = s1 ** 2 / n1, s2 ** 2 / n2
    se = math.sqrt(v1 + v2)
    t = (mean1 - mean2) / se if se else float("nan")
    df = (v1 + v2) ** 2 / (v1 ** 2 / (n1 - 1) + v2 ** 2 / (n2 - 1)) if (v1 + v2) else float("nan")
    p, kritisk = _hale(t, sided, lambda v: float(stats.t.cdf(v, df)),
                       lambda q: stats.t.ppf(q, df), alpha)
    return {"t": t, "df": float(df), "se": se, "kritisk": kritisk, "p": float(p),
            "forkast": bool(p < alpha), "alpha": alpha,
            "forskel": mean1 - mean2}


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


def binom_pmf_array(n: int, p: float):
    """Hele pmf'en P(X=0..n) i ét vektoriseret kald (hurtigt ved stort n)."""
    return stats.binom.pmf(np.arange(0, n + 1), n, p)


def binom_between(a: int, b: int, n: int, p: float) -> float:
    """P(a ≤ X ≤ b) = P(X ≤ b) − P(X ≤ a−1)."""
    if b < a:
        return 0.0
    lavere = binom_cdf(a - 1, n, p) if a >= 1 else 0.0
    return binom_cdf(b, n, p) - lavere


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
