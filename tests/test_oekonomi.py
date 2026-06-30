"""Verifikation af core/oekonomi.py mod hånd-beregnede facit."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import oekonomi as ok  # noqa: E402


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol * max(1.0, abs(b))


def test_npv_irr_payback():
    cf = [-1000, 400, 400, 400, 400]
    # NPV ved 10 %
    expect = -1000 + sum(400 / 1.1 ** t for t in range(1, 5))
    assert approx(ok.npv(0.10, cf), expect)
    # IRR: NPV(irr)=0
    r = ok.irr(cf)
    assert approx(ok.npv(r, cf), 0.0, tol=0.001)
    assert 0.20 < r < 0.25                     # ~21.9 %
    # payback = 1000/400 = 2.5 år
    assert approx(ok.payback(cf), 2.5)


def test_kritisk_levetid():
    cf = [-1000, 400, 400, 400, 400]
    kl = ok.kritisk_levetid(cf, 0.10)
    # diskonteret: 363.6, 330.6, 300.5 (kum 994.7 efter 3 år), år 4 dækker resten
    assert 3 < kl < 4


def test_break_even():
    r = ok.break_even(pris=100, variabel=60, faste=8000)
    assert approx(r["db_stk"], 40)
    assert approx(r["daekningsgrad"], 0.40)
    assert approx(r["nulpunktsmaengde"], 200)        # 8000/40
    assert approx(r["nulpunktsomsaetning"], 20000)   # 200·100
    assert approx(ok.safety_margin(25000, 20000), 0.20)


def test_bidragskalkulation():
    # kostpris 100, DG 75% -> DB=300, salgspris=400
    r = ok.bidragskalkulation(100, 0.75)
    assert approx(r["db"], 300)
    assert approx(r["salgspris"], 400)
    # kontrol: DG = DB/salgspris
    assert approx(r["db"] / r["salgspris"], 0.75)


def test_retrograd():
    # salgspris 500, DG 40%, var.salg 20, told 10% af købspris
    # købspris = (500*0.6 - 20)/1.1 = (300-20)/1.1 = 254.55
    r = ok.retrograd_kalkulation(500, 0.40, 20, 0.10)
    assert approx(r["maks_koebspris"], 280 / 1.1)


def test_prisoptimering():
    priser = [100, 90, 80, 70, 60]
    afs = [10, 20, 30, 40, 50]
    r = ok.prisoptimering(priser, afs, variabel_enhed=40, faste=500)
    # omsætning=1000,1800,2400,2800,3000 ; vo=400,800,1200,1600,2000
    # overskud=oms-vo-500 = 100,500,700,700,500 -> max ved idx 2 el. 3 (700)
    assert r["max_overskud"] == 700
    assert r["optimum_idx"] in (2, 3)


def test_afskrivning():
    r = ok.lineaer_afskrivning(120000, 20000, 5)
    assert approx(r["aarlig"], 20000)        # (120000-20000)/5
    assert approx(r["kvartal"], 5000)


def test_noegletal():
    r = ok.noegletal(omsaetning=1000, ebit=100, aarets_resultat=60, renteomk=20,
                     aktiver=800, egenkapital=400, gaeld=400,
                     omsaetningsaktiver=300, kortfristet_gaeld=150,
                     bruttofortjeneste=400)
    assert approx(r["overskudsgrad"], 0.10)
    assert approx(r["aoh"], 1.25)
    assert approx(r["afkastningsgrad"], 0.125)       # = overskudsgrad·AOH
    assert approx(r["overskudsgrad"] * r["aoh"], r["afkastningsgrad"])
    assert approx(r["soliditetsgrad"], 0.5)
    assert approx(r["likviditetsgrad"], 2.0)
    assert approx(r["egenkapitalforrentning"], 0.15)


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in fns:
        try:
            fn(); print(f"PASS  {fn.__name__}"); passed += 1
        except AssertionError as e:
            print(f"FAIL  {fn.__name__}: {e}")
        except Exception as e:
            print(f"ERROR {fn.__name__}: {type(e).__name__}: {e}")
    print(f"\n{passed}/{len(fns)} tests bestået")
    sys.exit(0 if passed == len(fns) else 1)
