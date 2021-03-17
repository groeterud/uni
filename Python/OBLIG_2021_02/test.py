from os import stat
import mysql.connector
from tkinter import *
from tkinter import messagebox

eksamensdatabase=mysql.connector.connect(host='localhost',port=3306,user='Eksamenssjef',passwd='oblig2021',db='oblig2021')
markor_eksamen=eksamensdatabase.cursor()

def lagre_karakterer():
    #strukturerer datasetningene våre
    karakterer=[]
    data=[]
    for x in range(len(karakter_sv_liste)):
        tempvar=karakter_sv_liste[x].get()
        #if test for å se om man ikke har tastet inn noen verdi i et felt. Sørger for at vi beholder NULL på det punktet. 
        if tempvar=='':
            tempvar=None
        karakterer+=[tempvar]
        data+=[(tempvar,post_list_eks_updt[x][2],post_list_eks_updt[x][3],post_list_eks_updt[x][4])]

    #ny markør
    lagrings_markor=eksamensdatabase.cursor()
    query=("UPDATE Eksamensresultat SET Karakter=%s WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s")

    lagrings_markor.executemany(query,data)
    eksamensdatabase.commit()
    lagrings_markor.close()

    messagebox.showinfo('Vellykket','Karakterene ble lagret!')
    
    





markor_eksamen.execute('''
    SELECT Fornavn,Etternavn,Eksamensresultat.*
    FROM Eksamensresultat JOIN 
        Student USING (Studentnr)
    WHERE Karakter IS NULL AND Emnekode='DATB1000' AND Dato='20200521'
''')

post_list_eks_updt=[]

for row in markor_eksamen:
    post_list_eks_updt+=[row]

#enkel gui ramme
window=Tk()
window.title('Masseregistrering av eksamensresultat')

registrering=LabelFrame(window,text='Skriv inn karakterer på registrerte studenter')
registrering.grid(row=0,column=0,padx=5,pady=5)

navn_header=Label(registrering,text='Navn')
navn_header.grid(row=0,column=0,padx=5,pady=5,sticky=W)

studnr_header=Label(registrering,text='Studentnr')
studnr_header.grid(row=0,column=1,padx=5,pady=5)

kar_header=Label(registrering,text='Karakter')
kar_header.grid(row=0,column=2,padx=5,pady=5)

karakter_sv_liste=[]

for x in range(len(post_list_eks_updt)):
    
    lbl_navn=Label(registrering,text=post_list_eks_updt[x][0]+' '+post_list_eks_updt[x][1])
    lbl_navn.grid(row=x+1,column=0,padx=5,pady=5,sticky=W)
    

    lbl_studentID=Label(registrering,text=post_list_eks_updt[x][2])
    lbl_studentID.grid(row=x+1,column=1,padx=5,pady=5)

    sv_Karakter=StringVar()
    ent_Karakter=Entry(registrering,textvariable=sv_Karakter,width=2)
    ent_Karakter.grid(row=x+1,column=2,padx=5,pady=5)

    karakter_sv_liste+=[sv_Karakter]


btn_lagre=Button(window,text='Lagre',width=10,command=lagre_karakterer)
btn_lagre.grid(row=1,column=0,padx=5,pady=5,sticky=W)

window.mainloop()