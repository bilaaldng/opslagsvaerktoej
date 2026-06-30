"""Ren matematik for Indkøb-modulet.

Ingen Streamlit-kald herinde — kun rene, testbare funktioner.
Notation matcher brugerens eget materiale (Nordic Components, Fyns Beklædning):

    EOQ   = sqrt(2*D*S / H)              H = enhedspris * lagerrente
    POQ   = sqrt(2*D*S / (H*(1-d/p)))    EPQ med produktionskorrektion
    SS    = z * sigma * sqrt(L)          sikkerhedslager
    ROP   = d*L + SS                     genbestillingspunkt
    ABC   : årsværdi = forbrug*pris, sortér faldende, A<=80%, B<=95%, C>95%
"""

from __future__ import annotations

import math
import numpy as np
import pandas as pd
from scipy import stats


# ---------------------------------------------------------------------------
# EOQ — Economic Order Quantity
# ---------------------------------------------------------------------------

def holding_cost_per_unit(price: float, rate: float) -> float:
    """Lageromkostning pr. enhed pr. år: H = enhedspris * lagerrente."""
    return price * rate


def eoq(D: float, S: float, H: float) -> float:
    """Optimal ordrestørrelse: EOQ = sqrt(2*D*S / H)."""
    if H <= 0 or D <= 0 or S <= 0:
        return float("nan")
    return math.sqrt((2 * D * S) / H)


def order_cost(D: float, S: float, Q: float) -> float:
    """Årlig bestillingsomkostning: (D/Q) * S."""
    return (D / Q) * S if Q > 0 else float("nan")


def holding_cost(H: float, Q: float) -> float:
    """Årlig lageromkostning: (Q/2) * H (gennemsnitslager = Q/2)."""
    return (Q / 2) * H


def total_inventory_cost(D: float, S: float, H: float, Q: float) -> float:
    """Samlet relevant årlig omkostning ved ordrestørrelse Q (ekskl. varekøb)."""
    return order_cost(D, S, Q) + holding_cost(H, Q)


def eoq_summary(D: float, S: float, H: float, Q: float | None = None) -> dict:
    """Komplet EOQ-resultat. Hvis Q ikke angives, bruges EOQ selv.

    Returnerer alle mellemregninger, så de kan vises ved siden af svaret.
    """
    q_star = eoq(D, S, H)
    Q = q_star if Q is None else Q
    oc = order_cost(D, S, Q)
    hc = holding_cost(H, Q)
    return {
        "EOQ": q_star,
        "Q": Q,
        "ordreomkostning": oc,
        "lageromkostning": hc,
        "total": oc + hc,
        "antal_ordrer": D / Q if Q > 0 else float("nan"),
        "cyklustid_dage": 365 * Q / D if D > 0 else float("nan"),
        "gns_lager": Q / 2,
    }


def eoq_curve(D: float, S: float, H: float, q_values: np.ndarray) -> dict:
    """Arrays til totalomkostningskurven (U-form) over et interval af Q."""
    q = np.asarray(q_values, dtype=float)
    q = q[q > 0]
    return {
        "Q": q,
        "ordreomkostning": (D / q) * S,
        "lageromkostning": (q / 2) * H,
        "total": (D / q) * S + (q / 2) * H,
    }


def current_policy_cost(D: float, S: float, H: float, Q_current: float) -> float:
    """Total omkostning ved nuværende ordrestørrelse (til besparelsesberegning)."""
    return total_inventory_cost(D, S, H, Q_current)


# ---------------------------------------------------------------------------
# POQ / EPQ — Production Order Quantity (produktionsseriestørrelse)
# ---------------------------------------------------------------------------

def epq(D: float, S: float, H: float, d: float, p: float) -> float:
    """Optimal produktionsseriestørrelse (EPQ/POQ).

    POQ = sqrt(2*D*S / (H * (1 - d/p)))
    d = daglig efterspørgsel, p = daglig produktionskapacitet (p > d).
    """
    if p <= d:
        return float("nan")
    factor = 1 - d / p
    if H <= 0 or factor <= 0:
        return float("nan")
    return math.sqrt((2 * D * S) / (H * factor))


def epq_summary(D: float, S: float, H: float, d: float, p: float,
                Q_current: float | None = None) -> dict:
    """Komplet POQ/EPQ-resultat med mellemregninger."""
    q_star = epq(D, S, H, d, p)
    factor = 1 - d / p if p > 0 else float("nan")
    max_lager = q_star * factor
    setup = (D / q_star) * S
    hold = (max_lager / 2) * H
    res = {
        "POQ": q_star,
        "andel_til_lager": factor,            # (1 - d/p)
        "maks_lager": max_lager,
        "gns_lager": max_lager / 2,
        "igangsaetning": setup,
        "lageromkostning": hold,
        "total": setup + hold,
        "antal_serier": D / q_star if q_star > 0 else float("nan"),
        "seriedage": q_star / p if p > 0 else float("nan"),
    }
    if Q_current:
        cur_max = Q_current * factor
        cur_total = (D / Q_current) * S + (cur_max / 2) * H
        res["total_nuvaerende"] = cur_total
        res["besparelse"] = cur_total - res["total"]
    return res


