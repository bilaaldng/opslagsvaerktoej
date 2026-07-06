"""Verifikation af core/distribution.py mod hånd-beregnede facit.

Kanban-facit stammer fra kursusmaterialets gennemregnede eksempel
(IOSM kap. 13): D=300/t, T=2,6 t, x=15 %, C=45 → 897/45 = 19,93 → 20 kort.
Efter forbedringer: D=300, T=1,6, x=4 %, C=25 → 499,2/25 = 19,968 → 20 kort,
men maks-lager falder fra 900 til 500 stk.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import distribution as ds  # noqa: E402


def approx(a, b, tol=0.01):
    return abs(a - b) <= tol * max(1.0, abs(b))


# --- Kanban ----------------------------------------------------------------

def test_kanban_kursus_eksempel_del1():
    r = ds.kanban_kort(D=300, T=2.6, x=0.15, C=45)
    assert approx(r["y_raa"], 19.9333)
    assert r["y"] == 20
    assert r["maks_lager"] == 900


def test_kanban_kursus_eksempel_del2_forbedret():
    r = ds.kanban_kort(D=300, T=1.6, x=0.04, C=25)
    assert approx(r["y_raa"], 19.968)
    assert r["y"] == 20
    assert r["maks_lager"] == 500


def test_kanban_runder_op_ikke_ned():
    # 10·1·1,0/100 = 0,1 → stadig 1 kort (aldrig 0)
    assert ds.kanban_kort(D=10, T=1, x=0.0, C=100)["y"] == 1
    # præcist helt tal må IKKE rundes en ekstra op: 300·1,5·1,0/45 = 10,0
    assert ds.kanban_kort(D=300, T=1.5, x=0.0, C=45)["y"] == 10


def test_kanban_ugyldige_input():
    assert "fejl" in ds.kanban_kort(D=0, T=1, x=0.1, C=10)
    assert "fejl" in ds.kanban_kort(D=10, T=1, x=-0.1, C=10)


# --- Tyngdepunkt -----------------------------------------------------------

def test_tyngdepunkt_symmetri_giver_midten():
    kvadrat = [{"x": 0, "y": 0, "D": 5}, {"x": 10, "y": 0, "D": 5},
               {"x": 0, "y": 10, "D": 5}, {"x": 10, "y": 10, "D": 5}]
    r = ds.tyngdepunkt(kvadrat)
    assert approx(r["x"], 5) and approx(r["y"], 5)


def test_tyngdepunkt_vaegtet_gennemsnit():
    # x* = (10·0 + 30·10)/40 = 7,5 — trækker mod den store mængde
    pkt = [{"x": 0, "y": 0, "D": 10}, {"x": 10, "y": 0, "D": 30}]
    r = ds.tyngdepunkt(pkt)
    assert approx(r["x"], 7.5) and approx(r["y"], 0)


def test_tyngdepunkt_fragtrate_taeller_med():
    # samme mængder, men F=3 på det ene punkt → vægt 30 mod 10 → x* = 7,5
    pkt = [{"x": 0, "y": 0, "D": 10, "F": 1}, {"x": 10, "y": 0, "D": 10, "F": 3}]
    assert approx(ds.tyngdepunkt(pkt)["x"], 7.5)


def test_optimering_slaar_altid_startpunktet():
    pkt = [{"x": 0, "y": 0, "D": 40}, {"x": 12, "y": 1, "D": 10},
           {"x": 5, "y": 9, "D": 5}]
    r = ds.optimer_placering(pkt)
    assert r["TC"] <= r["start_TC"] + 1e-9
    # med stort overtag til ét punkt ligger optimum stort set PÅ punktet
    assert ds._dist(r["x"], r["y"], 0, 0) < 1.0


def test_to_punkter_optimum_hos_den_tunge():
    # klassisk egenskab: med to punkter ligger minimum hos den tungeste
    pkt = [{"x": 0, "y": 0, "D": 10}, {"x": 10, "y": 0, "D": 30}]
    r = ds.optimer_placering(pkt)
    assert ds._dist(r["x"], r["y"], 10, 0) < 0.05
    # TC dér = 10 enheder · afstand 10 = 100 (mod 150 i tyngdepunktet)
    assert approx(r["TC"], 100, tol=0.02)


def test_tc_haandregning():
    # ét anlæg i (0,0): TC = 20·1·5 + 10·2·13 = 100 + 260 = 360
    pkt = [{"x": 3, "y": 4, "D": 20, "F": 1}, {"x": 5, "y": 12, "D": 10, "F": 2}]
    assert approx(ds.total_transportomkostning(0, 0, pkt), 360)


def test_tyngdepunkt_ingen_maengder():
    assert "fejl" in ds.tyngdepunkt([{"x": 1, "y": 1, "D": 0}])
