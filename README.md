# Opslagsværktøj — Logistikøkonom

Ét samlet opslagsværktøj til hurtigt opslag og anvendelse under opgaveskrivning
og eksamen. Regnetunge fag = regnemaskine + dynamisk graf. Bløde fag = søgbart
modelbibliotek (bygges senere).

**Formål:** korrekthed og hastighed. Tast ind → få svar → se grafen reagere.
Ikke et læringsværktøj.

## Kør lokalt

```bash
pip install -r requirements.txt
streamlit run Hjem.py
```

Åbner i browseren (typisk http://localhost:8501). Vælg fag i menuen til venstre.

## Status

| Fag | Status | Moduler |
|---|---|---|
| 🛒 Indkøb | ✅ Klar | EOQ · POQ/EPQ · ROP+SS · ABC/Pareto · Forecasting · Review-systemer · Make-vs-buy/TCO · Leverandørscore · Strategi & modeller (Kraljic/Bensaou/sourcing) |
| 🏭 Produktion | ✅ Klar | POQ · Linjebalancering · Processkort · Knap kapacitet · Produktionsstrategi (5 dim.) · MPS+ATP · MRP (BOM-eksplosion) · S&OP (Level/Chase) · Little's Law · OEE · Perfect Order/OTIF · Udnyttelsesgrad ρ |
| 📊 Statistik | ✅ Klar | Normalfordeling · Konfidensinterval (middelværdi/andel) · Binomialfordeling · Kontrolkort (p-kort, X̄- og R-kort) · Regression (scatter + R²) |
| 💰 Økonomi | ✅ Klar | Investeringskalkule (NPV/IRR/payback/kritisk levetid) · Break-even · Priskalkulation (bidrag/fordeling/retrograd) · Prisoptimering (total/grænse) · Nøgletalsanalyse · Budget |
| 🧭 Organisation | ✅ Klar | Søgbart modelkatalog (Porter, Ansoff, lean/agil SC, struktur, organisk/mekanistisk, McGregor X/Y, Schein, Blake & Mouton, Adizes PAEI, Hofstede) · Modelvælger |
| 💬 Kommunikation | ✅ Klar | Interessentanalyse (magt-interesse-grid) · Forhandlingsark (MDO/LDO) · ZOPA-visualizer · Forhandlingsbibliotek (BAPTA, principiel forhandling, distributiv/integrativ, kulturelle stile) |

Bygges ét fag ad gangen — næste fag tilføjes først, når det forrige er godkendt.

## Arkitektur

```
opslagsvaerktoej/
  Hjem.py              # forside med navigation
  pages/
    1_Indkøb.py        # UI: kalder core/indkoeb.py
  core/
    indkoeb.py         # ren matematik, ingen Streamlit-kald
  tests/
    test_indkoeb.py    # verifikation af formler mod kendte facit
  data/                # (eksempeldata ligger pt. i koden)
  .streamlit/config.toml
  requirements.txt
```

## Notation (matcher eget materiale)

| Modul | Formel |
|---|---|
| EOQ (Wilsons formel) | `EOQ = √(2·D·S / H)`,  `H = enhedspris · lagerrente` |
| POQ/EPQ | `POQ = √(2·D·S / (H·(1−d/p)))` |
| ABC | årsværdi = forbrug·pris, sortér faldende, A ≤ 80 %, B ≤ 95 %, C > 95 % (A≈20%vare/80%omsætning) |
| ROP/SS (benzinlampen) | `SS = z·σ·√L`,  `ROP = d·L + SS`,  d = D/52; faste z: 1,28/1,65/2,33 (90/95/99 %) |
| TCO | totalomkostning = faste + variabel·volumen; break-even hvor linjerne krydser; + 4 make-or-buy KPI'er |
| Forecasting | glidende gns. + eksp. udglatning (α); FE, MFE, MAD, MAPE, tracking signal |
| Review-systemer | periodisk: `R = d·(P+L)+SS`, `Q = R−I`; kontinuert: bestil EOQ ved ROP |
| Leverandørscore | Σ(vægt · score), vægte normaliseret |

Konventioner: dansk UI, ingen pile i tekst, TCO (ikke TCA) — matcher brugerens
`danish-indkob`-skill og `VIDEN_Logistik.md`. Bevidst udeladt: værdikædeanalyse
(særlig struktur, bygges senere) og indkøbsjura/CISG/Incoterms (eget modul #7).

## Test

```bash
python tests/test_indkoeb.py
python tests/test_produktion.py
```

Alle formler er verificeret mod hånd-beregnede facit (EOQ, POQ/EPQ, ABC, ROP/SS,
TCO, forecasting, linjebalancering, MPS/ATP, knap kapacitet m.fl.).

## Senere

- Homelab-deployment (containerisering, Odysseus via Tailscale) — først når appen kører lokalt.
- Evt. 7. modul: Jura (CISG, Incoterms 2020).
