"""Verifikation af core/produktion.py mod hånd-beregnede facit."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import produktion as pr  # noqa: E402


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol * max(1.0, abs(b))


def test_utilization_and_bottleneck():
    assert approx(pr.utilization(80, 100), 0.80)
    st = [{"navn": "A", "kapacitet": 120}, {"navn": "B", "kapacitet": 90},
          {"navn": "C", "kapacitet": 150}]
    res = pr.bottleneck(st)
    assert res["flaskehals"] == "B"
    assert approx(res["linjekapacitet"], 90)
    # udnyttelse: B=100%, A=90/120=0.75, C=90/150=0.6
    by = {s["navn"]: s["udnyttelse"] for s in res["stationer"]}
    assert approx(by["A"], 0.75) and approx(by["B"], 1.0) and approx(by["C"], 0.6)


def test_littles_law_all_directions():
    assert approx(pr.littles_law(throughput=50, flow_time=4)["WIP"], 200)
    assert approx(pr.littles_law(wip=200, flow_time=4)["R"], 50)
    assert approx(pr.littles_law(wip=200, throughput=50)["T"], 4)
    assert "fejl" in pr.littles_law(wip=1)


def test_oee():
    # planned 480, downtime 80 -> run 400; ideal 0.5/stk; 700 stk; 670 gode
    r = pr.oee(480, 80, 0.5, 700, 670)
    assert approx(r["tilgaengelighed"], 400 / 480)
    assert approx(r["ydelse"], (0.5 * 700) / 400)        # 350/400 = 0.875
    assert approx(r["kvalitet"], 670 / 700)
    assert approx(r["OEE"], (400/480) * 0.875 * (670/700))


def test_otif():
    # 90 til tiden, 95 komplet, antag uafhængighed
    r = pr.otif(90, 95, total=100)
    assert approx(r["OTIF"], 0.90 * 0.95)
    # med fælles måling
    r2 = pr.otif(90, 95, both=88, total=100)
    assert approx(r2["OTIF"], 0.88)


def test_line_balancing():
    assert approx(pr.takt_time(480, 120), 4.0)           # 480 min / 120 stk
    # opgavetider sum=18, takt=4 -> ceil(4.5)=5 stationer
    assert pr.theoretical_min_stations([5, 3, 4, 2, 4], 4) == 5
    # stationstider
    r = pr.line_balance([4, 4, 3.5, 4, 2.5])
    assert approx(r["cyklustid"], 4.0)
    assert approx(r["effektivitet"], 18 / (5 * 4))       # 0.9
    assert approx(r["output_pr_time"], 60 / 4)


def test_processkort():
    steps = [{"tid": 5, "type": "V"}, {"tid": 3, "type": "IV"},
             {"tid": 2, "type": "V"}, {"tid": 10, "type": "IV"}]
    r = pr.processkort(steps)
    assert approx(r["cyklustid"], 20)
    assert approx(r["vaerdigivende_tid"], 7)
    assert approx(r["vaerdigivende_pct"], 7 / 20)


def test_knap_kapacitet():
    prod = [
        {"navn": "A", "db_stk": 100, "tid_pr_stk": 2, "efterspoergsel": 50},
        {"navn": "B", "db_stk": 60, "tid_pr_stk": 1, "efterspoergsel": 100},
        {"navn": "C", "db_stk": 40, "tid_pr_stk": 2, "efterspoergsel": 50},
    ]
    r = pr.knap_kapacitet(prod, tilgaengelig_tid=200)
    # prioritering efter DB/time: B(60) > A(50) > C(20)
    assert r["plan"][0]["navn"] == "B"
    by = {p["navn"]: p["produceres"] for p in r["plan"]}
    assert by["B"] == 100 and by["A"] == 50 and by["C"] == 0
    assert approx(r["samlet_db"], 100 * 50 + 60 * 100)   # 11000


def test_queue_metrics():
    r = pr.queue_metrics(8, 10)
    assert approx(r["rho"], 0.80)
    assert approx(r["Ts"], 0.5)
    assert approx(r["Tw"], 0.4)
    assert pr.queue_metrics(10, 8)["Ts"] == float("inf")   # ustabil


def test_perfect_order():
    r = pr.perfect_order(0.95, 0.98, 0.99, 0.97)
    assert approx(r["perfect_order"], 0.95 * 0.98 * 0.99 * 0.97)
    assert approx(pr.perfect_order_direct(100, 12), 0.88)


def test_mps_atp():
    r = pr.mps_atp(forecast=[100, 100, 100, 100], booked=[80, 120, 50, 40],
                   mps=[200, 0, 200, 0], start_inventory=50)
    assert [round(x) for x in r["pei"]] == [150, 30, 130, 30]
    atp = r["atp"]
    assert approx(atp[0], 50) and atp[1] is None
    assert approx(atp[2], 110) and atp[3] is None


def test_mrp_item():
    # gross 0,0,50,0,60 ; on_hand 20 ; LT 1 ; lot-for-lot
    gross = [0, 0, 50, 0, 60]
    r = pr.mrp_item(gross, [0] * 5, on_hand=20, lead_time=1, lot_size=0, weeks=5)
    # uge 3: behov 50, lager 20 -> net 30, modtag 30
    assert approx(r["net"][2], 30)
    assert approx(r["planned_receipts"][2], 30)
    # planned order forskudt 1 uge tilbage -> uge 2 (index 1)
    assert approx(r["planned_orders"][1], 30)
    assert approx(r["planned_orders"][3], 60)   # for modtag i uge 5


def test_mrp_lotsize():
    gross = [0, 0, 50, 0, 0]
    r = pr.mrp_item(gross, [0] * 5, on_hand=0, lead_time=1, lot_size=80, weeks=5)
    assert approx(r["planned_receipts"][2], 80)   # maks(50, 80)
    assert approx(r["pei"][2], 30)                 # 80 - 50


def test_mrp_explode():
    rows = [
        {"navn": "Stol", "foraelder": "", "antal": 1, "ledetid": 1, "lot": 0, "lager": 0},
        {"navn": "Ben", "foraelder": "Stol", "antal": 4, "ledetid": 1, "lot": 0, "lager": 0},
    ]
    demand = [0, 0, 0, 10]
    res = pr.mrp_explode(rows, demand, weeks=4)
    stol = res["items"]["Stol"]
    # Stol planned order i uge 3 (index 2) = 10
    assert approx(stol["planned_orders"][2], 10)
    ben = res["items"]["Ben"]
    # Ben brutto = Stol planned orders × 4 -> uge 3 = 40
    assert approx(ben["gross"][2], 40)
    assert approx(ben["planned_orders"][1], 40)   # forskudt 1 uge


def test_sop_level_vs_chase():
    fc = [1000, 1200, 800, 1000]
    common = dict(timer_pr_enhed=2, timer_pr_md=160, startlager=0, start_arbejdere=12,
                  hyreomk=5000, fyreomk=8000, lageromk=10)
    lev = pr.sop_plan(fc, strategi="Level", **common)
    cha = pr.sop_plan(fc, strategi="Chase", **common)
    # Level: konstant arbejdsstyrke
    assert len(set(lev["workers"])) == 1
    # Chase: arbejdere følger efterspørgsel (varierer)
    assert len(set(cha["workers"])) > 1
    # begge har en samlet omkostning
    assert lev["total"] > 0 and cha["total"] > 0


def test_oee_guard_umulig_stilstand():
    # stilstand > planlagt tid: køretid negativ -> NaN i stedet for stille positivt tal
    r = pr.oee(480, 500, 0.5, 700, 670)
    assert math.isnan(r["tilgaengelighed"]) and math.isnan(r["OEE"])
    # stilstand = planlagt tid: køretid 0 -> ydelse og OEE NaN
    r0 = pr.oee(480, 480, 0.5, 700, 670)
    assert math.isnan(r0["ydelse"]) and math.isnan(r0["OEE"])


def test_assign_stations_heuristik():
    # takt 4: [3,1] fylder station 1, [2, 1.5] station 2, [2.5, 1] station 3
    assert pr.assign_stations([3, 1, 2, 1.5, 2.5, 1], 4) == [1, 1, 2, 2, 3, 3]
    # en opgave større end takt får sin egen station
    assert pr.assign_stations([5, 1], 4) == [1, 2]
    # ugyldig takt: én station pr. opgave (ingen crash)
    assert pr.assign_stations([1, 2, 3], 0) == [1, 2, 3]
    assert pr.assign_stations([], 4) == []


def test_mrp_lot_multipla():
    gross = [0, 0, 120, 0, 0]
    r_min = pr.mrp_item(gross, [0] * 5, on_hand=0, lead_time=1, lot_size=50,
                        weeks=5, lot_mode="min")
    r_mul = pr.mrp_item(gross, [0] * 5, on_hand=0, lead_time=1, lot_size=50,
                        weeks=5, lot_mode="multipla")
    assert approx(r_min["planned_receipts"][2], 120)   # maks(120, 50) = 120
    assert approx(r_mul["planned_receipts"][2], 150)   # loft(120/50)·50 = 150
    assert approx(r_mul["pei"][2], 30)                 # 150 - 120


def test_sop_restordre_og_afrunding():
    # Front-tung efterspørgsel giver restordre (negativt slutlager) i md. 1 for Level
    fc = [1600, 400]
    common = dict(timer_pr_enhed=2, timer_pr_md=160, startlager=0, start_arbejdere=13,
                  hyreomk=0, fyreomk=0, lageromk=10)
    lev = pr.sop_plan(fc, strategi="Level", restordreomk=30, **common)
    # krævede arbejdere [20, 5], snit 12,5 -> round-half-up = 13 (banker's ville give 12)
    assert lev["workers"] == [13, 13]
    # produktion 13·160/2 = 1040/md -> ending = [-560, +80]
    assert approx(lev["ending"][0], -560) and approx(lev["ending"][1], 80)
    assert approx(lev["lager_total"], 80 * 10)         # kun positivt lager til lagersats
    assert approx(lev["restordre_total"], 560 * 30)    # negativt lager til restordresats
    assert approx(lev["total"], 800 + 16800)
    # bagudkompatibelt: uden restordreomk falder den tilbage til lageromk
    lev2 = pr.sop_plan(fc, strategi="Level", **common)
    assert approx(lev2["restordre_total"], 560 * 10)


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
