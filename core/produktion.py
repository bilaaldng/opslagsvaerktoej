"""Ren matematik for Produktion-modulet.

Ingen Streamlit-kald herinde. Notation matcher brugerens danish-produktion-skill
og standard OM-lærebog (Bozarth):

    Kapacitet:      udnyttelsesgrad = belastning / kapacitet
    Little's Law:   WIP = gennemløbshastighed (R) · gennemløbstid (T)
    OEE:            OEE = tilgængelighed · ydelse · kvalitet
    OTIF:           on-time-in-full = andel ordrer leveret til tiden OG komplet
    Linjebalancering: takt time, min. stationer, effektivitet
    Processkort:    værdigivende % = V-tid / cyklustid
"""

from __future__ import annotations

import math


# ---------------------------------------------------------------------------
# Kapacitet, flaskehals og udnyttelsesgrad
# ---------------------------------------------------------------------------

def utilization(load: float, capacity: float) -> float:
    """Udnyttelsesgrad = belastning / kapacitet (1.0 = 100 %)."""
    return load / capacity if capacity else float("nan")


def bottleneck(stations: list[dict]) -> dict:
    """Find flaskehalsen i en serie af stationer.

    stations: liste af {"navn": str, "kapacitet": float} (stk./tidsenhed).
    Flaskehalsen er stationen med LAVEST kapacitet; den sætter linjens output.
    """
    valid = [s for s in stations if s.get("kapacitet", 0) > 0]
    if not valid:
        return {}
    bn = min(valid, key=lambda s: s["kapacitet"])
    output = bn["kapacitet"]
    for s in stations:
        cap = s.get("kapacitet", 0)
        s["udnyttelse"] = (output / cap) if cap else float("nan")
    return {"flaskehals": bn["navn"], "linjekapacitet": output, "stationer": stations}


# ---------------------------------------------------------------------------
# Little's Law:  WIP = R · T
# ---------------------------------------------------------------------------

def littles_law(wip: float | None = None, throughput: float | None = None,
                flow_time: float | None = None) -> dict:
    """Løs Little's Law for den manglende af de tre.

    WIP = gennemløbshastighed (R) · gennemløbstid (T). Angiv præcis to.
    """
    known = [x is not None for x in (wip, throughput, flow_time)]
    if sum(known) != 2:
        return {"fejl": "Angiv præcis to af de tre."}
    if wip is None:
        return {"WIP": throughput * flow_time, "R": throughput, "T": flow_time}
    if throughput is None:
        return {"WIP": wip, "R": wip / flow_time if flow_time else float("nan"),
                "T": flow_time}
    return {"WIP": wip, "R": throughput,
            "T": wip / throughput if throughput else float("nan")}


# ---------------------------------------------------------------------------
# OEE = tilgængelighed · ydelse · kvalitet
# ---------------------------------------------------------------------------

def oee(planned_time: float, downtime: float, ideal_cycle_time: float,
        total_count: float, good_count: float) -> dict:
    """Overall Equipment Effectiveness med de tre delfaktorer.

    planned_time, downtime: samme tidsenhed (fx min.).
    ideal_cycle_time: ideel tid pr. enhed (samme tidsenhed).
    total_count: producerede enheder. good_count: gode enheder.
    """
    run_time = planned_time - downtime
    availability = run_time / planned_time if planned_time else float("nan")
    performance = (ideal_cycle_time * total_count) / run_time if run_time else float("nan")
    quality = good_count / total_count if total_count else float("nan")
    return {
        "tilgaengelighed": availability,
        "ydelse": performance,
        "kvalitet": quality,
        "OEE": availability * performance * quality,
        "koeretid": run_time,
    }


# ---------------------------------------------------------------------------
# OTIF — On Time In Full
# ---------------------------------------------------------------------------

