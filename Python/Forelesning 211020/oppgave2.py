#program for å lese en hel fil på en gang

#åpner fila student.txt

studentfil=open('student.txt','r')

filinnhold=studentfil.read()

studentfil.close()

print(filinnhold)
