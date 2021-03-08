import mysql.connector
from tkinter import *
from tkinter import messagebox
#vi starter med denne regelen, jeg har ALT jeg kan ha inne i en enkelt funksjon. 
#så fort en annen funksjon kan ha bruk for det, flytter vi det utenfor
#enten som en egen funkson eller som globale variabler. 
#Vi skriver ikke duplikat kode, da får den en egen funksjon.

#connection til databasen: 
eksamensdatabase=mysql.connector.connect(host='localhost',port=3306,user='Eksamenssjef',passwd='oblig2021',db='oblig2021')

def ajour():
    #markøren vår
    ajour_markor=eksamensdatabase.cursor()
    #funksjon for å oppdatere listeboksen
    def oppdater_listeboks():
        updt_markor=eksamensdatabase.cursor()
        updt_markor.execute("SELECT * FROM eksamen WHERE Dato>CURRENT_DATE() ORDER BY Dato ASC")
        
        #hiver det inn i en tom liste
        ny_post_list=[]
        for row in updt_markor:
            ny_post_list+=[row]
        
        #sletter alt som er i listeboksen
        lst_eksamener.delete(0,END)

        for x in range(len(ny_post_list)):
            #legger inn alt fra tabellen inn i listeboksen
            lst_eksamener.insert(END,ny_post_list[x])
        updt_markor.close()
           
    #eksisterer fordi vi må sjekke duplukat både på oppdatering og oppretting
    def sjekk_rom_dato_duplikat(dato,romnr):
        duplikat=False
        #henter på nytt i tilfelle databasen har blitt oppdatert siden tidligere. 
        duplikat_markor=eksamensdatabase.cursor()
        duplikat_markor.execute("SELECT * FROM eksamen WHERE Dato>CURRENT_DATE() ORDER BY Dato ASC")
        
        #hiver det inn i en tom liste
        dup_post_list=[]
        for row in duplikat_markor:
            dup_post_list+=[row]

        
        #gjør duplikatsjekken vår
        for x in range(len(dup_post_list)):
            datofix=str(dup_post_list[x][1])
            #i listeformatet finnes datoen med bindestreker, vi fjerner de for å matche forventet input
            datofix=datofix.replace('-','')
            print(dato)
            print(datofix)
            if romnr==dup_post_list[x][2] and dato==datofix:
                duplikat=True
        
        duplikat_markor.close()
        return (duplikat)

    #funksjon for å legge til ny eksamen
    def legg_til_eksamen():
        def lagre_legg_til():
            emnekode=emnekode_legg_til_SV.get()
            dato=dato_legg_til_SV.get()
            rom=rom_legg_til_SV.get()

            duplikat=sjekk_rom_dato_duplikat(dato,rom)

            if duplikat==False:
                #lager markøren vår
                legg_til_markor=eksamensdatabase.cursor()
                query=("INSERT INTO Eksamen VALUES (%s,%s,%s)")
                data=(emnekode,dato,rom)
                legg_til_markor.execute(query,data)
                #commiter og lukker markøren
                eksamensdatabase.commit()
                legg_til_markor.close()
                #vi har lagt inn ny gyldig data, så vi oppdaterer listeboksen vår. 
                oppdater_listeboks()
                #Bekreftelse for bruker
                messagebox.showinfo('Vellykket','Følgende data ble lagret!:'+str(data),parent=ajour_window)
                
            else:
                messagebox.showinfo('Feil','Fant duplisert dato og rom. Vennligst prøv igjen',parent=ajour_window)
            
            
            legg_til_vindu.destroy()


        #her må vi ha nytt vindu, vi bygger GUI
        legg_til_vindu=Toplevel()
        legg_til_vindu.title('Legg til ny eksamen')

        lbl_emnekode_legg_til=Label(legg_til_vindu,text='Emnekode')
        lbl_emnekode_legg_til.grid(row=0,column=0,padx=5,pady=5,sticky=E)

        emnekode_legg_til_SV=StringVar()
        ent_emnekode_legg_til=Entry(legg_til_vindu,width=8,textvariable=emnekode_legg_til_SV)
        ent_emnekode_legg_til.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        lbl_dato_legg_til=Label(legg_til_vindu,text='Dato')
        lbl_dato_legg_til.grid(row=1,column=0,padx=5,pady=5,sticky=E)

        dato_legg_til_SV=StringVar()
        ent_dato_legg_til=Entry(legg_til_vindu,width=8,textvariable=dato_legg_til_SV)
        ent_dato_legg_til.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        lbl_rom_legg_til=Label(legg_til_vindu,text='Rom')
        lbl_rom_legg_til.grid(row=2,column=0,padx=5,pady=5,sticky=E)

        rom_legg_til_SV=StringVar()
        ent_rom_legg_til=Entry(legg_til_vindu,width=4,textvariable=rom_legg_til_SV)
        ent_rom_legg_til.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        btn_lagre_legg_til=Button(legg_til_vindu,text='Lagre',width=6,command=lagre_legg_til)
        btn_lagre_legg_til.grid(row=3,column=0,padx=5,pady=(10,5),sticky=W)

        btn_avslutt_legg_til=Button(legg_til_vindu,text='Avslutt',width=8,command=legg_til_vindu.destroy)
        btn_avslutt_legg_til.grid(row=3,column=1,padx=5,pady=(10,5),sticky=E)

    #funksjon for å oppdatere en eksamen    
    def oppdater_eksamen():
        print('oppdater_eksamen')
    #funksjon for å slette en eksamen
    def slett_eksamen():
        valgt=lst_eksamener.get(lst_eksamener.curselection())
        valgt=str(valgt)
        
        del_markor=eksamensdatabase.cursor()
        #gjør den om til kommaserparert streng
        valgt=valgt.replace('(','').replace(')','').replace(' ','').replace('-','').replace("'","")
        
        ans=messagebox.askyesno(title="Bekreft",message='Er du helt sikker på at du vil slette \n'+valgt,parent=ajour_window)

        valgt=valgt.split(',')
        
        if ans:
            #qry=("DELETE FROM eksamen WHERE (Dato='%s' AND Romnr='%s' AND Emnekode='%s')")
            del_markor.execute("DELETE FROM Eksamen WHERE (Emnekode=%s AND Dato=%s AND Romnr=%s)",(valgt[0],valgt[1],valgt[2],))
            eksamensdatabase.commit()
            oppdater_listeboks()
        del_markor.close()
    
    #henter alle poster med datering etter dagens dato. 
    ajour_markor.execute("SELECT * FROM eksamen WHERE Dato>CURRENT_DATE() ORDER BY Dato ASC")

    #hiver det inn i en tom liste
    post_list=[]
    for row in ajour_markor:
        post_list+=[row]
    
    #GUI for ajourføring
    ajour_window=Toplevel()
    ajour_window.title('Ajourføring av fremtidige eksamener')

    lst_label=Label(ajour_window,text='Emnekode | Dato | Rom')
    lst_label.grid(row=0,column=1,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll=Scrollbar(ajour_window,orient=VERTICAL)
    y_scroll.grid(row=1,column=2,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_eksamensliste=StringVar()
    lst_eksamener=Listbox(ajour_window,width=50,height=8,listvariable=innhold_i_eksamensliste,yscrollcommand=y_scroll.set)
    lst_eksamener.grid(row=1,column=1,rowspan=8,padx=(5,0),pady=5,sticky=E)

    innhold_i_eksamensliste.set(tuple(post_list))

    #knapper
    btn_legg_til=Button(ajour_window,text='Legg til ny eksamen',width=15,command=legg_til_eksamen)
    btn_legg_til.grid(row=1,column=0,padx=5,pady=(5,5),sticky=W)

    btn_oppdater_eksamen=Button(ajour_window,text='Oppdater valgt eksamen',width=18,command=oppdater_eksamen)
    btn_oppdater_eksamen.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    btn_slett_eksamen=Button(ajour_window,text='Slett valgt eksamen',width=15,command=slett_eksamen)
    btn_slett_eksamen.grid(row=3,column=0,padx=5,pady=5,sticky=W)

    #avslutt
    btn_avslutt_ajour=Button(ajour_window,text='Lukk vindu',width=10,command=ajour_window.destroy)
    btn_avslutt_ajour.grid(row=9,column=1,padx=5,pady=5,sticky=E)

    ajour_markor.close()


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