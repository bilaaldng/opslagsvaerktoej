"""Hvert modul på hver fagside skal kunne renderes uden at kaste en fejl.

Baggrund: siderne brugte før faneblade, hvor ALT indhold blev kørt ved hvert
klik. Nu køres kun det valgte modul. Det er hurtigere, men det betyder også
at en fejl i et sjældent brugt modul ikke længere opdages ved at åbne siden —
kun ved at klikke præcis derind. Derfor klikker denne test dem alle igennem.

Kører langsomt (hvert modul startes som sin egen app). Spring den over med:
    pytest -m "not langsom"
"""
import ast
import contextlib
import io
import os
import sys
import warnings

import pytest

ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROD)
warnings.filterwarnings("ignore")

from data.index import SIDER  # noqa: E402


def _vaelger(sti: str):
    """(MODULER, session-nøglen som st.pills bruger) læst uden at køre siden."""
    tree = ast.parse(io.open(os.path.join(ROD, sti), encoding="utf-8").read())
    moduler, key = [], None
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and any(getattr(t, "id", "") == "MODULER" for t in n.targets):
            moduler = [e.value for e in n.value.elts]
        if isinstance(n, ast.Call) and getattr(n.func, "attr", "") == "pills":
            for kw in n.keywords:
                if kw.arg == "key":
                    key = kw.value.value
    return moduler, key


PAR = [(fag, sti, m)
       for fag, sti in SIDER
       for m in (_vaelger(sti)[0] or [])]


@pytest.mark.langsom
@pytest.mark.parametrize("fag,sti,modul", PAR, ids=[f"{f}-{m}" for f, _s, m in PAR])
def test_modul_renderer_uden_fejl(fag, sti, modul):
    from streamlit.testing.v1 import AppTest

    _mods, key = _vaelger(sti)
    stoej = io.StringIO()
    with contextlib.redirect_stderr(stoej), contextlib.redirect_stdout(stoej):
        at = AppTest.from_file(os.path.join(ROD, sti), default_timeout=120)
        at.session_state[key] = modul
        at.run()

    # st.page_link virker ikke i testværktøjet (kræver sidekontekst) — den
    # ene fejl er en begrænsning i harnesset, ikke i appen.
    ægte = [e for e in at.exception if "url_pathname" not in (e.value or "")]
    assert not ægte, f"«{fag} / {modul}» fejler: {[e.value for e in ægte][:1]}"
    if fag == "Forsvarstræner":
        assert at.pills(key=key).value == modul
        assert len(at.subheader) > 0
