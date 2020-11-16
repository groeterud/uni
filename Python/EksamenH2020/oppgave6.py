def hunder_fra_kennel():
    #bool som holder koll på om vi fant kennel eller ikke
    funnet_kennel=False 
    #henter kennel navn som bruker skal få utfall på
    search=input('Skriv inn navn på kennelen for å skrive ut alle hunder registrert på oppdretteren: ')

    #henter ut relevant informasjon fra oppdretterfila
    oppdretterFil=open('oppdretter.txt','r')
    post_oppdretterID=oppdretterFil.readline()
    #while løkke for å gå gjennom fila og tilordne oppdretterID
    while post_oppdretterID!='':
        #leser posten 
        post_kennelNavn=oppdretterFil.readline()
        post_kennelEierFornavn=oppdretterFil.readline()
        post_kennelEierEtternavn=oppdretterFil.readline()

        #rstripper kennelNavn for å kunne sammenligne
        post_kennelNavn=post_kennelNavn.rstrip('\n')

        #dersom vi får en treff på kennelnavnet
        if post_kennelNavn==search:
            funnet_kennel=True
            #rstripper relevante dataposter
            post_oppdretterID=post_oppdretterID.rstrip('\n')
            #Vi trenger å ta vare på oppdretterID for å knytte sammen
            oppdretterID=post_oppdretterID
           
        #dytter løkka videre 
        post_oppdretterID=oppdretterFil.readline()
    #lukker fila asap
    oppdretterFil.close()

    if funnet_kennel==False:
        print('Fant ikke kennelen, vennligst sjekk at du skrev navnet korrekt')
    else:
        #vi skal nå hive all hundeinformasjon direkte tilknyttet kennelen inn i en liste
        hundeListe=[]

        #bool for å se om vi fant en hund tilknyttet kennelen
        funnet_hund=False

        hundeFil=open('hund.txt','r')

        hundeID=hundeFil.readline()

        #while løkke for å gå gjennom fila
        while hundeID!='':
            #leser resten av posten
            post_oppdretterID=hundeFil.readline()
            post_hundeeierID=hundeFil.readline()
            post_navn=hundeFil.readline()
            post_kjonn=hundeFil.readline()
            post_fodt=hundeFil.readline()

            #fjerner linjeskift på relevant postdata for å kunne lese data på en enklere måte
            post_oppdretterID=post_oppdretterID.rstrip('\n')
            post_hundeeierID=post_hundeeierID.rstrip('\n')
            post_navn=post_navn.rstrip('\n')
            post_kjonn=post_kjonn.rstrip('\n')
            post_fodt=post_fodt.rstrip('\n')

            #vi sjekker om posten vi er på er en av kennelen sine hunder
            if post_oppdretterID==oppdretterID:
                funnet_hund=True
                #hiver all relevant informasjon fra hunden inn i listen
                hundeListe+=[post_hundeeierID]
                hundeListe+=[post_navn]
                hundeListe+=[post_kjonn]
                hundeListe+=[post_fodt]
            

            #leser neste linje slik at løkka går rundt
            hundeID=hundeFil.readline()
        #lukker fila så tidlig som mulig
        hundeFil.close()

        if funnet_hund==False:
            print('Beklager, fant ingen hunder tilknyttet denne kennelen.')
        else:
            #hiver alle eierdata inn i en liste for bruk senere.
            eierListe=[]
            eierFil=open('hundeeier.txt','r')

            post_hundeeierID=eierFil.readline()

            #løkke for å gå gjennom fila og hive fildata inn i eierListe
            while post_hundeeierID!='':
                #leser posten
                post_fornavn=eierFil.readline()
                post_etternavn=eierFil.readline()

                #stripper linjeskift
                post_hundeeierID=post_hundeeierID.rstrip('\n')
                post_fornavn=post_fornavn.rstrip('\n')
                post_etternavn=post_etternavn.rstrip('\n')

                #legger post inn i liste
                eierListe+=[post_hundeeierID]
                eierListe+=[post_fornavn]
                eierListe+=[post_etternavn]

                #dytter løkka videre
                post_hundeeierID=eierFil.readline()
            #lukker asap
            eierFil.close()

            #formaterring for sluttprint
            print()
            print('Under følger alle hunder registrert på',search) #search = navn på kennelen
            print()
            #for løkka for å skrive ut relevant info for hunden, hopper med 4 fordi vi skal bare lese hundeEierID
            for x in range(0,len(hundeListe),4):
                print('Hundens navn:',hundeListe[x+1])
                print('kjønn:',hundeListe[x+2])
                print('Født:',hundeListe[x+3])

                #for løkke for å finne eiers informasjon, hopper med 3 ettersom vi bare skal sammenligne hundeEierID
                for n in range(0,len(eierListe),3):                
                    if eierListe[n]==hundeListe[x]:
                        print('Eiers fornavn:',eierListe[n+1])
                        print('Eiers etternavn:',eierListe[n+2])
                        print()

hunder_fra_kennel()
print('Program avsluttet')