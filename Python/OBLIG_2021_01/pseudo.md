# Pseudo for obligen. 

## Tanker
Forvent tanker, programlogikk og rasjonalisering. 
IKKE forvent funksjonell kode. Selv om kode kan eksistere der syntax-messig fremgangsmåte virker difus for underskrevne. 

### Ressurser

https://tkdocs.com/tutorial/widgets.html

### Formalia

Leveringen skal bestå av følgende filer, det skal ikke leveres zip-fil:
- Programkode som Python fil dvs .py
- Programkode kopiert inn i word/annen tekstbehandler og lagret som .docx, eller .odt

Filnavnene skal ha følgende struktur:

- PRG1100-Oblig1-<dine initialer>, initialene med STORE BOKSTAVER

Eksempel, innleveringen til studenten Kari Villikke blir da følgende filer:
- PRG1100-Oblig1-KV.py
- PRG1100-Oblig1-KV.docx eller PRG1100-Oblig1-KV.odt

## Oppgavetekst
Det skal programmeres et grafisk brukergrensesnitt for billånskalkulator, obligatorisk oppgave 1 PRG1000 høsten 2020. Det skal tas utgangspunkt i funksjonsorientert kode fra denne innleveringen, men det stilles krav til at denne koden forbedres slik at kalkulatoren alltid beregner riktig resultat.

### Tips til arbeidsrekkefølge:

1. Lag et eget program av kalkulatoren fra i høst, som du kan forbedre. Arbeid med dette programmet med et tekstbasert grensesnitt.
2. Lag et eget program for det grafiske brukergrensesnittet til kalkulatoren (med bare ledetekster, inndatafelter, utdatafelter, knapper osv) hvor du arbeider med layout til du er fornøyd.
3. Når kalkulatoren i program 1 fungerer riktig, og du er fornøyd med layout'n i program 2, så setter du disse sammen i et nytt program hvor programmet i program 1 blir en funksjon i det nye programmet som kalles ved f eks å trykke på en knapp "Beregn lånetilsagn". Her må du knytte GUI-lag og funksjonalitet sammen med get'ere og set'ere.



## Tenkte endringer:

### kalkulatoren
Kast vekk while løkka, GUI vinduet håndterer det. 
Omstrukturer slik at alle inputs går via StringVar() inputs fra TKinter/GUI. 
**SJEKK GRENSVERDIER SÅ DU ALLTID HAR RIKTIG RESULTAT**

### GUI/Tkinter
Vil wireframe/tegne en plan for GUI helt enkelt. 


## Lett pseudo for funksjonalitet:
inputs fra tkinter entrys
    få inn ønsket nedbetalingstid 
    få inn eksisterende egenkap
    få inn ønsket nedbetalignstid

beregn egenkap prosenten iht formalia

hiv eksisterende beregnings-kode inn i en def som get'er og set'er basert (trigges av tkinter knapp 'beregn')

output fra def inn i tkinter. 



