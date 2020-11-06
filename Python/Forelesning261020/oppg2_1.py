#grunnstruktur
#lager med komponentene ledetekst, inndatafelt, utdatafelt

from tkinter import *


def beregn_lan():
    if int(egenkap.get())/int(kjopesum.get())>=0.35:
        tilsagn.set('Lån kan innvilges')
    else:
        tilsagn.set('Lån kan ikke innvilges')

def avslutt():
    window.destroy()

#lag nytt vindu
window=Tk()

#gir vinduet et navn
window.title('Lånekalkulator billån')

#deklarering av variabler
kjopesum=StringVar()
egenkap=StringVar()
tilsagn=StringVar()

#deklarering
#ledetekster/labels
lbl_kjopesum=Label(window,text='Kjøpesum:')

lbl_egenkap=Label(window,text='Egenkapital:')

lbl_tilsagn=Label(window,text='Tilsagn på lån:')

#knapper
btn_beregn=Button(window,text='Beregn',width=15,command=beregn_lan)

btn_avslutt=Button(window, text='Avslutt', width=15,command=avslutt)

#entrys
ent_kjopesum=Entry(window,width=9,textvariable=kjopesum)

ent_egenkap=Entry(window,width=9,textvariable=egenkap)

tilsagn_output=Entry(window,width=20,state='readonly',textvariable=tilsagn)


#tilordning
#ledetekst/labels
lbl_kjopesum.grid(row=0,column=0, padx=100, pady=15, sticky=E)
lbl_egenkap.grid(row=1,column=0, padx=100, pady=15, sticky=E)
lbl_tilsagn.grid(row=3,column=0, padx=100, pady=15, sticky=E)

#knapper
btn_beregn.grid(row=2,column=1,pady=25)
btn_avslutt.grid(row=4,column=1,pady=15,sticky=S)

#entrys
ent_kjopesum.grid(row=0,column=2,padx=50,pady=15, sticky=E)
ent_egenkap.grid(row=1,column=2,padx=50,pady=15, sticky=E)
tilsagn_output.grid(row=3,column=2,padx=50,pady=15,sticky=E)

#kjør metoden, mainloop som starter vindu
window.mainloop()
