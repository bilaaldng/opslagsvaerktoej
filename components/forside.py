"""3D-forsiden — bygget som rigtig HTML/WebGL i stedet for Streamlit-kort.

Hvorfor ikke bare Streamlit-widgets: Streamlits egne komponenter kan males om
med CSS, men formen er deres. Her tegnes forsiden fra bunden med Three.js, så
den kan have dybde, parallakse og partikler. Fagsiderne er stadig Streamlit.

TRE TING SER MÆRKELIGE UD OG ER DET IKKE — Streamlit indlejrer os i en
`about:srcdoc`-ramme, og det giver tre fælder som hver har sin løsning:

1. `import()` af three.js virker ikke (srcdoc har ingen adresse at opløse
   relative stier mod). `fetch()` virker. Derfor hentes bibliotekets to filer
   manuelt, kernen får en blob-adresse, og skallens ene relative henvisning
   skrives om til den. Se hentThree().

2. Rammen må ikke navigere den omgivende side (sandkassen mangler
   allow-top-navigation). Men allow-same-origin ER sat, så vi kan nå den
   omgivende sides DOM og klikke på Streamlits *eget* link. Se gaaTil().

3. Rammen har fast højde. Vi sætter den selv via window.frameElement, som er
   tilgængelig af samme grund som punkt 2. Se saetHoejde().
"""
import json
import os

import streamlit.components.v1 as components

# Ikonstreger (Lucide, MIT) — indlejret som SVG i stedet for emoji, så de
# arver farven og ser ens ud på Mac, Windows og telefon.
IKONER = {
    "Værdikædeanalyse": "M3 12h4l3-8 4 16 3-8h4",
    "Indkøb": "M3 5h2l2 11h10l2-7H7M9 20h.01M17 20h.01",
    "Produktion": "M3 20V9l5 3V9l5 3V9l5 3v8z",
    "Statistik": "M4 19V5m0 14h16M8 16v-5m4 5V8m4 8v-3",
    "Økonomi": "M12 2v20M17 6H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6",
    "Organisation": "M12 3l8 4.5v9L12 21l-8-4.5v-9z M12 12l8-4.5M12 12v9M12 12L4 7.5",
    "Kommunikation": "M21 12a8 8 0 0 1-11.5 7.2L3 21l1.8-6.5A8 8 0 1 1 21 12z",
    "Jura": "M12 3v18M5 7h14M7 7l-3 7h6zM17 7l-3 7h6z",
    "Distribution": "M3 7h11v9H3zM14 10h4l3 3v3h-7zM7 19h.01M18 19h.01",
    "Forsvarstræner": "M22 9L12 4 2 9l10 5zM6 12v5c0 1.5 3 3 6 3s6-1.5 6-3v-5",
    "Projektstyring": "M3 4h18v16H3zM9 4v16M15 4v16M5 8h2M11 8h2M17 8h2",
    "Ordbog": "M12 6v14M12 6c-2-1.5-4.5-2-8-2v14c3.5 0 6 .5 8 2M12 6c2-1.5 4.5-2 8-2v14c-3.5 0-6 .5-8 2",
}

_HER = os.path.dirname(os.path.abspath(__file__))


def _laes(navn: str) -> str:
    with open(os.path.join(_HER, navn), encoding="utf-8") as f:
        return f.read()


def _slug(sti: str) -> str:
    """pages/4_Økonomi.py → 'Økonomi' (sådan hedder Streamlits eget link)."""
    return os.path.splitext(os.path.basename(sti))[0].split("_", 1)[-1]


def vis_forside(fag: list, opslag: list, hoejde: int = 1180) -> None:
    """Tegn 3D-forsiden.

    fag:    (navn, sidesti, beskrivelse, farve) — kortene.
    opslag: (fag, modul, sidesti, farve, hop) — søgeindekset. `hop` er nummeret
            på den skjulte Streamlit-knap der deep-linker til modulet, eller
            None hvis der kun kan navigeres til selve siden.
    """
    kort = [
        {"navn": navn, "slug": _slug(sti), "beskrivelse": besk, "farve": farve,
         "ikon": IKONER.get(navn, "M12 2v20")}
        for navn, sti, besk, farve in fag
    ]
    idx = [
        {"fag": f, "modul": m, "slug": _slug(sti), "farve": farve,
         "hop": hop, "ord": " ".join(ord_)}
        for f, m, sti, farve, hop, ord_ in opslag
    ]
    html = (_laes("forside.html")
            .replace("__FAG__", json.dumps(kort, ensure_ascii=False))
            .replace("__INDEKS__", json.dumps(idx, ensure_ascii=False))
            .replace("__ANTAL_SIDER__", str(len(fag)))
            .replace("__ANTAL_MODULER__", str(len(opslag))))
    components.html(html, height=hoejde, scrolling=False)
