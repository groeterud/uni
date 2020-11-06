from tkinter import *

def beregn_skatt():
    manedslonn=int(manedslonn_in.get())

    if manedslonn<=20000:
        skatt=0.00
    else:
        if manedslonn<=35000:
            skatt=0.28
        else:
            if manedslonn<=50000:
                skatt=0.35
            else:
                if manedslonn<=70000:
                    skatt=0.42
                else:
                    skatt=0.48

    utbetalt=manedslonn*(1-skatt)
    utbetalt_out.set(utbetalt)

def avslutt():
    window.destroy()

window=Tk()

window.title('Skatteberegning')

#variabler
manedslonn_in=StringVar()
utbetalt_out=StringVar()

#ledetekster 
lbl_manedslonn=Label(window,text='Månedslønn:')
lbl_utbetalt=Label(window,text='Utvetalt')

#knapper
btn_beregn=Button(window,text='Beregn',width=15,command=beregn_skatt)
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