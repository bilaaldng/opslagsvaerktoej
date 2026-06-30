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
