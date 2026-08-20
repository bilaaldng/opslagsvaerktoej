"""Ren matematik for Distribution-modulet (3. semester).

Ingen Streamlit-kald herinde. Notation matcher kursusmaterialet:

    Tyngdepunkt (gravity model, Chopra kap. 5, fase III):
        TC = Σ Dn · Fn · dn ,   dn = √((x−xn)² + (y−yn)²)
        Dn = mængde til/fra punkt n, Fn = fragtrate pr. enhed pr. afstand,
        dn = luftlinjeafstand fra anlægget (x, y) til punkt n.
        Startpunkt: vægtet gennemsnit af koordinaterne (tyngdepunktet).
        Optimum: iterativ forbedring (Weiszfeld) der minimerer TC.

    Kanban-kort (IOSM kap. 13, JIT/Lean):
        y = D · T · (1 + x) / C   — rundes ALTID op til nærmeste hele kort.
        D = efterspørgsel pr. tidsenhed, T = tid for at fylde og flytte én
        beholder, x = sikkerhedsfaktor (decimal), C = beholderstørrelse.

    Volumenvægt / fragtgrundlag (measureton):
        Fragtføreren betales for det, der fylder mest — vægt ELLER volumen.
        volumenvægt = m³ · omregningsfaktor
        fragtgrundlag = max(faktisk vægt, volumenvægt)
        Omregningsfaktoren afhænger af transportformen, fordi et fly har
        vægtproblemet og et skib pladsproblemet.
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Tyngdepunktsmetoden (gravity location model)
# ---------------------------------------------------------------------------

def _dist(x: float, y: float, px: float, py: float) -> float:
    return math.hypot(x - px, y - py)


def total_transportomkostning(x: float, y: float, punkter: list[dict]) -> float:
    """TC = Σ Dn·Fn·dn for et anlæg placeret i (x, y).

    punkter: liste af {"x": float, "y": float, "D": float, "F": float}.
    F (fragtrate) kan udelades — så vægtes kun med mængden D.
    """
    return sum(p["D"] * p.get("F", 1.0) * _dist(x, y, p["x"], p["y"])
               for p in punkter)


def tyngdepunkt(punkter: list[dict]) -> dict:
    """Vægtet gennemsnit af koordinaterne — gravity-modellens startpunkt.

    x* = Σ(D·F·x)/Σ(D·F),  y* = Σ(D·F·y)/Σ(D·F).
    """
    valid = [p for p in punkter if p.get("D", 0) > 0]
    if not valid:
        return {"fejl": "Mindst ét punkt skal have en mængde D > 0."}
    vaegt = sum(p["D"] * p.get("F", 1.0) for p in valid)
    x = sum(p["D"] * p.get("F", 1.0) * p["x"] for p in valid) / vaegt
    y = sum(p["D"] * p.get("F", 1.0) * p["y"] for p in valid) / vaegt
    return {"x": x, "y": y, "TC": total_transportomkostning(x, y, valid)}


def optimer_placering(punkter: list[dict], max_iter: int = 500,
                      tol: float = 1e-7) -> dict:
    """Find placeringen der minimerer TC (Weiszfelds iterative metode).

    Starter i tyngdepunktet og flytter sig skridt for skridt mod lavere
    samlet transportomkostning. Står anlægget præcis oven i et kundepunkt,
    er afstanden 0 og vægten ville dele med nul — punktet håndteres da som
    kandidatløsning i sig selv.
    """
    start = tyngdepunkt(punkter)
    if "fejl" in start:
        return start
    valid = [p for p in punkter if p.get("D", 0) > 0]
    x, y = start["x"], start["y"]
    for _ in range(max_iter):
        num_x = num_y = naevner = 0.0
        paa_punkt = None
        for p in valid:
            d = _dist(x, y, p["x"], p["y"])
            if d < 1e-12:
                paa_punkt = p
                continue
            w = p["D"] * p.get("F", 1.0) / d
            num_x += w * p["x"]
            num_y += w * p["y"]
            naevner += w
        if naevner == 0.0:          # står oven i det eneste punkt
            break
        nx, ny = num_x / naevner, num_y / naevner
        if paa_punkt is not None:
            # sammenlign med at blive stående på kundepunktet
            if (total_transportomkostning(x, y, valid)
                    <= total_transportomkostning(nx, ny, valid)):
                break
        if _dist(x, y, nx, ny) < tol:
            x, y = nx, ny
            break
        x, y = nx, ny
    return {"x": x, "y": y, "TC": total_transportomkostning(x, y, valid),
            "start_x": start["x"], "start_y": start["y"],
            "start_TC": start["TC"]}


# ---------------------------------------------------------------------------
# Kanban-kort (to-korts system, produktionskort)
# ---------------------------------------------------------------------------

def kanban_kort(D: float, T: float, x: float, C: float) -> dict:
    """y = D·T·(1+x)/C — antal kanban-kort/beholdere, rundet OP.

    D = efterspørgsel pr. tidsenhed (samme tidsenhed som T!),
    T = tid for at fylde og flytte én beholder, x = sikkerhedsfaktor
    som decimaltal (0,15 = 15 %), C = beholderstørrelse (stk.).
    Rundes op: rundes der ned, kan systemet ikke dække efterspørgslen.
    """
    if min(D, T, C) <= 0 or x < 0:
        return {"fejl": "D, T og C skal være positive; x må ikke være negativ."}
    y_raa = D * T * (1 + x) / C
    y = math.ceil(y_raa - 1e-9)     # 20,0000001 pga. flydende tal → stadig 20
    return {"y_raa": y_raa, "y": y, "maks_lager": y * C,
            "taeller": D * T * (1 + x)}


# ---------------------------------------------------------------------------
# Volumenvægt / fragtgrundlag (measureton)
# ---------------------------------------------------------------------------

# kg pr. m³ — hvad ét kubikmeter "vejer" i fragtberegningen. Tallene er
# branchens gængse omregningsfaktorer og adskiller sig, fordi transportformerne
# har hver deres knappe ressource: flyet mangler løfteevne, skibet mangler plads.
OMREGNING = {
    "Luftfragt": 167.0,      # 1 m³ ≈ 167 kg  (svarer til 1:6 000 cm³/kg)
    "Landevej": 333.0,       # 1 m³ ≈ 333 kg  (1:3)
    "Søfragt (LCL)": 1000.0,  # 1 m³ ≈ 1 000 kg — measureton, 1:1
    "Kurér/ekspres": 200.0,  # 1 m³ ≈ 200 kg  (1:5 000 cm³/kg)
}


def volumenvaegt(laengde_cm: float, bredde_cm: float, hoejde_cm: float,
                 faktisk_vaegt_kg: float, antal: int = 1,
                 faktor_kg_pr_m3: float = 167.0) -> dict:
    """Fragtgrundlaget = det største af faktisk vægt og volumenvægt.

    Mål angives i cm pr. kolli, vægt i kg pr. kolli. Faktoren er kg pr. m³
    og afhænger af transportformen (se OMREGNING).

    Returnerer også hvilken af de to der blev betalt for, og hvor meget den
    oversteg den anden — det er dér, pointen ligger: let og voluminøst gods
    betales efter pladsen, ikke efter vægten.
    """
    if min(laengde_cm, bredde_cm, hoejde_cm) <= 0:
        return {"fejl": "Længde, bredde og højde skal alle være positive."}
    if faktisk_vaegt_kg <= 0:
        return {"fejl": "Vægten skal være positiv."}
    if antal < 1:
        return {"fejl": "Antal kolli skal være mindst 1."}
    if faktor_kg_pr_m3 <= 0:
        return {"fejl": "Omregningsfaktoren skal være positiv."}

    m3_pr_kolli = (laengde_cm * bredde_cm * hoejde_cm) / 1_000_000
    m3 = m3_pr_kolli * antal
    vaegt = faktisk_vaegt_kg * antal
    vol_vaegt = m3 * faktor_kg_pr_m3
    grundlag = max(vaegt, vol_vaegt)
    return {
        "m3_pr_kolli": m3_pr_kolli,
        "m3": m3,
        "faktisk_vaegt": vaegt,
        "volumenvaegt": vol_vaegt,
        "fragtgrundlag": grundlag,
        "betales_efter": "volumen" if vol_vaegt > vaegt else "vægt",
        # hvor meget det betalte grundlag overstiger det andet mål
        "overskydende_kg": abs(vol_vaegt - vaegt),
        "densitet_kg_pr_m3": vaegt / m3 if m3 > 0 else 0.0,
    }