def otif(on_time: float, in_full: float, both: float | None = None,
         total: float = 100) -> dict:
    """OTIF-andel.

    on_time, in_full, both, total: antal ordrer (eller procenter med total=100).
    Hvis 'both' (til tiden OG komplet) er kendt, bruges den; ellers antages
    uafhængighed: OTIF = (on_time/total)·(in_full/total).
    """
    ot = on_time / total if total else float("nan")
    iff = in_full / total if total else float("nan")
    if both is not None:
        otif_rate = both / total if total else float("nan")
    else:
        otif_rate = ot * iff
    return {"on_time": ot, "in_full": iff, "OTIF": otif_rate}


# ---------------------------------------------------------------------------
# Linjebalancering (assembly line balancing)
# ---------------------------------------------------------------------------

def takt_time(available_time: float, required_output: float) -> float:
    """Takt time = tilgængelig produktionstid / krævet output."""
    return available_time / required_output if required_output else float("nan")


def theoretical_min_stations(task_times: list[float], takt: float) -> int:
    """Min. antal stationer = loft(Σ opgavetider / takt time)."""
    total = sum(task_times)
    return math.ceil(total / takt) if takt else 0


def line_balance(station_times: list[float]) -> dict:
    """Effektivitet ud fra de faktiske stationstider.

    Cyklustid = max(stationstider). Effektivitet = Σtid / (n · cyklustid).
    """
    valid = [t for t in station_times if t is not None]
    n = len(valid)
    if n == 0:
        return {}
    cycle = max(valid)
    total = sum(valid)
    eff = total / (n * cycle) if cycle else float("nan")
    return {
        "cyklustid": cycle,
        "antal_stationer": n,
        "effektivitet": eff,
        "balancetab": 1 - eff,
        "samlet_idle": n * cycle - total,
        "output_pr_time": 60 / cycle if cycle else float("nan"),
    }


# ---------------------------------------------------------------------------
# Processkort (Lean-procesanalyse)
# ---------------------------------------------------------------------------

def processkort(steps: list[dict]) -> dict:
    """Værdigivende analyse.

    steps: liste af {"tid": float, "type": "V"|"IV"}.
    Cyklustid = Σtider. Værdigivende % = V-tid / cyklustid.
    """
    total = sum(s.get("tid", 0) for s in steps)
    v_tid = sum(s.get("tid", 0) for s in steps if str(s.get("type", "")).upper() == "V")
    return {
        "cyklustid": total,
        "vaerdigivende_tid": v_tid,
        "ikke_vaerdigivende_tid": total - v_tid,
        "vaerdigivende_pct": (v_tid / total) if total else float("nan"),
    }


# ---------------------------------------------------------------------------
# Knap kapacitet — produktmix efter dækningsbidrag pr. flaskehalstime
# ---------------------------------------------------------------------------

def knap_kapacitet(produkter: list[dict], tilgaengelig_tid: float) -> dict:
    """Optimal produktmix når en flaskehalsressource er knap.

    produkter: liste af {"navn", "db_stk", "tid_pr_stk", "efterspoergsel"}.
    Prioritér efter DB pr. flaskehalstime (= db_stk / tid_pr_stk), fyld op til
    efterspørgsel indtil tiden er brugt.
    """
    items = []
    for p in produkter:
        tid = p.get("tid_pr_stk", 0)
        db = p.get("db_stk", 0)
        items.append({
            "navn": p.get("navn", ""),
            "db_stk": db,
            "tid_pr_stk": tid,
            "efterspoergsel": p.get("efterspoergsel", 0),
            "db_pr_time": (db / tid) if tid else float("nan"),
        })
    items.sort(key=lambda x: (x["db_pr_time"] if x["db_pr_time"] == x["db_pr_time"] else -1),
              reverse=True)
    rest = tilgaengelig_tid
    samlet_db = 0.0
    for it in items:
        tid_kraevet = it["efterspoergsel"] * it["tid_pr_stk"]
        if it["tid_pr_stk"] <= 0:
            it["produceres"] = 0
        elif tid_kraevet <= rest:
            it["produceres"] = it["efterspoergsel"]
        else:
            it["produceres"] = int(rest / it["tid_pr_stk"])
        brugt = it["produceres"] * it["tid_pr_stk"]
        rest -= brugt
        it["tid_brugt"] = brugt
        it["db_i_alt"] = it["produceres"] * it["db_stk"]
        samlet_db += it["db_i_alt"]
    return {"plan": items, "samlet_db": samlet_db, "uudnyttet_tid": max(rest, 0.0)}


