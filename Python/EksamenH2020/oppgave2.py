from tkinter import *

def kalkuler():
    #Forsendelsens vekt som inndata fra bruker
    vekt=int(vekt_in.get())
    #Tilordning av porto
    if vekt<=20:
        porto=17
    else:
        if vekt<=50:
            porto=24
        else:
            if vekt<=100:
                porto=27
            else:
                if vekt<=350:
                    porto=45
                else:
                    if vekt<=1000:
                        porto=88
                    else:
                        porto=125
    #tilordner resultatet
    porto_out.set(porto)

#funksjon for å avslutte GUI 
def avslutt():
    window.destroy()

window=Tk()

window.title('Portokalkulator')

#variabler
vekt_in=StringVar()
porto_out=StringVar()

#ledetekster 
lbl_vekt=Label(window,text='Forsendelsens vekt (i gram):')
lbl_porto=Label(window,text='Porto:')

#knapper med tilhørende funksjonskall 
btn_beregn=Button(window,text='Beregn porto',width=10,command=kalkuler)
btn_avslutt=Button(window,text='Avslutt',width=5,command=avslutt)

#entrys
ent_manedslonn=Entry(window,width=10,textvariable=vekt_in)
output_utbetalt=Entry(window,width=5,state='readonly',textvariable=porto_out)

#plassering
#ledetekster
lbl_vekt.grid(row=0,column=0,pady=15,sticky=E)
lbl_porto.grid(row=1,column=0,pady=15,sticky=E)

#knapper
btn_beregn.grid(row=0,column=2,padx=15)
btn_avslutt.grid(row=2,column=2,sticky=E,padx=15,pady=15)

#entrys
ent_manedslonn.grid(row=0,column=1,pady=15,sticky=W)
output_utbetalt.grid(row=1,column=1,pady=15,sticky=W)

#kjør GUI 
window.mainloop()