"""Forsvarstræner — træn det mundtlige eksamensforsvar.

Læreren vil høre HVORFOR. Der er sjældent ét rigtigt svar — samme leverandør kan
være strategisk i én optik og flaskehals i en anden; det afgørende er argumentet
og at man kan forsvare det, når eksaminator borer dybere. Tilstandene: eksaminér
mig (blandet pool), fælde-jagt (kun snydespørgsmål), dybde-drill (eksaminator
borer lag for lag), argumentér-selv (lås din position før svaret vises), forklar
selv (Feynman), regn (selvrettende opgaver), faktatjek (fundamentet) og
prøveeksamen (10 spørgsmål på tid). Dit fremskridt (svær-kø, drill-dybde,
faktatjek-bunker, regn-score) gemmes automatisk i data/forsvar_progress.json.
"""
import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hashlib  # noqa: E402
import json  # noqa: E402
import random  # noqa: E402
import re  # noqa: E402
import streamlit.components.v1 as components  # noqa: E402

from ui_theme import inject_css  # noqa: E402
from regn_data import REGN  # noqa: E402
from pakke_spoergsmaal import KONCEPT  # noqa: E402
from pakke_kaeder import EKSTRA_KAEDER  # noqa: E402
from pakke_argumenter import EKSTRA_ARGUMENTER  # noqa: E402
from pakke_fakta import EKSTRA_FAKTA  # noqa: E402
from pakke_3sem import (KONCEPT_3SEM, KAEDER_3SEM,  # noqa: E402
                        ARGUMENTER_3SEM)
from pakke_kobling import KOBLINGER, VALG  # noqa: E402
from pakke_paastande import PAASTANDE  # noqa: E402
import regnegen  # noqa: E402

st.set_page_config(page_title="Forsvarstræner", page_icon="🎓", layout="wide")
inject_css()

ss = st.session_state


# ===========================================================================
# INDHOLD
# ===========================================================================
# Dybde-drill: hvert emne er en kæde af spørgsmål der borer dybere. Svaret er et
# *argument* (ikke et facit), og hvor flere svar kan forsvares, står det i "alt".
KÆDER = [
    {
        "emne": "Integreret ERP-system",
        "fag": "Teknologi",
        "lag": [
            {"sp": "I skriver i opgaven, at virksomheden vil lave et integreret ERP-system. "
                   "Hvad er et ERP-system egentlig?",
             "arg": "Et ERP-system (Enterprise Resource Planning) samler alle afdelingers data i "
                    "**én fælles database** — indkøb, lager, produktion, økonomi og salg taler "
                    "sammen i stedet for hver sit ø-system. *Integreret* betyder netop, at fx en "
                    "salgsordre automatisk opdaterer lager, produktion og regnskab på én gang.",
             "fakta": True},
            {"sp": "Fint. Så hvilket ERP-system vil du anbefale dem?",
             "snyd": True,
             "arg": "Det kan jeg ikke svare på endnu — og det er pointen. Man vælger ikke et "
                    "produkt (SAP, Microsoft Dynamics, Navision …) ud fra navnet. Først laver jeg "
                    "en **behovsanalyse / kravspecifikation**: hvilke processer skal systemet "
                    "understøtte, hvilke moduler er nødvendige, hvor mange brugere, hvilket budget, "
                    "og hvad skal det integrere med. *Derefter* matcher jeg kravene mod systemerne.",
             "fisker": "Han vil ikke høre et produktnavn — han tester, om du kan **metoden**: behov "
                       "→ kravspecifikation → match. At kaste et systemnavn ud uden analyse er fælden."},
            {"sp": "Og hvordan finder du så de behov?",
             "arg": "Ved at gå ud på gulvet og kortlægge de faktiske arbejdsgange — "
                    "**behovsplanlægning ude i driften**. Dem der bruger systemet (lager, "
                    "produktion, indkøb) kender de reelle behov og flaskehalse. Jeg "
                    "interviewer/observerer dem og oversætter det til konkrete krav.",
             "fisker": "At behovet kommer fra brugerne i driften — ikke fra ledelsens skrivebord."},
            {"sp": "Hvorfor er det så vigtigt at inddrage gulvet — hvad er risikoen ellers?",
             "arg": "Et system valgt fra skrivebordet rammer ved siden af de reelle behov og giver "
                    "lav brugeradoption — folk laver workarounds eller bruger det slet ikke. "
                    "ERP-projekter er i forvejen dyre og langvarige, og den største risiko er netop "
                    "modstand mod forandring og dårlig kravafdækning. Inddragelse skaber både bedre "
                    "krav og ejerskab.",
             "fisker": "At du kender de klassiske ERP-faldgruber: adoption, forandringsledelse, "
                       "dyr implementering."},
        ],
    },
    {
        "emne": "Incoterm DDP, Duty og told",
        "fag": "Jura / Logistik",
        "lag": [
            {"sp": "Hvad er Incoterm DDP?",
             "arg": "DDP = **Delivered Duty Paid**. Sælger bærer *alt*: transport, forsikring, "
                    "risiko OG told/afgifter — helt frem til købers dør. Køber skal nærmest bare "
                    "tage imod. Det er den mest sælger-tunge Incoterm (modsætningen er EXW, hvor "
                    "køber gør alt).",
             "fakta": True},
            {"sp": "Du nævner told og afgifter. Hvad dækker 'Duty' så specifikt?",
             "arg": "Duty = **importtold** — den afgift, der pålægges en vare, når den krydser en "
                    "toldgrænse ind i et land. I DDP er det sælgers ansvar at toldklarere og betale "
                    "den (plus evt. importmoms/punktafgifter, alt efter aftale).",
             "fakta": True},
            {"sp": "Er der så told fra Danmark til Tyskland?",
             "snyd": True,
             "arg": "Nej. Danmark og Tyskland er **begge i EU's toldunion og indre marked** → fri "
                    "bevægelighed for varer → **ingen told** mellem EU-lande. 'Duty/told' bliver "
                    "først relevant ved handel **ud af** EU (fx UK efter Brexit, USA, Kina). "
                    "Internt i EU er det momsreglerne (reverse charge / EU-handel), der er det "
                    "interessante — ikke told.",
             "fisker": "Fælden er at sige pr. refleks 'ja, sælger betaler tolden'. Han tester, om "
                       "du ved, at DDP's told-ansvar i praksis kun har betydning *uden for* EU — og "
                       "at du kender toldunionen."},
            {"sp": "Så hvornår gør valget mellem fx DDP og DAP en reel forskel?",
             "arg": "Forskellen ligger i, hvem der står for importtold og -klarering. Inden for EU "
                    "er der ingen told, så de to ligner hinanden mere der. Ved import fra et "
                    "**tredjeland** betyder DDP, at sælger påtager sig told, klarering og ansvar i "
                    "et land, han måske ikke kender — en stor byrde, og derfor vælges DDP ofte fra "
                    "ved oversøisk handel.",
             "fisker": "At du kan koble Incoterm-valget til, om handlen krydser EU's *ydre* grænse."},
        ],
    },
    {
        "emne": "EOQ / Wilsons formel",
        "fag": "Indkøb",
        "lag": [
            {"sp": "Hvad beregner EOQ?",
             "arg": "Den **optimale ordrestørrelse** — hvor meget man skal bestille ad gangen, så "
                    "summen af **bestillingsomkostninger** og **lageromkostninger** er mindst. Få "
                    "store ordrer = lavt bestillingsarbejde, men højt lager; mange små = omvendt. "
                    "EOQ rammer balancen.",
             "fakta": True},
            {"sp": "Hvilke antagelser bygger formlen på?",
             "arg": "Konstant og kendt efterspørgsel, konstant leveringstid, ingen mængderabatter, "
                    "og at hele ordren kommer på én gang. Lager- og bestillingsomkostninger er "
                    "kendte og konstante.",
             "fakta": True},
            {"sp": "Holder de antagelser i virkeligheden?",
             "snyd": True,
             "arg": "Sjældent helt. Efterspørgsel svinger, leveringstider varierer, og der er ofte "
                    "rabatter. Derfor er EOQ et **udgangspunkt/pejlemærke**, ikke et facit — man "
                    "justerer for virkeligheden.",
             "fisker": "At du ikke tror blindt på modellen. At kunne kritisere/forbeholde modellen "
                       "giver point."},
            {"sp": "Hvad gør du, hvis leverandøren tilbyder mængderabat ved en større ordre?",
             "arg": "Så kan EOQ blive suboptimal. Jeg regner **totalomkostningen** (vare + "
                    "bestilling + lager) ved EOQ *og* ved hvert rabat-trin og vælger den med lavest "
                    "total — nogle gange betaler det sig at købe mere end EOQ for at få rabatten.",
             "fisker": "At du kan håndtere brud på antagelserne, ikke bare sætte tal i formlen."},
        ],
    },
    {
        "emne": "Kraljics indkøbsmatrix",
        "fag": "Indkøb",
        "lag": [
            {"sp": "Hvad bruger man Kraljics matrix til?",
             "arg": "Til at opdele indkøb i fire typer efter **forsyningsrisiko** og **økonomisk "
                    "betydning/indkøbsandel**: ukritiske, hævearm (leverage), flaskehals og "
                    "strategiske varer. Hver type har sin egen indkøbsstrategi.",
             "fakta": True},
            {"sp": "Du placerer en leverandør som strategisk. Begrund det.",
             "arg": "Fordi varen både har **høj forsyningsrisiko** (få udbydere, svær at erstatte) "
                    "og **høj betydning** for vores produkt/forretning. Derfor: tæt, langsigtet "
                    "partnerskab, delte prognoser, sikret forsyning.",
             "alt": "Men det er ikke det eneste forsvarlige. Hvis du i stedet vægter at varen fylder "
                    "**lidt økonomisk**, kan den samme leverandør forsvares som en **flaskehalsvare** "
                    "(lav værdi, høj risiko) — så er fokus på forsyningssikkerhed, ikke partnerskab. "
                    "Begge kan være rigtige; det afhænger af, hvilket kriterium du vægter, og om du "
                    "argumenterer konsistent.",
             "fisker": "At du kobler placeringen til **kriterierne** (risiko vs. beløb) og er "
                       "bevidst om dit valg — ikke at du rammer en bestemt boks."},
            {"sp": "Hvad gør du så konkret ved den leverandør?",
             "arg": "Det følger af din placering: strategisk → byg partnerskab og sikr forsyning; "
                    "flaskehals → læg lager, find alternative leverandører, lav rammeaftaler. "
                    "Pointen er, at **handlingen skal matche argumentet**.",
             "fisker": "At du kan oversætte modellen til en konkret indkøbsstrategi."},
            {"sp": "Kan en leverandør flytte sig i matricen over tid?",
             "arg": "Ja. Markedet ændrer sig — en ny udbyder sænker risikoen (strategisk → "
                    "leverage), eller en leverandør lukker (leverage → flaskehals). Matricen er et "
                    "øjebliksbillede, man skal opdatere.",
             "fisker": "At modellen er dynamisk, ikke en endegyldig bås."},
        ],
    },
    {
        "emne": "NPV / kapitalværdi",
        "fag": "Økonomi",
        "lag": [
            {"sp": "Hvad betyder en positiv NPV?",
             "arg": "At investeringen tjener mere hjem end afkastkravet — den **skaber værdi**. "
                    "Alle fremtidige betalinger er regnet om til nutidskroner og lagt sammen med "
                    "startinvesteringen; er summen positiv, bør man investere.",
             "fakta": True},
            {"sp": "Hvad er kalkulationsrenten, og hvorfor bruger man den?",
             "arg": "Renten er **afkastkravet** — hvad pengene mindst skulle tjene alternativt "
                    "(alternativomkostning) plus et risikotillæg. Den tilbagediskonterer fremtidige "
                    "kroner, fordi en krone i dag er mere værd end en krone om tre år.",
             "alt": "Her er der et skøn: hvilken rente er 'den rigtige'? Det kan diskuteres "
                    "(virksomhedens lånerente, ejernes afkastkrav, projektets risiko). Du skal "
                    "kunne **begrunde** dit renteniveau — ikke bare bruge et tal.",
             "fisker": "At du forstår *hvad* renten repræsenterer, ikke kun at den står i Excel."},
            {"sp": "Hvad sker der med NPV, hvis renten stiger?",
             "snyd": True,
             "arg": "NPV **falder** — højere rente diskonterer fremtidige indbetalinger hårdere. Et "
                    "projekt, der lige var rentabelt, kan tippe til negativt. Derfor er en "
                    "følsomhedsberegning på renten klog.",
             "fisker": "At du forstår sammenhængen rente↑ → NPV↓."},
        ],
    },
    {
        "emne": "JIT (Just In Time)",
        "fag": "Produktion",
        "lag": [
            {"sp": "Hvad er JIT?",
             "arg": "Et **træk-princip**: varer/materialer kommer lige når der er brug for dem, "
                    "ikke før. Målet er minimalt lager og spild — produktionen *trækker* efter "
                    "faktisk behov i stedet for at *skubbe* efter prognoser (som MRP).",
             "fakta": True},
            {"sp": "Hvad kræver JIT af leverandørerne?",
             "arg": "Meget **pålidelige, hyppige leverancer** i små mængder, høj kvalitet (ingen "
                    "tid til fejl) og en tæt relation med god kommunikation. JIT virker kun, hvis "
                    "leverandøren kan levere præcist til tiden.",
             "fisker": "At du ser koblingen mellem produktionsprincip og leverandørrelation."},
            {"sp": "Hvad er så bagsiden — risikoen ved JIT?",
             "snyd": True,
             "arg": "Lavt lager gør dig **sårbar over for forsyningsbrud**: en strejke, en "
                    "forsinkelse eller en krise (fx corona) kan stoppe hele produktionen, fordi der "
                    "ingen buffer er. JIT optimerer omkostninger på bekostning af robusthed.",
             "alt": "Derfor kan man sagtens **argumentere imod JIT** for en sårbar forsyningskæde — "
                    "og for en buffer i stedet. Der er ikke ét rigtigt svar; det afhænger af, hvor "
                    "stabil efterspørgsel og forsyning er.",
             "fisker": "At du kan se trade-off'et: billigt lager vs. forsyningssikkerhed."},
        ],
    },
    {
        "emne": "Sikkerhedslager & servicegrad",
        "fag": "Indkøb",
        "lag": [
            {"sp": "Hvad er et sikkerhedslager?",
             "arg": "En ekstra buffer ud over det forventede forbrug, der dækker **usikkerhed** — "
                    "hvis efterspørgslen bliver større end ventet, eller leverancen forsinkes — så "
                    "man ikke løber tør (undgår restordrer).",
             "fakta": True},
            {"sp": "Hvad bestemmer, hvor stort det skal være?",
             "arg": "Tre ting: **usikkerheden** i efterspørgslen (standardafvigelsen), "
                    "**leveringstiden** (længere tid = mere kan nå at gå galt) og den **ønskede "
                    "servicegrad** (hvor sikker vil du være på ikke at løbe tør — udtrykt som en "
                    "z-værdi).",
             "fakta": True},
            {"sp": "Hvad koster det at hæve servicegraden fra fx 95 % til 99 %?",
             "snyd": True,
             "arg": "Uforholdsmæssigt meget. De sidste procent kræver **eksponentielt mere lager**, "
                    "fordi du skal dække stadig mere sjældne udsving. Derfor er 100 % servicegrad i "
                    "praksis uøkonomisk — man vælger et niveau, hvor omkostningen ved mere lager "
                    "balancerer omkostningen ved at mangle.",
             "alt": "Hvilket niveau der er 'rigtigt', kan diskuteres: en A-vare/kritisk kunde "
                    "forsvarer høj servicegrad; en C-vare gør ikke. Argumentér ud fra varens/kundens "
                    "betydning.",
             "fisker": "At servicegrad er en **afvejning**, ikke 'jo højere jo bedre'."},
        ],
    },
    {
        "emne": "Porters generiske strategier + harmoni",
        "fag": "Strategi",
        "lag": [
            {"sp": "Hvilken generisk strategi kører virksomheden?",
             "arg": "Det argumenterer jeg for ud fra, hvordan de faktisk vinder kunder: "
                    "**omkostningsleder** (billigst), **differentiering** (unik, højere pris) eller "
                    "**fokus** (samme to på et nichemarked).",
             "alt": "Her er sjældent ét rigtigt svar — den samme virksomhed kan forsvares som "
                    "differentiering (de tager overpris for kvalitet) *eller* fokus (de rammer kun "
                    "et snævert segment). Det afgørende er, hvilke fakta fra casen du fremhæver.",
             "fisker": "At du **begrunder** strategivalget med konkrete træk fra casen."},
            {"sp": "Kan man ikke bare være både billigst OG mest unik?",
             "snyd": True,
             "arg": "Sjældent — Porter kalder det 'stuck in the middle': man taber fokus og rammer "
                    "ingen af delene. Nogle få kan begge via fx teknologi eller stordrift, men som "
                    "udgangspunkt skal man vælge.",
             "fisker": "At du kender 'stuck in the middle' *og* nuancen om, at nogle kan begge."},
            {"sp": "Passer deres forsyningskæde til den strategi?",
             "arg": "Det er **harmoni**-spørgsmålet. Differentiering kræver typisk en "
                    "**responsiv/agil** kæde (hurtig, fleksibel); omkostningsleder kræver en "
                    "**lean/efficient** kæde (billig, stabil). Matcher kæden ikke strategien, er det "
                    "en svaghed.",
             "fisker": "Harmoni mellem strategi og forsyningskæde — kernen i hele faget."},
        ],
    },
]
# Læg de mange censur-verificerede dybde-kæder oven på de oprindelige (ingen fjernes).
KÆDER = KÆDER + EKSTRA_KAEDER + KAEDER_3SEM

