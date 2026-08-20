"""Påstande til kildekritik-tilstanden i Forsvarstræneren.

Hvorfor
-------
Semestret er bygget på kritisk tænkning, og fagets eget AI-oplæg lærer fire
spørgsmål til ethvert svar plus hvordan man fanger en hallucination, før den
ender i afleveringen. Værktøjet trænede det ingen steder: Fælde-jagt tester
*spørgsmål* med forkert præmis, men ikke *påstande* og *kilder*.

Formatet
--------
(påstand, holder_den, hvad_der_er_galt, hvad_der_faktisk_gælder, fag)

  holder_den   True  = påstanden er korrekt som den står
               False = der er plantet en fejl

Fejltyperne er bevidst de fire, man reelt møder: et forkert tal, en opdigtet
kilde, ombyttet årsag og virkning, og en model brugt uden for sit
gyldighedsområde. Nogle påstande ER rigtige — ellers lærer man bare at svare
"forkert" hver gang, og så træner tilstanden mistro i stedet for vurdering.

Ingen virksomheds- eller personnavne.
"""

PAASTANDE = [
    # --- ombyttet årsag og virkning ---------------------------------------
    ("Jo højere udnyttelsesgrad på maskinerne, jo kortere gennemløbstid — "
     "fordi der bliver produceret mere pr. time.",
     False,
     "Årsag og virkning er byttet om.",
     "Det modsatte gælder. Presses udnyttelsen mod 100 %, vokser køen — og "
     "dermed gennemløbstiden — eksplosivt. Sammenhængen er ikke lineær, den "
     "er en hockeystav, og det er hele grundlaget for QRM's krav om "
     "reservekapacitet. Travlhed er ikke det samme som hastighed.",
     "Produktion"),

    ("Kanban egner sig bedst, når efterspørgslen svinger meget, fordi "
     "systemet reagerer automatisk på forbruget.",
     False,
     "Modellen er vendt på hovedet.",
     "Kanban forudsætter nogenlunde **jævnt** træk. Svinger efterspørgslen, "
     "vokser antallet af nødvendige kort, og lagrene med. Systemet *reagerer* "
     "på forbrug — det *forudsiger* ikke — og netop dét er QRM's kritik af "
     "kanban ved høj variation.",
     "Distribution"),

    # --- forkert tal / forkert regel --------------------------------------
    ("Fragtførerens ansvar dækker godsets fakturaværdi, når skaden sker "
     "under transporten.",
     False,
     "Forkert grundlag for erstatningen.",
     "Ansvarsgrænsen er **vægtbaseret**, ikke værdibaseret — et beløb pr. kilo "
     "opgjort i SDR. Let og dyrt gods er derfor systematisk underdækket. "
     "Konklusionen på en godsskade-opgave er sjældent «fragtføreren betaler», "
     "men «fragtføreren betaler en brøkdel, resten skulle have været "
     "forsikret».",
     "Jura"),

    ("Ved CIF bærer sælgeren risikoen for godset helt frem til "
     "destinationshavnen, eftersom det er sælger, der betaler fragten.",
     False,
     "Risiko og omkostning forveksles.",
     "Det er C-gruppens klassiske fælde. Ved CIF betaler sælger ganske rigtigt "
     "fragt og forsikring frem til destinationshavnen, men **risikoen går "
     "over allerede ved afskibningen**. Et tab undervejs er dermed købers, "
     "selvom sælger stod for transporten. De to punkter er forskellige.",
     "Jura"),

    ("En Euro 6-lastbil udleder mindre CO₂ end en Euro 4-lastbil, fordi "
     "normen er skærpet.",
     False,
     "Forkert forureningstype.",
     "Euro-normerne regulerer **luftforurening** — især NOx og partikler — "
     "ikke CO₂. CO₂ følger brændstofforbruget og energikilden. En Euro 6-bil "
     "er renere i byluften, men ikke nødvendigvis mindre klimabelastende.",
     "Distribution"),

    # --- opdigtet kilde ----------------------------------------------------
    ("Ifølge Rushton et al. (2019) faldt distributionsomkostningerne med "
     "23,7 % efter automatisering af lageret.",
     False,
     "Kilden ser rigtig ud, men er opdigtet.",
     "Det er fagets eget eksempel på en hallucination: forfatter, år, "
     "procenttal og resultat lyder fagligt overbevisende og er fri fantasi. "
     "Et præcist tal med en præcis kilde er ikke bevis — det er dét, der "
     "skal tjekkes først. Slå kilden op, eller lad være med at bruge tallet.",
     "Distribution"),

    # --- model uden for sit gyldighedsområde ------------------------------
    ("De fem Lean-principper kan tages i den rækkefølge, der passer "
     "virksomheden bedst.",
     False,
     "Rækkefølgen er en del af modellen.",
     "Principperne forudsætter hinanden: værdi → værdistrøm → flow → pull → "
     "perfektion. Indfører man pull uden først at have skabt flow, vokser "
     "lagrene i stedet for at falde — pull uden flow er bare et lager med et "
     "nyt navn.",
     "Produktion"),

    ("EOQ-formlen kan bruges direkte til at bestemme seriestørrelsen i egen "
     "produktion.",
     False,
     "Forkert formel til situationen.",
     "EOQ antager, at hele ordren lander på lageret på én gang. Produceres "
     "varerne løbende, mens de også forbruges, er det **POQ/EPQ**, der "
     "gælder — det maksimale lager bliver lavere, og den optimale serie "
     "større. Bruger man EOQ, overvurderer man lageromkostningen.",
     "Indkøb"),

    ("Little's Law kan bruges til at beregne gennemløbstiden midt i en "
     "ordrepukkel.",
     False,
     "Modellens forudsætning er ikke opfyldt.",
     "Little's Law gælder for et system i **ligevægt over tid**. Måler man "
     "midt i en pukkel, får man et tal, der ser rigtigt ud, men ikke "
     "beskriver noget stabilt. Formlen er ikke forkert — situationen er.",
     "Produktion"),

    ("Et projekt kan planlægges i detaljer fra start, når blot man er "
     "grundig nok i opstartsprocessen.",
     False,
     "Overser opgavens karakter.",
     "Det afhænger af, hvor opgaven ligger i kendt/ukendt-matricen. Er både "
     "hvad og hvordan kendt, kan den detailplanlægges — det er "
     "rutineprojektet. Er vejen ukendt, kan den ikke, uanset grundighed, og "
     "så peger modellen på en agil eller blandet tilgang.",
     "Projektstyring"),

    # --- korrekte påstande — ellers trænes mistro, ikke vurdering ---------
    ("Ved søfragt regnes 1 m³ som 1.000 kg i fragtberegningen, hvis vægten "
     "er lavere.",
     True,
     None,
     "Korrekt — det er den klassiske **measureton** (w/m). Fragtgrundlaget er "
     "det største af faktisk vægt og volumenvægt, og for søfragt er "
     "omregningen 1:1 pr. kubikmeter. Let, voluminøst gods betaler dermed "
     "for pladsen, ikke for vægten.",
     "Distribution"),

    ("En reduktion af skibets fart på omkring 10 % kan give omkring 20-25 % "
     "lavere brændstofforbrug.",
     True,
     None,
     "Korrekt — det er **slow steaming**, og det er søfartens stærkeste "
     "enkeltgreb mod CO₂. Sammenhængen mellem fart og forbrug er ikke "
     "lineær, og derfor giver en beskeden fartnedsættelse en stor "
     "brændstofbesparelse. Prisen er længere transittid, som skal dækkes af "
     "lager eller planlægning.",
     "Distribution"),

    ("Projektlederen har typisk ikke formel instruktionsbeføjelse over "
     "deltagerne i projektgruppen.",
     True,
     None,
     "Korrekt, og det er selve kernen i faget. Den midlertidige organisation "
     "lever inde i den permanente, deltagerne er udlånt fra driften og har to "
     "chefer. Derfor handler projektledelse mere om forhandling og "
     "styregruppe-brug end om kommando.",
     "Projektstyring"),

    ("Aggregering betyder, at det samlede sikkerhedslager falder, når man "
     "samler lagrene færre steder.",
     True,
     None,
     "Korrekt. Usikkerheden i den samlede efterspørgsel er mindre end summen "
     "af usikkerhederne hvert sted, så sikkerhedslageret falder mindre end "
     "proportionalt med antallet af lagre. Det er den reelle gevinst ved "
     "centralisering — modvægten er længere svartid og højere udgående "
     "transport.",
     "Distribution"),

    ("Et ordrekvalificerende krav vinder ikke ordren i sig selv.",
     True,
     None,
     "Korrekt. Ordrekvalificerende krav er adgangsbilletten — uden dem er man "
     "ude, men de skaber ikke salget. Det gør **ordrevinderne**. Forskellen "
     "er vigtig i en case: at forbedre noget ordrekvalificerende ud over "
     "markedets niveau koster penge uden at give ordrer.",
     "Indkøb"),

    ("Lean og JIT er to ord for det samme.",
     False,
     "Begreberne blandes sammen.",
     "JIT er et **værktøj inden for** Lean — princippet om at producere først, "
     "når der trækkes. Lean er den bredere tankegang med fem principper, "
     "hvor JIT hører til under flow og pull. Man kan sagtens køre JIT uden at "
     "være Lean, og Lean rummer meget mere end JIT.",
     "Produktion"),

    ("Ved multimodal transport gælder ét samlet regelsæt for hele rejsen.",
     False,
     "Forkert antagelse om regelgrundlaget.",
     "Konventionen følger **transportformen**, ikke sendingen. Skaden kan "
     "falde ind under CMR på vejstrækningen og Haag-Visby til søs, og "
     "grænserne er vidt forskellige. Kan skadestidspunktet ikke fastslås, "
     "bliver det et bevisspørgsmål — og det er ofte dér, sagen afgøres.",
     "Jura"),

    ("Servicegrad på 100 % bør altid være målet, når kunden er vigtig.",
     False,
     "Ignorerer omkostningskurven.",
     "Sammenhængen er eksponentiel: de sidste procenter kræver "
     "uforholdsmæssigt meget sikkerhedslager. 100 % er ikke et mål, det er en "
     "regning. Det rigtige spørgsmål er, hvad en manglende leverance "
     "faktisk koster — og om variationen i leveringstiden kan reduceres i "
     "stedet.",
     "Indkøb"),
]