def epq_curve(D: float, S: float, H: float, d: float, p: float,
              q_values: np.ndarray) -> dict:
    """Arrays til totalomkostningskurven for POQ/EPQ."""
    q = np.asarray(q_values, dtype=float)
    q = q[q > 0]
    factor = 1 - d / p
    return {
        "Q": q,
        "igangsaetning": (D / q) * S,
        "lageromkostning": (q * factor / 2) * H,
        "total": (D / q) * S + (q * factor / 2) * H,
    }


# ---------------------------------------------------------------------------
# ABC / Pareto-analyse
# ---------------------------------------------------------------------------

def abc_analysis(df: pd.DataFrame,
                 forbrug_col: str = "Årligt forbrug",
                 pris_col: str = "Enhedspris",
                 navn_col: str = "Betegnelse",
                 a_cut: float = 0.80,
                 b_cut: float = 0.95) -> pd.DataFrame:
    """ABC-klassifikation efter årsværdi (forbrug * pris).

    Sorterer faldende, beregner akkumuleret andel og tildeler kategori:
        A hvis akkum. % <= a_cut, B hvis <= b_cut, ellers C.
    """
    out = df.copy()
    out = out[pd.to_numeric(out[forbrug_col], errors="coerce").notna()]
    out[forbrug_col] = pd.to_numeric(out[forbrug_col], errors="coerce")
    out[pris_col] = pd.to_numeric(out[pris_col], errors="coerce")
    out = out.dropna(subset=[forbrug_col, pris_col])

    out["Årsværdi"] = out[forbrug_col] * out[pris_col]
    out = out.sort_values("Årsværdi", ascending=False).reset_index(drop=True)

    total = out["Årsværdi"].sum()
    out["Akkumuleret værdi"] = out["Årsværdi"].cumsum()
    out["Akkumuleret %"] = out["Akkumuleret værdi"] / total if total else 0.0

    def klass(p: float) -> str:
        if p <= a_cut:
            return "A"
        if p <= b_cut:
            return "B"
        return "C"

    out["Kategori"] = out["Akkumuleret %"].apply(klass)
    out["Andel %"] = out["Årsværdi"] / total if total else 0.0
    return out


