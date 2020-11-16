def registrer_ny_hund():
    funnet_oppdrett=False #bool for å se om vi har funnet kennel
    
    print('Velkommen til registrering av ny hund')
    #starter med å lete etter oppdretterID, så vi etterspør det.
    search_oppdretterID=input('Skriv inn din oppdretterID for å starte: ')

    #åpner oppdrettfila for å lete igjennom den
    oppdrettFil=open('oppdretter.txt','r')

    #starter med å lese gjennom poster
    oppdretterID=oppdrettFil.readline()

    #while løkke for å gå gjennom fila 
    while oppdretterID!='':
        #leser inn resten av posten
        kennelnavn=oppdrettFil.readline()
        kenneleier_fornavn=oppdrettFil.readline()
        kenneleier_etternavn=oppdrettFil.readline()

        #rstripper linjeskift så vi kan sammenligned data
        oppdretterID=oppdretterID.rstrip('\n')
        
        #sjekker om oppdretterID er den samme som brukeren skrev inn
        if oppdretterID==search_oppdretterID:
            funnet_oppdrett=True

        #leser neste linje så loopen går
        oppdretterID=oppdrettFil.readline()
    
    #lukker fila så fort vi kan
    oppdrettFil.close()

    if funnet_oppdrett==True:
        funnet_eier=False #bool for å se om vi har funnet eier
        print('Oppdretter funnet.')
        #henter input på eiers ID
        search_hundeEierID=input('Vennligst skriv inn HundeeierID for verifikasjon: ')

        #åpner fila for å gå gjennom den
        eierFil=open('hundeeier.txt','r')
        hundeEierID=eierFil.readline()

        #while løkke for å gå gjennom fila 
        while hundeEierID!='':
            fornavn=eierFil.readline()
            etternavn=eierFil.readline()

            #fjerner linjeskift på hundeEierID for å sammenligne
            hundeEierID=hundeEierID.rstrip()

            #sammenligner input og data fra post
            if hundeEierID==search_hundeEierID:
                funnet_eier=True
            
            #beveger løkka videre
            hundeEierID=eierFil.readline()
        #lukker åpen fil asap
        eierFil.close()

        if funnet_eier==True:
            print('Eier funnet. Registrering av hund kan nå påbegynnes')
            funnet_hund=False #bool for å se om vi prøver å registrere en hund som allerede er registrert      
            #etterspørr hundeID
            search_hundeID=input('Vennligst skriv inn hundeID på hunden du ønsker å registrere: ')

            #åpner hund.txt for å se om hunden allerede er registrert
            hundeFil=open('hund.txt','r')      

            hundeID=hundeFil.readline()

            #while løkke for å gå gjennom fila post for post
            while hundeID!='':
                #leser inn posten
                oppdretterID=hundeFil.readline()
                hundeEierID=hundeFil.readline()
                navn=hundeFil.readline()
                kjonn=hundeFil.readline()
                fodt=hundeFil.readline()

                #fjerner linjeskift for å kunne sammenligne
                hundeID=hundeID.rstrip('\n')

                #sjekker om input matcher hundeID
                if hundeID==search_hundeID:
                    funnet_hund=True
                #beveger løkka videre    
                hundeID=hundeFil.readline()
            #lukker hundefil etter løkka
            hundeFil.close()

            if funnet_hund==True:
                print('Beklager, kan ikke registrere en hund som allerede er registrert.')
            else:
                #henter gjennværende input fra bruker
                navn=input('Hva er navnet på hunden? ')
                kjonn=input('Hva er hundens kjønn? ')
                fodt=input('Når er hunden født? ')

                #åpner hund.txt i append modus for å kunne skrive data til fil.
                hundeFil=open('hund.txt','a')

                #skriver all data til fil
                hundeFil.write(search_hundeID+'\n')
                hundeFil.write(search_oppdretterID+'\n')
                hundeFil.write(search_hundeEierID+'\n')
                hundeFil.write(navn+'\n')
                hundeFil.write(kjonn+'\n')
                hundeFil.write(fodt+'\n')

                #lukker fila
                hundeFil.close()

                print('Hunden er registrert')

        #else til funnet_eier==True    
        else:
            print('Beklager, eier ikke funnet. Vennligst registrert eier først. ')

    #else til funnet_oppdrett==True
    else:
        print('Beklager, kan ikke registrere ny hund før oppdretter er registrert.')
registrer_ny_hund()
print('Program avsluttet')