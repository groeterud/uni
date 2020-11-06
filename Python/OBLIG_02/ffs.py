import os

search=input('Skriv in studentnr du vil slette: ')

studentfil=open('student.txt','r')
tempfil=open('tempfil.txt','w')

studentnr=studentfil.readline()

while studentnr!='':
    studentnr=studentnr.rstrip('\n')
    fornavn=studentfil.readline()
    etternavn=studentfil.readline()
    studie=studentfil.readline()

    if studentnr!=search:
        tempfil.write(studentnr+'\n')
        tempfil.write(fornavn)
        tempfil.write(etternavn)
        tempfil.write(studie)
    
    studentnr==studentfil.readline()

tempfil.close()
studentfil.close()

os.remove('student.txt')
os.rename('tempfil.txt','student.txt')

print('studentdata slettet')

