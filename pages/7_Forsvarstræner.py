"""Forsvarstræner — træn det mundtlige eksamensforsvar.

Læreren vil høre HVORFOR. Der er sjældent ét rigtigt svar — samme leverandør kan
være strategisk i én optik og flaskehals i en anden; det afgørende er argumentet
og at man kan forsvare det, når eksaminator borer dybere. Værktøjet har tre
tilstande: dybde-drill (eksaminator borer lag for lag), argumentér-selv (samme
situation kan forsvares flere veje), og faktatjek (det der ER fakta og skal sidde
fast — fundamentet man argumenterer ovenpå).
"""
import os
import sys

import streamlit as st

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random  # noqa: E402
import streamlit.components.v1 as components  # noqa: E402

from ui_theme import inject_css  # noqa: E402
from regn_data import REGN  # noqa: E402
from pakke_spoergsmaal import KONCEPT  # noqa: E402
from pakke_kaeder import EKSTRA_KAEDER  # noqa: E402
from pakke_argumenter import EKSTRA_ARGUMENTER  # noqa: E402
from pakke_fakta import EKSTRA_FAKTA  # noqa: E402
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
KÆDER = KÆDER + EKSTRA_KAEDER

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
ARGUMENTER = ARGUMENTER + EKSTRA_ARGUMENTER

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
# CALLBACKS
# ===========================================================================
def _deeper(k):
    ss[k] = ss.get(k, 1) + 1


def _reset_kaede(k):
    ss[k] = 1


def _drill_random():
    ss.drill_emne = random.choice([k["emne"] for k in KÆDER])


def _fc_flip():
    ss.fc_show = not ss.get("fc_show", False)


def _fc_step(d):
    ss.fc_pos = (ss.get("fc_pos", 0) + d) % len(FAKTA)
    ss.fc_show = False


def _fc_shuffle():
    random.shuffle(ss.fc_order)
    ss.fc_pos = 0
    ss.fc_show = False


# ===========================================================================
# SAMLET POOL til "Eksaminér mig" (interleaved på tværs af alt)
# ===========================================================================
def _build_pool():
    pool = []
    for q in KONCEPT:
        rev = [("Svar", q["svar"])]
        if q.get("alt"):
            rev.append(("Kan også forsvares", q["alt"]))
        if q.get("fisker"):
            rev.append(("Hvad eksaminator fisker efter", q["fisker"]))
        pool.append({"id": f"k{len(pool)}", "fag": q["fag"], "emne": q["emne"],
                     "sp": q["sp"], "reveal": rev})
    for it in REGN:
        pool.append({"id": f"r{len(pool)}", "fag": it["fag"], "emne": it["emne"], "sp": it["sp"],
                     "reveal": [("Svar", it["svar"]), ("Udregning", it["metode"]),
                                ("Fortolkning", it["fortolk"]), ("Typisk fælde", it["faelde"])]})
    for a in ARGUMENTER:
        rev = [(p["navn"], p["arg"]) for p in a["positioner"]]
        rev.append(("Pointe", a["pointe"]))
        pool.append({"id": f"a{len(pool)}", "fag": a["fag"].split("·")[0].strip(),
                     "emne": a["fag"], "sp": a["situation"] + "\n\n**" + a["spm"] + "**",
                     "reveal": rev})
    for kæde in KÆDER:
        L = kæde["lag"][0]
        pool.append({"id": f"d{len(pool)}", "fag": kæde["fag"], "emne": kæde["emne"],
                     "sp": L["sp"], "reveal": [("Sådan kan du argumentere", L["arg"])]})
    return pool


POOL = _build_pool()
POOL_BY_ID = {p["id"]: p for p in POOL}
POOL_FAG = ["Alle"] + sorted({p["fag"] for p in POOL})


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
    cur = ss.get("ex_cur")
    valg = [i for i in ids if i != cur] or ids
    ss.ex_cur = random.choice(valg)
    ss.ex_show = False


def _ex_reveal():
    ss.ex_show = True


def _ex_kunne():
    sv = ss.get("ex_svaere", set())
    sv.discard(ss.get("ex_cur"))
    ss.ex_svaere = sv
    _ex_draw()


