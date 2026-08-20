"""De nye træningstilstandes datagrundlag.

Bankerne er ren data, så de kan testes uden at køre Streamlit. Det, der
faktisk kan gå galt her, er indholdsfejl: en påstand uden forklaring, en
kobling der kun rører ét fag (og dermed ikke træner det, den lover), eller
et virksomhedsnavn der er sluppet med ind.
"""
import os
import re
import sys

import pytest

ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROD)

from pakke_kobling import KOBLINGER, VALG  # noqa: E402
from pakke_paastande import PAASTANDE  # noqa: E402
from data.ordbog import FAGREGLER  # noqa: E402

KENDTE_FAG = {fag for fag, _ in FAGREGLER}

# Værktøjet er et generelt opslagsværk, ikke et case-referat. Hverken de gamle
# eksamenscaser eller fagenes nye må optræde i det synlige indhold.
FORBUDTE_NAVNE = [
    "Fyns Beklædning", "Dansk Stål", "Acme", "Marsica", "DSV", "Vestas",
    "DS Gruppen", "DanPejs", "Nordic Rims", "CookieDan", "Komergo",
    "Myonmo", "Tønder Brewery", "Topstans", "Dandairies", "LiX",
]


def _al_tekst(*dele):
    ud = []
    for d in dele:
        if isinstance(d, str):
            ud.append(d)
        elif isinstance(d, (list, tuple)):
            ud.append(_al_tekst(*d))
    return " ".join(ud)


# --- Kobl fagene -----------------------------------------------------------

def test_koblinger_rammer_mindst_to_fag():
    """En kobling der kun rører ét fag træner ikke det, tilstanden lover."""
    for situation, fag, _spm, _svar in KOBLINGER:
        assert len(set(fag)) >= 2, f"«{situation[:60]}…» kobler kun {fag}"


def test_koblingernes_fag_er_kendte():
    for situation, fag, _spm, _svar in KOBLINGER:
        for f in fag:
            assert f in KENDTE_FAG, f"ukendt fag «{f}» i «{situation[:50]}…»"


def test_koblinger_har_spoergsmaal_og_svar():
    for situation, _fag, spm, svar in KOBLINGER:
        assert spm, f"«{situation[:50]}…» har ingen spørgsmål"
        assert len(svar) > 200, (
            f"«{situation[:50]}…» har et for kort modelsvar — koblingen skal "
            "vises, ikke bare påstås")


# --- Forsvar dit valg ------------------------------------------------------

def test_valg_har_alternativ_modspoergsmaal_og_forsvar():
    for valg, alt, modspm, forsvar in VALG:
        assert alt, f"«{valg[:50]}…» mangler et alternativ at holde op mod"
        assert modspm, f"«{valg[:50]}…» mangler modspørgsmål"
        assert len(forsvar) > 150, f"«{valg[:50]}…» har et for tyndt forsvar"


# --- Kildekritik -----------------------------------------------------------

def test_paastande_har_forklaring():
    for p, holder, fejltype, forklaring, fag in PAASTANDE:
        assert len(forklaring) > 80, f"«{p[:50]}…» har for tynd forklaring"
        assert fag in KENDTE_FAG, f"«{p[:50]}…» har ukendt fag «{fag}»"


def test_falske_paastande_har_en_fejltype():
    """Uden fejltype lærer man ikke at genkende mønstret næste gang."""
    for p, holder, fejltype, _forkl, _fag in PAASTANDE:
        if not holder:
            assert fejltype, f"«{p[:50]}…» er falsk, men fejltypen mangler"


def test_sande_paastande_har_ingen_fejltype():
    for p, holder, fejltype, _forkl, _fag in PAASTANDE:
        if holder:
            assert fejltype is None, (
                f"«{p[:50]}…» er markeret sand, men har en fejltype")


def test_der_er_baade_sande_og_falske_paastande():
    """Er alle falske, træner tilstanden mistro i stedet for vurdering."""
    sande = sum(1 for p in PAASTANDE if p[1])
    assert sande >= 3, f"kun {sande} sande påstande — så lærer man bare at sige nej"
    assert sande < len(PAASTANDE), "der skal også være fejl at fange"


# --- Fælles for alle nye banker -------------------------------------------

@pytest.mark.parametrize("navn", FORBUDTE_NAVNE)
def test_ingen_virksomhedsnavne_i_de_nye_banker(navn):
    tekst = _al_tekst(
        [_al_tekst(k) for k in KOBLINGER],
        [_al_tekst(v) for v in VALG],
        [_al_tekst([x for x in p if isinstance(x, str)]) for p in PAASTANDE],
    ).lower()
    # Ordgrænser, ikke delstrenge: korte forkortelser som «DSV» rammer ellers
    # midt inde i almindelige ord (sæsonud-sv-ing) og giver falsk alarm.
    mønster = r"\b" + re.escape(navn.lower()) + r"\b"
    assert not re.search(mønster, tekst), (
        f"virksomhedsnavnet «{navn}» står i en af de nye banker — "
        "værktøjet skal formuleres neutralt")


def test_bankerne_er_ikke_tomme():
    assert len(KOBLINGER) >= 6
    assert len(VALG) >= 5
    assert len(PAASTANDE) >= 12


# --- 3. semesters spørgsmålsbank -------------------------------------------
from pakke_3sem import KONCEPT_3SEM  # noqa: E402

