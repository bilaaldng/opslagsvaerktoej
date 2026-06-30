"""Mørk slate-tema — fælles UI-styling for alle sider.

inject_css(): indlæser theme.css (rolig mørk baggrund, taktile kort, smooth
  hover/klik/fokus) og injicerer den. Kald øverst på hver side (efter
  set_page_config). Selve stilen ligger i theme.css ved siden af denne fil,
  så CSS og Python holdes adskilt og let at redigere.
style_fig(fig): gør Plotly-grafer transparente og lyse, så de smelter ind.
Farvepalet eksporteres som konstanter, så grafer er ens på tværs af moduler.
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

_CSS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "theme.css")


def inject_css() -> None:
    """Indlæs slate-temaet fra theme.css. Kald øverst på hver side."""
    try:
        with open(_CSS_PATH, encoding="utf-8") as f:
            css = f.read()
    except OSError:
        css = ""  # uden tema er appen stadig fuldt funktionel
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def style_fig(fig):
    """Giv en Plotly-figur slate-look: transparent bund, lys skrift, svagt gitter."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=C_FONT),
        legend=dict(font=dict(color=C_FONT)),
        hoverlabel=dict(bgcolor="#1e293b", font_color="#e2e8f0"),
    )
    fig.update_xaxes(gridcolor=C_GRID, zeroline=False, linecolor=C_GRID)
    fig.update_yaxes(gridcolor=C_GRID, zeroline=False, linecolor=C_GRID)
    return fig