# ---------------------------------------------------------------------------
# Udnyttelsesgrad / kø (M/M/1):  rho = lambda / my
# ---------------------------------------------------------------------------

def queue_metrics(arrival: float, service: float) -> dict:
    """Udnyttelsesgrad og ventetid for en enkelt ressource (M/M/1).

    arrival (λ) = ankomst-/efterspørgselsrate, service (μ) = kapacitetsrate.
    rho = λ/μ. Ts = gennemløbstid i systemet, Tw = ventetid i kø.
    """
    rho = arrival / service if service else float("nan")
    if service > arrival:
        Ts = 1 / (service - arrival)
        Tw = arrival / (service * (service - arrival))
    else:
        Ts = float("inf")
        Tw = float("inf")
    return {"rho": rho, "Ts": Ts, "Tw": Tw}


# ---------------------------------------------------------------------------
# Perfect Order / OTIF  (Bozarth: andel uden fejl)
# ---------------------------------------------------------------------------

def perfect_order(til_tiden: float, komplet: float, ubeskadiget: float,
                  korrekt_faktura: float) -> dict:
    """Perfect Order-rate ud fra de fire delkriterier (som andele 0-1).

    Antager uafhængighed: perfect order = produkt af de fire delrater.
    """
    rates = {"til_tiden": til_tiden, "komplet": komplet,
             "ubeskadiget": ubeskadiget, "korrekt_faktura": korrekt_faktura}
    p = 1.0
    for v in rates.values():
        p *= v
    return {"perfect_order": p, "komponenter": rates}


def perfect_order_direct(total: float, fejlordrer: float) -> float:
    """Perfect Order målt direkte: (total − ordrer med ≥1 fejl) / total."""
    return (total - fejlordrer) / total if total else float("nan")


# ---------------------------------------------------------------------------
# MPS + ATP (Master Production Schedule / Available to Promise)
# ---------------------------------------------------------------------------

def mrp_item(gross: list[float], scheduled: list[float], on_hand: float,
             lead_time: int, lot_size: float, weeks: int) -> dict:
    """Tidsfaset MRP for ÉN komponent.

    PEI_t = PEI_(t−1) + scheduled + planned_receipt − gross.
    Net_t = gross − scheduled − PEI_(t−1) (kun positiv).
    Planned receipt = maks(net, lotstørrelse); lot_size=0 betyder lot-for-lot.
    Planned orders = planned receipts forskudt LT uger tilbage.
    """
    pei = [0.0] * weeks
    net = [0.0] * weeks
    prec = [0.0] * weeks
    porders = [0.0] * weeks
    overdue = 0.0
    prev = on_hand
    for t in range(weeks):
        avail = prev + scheduled[t]
        if avail >= gross[t]:
            net[t] = 0.0
            prec[t] = 0.0
        else:
            net[t] = gross[t] - avail
            prec[t] = max(net[t], lot_size) if lot_size > 0 else net[t]
        pei[t] = avail + prec[t] - gross[t]
        prev = pei[t]
        if prec[t] > 0:
            rel = t - lead_time
            if rel >= 0:
                porders[rel] += prec[t]
            else:
                overdue += prec[t]
    return {"gross": gross, "scheduled": scheduled, "pei": pei, "net": net,
            "planned_receipts": prec, "planned_orders": porders, "overdue": overdue}


def _mrp_level(name, parent_of):
    lvl, p, seen = 0, parent_of.get(name), set()
    while p and p not in seen:
        seen.add(p)
        lvl += 1
        p = parent_of.get(p)
    return lvl


