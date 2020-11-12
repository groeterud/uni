from tkinter import *

def beregn_skatt():
    manedslonn=int(manedslonn_in.get())

    if manedslonn>=964801:
        skatt=0.464
    else:
        if manedslonn>=617501:
            skatt=0.434
        else:
            if manedslonn>=245651:
                skatt=0.344
            else:
                if manedslonn>=174501:
                    skatt=0.22
                else:
                    if manedslonn>=102819:
                        skatt=0.203
    if manedslonn >=102819:
        utbetalt=manedslonn*(1-skatt)
        skatt=skatt*100
        skatt=str(skatt)
        utbetalt_out.set(skatt+'%')
    else:
        utbetalt_out.set('N/A')

def avslutt():
    window.destroy()

window=Tk()

window.title('Skatteberegning')

#variabler
manedslonn_in=StringVar()
utbetalt_out=StringVar()

#ledetekster 
lbl_manedslonn=Label(window,text='Lønnsinntekt:')
lbl_utbetalt=Label(window,text='Marginalskatt')

#knapper
btn_beregn=Button(window,text='Beregn marginalskatteprosent',width=25,command=beregn_skatt)
btn_avslutt=Button(window,text='Avslutt',width=5,command=avslutt)

#entrys
ent_manedslonn=Entry(window,width=10,textvariable=manedslonn_in)
output_utbetalt=Entry(window,width=10,state='readonly',textvariable=utbetalt_out)

#plassering
#ledetekster
lbl_manedslonn.grid(row=0,column=0,pady=15,sticky=E)
lbl_utbetalt.grid(row=1,column=0,pady=15,sticky=E)

#knapper
btn_beregn.grid(row=0,column=2,padx=10)
btn_avslutt.grid(row=2,column=2,sticky=E,padx=10,pady=10)

#entrys
ent_manedslonn.grid(row=0,column=1,padx=15,pady=15,sticky=E)
output_utbetalt.grid(row=1,column=1,padx=15,pady=15,sticky=E)


window.mainloop()