FELTER = {"fag", "emne", "sp", "type", "svar", "alt", "fisker", "soeg"}


def test_3sem_poster_har_praecis_de_forventede_felter():
    """Bankerne flettes ind i KONCEPT, så formatet skal matche præcist —
    et manglende felt fejler først, når spørgsmålet trækkes i træneren."""
    for q in KONCEPT_3SEM:
        assert set(q) == FELTER, (
            f"«{q.get('emne', '?')}» har felterne {sorted(set(q))}, "
            f"forventede {sorted(FELTER)}")


def test_3sem_daekker_begge_de_manglende_fag():
    fag = {q["fag"] for q in KONCEPT_3SEM}
    assert "Distribution" in fag and "Projektstyring" in fag


def test_3sem_argumentspoergsmaal_har_et_modsvar():
    """type='argument' betyder flere forsvarlige svar — uden 'alt' er kortet
    bare et almindeligt spørgsmål med en forkert etiket."""
    for q in KONCEPT_3SEM:
        if q["type"] == "argument":
            assert q["alt"].strip(), f"«{q['emne']}» er argument-type uden alt"
        else:
            assert q["type"] == "rigtigt", f"«{q['emne']}» har ukendt type"
            assert not q["alt"], f"«{q['emne']}» er 'rigtigt', men har alt"


def test_3sem_har_fyldestgoerende_svar():
    for q in KONCEPT_3SEM:
        assert len(q["svar"]) > 300, f"«{q['emne']}» har for kort svar"
        assert q["fisker"], f"«{q['emne']}» mangler 'hvad eksaminator fisker efter'"
        assert q["soeg"], f"«{q['emne']}» mangler søgeord"


def test_3sem_ingen_dublerede_emner():
    emner = [q["emne"] for q in KONCEPT_3SEM]
    dub = {e for e in emner if emner.count(e) > 1}
    assert not dub, f"samme emne flere gange: {dub}"


@pytest.mark.parametrize("navn", FORBUDTE_NAVNE)
def test_3sem_har_ingen_virksomhedsnavne(navn):
    tekst = " ".join(q["sp"] + q["svar"] + q["alt"] + q["fisker"]
                     for q in KONCEPT_3SEM).lower()
    mønster = r"\b" + re.escape(navn.lower()) + r"\b"
    assert not re.search(mønster, tekst), f"virksomhedsnavnet «{navn}» står i banken"


def test_3sem_daekning_staar_maal_med_ects():
    """Vagthund på selve formålet: Distribution vejer 7 ECTS og skal have
    mest. Falder den, er banken skævvredet igen."""
    dist = sum(1 for q in KONCEPT_3SEM if q["fag"] == "Distribution")
    proj = sum(1 for q in KONCEPT_3SEM if q["fag"] == "Projektstyring")
    assert dist >= 15, f"kun {dist} Distribution-spørgsmål — faget vejer 7 ECTS"
    assert proj >= 8, f"kun {proj} Projektstyring-spørgsmål — faget vejer 4 ECTS"


# --- 3. semesters kæder og argument-cases ----------------------------------
from pakke_3sem import KAEDER_3SEM, ARGUMENTER_3SEM  # noqa: E402


def test_kaeder_har_den_forventede_struktur():
    """Kæderne flettes ind i KÆDER, så hvert lag skal have alle felter —
    et manglende felt fejler først, når laget trækkes i drillen."""
    lag_felter = {"sp", "arg", "fisker", "alt", "snyd", "fakta"}
    for k in KAEDER_3SEM:
        assert {"emne", "fag", "lag"} <= set(k), f"kæde mangler felt: {k.get('emne')}"
        assert k["lag"], f"«{k['emne']}» har ingen lag"
        for i, L in enumerate(k["lag"]):
            assert set(L) == lag_felter, (
                f"«{k['emne']}» lag {i + 1} har {sorted(set(L))}")
            assert isinstance(L["snyd"], bool) and isinstance(L["fakta"], bool)


def test_kaeder_starter_med_et_faktalag():
    """Drillen borer lag for lag — første lag skal etablere definitionen,
    ellers spørges der i dybden om noget, der ikke er defineret."""
    for k in KAEDER_3SEM:
        assert k["lag"][0]["fakta"] is True, (
            f"«{k['emne']}» starter ikke med et faktalag")


def test_hver_kaede_har_mindst_en_faelde():
    """Fælde-jagt trækker netop de lag, hvor præmissen er forkert."""
    for k in KAEDER_3SEM:
        assert any(L["snyd"] for L in k["lag"]), (
            f"«{k['emne']}» har ingen fælde-lag")


def test_argumentcases_har_flere_forsvarlige_positioner():
    for a in ARGUMENTER_3SEM:
        assert {"fag", "situation", "spm", "positioner", "pointe"} <= set(a)
        assert len(a["positioner"]) >= 2, (
            f"«{a['spm'][:40]}…» har kun én position — så er det ikke en argument-case")
        for pos in a["positioner"]:
            assert pos["navn"] and len(pos["arg"]) > 150


def test_3sem_kaeder_og_argumenter_daekker_de_nye_fag():
    fag = {k["fag"] for k in KAEDER_3SEM} | {a["fag"] for a in ARGUMENTER_3SEM}
    assert "Distribution" in fag and "Projektstyring" in fag
