#Program for å skrive 3 navn til ny fil 

#definerer og pner fila student.txt
student_fil=open('student.txt','w')

#skriver 3 navn til fila
#hver tekststreng slutter med \n, "the new line escape sequence", jfr side 89 og 316
student_fil.write('Torvald\n')
student_fil.write('Kari\n')
student_fil.write('Ola\n')






'''
student_fil.close()

student_fil=open('student.txt','r')

student_fil_lengde=len(student_fil.readlines())

print('Antall linjer i fila er:',student_fil_lengde)

student_fil.seek(0)

print('Data i fila  er:',student_fil.readlines())
'''
student_fil.close()