#Program for å lese navn for navn og skrive ut de navnene som passer med søkekriterie
#Generell framgangsmåte jfr fig 6-17 og program 6-9 

#Åpner fila student.txt
studentfil=open('student.txt','r')

#leser første linje i fila ved bruk av readline-metoden
student=studentfil.readline()

#I Python, readline returnerer en tom streng ('') når en har forsøkt å lese
#forbi "end of file"/eof, da tester vi på det. 
studenter_paa_o=[]

while student != '': 
    if student[0]=='O':
        student = student.rstrip('\n')
        studenter_paa_o+=[student]
    student=studentfil.readline()

print('Navn på studenter med navn på O:')
for i in range(0, len(studenter_paa_o),1):
    print(studenter_paa_o[i])

#stenger fila
studentfil.close()