"""Sammenhængen mellem søgeindekset og fagsiderne.

Det her er testen der fanger den fejltype man ellers først opdager når man
sidder til eksamen: et deep-link der peger på et modul som er blevet
omdøbt eller slettet. Den fejler tavst i appen — men ikke her.
"""
import os
import sys

import pytest

ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROD)

from data.index import INDEKS, SIDER, moduler_paa  # noqa: E402
from ui_theme import FAGFARVER  # noqa: E402


def test_alle_sidestier_findes():
    for fag, titel, sti, _modul, _ord in INDEKS:
        assert os.path.exists(os.path.join(ROD, sti)), f"{fag}/{titel} peger på {sti}"


def test_deeplinks_matcher_et_rigtigt_modul():
    """Hvert opslag med deep-link skal ramme et modul der faktisk findes."""
    for fag, titel, sti, modul, _ord in INDEKS:
        if modul is None:
            continue
        if fag == "Ordbog":
            # Ordbogen har ingen modulvælger — dens deep-link bærer et
            # BEGREB, ikke et modulnavn. At begrebet findes, og at dets egne
            # «hvor»-links peger på rigtige moduler, testes i test_ordbog.py.
            continue
        mods = moduler_paa(sti)
        assert modul in mods, (
            f"«{fag} / {titel}» deep-linker til modulet «{modul}», "
            f"men {os.path.basename(sti)} har kun: {mods}")


def test_alle_moduler_kan_findes_i_soegningen():
    """Tilføjes et modul på en fagside, skal det dukke op i indekset."""
    dækket = {(sti, modul) for _f, _t, sti, modul, _o in INDEKS if modul}
    for fag, sti in SIDER:
        for m in moduler_paa(sti):
            assert (sti, m) in dækket, f"modulet «{m}» på {fag} mangler i indekset"


def test_ingen_dublerede_modulnavne_paa_samme_side():
    for fag, sti in SIDER:
        mods = moduler_paa(sti)
        assert len(mods) == len(set(mods)), f"{fag} har to moduler med samme navn"


def test_hvert_fag_har_en_farve():
    for fag, _sti in SIDER:
        assert fag in FAGFARVER, f"{fag} mangler en accentfarve i FAGFARVER"


def test_indekset_er_ikke_skrumpet():
    """Vagthund: indekset er bygget ud fra siderne, så et fald i antal
    betyder at noget er faldet ud — ikke at der er ryddet op."""
    assert len(INDEKS) >= 95, f"kun {len(INDEKS)} opslag — er en kilde holdt op med at svare?"


@pytest.mark.parametrize("fag,sti", SIDER)
def test_hver_side_har_enten_moduler_eller_er_kendt_uden(fag, sti):
    from data.index import UDEN_MODULER
    assert moduler_paa(sti) or fag in UDEN_MODULER, (
        f"{fag} har hverken MODULER eller står i UDEN_MODULER — "
        "så kan søgningen ikke ramme den")
