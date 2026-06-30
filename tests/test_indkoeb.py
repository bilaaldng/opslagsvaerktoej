"""Verifikation af core/indkoeb.py mod facit fra brugerens materiale.

Kør:  python -m pytest tests/ -q        (eller:  python tests/test_indkoeb.py)
"""
import math
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import indkoeb as ik  # noqa: E402


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol * max(1.0, abs(b))


# --- EOQ: Nordic Components "Stormkøkken S" --------------------------------
# D=7800, S=450, pris=148, lagerrente i=0.18 -> H=26.64
def test_eoq_nordic_stormkoekken():
    H = ik.holding_cost_per_unit(148, 0.18)
    assert approx(H, 26.64)
    q = ik.eoq(7800, 450, H)
    assert approx(q, 513.3, tol=0.005)           # facit ~513 stk
    s = ik.eoq_summary(7800, 450, H)
    # ved Q* skal ordreomk. = lageromk. (klassisk EOQ-egenskab)
    assert approx(s["ordreomkostning"], s["lageromkostning"], tol=0.01)
    assert approx(s["antal_ordrer"], 7800 / q)


# --- POQ/EPQ: Fyns Beklædning Bilag 8, ES-220 -----------------------------
# D=48000, S=850, produktionspris=4.20, rate=0.22 -> H=0.924
# d=192/dag, p=600/dag -> (1-d/p)=0.68
def test_poq_fyns_es220():
    H = ik.holding_cost_per_unit(4.20, 0.22)
    assert approx(H, 0.924)
    q = ik.epq(48000, 850, H, d=192, p=600)
    assert approx(q, 11396, tol=0.01)            # POQ ~11.4k stk
    s = ik.epq_summary(48000, 850, H, d=192, p=600, Q_current=8000)
    assert approx(s["andel_til_lager"], 0.68)
    # ved POQ* skal igangsætning = lageromkostning
    assert approx(s["igangsaetning"], s["lageromkostning"], tol=0.01)
    # nuværende serie (8000) er suboptimal -> positiv besparelse
    assert s["besparelse"] > 0


# --- ABC: Nordic Components 15 varer --------------------------------------
def test_abc_nordic():
    data = pd.DataFrame({
        "Betegnelse": ["Kompas Pro", "Mini Gasbrænder", "Vandfilter Pure",
                       "Karabinhage XL", "Stormkøkken L", "Stormkøkken S",
                       "Powerbank 10k", "Powerbank 20k", "Titanium Spork",
                       "Reparationskit", "First-Aid Micro", "Sovepose -10",
                       "Ultralight Underlag", "Pakkepose 10L", "Pakkepose 30L"],
        "Årligt forbrug": [12000, 9600, 4800, 38000, 3000, 7800, 2400, 1600,
                            26000, 5000, 14000, 600, 1200, 8200, 4200],
        "Enhedspris": [28, 52, 118, 8, 210, 148, 260, 340, 19, 46, 24, 790,
                       540, 64, 96],
    })
    res = ik.abc_analysis(data)
    # sorteret faldende efter årsværdi
    assert res["Årsværdi"].is_monotonic_decreasing
    # akkumuleret % slutter på 1.0
    assert approx(res["Akkumuleret %"].iloc[-1], 1.0)
    # kategorier findes
    assert set(res["Kategori"]).issubset({"A", "B", "C"})
    summ = ik.abc_summary(res)
    assert approx(summ["Andel af værdi %"].sum(), 1.0)


# --- ROP / SS: Nordic Components "Stormkøkken S" --------------------------
# D=7800, sigma=11/uge, L=2 uger, z(95%)=1.65 -> SS=1.65*11*sqrt(2)
def test_rop_nordic():
    z = ik.z_from_service(0.95)
    assert approx(z, 1.645, tol=0.01)
    ss = ik.safety_stock(1.65, 11, 2)
    assert approx(ss, 25.67, tol=0.01)           # facit ~25.7 stk
    s = ik.rop_summary(7800, sigma=11, L=2, service=0.95)
    assert approx(s["d"], 150.0)                 # 7800/52
    assert approx(s["forbrug_i_ledetid"], 300.0)


