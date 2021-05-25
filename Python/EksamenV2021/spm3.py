from tkinter import *
from tkinter import messagebox
import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,user='Dekksjef',passwd='eksamen2021',db='Dekkhotell')

def lagre():
    #henter inputs
    mobilnr=mobilnr_sv.get()
    fornavn=fornavn_sv.get()
    etternavn=etternavn_sv.get()
    epost=epost_sv.get()
    regnr=regnr_sv.get()
    hylle=hylle_sv.get()
    
    #sjekk at kunden ikke eksisterer fra før
    kunde_markor=db.cursor()
    kunde_markor.execute('''
    SELECT Mobilnr
    FROM Kunde
    ''')
    duplikat=False
    for row in kunde_markor:
        if mobilnr==row[0]:
            duplikat=True
    kunde_markor.close()
    
    if duplikat==True:
        messagebox.showerror('FEIL','Kunden er allerede registrert')
    else:
        #registrer ny kunde
        insert_kunde=db.cursor()
        insert_kunde.execute('''
        INSERT INTO Kunde VALUES
        (%s,%s,%s,%s)
        ''',(mobilnr,fornavn,etternavn,epost))
        db.commit()
        insert_kunde.close()

        #registrer dekksett på kunde
        insert_dekksett=db.cursor()
        insert_dekksett.execute('''
        INSERT INTO Dekksett VALUES
        (%s,%s)
        ''',(mobilnr,regnr))
        db.commit()
        insert_dekksett.close()

        #registrer Oppbevaring
        oppb_markor=db.cursor()
        oppb_markor.execute('''
        INSERT INTO Oppbevaring VALUES
        (%s,%s,CURRENT_DATE,NULL,%s,NULL)
        ''',(mobilnr,regnr,hylle))
        db.commit()
        oppb_markor.close()

        messagebox.showinfo('Vellykket','Kunden, Dekksett og Oppbevaring ble lagret')


## UI 
window=Tk()
window.title('Kunderegistrering')

mobilnr_lbl=Label(window,text='Mobilnr:')
mobilnr_lbl.grid(row=0,column=0,padx=5,pady=5,sticky=W)

mobilnr_sv=StringVar()
mobilnr_ent=Entry(window,width=12,textvariable=mobilnr_sv)
mobilnr_ent.grid(row=0,column=1,padx=5,pady=5,sticky=W)

fornavn_lbl=Label(window,text='Fornavn:')
fornavn_lbl.grid(row=1,column=0,padx=5,pady=5,sticky=W)

fornavn_sv=StringVar()
fornavn_ent=Entry(window,width=30,textvariable=fornavn_sv)
fornavn_ent.grid(row=1,column=1,padx=5,pady=5,sticky=W)

etternavn_lbl=Label(window,text='Etternavn:')
etternavn_lbl.grid(row=2,column=0,padx=5,pady=5,sticky=W)

etternavn_sv=StringVar()
etternavn_ent=Entry(window,width=30,textvariable=etternavn_sv)
etternavn_ent.grid(row=2,column=1,padx=5,pady=5,sticky=W)

epost_lbl=Label(window,text='Epost:')
epost_lbl.grid(row=3,column=0,padx=5,pady=5,sticky=W)

epost_sv=StringVar()
epost_ent=Entry(window,width=30,textvariable=epost_sv)
epost_ent.grid(row=3,column=1,padx=5,pady=5,sticky=W)

regnr_lbl=Label(window,text='Regnr:')
regnr_lbl.grid(row=4,column=0,padx=5,pady=5,sticky=W)

regnr_sv=StringVar()
regnr_ent=Entry(window,width=7,textvariable=regnr_sv)
regnr_ent.grid(row=4,column=1,padx=5,pady=5,sticky=W)

hylle_lbl=Label(window,text='Hylle:')
hylle_lbl.grid(row=5,column=0,padx=5,pady=5,sticky=W)

hylle_sv=StringVar()
hylle_ent=Entry(window,width=5,textvariable=hylle_sv)
hylle_ent.grid(row=5,column=1,padx=5,pady=5,sticky=W)

btn_lagre=Button(window,text='Lagre',width=7,command=lagre)
btn_lagre.grid(row=6,column=0,padx=5,pady=5,sticky=SW)

btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
btn_avslutt.grid(row=6,column=1,padx=5,pady=(20,5),sticky=SE)

window.mainloop()