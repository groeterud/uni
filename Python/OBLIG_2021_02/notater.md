programmstruktur

Tk()-main vindu 
    - eksamensvisninger - messagebox for question: en dag eller periode?
      - skriv inn dato, om tom sluttdato vis for en dag. Listbox med oppdatert info om rom, dato og emne når man trykker på den. kan legge til eksamensresultater på den eksamen man velger. 
        - eksamensresultatvindu: legg til resultat for valgt eksamen, få opp "ok" når det er registrert resultat, 
    - ajourholding
      - listbox over eksamener etter dagens sortert med nærmeste øverst
        - legg til ny eksamen: opprett ny eksamen på dato og rom
        - slett valgt eksamen 
        - endre valgt eksamen 
    -  Karakterliste
       -  Listbox med emnenavn, knapp: print karakterer for valgt emne
          -  messagebox eller nytt vindu med listbox med karakterer for emnmet.
    - Karakterstatistikk
      - Skriv inn emnekode, få opp alle eksamener med emnekoden. Velg en eksamen og trykk, vis statistikk. 
        - Viser emneopplysninger og karakterfordeling (antall kandidater på hver karakter)
    - Eksamensresultater per student
      - Skriv inn studentnr
        - Inneholder emnenavn og antall studiepoeng for studenten
        - Ordnet etter eksamensdato
    - Vitnemål
      - Skriv inn studentnr
        - Få beste resultat per avlagte eksamen
        - Emnene storters på fagnivå og emnekode (PRG1000 før PRG2000 etc)
        - Vitnemålet må ha en summering av antall oppnådde studiepoeng for beståtte emner. 