# Argumentér-selv: samme situation kan forsvares flere veje. Pointen er argumentet.
ARGUMENTER = [
    {
        "fag": "Indkøb · Kraljic",
        "situation": "En leverandør leverer en kritisk specialkomponent til jeres flagskibsprodukt. "
                     "I aftager småt (lille andel af indkøbsbudgettet), men der findes kun få "
                     "udbydere af komponenten.",
        "spm": "Hvor placerer du leverandøren i Kraljic — og hvorfor?",
        "positioner": [
            {"navn": "Strategisk vare", "arg": "Hvis du vægter den **strategiske betydning**: "
             "komponenten er afgørende for flagskibsproduktet og svær at erstatte, så produktet "
             "falder uden den. Vigtighed ≠ kun kroner. → tæt partnerskab, sikret forsyning."},
            {"navn": "Flaskehalsvare", "arg": "Hvis du vægter **indkøbsandelen** strengt: lille "
             "beløb, men høj forsyningsrisiko = flaskehals. → fokus på forsyningssikkerhed (lager, "
             "alternative leverandører), ikke partnerskab."},
        ],
        "pointe": "Begge kan forsvares. Forskellen er, om du vægter *den strategiske betydning for "
                  "slutproduktet* (→ strategisk) eller *det lave indkøbsbeløb* (→ flaskehals). Vælg "
                  "ét kriterium, vær eksplicit om det, og vær konsekvent — så er svaret stærkt "
                  "uanset boksen.",
    },
    {
        "fag": "Indkøb · Bensaou",
        "situation": "I har investeret i fælles IT-integration og specialværktøj med en leverandør. "
                     "Leverandøren har derimod ikke lavet særlige investeringer rettet mod jer.",
        "spm": "Hvilken relation er det i Bensaou — og hvorfor?",
        "positioner": [
            {"navn": "Captive buyer (du er bundet)", "arg": "Fordi **kun I** har lavet specifikke "
             "investeringer. I er låst til leverandøren, mens han frit kan gå — det giver jer lav "
             "forhandlingsmagt og en sårbar position."},
            {"navn": "Strategisk partnerskab", "arg": "*Hvis* man kan argumentere for, at "
             "leverandøren reelt også har bundet sig (fx tilpasset sin produktion til jer), så er "
             "der gensidige investeringer = strategisk partner."},
        ],
        "pointe": "Svaret afhænger helt af, **hvem der har lavet de specifikke investeringer**. "
                  "Bensaou handler netop om den asymmetri — argumentér ud fra, hvad casen siger om "
                  "begge parters investeringer.",
    },
    {
        "fag": "Produktion · Ordretype",
        "situation": "Virksomheden samler produkter af standarddele, men kunden vælger selv "
                     "konfigurationen ved bestilling.",
        "spm": "Er det ATO eller MTO — og hvorfor?",
        "positioner": [
            {"navn": "ATO (Assemble-To-Order)", "arg": "Hvis delene er **standard og ligger på "
             "lager**, og man kun *samler* efter ordre. Kort leveringstid, lavt færdigvarelager. "
             "Det er det stærkeste argument her."},
            {"navn": "MTO (Make-To-Order)", "arg": "Kan forsvares, *hvis* nogle dele reelt "
             "fremstilles specifikt til ordren (ikke kun samles). Så er der mere produktion efter "
             "ordre, og leveringstiden er længere."},
        ],
        "pointe": "Afgør det ud fra, om delene **samles** (ATO) eller **fremstilles** (MTO) efter "
                  "ordre. Det er koblingen mellem casens fakta og definitionen, der bærer svaret.",
    },
    {
        "fag": "Indkøb · Make vs. buy",
        "situation": "Virksomheden overvejer at outsource en produktion, der i dag laves in-house. "
                     "Det er lidt billigere at købe udefra, men komponenten er tæt på kerneproduktet.",
        "spm": "Skal de outsource — og hvorfor?",
        "positioner": [
            {"navn": "Behold in-house (make)", "arg": "Hvis du vægter **strategisk kontrol og "
             "kernekompetence**: komponenten er tæt på kerneproduktet, så man bevarer kvalitet, "
             "viden og uafhængighed — selv om det koster lidt mere."},
            {"navn": "Outsource (buy)", "arg": "Hvis du vægter **omkostning og fokus**: det er "
             "billigere, og virksomheden kan koncentrere sig om sit kerneområde. Suppler gerne med "
             "en TCO-beregning (alle omkostninger, ikke kun prisen)."},
        ],
        "pointe": "Klassisk 'det afhænger': vægter du **kostpris** eller **strategisk kontrol**? "
                  "Et stærkt svar nævner begge og forsvarer, hvorfor det ene vejer tungest *her* — "
                  "gerne underbygget med tal (TCO).",
    },
]
# Mange flere fler-forsvarlige cases oven på de oprindelige (ingen fjernes).
ARGUMENTER = ARGUMENTER + EKSTRA_ARGUMENTER + ARGUMENTER_3SEM

