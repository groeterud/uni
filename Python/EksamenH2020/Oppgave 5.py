import os

def slett_hundeier():  
    #input fra bruker
    search_hundeEierID=input('Skriv inn id på eieren du ønsker å slette: ')

    #bool for å se om vi fant bruker
    funnet_eier=False

    hundeFil=open('hund.txt','r')

    hundeID=hundeFil.readline()

    #while løkke for å gå gjennom fila
    while hundeID!='':
        #leser resten av posten
        oppdretterID=hundeFil.readline()
        hundeeierID=hundeFil.readline()
        navn=hundeFil.readline()
        kjonn=hundeFil.readline()
        fodt=hundeFil.readline()

        hundeeierID=hundeeierID.rstrip('\n')
       
        if hundeeierID==search_hundeEierID:
            funnet_eier=True
        
        #leser neste linje slik at løkka går rundt
        hundeID=hundeFil.readline()
    #lukker fila så tidlig som mulig
    hundeFil.close()


    if funnet_eier==True:
        print('Kan ikke slette eier da det er registrert en hund på eieren')
    else:
        #lager tempfil for å hive inn data vi ikke skal slette
        tempfil=open('temp.txt','w')
        #åpner eierfila
        eierFil=open('hundeeier.txt','r')

        hundeeierID=eierFil.readline()
        #while løkke for å gå gjennom fila post for post
        while hundeeierID!='':
            fornavn=eierFil.readline()
            etternavn=eierFil.readline()

            #stripper linjeskift fra hundeeierID for å sjekke om det er den vi er ute etter å slette. 
            hundeeierID=hundeeierID.rstrip('\n')

            #om hundeeierID IKKE er den vi vil slette, så skriver vi posten til tempfila. 
            if hundeeierID!=search_hundeEierID:
                tempfil.write(hundeeierID+'\n')
                tempfil.write(fornavn)
                tempfil.write(etternavn)
            
            #beveger løkka videre
            hundeeierID=eierFil.readline()
        
        #stenger begge filene
        tempfil.close()
        eierFil.close()

        #sletter gamle eierfil
        os.remove('hundeeier.txt')
        #endrer navn på temp fila til hundeier.txt - vi har nå fjernet posten vi ønsket å fjerne
        os.rename('temp.txt','hundeeier.txt')

        print('Eieren har blitt slettet')
slett_hundeier()
print('Program avsluttet')