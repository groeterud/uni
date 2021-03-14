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
            #NBNB: OM DU HAR TID 
                #OM du selekterer en popup, så forsvinner seleksjonen i listeboksen, og den gamle lista blir overskrevet med en tom liste
                #Dette thrower en error. 
                # OM du har tid, finn en måte å ta vare på siste gyldige seleksjon og skriv en 'if valg_liste_ajour==None --> erstatt med gammel verdi. 
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
    btn_avslutt_reg=Button(reg_eks_window,text='Lukk vindu',width=10,command=reg_eks_window.destroy)
    btn_avslutt_reg.grid(row=9,column=2,padx=5,pady=5,sticky=E)

    reg_markor.close()

#resultater for enkelt emne
def vis_emneresultater():
    def oppdater_seleksjon_emne(event):
        global valgt_liste_emne #Gaddis s258 
        #skulle ønske jeg kunne passe argumenter med bind så jeg kunne bare hatt en funksjon og variabel på dette... 
        valgt_liste_emne=curselection_to_list(lst_eksamener_emneresultat)
        
    def vis_emneresultat_valg():
        valgt=valgt_liste_emne[0]

        qry=('''
            SELECT Studentnr,Karakter,Dato AS Eksamensdato
            FROM eksamensresultat
            WHERE Emnekode=%s
            ORDER BY Studentnr
            ''')
        #lager markør
        emneresultat_valg_markor=eksamensdatabase.cursor()
        emneresultat_valg_markor.execute(qry,(valgt,))
        
        post_list_emneresultat_valg=[]
        for row in emneresultat_valg_markor:
            post_list_emneresultat_valg+=[row]

        #GUI  
        emneresultat_valg_window=Toplevel()
        emneresultat_valg_window.title('Resultater for valgt emne')

        lst_label_emneresultat_valg=Label(emneresultat_valg_window,text='Studentnr | Karakter | Dato')
        lst_label_emneresultat_valg.grid(row=0,column=0,padx=5,pady=(5,0),sticky=W)
        #scrollbar
        y_scroll_emneresultat_valg=Scrollbar(emneresultat_valg_window,orient=VERTICAL)
        y_scroll_emneresultat_valg.grid(row=1,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

        innhold_i_liste_emneresultat_valg=StringVar()
        lst_eksamener_emneresultat_valg=Listbox(emneresultat_valg_window,width=50,height=8,listvariable=innhold_i_liste_emneresultat_valg,yscrollcommand=y_scroll_emneresultat_valg.set)
        lst_eksamener_emneresultat_valg.grid(row=1,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
        innhold_i_liste_emneresultat_valg.set(tuple(post_list_emneresultat_valg))

        y_scroll_emneresultat_valg['command']=lst_eksamener_emneresultat_valg.yview

        #avslutt
        btn_avslutt_emneresultat_valg=Button(emneresultat_valg_window,text='Lukk vindu',width=10,command=emneresultat_valg_window.destroy)
        btn_avslutt_emneresultat_valg.grid(row=9,column=2,padx=5,pady=5,sticky=E)


    #lager markøren vår
    emneresultat_markor=eksamensdatabase.cursor()
    #henter emnekoder
    emneresultat_markor.execute("SELECT Emnekode FROM emne")
    #hiver de i en liste
    post_list_emneresultat=[]
    for row in emneresultat_markor:
        post_list_emneresultat+=[row]

    #GUI  
    emneresultat_window=Toplevel()
    emneresultat_window.title('Visning av resultater i emne')

    lst_label_emneresultat=Label(emneresultat_window,text='Emnekode')
    lst_label_emneresultat.grid(row=0,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_emneresultat=Scrollbar(emneresultat_window,orient=VERTICAL)
    y_scroll_emneresultat.grid(row=1,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_liste_emneresultat=StringVar()
    lst_eksamener_emneresultat=Listbox(emneresultat_window,width=50,height=8,listvariable=innhold_i_liste_emneresultat,yscrollcommand=y_scroll_emneresultat.set)
    lst_eksamener_emneresultat.grid(row=1,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    lst_eksamener_emneresultat.bind('<<ListboxSelect>>',oppdater_seleksjon_emne)
    innhold_i_liste_emneresultat.set(tuple(post_list_emneresultat))

    y_scroll_emneresultat['command']=lst_eksamener_emneresultat.yview

    #knapper
    btn_legg_til_emneresultat=Button(emneresultat_window,text='Vis eksamensresultat for valgt emne',width=34,command=vis_emneresultat_valg)
    btn_legg_til_emneresultat.grid(row=9,column=0,padx=5,pady=(5,5),sticky=W)

    #avslutt
    btn_avslutt_emneresultat=Button(emneresultat_window,text='Lukk vindu',width=10,command=emneresultat_window.destroy)
    btn_avslutt_emneresultat.grid(row=9,column=2,padx=5,pady=5,sticky=E)
    
    emneresultat_markor.close()

#viser alle eksamensresultater for en enkelt eksamen
def vis_eksamensresultater_enkelt_eksamen():
    def oppdater_seleksjon_enk(event):
        global valgt_liste_enk #Gaddis s258 
        #skulle ønske jeg kunne passe argumenter med bind så jeg kunne bare hatt en funksjon og variabel på dette... 
        valgt_liste_enk=curselection_to_list(lst_eksamener_enk_eks)
    def vis_enk_eksamen_valg():
        #her må vi bruke infoen fra seleksjon til å hente ut resultatene tilknyttet den eksamen og vise i ny listebox. 
        eks_valgt_markor=eksamensdatabase.cursor()
        qry=("SELECT Studentnr, Karakter FROM eksamensresultat WHERE Emnekode=%s AND Dato=%s")
        data=(valgt_liste_enk[0],valgt_liste_enk[1])
        eks_valgt_dato=str(valgt_liste_enk[1])
        eks_valgt_markor.execute(qry,data)
        #tom liste med innholdet fra spørringen
        seleksjons_liste=[]
        #hiver data inn i listen
        for rows in eks_valgt_markor:
            seleksjons_liste+=[rows]
        
        #henter emnenavn
        qry=("SELECT Emnenavn FROM emne WHERE Emnekode=%s")
        data=(valgt_liste_enk[0],)
        eks_valgt_markor.execute(qry,data)
        emnenavn_eks_valgt=''
        for row in eks_valgt_markor:
            emnenavn_eks_valgt=str(row)
        #fjerner paranteser og appostrofer
        emnenavn_eks_valgt=emnenavn_eks_valgt.replace('(','').replace(')','').replace("'","").replace(",","")

        #lukker markøren når vi er ferdig med den
        eks_valgt_markor.close()
        eks_valgt_a=0
        eks_valgt_b=0
        eks_valgt_c=0
        eks_valgt_d=0
        eks_valgt_e=0
        eks_valgt_f=0
        #går gjennom lista og teller karakterer. Legger også på emenenavn
        for x in range(len(seleksjons_liste)):
            if seleksjons_liste[x][1]=='A':
                eks_valgt_a+=1
            elif seleksjons_liste[x][1]=='B':
                eks_valgt_b+=1
            elif seleksjons_liste[x][1]=='C':
                eks_valgt_c+=1
            elif seleksjons_liste[x][1]=='D':
                eks_valgt_d+=1
            elif seleksjons_liste[x][1]=='E':
                eks_valgt_e+=1
            else:
                eks_valgt_f+=1
            
  
        #GUI for visnig av eksamensresultater
        eks_valgt_window=Toplevel()
        eks_valgt_window.title('Eksamensresultater for '+emnenavn_eks_valgt)

        frame_emnenavn_eks_valgt=LabelFrame(eks_valgt_window,text='Eksamen i '+emnenavn_eks_valgt+' - '+eks_valgt_dato)
        frame_emnenavn_eks_valgt.grid(row=0,column=0,padx=5,pady=(5,0),sticky=W)

        lst_label_eks_valgt=Label(frame_emnenavn_eks_valgt,text='Studentnr | Karakter')
        lst_label_eks_valgt.grid(row=1,column=0,padx=5,pady=(5,0),sticky=W)
        #scrollbar
        y_scroll_eks_valgt=Scrollbar(frame_emnenavn_eks_valgt,orient=VERTICAL)
        y_scroll_eks_valgt.grid(row=2,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

        innhold_i_liste_eks_valgt=StringVar()
        lst_eksamener_eks_valgt=Listbox(frame_emnenavn_eks_valgt,width=40,height=8,listvariable=innhold_i_liste_eks_valgt,yscrollcommand=y_scroll_eks_valgt.set)
        lst_eksamener_eks_valgt.grid(row=2,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
        innhold_i_liste_eks_valgt.set(tuple(seleksjons_liste))
        y_scroll_eks_valgt['command']=lst_eksamener_eks_valgt.yview

        #labelframe for karakterfordeling.
        karakterfordeling_eks_valgt=LabelFrame(eks_valgt_window,text='Karakterfordeling')
        karakterfordeling_eks_valgt.grid(row=2,column=0,columnspan=2,padx=5,pady=0,sticky=W)

        #labels på row 0, enter på row 1
        lbl_a_eks_valgt=Label(karakterfordeling_eks_valgt,text='A:')
        lbl_a_eks_valgt.grid(row=0,column=0,padx=5,pady=(5,0),sticky=E)
        
        eks_valgt_a_SV=StringVar()
        ent_a_eks_valgt=Entry(karakterfordeling_eks_valgt,textvariable=eks_valgt_a_SV,state='readonly',width=3)
        ent_a_eks_valgt.grid(row=1,column=0,padx=5,pady=(0,5),sticky=W)

        lbl_b_eks_valgt=Label(karakterfordeling_eks_valgt,text='B:')
        lbl_b_eks_valgt.grid(row=0,column=1,padx=5,pady=(5,0),sticky=W)

        eks_valgt_b_SV=StringVar()
        ent_b_eks_valgt=Entry(karakterfordeling_eks_valgt,textvariable=eks_valgt_b_SV,state='readonly',width=3)
        ent_b_eks_valgt.grid(row=1,column=1,padx=5,pady=(0,5),sticky=W)

        lbl_c_eks_valgt=Label(karakterfordeling_eks_valgt,text='C:')
        lbl_c_eks_valgt.grid(row=0,column=2,padx=5,pady=(5,0),sticky=W)

        eks_valgt_c_SV=StringVar()
        ent_c_eks_valgt=Entry(karakterfordeling_eks_valgt,textvariable=eks_valgt_c_SV,state='readonly',width=3)
        ent_c_eks_valgt.grid(row=1,column=2,padx=5,pady=(0,5),sticky=W)

        lbl_d_eks_valgt=Label(karakterfordeling_eks_valgt,text='D:')
        lbl_d_eks_valgt.grid(row=0,column=3,padx=5,pady=(5,0),sticky=W)

        eks_valgt_d_SV=StringVar()
        ent_d_eks_valgt=Entry(karakterfordeling_eks_valgt,textvariable=eks_valgt_d_SV,state='readonly',width=3)
        ent_d_eks_valgt.grid(row=1,column=3,padx=5,pady=(0,5),sticky=W)

        lbl_e_eks_valgt=Label(karakterfordeling_eks_valgt,text='E:')
        lbl_e_eks_valgt.grid(row=0,column=4,padx=5,pady=(5,0),sticky=W)

        eks_valgt_e_SV=StringVar()
        ent_e_eks_valgt=Entry(karakterfordeling_eks_valgt,textvariable=eks_valgt_e_SV,state='readonly',width=3)
        ent_e_eks_valgt.grid(row=1,column=4,padx=5,pady=(0,5),sticky=W)

        lbl_f_eks_valgt=Label(karakterfordeling_eks_valgt,text='F:')
        lbl_f_eks_valgt.grid(row=0,column=5,padx=5,pady=(5,0),sticky=W)

        eks_valgt_f_SV=StringVar()
        ent_f_eks_valgt=Entry(karakterfordeling_eks_valgt,textvariable=eks_valgt_f_SV,state='readonly',width=3)
        ent_f_eks_valgt.grid(row=1,column=5,padx=5,pady=(0,5),sticky=W)

        #avslutt
        btn_avslutt_eks_valgt=Button(eks_valgt_window,text='Lukk vindu',width=10,command=eks_valgt_window.destroy)
        btn_avslutt_eks_valgt.grid(row=2,column=1,padx=5,pady=5,sticky=SE)

        #settere
        eks_valgt_a_SV.set(eks_valgt_a)
        eks_valgt_b_SV.set(eks_valgt_b)
        eks_valgt_c_SV.set(eks_valgt_c)
        eks_valgt_d_SV.set(eks_valgt_d)
        eks_valgt_e_SV.set(eks_valgt_e)
        eks_valgt_f_SV.set(eks_valgt_f)

    #markør    
    enk_eksamen_markor=eksamensdatabase.cursor()
    #henter alle poster registrert eksamensresultat, vi gjør også en sjekk for dato bare sånn i tilfelle. 
    enk_eksamen_markor.execute("SELECT Emnekode, Dato, Romnr, COUNT(*) AS Antall FROM eksamen JOIN eksamensresultat USING (Emnekode,Dato) WHERE Dato<=CURRENT_DATE() GROUP BY Emnekode,Dato HAVING Antall>0 ORDER BY Dato DESC")

    #hiver det inn i en tom liste
    post_list_enk_eks=[]
    for row in enk_eksamen_markor:
        post_list_enk_eks+=[row]
    
    #GUI for oversikt over eksamener og meny. 
    enk_eks_window=Toplevel()
    enk_eks_window.title('Visning av eksamensresultater')

    lst_label_enk_eks=Label(enk_eks_window,text='Emnekode | Dato | Rom | Antall registrerte eksamensresultat')
    lst_label_enk_eks.grid(row=0,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_enk_eks=Scrollbar(enk_eks_window,orient=VERTICAL)
    y_scroll_enk_eks.grid(row=1,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_liste_enk_eks=StringVar()
    lst_eksamener_enk_eks=Listbox(enk_eks_window,width=50,height=8,listvariable=innhold_i_liste_enk_eks,yscrollcommand=y_scroll_enk_eks.set)
    lst_eksamener_enk_eks.grid(row=1,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    lst_eksamener_enk_eks.bind('<<ListboxSelect>>',oppdater_seleksjon_enk)
    innhold_i_liste_enk_eks.set(tuple(post_list_enk_eks))

    y_scroll_enk_eks['command']=lst_eksamener_enk_eks.yview

    #knapper
    btn_legg_til_enk_eks=Button(enk_eks_window,text='Vis eksamensresultat for valgt eksamen',width=34,command=vis_enk_eksamen_valg)
    btn_legg_til_enk_eks.grid(row=9,column=0,padx=5,pady=(5,5),sticky=W)

    #avslutt
    btn_avslutt_enk_eks=Button(enk_eks_window,text='Lukk vindu',width=10,command=enk_eks_window.destroy)
    btn_avslutt_enk_eks.grid(row=9,column=2,padx=5,pady=5,sticky=E)
    

    enk_eksamen_markor.close()

#viser alle eksamensresultater for en enkelt student
def eksamensresultater_student():
    def student_eksamensres_sok():
        eksamensres_sok_markor=eksamensdatabase.cursor()
        studentnr=eksamensresultater_student_studnr_sv.get()
        qry=('''
            SELECT eksamensresultat.Dato,eksamensresultat.Emnekode,Emnenavn,Karakter,Studiepoeng
            FROM eksamensresultat,Emne
            WHERE eksamensresultat.Emnekode=emne.Emnekode 
            AND Studentnr=%s 
            ORDER BY eksamensresultat.Dato
        ''')
        eksamensres_sok_markor.execute(qry,(studentnr,))
        
        post_list_eksamensresultater_student=[]
        
        for row in eksamensres_sok_markor:
            post_list_eksamensresultater_student+=[row]
        
        eksamensres_sok_markor.close()
        
        innhold_i_liste_eksamensresultater_student.set(tuple(post_list_eksamensresultater_student))
    
    #GUI  
    eksamensresultater_student_window=Toplevel()
    eksamensresultater_student_window.title('Eksamensresultat for enkeltstudent')

    eksamensresultater_student_frame=LabelFrame(eksamensresultater_student_window,text='Søk opp student')
    eksamensresultater_student_frame.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    eksamensresultater_student_lbl_studnr=Label(eksamensresultater_student_frame,text='Studentnr:')
    eksamensresultater_student_lbl_studnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    eksamensresultater_student_studnr_sv=StringVar()
    eksamensresultater_student_ent_studnr=Entry(eksamensresultater_student_frame,textvariable=eksamensresultater_student_studnr_sv,width=6)
    eksamensresultater_student_ent_studnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    btn_student_eksamensres_sok=Button(eksamensresultater_student_frame,text='Søk',width=6,command=student_eksamensres_sok)
    btn_student_eksamensres_sok.grid(row=0,column=2,padx=5,pady=5,sticky=E)

    lst_label_eksamensresultater_student=Label(eksamensresultater_student_window,text='Dato | Emnekode | Emnenavn | Karakter | Studiepoeng')
    lst_label_eksamensresultater_student.grid(row=1,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_eksamensresultater_student=Scrollbar(eksamensresultater_student_window,orient=VERTICAL)
    y_scroll_eksamensresultater_student.grid(row=2,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_liste_eksamensresultater_student=StringVar()
    lst_eksamener_eksamensresultater_student=Listbox(eksamensresultater_student_window,width=65,height=8,listvariable=innhold_i_liste_eksamensresultater_student,yscrollcommand=y_scroll_eksamensresultater_student.set)
    lst_eksamener_eksamensresultater_student.grid(row=3,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    y_scroll_eksamensresultater_student['command']=lst_eksamener_eksamensresultater_student.yview

    #avslutt
    btn_avslutt_eksamensresultater_student=Button(eksamensresultater_student_window,text='Lukk vindu',width=10,command=eksamensresultater_student_window.destroy)
    btn_avslutt_eksamensresultater_student.grid(row=11,column=2,padx=5,pady=5,sticky=E)
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
    btn_vis_eksamensresultater=Button(visninger_frame,text='Vis alle eksamensresultater fra en eksamen',width=33,command=vis_eksamensresultater_enkelt_eksamen)
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