def _ex_svaer():
    cur = ss.get("ex_cur")
    if cur:
        sv = ss.get("ex_svaere", set())
        sv.add(cur)
        ss.ex_svaere = sv
    _ex_draw()


def _rt_ny():
    ss.rt_opg = regnegen.lav_opgave(ss.get("rt_fag", "Alle"))
    ss.rt_svar = ""
    ss.rt_facit = False
    ss.rt_result = None


def _rt_facit():
    ss.rt_facit = True


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


# ===========================================================================
# RENDER
# ===========================================================================
st.title("🎓 Forsvarstræner")
st.caption("Træn til eksamen på flere måder: **🎲 Eksaminér mig** (tilfældigt på tværs af alt), "
           "**eksaminator borer** dybere, **argumentér selv**, **forklar selv** (Feynman), "
           "**regn** med nye tal der retter sig selv, og **faktatjek**. Den generelle udgave af "
           "din gamle case-forsvarstræner.")

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

tab_ex, tab_drill, tab_arg, tab_feyn, tab_regn, tab_fakta = st.tabs([
    "🎲 Eksaminér mig", "🎤 Eksaminator borer", "⚖️ Argumentér selv",
    "🗣️ Forklar selv", "🔢 Regn", "🧠 Faktatjek",
])


# --- Eksaminér mig (interleaved, tilfældigt, aktiv genkaldelse + selvrating) ---
with tab_ex:
    st.subheader("Eksaminér mig — tilfældigt på tværs af det hele")
    st.caption("Spørgsmål trækkes tilfældigt fra HELE værktøjet (modeller, begreber, værdikæde, "
               "nøgletal, statistik). Sig/tænk dit svar FØR du folder ud — det er genkaldelsen, "
               "der lærer dig det. Markér de svære, så de kommer igen.")

    c1, c2, c3 = st.columns([1.5, 1, 1])
    c1.selectbox("Fag", POOL_FAG, key="ex_fag")
    c2.checkbox("Kun de svære", key="ex_kun_svaere", help="Træn kun dem, du har markeret som svære.")
    c3.metric("Svære i kø", len(ss.get("ex_svaere", set())))

    soeg = st.text_input("…eller søg et emne at træne (fx 'kraljic', 'npv', 'zopa')",
                         key="ex_soeg").lower().strip()
    if soeg:
        hits = [p for p in POOL if soeg in (p["emne"] + " " + p["sp"] + " " + p["fag"]).lower()]
        st.caption(f"{len(hits)} emner matcher — fold ud for svaret.")
        for p in hits[:40]:
            with st.expander(f"{p['emne']}  ·  {p['fag']}"):
                st.markdown(p["sp"])
                for lab, txt in p["reveal"]:
                    st.markdown(f"**{lab}:** {txt}")
    else:
        st.button("🎲 Stil mig et spørgsmål", on_click=_ex_draw, type="primary")
        cur = ss.get("ex_cur")
        if not cur:
            st.info("Tryk på knappen — så får du et tilfældigt spørgsmål fra hele pensum.")
        else:
            p = POOL_BY_ID[cur]
            with st.container(border=True):
                st.markdown(f"**{p['fag']}  ·  {p['emne']}**")
                st.markdown(f"### {p['sp']}")
                if not ss.get("ex_show"):
                    st.caption("💭 Sig dit svar højt først.")
                    st.button("👁️ Vis svar", on_click=_ex_reveal)
                else:
                    for lab, txt in p["reveal"]:
                        st.markdown(f"**{lab}:** {txt}")
                    cc1, cc2 = st.columns(2)
                    cc1.button("✅ Kunne den", on_click=_ex_kunne, use_container_width=True)
                    cc2.button("🔁 Svær — igen senere", on_click=_ex_svaer, use_container_width=True)


