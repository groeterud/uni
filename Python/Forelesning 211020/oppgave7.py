#while variabel
igjen='ja'

#tom liste som vi kan dytte data inn i 
navneliste=[]

#spør om input og legger det inn i lista
while igjen=='ja' or igjen=='Ja' or igjen=='JA':
    fornavn=input('Skriv in fornavn: ')
    navneliste+=[fornavn]
    igjen=input('Ønsker du å skrive inn et til navn? Om så, skriv "ja": ')

#bare print som verifikasjon
print('Listen med navn du skrev in:',navneliste)

#ny tom liste, hvor jeg har tenkt til å legge reversert data inn
navneliste_reverse=[]

#range starter på lengden av navnelist -1 fordi index starter på 0. 
#range har step på -1 fordi vi skal ned en plass hver gang ettersom vi starter på slutten 
#range slutter på -1 ettersom vi skal ha med navneliste[0] så vi må gå en lenger. 
#legg til alle verdiene fra slutten til starten av navneliste inn i navneliste_reverse. 
for index in range(len(navneliste)-1,-1,-1):
    navneliste_reverse+=[navneliste[index]]


#print lista
print('Dette er listen reversert',navneliste_reverse)

#bare for å irritere oss, vis den innebygde metoden for å gjøre dette i Python. 
navneliste.reverse()

print('Verifikasjon:',navneliste)



