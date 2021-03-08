from tkinter import *
from tkinter import messagebox


def saniter_input(egenkap,nedbet,kjopesum):
    #denne funksjonen har en rekke logiske tester for å verifisere programlogikken og gir brukeren error-meldinger dersom noe ikke er tilfredsstillende.
    laanekalulasjon=False
    #basisverdi på 0 for if test lenger ned
    egenkapital_pct=0
    if nedbet<0:
        messagebox.showerror('Feil','Nedbetalingstid må være positivt tall over 0')
    else:
        if kjopesum<=0:
            messagebox.showerror('Feil','Pris på bil kan ikke være negativ')
        else:
            if egenkap<0:
                messagebox.showerror('Feil','Egenkapital kan ikke være negativ')
            else:
                if egenkap>kjopesum:
                    messagebox.showerror('Feil','Du har nok egenkapital til at du ikke behøver noe lån, dermed kan vi ikke tilby deg et.')
                else:
                    egenkapital_pct=egenkap/kjopesum*100
                    if egenkapital_pct<35:
                        messagebox.showerror('Feil',("Beklager, det foreligger krav om 35.00 prosent egenkapital og du har bare "+format(egenkapital_pct,".2f")+" prosent egenkapital. Lånet kan dermed ikke innvilges"))
                    else:
                        laanekalulasjon=True #bare kjøre lånekalkulasjon om input er ok
    return(laanekalulasjon,egenkapital_pct)

def beregn_aarlig_rente(egenkapital_pct):
    if egenkapital_pct<50:
        aarlig_rente=0.045
    else:
        if egenkapital_pct<60:
            aarlig_rente=0.03
        else:
            aarlig_rente=0.025
    return (aarlig_rente)

#oppderer verdien på entryen endbetalingstid med inndata
def update_nedbet(event):
    nedbetalingstid.set(event)
    egenkap,nedbet,kjopesum,validert=datavalidering()
    if validert==True:
        beregn()

#oppdaterer verdien på nedbetalings-scalaen med inndata, dersom det er numerisk. 
def update_nedbet_scale(event):
    if (event.char.isnumeric())==True:
        nedbet=nedbetalingstid.get()
        #stripper år
        nedbet=int(nedbet.rstrip(' år'))
        nedbet_scale.set(nedbet)
    egenkap,nedbet,kjopesum,validert=datavalidering()
    if validert==True:
        beregn()

#påser at vi fjerner evt 'kr' eller '%' på slutten av felte.
def datavalidering():
    validert=False
    #henter inputs fra GUI
    egenkap=egenkapital.get()
    nedbet=nedbetalingstid.get()
    kjopesum=pris_bil.get()
    
    #sjekker om de er tomme før vi prøver å gjøre noe med de
    if (egenkap!='') and (nedbet!='') and (kjopesum!=''):
        validert=True
        egenkap=int(egenkap.rstrip(' kr'))
        nedbet=int(nedbet.rstrip(' år'))
        kjopesum=int(kjopesum.rstrip(' kr'))
    
    return (egenkap,nedbet,kjopesum,validert)

def beregn(): 
    #validerer fjerner eventuelle etterslep av strengverdier
    egenkap,nedbet,kjopesum,validert=datavalidering()

    if validert==False:
        messagebox.showerror('Feil','Vennligst påse at du har verdier i alle textboksene')
    else:
        #sjekker om inputs er innenfor akseptable rammer.
        laanekalulasjon,egenkapital_pct=saniter_input(egenkap,nedbet,kjopesum)
        
        #Hvis den er det så beregner vi årlig rente
        if laanekalulasjon==True:
            aarlig_rente=beregn_aarlig_rente(egenkapital_pct)

            #Beregne variabler som er avhengige av if løkkens utfall
            terminrente=aarlig_rente/12
            antall_terminer=nedbet*12
            laanebelop=kjopesum-egenkap

            #Beregne terminbeløp
            terminbelopet = laanebelop*((((1+terminrente)**antall_terminer)*terminrente)/(((1+terminrente)**antall_terminer)-1))

            #outputs til GUI
            ## Setter terminbeløpet
            terminbelopet=format(terminbelopet,".2f")
            terminbelop.set(terminbelopet+' kr')
            aarlig_rente=aarlig_rente*100
            aarlig_rente=str(aarlig_rente)
            rentesats.set(aarlig_rente+' %')
            egenkapital_pct=format(egenkapital_pct,".2f")
            egenkapital_pct=str(egenkapital_pct)
            prosent_egenkap.set(egenkapital_pct+' %')

            #formatering av inputs for å gjøre det litt penere
            egenkap=str(egenkap)
            egenkapital.set(egenkap+' kr')
            nedbet=str(nedbet)
            nedbetalingstid.set(nedbet+' år')
            kjopesum=str(kjopesum)
            pris_bil.set(kjopesum+' kr')

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
lbl_nedbet.grid(row=2,column=0,padx=5,pady=(5,0),sticky=E)
## entry       Velger 5 width for 2 siffer + mellomrom + år
ent_nedbet=Entry(window,width=5,textvariable=nedbetalingstid)
ent_nedbet.grid(row=2,column=1,padx=5,pady=(5,0),sticky=W)
#oppdater scalen når verdi blir tastet
ent_nedbet.bind("<KeyRelease>", update_nedbet_scale)
#scale, opppdaterer Entry med verdi fra scalen når den flyttes
nedbet_scale=Scale(window, from_=1, to=15, orient=HORIZONTAL, length=250,showvalue=0,command=update_nedbet)
nedbet_scale.grid(row=3, column=0,columnspan=3, padx=5)


#Rentesats
rentesats=StringVar()
## ledetekst
lbl_rente=Label(window,text='Rentesats')
lbl_rente.grid(row=4,column=0,padx=5,pady=(25,5),sticky=E)
## entry      width 6 = 1 tall+punktum+2 desimaler+space+% 
ent_rente=Entry(window,width=6,state='readonly',textvariable=rentesats)
ent_rente.grid(row=4,column=1,padx=5,pady=(25,5),sticky=W)

#egenkapital i prosent
prosent_egenkap=StringVar()
##ledetekst
lbl_prosent_egenkap=Label(window,text='Prosent egenkapital')
lbl_prosent_egenkap.grid(row=5,column=0,padx=5,pady=5,sticky=W)
## entry
ent_prosent_egenkap=Entry(window,width=7,state='readonly',textvariable=prosent_egenkap)
ent_prosent_egenkap.grid(row=5,column=1,padx=5,pady=5,sticky=W)

#Terminbeløp
terminbelop=StringVar()
## ledetekst
lbl_termin=Label(window,text='Terminbeløp')
lbl_termin.grid(row=6,column=0,padx=5,pady=5,sticky=E)
## entry
ent_termin=Entry(window,width=10,state='readonly',textvariable=terminbelop)
ent_termin.grid(row=6,column=1,padx=5,pady=5,sticky=W)

#knapp avslutt, gir den litt padding oppover. 
btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
btn_avslutt.grid(row=7,column=2,padx=5,pady=(15,5),sticky=E)

#knapp_beregn
btn_beregn=Button(window,text='Beregn',width=20,command=beregn)
btn_beregn.grid(row=7,column=0,columnspan=2,padx=5,pady=(15,5),sticky=E)

#start vindu
window.mainloop()