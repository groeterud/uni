#registrere karakterer for en avholdt eksamen samlet 

import mysql.connector
from tkinter import *
from tkinter import messagebox

eksamensdatabase=mysql.connector.connect(host='localhost',port=3306,user='Eksamenssjef',passwd='oblig2021',db='oblig2021')
markor_eksamen=eksamensdatabase.cursor()

print('Klar for å skrive inn ny eksamensdato ')
ok=True
studentnr=input('Skriv inn studentnr (6 siffer): ')
if len(studentnr)!=6:
    print('error, feil lengde')
    ok=False
emnekode=input('Skriv inn emnekode: ')
if len(emnekode)!=8:
    print('error, feil lengde')
    ok=False
dato=input('Skriv inn dato, format ÅÅÅÅMMDD: ')
if len(dato)!=8:
    print('error, feil lengde')
    ok=False
karakter=input('Oppgi karakter for: ')
if len(karakter)!=1:
    print('error, feil lengde')
    ok=False

if ok:
    query=('INSERT INTO eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES (%s,%s,%s,%s)')
    data=(studentnr,emnekode,dato,karakter)
    markor_eksamen.execute(query,data)
    eksamensdatabase.commit()


