import mysql.connector
from tkinter import *
from tkinter import messagebox

def ajour():
    print('ajour')
def registrer_eksamensresultat():
    print('registrer_eksamensresultat')
def vis_emneresultater():
    print('vis_emneresultater')
def vis_eksamensresultater():
    print('vis_eksamensresultater')
def eksamensresultater_student():
    print('eksamensresultater_student')
def vitnemal():
    print('vitnemal')
def planlagte_eksamener_dag():
    print('planlagte_eksamener_dag')
def planlagte_eksamener_periode():
    print('planlagte_eksamener_periode')

#GUI
window=Tk()
window.title('Eksamenshåndtering')

#frame for eksamensmanipulasjon
eksamensmanipulasjon_frame=LabelFrame(window,text='Eksamensmanipulasjon')
eksamensmanipulasjon_frame.grid(row=0,column=0,padx=5,pady=10,sticky=N)

#knapper i framen
btn_registrer_eksamensresultat=Button(eksamensmanipulasjon_frame,text='Legg til eksamensresultat',width=20,command=registrer_eksamensresultat)
btn_registrer_eksamensresultat.grid(row=0,column=0,padx=5,pady=(10,5),sticky=W)

btn_ajour=Button(eksamensmanipulasjon_frame,text='Legg til, slett eller endre eksamen',width=26,command=ajour)
btn_ajour.grid(row=1,column=0,padx=5,pady=5,sticky=W)

#frem for enkeltstudent, ble rotete med for mange visninger
enkeltstudent_frame=LabelFrame(window,text='Visninger for en enkelt student')
enkeltstudent_frame.grid(row=0,column=1,padx=5,pady=10,sticky=N)

btn_vitnemal=Button(enkeltstudent_frame,text='Vis vitnemål for en student',width=22,command=vitnemal)
btn_vitnemal.grid(row=0,column=0,padx=5,pady=(10,5),sticky=W)

btn_vis_eksamensresultater_student=Button(enkeltstudent_frame,text='Vis alle eksamensresultater for enkeltstudent',width=34,command=eksamensresultater_student)
btn_vis_eksamensresultater_student.grid(row=1,column=0,padx=5,pady=5,sticky=W)

#frame for visninger
visninger_frame=LabelFrame(window,text='Øvrige Visninger')
visninger_frame.grid(row=1,column=0,columnspan=2,padx=5,pady=10,sticky=N)

#knapper i framet
btn_vis_eksamensresultater=Button(visninger_frame,text='Vis alle eksamensresultater fra en eksamen',width=33,command=vis_eksamensresultater)
btn_vis_eksamensresultater.grid(row=0,column=0,padx=5,pady=(10,5),sticky=W)

btn_vis_emneresultater=Button(visninger_frame,text='Vis eksamensresultater i et emne',width=26,command=vis_emneresultater)
btn_vis_emneresultater.grid(row=0,column=1,padx=5,pady=(10,5),sticky=W)

btn_planlagte_eksamener_periode=Button(visninger_frame,text='Vis alle eksamener i en bestemt periode',width=31,command=planlagte_eksamener_periode)
btn_planlagte_eksamener_periode.grid(row=1,column=0,padx=5,pady=5,sticky=W)

btn_planlagte_eksamener_dag=Button(visninger_frame,text='Vis alle eksamener på en bestemt dag',width=30,command=planlagte_eksamener_dag)
btn_planlagte_eksamener_dag.grid(row=1,column=1,padx=5,pady=5,sticky=W)

#Terminer program
btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
btn_avslutt.grid(row=2,column=1,padx=5,pady=5,sticky=E)

window.mainloop()