def abc_summary(df_classified: pd.DataFrame) -> pd.DataFrame:
    """Opsummering pr. kategori: antal varer, andel af varer, andel af værdi."""
    n_total = len(df_classified)
    val_total = df_classified["Årsværdi"].sum()
    rows = []
    for kat in ["A", "B", "C"]:
        sub = df_classified[df_classified["Kategori"] == kat]
        rows.append({
            "Kategori": kat,
            "Antal varer": len(sub),
            "Andel af varer %": len(sub) / n_total if n_total else 0.0,
            "Værdi (kr.)": sub["Årsværdi"].sum(),
            "Andel af værdi %": sub["Årsværdi"].sum() / val_total if val_total else 0.0,
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Genbestillingspunkt (ROP) + sikkerhedslager (SS)
# ---------------------------------------------------------------------------

# Brugerens faste z-tabel (matcher afleveringer/undervisning)
Z_TABLE = {0.90: 1.28, 0.95: 1.65, 0.99: 2.33}


def z_from_service(service: float) -> float:
    """Serviceniveau (fx 0.95) -> z-værdi via normalfordelingens invers (scipy)."""
    service = min(max(service, 1e-6), 1 - 1e-9)
    return float(stats.norm.ppf(service))


def safety_stock(z: float, sigma: float, L: float) -> float:
    """Sikkerhedslager: SS = z * sigma * sqrt(L).

    sigma = std.afvigelse pr. periode, L = ledetid i samme periode-enhed.
    """
    return z * sigma * math.sqrt(L)


def reorder_point(d: float, L: float, ss: float) -> float:
    """Genbestillingspunkt: ROP = d*L + SS (d = efterspørgsel pr. periode)."""
    return d * L + ss


def rop_summary(D: float, sigma: float, L: float, service: float,
                periods_per_year: float = 52) -> dict:
    """Komplet ROP/SS-resultat med mellemregninger (ugebaseret som standard)."""
    d = D / periods_per_year
    z = z_from_service(service)
    ss = safety_stock(z, sigma, L)
    rop = reorder_point(d, L, ss)
    return {
        "d": d,
        "z": z,
        "sikkerhedslager": ss,
        "forbrug_i_ledetid": d * L,
        "ROP": rop,
    }


# ---------------------------------------------------------------------------
# Make-vs-buy / TCA (Total Cost Analysis)
# ---------------------------------------------------------------------------

def total_cost_linear(fixed: float, var_per_unit: float, volume: float) -> float:
    """Lineær totalomkostning: fixed + var_per_unit * volume."""
    return fixed + var_per_unit * volume


def breakeven_volume(fixed_a: float, var_a: float,
                     fixed_b: float, var_b: float) -> float:
    """Volumen hvor to lineære omkostningslinjer krydser.

    (fixed_a - fixed_b) / (var_b - var_a). NaN hvis de er parallelle.
    """
    if var_a == var_b:
        return float("nan")
    return (fixed_a - fixed_b) / (var_b - var_a)


def tca_total(components: dict) -> float:
    """Sum af TCO-komponenter (kr./år)."""
    return float(sum(v for v in components.values() if v is not None))


# ---------------------------------------------------------------------------
# Leverandørevaluering — vægtet score
# ---------------------------------------------------------------------------

def weighted_score(scores: dict, weights: dict) -> float:
    """Samlet vægtet score: Σ(vægt · score). weights bør summe til 1."""
    return float(sum(scores.get(k, 0) * weights.get(k, 0) for k in weights))


def evaluate_suppliers(df_scores: pd.DataFrame, weights: dict,
                       navn_col: str = "Leverandør") -> pd.DataFrame:
    """Vægtet leverandørevaluering.

    df_scores: én række pr. leverandør, én kolonne pr. kriterium (score 1-5).
    weights: {kriterium: vægt}. Vægtene normaliseres så de summer til 1.
    Returnerer leverandører sorteret efter samlet score (faldende).
    """
    out = df_scores.copy()
    total_w = sum(weights.values())
    norm = {k: (v / total_w if total_w else 0) for k, v in weights.items()}
    crits = [k for k in norm if k in out.columns]
    out["Samlet score"] = out.apply(
        lambda r: sum(float(r[k]) * norm[k] for k in crits
                      if pd.notna(r[k])), axis=1)
    out = out.sort_values("Samlet score", ascending=False).reset_index(drop=True)
    return out


# ---------------------------------------------------------------------------
# Lagerstyringssystemer (review)
# ---------------------------------------------------------------------------

def periodic_max_level(d: float, P: float, L: float, ss: float) -> float:
    """Periodisk review: max-niveau R = d·(P+L) + SS.

    d = efterspørgsel pr. periode, P = review-interval, L = ledetid (samme enhed).
    Ved hvert tjek bestilles op til R: ordrestørrelse Q = R − I (nuværende beholdning).
    """
    return d * (P + L) + ss


def order_up_to(R_level: float, I: float) -> float:
    """Bestil op til max-niveau: Q = R − I (aldrig negativ)."""
    return max(R_level - I, 0.0)


# ---------------------------------------------------------------------------
# Forecasting — glidende gennemsnit + eksponentiel udglatning + fejlmål
# ---------------------------------------------------------------------------

def moving_average(actual, n: int):
    """Glidende gennemsnit. F[t] = gns. af de n foregående faktiske værdier.

    Returnerer liste med samme længde som actual (None hvor der ikke er nok
    historik) plus ét punkt mere = forecast for næste periode.
    """
    a = list(actual)
    fc = [None] * len(a)
    for t in range(n, len(a)):
        fc[t] = sum(a[t - n:t]) / n
    nxt = sum(a[-n:]) / n if len(a) >= n else None
    fc.append(nxt)
    return fc


def exp_smoothing(actual, alpha: float, f0=None):
    """Eksponentiel udglatning. F[t] = α·D[t-1] + (1-α)·F[t-1].

    Returnerer liste med len(actual)+1 forecasts (incl. næste periode).
    F[0] sættes til f0 eller actual[0].
    """
    a = list(actual)
    if not a:
        return []
    F = [f0 if f0 is not None else a[0]]
    for t in range(1, len(a) + 1):
        F.append(alpha * a[t - 1] + (1 - alpha) * F[t - 1])
    return F


def forecast_errors(actual, forecast) -> dict:
    """Fejlmål: MFE (bias), MAD, MAPE, tracking signal.

    FE = D − F. Beregnes kun hvor både faktisk og forecast findes.
    """
    pairs = [(d, f) for d, f in zip(actual, forecast)
             if d is not None and f is not None]
    if not pairs:
        return {"n": 0, "MFE": float("nan"), "MAD": float("nan"),
                "MAPE": float("nan"), "tracking_signal": float("nan")}
    fe = [d - f for d, f in pairs]
    abs_fe = [abs(e) for e in fe]
    ape = [abs(e) / d for (d, f), e in zip(pairs, fe) if d != 0]
    n = len(fe)
    mad = sum(abs_fe) / n
    return {
        "n": n,
        "MFE": sum(fe) / n,
        "MAD": mad,
        "MAPE": (sum(ape) / len(ape)) if ape else float("nan"),
        "tracking_signal": (sum(fe) / mad) if mad else float("nan"),
    }
