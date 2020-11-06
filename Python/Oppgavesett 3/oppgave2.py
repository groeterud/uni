'''
igjen='ja'
studentliste=[]

while igjen=='ja' or igjen=='Ja' or igjen=='JA':
    print('Registrering av ny student:')
    studentnr=int(input('Skriv inn student nr: '))
    studentliste+=[studentnr]
    fornavn=input('Skriv inn studentens fornavn: ')
    studentliste+=[fornavn]
    studie=input('Skriv studentens studie: ')
    studentliste+=[studie]
    igjen=input('Ønsker du å registere en til student? "skriv ja": ')

print(studentliste)
'''
#bare lagt in manuell liste og kommentert ut det over fordi det blir drit kjedelig å skrive inn dataene hver gang.
studentliste=[240214, 'Andreas', 'bachelor it', 240319, 'Terje', 'bachelor it', 240991, 'Marlene', 'bachelor økad', 240112, 'Trump', 'bachelor jus', 240376, 'Andrea', 'bachelor it']

print('Søk etter studentinformasjon:')
person=int(input('Skriv in studentnr på studenten du ønsker å finne informasjon om: '))
funnet=False

#starter på,med lengden 
for index in range(0,len(studentliste),3):
    if studentliste[index]==person:
        print('Her følger studentinformasjon')
        print('Studentnr:',studentliste[index])
        print('Fornavn:',studentliste[index+1])
        print('Studie:',studentliste[index+2])
        funnet=True

if funnet==False:
    print('Beklager, ingen student med det studentnr')

studium=input('Oppgi studie du ønsker å se relevant studentinformasjon fra: ')
print('Her følger liste over studenter på studie')

funnet=False

for index in range(2,len(studentliste)+1,3):
    if studentliste[index]==studium:
        print('Studentnr:', studentliste[index-2])
        print('Fornavn:',studentliste[index-1])
        print('Studie:',studentliste[index])
        funnet=True     
if funnet==False:
    print('Ingen studenter på det studiet')
print('Program avsluttet')          