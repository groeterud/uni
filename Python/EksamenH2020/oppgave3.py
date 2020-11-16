hundeListe=[]

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

    #fjerner linjeskift for å kunne lese data på en enklere måte
    hundeID=hundeID.rstrip('\n')
    oppdretterID=oppdretterID.rstrip('\n')
    hundeeierID=hundeeierID.rstrip('\n')
    navn=navn.rstrip('\n')
    kjonn=kjonn.rstrip('\n')
    fodt=fodt.rstrip('\n')

    #legger post inn i liste
    hundeListe+=[hundeID]
    hundeListe+=[oppdretterID]
    hundeListe+=[hundeeierID]
    hundeListe+=[navn]
    hundeListe+=[kjonn]
    hundeListe+=[fodt]

    #leser neste linje slik at løkka går rundt
    hundeID=hundeFil.readline()
#lukker fila så tidlig som mulig
hundeFil.close()
#henter oppdretterID som bruker ønsker å søke på
search=input('Skriv inn OppdretterID for å skrive ut alle hunder registrert på oppdretteren: ')

#For løkke for å gå gjennom alle OppdtretterID. 
for x in range (1,len(hundeListe),6):
    #For alle OppdretterID, sjekker om den matcher med input fra bruker og printer ut tilhørende info dersom det er tilfelle. 
    if hundeListe[x]==search:
        print('Hund funnet:')
        print('ID:',hundeListe[x-1])
        print('Navn:',hundeListe[x+2])
        print('Kjønn:',hundeListe[x+3])
        print('Født:',hundeListe[x+4])
        print()