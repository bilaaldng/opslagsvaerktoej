"""Ordbogen — at den hænger sammen med fagsiderne.

Ordbogens hele pointe er, at et begreb kan høre til flere fag og pege videre
til de moduler, der underviser i det. De links er præcis den slags, der
fejler tavst i appen: modulet bliver omdøbt, og knappen lander ingen steder.
Her fejler det højlydt i stedet.
"""
import os
import sys

import pytest

ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROD)

from data.index import SIDER, moduler_paa  # noqa: E402
from data.ordbog import BEGREBER, FAGREGLER, slaa_op  # noqa: E402
from ui_theme import FAGFARVER  # noqa: E402

GYLDIGE_MODULER = {(fag, m) for fag, sti in SIDER for m in moduler_paa(sti)}
KENDTE_FAG = {fag for fag, _ in FAGREGLER}


def test_hvert_hvor_link_rammer_et_rigtigt_modul():
    """«Hvor mødes begrebet» skal lande på et modul der faktisk findes."""
    for b in BEGREBER:
        for fag, modul in b["hvor"]:
            assert (fag, modul) in GYLDIGE_MODULER, (
                f"«{b['begreb']}» linker til «{fag} › {modul}», men det modul "
                f"findes ikke. Kendte moduler på {fag}: "
                f"{sorted(m for f, m in GYLDIGE_MODULER if f == fag)}")


def test_hvor_link_matcher_begrebets_egne_fag():
    """Peger et begreb ind i et fag, skal faget også stå på begrebet —
    ellers viser kortet et link til et fag, det påstår ikke at høre til."""
    for b in BEGREBER:
        for fag, _modul in b["hvor"]:
            assert fag in b["fag"], (
                f"«{b['begreb']}» linker til {fag}, men har kun "
                f"fagene {b['fag']}")


def test_alle_fag_er_kendte():
    for b in BEGREBER:
        for fag in b["fag"]:
            assert fag in KENDTE_FAG, f"«{b['begreb']}» har ukendt fag «{fag}»"


def test_hvert_begreb_har_mindst_et_fag():
    """Et begreb uden fag kan hverken filtreres eller findes via fag."""
    uden = [b["begreb"] for b in BEGREBER if not b["fag"]]
    assert not uden, f"begreber uden fag: {uden}"


def test_hvert_fag_har_en_farve():
    """Fag-mærkaterne farves efter fag — et fag uden farve bliver grå."""
    for b in BEGREBER:
        for fag in b["fag"]:
            assert fag in FAGFARVER, f"{fag} mangler en accentfarve i FAGFARVER"


def test_se_ogsaa_peger_paa_begreber_der_findes():
    """Et «se også» der ikke kan slås op, bliver til en knap der intet gør."""
    for b in BEGREBER:
        for navn in b["se_ogsaa"]:
            assert slaa_op(navn) is not None, (
                f"«{b['begreb']}» henviser til «{navn}», som ikke findes "
                "i ordbogen")


def test_se_ogsaa_peger_ikke_paa_sig_selv():
    for b in BEGREBER:
        for navn in b["se_ogsaa"]:
            assert slaa_op(navn)["begreb"] != b["begreb"], (
                f"«{b['begreb']}» henviser til sig selv")


def test_ingen_dublerede_begreber():
    navne = [b["begreb"] for b in BEGREBER]
    dubletter = {n for n in navne if navne.count(n) > 1}
    assert not dubletter, f"samme begreb står flere gange: {dubletter}"


def test_begreber_med_flere_betydninger_har_ogsaa_flere_fag():
    """Har et ord to betydninger, er det fordi to fag bruger det forskelligt —
    fx kanban som træk-signal og kanban som opgavetavle."""
    for b in BEGREBER:
        if b["betydninger"]:
            assert len(b["fag"]) > 1, (
                f"«{b['begreb']}» har flere betydninger, men kun ét fag")


def test_kanban_findes_i_baade_distribution_og_projektstyring():
    """Vagthund på sidens vigtigste fund: samme ord, to fag, to betydninger.
    Falder den, er ordbogens grundpræmis holdt op med at være dækket."""
    kanban = slaa_op("Kanban")
    assert kanban is not None, "Kanban mangler i ordbogen"
    assert "Distribution" in kanban["fag"] and "Projektstyring" in kanban["fag"]
    assert len(kanban["betydninger"]) >= 2, (
        "Kanban skal beskrive både træk-signalet og opgavetavlen")


def test_lean_findes_i_baade_produktion_og_distribution():
    """Det hul der startede det hele: søgning på lean pegede kun ét sted."""
    lean = slaa_op("Lean")
    assert lean is not None
    assert {"Produktion", "Distribution"} <= set(lean["fag"])


def test_de_fem_lean_principper_er_med():
    """«perfektion» gav nul hits i hele kodebasen, før ordbogen kom."""
    p = slaa_op("De 5 Lean-principper")
    assert p is not None, "de 5 Lean-principper mangler"
    tekst = p["kort"].lower()
    for ord_ in ("værdi", "værdistrøm", "flow", "pull", "perfektion"):
        assert ord_ in tekst, f"princippet «{ord_}» mangler i beskrivelsen"


def test_ordbogen_er_ikke_skrumpet():
    """Vagthund: ordbogen bygges oven på faktakortene, så et fald i antal
    betyder at en kilde er holdt op med at svare — ikke at der er ryddet op."""
    assert len(BEGREBER) >= 115, (
        f"kun {len(BEGREBER)} begreber — læses faktakortene stadig?")


def test_der_er_reelt_tvaerfaglige_begreber():
    """Uden begreber i flere fag er ordbogen bare en anden fag-opdeling."""
    tvaer = [b for b in BEGREBER if len(b["fag"]) > 1]
    assert len(tvaer) >= 25, (
        f"kun {len(tvaer)} begreber i flere fag — fag-afledningen er "
        "sandsynligvis faldet tilbage til ét fag pr. begreb")


@pytest.mark.parametrize("felt", ["begreb", "fag", "soeg", "se_ogsaa",
                                  "betydninger", "hvor"])
def test_alle_poster_har_de_forventede_felter(felt):
    for b in BEGREBER:
        assert felt in b, f"«{b.get('begreb', '?')}» mangler feltet «{felt}»"
