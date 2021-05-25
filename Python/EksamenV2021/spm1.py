# Lag et program som leser all informasjon om kundene inn i en to-dimensjonal liste og, som skirver ut mobilnr,
#  fornavn og etternavn ved en gjennomgang av lista. 

f=open('Kunde.txt','r',encoding='utf-8')

mobilnr=f.readline()
kunder=[]
while mobilnr!='':
    mobilnr=mobilnr.rstrip('\n')
    fornavn=f.readline().strip('\n')
    etternavn=f.readline().rstrip('\n')
    epost=f.readline().rstrip('\n')

    kunder+=[[mobilnr,fornavn,etternavn,epost]]

    mobilnr=f.readline()

f.close()

for x in range(len(kunder)):
    print()
    print('Mobilnr:\t',kunder[x][0])
    print('Fornavn:\t',kunder[x][1])
    print('Etternavn:\t',kunder[x][2])