# --- Dybde-drill -----------------------------------------------------------
with tab_drill:
    st.subheader("Eksaminator borer dybere")
    st.caption("Vælg et emne. Læs spørgsmålet, formulér dit svar højt eller i hovedet, fold så "
               "“Sådan kan du argumentere” ud — og tryk **Bor dybere** for næste, sværere lag.")

    if st.checkbox("⏱️ Pres-tilstand — sig svaret højt på tid", key="drill_pres"):
        components.html(TIMER_HTML, height=60)

    emner = [k["emne"] for k in KÆDER]
    st.caption(f"{len(KÆDER)} emner at blive eksamineret i — vælg ét, eller få et tilfældigt.")
    dc1, dc2 = st.columns([3, 1])
    valg = dc1.selectbox("Emne at forsvare", emner, key="drill_emne")
    dc2.button("🎲 Tilfældigt emne", on_click=_drill_random, use_container_width=True)
    kæde = next(k for k in KÆDER if k["emne"] == valg)
    nkey = f"drill_n_{valg}"
    if nkey not in ss:
        ss[nkey] = 1
    n = min(ss[nkey], len(kæde["lag"]))

    st.caption(f"Fag: {kæde['fag']}  ·  lag {n} af {len(kæde['lag'])}")

    for i in range(n):
        L = kæde["lag"][i]
        # Bemærk: ingen "snyd"-mærke på selve spørgsmålet — fælden må ikke afsløres,
        # før man har svaret. Den indrømmes først i svaret nedenfor.
        mærke = "  📌 *fakta*" if L.get("fakta") else ""
        with st.container(border=True):
            st.markdown(f"**Lag {i + 1} — eksaminator:** {L['sp']}{mærke}")
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
    if ss[nkey] < len(kæde["lag"]):
        c1.button("Bor dybere ↓", key=f"deep_{valg}", on_click=_deeper, args=(nkey,),
                  use_container_width=True)
    else:
        c1.success("Du er nået til bunden af emnet 🎯", icon="✅")
    c2.button("↺ Forfra", key=f"reset_{valg}", on_click=_reset_kaede, args=(nkey,),
              use_container_width=True)


# --- Argumentér selv -------------------------------------------------------
with tab_arg:
    st.subheader("Argumentér selv — “det afhænger”")
    st.caption("Samme situation kan forsvares flere veje. Bestem dig for ét svar og din "
               "begrundelse, før du folder ud — og se så, hvordan *begge* positioner kan holde.")

    for j, a in enumerate(ARGUMENTER):
        with st.container(border=True):
            st.markdown(f"**{a['fag']}**")
            st.markdown(a["situation"])
            st.markdown(f"❓ **{a['spm']}**")
            with st.expander("Vis mulige argumenter"):
                for p in a["positioner"]:
                    st.markdown(f"**{p['navn']}** — {p['arg']}")
                st.success(f"🎯 {a['pointe']}")