# Faktatjek: det der ER fakta og skal sidde fast — fundamentet du argumenterer ovenpå.
FAKTA = [
    ("Incoterm DDP", "Delivered Duty Paid: sælger bærer alt — transport, risiko, told og afgifter "
     "— helt til købers dør. Mest sælger-tunge Incoterm."),
    ("Incoterm EXW", "Ex Works: køber bærer alt fra leverandørens fabrik. Mest køber-tunge Incoterm."),
    ("Duty / told", "Importafgift når en vare krydser en toldgrænse ind i et land. Kun relevant "
     "*ud af* EU — der er ingen told internt i EU's toldunion (fx DK→DE)."),
    ("ERP", "Enterprise Resource Planning: ét integreret system, der samler alle afdelingers data "
     "i én fælles database."),
    ("EOQ (Wilson)", "Optimal ordrestørrelse: minimerer summen af bestillings- og "
     "lageromkostninger. Antager bl.a. konstant efterspørgsel og ingen rabatter."),
    ("NPV / kapitalværdi", "Nutidsværdien af alle fremtidige betalinger minus investeringen. "
     "Positiv NPV = skaber værdi. Rente op → NPV ned."),
    ("Kalkulationsrente", "Afkastkravet: alternativomkostning + risikotillæg. Bruges til at "
     "tilbagediskontere fremtidige kroner."),
    ("JIT", "Just In Time: træk-princip, varer kommer lige når der er brug for dem. Minimalt "
     "lager, men sårbar over for forsyningsbrud."),
    ("MRP", "Materialebehovsplanlægning: skub-princip, planlægger materialer ud fra prognoser og "
     "styklister (BOM)."),
    ("Kraljic", "Indkøbsmatrix: forsyningsrisiko × økonomisk betydning → 4 typer (ukritisk, "
     "leverage, flaskehals, strategisk), hver med sin strategi."),
    ("Bensaou", "Leverandørrelations-matrix efter hvem der har lavet specifikke investeringer: "
     "markedsudveksling, captive buyer, captive supplier, strategisk partner."),
    ("Sikkerhedslager", "Buffer mod usikkerhed i efterspørgsel/leveringstid. Størrelse afhænger "
     "af usikkerhed, leveringstid og ønsket servicegrad (z-værdi)."),
    ("Stuck in the middle", "Porter: at fejle ved at forsøge både omkostningsleder og "
     "differentiering på én gang og ikke ramme nogen af dem."),
    ("Harmoni", "At konkurrencestrategi og forsyningskæde passer sammen "
     "(differentiering ↔ agil, omkostningsleder ↔ lean)."),
    ("Behovsanalyse / kravspecifikation", "Kortlægning af, hvad et system/produkt skal kunne (fx "
     "før ERP-valg) — lavet ud fra brugernes faktiske behov i driften, ikke fra skrivebordet."),
]
# Mange flere fakta-kort oven på de oprindelige (ingen fjernes).
FAKTA = FAKTA + EKSTRA_FAKTA


# ===========================================================================
# FAG-HARMONISERING
# ===========================================================================
# Bankerne bruger mange forskellige fag-mærkater (Strategi, Ledelse, Logistik,
# Forhandling, 'Indkøb (beregning)' …). Her oversættes alt til de 8 kanoniske
# fag (appens 7 sider + Jura), så fag-filteret aldrig gemmer spørgsmål væk.
# Den oprindelige mærkat vises som undertag, fx 'Indkøb · Logistik'.
KANONISKE_FAG = ["Værdikæde", "Indkøb", "Produktion", "Statistik", "Økonomi",
                 "Organisation", "Kommunikation", "Jura",
                 # 3. semester: prøvens egne fag. Manglede før, så Distribution
                 # og Projektstyring faldt bagest som "ukendte" i fagfiltret.
                 "Distribution", "Projektstyring"]
FAG_MAP = {
    "Strategi": "Organisation",
    "Ledelse": "Organisation",
    "Logistik": "Indkøb",
    "Teknologi": "Indkøb",
    "Forhandling": "Kommunikation",
    "Jura / Logistik": "Jura",
}


def _norm_fag(raa):
    """Oversæt et bank-fag til (kanonisk fag, undertag).

    Undertag er den oprindelige mærkat, når den afviger fra det kanoniske fag.
    '(beregning)'-varianterne falder sammen med deres fag uden undertag.
    """
    base = raa.split("·")[0].strip()
    ren = base.replace(" (beregning)", "").strip()
    kanon = FAG_MAP.get(ren, ren)
    undertag = ren if ren != kanon else None
    return kanon, undertag


def _fag_liste(fags):
    """Filter-liste: de kanoniske fag der findes + evt. ukendte bagest."""
    fags = set(fags)
    return (["Alle"] + [f for f in KANONISKE_FAG if f in fags]
            + sorted(fags - set(KANONISKE_FAG)))


def _stabil_id(prefix, emne, sp, brugt):
    """Stabilt id: hash af emne + spørgsmålets første 40 tegn.

    Overlever at bankerne vokser eller omordnes (modsat positionelle id'er),
    så svær-køen kan gemmes på disk uden at pege på forkerte spørgsmål.
    """
    h = hashlib.md5(f"{emne}|{sp[:40]}".encode("utf-8")).hexdigest()[:8]
    pid = f"{prefix}{h}"
    while pid in brugt:
        pid += "x"
    brugt.add(pid)
    return pid


def _fagvis(fag, undertag):
    return fag + (f" · {undertag}" if undertag else "")


# ===========================================================================
# ARGUMENT-KORT (case + kort titel + kanonisk fag)
# ===========================================================================
def _arg_titel(a):
    """Kort casetitel: emnedelen efter '·' hvis den findes, ellers første
    sætning af situationen (afkortet) — så headeren aldrig bliver 'Forhandling
    · Forhandling'."""
    if "·" in a["fag"]:
        return a["fag"].split("·", 1)[1].strip()
    s = re.split(r"[.!?]", a["situation"], maxsplit=1)[0].strip()
    return s if len(s) <= 60 else s[:57].rstrip() + "…"


ARG_KORT = []
_brugt_ids = set()
for _a in ARGUMENTER:
    _fag, _under = _norm_fag(_a["fag"])
    _titel = _arg_titel(_a)
    ARG_KORT.append({"id": _stabil_id("a", _titel, _a["spm"], _brugt_ids),
                     "fag": _fag, "undertag": _under, "titel": _titel, "case": _a})
ARG_BY_ID = {k["id"]: k for k in ARG_KORT}
ARG_FAG = _fag_liste(k["fag"] for k in ARG_KORT)


# ===========================================================================
# FAKTA-KORT (dedup + mekanisk fag-afledning — formatet i pakke_fakta.py røres ikke)
# ===========================================================================
# Nøgleordene tjekkes i rækkefølge; første match vinder. Specifikke
# model-/lov-ord står før de brede, så fx Kraljic-kortet ikke ryger i
# Produktion, bare fordi bagsiden nævner 'flaskehals'.
_FAKTA_REGLER = [
    ("Jura", ["incoterm", "told", "duty", "cisg", "købelov", "aftalelov",
              "reklamation", "misligholdelse", "risikoovergang", "force majeure",
              "voldgift", "exw", "fca", "fob", "cif", "cfr", "ddp", "dap", "cpt",
              "cip", "fas", "erstatning"]),
    ("Værdikæde", ["værdikæde", "primære aktiviteter", "primær aktivitet",
                   "støtteaktivitet", "harmoni", "forsyningskæde"]),
    ("Indkøb", ["kraljic", "bensaou", "eoq", "wilson", "genbestillingspunkt",
                "rop", "sikkerhedslager", "servicegrad", "abc analyse",
                "leverandør", "sourcing", "indkøb", "tco", "total cost",
                "rammeaftale", "mængderabat", "erp", "kravspecifikation",
                "behovsanalyse", "forecast", "prognose", "poq"]),
    ("Kommunikation", ["batna", "zopa", "mdo", "ldo", "distributiv",
                       "integrativ", "forhandling", "byttechips", "målpunkt",
                       "aspirationsniveau", "reservationspunkt",
                       "aktiv lytning", "spørgeteknik", "kropssprog",
                       "kommunikation", "transaktionsanalyse"]),
    ("Statistik", ["konfidensinterval", "konfidens", "hypotese", "p værdi",
                   "signifikans", "normalfordeling", "normalfordelt",
                   "standardafvigelse", "stikprøve", "varians", "korrelation",
                   "regression", "z værdi", "z score", "t test", "t fordeling",
                   "median", "kvartil", "binomial", "fraktil", "outlier",
                   "kontrolkort", "kontrolgrænse", "ucl", "lcl", "særårsag",
                   "forklaringsgrad", "sandsynlighed"]),
    ("Økonomi", ["npv", "kapitalværdi", "annuitet", "kalkulationsrente",
                 "intern rente", "irr", "afskrivning", "dækningsbidrag",
                 "dækningsgrad", "nulpunkt", "break even", "likviditet",
                 "soliditet", "afkastningsgrad", "overskudsgrad", "egenkapital",
                 "balance", "resultatopgørelse", "investering",
                 "tilbagebetalingstid", "payback", "kritisk levetid",
                 "følsomhed", "kalkulation", "bidragskalkulation", "aoh",
                 "omsætningshastighed", "benzinlampe"]),
    ("Produktion", ["mts", "mto", "ato", "eto", "jit", "just in time", "kanban",
                    "lean", "kaizen", "oee", "smed", "mrp", "stykliste", "bom",
                    "takt", "gennemløbstid", "layout", "5s", "muda", "tqm",
                    "flaskehals", "kapacitet", "omstilling", "spild", "otif",
                    "ordrevinder", "ordrekvalificerende", "leveringspræstation",
                    "produktion", "kvalitetsstyring", "seriestørrelse"]),
    ("Organisation", ["mcgregor", "schein", "adizes", "ledergitter", "maslow",
                      "herzberg", "hofstede", "motivation", "kultur", "ansoff",
                      "porter", "swot", "mintzberg", "interessent", "strategi",
                      "stuck in the middle", "differentiering", "diversifikation",
                      "kontrolspænd", "span of control", "ledelseslag",
                      "kommandovej", "menneskesyn", "mekanistisk",
                      "omkostningsleder", "ledelse", "organisation"]),
]


def _fakta_fag(forside, bagside):
    """Afled fag pr. kort mekanisk ud fra nøgleord (kortene bærer ikke selv fag).

    Lange nøgleord matcher som forstavelse ('ansoff' rammer også 'Ansoffs'),
    korte som helt ord (så 'irr' ikke rammer 'irrelevant'). Flerords-nøgler
    matcher som frase.
    """
    tokens = re.sub(r"[^a-zæøå0-9]+", " ", (forside + " " + bagside).lower()).split()
    hay = " " + " ".join(tokens) + " "
    for fag, ord_ in _FAKTA_REGLER:
        for o in ord_:
            if " " in o:
                ramt = f" {o} " in hay
            elif len(o) >= 5:
                ramt = any(t.startswith(o) for t in tokens)
            else:
                ramt = f" {o} " in hay
            if ramt:
                return fag
    return "Øvrigt"


def _forside_noegle(forside):
    """Dedup-nøgle: små bogstaver, ordstilling ligegyldig, 'Incoterm'-præfiks
    ignoreres — så 'Incoterm DDP' ≡ 'DDP' og 'Duty / told' ≡ 'Told / Duty'."""
    tokens = re.sub(r"[^a-zæøå0-9]+", " ", forside.lower()).split()
    tokens = [t for t in tokens if t != "incoterm"]
    return " ".join(sorted(tokens)) or forside.strip().lower()


FAKTA_KORT = []
_set_forsider = set()
for _kort in FAKTA:
    _for, _bag = _kort[0], _kort[1]
    _noegle = _forside_noegle(_for)
    if _noegle in _set_forsider:  # dublet (fx DDP/EXW/told i to banker) — behold én
        continue
    _set_forsider.add(_noegle)
    FAKTA_KORT.append({"id": _stabil_id("f", _for, _bag, _brugt_ids),
                       "forside": _for, "bagside": _bag,
                       "fag": _fakta_fag(_for, _bag)})
