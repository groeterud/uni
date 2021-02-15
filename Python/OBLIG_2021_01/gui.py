from tkinter import *
from tkinter import messagebox

def beregn():
    egenkap=egenkapital.get()
    nedbet=nedbetalingstid.get()
    kjopesum=pris_bil.get()

    messagebox.showerror('Feil','Nedbetalingstid må være positivt tall over 0')

#GUI vinduet
window=Tk()

window.title('Lånekalkulator billån')

# Kjøpesum
pris_bil=StringVar()
## ledetekst
lbl_kjopesum=Label(window,text='Kjøpesum')
lbl_kjopesum.grid(row=0,column=0,padx=5,pady=5,sticky=E)
## input, knytter textvar til pris_bil definert over
ent_kjopesum=Entry(window,width=9,textvariable=pris_bil)
ent_kjopesum.grid(row=0,column=1,padx=5,pady=5, sticky=W)

#egenkapital
egenkapital=StringVar()
## ledetekst
lbl_egenkap=Label(window,text='Egenkapital')
lbl_egenkap.grid(row=1,column=0,padx=5,pady=5,sticky=E)
## entry
ent_egenkap=Entry(window,width=9,textvariable=egenkapital)
ent_egenkap.grid(row=1,column=1,padx=5,pady=5,sticky=W)

#Nedbetalingstid
nedbetalingstid=StringVar()
## ledetekst
lbl_nedbet=Label(window,text='Nedbetalingstid')
lbl_nedbet.grid(row=2,column=0,padx=5,pady=5,sticky=E)
## entry       Velger 5 width for 2 siffer + mellomrom + år
ent_nedbet=Entry(window,width=5,textvariable=nedbetalingstid)
ent_nedbet.grid(row=2,column=1,padx=5,pady=5,sticky=W)

#Rentesats
rentesats=StringVar()
## ledetekst
lbl_rente=Label(window,text='Rentesats')
lbl_rente.grid(row=3,column=0,padx=5,pady=(25,5),sticky=E)
## entry      width 6 = 1 tall+punktum+2 desimaler+space+% 
ent_rente=Entry(window,width=6,state='readonly',textvariable=rentesats)
ent_rente.grid(row=3,column=1,padx=5,pady=(25,5),sticky=W)

#egenkapital i prosent
prosent_egenkap=StringVar()
##ledetekst
lbl_prosent_egenkap=Label(window,text='Prosent egenkapital')
lbl_prosent_egenkap.grid(row=4,column=0,padx=5,pady=5,sticky=W)
## entry
ent_prosent_egenkap=Entry(window,width=7,state='readonly',textvariable=prosent_egenkap)
ent_prosent_egenkap.grid(row=4,column=1,padx=5,pady=5,sticky=W)

#Terminbeløp
terminbelop=StringVar()
## ledetekst
lbl_termin=Label(window,text='Terminbeløp')
lbl_termin.grid(row=5,column=0,padx=5,pady=5,sticky=E)
## entry
ent_termin=Entry(window,width=10,state='readonly',textvariable=terminbelop)
ent_termin.grid(row=5,column=1,padx=5,pady=5,sticky=W)

#knapp avslutt, gir den litt padding oppover. 
btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
btn_avslutt.grid(row=6,column=2,padx=5,pady=(15,5),sticky=E)

#knapp_beregn
btn_beregn=Button(window,text='Beregn',width=20,command=beregn)
btn_beregn.grid(row=6,column=0,columnspan=2,padx=5,pady=(15,5),sticky=E)

#start vindu
window.mainloop()