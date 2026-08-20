"""Mørk slate-tema — fælles UI-styling for alle sider.

inject_css(): indlæser theme.css (rolig mørk baggrund, taktile kort, smooth
  hover/klik/fokus) og injicerer den. Kald øverst på hver side (efter
  set_page_config). Selve stilen ligger i theme.css ved siden af denne fil,
  så CSS og Python holdes adskilt og let at redigere. Læsningen caches på
  filens ændringstid, så disken ikke rammes ved hvert rerun.
style_fig(fig): gør Plotly-grafer transparente og lyse, så de smelter ind —
  og sætter DANSK talformat på akser/hover (komma-decimal, punktum-tusind),
  fælles colorway og samme skrifttype som resten af appen.
Farvepalet eksporteres som konstanter, så grafer er ens på tværs af moduler.
FAGFARVER: én accentfarve pr. fag — bruges til kort/badges på forsiden.
"""
import os

import streamlit as st

# Slate-palet (rolig, professionel, mørk)
C_TOTAL = "#3b82f6"   # blå    — hovedlinje
C_ORDER = "#f59e0b"   # amber
C_HOLD = "#10b981"    # emerald
C_OPT = "#ef4444"     # rød    — optimum/markør
C_A, C_B, C_C = "#ef4444", "#f59e0b", "#10b981"   # ABC: rød / amber / grøn
C_MUTED = "#64748b"
C_FONT = "#cbd5e1"
C_GRID = "rgba(148,163,184,0.14)"

# Samme skrift i graferne som i resten af appen (fallback til system)
FONT_STACK = ('"Familjen Grotesk", -apple-system, BlinkMacSystemFont, '
              '"Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif')

# Én accentfarve pr. fag — genkendelighed på tværs (kort, badges, striber)
FAGFARVER = {
    "Værdikædeanalyse": "#818cf8",   # indigo  — rammen om det hele
    "Indkøb":           "#f59e0b",   # amber
    "Produktion":       "#22d3ee",   # cyan
    "Statistik":        "#60a5fa",   # blå
    "Økonomi":          "#34d399",   # emerald
    "Organisation":     "#a78bfa",   # violet
    "Kommunikation":    "#fb7185",   # rosa
    "Jura":             "#eab308",   # gylden — vægtskålen
    "Distribution":     "#fb923c",   # orange — lastbilen
    "Forsvarstræner":   "#e879f9",   # fuchsia — eksamensdagen
    "Projektstyring":   "#2dd4bf",   # teal   — planen og holdet
    "Ordbog":           "#94a3b8",   # slate  — neutral, den står uden for fagene
}

_CSS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "theme.css")


@st.cache_data(show_spinner=False)
def _laes_css(sti: str, mtime: float) -> str:
    """Læs theme.css én gang pr. version af filen (mtime = cache-nøgle)."""
    try:
        with open(sti, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""  # uden tema er appen stadig fuldt funktionel


def inject_css() -> None:
    """Indlæs slate-temaet fra theme.css. Kald øverst på hver side."""
    try:
        mtime = os.path.getmtime(_CSS_PATH)
    except OSError:
        mtime = 0.0
    css = _laes_css(_CSS_PATH, mtime)
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def style_fig(fig):
    """Giv en Plotly-figur slate-look: transparent bund, lys skrift, svagt
    gitter — og dansk talformat (1.234,5) så akserne matcher num()/kr()."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=C_FONT, family=FONT_STACK),
        legend=dict(font=dict(color=C_FONT)),
        hoverlabel=dict(
            bgcolor="#1e293b", font_color="#e2e8f0",
            bordercolor="rgba(96,165,250,0.4)",
            font=dict(family=FONT_STACK),
        ),
        separators=",.",   # dansk: komma-decimal, punktum-tusind
        colorway=[C_TOTAL, C_ORDER, C_HOLD, C_OPT, C_MUTED],
        margin=dict(t=48, r=16, b=44, l=56),
    )
    fig.update_xaxes(gridcolor=C_GRID, zeroline=False, linecolor=C_GRID)
    fig.update_yaxes(gridcolor=C_GRID, zeroline=False, linecolor=C_GRID)
    return fig


def vis_fig(fig) -> None:
    """Vis en styled figur uden Plotly-værktøjslinje: ét kald i stedet for
    st.plotly_chart(style_fig(fig), ...) — brug den til nye grafer."""
    st.plotly_chart(
        style_fig(fig),
        width="stretch",
        config={"displayModeBar": False},
    )