FAKTA_BY_ID = {k["id"]: k for k in FAKTA_KORT}
FAKTA_FAG = _fag_liste(k["fag"] for k in FAKTA_KORT)


# ===========================================================================
# SAMLET POOL til "Eksaminér mig" (interleaved på tværs af alt)
# ===========================================================================
# 3. semesters spørgsmål lægges OVEN PÅ den oprindelige bank (ingen fjernes).
# De bærer fagene "Distribution" og "Projektstyring", som nu også er
# kanoniske — før faldt de bagest i fagfiltret som ukendte.
KONCEPT = KONCEPT + KONCEPT_3SEM

KONCEPT_EMNER = {q["emne"].strip().lower() for q in KONCEPT}


def _build_pool():
    pool = []
    brugt = set(ARG_BY_ID) | set(FAKTA_BY_ID)
    for q in KONCEPT:
        fag, under = _norm_fag(q["fag"])
        rev = [("Svar", q["svar"])]
        if q.get("alt"):
            rev.append(("Kan også forsvares", q["alt"]))
        if q.get("fisker"):
            rev.append(("Hvad eksaminator fisker efter", q["fisker"]))
        pool.append({"id": _stabil_id("k", q["emne"], q["sp"], brugt), "fag": fag,
                     "undertag": under, "emne": q["emne"], "sp": q["sp"],
                     "reveal": rev, "snyd": False, "slags": "koncept"})
    for it in REGN:
        fag, under = _norm_fag(it["fag"])
        rev = [("Svar", it["svar"]), ("Udregning", it["metode"])]
        if it.get("fortolk"):
            rev.append(("Fortolkning", it["fortolk"]))
        if it.get("faelde"):
            rev.append(("Typisk fælde", it["faelde"]))
        pool.append({"id": _stabil_id("r", it["emne"], it["sp"], brugt), "fag": fag,
                     "undertag": under, "emne": it["emne"], "sp": it["sp"],
                     "reveal": rev, "snyd": False, "slags": "regn"})
    for kort in ARG_KORT:
        a = kort["case"]
        rev = [(p["navn"], p["arg"]) for p in a["positioner"]]
        rev.append(("Pointe", a["pointe"]))
        pool.append({"id": kort["id"], "fag": kort["fag"], "undertag": kort["undertag"],
                     "emne": kort["titel"], "sp": a["situation"] + "\n\n**" + a["spm"] + "**",
                     "reveal": rev, "snyd": False, "slags": "argument"})
    for kaede in KÆDER:
        fag, under = _norm_fag(kaede["fag"])
        for L in kaede["lag"]:
            # Nær-dublet: rene fakta-lag springes over, hvis KONCEPT allerede
            # stiller definitionsspørgsmålet om samme emne.
            if L.get("fakta") and kaede["emne"].strip().lower() in KONCEPT_EMNER:
                continue
            # 🪤 må ALDRIG stå i spørgsmålet — fælden indrømmes først i svaret.
            rev = []
            if L.get("snyd"):
                rev.append(("🪤 Snydespørgsmål", "Det intuitive svar er en fælde — "
                            "sådan griber du det rigtigt an:"))
            rev.append(("Sådan kan du argumentere", L["arg"]))
            if L.get("alt"):
                rev.append(("Kan også forsvares", L["alt"]))
            if L.get("fisker"):
                rev.append(("Hvad eksaminator fisker efter", L["fisker"]))
            pool.append({"id": _stabil_id("d", kaede["emne"], L["sp"], brugt),
                         "fag": fag, "undertag": under, "emne": kaede["emne"],
                         "sp": L["sp"], "reveal": rev, "snyd": bool(L.get("snyd")),
                         "slags": "kæde"})
    return pool


POOL = _build_pool()
POOL_BY_ID = {p["id"]: p for p in POOL}
POOL_FAG = _fag_liste(p["fag"] for p in POOL)
FAELDE_IDS = [p["id"] for p in POOL if p["snyd"]]


# ===========================================================================
# PERSISTENS — fremskridt gemmes i data/forsvar_progress.json
# ===========================================================================
_ROD = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRESS_FIL = os.path.join(_ROD, "data", "forsvar_progress.json")
_TOM_SCORE = {"rigtige": 0, "forkerte": 0, "streak": 0, "bedste": 0}


# --- Fælles svaghedsprofil på tværs af tilstandene -------------------------
# Før havde hver tilstand sin egen svær-kø, og de talte ikke sammen: en
# svaghed fundet i Regn dukkede aldrig op i Eksaminér mig. Her samles de i
# ÉN profil pr. fag+emne, som alle tilstande skriver til og læser fra.
# Det forudsætter ordbogens fag-lister, fordi et emne kan høre til flere fag.

def _notér_svaghed(fag, emne: str) -> None:
    """Registrér at noget var svært. `fag` må være en streng eller en liste —
    et emne kan høre til flere fag, og så tæller det i dem alle."""
    if not emne:
        return
    prof = ss.setdefault("svagheder", {})
    for f in ([fag] if isinstance(fag, str) else list(fag)) or ["Øvrigt"]:
        prof[f"{f} :: {emne}"] = prof.get(f"{f} :: {emne}", 0) + 1
    _save_progress()


def _svagheds_top(n: int = 8) -> list:
    """De emner der oftest er gået galt — (fag, emne, antal), værst først."""
    prof = ss.get("svagheder", {})
    rækker = []
    for nøgle, antal in prof.items():
        fag, _, emne = nøgle.partition(" :: ")
        rækker.append((fag, emne, antal))
    return sorted(rækker, key=lambda r: (-r[2], r[0], r[1]))[:n]


def _save_progress():
    """Atomisk skrivning (temp + rename) — en afbrudt gemning ødelægger aldrig filen."""
    data = {
        "ex_svaere": sorted(ss.get("ex_svaere", set())),
        "drill": {k[len("drill_n_"):]: int(ss[k]) for k in ss
                  if str(k).startswith("drill_n_") and isinstance(ss[k], int)},
        "fakta_svaere": sorted(ss.get("fk_svaere", set())),
        "regn_score": ss.get("rt_score", dict(_TOM_SCORE)),
        "svagheder": ss.get("svagheder", {}),
    }
    try:
        os.makedirs(os.path.dirname(PROGRESS_FIL), exist_ok=True)
        tmp = PROGRESS_FIL + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        os.replace(tmp, PROGRESS_FIL)
    except OSError:
        pass  # kan ikke gemme (fx skrivebeskyttet) — appen skal stadig virke