def mrp_explode(rows: list[dict], demand: list[float], weeks: int) -> dict:
    """Multi-niveau MRP (BOM-eksplosion).

    rows: liste af {navn, foraelder, antal, ledetid, lot, lager}.
    Slutproduktet har tom forælder og får demand som bruttobehov. Børn får
    bruttobehov = forælderens planned orders × antal pr. styk.
    """
    parent_of = {r["navn"]: (r.get("foraelder") or None) for r in rows}
    rows_sorted = sorted(rows, key=lambda r: _mrp_level(r["navn"], parent_of))
    results = {}
    for r in rows_sorted:
        par = r.get("foraelder")
        if not par:
            gross = list(demand)
        elif par in results:
            pp = results[par]["planned_orders"]
            gross = [pp[t] * r["antal"] for t in range(weeks)]
        else:
            gross = [0.0] * weeks
        results[r["navn"]] = mrp_item(gross, [0.0] * weeks, r["lager"],
                                      int(r["ledetid"]), r["lot"], weeks)
    return {"items": results, "raekkefoelge": [r["navn"] for r in rows_sorted]}


# ---------------------------------------------------------------------------
# S&OP / aggregeret produktionsplan (Level vs. Chase)
# ---------------------------------------------------------------------------

def sop_plan(forecast: list[float], timer_pr_enhed: float, timer_pr_md: float,
             startlager: float, start_arbejdere: float, hyreomk: float,
             fyreomk: float, lageromk: float, strategi: str) -> dict:
    """Aggregeret produktionsplan efter Level- eller Chase-strategi.

    Level: konstant arbejdsstyrke (årsgennemsnit), lager svinger.
    Chase: arbejdsstyrke følger efterspørgslen (rundes op), lager ~konstant.
    """
    n = len(forecast)
    workers_req = [f * timer_pr_enhed / timer_pr_md for f in forecast]
    if strategi == "Level":
        w = round(sum(workers_req) / n) if n else 0
        workers = [w] * n
    else:  # Chase
        workers = [math.ceil(x) for x in workers_req]

    production = [workers[t] * timer_pr_md / timer_pr_enhed for t in range(n)]
    hires, layoffs = [], []
    prev_w = start_arbejdere
    for t in range(n):
        diff = workers[t] - prev_w
        hires.append(diff if diff > 0 else 0)
        layoffs.append(-diff if diff < 0 else 0)
        prev_w = workers[t]

    ending = []
    inv = startlager
    for t in range(n):
        inv = inv + production[t] - forecast[t]
        ending.append(inv)

    hyre_total = sum(hires) * hyreomk
    fyre_total = sum(layoffs) * fyreomk
    lager_total = sum(abs(e) for e in ending) * lageromk
    return {
        "workers": workers, "production": production, "hires": hires,
        "layoffs": layoffs, "ending": ending,
        "hyre_total": hyre_total, "fyre_total": fyre_total, "lager_total": lager_total,
        "total": hyre_total + fyre_total + lager_total,
    }


def mps_atp(forecast: list[float], booked: list[float], mps: list[float],
            start_inventory: float) -> dict:
    """Beregn projected ending inventory (PEI) og available-to-promise (ATP).

    PEI_t = PEI_(t-1) + MPS_t − MAX(forecast_t, booked_t).
    ATP beregnes kun i uger med MPS > 0 (samt uge 1):
        ATP = MPS_t (+ startlager kun i uge 1) − Σ bookede ordrer frem til
        næste uge med MPS.
    """
    n = len(forecast)
    pei = []
    prev = start_inventory
    for t in range(n):
        prev = prev + mps[t] - max(forecast[t], booked[t])
        pei.append(prev)

    atp = [None] * n
    for t in range(n):
        if mps[t] > 0 or t == 0:
            # summer bookede ordrer fra denne uge til (men ikke med) næste MPS-uge
            nxt = n
            for j in range(t + 1, n):
                if mps[j] > 0:
                    nxt = j
                    break
            booked_sum = sum(booked[t:nxt])
            base = mps[t] + (start_inventory if t == 0 else 0)
            atp[t] = base - booked_sum
    return {"pei": pei, "atp": atp}
