"""Øvelserne virker uden profil, registrering eller selvevaluering."""
from pathlib import Path
import sys

import pytest
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


@pytest.fixture
def app():
    return AppTest.from_file(str(ROOT / "pages/7_Forsvarstræner.py"), default_timeout=30)


def start(app, mode):
    app.session_state["forsvar_modul"] = mode
    app.run()
    assert not app.exception
    assert app.pills(key="forsvar_modul").value == mode
    return app


def click(app, label):
    next(b for b in app.button if b.label == label).click().run()
    assert not app.exception


def assert_no_progress_ui(app):
    assert not app.metric
    assert "Hvor står jeg" not in app.pills(key="forsvar_modul").options
    labels = [b.label for b in app.button] + [b.label for b in app.checkbox]
    forbidden = ("Kunne den", "Svær — igen senere", "Kun de svære", "svaghedsprofil",
                 "svage emner", "backup", "Nulstil denne profil", "Skal øves igen")
    assert not [label for label in labels if any(term in label for term in forbidden)]
    assert not app.get("download_button")
    assert not app.file_uploader


def test_old_progress_module_falls_back_to_an_exercise(app):
    app.session_state["forsvar_modul"] = "Hvor står jeg"
    app.run()
    assert not app.exception
    assert app.pills(key="forsvar_modul").value == "Eksaminér mig"
    assert_no_progress_ui(app)


@pytest.mark.parametrize("mode,draw,key,show_key", [
    ("Eksaminér mig", "🎲 Stil mig et spørgsmål", "ex_cur", "ex_show"),
    ("Fælde-jagt", "🪤 Stil mig et fælde-spørgsmål", "fj_cur", "fj_show"),
])
def test_question_reveal_and_next_need_no_rating(app, mode, draw, key, show_key):
    start(app, mode)
    click(app, draw)
    first = app.session_state[key]
    assert app.session_state.filtered_state.get(show_key, False) is False
    click(app, "👁️ Vis svar")
    assert app.session_state[show_key] is True
    assert_no_progress_ui(app)
    click(app, "Næste spørgsmål →")
    assert app.session_state[key] != first
    assert app.session_state[show_key] is False


def test_calculation_keeps_direct_feedback_without_scores(app):
    start(app, "Regn")
    answer = app.session_state["rt_opg"]["svar"]
    app.text_input(key="rt_svar").input(str(answer + 100000000))
    click(app, "✅ Tjek svar")
    assert any("Ikke helt" in e.value for e in app.error)
    app.text_input(key="rt_svar").input(str(answer))
    click(app, "✅ Tjek svar")
    assert any("Rigtigt!" in e.value for e in app.success)
    assert any("Udregning:" in e.value for e in app.markdown)
    assert_no_progress_ui(app)
    click(app, "🎲 Ny opgave")
    assert not app.session_state["rt_facit"]
    click(app, "👁️ Vis facit")
    assert any("Facit:" in e.value for e in app.info)
    assert_no_progress_ui(app)


def test_fact_card_flips_and_moves_without_a_rating(app):
    start(app, "Faktatjek")
    first_position = app.session_state["fc_pos"]
    click(app, "🔄 Vend kort")
    assert app.session_state["fc_show"] is True
    assert app.success
    assert_no_progress_ui(app)
    click(app, "➡️ Næste")
    assert app.session_state["fc_pos"] == first_position + 1
    assert app.session_state["fc_show"] is False


def test_practice_exam_finishes_by_navigation_without_scoring(app):
    start(app, "Prøveeksamen")
    click(app, "▶️ Start prøveeksamen")
    count = len(app.session_state["sim_qs"])
    assert count == 10
    for index in range(count):
        assert app.session_state["sim_i"] == index
        assert not app.session_state["sim_show"]
        click(app, "👁️ Vis svar")
        assert app.session_state["sim_show"] is True
        assert_no_progress_ui(app)
        click(app, "Næste spørgsmål →")
    assert any("prøveeksamen er slut" in m.value for m in app.markdown)
    assert_no_progress_ui(app)
    click(app, "↺ Ny prøveeksamen")
    assert app.session_state["sim_i"] == 0


def test_defense_finishes_without_phase_ratings_or_history(app):
    start(app, "30-min forsvaret")
    click(app, "▶️ Start forsvaret")
    for index in range(4):
        assert app.session_state["fs_fase"] == index
        click(app, "Næste fase →")
    assert any("Forsvaret er slut" in m.value for m in app.markdown)
    assert not app.checkbox
    assert_no_progress_ui(app)
    click(app, "↺ Nyt forsvar")
    assert app.session_state["fs_fase"] == 0