def _load_progress():
    """Robust indlæsning: manglende/korrupt fil = frisk start, og id'er der
    ikke længere findes (fordi bankerne er ændret) filtreres bare fra."""
    try:
        with open(PROGRESS_FIL, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            data = {}
    except (OSError, ValueError):
        data = {}
    try:
        ss.ex_svaere = {i for i in data.get("ex_svaere", []) if i in POOL_BY_ID}
        ss.fk_svaere = {i for i in data.get("fakta_svaere", []) if i in FAKTA_BY_ID}
        for emne, n in (data.get("drill") or {}).items():
            kaede = next((k for k in KÆDER if k["emne"] == emne), None)
            if kaede and isinstance(n, int):
                ss[f"drill_n_{emne}"] = max(1, min(n, len(kaede["lag"])))
        rs = data.get("regn_score") or {}
        ss.rt_score = {k: max(0, int(rs.get(k, 0))) for k in _TOM_SCORE}
        sv = data.get("svagheder") or {}
        ss.svagheder = {str(k): int(v) for k, v in sv.items()
                        if isinstance(v, (int, float)) and int(v) > 0}
    except (TypeError, ValueError):
        ss.ex_svaere = set()
        ss.fk_svaere = set()
        ss.rt_score = dict(_TOM_SCORE)
        ss.svagheder = {}


def _nulstil_fremskridt():
    ss.ex_svaere = set()
    ss.fk_svaere = set()
    ss.svagheder = {}
    ss.rt_score = dict(_TOM_SCORE)
    for k in [k for k in ss if str(k).startswith("drill_n_")]:
        ss[k] = 1
    ss.nulstil_ok = False
    try:
        os.remove(PROGRESS_FIL)
    except OSError:
        pass


if not ss.get("fv_progress_indlaest"):
    _load_progress()
    ss.fv_progress_indlaest = True


# ===========================================================================
# CALLBACKS
# ===========================================================================
def _deeper(k):
    ss[k] = ss.get(k, 1) + 1
    _save_progress()


def _reset_kaede(k):
    ss[k] = 1
    _save_progress()


def _drill_random():
    ss.drill_emne = random.choice([k["emne"] for k in KÆDER])


# --- Eksaminér mig: shuffle-bag = træk uden tilbagelægning -----------------
def _ex_filtered():
    fag = ss.get("ex_fag", "Alle")
    ids = [p["id"] for p in POOL if fag == "Alle" or p["fag"] == fag]
    if ss.get("ex_kun_svaere"):
        sv = ss.get("ex_svaere", set())
        ids = [i for i in ids if i in sv]
    return ids


def _ex_draw():
    ids = _ex_filtered()
    if not ids:
        ss.ex_cur = None
        ss.ex_show = False
        return
    sig = (ss.get("ex_fag", "Alle"), bool(ss.get("ex_kun_svaere")))
    gyldige = set(ids)
    bag = [i for i in ss.get("ex_bag", []) if i in gyldige]
    if ss.get("ex_bag_sig") != sig or not bag:
        bag = ids[:]
        random.shuffle(bag)
        ss.ex_bag_sig = sig
    if len(bag) > 1 and bag[-1] == ss.get("ex_cur"):
        bag.insert(0, bag.pop())  # aldrig samme spørgsmål to gange i træk
    ss.ex_cur = bag.pop()
    ss.ex_bag = bag
    ss.ex_show = False


def _ex_reveal():
    ss.ex_show = True


def _ex_kunne():
    sv = ss.get("ex_svaere", set())
    sv.discard(ss.get("ex_cur"))
    ss.ex_svaere = sv
    _save_progress()
    _ex_draw()


def _ex_svaer():
    cur = ss.get("ex_cur")
    if cur:
        sv = ss.get("ex_svaere", set())
        sv.add(cur)
        ss.ex_svaere = sv
        _save_progress()
    _ex_draw()


# --- Fælde-jagt --------------------------------------------------------------
def _fj_draw():
    if not FAELDE_IDS:
        ss.fj_cur = None
        return
    bag = [i for i in ss.get("fj_bag", []) if i in set(FAELDE_IDS)]
    if not bag:
        bag = FAELDE_IDS[:]
        random.shuffle(bag)
    if len(bag) > 1 and bag[-1] == ss.get("fj_cur"):
        bag.insert(0, bag.pop())
    ss.fj_cur = bag.pop()
    ss.fj_bag = bag
    ss.fj_show = False


def _fj_reveal():
    ss.fj_show = True


def _fj_rate(kunne):
    cur = ss.get("fj_cur")
    if cur:
        sv = ss.get("ex_svaere", set())
        (sv.discard if kunne else sv.add)(cur)
        ss.ex_svaere = sv
        _save_progress()
    _fj_draw()


# --- Argumentér selv ---------------------------------------------------------
def _arg_traek():
    fag = ss.get("arg_fag", "Alle")
    kort = [k["id"] for k in ARG_KORT if fag == "Alle" or k["fag"] == fag]
    if not kort:
        ss.arg_cur = None
        return
    valg = [i for i in kort if i != ss.get("arg_cur")] or kort
    ss.arg_cur = random.choice(valg)
    ss.arg_locked = False
    ss.arg_valgt = None


def _arg_laas():
    # Gem valget nu — radio-widgetten forsvinder efter låsning, og dens
    # session-state ryddes så automatisk af Streamlit.
    ss.arg_valgt = ss.get(f"arg_pos_{ss.get('arg_cur')}")
    ss.arg_locked = True


# --- Forklar selv (Feynman) --------------------------------------------------
def _fey_skift():
    ss.fey_txt = ""  # ryd gammel forklaring, når begrebet skifter


# --- Regn --------------------------------------------------------------------
def _rt_ny():
    ss.rt_opg = regnegen.lav_opgave(ss.get("rt_fag", "Alle"))
    ss.rt_svar = ""
    ss.rt_facit = False
    ss.rt_result = None
    ss.rt_scoret = False


def _parse_tal(s):
    s = s.strip().replace(" ", "")
    cands = []
    for variant in (s.replace(",", "."), s.replace(".", "").replace(",", ".")):
        try:
            cands.append(float(variant))
        except ValueError:
            pass
    return cands


def _facit_str(opg):
    dec = opg.get("dec", 0)
    s = f"{opg['svar']:,.{dec}f}".replace(",", "§").replace(".", ",").replace("§", ".")
    return (s + " " + opg["enhed"]).strip()


# --- Faktatjek ---------------------------------------------------------------
def _fc_flip():
    ss.fc_show = not ss.get("fc_show", False)


def _fc_step(d):
    n = len(ss.get("fc_order", [])) or 1
    ss.fc_pos = (ss.get("fc_pos", 0) + d) % n
    ss.fc_show = False


def _fc_shuffle():
    orden = ss.get("fc_order", [])
    random.shuffle(orden)
    ss.fc_order = orden
    ss.fc_pos = 0
    ss.fc_show = False


def _fk_rate(kunne):
    orden = ss.get("fc_order", [])
    if not orden:
        return
    fid = orden[ss.get("fc_pos", 0) % len(orden)]
    sv = ss.get("fk_svaere", set())
    (sv.discard if kunne else sv.add)(fid)
    ss.fk_svaere = sv
    ss.fc_pos = ss.get("fc_pos", 0) + 1
    ss.fc_show = False
    _save_progress()


# --- Prøveeksamen --------------------------------------------------------------
def _sim_start():
    n = min(10, len(POOL))
    qs = []
    # Vægtet trækning: garantér mindst ét regne-, ét argument- og ét fælde-spørgsmål.
    for krav in (lambda p: p["slags"] == "regn",
                 lambda p: p["slags"] == "argument",
                 lambda p: p["snyd"]):
        kand = [p["id"] for p in POOL if krav(p) and p["id"] not in qs]
        if kand:
            qs.append(random.choice(kand))
    rest = [p["id"] for p in POOL if p["id"] not in set(qs)]
    random.shuffle(rest)
    qs += rest[:max(0, n - len(qs))]
    random.shuffle(qs)
    ss.sim_qs = qs
    ss.sim_i = 0
    ss.sim_res = {}
    ss.sim_show = False


def _sim_vis():
    ss.sim_show = True


def _sim_svar(kunne):
    qs = ss.get("sim_qs") or []
    i = ss.get("sim_i", 0)
    if i < len(qs):
        ss.sim_res[qs[i]] = kunne
        if not kunne:
            sv = ss.get("ex_svaere", set())
            sv.add(qs[i])
            ss.ex_svaere = sv
            _save_progress()
    ss.sim_i = i + 1
    ss.sim_show = False


# Klient-side 30-sek. nedtælling (pres-tilstand) — kører i browseren, uafhængigt af reruns
TIMER_HTML = """
<div id="t" style="font:600 14px -apple-system,Segoe UI,sans-serif;color:#cbd5e1">⏱️ Sig svaret højt — <span id="s">30</span>s</div>
<div style="height:8px;background:#1e293b;border-radius:6px;overflow:hidden;margin-top:5px">
 <div id="b" style="height:100%;width:100%;background:#3b82f6;transition:width 1s linear"></div></div>
<script>
(function(){var n=30,s=document.getElementById('s'),b=document.getElementById('b'),t=document.getElementById('t');
var iv=setInterval(function(){n--;if(n<=0){clearInterval(iv);s.textContent='0';b.style.width='0%';b.style.background='#ef4444';t.innerHTML='⏱️ Tiden er gået — kunne du svare flydende?';}else{s.textContent=n;b.style.width=(n/30*100)+'%';if(n<=10)b.style.background='#f59e0b';}},1000);})();
</script>
"""


def _timer_html(sekunder: int, tekst: str, slut_tekst: str) -> str:
    """Samme nedtælling, men med valgfri varighed.

    Prøveeksamen kører 30 sekunder pr. spørgsmål. Det rigtige forsvar er 30
    sammenhængende MINUTTER fordelt på faser, så uret skal kunne sættes til
    andet end 30 sekunder. Viser mm:ss når der er mere end et minut igen.
    """
    return f"""
<div id="t" style="font:600 14px -apple-system,Segoe UI,sans-serif;color:#cbd5e1">⏱️ {tekst} — <span id="s"></span></div>
<div style="height:8px;background:#1e293b;border-radius:6px;overflow:hidden;margin-top:5px">
 <div id="b" style="height:100%;width:100%;background:#3b82f6;transition:width 1s linear"></div></div>
<script>
(function(){{
  var total={int(sekunder)}, n=total;
  var s=document.getElementById('s'), b=document.getElementById('b'), t=document.getElementById('t');
  function vis(v){{
    if (v>=60) {{ var m=Math.floor(v/60), r=v%60; return m+':'+(r<10?'0':'')+r; }}
    return v+'s';
  }}
  s.textContent=vis(n);
  var iv=setInterval(function(){{
    n--;
    if(n<=0){{ clearInterval(iv); s.textContent='0s'; b.style.width='0%';
               b.style.background='#ef4444';
               t.innerHTML='⏱️ {slut_tekst}'; }}
    else {{ s.textContent=vis(n); b.style.width=(n/total*100)+'%';
            if(n<=Math.max(10, total*0.15)) b.style.background='#f59e0b'; }}
  }},1000);
}})();
</script>
"""


def _vis_pool_kort(p, vist, vis_svar_cb, kunne_cb, svaer_cb, ns):
    """Fælles kort-rendering for Eksaminér mig og Fælde-jagt (samme flow)."""
    with st.container(border=True):
        st.markdown(f"**{_fagvis(p['fag'], p['undertag'])}  ·  {p['emne']}**")
        st.markdown(f"### {p['sp']}")
        if not vist:
            st.caption("💭 Sig dit svar højt først.")
            st.button("👁️ Vis svar", on_click=vis_svar_cb, key=f"{ns}_vis")
        else:
            for lab, txt in p["reveal"]:
                st.markdown(f"**{lab}:** {txt}")
            cc1, cc2 = st.columns(2)
            cc1.button("✅ Kunne den", on_click=kunne_cb, width="stretch", key=f"{ns}_ok")
            cc2.button("🔁 Svær — igen senere", on_click=svaer_cb, width="stretch",
                       key=f"{ns}_sv")


# ===========================================================================
# RENDER
# ===========================================================================
st.title("🎓 Forsvarstræner")
st.caption("Træn til eksamen på flere måder: **🎲 Eksaminér mig** (tilfældigt på tværs af alt), "
           "**🪤 fælde-jagt** (kun snydespørgsmål), **eksaminator borer** dybere, **argumentér "
           "selv** (lås din position før svaret), **forklar selv** (Feynman), **regn** med nye "
           "tal der retter sig selv, **faktatjek** og en **⏱️ prøveeksamen** på tid. Dit "
           "fremskridt gemmes automatisk.")

st.warning(
    "**To slags spørgsmål — to slags svar:**\n\n"
    "🧩 **Bløde fag** (strategi, organisation, leverandørrelationer): her er der sjældent ét "
    "rigtigt svar — den samme leverandør kan være *strategisk* i én optik og *flaskehals* i en "
    "anden. Det tæller, at du kobler valget til modellens **kriterier** og argumenterer "
    "**konsistent** — og kan forsvare det, når eksaminator foreslår det modsatte.\n\n"
    "🔢 **Regnefag** (især økonomi og statistik): her **ER** der et rigtigt svar — en NPV eller en "
    "dækningsgrad er enten korrekt eller forkert. **Regn rigtigt** *og* kunne **fortolke** tallet. "
    "Ren fakta (fx hvad DDP betyder) er fundamentet under begge dele."
)

# --- Modulvælger (erstatter tabs, så der kan deep-linkes fra andre sider) --
# Vigtigt her: med tabs blev ALLE otte træningstilstande beregnet ved hvert
# klik. Nu køres kun den valgte.
MODULER = [
    "Eksaminér mig", "Fælde-jagt", "Eksaminator borer", "Argumentér selv",
    "Kobl fagene", "Forsvar dit valg", "Hold påstanden op",
    "Forklar selv", "Regn", "Faktatjek", "Prøveeksamen", "30-min forsvaret",
    "Hvor står jeg",
]

# Deep-link-konvention: andre sider sætter st.session_state['goto_modul']
# lige før st.switch_page — læses HER, før modulvælger-widgetten oprettes.
goto = st.session_state.pop("goto_modul", None)
if goto in MODULER:
    st.session_state["forsvar_modul"] = goto
if "forsvar_modul" not in st.session_state:
    st.session_state["forsvar_modul"] = MODULER[0]

modul = st.pills("Vælg træningstilstand", MODULER, key="forsvar_modul",
                 label_visibility="collapsed")
if modul is None:          # brugeren har klikket det valgte modul væk
    modul = MODULER[0]


# --- Eksaminér mig (interleaved, tilfældigt, aktiv genkaldelse + selvrating) ---
if modul == "Eksaminér mig":
    st.subheader("Eksaminér mig — tilfældigt på tværs af det hele")
    st.caption("Spørgsmål trækkes tilfældigt fra HELE værktøjet — nu også alle de dybe lag og "
               "fælderne fra 'Eksaminator borer'. Sig/tænk dit svar FØR du folder ud — det er "
               "genkaldelsen, der lærer dig det. Markér de svære, så de kommer igen.")

    c1, c2, c3 = st.columns([1.5, 1, 1])
    c1.selectbox("Fag", POOL_FAG, key="ex_fag", on_change=_ex_draw,
                 help="Fagene er harmoniseret — fx tæller 'Logistik' og 'Forhandling' nu med "
                      "under Indkøb og Kommunikation, så intet gemmer sig.")
    c2.checkbox("Kun de svære", key="ex_kun_svaere", help="Træn kun dem, du har markeret som svære.")
    c3.metric("Svære i kø", len(ss.get("ex_svaere", set())))

    soeg = st.text_input("…eller søg et emne at træne (fx 'kraljic', 'npv', 'zopa')",
                         key="ex_soeg").lower().strip()
    if soeg:
        hits = [p for p in POOL if soeg in (p["emne"] + " " + p["sp"] + " " + p["fag"]).lower()]
        st.caption(f"{len(hits)} spørgsmål matcher — fold ud for svaret.")
        for p in hits[:40]:
            with st.expander(f"{p['emne']}  ·  {_fagvis(p['fag'], p['undertag'])}"):
                st.markdown(p["sp"])
                for lab, txt in p["reveal"]:
                    st.markdown(f"**{lab}:** {txt}")
    else:
        st.button("🎲 Stil mig et spørgsmål", on_click=_ex_draw, type="primary")
        cur = ss.get("ex_cur")
        if not cur or cur not in POOL_BY_ID:
            st.info("Tryk på knappen — så får du et tilfældigt spørgsmål fra hele pensum. "
                    "Der trækkes uden tilbagelægning, så du kommer hele vejen rundt.")
        else:
            _vis_pool_kort(POOL_BY_ID[cur], ss.get("ex_show", False),
                           _ex_reveal, _ex_kunne, _ex_svaer, "ex")


# --- Fælde-jagt (kun snydespørgsmål) ----------------------------------------
elif modul == "Fælde-jagt":
    st.subheader("Fælde-jagt — kun snydespørgsmålene")
    st.caption(f"{len(FAELDE_IDS)} spørgsmål, hvor det intuitive svar er en fælde — præcis dem "
               "eksaminator elsker. Quick-fire: sig dit svar højt, afslør så fælden, og vær "
               "ærlig med, om du gik i den. De svære ryger i samme kø som i 🎲 Eksaminér mig.")

    if not FAELDE_IDS:
        st.info("Der er ingen fælde-spørgsmål i banken lige nu.")
    else:
        st.button("🪤 Stil mig et fælde-spørgsmål", on_click=_fj_draw, type="primary")
        cur = ss.get("fj_cur")
        if not cur or cur not in POOL_BY_ID:
            st.info("Tryk på knappen — og husk: hvis svaret føles helt oplagt, er det nok "
                    "netop fælden.")
        else:
            _vis_pool_kort(POOL_BY_ID[cur], ss.get("fj_show", False),
                           _fj_reveal, lambda: _fj_rate(True), lambda: _fj_rate(False), "fj")


# --- Dybde-drill -----------------------------------------------------------
elif modul == "Eksaminator borer":
    st.subheader("Eksaminator borer dybere")
    st.caption("Vælg et emne. Læs spørgsmålet, formulér dit svar højt eller i hovedet, fold så "
               "“Sådan kan du argumentere” ud — og tryk **Bor dybere** for næste, sværere lag. "
               "Hvor langt du er nået, huskes — også efter genstart.")

    if st.checkbox("⏱️ Pres-tilstand — sig svaret højt på tid", key="drill_pres"):
        components.html(TIMER_HTML, height=60)

    emner = [k["emne"] for k in KÆDER]
    st.caption(f"{len(KÆDER)} emner at blive eksamineret i — vælg ét, eller få et tilfældigt.")
    dc1, dc2 = st.columns([3, 1])
    valg = dc1.selectbox("Emne at forsvare", emner, key="drill_emne")
    dc2.button("🎲 Tilfældigt emne", on_click=_drill_random, width="stretch")
    kaede = next(k for k in KÆDER if k["emne"] == valg)
    nkey = f"drill_n_{valg}"
    if nkey not in ss:
        ss[nkey] = 1
    n = min(ss[nkey], len(kaede["lag"]))

    st.caption(f"Fag: {_fagvis(*_norm_fag(kaede['fag']))}  ·  lag {n} af {len(kaede['lag'])}")

    for i in range(n):
        L = kaede["lag"][i]
        # Bemærk: ingen "snyd"-mærke på selve spørgsmålet — fælden må ikke afsløres,
        # før man har svaret. Den indrømmes først i svaret nedenfor.
        maerke = "  📌 *fakta*" if L.get("fakta") else ""
        with st.container(border=True):
            st.markdown(f"**Lag {i + 1} — eksaminator:** {L['sp']}{maerke}")
            with st.expander("💬 Sådan kan du argumentere"):
                if L.get("snyd"):
                    st.markdown("🪤 **Det her var et snydespørgsmål** — det intuitive svar er en "
                                "fælde. Sådan griber du det rigtigt an:")
                st.markdown(L["arg"])
                if L.get("alt"):
                    st.markdown(f"🔄 **Kan også forsvares:** {L['alt']}")
                if L.get("fisker"):
                    st.info(f"💡 **Hvad eksaminator fisker efter:** {L['fisker']}")

    c1, c2 = st.columns(2)
    if ss[nkey] < len(kaede["lag"]):
        c1.button("Bor dybere ↓", key=f"deep_{valg}", on_click=_deeper, args=(nkey,),
                  width="stretch")
    else:
        c1.success("Du er nået til bunden af emnet 🎯", icon="✅")
    c2.button("↺ Forfra", key=f"reset_{valg}", on_click=_reset_kaede, args=(nkey,),
              width="stretch")


# --- Argumentér selv -------------------------------------------------------
elif modul == "Argumentér selv":
    st.subheader("Argumentér selv — “det afhænger”")
    st.caption("Samme situation kan forsvares flere veje. Træk en case, **vælg din position og "
               "lås den** — først derefter ser du, hvordan positionerne kan forsvares. Det "
               "tvungne valg er selve træningen: til eksamen skal du også lægge dig fast, før "
               "censor svarer igen.")

    ac1, ac2 = st.columns([1.5, 1])
    ac1.selectbox("Fag", ARG_FAG, key="arg_fag", on_change=_arg_traek,
                  help="Vælg et fag at træne cases i — eller 'Alle' for at blive udfordret bredt.")
    ac2.button("🎲 Træk en case", on_click=_arg_traek, type="primary", width="stretch")

    kort = ARG_BY_ID.get(ss.get("arg_cur"))
    if not kort:
        st.info(f"Tryk '🎲 Træk en case' — der ligger {len(ARG_KORT)} cases klar, hvor flere "
                "svar kan forsvares.")
    else:
        a = kort["case"]
        with st.container(border=True):
            st.markdown(f"**{_fagvis(kort['fag'], kort['undertag'])}  ·  {kort['titel']}**")
            st.markdown(a["situation"])
            st.markdown(f"❓ **{a['spm']}**")
            navne = [p["navn"] for p in a["positioner"]] + ["Min egen vinkel"]
            if not ss.get("arg_locked"):
                st.radio("Hvilken position vælger du?", navne, key=f"arg_pos_{kort['id']}",
                         help="Bestem dig, FØR du ser argumenterne — det er commitment, "
                              "der gør genkaldelsen effektiv.")
                st.button("🔒 Lås mit valg", on_click=_arg_laas, type="primary")
            else:
                valgt = ss.get("arg_valgt") or navne[0]
                st.caption(f"🔒 Du valgte: **{valgt}**")
                for p in a["positioner"]:
                    if p["navn"] == valgt:
                        st.markdown(f"✔ **{p['navn']}** *(dit valg)* — {p['arg']}")
                    else:
                        st.markdown(f"**{p['navn']}** — {p['arg']}")
                if valgt == "Min egen vinkel":
                    st.caption("Du valgte din egen vinkel — hold din begrundelse op mod "
                               "positionerne ovenfor: dækker den samme kriterier?")
                st.success(f"🎯 {a['pointe']}")
                st.button("🎲 Næste case", on_click=_arg_traek)


# --- Forklar selv (Feynman) ------------------------------------------------
elif modul == "Forklar selv":
    st.subheader("Forklar selv (Feynman)")
    st.caption("Forklar begrebet i helt enkle ord, som om modparten aldrig har hørt om det. "
               "Kan du ikke forklare det simpelt, ved du det ikke endnu. Sammenlign så med "
               "modelsvaret.")
    fey_emner = sorted({p["emne"] for p in KONCEPT})
    valg = st.selectbox("Vælg et begreb at forklare", fey_emner, key="fey_emne",
                        on_change=_fey_skift)
    item = next(p for p in KONCEPT if p["emne"] == valg)
    st.markdown(f"**Forklar:** {valg}  ·  *{item['fag']}*")
    st.text_area("Din forklaring (skriv — eller sig den højt og spring feltet over)",
                 key="fey_txt", height=130,
                 placeholder="Forklar det som til en, der aldrig har hørt om det…")
    with st.expander("Vis modelsvar — sammenlign med din forklaring"):
        st.markdown(item["svar"])
        if item.get("fisker"):
            st.info(f"💡 {item['fisker']}")


# --- Regn (auto-træning + gennemregnede eksempler) -------------------------
elif modul == "Regn":
    st.subheader("Regn — her ER der et rigtigt svar")
    mode = st.radio("Tilstand", ["🎯 Træn med nye tal (auto)", "📖 Gennemgå eksempler"],
                    key="regn_mode", horizontal=True)
    st.divider()

    if mode.startswith("🎯"):
        st.caption("Friske opgaver med tilfældige tal, der **retter sig selv** mod værktøjets egne "
                   "formler. Uendeligt mange — træn til metoden sidder fast. Tryk **Enter** i "
                   "svarfeltet for at tjekke.")
        if "rt_opg" not in ss:
            ss.rt_opg = regnegen.lav_opgave(ss.get("rt_fag", "Alle"))
        c1, c2 = st.columns([1, 1])
        c1.selectbox("Fag", ["Alle"] + regnegen.FAG_LISTE, key="rt_fag", on_change=_rt_ny)
        c2.button("🎲 Ny opgave", on_click=_rt_ny, width="stretch")
        opg = ss.rt_opg
        score = ss.get("rt_score", dict(_TOM_SCORE))
        with st.container(border=True):
            st.markdown(f"**{opg['fag']}  ·  {opg['emne']}**")
            st.markdown(f"### {opg['sp']}")
            enhed = f" ({opg['enhed']})" if opg["enhed"] else ""
            with st.form("rt_form", border=False):
                svar_input = st.text_input(
                    f"Dit svar{enhed}", key="rt_svar", placeholder="Skriv et tal …",
                    help="Dansk talformat er fint (fx 1.250 eller 20,9) — og Enter tjekker svaret.")
                b1, b2 = st.columns(2)
                tjek = b1.form_submit_button("✅ Tjek svar", width="stretch")
                givop = b2.form_submit_button("👁️ Vis facit (giv op)", width="stretch")
            if tjek:
                cands = _parse_tal(svar_input)
                if not cands:
                    st.warning("Skriv et tal først (fx 894 eller 20,9).")
                else:
                    rigtig = any(abs(c - opg["svar"]) <= opg["tol"] for c in cands)
                    ss.rt_facit = True
                    ss.rt_result = "rigtigt" if rigtig else "forkert"
                    if not ss.get("rt_scoret"):  # samme opgave tæller kun én gang
                        ss.rt_scoret = True
                        if rigtig:
                            score["rigtige"] += 1
                            score["streak"] += 1
                            score["bedste"] = max(score["bedste"], score["streak"])
                        else:
                            score["forkerte"] += 1
                            score["streak"] = 0
                        ss.rt_score = score
                        _save_progress()
            elif givop:
                ss.rt_facit = True
                ss.rt_result = None
                if not ss.get("rt_scoret"):
                    ss.rt_scoret = True
                    score["streak"] = 0  # at give op nulstiller stimen, men tæller ikke forkert
                    ss.rt_score = score
                    _save_progress()
            if ss.get("rt_facit"):
                res = ss.get("rt_result")
                if res == "rigtigt":
                    st.success(f"✅ Rigtigt! Facit: {_facit_str(opg)}")
                elif res == "forkert":
                    st.error(f"❌ Ikke helt. Facit: {_facit_str(opg)}")
                else:
                    st.info(f"Facit: {_facit_str(opg)}")
                st.markdown(f"**Udregning:** {opg['metode']}")
                if opg.get("fortolk"):
                    st.markdown(f"**Fortolkning:** {opg['fortolk']}")
                if opg.get("faelde"):
                    st.warning(f"⚠️ **Typisk fælde:** {opg['faelde']}")
        score = ss.get("rt_score", dict(_TOM_SCORE))
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("✅ Rigtige", score["rigtige"])
        m2.metric("❌ Forkerte", score["forkerte"])
        m3.metric("🔥 Stime", score["streak"], help="Rigtige svar i træk lige nu.")
        m4.metric("🏆 Bedste stime", score["bedste"])
    else:
        st.caption("Færdige, gennemregnede eksempler med fortolkning og typisk fælde — "
                   "censur-kontrolleret mod dine egne formler.")
        regn_fag = list(dict.fromkeys(_norm_fag(it["fag"])[0] for it in REGN))
        c1, c2 = st.columns([2, 1])
        rsoeg = c1.text_input("Søg (fx 'npv', 'konfidens', 'eoq', 'oee')",
                              key="regn_soeg").lower().strip()
        rfag = c2.selectbox("Fag", ["Alle"] + regn_fag, key="regn_fag")
        vist = 0
        for it in REGN:
            if rfag != "Alle" and _norm_fag(it["fag"])[0] != rfag:
                continue
            hay = (it["emne"] + " " + it["sp"] + " " + " ".join(it["soeg"])).lower()
            if rsoeg and rsoeg not in hay:
                continue
            vist += 1
            with st.container(border=True):
                st.markdown(f"**{it['emne']}**  ·  *{_fagvis(*_norm_fag(it['fag']))}*")
                st.markdown(it["sp"])
                with st.expander("Vis det rigtige svar + udregning"):
                    st.success(f"**Svar:** {it['svar']}")
                    st.markdown(f"**Udregning:** {it['metode']}")
                    if it.get("fortolk"):
                        st.markdown(f"**Fortolkning:** {it['fortolk']}")
                    if it.get("faelde"):
                        st.warning(f"⚠️ **Typisk fælde:** {it['faelde']}")
        if vist == 0:
            st.info("Ingen opgaver matchede. Prøv et andet ord, eller vælg 'Alle' fag.")


# --- Faktatjek (flashcards med fag og kunne/svær-bunker) --------------------
elif modul == "Faktatjek":
    st.subheader("Faktatjek")
    st.caption("Det her ER fakta — fundamentet du argumenterer ovenpå. Forsiden er begrebet; "
               "vend kortet for definitionen. Markér kunne/svær, så de svære samler sig i en "
               "bunke, du kan træne for sig.")

    fk1, fk2, fk3 = st.columns([1.5, 1, 1])
    fk1.selectbox("Fag", FAKTA_FAG, key="fk_fag",
                  help="Fagene er sat automatisk ud fra kortets nøgleord.")
    fk2.checkbox("Kun de svære", key="fk_kun_svaere",
                 help="Vis kun de kort, du har markeret som svære.")
    fk3.metric("Svære kort", len(ss.get("fk_svaere", set())))

    fk_fag = ss.get("fk_fag", "Alle")
    fk_sv = ss.get("fk_svaere", set())
    fk_ids = [k["id"] for k in FAKTA_KORT
              if (fk_fag == "Alle" or k["fag"] == fk_fag)
              and (not ss.get("fk_kun_svaere") or k["id"] in fk_sv)]

    if not fk_ids:
        st.info("Ingen kort matcher — slå 'Kun de svære' fra, eller vælg et andet fag.")
    else:
        if set(ss.get("fc_order", [])) != set(fk_ids):
            gamle = [i for i in ss.get("fc_order", []) if i in set(fk_ids)]
            ss.fc_order = gamle + [i for i in fk_ids if i not in set(gamle)]
            ss.fc_pos = min(ss.get("fc_pos", 0), len(ss.fc_order) - 1)
        ss.fc_pos = ss.get("fc_pos", 0) % len(ss.fc_order)
        kortet = FAKTA_BY_ID[ss.fc_order[ss.fc_pos]]

        with st.container(border=True):
            st.markdown(f"### {kortet['forside']}")
            st.caption(f"Fag: {kortet['fag']}"
                       + ("  ·  🔁 i din svær-bunke" if kortet["id"] in fk_sv else ""))
            if ss.get("fc_show"):
                st.success(kortet["bagside"])
                r1, r2 = st.columns(2)
                r1.button("✅ Kunne den", on_click=_fk_rate, args=(True,), width="stretch")
                r2.button("🔁 Svær — igen senere", on_click=_fk_rate, args=(False,),
                          width="stretch")
            else:
                st.caption("🤔 Hvad betyder det? Sig det højt — og vend så kortet.")

        c1, c2, c3, c4 = st.columns(4)
        c1.button("⬅️ Forrige", on_click=_fc_step, args=(-1,), width="stretch")
        c2.button("🔄 Vend kort", on_click=_fc_flip, width="stretch")
        c3.button("➡️ Næste", on_click=_fc_step, args=(1,), width="stretch")
        c4.button("🔀 Bland", on_click=_fc_shuffle, width="stretch")
        st.caption(f"Kort {ss.fc_pos + 1} af {len(ss.fc_order)}")


# --- Prøveeksamen -----------------------------------------------------------
elif modul == "Prøveeksamen":
    st.subheader("Prøveeksamen — 10 spørgsmål på tid")

    if not ss.get("sim_qs"):
        st.caption("10 spørgsmål trukket på tværs af hele pensum — altid mindst ét "
                   "regnespørgsmål, én argument-case og ét fælde-spørgsmål. 30 sekunder pr. "
                   "spørgsmål, som ved det rigtige forsvar. Til sidst får du en opsummering, "
                   "og de svære ryger i din svær-kø.")
        st.button("▶️ Start prøveeksamen", on_click=_sim_start, type="primary")
    elif ss.get("sim_i", 0) >= len(ss.sim_qs):
        kunne_n = sum(1 for v in ss.get("sim_res", {}).values() if v)
        svaere = [q for q in ss.sim_qs if ss.get("sim_res", {}).get(q) is False]
        st.markdown("### Din prøveeksamen er slut 🎓")
        r1, r2 = st.columns(2)
        r1.metric("✅ Kunne", kunne_n)
        r2.metric("🔁 Svære", len(svaere))
        if svaere:
            st.markdown("**Til svær-køen** (kommer igen i 🎲 Eksaminér mig og 🪤 Fælde-jagt):")
            for q in svaere:
                if q in POOL_BY_ID:
                    p = POOL_BY_ID[q]
                    st.markdown(f"- {p['emne']}  ·  *{_fagvis(p['fag'], p['undertag'])}*")
        else:
            st.success("Alle spørgsmål sad lige i skabet 🎉")
        st.button("↺ Ny prøveeksamen", on_click=_sim_start)
    else:
        i = ss.sim_i
        q = ss.sim_qs[i]
        p = POOL_BY_ID.get(q)
        if p is None:  # banken er ændret midt i sessionen — spring spørgsmålet over
            ss.sim_i = i + 1
            st.rerun()
        else:
            st.progress((i + 1) / len(ss.sim_qs), text=f"Spørgsmål {i + 1} af {len(ss.sim_qs)}")
            if not ss.get("sim_show"):
                components.html(TIMER_HTML, height=60)
            with st.container(border=True):
                st.markdown(f"**{_fagvis(p['fag'], p['undertag'])}  ·  {p['emne']}**")
                st.markdown(f"### {p['sp']}")
                if not ss.get("sim_show"):
                    st.caption("💭 Svar højt inden tiden løber ud — og vis så svaret.")
                    st.button("👁️ Vis svar", on_click=_sim_vis, key="sim_vis")
                else:
                    for lab, txt in p["reveal"]:
                        st.markdown(f"**{lab}:** {txt}")
                    sc1, sc2 = st.columns(2)
                    sc1.button("✅ Kunne den", on_click=_sim_svar, args=(True,),
                               width="stretch", key="sim_ok")
                    sc2.button("🔁 Svær — igen senere", on_click=_sim_svar, args=(False,),
                               width="stretch", key="sim_sv")


# ===========================================================================
# KOBL FAGENE — den tilstand prøveformen decideret kalder på
# ===========================================================================
elif modul == "Kobl fagene":
    st.subheader("Kobl fagene — spørgsmål der ikke kan besvares fra ét fag")
    st.caption(
        "Prøven er tværfaglig: fire fag afgøres i én prøve, og casen kræver, "
        "at transportansvar og projektstyring kobles på det samme flow som "
        "Lean, Chopra og lagerdesign. Her er situationer, hvor ét fag ikke "
        "rækker. Sig dit svar højt, FØR du folder modelsvaret ud — og læg "
        "mærke til, om du selv kom hele vejen rundt.")

    if "kob_i" not in ss:
        ss.kob_i = 0
        ss.kob_vist = False

    def _kob_næste():
        ss.kob_i = (ss.kob_i + 1) % len(KOBLINGER)
        ss.kob_vist = False

    def _kob_tilfældig():
        ss.kob_i = random.randrange(len(KOBLINGER))
        ss.kob_vist = False

    situation, fag, spørgsmål, svar = KOBLINGER[ss.kob_i]

    with st.container(border=True):
        st.markdown(" · ".join(f"`{f}`" for f in fag))
        st.markdown(f"### {situation}")
        st.markdown("**Eksaminator spørger:**")
        for s in spørgsmål:
            st.markdown(f"- {s}")

        if not ss.kob_vist:
            st.caption(f"💭 Svar højt. Mindst **{len(fag)} fag** skal med, "
                       "før svaret er helt.")
            st.button("Vis hvordan koblingen hænger sammen",
                      on_click=lambda: ss.update(kob_vist=True),
                      type="primary", key="kob_vis")
        else:
            st.success(svar)
            k1, k2, k3 = st.columns(3)
            k1.button("✅ Jeg fik alle fag med", on_click=_kob_næste,
                      width="stretch", key="kob_ok")

            def _kob_svær():
                for f in fag:
                    _notér_svaghed(f, "Tværfaglig kobling")
                _kob_næste()

            k2.button("🔁 Jeg manglede et fag", on_click=_kob_svær,
                      width="stretch", key="kob_sv")
            k3.button("🎲 Tilfældig", on_click=_kob_tilfældig,
                      width="stretch", key="kob_rnd")

    st.caption(f"Kort {ss.kob_i + 1} af {len(KOBLINGER)}")


# ===========================================================================
# FORSVAR DIT VALG — du forsvarer din EGEN rapport, ikke pensum
# ===========================================================================
elif modul == "Forsvar dit valg":
    st.subheader("Forsvar dit valg — «hvorfor ikke det modsatte?»")
    st.caption(
        "Til det mundtlige forsvarer du **din egen rapport**, ikke pensum. "
        "Den klassiske åbning er «du valgte X — hvorfor ikke Y?». Kortene "
        "træner formen: vælg position, begrund den, anerkend afvejningen "
        "ærligt, og hold fast. Det svageste svar er at benægte ulempen.")

    if "vlg_i" not in ss:
        ss.vlg_i = 0
        ss.vlg_vist = False

    def _vlg_næste():
        ss.vlg_i = (ss.vlg_i + 1) % len(VALG)
        ss.vlg_vist = False

    valg, alternativ, modspørgsmål, forsvar = VALG[ss.vlg_i]

    with st.container(border=True):
        st.markdown(f"### {valg}")
        st.markdown(f"Eksaminator: *«Hvorfor ikke {alternativ}?»*")
        for m in modspørgsmål:
            st.markdown(f"- {m}")

        if not ss.vlg_vist:
            st.caption("💭 Svar højt. Husk de fire trin: position → "
                       "begrundelse → anerkend prisen → hvad ville ændre din "
                       "anbefaling.")
            st.button("Vis et stærkt forsvar",
                      on_click=lambda: ss.update(vlg_vist=True),
                      type="primary", key="vlg_vis")
        else:
            st.success(forsvar)
            v1, v2 = st.columns(2)
            v1.button("✅ Mit svar holdt", on_click=_vlg_næste,
                      width="stretch", key="vlg_ok")

            def _vlg_svær():
                _notér_svaghed("Projektstyring", "Forsvar af eget valg")
                _vlg_næste()

            v2.button("🔁 Jeg vaklede", on_click=_vlg_svær,
                      width="stretch", key="vlg_sv")

    st.caption(f"Kort {ss.vlg_i + 1} af {len(VALG)}")


# ===========================================================================
# HOLD PÅSTANDEN OP — kildekritik, semestrets kerne
# ===========================================================================
elif modul == "Hold påstanden op":
    st.subheader("Hold påstanden op — holder den, eller gør den ikke?")
    st.caption(
        "Semestret er bygget på kritisk tænkning, og fagets eget AI-oplæg "
        "lærer at fange en hallucination, før den ender i afleveringen. "
        "Herunder står en påstand. **Nogle er rigtige.** Døm først — så "
        "afsløres det, om der var plantet en fejl, og hvilken type.")

    if "pst_raek" not in ss:
        ss.pst_raek = random.sample(range(len(PAASTANDE)), len(PAASTANDE))
        ss.pst_pos = 0
        ss.pst_valg = None

    def _pst_næste():
        ss.pst_pos = (ss.pst_pos + 1) % len(ss.pst_raek)
        ss.pst_valg = None

    def _pst_dom(holder: bool):
        ss.pst_valg = holder

    idx = ss.pst_raek[ss.pst_pos]
    påstand, holder, fejltype, forklaring, p_fag = PAASTANDE[idx]

    with st.container(border=True):
        st.markdown(f"`{p_fag}`")
        st.markdown(f"### «{påstand}»")

        if ss.pst_valg is None:
            st.caption("💭 Fire spørgsmål til enhver påstand: Hvad bygger den "
                       "på? Er tallet efterprøveligt? Er årsag og virkning "
                       "byttet om? Bruges modellen inden for sit "
                       "gyldighedsområde?")
            d1, d2 = st.columns(2)
            d1.button("✅ Den holder", on_click=_pst_dom, args=(True,),
                      width="stretch", key="pst_ja")
            d2.button("❌ Der er noget galt", on_click=_pst_dom, args=(False,),
                      width="stretch", key="pst_nej")
        else:
            rigtigt = (ss.pst_valg == holder)
            if rigtigt:
                st.success("Rigtigt vurderet.")
            else:
                st.error("Ikke helt — læs hvorfor.")
                _notér_svaghed(p_fag, "Kildekritik")

            if not holder:
                st.markdown(f"**Fejltype:** {fejltype}")
            st.info(forklaring)
            st.button("Næste påstand →", on_click=_pst_næste, type="primary",
                      key="pst_n")

    st.caption(f"Påstand {ss.pst_pos + 1} af {len(PAASTANDE)} · "
               f"{sum(1 for p in PAASTANDE if p[1])} af dem er korrekte")


# ===========================================================================
# 30-MIN FORSVARET — generalprøven i prøvens faktiske form
# ===========================================================================
elif modul == "30-min forsvaret":
    st.subheader("30-minutters forsvaret — generalprøven")
    st.caption(
        "Prøveeksamen træner hurtig genkaldelse: 10 spørgsmål à 30 sekunder, "
        "cirka fem minutter i alt. Det rigtige forsvar er **30 "
        "sammenhængende minutter** over én case. Det er en anden disciplin — "
        "her er udholdenhed og struktur det svære, ikke paratviden.")

    FASER = [
        ("Præsentation", 5,
         "Fortæl om din løsning uden at læse op. Hvad var problemet, hvad "
         "valgte du, og hvorfor?",
         ["Hold dig til hovedlinjen — detaljerne kommer i uddybningen.",
          "Sig konklusionen først, ikke til sidst.",
          "Nævn selv den vigtigste afvejning, du har truffet."]),
        ("Uddybning", 10,
         "Eksaminator borer i det, du lige sagde. Regn med, at det svageste "
         "led i din præsentation er dét, der spørges til.",
         ["Har du regnet noget, så kend både formlen og fortolkningen.",
          "«Det afhænger af…» er et godt svar — hvis du siger hvad.",
          "Ved du det ikke, så sig det, og sig hvordan du ville finde ud af det."]),
        ("Tværfaglig kobling", 10,
         "Nu skal fagene bindes sammen. Casen er tværfaglig, og det er her, "
         "karakteren adskiller sig.",
         ["Kobl mindst to fag i hvert svar — flowet, jura'en, projektet, økonomien.",
          "Brug 'Kobl fagene'-tilstanden til at træne netop det.",
          "Peg selv på sammenhænge, eksaminator ikke har spurgt til."]),
        ("Kritisk indvending", 5,
         "«Hvorfor ikke det modsatte?» Til sidst presses din anbefaling.",
         ["Anerkend ulempen ærligt — benægtelse er det svageste svar.",
          "Sig hvad der skulle ændre sig, for at du ville vælge om.",
          "Hold fast i din position, når begrundelsen stadig holder."]),
    ]

    if "fs_fase" not in ss:
        ss.fs_fase = -1          # -1 = ikke startet

    def _fs_start():
        ss.fs_fase = 0

    def _fs_næste():
        ss.fs_fase += 1

    def _fs_stop():
        ss.fs_fase = -1

    if ss.fs_fase < 0:
        st.markdown(
            "| Fase | Tid | Hvad der sker |\n|---|---|---|\n"
            + "\n".join(f"| **{n}** | {m} min | {b} |"
                        for n, m, b, _ in FASER))
        st.info("Find din egen case eller rapport frem, og sig svarene **højt**. "
                "Uret kører i browseren, så det påvirkes ikke af, at siden "
                "genindlæser.")
        st.button("▶️ Start forsvaret", on_click=_fs_start, type="primary")
    elif ss.fs_fase >= len(FASER):
        st.markdown("### Forsvaret er slut 🎓")
        st.caption("Tag stilling til det med det samme, mens det er friskt.")
        for navn, _m, _b, _r in FASER:
            st.checkbox(f"«{navn}» gik fint", key=f"fs_ok_{navn}")
        svage = [n for n, _m, _b, _r in FASER if not ss.get(f"fs_ok_{n}")]

        def _fs_gem():
            for n in svage:
                _notér_svaghed("Projektstyring", f"Forsvar: {n}")
            _fs_stop()

        if svage:
            st.warning("Du markerede ikke: " + " · ".join(svage))
        st.button("Gem i svaghedsprofilen og afslut", on_click=_fs_gem,
                  type="primary")
    else:
        navn, minutter, brief, råd = FASER[ss.fs_fase]
        st.markdown(f"### Fase {ss.fs_fase + 1} af {len(FASER)} · {navn}")
        components.html(
            _timer_html(minutter * 60, f"{navn} ({minutter} min)",
                        f"{navn} er slut — gå videre til næste fase."),
            height=60)
        st.markdown(brief)
        with st.expander("Hvad eksaminator lytter efter"):
            for r in råd:
                st.markdown(f"- {r}")
        f1, f2 = st.columns(2)
        f1.button("Næste fase →", on_click=_fs_næste, type="primary",
                  width="stretch", key="fs_n")
        f2.button("Afbryd", on_click=_fs_stop, width="stretch", key="fs_stop")


# ===========================================================================
# HVOR STÅR JEG — dækningskort + fælles svaghedsprofil
# ===========================================================================
elif modul == "Hvor står jeg":
    st.subheader("Hvor står jeg")
    st.caption(
        "Ærlig status, ikke opmuntring. Prøven afgør 20 ECTS på én gang — "
        "Distribution (7), SCM (5), transportjura (4) og projektstyring (4) — "
        "så et fag der er tyndt dækket her, er også tyndt dækket til "
        "eksamen.")

    st.markdown("#### Dine svageste emner på tværs af alle tilstande")
    top = _svagheds_top(10)
    if not top:
        st.info("Endnu ingen registrerede svagheder. De samler sig, når du "
                "markerer noget som svært i træningstilstandene — og de "
                "tælles nu på tværs, så en svaghed fundet i Regn også dukker "
                "op i de andre tilstande.")
    else:
        for fag, emne, antal in top:
            st.markdown(f"- **{emne}** · `{fag}` — gået galt {antal} "
                        f"{'gang' if antal == 1 else 'gange'}")
        st.caption("Start næste session dér, hvor listen er længst.")

    st.markdown("#### Dækning pr. fag i prøven")
    _dæk = {}
    for _p in POOL:
        for _f in ([_p["fag"]] if isinstance(_p.get("fag"), str) else _p.get("fag", [])):
            _dæk[_f] = _dæk.get(_f, 0) + 1
    for _k in KOBLINGER:
        for _f in _k[1]:
            _dæk[_f] = _dæk.get(_f, 0) + 1

    # Prøvens fire fag, ikke værktøjets sider. SCM undervises ikke som ét
    # fag i værktøjet — stoffet ligger spredt i Indkøb og Produktion, så de
    # tælles sammen her.
    PRØVEFAG = [
        ("Distribution", 7, ["Distribution"]),
        ("Supply Chain Management", 5, ["Indkøb", "Produktion"]),
        ("Transportjura", 4, ["Jura"]),
        ("Projektstyring", 4, ["Projektstyring"]),
    ]
    _maks = max((sum(_dæk.get(k, 0) for k in kilder)
                 for _n, _e, kilder in PRØVEFAG), default=1) or 1
    for navn, ects, kilder in PRØVEFAG:
        antal = sum(_dæk.get(k, 0) for k in kilder)
        pr_ects = antal / ects if ects else 0
        st.markdown(f"**{navn}** · {ects} ECTS — {antal} spørgsmål "
                    f"({pr_ects:.1f}".replace(".", ",") + " pr. ECTS)")
        st.progress(min(1.0, antal / _maks))
    st.caption(
        "Søjlerne er antal spørgsmål i banken pr. fag — ikke din kunnen. Er "
        "en søjle kort, er det **værktøjet** der mangler stof, ikke dig. "
        "Kolonnen «pr. ECTS» er den ærlige: den viser, om dækningen står mål "
        "med, hvor meget faget vejer til prøven.")


st.divider()
with st.expander("🗑️ Nulstil fremskridt"):
    st.caption("Sletter din svær-kø, drill-dybde, faktatjek-bunker og regn-score — både i "
               "appen og i den gemte fil (data/forsvar_progress.json). Kan ikke fortrydes.")
    if st.checkbox("Ja, jeg er sikker", key="nulstil_ok"):
        st.button("Slet alt fremskridt", on_click=_nulstil_fremskridt, type="primary")

_n_lag = sum(len(k["lag"]) for k in KÆDER)
st.caption(f"🤖 Bygget med Claude. Banken lige nu: {len(KONCEPT)} forsvarsspørgsmål, "
           f"{len(KÆDER)} dybde-kæder med {_n_lag} lag (heraf {len(FAELDE_IDS)} fælder), "
           f"{len(ARGUMENTER)} argumentér-selv-cases, {len(FAKTA_KORT)} faktakort og "
           f"{len(REGN)} gennemregnede opgaver — {len(POOL)} spørgsmål i den blandede pool, "
           f"alle censur-kontrolleret. Regnetræneren laver uendeligt mange nye opgaver, der "
           f"retter sig selv mod dine egne formler. Dit fremskridt gemmes automatisk i "
           f"data/forsvar_progress.json.")
