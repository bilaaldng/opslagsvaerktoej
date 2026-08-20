"""Ordbogen — ét opslag pr. begreb, på tværs af fagene.

Resten af værktøjet er skåret efter fag. Den her side er skåret efter
BEGREB, fordi 3. semester prøves tværfagligt: fire fag afgøres i én prøve,
og casen kræver, at de kobles på det samme flow.

Hvert opslag svarer på fire ting:
  * hvad betyder ordet (og betyder det noget forskelligt i forskellige fag)
  * HVOR undervises der i det — med klik direkte til modulet
  * hvornår holder begrebet IKKE
  * hvad hænger sammen med det

Filtret «kun begreber i flere fag» er sidens egentlige pointe: det er dér,
koblingerne til den tværfaglige prøve ligger.
"""
import os
import re
import sys

import streamlit as st

st.set_page_config(page_title="Ordbog — Opslagsværktøj", page_icon="📖",
                   layout="wide")

_ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _ROD)
from ui_theme import inject_css, FAGFARVER          # noqa: E402
from data.index import SIDER                        # noqa: E402
from data.ordbog import BEGREBER, slaa_op           # noqa: E402

inject_css()

# Fag → sidesti, så «hvor mødes begrebet» kan hoppe det rigtige sted hen
STI_FOR_FAG = dict(SIDER)

st.title("📖 Ordbog")
st.caption(
    "Begreberne på tværs af fagene. Samme ord betyder ikke altid det samme — "
    "og et begreb hører sjældent til i kun ét fag. Klik et fag-link for at "
    "hoppe direkte til det modul, der underviser i begrebet."
)


def _norm(s: str) -> str:
    """Tolerant sammenligning: små bogstaver og æ/ø/å skrevet på begge måder,
    så «stoej» også rammer «støj» (samme greb som den globale søgning)."""
    s = (s or "").lower()
    for a, b in (("æ", "ae"), ("ø", "oe"), ("å", "aa")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def _søgetekst(b: dict) -> str:
    dele = [b["begreb"], b.get("kort") or "", b.get("engelsk") or "",
            b.get("holder_ikke") or "", " ".join(b.get("soeg", [])),
            " ".join(f"{k} {v}" for k, v in b.get("betydninger", []))]
    return _norm(" ".join(dele))


# --- Indgang udefra: forsiden/søgningen sender begrebet i goto_modul -------
_ind = st.session_state.pop("goto_modul", None)
if _ind:
    st.session_state["ord_soeg"] = _ind

# --- Filtre ----------------------------------------------------------------
f1, f2, f3 = st.columns([3, 2, 2])
with f1:
    soeg = st.text_input(
        "Søg (fx 'lean', 'kanban', 'perfektion', 'ansvarsgrænse')",
        key="ord_soeg",
        help="Søger i navn, definition, engelsk term, betydninger og nøgleord. "
             "Æ/ø/å må skrives som ae/oe/aa.",
    )
with f2:
    fag_valg = st.selectbox(
        "Fag", ["Alle fag"] + [f for f, _ in SIDER if f != "Forsvarstræner"],
        key="ord_fag",
        help="Vis kun begreber, der hører til dette fag — også når de "
             "samtidig hører til andre.",
    )
with f3:
    kun_tvaer = st.toggle(
        "Kun begreber i flere fag", key="ord_tvaer",
        help="Det er her koblingerne til den tværfaglige prøve ligger.",
    )

q = _norm(soeg)
vist = [b for b in BEGREBER
        if (not q or q in _søgetekst(b))
        and (fag_valg == "Alle fag" or fag_valg in b["fag"])
        and (not kun_tvaer or len(b["fag"]) > 1)]

tvaer_i_alt = sum(1 for b in BEGREBER if len(b["fag"]) > 1)
st.caption(f"**{len(vist)}** af {len(BEGREBER)} begreber vist · "
           f"{tvaer_i_alt} af dem lever i flere fag")

if not vist:
    st.info("Ingen begreber matchede. Prøv et bredere ord, eller ryd filtrene.")
    st.stop()


def _fag_chips(fag: list) -> str:
    """Fag-mærkater i fagets egen accentfarve — samme farver som forsiden."""
    ud = []
    for f in fag:
        c = FAGFARVER.get(f, "#64748b")
        ud.append(
            f'<span class="ord-chip" style="--c:{c}">{f}</span>'
        )
    return '<div class="ord-chips">' + "".join(ud) + "</div>"


def _gaa_til(fag: str, modul: str) -> None:
    """Hop til det modul, der underviser i begrebet — samme konvention som
    forsiden bruger (goto_modul + switch_page).

    NB: kaldes fra scriptets normale forløb, IKKE fra en on_click-callback.
    Streamlit må ikke skifte side inde i en callback ("Calling st.rerun()
    within a callback is a no-op"), så knappen aflæses på sin returværdi —
    præcis som Hjem.py gør det.
    """
    sti = STI_FOR_FAG.get(fag)
    if not sti:
        return
    st.session_state["goto_modul"] = modul
    st.switch_page(sti)


def _slå_op(navn: str) -> None:
    """«Se også» → sæt søgefeltet til begrebet og bliv på siden."""
    st.session_state["ord_soeg"] = navn
    st.session_state["ord_fag"] = "Alle fag"
    st.session_state["ord_tvaer"] = False


for b in vist:
    tvaer = " · ".join(b["fag"]) if len(b["fag"]) > 1 else b["fag"][0] if b["fag"] else "—"
    titel = b["begreb"] + (f"  ·  {tvaer}" if len(b["fag"]) > 1 else "")
    with st.expander(titel, expanded=bool(q) and len(vist) <= 8):
        if b.get("engelsk"):
            st.caption(f"På engelsk: **{b['engelsk']}** — en væsentlig del af "
                       "litteraturen er engelsk, så termen skal sidde på begge sprog.")
        st.markdown(_fag_chips(b["fag"]), unsafe_allow_html=True)

        if b.get("kort"):
            st.markdown(b["kort"])

        # Samme ord, forskellig betydning alt efter fag — sidens vigtigste fund
        if b.get("betydninger"):
            st.markdown("**Betyder ikke det samme overalt:**")
            for sammenhæng, forklaring in b["betydninger"]:
                st.markdown(f"- **{sammenhæng}:** {forklaring}")

        if b.get("hvor"):
            st.markdown("**Hvor mødes begrebet:**")
            kols = st.columns(min(len(b["hvor"]), 3))
            for i, (fag, modul) in enumerate(b["hvor"]):
                with kols[i % len(kols)]:
                    if st.button(
                        f"{fag} › {modul}",
                        key=f"hvor_{b['begreb']}_{fag}_{modul}",
                        width="stretch",
                    ):
                        _gaa_til(fag, modul)

        if b.get("holder_ikke"):
            st.markdown("**Hvornår holder det ikke:**")
            st.warning(b["holder_ikke"])

        if b.get("se_ogsaa"):
            st.markdown("**Se også:**")
            kols = st.columns(min(len(b["se_ogsaa"]), 4))
            for i, navn in enumerate(b["se_ogsaa"]):
                mål = slaa_op(navn)
                if not mål:
                    continue
                with kols[i % len(kols)]:
                    st.button(navn, key=f"se_{b['begreb']}_{navn}",
                              width="stretch",
                              on_click=_slå_op, args=(mål["begreb"],))

st.divider()
st.caption(
    "Ordbogen er bygget oven på faktakortene i Forsvarstræneren, så et begreb "
    "kun står ét sted. Mangler et begreb et fag eller et link, rettes det i "
    "`data/ordbog.py` under BERIGELSER."
)