# --- Forklar selv (Feynman) ------------------------------------------------
with tab_feyn:
    st.subheader("Forklar selv (Feynman)")
    st.caption("Forklar begrebet i helt enkle ord, som om modparten aldrig har hørt om det. "
               "Kan du ikke forklare det simpelt, ved du det ikke endnu. Sammenlign så med "
               "modelsvaret.")
    fey_emner = sorted({p["emne"] for p in KONCEPT})
    valg = st.selectbox("Vælg et begreb at forklare", fey_emner, key="fey_emne")
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
with tab_regn:
    st.subheader("Regn — her ER der et rigtigt svar")
    mode = st.radio("Tilstand", ["🎯 Træn med nye tal (auto)", "📖 Gennemgå eksempler"],
                    key="regn_mode", horizontal=True)
    st.divider()

    if mode.startswith("🎯"):
        st.caption("Friske opgaver med tilfældige tal, der **retter sig selv** mod værktøjets egne "
                   "formler. Uendeligt mange — træn til metoden sidder fast.")
        if "rt_opg" not in ss:
            ss.rt_opg = regnegen.lav_opgave(ss.get("rt_fag", "Alle"))
        c1, c2 = st.columns([1, 1])
        c1.selectbox("Fag", ["Alle"] + regnegen.FAG_LISTE, key="rt_fag", on_change=_rt_ny)
        c2.button("🎲 Ny opgave", on_click=_rt_ny, use_container_width=True)
        opg = ss.rt_opg
        with st.container(border=True):
            st.markdown(f"**{opg['fag']}  ·  {opg['emne']}**")
            st.markdown(f"### {opg['sp']}")
            enhed = f" ({opg['enhed']})" if opg["enhed"] else ""
            svar_input = st.text_input(f"Dit svar{enhed}", key="rt_svar", placeholder="Skriv et tal …")
            b1, b2 = st.columns(2)
            tjek = b1.button("✅ Tjek svar", use_container_width=True)
            b2.button("Vis facit (giv op)", on_click=_rt_facit, use_container_width=True)
            if tjek:
                cands = _parse_tal(svar_input)
                if not cands:
                    st.warning("Skriv et tal først (fx 894 eller 20,9).")
                else:
                    ss.rt_facit = True
                    ss.rt_result = ("rigtigt" if any(abs(c - opg["svar"]) <= opg["tol"]
                                                     for c in cands) else "forkert")
            if ss.get("rt_facit"):
                res = ss.get("rt_result")
                if res == "rigtigt":
                    st.success(f"✅ Rigtigt! Facit: {_facit_str(opg)}")
                elif res == "forkert":
                    st.error(f"❌ Ikke helt. Facit: {_facit_str(opg)}")
                else:
                    st.info(f"Facit: {_facit_str(opg)}")
                st.markdown(f"**Udregning:** {opg['metode']}")
    else:
        st.caption("Færdige, gennemregnede eksempler med fortolkning og typisk fælde — "
                   "censur-kontrolleret mod dine egne formler.")
        regn_fag = list(dict.fromkeys(it["fag"] for it in REGN))
        c1, c2 = st.columns([2, 1])
        rsoeg = c1.text_input("Søg (fx 'npv', 'konfidens', 'eoq', 'oee')",
                              key="regn_soeg").lower().strip()
        rfag = c2.selectbox("Fag", ["Alle"] + regn_fag, key="regn_fag")
        vist = 0
        for it in REGN:
            if rfag != "Alle" and it["fag"] != rfag:
                continue
            hay = (it["emne"] + " " + it["sp"] + " " + " ".join(it["soeg"])).lower()
            if rsoeg and rsoeg not in hay:
                continue
            vist += 1
            with st.container(border=True):
                st.markdown(f"**{it['emne']}**  ·  *{it['fag']}*")
                st.markdown(it["sp"])
                with st.expander("Vis det rigtige svar + udregning"):
                    st.success(f"**Svar:** {it['svar']}")
                    st.markdown(f"**Udregning:** {it['metode']}")
                    st.markdown(f"**Fortolkning:** {it['fortolk']}")
                    st.warning(f"⚠️ **Typisk fælde:** {it['faelde']}")
        if vist == 0:
            st.info("Ingen opgaver matchede. Prøv et andet ord, eller vælg 'Alle' fag.")


# --- Faktatjek (flashcards) ------------------------------------------------
with tab_fakta:
    st.subheader("Faktatjek")
    st.caption("Det her ER fakta — fundamentet du argumenterer ovenpå. Forsiden er begrebet; "
               "vend kortet for definitionen.")

    if "fc_order" not in ss:
        ss.fc_order = list(range(len(FAKTA)))
        ss.fc_pos = 0
        ss.fc_show = False

    idx = ss.fc_order[ss.fc_pos % len(FAKTA)]
    forside, bagside = FAKTA[idx]

    with st.container(border=True):
        st.markdown(f"### {forside}")
        if ss.fc_show:
            st.success(bagside)
        else:
            st.caption("🤔 Hvad betyder det? Sig det højt — og vend så kortet.")

    c1, c2, c3, c4 = st.columns(4)
    c1.button("⬅️ Forrige", on_click=_fc_step, args=(-1,), use_container_width=True)
    c2.button("🔄 Vend kort", on_click=_fc_flip, use_container_width=True)
    c3.button("➡️ Næste", on_click=_fc_step, args=(1,), use_container_width=True)
    c4.button("🔀 Bland", on_click=_fc_shuffle, use_container_width=True)
    st.caption(f"Kort {(ss.fc_pos % len(FAKTA)) + 1} af {len(FAKTA)}")


st.divider()
st.caption("🤖 Bygget med Claude. Spørgsmålsbanken dækker hele værktøjet (68 forsvarsspørgsmål "
           "+ 36 gennemregnede opgaver, alle censur-kontrolleret) og regnetræneren laver "
           "uendeligt mange nye opgaver, der retter sig selv mod dine egne formler. De svære, du "
           "markerer i 🎲 Eksaminér mig, holdes i kø under sessionen. Sig til, hvis du vil have "
           "endnu flere emner eller dine egne case-spørgsmål ind.")
