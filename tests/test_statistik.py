"""Verifikation af core/statistik.py mod kendte facit (scipy)."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import statistik as stat  # noqa: E402


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol * max(1.0, abs(b))


def test_normal():
    # P(-1.96 < Z < 1.96) ≈ 0.95
    assert approx(stat.normal_area(-1.96, 1.96), 0.95, tol=0.005)
    # haleareal 0.975 -> z ≈ 1.96
    assert approx(stat.prob_to_z(0.975), 1.96, tol=0.005)
    assert approx(stat.z_score(120, 100, 10), 2.0)
    assert approx(stat.normal_area(None, 0), 0.5)          # P(Z<0)=0.5


def test_ci_mean():
    # n=25, gns=50, s=10, 95% -> t(0.975,24)=2.0639 -> ME=4.128
    r = stat.ci_mean(50, 10, 25, 0.95)
    assert approx(r["t"], 2.0639, tol=0.01)
    assert approx(r["margin"], 4.128, tol=0.01)
    assert approx(r["nedre"], 45.872, tol=0.01)


def test_ci_proportion():
    # phat=0.4, n=100, 95% -> z=1.96, se=0.04899, ME=0.0960
    r = stat.ci_proportion(0.4, 100, 0.95)
    assert approx(r["z"], 1.96, tol=0.005)
    assert approx(r["margin"], 0.0960, tol=0.01)


def test_binom():
    # P(X=2; n=10, p=0.5) = 45/1024 ≈ 0.043945
    assert approx(stat.binom_pmf(2, 10, 0.5), 45 / 1024, tol=0.005)
    s = stat.binom_summary(10, 0.5, 2)
    assert approx(s["middel"], 5.0)
    assert approx(s["sigma"], math.sqrt(10 * 0.5 * 0.5))
    # P(X>=1) = 1 - P(X=0) = 1 - 0.5^10
    assert approx(stat.binom_summary(10, 0.5, 1)["P_mindst"], 1 - 0.5 ** 10, tol=0.005)
    ap = stat.binom_normal_approx(100, 0.3)
    assert approx(ap["mu"], 30) and ap["gyldig"]


def test_p_chart():
    defects = [2, 4, 3, 5, 1]
    sizes = [100, 100, 100, 100, 100]
    r = stat.p_chart(defects, sizes)
    assert approx(r["pbar"], 15 / 500)                    # 0.03
    # σ_p = sqrt(0.03*0.97/100)=0.01706 -> UCL≈0.0812
    assert approx(float(r["UCL"][0]), 0.03 + 3 * math.sqrt(0.03 * 0.97 / 100), tol=0.01)
    assert float(r["LCL"][0]) == 0.0                      # max(neg, 0)


def test_linear_regression():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    r = stat.linear_regression(x, y)
    assert approx(r["haeldning"], 0.6)
    assert approx(r["skaering"], 2.2)
    assert approx(r["r2"], 0.6, tol=0.02)
    # forudsigelse: y(6) = 2.2 + 0.6*6 = 5.8
    assert approx(stat.regression_predict(6, r["haeldning"], r["skaering"]), 5.8)


# --- Hypotesetest -----------------------------------------------------------

def test_z_test_mean_fyns_spm11():
    # Fyns Spm 11-facit: x̄=76,97 mod μ0=75 (ensidet, højre) -> z=2,15,
    # kritisk 1,645, p=0,016 < 0,05 -> forkast H0 (signifikant over 75).
    r = stat.z_test_mean(76.97, 9.1628, 100, 75, sided="hoejre", alpha=0.05)
    assert approx(r["z"], 2.15, tol=0.005)
    assert approx(r["kritisk"], 1.645, tol=0.005)
    assert approx(r["p"], 0.016, tol=0.05)
    assert r["forkast"] is True


def test_z_test_mean_tosidet():
    # Tosidet: z=1,96 giver p=0,05 lige på grænsen
    r = stat.z_test_mean(51.96, 10, 100, 50, sided="tosidet", alpha=0.05)
    assert approx(r["z"], 1.96, tol=0.005)
    assert approx(r["p"], 0.05, tol=0.01)


def test_t_test_mean_mod_scipy():
    from scipy import stats as ss
    v = [11.69, 11.90, 11.93, 12.03, 11.88, 11.74, 11.73, 12.08, 11.66, 12.11]
    m = sum(v) / len(v)
    s = math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1))
    r = stat.t_test_mean(m, s, len(v), 12, sided="tosidet")
    ref = ss.ttest_1samp(v, 12)
    assert approx(r["t"], float(ref.statistic), tol=0.001)
    assert approx(r["p"], float(ref.pvalue), tol=0.001)
    assert r["df"] == len(v) - 1


def test_t_test_two_means_welch_mod_scipy():
    from scipy import stats as ss
    import numpy as np
    a = np.array([11.69, 11.90, 11.93, 12.03, 11.88, 11.74, 11.73, 12.08, 11.66, 12.11])
    b = np.array([12.0, 12.1, 11.9, 12.3, 12.2, 12.0])
    r = stat.t_test_two_means(a.mean(), a.std(ddof=1), a.size,
                              b.mean(), b.std(ddof=1), b.size, sided="tosidet")
    ref = ss.ttest_ind(a, b, equal_var=False)
    assert approx(r["t"], float(ref.statistic), tol=0.001)
    assert approx(r["p"], float(ref.pvalue), tol=0.001)


def test_z_test_two_means_venstre():
    # Élanor (70,28) < Sorén (76,97): venstre hale, klart signifikant
    r = stat.z_test_two_means(70.28, 8, 100, 76.97, 8, 100, sided="venstre")
    assert r["z"] < r["kritisk"] < 0
    assert r["p"] < 0.0001 and r["forkast"] is True


# --- Rå data ----------------------------------------------------------------

CHROM = [11.69, 11.90, 11.93, 12.03, 11.88, 11.74, 11.73, 12.08, 11.66, 12.11,
         11.64, 11.98, 11.92, 11.89, 12.30, 11.98, 11.79, 11.93, 11.87, 11.77,
         11.80, 11.69, 11.97, 11.89, 12.12, 11.84, 12.12, 11.87, 11.88, 11.94,
         11.63, 11.60, 11.85, 11.93, 11.67, 11.81, 12.07, 11.85, 11.66, 11.87,
         11.72, 11.71, 11.98, 12.25, 11.33, 11.73, 12.02, 11.72, 12.05, 11.96]


def test_parse_maalinger():
    r = stat.parse_maalinger("11,69 11.90; 12,03,\n1.234,5 abc 12")
    assert r["vaerdier"] == [11.69, 11.90, 12.03, 1234.5, 12.0]
    assert r["ignoreret"] == ["abc"]
    assert stat.parse_maalinger("")["vaerdier"] == []


def test_beskrivende_chrom():
    # DSS Spm 8: 50 chrom-målinger -> x̄=11,867, s=0,1791 (Excel-facit)
    d = stat.beskrivende(CHROM)
    assert d["n"] == 50
    assert approx(d["gennemsnit"], 11.867, tol=0.001)
    assert approx(d["s"], 0.1791, tol=0.005)
    assert approx(d["median"], 11.875, tol=0.001)


def test_ci_chrom_mod_krav():
    # 95 % KI for chrom: [11,816 ; 11,918] -> hele intervallet under kravet 12
    d = stat.beskrivende(CHROM)
    r = stat.ci_mean(d["gennemsnit"], d["s"], d["n"], 0.95)
    assert approx(r["nedre"], 11.816, tol=0.001)
    assert approx(r["oevre"], 11.918, tol=0.001)
    assert r["oevre"] < 12


# --- KI-udvidelser ----------------------------------------------------------

def test_ci_mean_z():
    # Kendt σ: n=25, gns=50, σ=10, 95 % -> ME = 1,96·10/5 = 3,92
    r = stat.ci_mean_z(50, 10, 25, 0.95)
    assert approx(r["z"], 1.96, tol=0.005)
    assert approx(r["margin"], 3.92, tol=0.005)


def test_sample_size():
    # n = (1,96·15/3)² = 96,04 -> 97
    assert stat.sample_size_mean(15, 3, 0.95)["n"] == 97
    # worst case p=0,5, ME=3 %-point -> n = 1,96²·0,25/0,03² = 1067,1 -> 1068
    assert stat.sample_size_proportion(0.5, 0.03, 0.95)["n"] == 1068


# --- Binomial-udvidelser ----------------------------------------------------

def test_binom_between():
    # P(2 ≤ X ≤ 4; n=10, p=0,5) = (45+120+210)/1024
    assert approx(stat.binom_between(2, 4, 10, 0.5), 375 / 1024, tol=0.001)
    assert stat.binom_between(4, 2, 10, 0.5) == 0.0
    assert approx(stat.binom_between(0, 10, 10, 0.5), 1.0)


def test_binom_pmf_array():
    arr = stat.binom_pmf_array(10, 0.5)
    assert len(arr) == 11
    assert approx(float(arr[2]), 45 / 1024, tol=0.005)
    assert approx(float(sum(arr)), 1.0)


def test_xbar_r_chart():
    samples = [[10, 12, 11], [9, 11, 10], [12, 13, 11], [10, 10, 12]]
    r = stat.xbar_r_chart(samples)
    assert r["n"] == 3
    assert approx(r["A2"], 1.023) and approx(r["D4"], 2.574)
    # X̿ og R̄
    assert approx(r["Xbarbar"], sum(r["means"]) / 4)
    assert approx(r["X_UCL"], r["Xbarbar"] + 1.023 * r["Rbar"], tol=0.01)


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
