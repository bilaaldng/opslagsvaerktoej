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


def test_npv_med_hul_i_aar():
    # År-kolonnen skal bruges til diskontering: år 0, 1 og 5 (hul i årrækken)
    cf = [-1000, 500, 800]
    ys = [0, 1, 5]
    expect = -1000 + 500 / 1.1 + 800 / 1.1 ** 5
    assert approx(ok.npv(0.10, cf, ys), expect, tol=0.001)
    # Uden years antages konsekutive år 0,1,2 — dét giver et ANDET (og her positivt) tal,
    # så testen fanger regressionen hvor år-kolonnen ignoreres
    assert ok.npv(0.10, cf, ys) < 0 < ok.npv(0.10, cf)
    # IRR skal være konsistent med samme diskontering
    r = ok.irr(cf, ys)
    assert approx(ok.npv(r, cf, ys), 0.0, tol=0.001)
    # payback interpolerer hen over hullet: -500 mangler efter år 1, år 5 giver 800
    # => 1 + 4·(500/800) = 3,5 år
    assert approx(ok.payback(cf, ys), 3.5)


def test_kritisk_levetid_med_hul_i_aar():
    cf = [-1000, 500, 800]
    ys = [0, 1, 5]
    # Ved 5 %: diskonteret år 1 = 476,2; år 5 = 626,8 — investeringen tjenes hjem
    # i spændet år 1→5: 1 + 4·(1000−476,2)/626,8 ≈ 4,34 år
    kl = ok.kritisk_levetid(cf, 0.05, ys)
    assert approx(kl, 4.34, tol=0.01)
    # Ved 10 % dækker de diskonterede cashflows (951,2) aldrig investeringen → NaN
    kl10 = ok.kritisk_levetid(cf, 0.10, ys)
    assert kl10 != kl10


def test_fyns_maskine_1():
    # Fyns Beklædning Spm 7 (Bilag 3): Maskine I, 8 %, DB 100 kr./stk., scrap 50.000 i år 5
    cf = [-500000, 100000, 110000, 120000, 130000, 190000]
    assert approx(ok.npv(0.08, cf), 7024, tol=0.001)          # facit: 7.024 kr.
    ko = ok.kritisk_omsaetning(cf, 0.08, salgspris_pr_stk=400, db_pr_stk=100)
    assert approx(ko["kritisk_stk"], 924, tol=0.001)          # facit: 924 stk.
    assert approx(ko["kritisk_omsaetning"], 369655, tol=0.001)  # facit: ca. 369.000 kr.


def test_fyns_maskine_2():
    # Fyns Beklædning Spm 8 (Bilag 3): Maskine II, 8 %, DB 160 kr./stk., scrap 60.000 i år 5
    cf = [-750000, 160000, 176000, 192000, 208000, 284000]
    assert approx(ok.npv(0.08, cf), 47627, tol=0.001)                          # facit: 47.627 kr.
    assert approx(ok.kritisk_investeringsbeloeb(cf, 0.08), 797627, tol=0.001)  # facit: 797.627 kr.
    assert approx(ok.kritisk_aarlig_indbetaling(750000, 0.08, 5, 60000),
                  177615, tol=0.001)                                           # facit: 177.615 kr./år
    # kritisk indkøbspris er samme mekanik som kritisk investeringsbeløb (DSS Spm 6)
    assert approx(ok.kritisk_indkoebspris(cf, 0.08), ok.kritisk_investeringsbeloeb(cf, 0.08))


def test_fordelingskalkulation():
    # var 40, faste 200.000, kapacitet 10.000, udnyttelse 80 %, fortjeneste 40 % af salgsprisen
    r = ok.fordelingskalkulation(40, 200000, 10000, 0.8, 0.40)
    assert approx(r["andel_kapacitetsomk"], 25)     # 200000/(10000·0,8)
    assert approx(r["egenpris"], 65)                # 40 + 25
    assert approx(r["salgspris"], 108.33, tol=0.001)
    # avancen udgør præcis 40 % af salgsprisen ...
    assert approx(r["avance"] / r["salgspris"], 0.40, tol=0.001)
    # ... men den FAKTISKE dækningsgrad er højere (egenprisen indeholder faste omk.)
    assert approx(r["faktisk_dg"], (108.3333 - 40) / 108.3333, tol=0.001)
    assert r["faktisk_dg"] > 0.40


def test_indekstal():
    idx = ok.indekstal([200, 220, 180])
    assert approx(idx[0], 100)
    assert approx(idx[1], 110)
    assert approx(idx[2], 90)
    # basis 0 eller NaN giver NaN hele vejen
    assert all(v != v for v in ok.indekstal([0, 10]))
    assert ok.indekstal([]) == []


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