# --- TCA / Make-vs-buy: Fyns Beklædning Bilag 7 ---------------------------
def test_tca_fyns_bilag7():
    outsource = {
        "indkøb": 134400, "søfragt": 40800, "told": 7884, "adm": 14400,
        "lager": 9636, "kassation": 7480, "risiko": 2688,
    }
    insource = {
        "råmateriale": 86400, "løn": 115200, "maskine": 18000,
        "igangsætning": 5100, "lager": 3696, "kassation": 3024,
        "engangsomk": 5000,
    }
    assert approx(ik.tca_total(outsource), 217288, tol=0.001)
    assert approx(ik.tca_total(insource), 236420, tol=0.001)
    # pris pr. stk ved 48000 stk
    assert approx(ik.tca_total(outsource) / 48000, 4.53, tol=0.01)
    assert approx(ik.tca_total(insource) / 48000, 4.93, tol=0.01)


def test_z_table_matches_user():
    # brugerens faste z-tabel
    assert ik.Z_TABLE[0.90] == 1.28
    assert ik.Z_TABLE[0.95] == 1.65
    assert ik.Z_TABLE[0.99] == 2.33


def test_weighted_supplier_score():
    df = pd.DataFrame({
        "Leverandør": ["A", "B"],
        "Pris/TCO": [5, 3],
        "Kvalitet": [3, 5],
    })
    w = {"Pris/TCO": 0.5, "Kvalitet": 0.5}
    res = ik.evaluate_suppliers(df, w)
    # A: 0.5*5+0.5*3=4.0 ; B: 0.5*3+0.5*5=4.0 -> ens
    assert approx(res["Samlet score"].iloc[0], 4.0)
    # vægte normaliseres hvis de ikke summer til 1
    res2 = ik.evaluate_suppliers(df, {"Pris/TCO": 1, "Kvalitet": 1})
    assert approx(res2["Samlet score"].iloc[0], 4.0)


def test_review_periodic():
    # d=100/uge, P=4 uger review, L=2 uger, SS=50
    R = ik.periodic_max_level(100, 4, 2, 50)
    assert approx(R, 650)                 # 100*(4+2)+50
    assert approx(ik.order_up_to(R, 200), 450)
    assert ik.order_up_to(R, 1000) == 0   # aldrig negativ


def test_forecast_moving_average():
    actual = [10, 12, 13, 12, 15]
    fc = ik.moving_average(actual, 3)
    assert len(fc) == len(actual) + 1     # incl. næste periode
    assert fc[3] is not None and approx(fc[3], (10 + 12 + 13) / 3)
    assert approx(fc[-1], (13 + 12 + 15) / 3)
    err = ik.forecast_errors(actual, fc)
    assert err["n"] == 2                  # kun t=3,4 har både D og F
    assert approx(err["MAD"], 1.5)


def test_forecast_exp_smoothing():
    actual = [10, 12, 13, 12, 15]
    F = ik.exp_smoothing(actual, alpha=0.3, f0=10)
    assert len(F) == len(actual) + 1
    assert approx(F[2], 0.3 * 12 + 0.7 * 10)
    err = ik.forecast_errors(actual, F)
    assert err["MFE"] == err["MFE"]       # ikke NaN
    assert err["MAD"] >= 0


def test_breakeven_crossing():
    # to linjer: A billig fast/dyr variabel, B dyr fast/billig variabel
    v = ik.breakeven_volume(fixed_a=0, var_a=4.53, fixed_b=51220, var_b=3.85)
    # kontrol: totalerne skal være ens ved v
    ta = ik.total_cost_linear(0, 4.53, v)
    tb = ik.total_cost_linear(51220, 3.85, v)
    assert approx(ta, tb)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS  {fn.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"FAIL  {fn.__name__}: {e}")
        except Exception as e:
            print(f"ERROR {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(fns)} tests bestået")
    sys.exit(0 if passed == len(fns) else 1)
