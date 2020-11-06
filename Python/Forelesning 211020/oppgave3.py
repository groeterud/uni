#program for å skrive 3 nye navn til en eksisterende fil 
filnavn=open('student.txt','a')

filnavn.write('Olivia\n')
filnavn.write('Oline\n')
filnavn.write('Petrus\n')

filnavn.close()
