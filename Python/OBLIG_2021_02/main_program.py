import mysql.connector
from tkinter import *
from tkinter import messagebox

#connection til databasen: 
eksamensdatabase=mysql.connector.connect(host='localhost',port=3306,user='Eksamenssjef',passwd='oblig2021',db='oblig2021')

#funksjon for å gjøre en listeboksseleksjon om til en liste. Bruker den i flere funksjoner
def curselection_to_list(list_name):
    try:
        valgt=str(list_name.get(list_name.curselection()))
        #gjør den om til kommaserparert streng
        valgt=valgt.replace('(','').replace(')','').replace(' ','').replace('-','').replace("'","")
        #gjør kommeseparert streng om til liste
        curselection_list=valgt.split(',')
        return(curselection_list)
    #thrower av og til errorer når ingenting er selektert. Har ingenting å si for funksjonaliteten. 
    except TclError:
        ingenting_er_selektert=True  

#ajourføring av fremtidige eksamener
def ajour():     
    #trigger for å oppdatere seleksjonen. Dette er fordi vi må ha tilgang til valgt_liste i andre TopLevels, 
    # så de må arve denne variabelen når de ikke kan kalle funksjonen.
    def oppdater_seleksjon(event):
            global valgt_liste_ajour #Gaddis s258 
            valgt_liste_ajour=curselection_to_list(lst_eksamener)
    
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
        ent_emnekode_legg_til=Entry(legg_til_vindu,width=10,textvariable=emnekode_legg_til_SV)
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
               
        def populere_enter():
            ##henter ut seleksjonen fra listeboksen og hiver de rent i en liste. 
            #valgt_liste=curselection_to_list(lst_eksamener)
            #setter entene
            emnekode_updt_SV.set(valgt_liste_ajour[0])
            dato_updt_SV.set(valgt_liste_ajour[1])
            rom_updt_SV.set(valgt_liste_ajour[2])
        
        #funksjon for å skrive til databasen
        def oppdater():
            #oppdaterer variabler med nye verdier fra entene
            emnekode=emnekode_updt_SV.get()
            dato=dato_updt_SV.get()
            rom=rom_updt_SV.get()

            duplikat=sjekk_rom_dato_duplikat(dato,rom)

            if duplikat==False:

                #lager markøren vår
                updt_markor=eksamensdatabase.cursor()
                query=("UPDATE Eksamen SET Emnekode=%s,Dato=%s,Romnr=%s WHERE Emnekode=%s AND Dato=%s AND Romnr=%s")
                data=(emnekode,dato,rom,valgt_liste_ajour[0],valgt_liste_ajour[1],valgt_liste_ajour[2])
            
                updt_markor.execute(query,data)
                #commiter og lukker markøren
                eksamensdatabase.commit()
                updt_markor.close()
                #vi har lagt inn ny gyldig data, så vi oppdaterer listeboksen vår. 
                oppdater_listeboks()
                #Bekreftelse for bruker
                messagebox.showinfo('Vellykket','Følgende endringer ble lagret:\n'+emnekode+' '+dato+' '+rom,parent=updt_vindu)
            else:
                messagebox.showinfo('Feil','Fant duplisert dato og rom. Vennligst prøv igjen',parent=updt_vindu)
                

        #gui - låner struktur fra legg til, iom at det er samme vindu, bare med litt annen tekst.
        updt_vindu=Toplevel()
        updt_vindu.title('Oppdater eksamen')

        lbl_emnekode_updt=Label(updt_vindu,text='Emnekode')
        lbl_emnekode_updt.grid(row=0,column=0,padx=5,pady=5,sticky=E)

        emnekode_updt_SV=StringVar()
        ent_emnekode_updt=Entry(updt_vindu,width=10,textvariable=emnekode_updt_SV)
        ent_emnekode_updt.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        lbl_dato_updt=Label(updt_vindu,text='Dato')
        lbl_dato_updt.grid(row=1,column=0,padx=5,pady=5,sticky=E)

        dato_updt_SV=StringVar()
        ent_dato_updt=Entry(updt_vindu,width=8,textvariable=dato_updt_SV)
        ent_dato_updt.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        lbl_rom_updt=Label(updt_vindu,text='Rom')
        lbl_rom_updt.grid(row=2,column=0,padx=5,pady=5,sticky=E)

        rom_updt_SV=StringVar()
        ent_rom_updt=Entry(updt_vindu,width=4,textvariable=rom_updt_SV)
        ent_rom_updt.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        btn_updt=Button(updt_vindu,text='Oppdater',width=8,command=oppdater)
        btn_updt.grid(row=3,column=0,padx=5,pady=(10,5),sticky=W)

        btn_avslutt_updt=Button(updt_vindu,text='Avslutt',width=8,command=updt_vindu.destroy)
        btn_avslutt_updt.grid(row=3,column=1,padx=5,pady=(10,5),sticky=E)

        #kjører en funksjon for å oppdatere ent'ene med eksisterende info. 
        populere_enter()


    #funksjon for å slette en eksamen
    def slett_eksamen():
        valgt=str(lst_eksamener.get(lst_eksamener.curselection()))
        
        ans=messagebox.askyesno(title="Bekreft",message='Er du helt sikker på at du vil slette \n'+valgt,parent=ajour_window)
        del_markor=eksamensdatabase.cursor()
        #kaller på funksjonen for å få tilbake seleksjonen over som en liste. 
        #valgt_liste=curselection_to_list(lst_eksamener)

        if ans:
            #qry=("DELETE FROM eksamen WHERE (Dato='%s' AND Romnr='%s' AND Emnekode='%s')")
            del_markor.execute("DELETE FROM Eksamen WHERE (Emnekode=%s AND Dato=%s AND Romnr=%s)",(valgt_liste_ajour[0],valgt_liste_ajour[1],valgt_liste_ajour[2],))
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
    y_scroll_eksamener=Scrollbar(ajour_window,orient=VERTICAL)
    y_scroll_eksamener.grid(row=1,column=2,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_eksamensliste=StringVar()
    lst_eksamener=Listbox(ajour_window,width=50,height=8,listvariable=innhold_i_eksamensliste,yscrollcommand=y_scroll_eksamener.set)
    lst_eksamener.grid(row=1,column=1,rowspan=8,padx=(5,0),pady=5,sticky=E)
    lst_eksamener.bind('<<ListboxSelect>>',oppdater_seleksjon)
    innhold_i_eksamensliste.set(tuple(post_list))

    y_scroll_eksamener['command']=lst_eksamener.yview

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

#registrerer flere eksamensresultat for en avholdt eksamen.  
def registrer_eksamensresultat():
    reg_markor=eksamensdatabase.cursor()

    def oppdater_seleksjon_reg(event):
        global valgt_liste_reg #Gaddis s258 
        valgt_liste_reg=curselection_to_list(lst_eksamener_reg)

    def legg_til_eksamensresultat():
        def lagre_legg_til_reg():
            #henter inn verdier som skal lagres
            studentnr_reg=studentnr_reg_SV.get()
            karakter_reg=karakter_reg_SV.get()

            #lager oss en lagringsmarkør. 
            markor_lagre_reg=eksamensdatabase.cursor()
            #Eksamensresultat(_Studentnr*_,_Emnekode*_,_Dato*_,Karakter)
            qry=("INSERT INTO Eksamensresultat VALUES (%s,%s,%s,%s)")
            data=(studentnr_reg,emnekode_reg,dato_reg,karakter_reg)
            #exuter inserten
            markor_lagre_reg.execute(qry,data)
            #commiter endringen og lukker markøren
            eksamensdatabase.commit()
            markor_lagre_reg.close()


            messagebox.showinfo('Vellykket','Følgende data ble lagret!:\n'+str(data),parent=legg_til_vindu_reg)
        #fanger emnekode og dato for seleksjonen.     
        emnekode_reg=valgt_liste_reg[0]
        dato_reg=valgt_liste_reg[1]
        #her må vi ha nytt vindu, vi bygger GUI
        legg_til_vindu_reg=Toplevel()
        legg_til_vindu_reg.title('Legg til eksamensresultater for valgt emnme')

        lbl_studentnr_reg=Label(legg_til_vindu_reg,text='Studentnr')
        lbl_studentnr_reg.grid(row=0,column=0,padx=5,pady=5,sticky=E)

        studentnr_reg_SV=StringVar()
        ent_studentnr_reg=Entry(legg_til_vindu_reg,width=7,textvariable=studentnr_reg_SV)
        ent_studentnr_reg.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        lbl_karakter_reg=Label(legg_til_vindu_reg,text='Karakter')
        lbl_karakter_reg.grid(row=1,column=0,padx=5,pady=5,sticky=E)

        karakter_reg_SV=StringVar()
        ent_karakter_reg=Entry(legg_til_vindu_reg,width=2,textvariable=karakter_reg_SV)
        ent_karakter_reg.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #knapper
        btn_lagre_legg_til_reg=Button(legg_til_vindu_reg,text='Lagre',width=6,command=lagre_legg_til_reg)
        btn_lagre_legg_til_reg.grid(row=3,column=0,padx=5,pady=(10,5),sticky=W)

        btn_avslutt_legg_til_reg=Button(legg_til_vindu_reg,text='Avslutt',width=8,command=legg_til_vindu_reg.destroy)
        btn_avslutt_legg_til_reg.grid(row=3,column=1,padx=5,pady=(10,5),sticky=E)

    #henter alle poster med datering etter dagens dato. 
    reg_markor.execute("SELECT * FROM eksamen WHERE Dato<=CURRENT_DATE() ORDER BY Dato DESC")

    #hiver det inn i en tom liste
    post_list_reg=[]
    for row in reg_markor:
        post_list_reg+=[row]
    
    
    #GUI for oversikt over eksamener og meny. 
    reg_eks_window=Toplevel()
    reg_eks_window.title('Registrering av eksamesresultater')

    lst_label_reg=Label(reg_eks_window,text='Emnekode | Dato | Rom')
    lst_label_reg.grid(row=0,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_reg=Scrollbar(reg_eks_window,orient=VERTICAL)
    y_scroll_reg.grid(row=1,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_eksamensliste_reg=StringVar()
    lst_eksamener_reg=Listbox(reg_eks_window,width=50,height=8,listvariable=innhold_i_eksamensliste_reg,yscrollcommand=y_scroll_reg.set)
    lst_eksamener_reg.grid(row=1,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    lst_eksamener_reg.bind('<<ListboxSelect>>',oppdater_seleksjon_reg)
    innhold_i_eksamensliste_reg.set(tuple(post_list_reg))

    y_scroll_reg['command']=lst_eksamener_reg.yview

    #knapper
    btn_legg_til_reg=Button(reg_eks_window,text='Legg til eksamensresultat for valgt eksamen',width=34,command=legg_til_eksamensresultat)
    btn_legg_til_reg.grid(row=9,column=0,padx=5,pady=(5,5),sticky=W)

    #avslutt
    btn_avslutt_ajour=Button(reg_eks_window,text='Lukk vindu',width=10,command=reg_eks_window.destroy)
    btn_avslutt_ajour.grid(row=9,column=2,padx=5,pady=5,sticky=E)

    reg_markor.close()

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

#kaster det i en main, mest så jeg kan kollapse det og slippe scrolling.
def main():
    #GUI
    window=Tk()
    window.title('Eksamenshåndtering')

    #frame for eksamensmanipulasjon
    eksamensmanipulasjon_frame=LabelFrame(window,text='Eksamensmanipulasjon')
    eksamensmanipulasjon_frame.grid(row=0,column=0,padx=5,pady=10,sticky=N)

    #knapper i framen
    btn_registrer_eksamensresultat=Button(eksamensmanipulasjon_frame,text='Legg til eksamensresultater',width=20,command=registrer_eksamensresultat)
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
main()