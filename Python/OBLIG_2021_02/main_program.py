import mysql.connector
from tkinter import *
from tkinter import messagebox

from mysql.connector.errors import DataError

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

#gjør en av to spørringer basert på input og returnerer en liste med data fra spørringen.
def eksamen_dato_til_liste(nedre,ovre=True):
    eksamen_dato_markor=eksamensdatabase.cursor()
    #om bare en dato
    if ovre==True:
        qry=('''
            SELECT *
            FROM eksamen
            WHERE Dato=%s
        ''')
        data=(nedre)
        eksamen_dato_markor.execute(qry,(data,))
    #eller om vi har fått en verdi på ovre
    else:
        qry=('''
            SELECT *
            FROM eksamen
            WHERE Dato>=%s AND Dato<=%s
            ORDER BY Dato
        ''')
        data=(nedre,ovre)
        eksamen_dato_markor.execute(qry,data)

    #lager liste
    eksamensliste=[]
    for row in eksamen_dato_markor:
        eksamensliste+=[row]

    eksamen_dato_markor.close()
    return(eksamensliste)
    
#ajourføring av fremtidige eksamener
def ajour_eksamen():     
    #trigger for å oppdatere seleksjonen. Dette er fordi vi må ha tilgang til valgt_liste i andre TopLevels, 
    # så de må arve denne variabelen når de ikke kan kalle funksjonen. Bruker avarter av denne funksjonen flere ganger. 
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

def ajour_student():
    print('ajour_student')

def legg_til_student():
    #henter høyeste studentnr+1 fra databasen 
    def nytt_studentnr():
        studentnr_markor=eksamensdatabase.cursor()
        #henter ut høyeste studentnr og legger det i en liste
        studentnr_markor.execute('''
            SELECT MAX(Studentnr)
            FROM student 
        ''')
        studentnr_liste=[]
        for row in studentnr_markor:
            studentnr_liste+=[row]
        studentnr_markor.close()
        #øker det med 1 og gjør det om til streng for input
        studentnr=int(studentnr_liste[0][0])
        studentnr+=1
        studentnr=str(studentnr)
        #hiver det tilbake
        return(studentnr)
        
    def insert_student():
        #henter høyeste studentnr+1 fra databasen 
        studentnr=nytt_studentnr()
        #henter verdier fra input
        fornavn=fornavn_sv.get()
        etternavn=etternavn_sv.get()
        epost=epost_sv.get()
        tlfnr=telefon_sv.get()

        #lager markør og spørringsstruktur
        insert_markor=eksamensdatabase.cursor()
        qry=("INSERT INTO Student VALUES (%s,%s,%s,%s,%s)")
        data=(studentnr,fornavn,etternavn,epost,tlfnr)
        #utfører
        insert_markor.execute(qry,data)
        #commiter
        eksamensdatabase.commit()
        insert_markor.close()
        messagebox.showinfo('Velykket','Studenten ble lagret')    
    
    #GUI 
    legg_til_student_window=Toplevel()
    legg_til_student_window.title('Legg til en ny student')

    lbl_fornavn=Label(legg_til_student_window,text='Fornavn')
    lbl_fornavn.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    fornavn_sv=StringVar()
    ent_fornavn=Entry(legg_til_student_window,width=30,textvariable=fornavn_sv)
    ent_fornavn.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lbl_etternavn=Label(legg_til_student_window,text='Etternavn')
    lbl_etternavn.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    etternavn_sv=StringVar()
    ent_etternavn=Entry(legg_til_student_window,width=20,textvariable=etternavn_sv)
    ent_etternavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    lbl_epost=Label(legg_til_student_window,text='E-post')
    lbl_epost.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    epost_sv=StringVar()
    ent_epost=Entry(legg_til_student_window,width=40,textvariable=epost_sv)
    ent_epost.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    lbl_telefon=Label(legg_til_student_window,text='Telefon')
    lbl_telefon.grid(row=3,column=0,padx=5,pady=5,sticky=W)

    telefon_sv=StringVar()
    ent_telefon=Entry(legg_til_student_window,width=8,textvariable=telefon_sv)
    ent_telefon.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    btn_insert=Button(legg_til_student_window,text='Lagre',width=10,command=insert_student)
    btn_insert.grid(row=4,column=0,padx=5,pady=5,sticky=W)

    btn_avslutt_insert=Button(legg_til_student_window,text='Lukk vindu',width=15,command=legg_til_student_window.destroy)
    btn_avslutt_insert.grid(row=4,column=1,padx=5,pady=5,sticky=E)


#registrerer flere eksamensresultat for en avholdt eksamen.  
def registrer_eksamensresultat():
    reg_markor=eksamensdatabase.cursor()

    def oppdater_seleksjon_reg(event):
        global valgt_liste_reg #Gaddis s258 
        valgt_liste_reg=curselection_to_list(lst_eksamener_reg)

    def legg_til_eksamensresultat():
        def lagre_karakterer():
            karakterer=[]
            data=[]
            for x in range(len(karakter_sv_liste)):
                tempvar=karakter_sv_liste[x].get()
                #if test for å se om man ikke har tastet inn noen verdi i et felt. Sørger for at vi beholder NULL på det punktet. 
                if tempvar=='':
                    tempvar=None
                karakterer+=[tempvar]
                data+=[(tempvar,post_list_eks_updt[x][2],post_list_eks_updt[x][3],post_list_eks_updt[x][4])]

            #ny markør
            lagrings_markor=eksamensdatabase.cursor()
            query=("UPDATE Eksamensresultat SET Karakter=%s WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s")

            lagrings_markor.executemany(query,data)
            eksamensdatabase.commit()
            lagrings_markor.close()

            messagebox.showinfo('Vellykket','Karakterene ble lagret!')
        #fanger emnekode og dato for seleksjonen.     
        emnekode_reg=valgt_liste_reg[0]
        dato_reg=valgt_liste_reg[1]

        #markør for å hente seleksjonen for den valgte eksamen
        markor_eksamen=eksamensdatabase.cursor()
        qry=('''
            SELECT Fornavn,Etternavn,Eksamensresultat.*
            FROM Eksamensresultat JOIN 
                Student USING (Studentnr)
            WHERE Karakter IS NULL AND Emnekode=%s AND Dato=%s
        ''')
        data=(emnekode_reg,dato_reg)
        markor_eksamen.execute(qry,data)
        post_list_eks_updt=[]
        
        for row in markor_eksamen:
            post_list_eks_updt+=[row]

        markor_eksamen.close()
        #enkel gui ramme
        legg_til_vindu_reg=Toplevel()
        legg_til_vindu_reg.title('Masseregistrering av eksamensresultat')

        registrering=LabelFrame(legg_til_vindu_reg,text='Skriv inn karakterer på registrerte studenter')
        registrering.grid(row=0,column=0,padx=5,pady=5)

        navn_header=Label(registrering,text='Navn')
        navn_header.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studnr_header=Label(registrering,text='Studentnr')
        studnr_header.grid(row=0,column=1,padx=5,pady=5)

        kar_header=Label(registrering,text='Karakter')
        kar_header.grid(row=0,column=2,padx=5,pady=5)

        karakter_sv_liste=[]

        for x in range(len(post_list_eks_updt)):
            
            lbl_navn=Label(registrering,text=post_list_eks_updt[x][0]+' '+post_list_eks_updt[x][1])
            lbl_navn.grid(row=x+1,column=0,padx=5,pady=5,sticky=W)
            

            lbl_studentID=Label(registrering,text=post_list_eks_updt[x][2])
            lbl_studentID.grid(row=x+1,column=1,padx=5,pady=5)

            sv_Karakter=StringVar()
            ent_Karakter=Entry(registrering,textvariable=sv_Karakter,width=2)
            ent_Karakter.grid(row=x+1,column=2,padx=5,pady=5)

            karakter_sv_liste+=[sv_Karakter]


        btn_lagre=Button(legg_til_vindu_reg,text='Lagre',width=10,command=lagre_karakterer)
        btn_lagre.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        btn_avslutt_legg_til_reg=Button(legg_til_vindu_reg,text='Avslutt',width=8,command=legg_til_vindu_reg.destroy)
        btn_avslutt_legg_til_reg.grid(row=1,column=1,padx=5,pady=(10,5),sticky=E)

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

def registrer_eksamen():
    reg_eks_markor=eksamensdatabase.cursor()

    def oppdater_seleksjon_reg_eks(event):
        global valgt_liste_reg_eks #Gaddis s258 
        valgt_liste_reg_eks=curselection_to_list(lst_eksamener_reg_eks)

    def legg_til_deltagere():
        def lagre_deltager():
            #henter innhold fra tekstboksen, og setter det i en liste
            innhold_i_textbox=input_tekstbox.get("1.0","end")
            innhold_i_textbox=innhold_i_textbox.replace('\n','')
            liste_textbox=innhold_i_textbox.split(',')

            #henter annen info vi trenger for å strukturere insert setningen.
            emnekode=valgt_liste_reg_eks[0]
            dato=valgt_liste_reg_eks[1]

            #lager tabellen vi bruker for executemany. 
            data=[]
            for x in range(len(liste_textbox)):
                data+=[(liste_textbox[x],emnekode,dato,None)]

            query=("INSERT INTO Eksamensresultat VALUES (%s,%s,%s,%s)")
            markor_lagre_deltagere=eksamensdatabase.cursor()
            markor_lagre_deltagere.executemany(query,data)
            eksamensdatabase.commit()
            markor_lagre_deltagere.close()

            messagebox.showinfo('Vellykket','Deltager(e) lagret')
        #enkel gui ramme
        legg_til_vindu_reg=Toplevel()
        legg_til_vindu_reg.title('Registrering av eksamensdeltagere')

        registrering_studnr=LabelFrame(legg_til_vindu_reg,text='Skriv inn studentnr på deltagere')
        registrering_studnr.grid(row=1,column=0,padx=5,pady=5)
        
        info_lbl=Label(legg_til_vindu_reg,text='Skriv inn studentnr for hver student, separert med komma for alle studenter \ndu ønsker å registrere på valgt eksamen\n Eksempel: 240214,240213,24015')
        info_lbl.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        input_tekstbox=Text(registrering_studnr,height=10,width=60)
        input_tekstbox.grid(row=0,column=0,columnspan=2,padx=5,pady=5)

        btn_lagre=Button(legg_til_vindu_reg,text='Lagre',width=10,command=lagre_deltager)
        btn_lagre.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        btn_avslutt_legg_til_reg=Button(legg_til_vindu_reg,text='Avslutt',width=8,command=legg_til_vindu_reg.destroy)
        btn_avslutt_legg_til_reg.grid(row=2,column=1,padx=5,pady=(10,5),sticky=E)

    #henter alle poster med datering etter dagens dato. 
    reg_eks_markor.execute("SELECT * FROM eksamen ORDER BY Dato DESC")

    #hiver det inn i en tom liste
    post_list_reg_eks=[]
    for row in reg_eks_markor:
        post_list_reg_eks+=[row]
    
    
    #GUI for oversikt over eksamener og meny. 
    reg_eks_window=Toplevel()
    reg_eks_window.title('Registrering av eksamensdeltagere')

    lst_label_reg_eks=Label(reg_eks_window,text='Emnekode | Dato | Rom')
    lst_label_reg_eks.grid(row=0,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_reg_eks=Scrollbar(reg_eks_window,orient=VERTICAL)
    y_scroll_reg_eks.grid(row=1,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_eksamensliste_reg_eks=StringVar()
    lst_eksamener_reg_eks=Listbox(reg_eks_window,width=50,height=8,listvariable=innhold_i_eksamensliste_reg_eks,yscrollcommand=y_scroll_reg_eks.set)
    lst_eksamener_reg_eks.grid(row=1,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    lst_eksamener_reg_eks.bind('<<ListboxSelect>>',oppdater_seleksjon_reg_eks)
    innhold_i_eksamensliste_reg_eks.set(tuple(post_list_reg_eks))

    y_scroll_reg_eks['command']=lst_eksamener_reg_eks.yview

    #knapper
    btn_legg_til_reg=Button(reg_eks_window,text='Legg til eksamensdeltagere for valgt eksamen',width=34,command=legg_til_deltagere)
    btn_legg_til_reg.grid(row=9,column=0,padx=5,pady=(5,5),sticky=W)

    #avslutt
    btn_avslutt_reg=Button(reg_eks_window,text='Lukk vindu',width=10,command=reg_eks_window.destroy)
    btn_avslutt_reg.grid(row=9,column=2,padx=5,pady=5,sticky=E)

    reg_eks_markor.close()

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
            WHERE Emnekode=%s AND Karakter IS NOT NULL
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
        qry=("SELECT Studentnr, Karakter FROM eksamensresultat WHERE Emnekode=%s AND Dato=%s AND Karakter IS NOT NULL")
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
            AND Studentnr=%s AND Karakter IS NOT NULL
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

#vis vitnemål
def vitnemal():

    def vitnemal_sok():
        vitnemal_sok_markor=eksamensdatabase.cursor()
        studentnr=vitnemal_studnr_sv.get()
        qry=('''
        SELECT eksamensresultat.Emnekode,Emnenavn,MIN(Karakter) AS StandpunktKarakter,Studiepoeng
        FROM eksamensresultat,Emne
        WHERE eksamensresultat.Emnekode=emne.Emnekode 
        AND Studentnr=%s
        GROUP BY eksamensresultat.Emnekode
        ORDER BY SUBSTRING(eksamensresultat.Emnekode,4),eksamensresultat.Emnekode
        ''')
        vitnemal_sok_markor.execute(qry,(studentnr,))
        
        post_list_vitnemal=[]
        
        for row in vitnemal_sok_markor:
            post_list_vitnemal+=[row]

        vitnemal_sok_markor.close()
        
        innhold_i_liste_vitnemal.set(tuple(post_list_vitnemal))

        #summerer studiepoeng
        studiepoeng=0
        for x in range(len(post_list_vitnemal)):
            studiepoeng+=post_list_vitnemal[x][3]
        
        vitnemal_studiepoeng_sv.set(studiepoeng)
    

    #GUI  
    vitnemal_window=Toplevel()
    vitnemal_window.title('Eksamensresultat for enkeltstudent')

    vitnemal_frame=LabelFrame(vitnemal_window,text='Søk opp student')
    vitnemal_frame.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    vitnemal_lbl_studnr=Label(vitnemal_frame,text='Studentnr:')
    vitnemal_lbl_studnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    vitnemal_studnr_sv=StringVar()
    vitnemal_ent_studnr=Entry(vitnemal_frame,textvariable=vitnemal_studnr_sv,width=6)
    vitnemal_ent_studnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    btn_student_eksamensres_sok=Button(vitnemal_frame,text='Søk',width=6,command=vitnemal_sok)
    btn_student_eksamensres_sok.grid(row=0,column=2,padx=5,pady=5,sticky=E)

    lst_label_vitnemal=Label(vitnemal_window,text='Emnekode | Emnenavn | Standpunkt | Studiepoeng')
    lst_label_vitnemal.grid(row=1,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_vitnemal=Scrollbar(vitnemal_window,orient=VERTICAL)
    y_scroll_vitnemal.grid(row=2,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_liste_vitnemal=StringVar()
    lst_eksamener_vitnemal=Listbox(vitnemal_window,width=65,height=8,listvariable=innhold_i_liste_vitnemal,yscrollcommand=y_scroll_vitnemal.set)
    lst_eksamener_vitnemal.grid(row=3,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    y_scroll_vitnemal['command']=lst_eksamener_vitnemal.yview

    vitnemal_studiepoeng_frame=LabelFrame(vitnemal_window,text='Studiepoeng')
    vitnemal_studiepoeng_frame.grid(row=11,column=0,padx=5,pady=5,sticky=W)

    vitnemal_studiepoeng_lbl=Label(vitnemal_studiepoeng_frame,text='Totalt antall studiepoeng')
    vitnemal_studiepoeng_lbl.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    vitnemal_studiepoeng_sv=StringVar()
    vitnemal_studiepoeng_ent=Entry(vitnemal_studiepoeng_frame,width=5,textvariable=vitnemal_studiepoeng_sv,state='readonly')
    vitnemal_studiepoeng_ent.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #avslutt
    btn_avslutt_vitnemal=Button(vitnemal_window,text='Lukk vindu',width=10,command=vitnemal_window.destroy)
    btn_avslutt_vitnemal.grid(row=11,column=2,padx=5,pady=5,sticky=E)

#viser alle eksamener på en gitt dag
def eksamener_dag():
    def vis_eksamener():
        #henter dato fra input
        dato_inn=eksamener_dag_dato_sv.get()
        #får en liste ut fra SQL spørring på datoen
        eksamensliste=eksamen_dato_til_liste(dato_inn)
        #setter listen inn i listeboksen
        innhold_i_liste_eksamener_dag.set(eksamensliste)
        
    #GUI  
    eksamener_dag_window=Toplevel()
    eksamener_dag_window.title('Alle eksamener på en enkelt dag')

    eksamener_dag_frame=LabelFrame(eksamener_dag_window,text='Søk opp dato')
    eksamener_dag_frame.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    eksamener_dag_lbl_dato=Label(eksamener_dag_frame,text='Dato (ÅÅÅÅMMDD):')
    eksamener_dag_lbl_dato.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    eksamener_dag_dato_sv=StringVar()
    eksamener_dag_ent_dato=Entry(eksamener_dag_frame,textvariable=eksamener_dag_dato_sv,width=10)
    eksamener_dag_ent_dato.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    btn_vis_eksamener=Button(eksamener_dag_frame,text='Søk',width=6,command=vis_eksamener)
    btn_vis_eksamener.grid(row=0,column=2,padx=5,pady=5,sticky=E)

    lst_label_eksamener_dag=Label(eksamener_dag_window,text='Emnekode | Dato | Romnr')
    lst_label_eksamener_dag.grid(row=1,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_eksamener_dag=Scrollbar(eksamener_dag_window,orient=VERTICAL)
    y_scroll_eksamener_dag.grid(row=2,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_liste_eksamener_dag=StringVar()
    lst_eksamener_eksamener_dag=Listbox(eksamener_dag_window,width=65,height=8,listvariable=innhold_i_liste_eksamener_dag,yscrollcommand=y_scroll_eksamener_dag.set)
    lst_eksamener_eksamener_dag.grid(row=3,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    y_scroll_eksamener_dag['command']=lst_eksamener_eksamener_dag.yview

    #avslutt
    btn_avslutt_eksamener_dag=Button(eksamener_dag_window,text='Lukk vindu',width=10,command=eksamener_dag_window.destroy)
    btn_avslutt_eksamener_dag.grid(row=11,column=2,padx=5,pady=5,sticky=E)

#viser alle eksamener i en gitt periode
def eksamener_periode():
    def vis_eksamener_periode():
        #henter dato fra input
        dato_nedre=eksamener_periode_dato_sv_nedre.get()
        dato_ovre=eksamener_periode_dato_sv_ovre.get()
        #får en liste ut fra SQL spørring på datoen
        eksamensliste=eksamen_dato_til_liste(dato_nedre,dato_ovre)
        #setter listen inn i listeboksen
        innhold_i_liste_eksamener_periode.set(eksamensliste)
        
    #GUI  
    eksamener_periode_window=Toplevel()
    eksamener_periode_window.title('Alle eksamener i en periode')

    eksamener_periode_frame=LabelFrame(eksamener_periode_window,text='Tidsperiode')
    eksamener_periode_frame.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    eksamener_periode_lbl_dato_nedre=Label(eksamener_periode_frame,text='Startdato (ÅÅÅÅMMDD):')
    eksamener_periode_lbl_dato_nedre.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    eksamener_periode_dato_sv_nedre=StringVar()
    eksamener_periode_ent_dato_nedre=Entry(eksamener_periode_frame,textvariable=eksamener_periode_dato_sv_nedre,width=10)
    eksamener_periode_ent_dato_nedre.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    eksamener_periode_lbl_dato_ovre=Label(eksamener_periode_frame,text='Sluttdato (ÅÅÅÅMMDD):')
    eksamener_periode_lbl_dato_ovre.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    eksamener_periode_dato_sv_ovre=StringVar()
    eksamener_periode_ent_dato_ovre=Entry(eksamener_periode_frame,textvariable=eksamener_periode_dato_sv_ovre,width=10)
    eksamener_periode_ent_dato_ovre.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    btn_vis_eksamener=Button(eksamener_periode_frame,text='Søk',width=6,command=vis_eksamener_periode)
    btn_vis_eksamener.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    lst_label_eksamener_periode=Label(eksamener_periode_window,text='Emnekode | Dato | Romnr')
    lst_label_eksamener_periode.grid(row=1,column=0,padx=5,pady=(5,0),sticky=W)
    #scrollbar
    y_scroll_eksamener_periode=Scrollbar(eksamener_periode_window,orient=VERTICAL)
    y_scroll_eksamener_periode.grid(row=2,column=1,rowspan=8,padx=(0,5),pady=5,sticky=NS)

    innhold_i_liste_eksamener_periode=StringVar()
    lst_eksamener_eksamener_periode=Listbox(eksamener_periode_window,width=65,height=8,listvariable=innhold_i_liste_eksamener_periode,yscrollcommand=y_scroll_eksamener_periode.set)
    lst_eksamener_eksamener_periode.grid(row=3,column=0,rowspan=8,padx=(5,0),pady=5,sticky=E)
    y_scroll_eksamener_periode['command']=lst_eksamener_eksamener_periode.yview

    #avslutt
    btn_avslutt_eksamener_periode=Button(eksamener_periode_window,text='Lukk vindu',width=10,command=eksamener_periode_window.destroy)
    btn_avslutt_eksamener_periode.grid(row=11,column=2,padx=5,pady=5,sticky=E)

#kaster GUI i en main, mest så jeg kan kollapse det og slippe scrolling.
def main():
    #GUI
    window=Tk()
    window.title('Eksamenshåndtering')

    #frame for eksamensmanipulasjon
    eksamensmanipulasjon_frame=LabelFrame(window,text='Eksamensmanipulasjon')
    eksamensmanipulasjon_frame.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    #knapper i framen
    btn_registrer_eksamensresultat=Button(eksamensmanipulasjon_frame,text='Legg til eksamensresultater',width=22,command=registrer_eksamensresultat)
    btn_registrer_eksamensresultat.grid(row=0,column=0,padx=5,pady=(10,5),sticky=W)

    btn_registrer_eksamen=Button(eksamensmanipulasjon_frame,text='Registrer eksamensdeltagere',width=22,command=registrer_eksamen)
    btn_registrer_eksamen.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btn_ajour=Button(eksamensmanipulasjon_frame,text='Legg til, slett eller endre eksamen',width=26,command=ajour_eksamen)
    btn_ajour.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    #frame for enkeltstudent, ble rotete med for mange visninger
    visninger=LabelFrame(window,text='Visninger')
    visninger.grid(row=0,rowspan=2,column=1,padx=5,pady=5,sticky=NW)

    btn_vitnemal=Button(visninger,text='Vis vitnemål for en student',width=22,command=vitnemal)
    btn_vitnemal.grid(row=0,column=0,padx=5,pady=(10,5),sticky=W)

    btn_vis_eksamensresultater_student=Button(visninger,text='Vis alle eksamensresultater for enkeltstudent',width=34,command=eksamensresultater_student)
    btn_vis_eksamensresultater_student.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btn_vis_eksamensresultater=Button(visninger,text='Vis alle eksamensresultater fra en eksamen',width=33,command=vis_eksamensresultater_enkelt_eksamen)
    btn_vis_eksamensresultater.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    btn_vis_emneresultater=Button(visninger,text='Vis eksamensresultater i et emne',width=26,command=vis_emneresultater)
    btn_vis_emneresultater.grid(row=3,column=0,padx=5,pady=5,sticky=W)

    btn_eksamener_periode=Button(visninger,text='Vis alle eksamener i en bestemt periode',width=31,command=eksamener_periode)
    btn_eksamener_periode.grid(row=4,column=0,padx=5,pady=5,sticky=W)
    
    #frame for ajourhold for student, jukser litt med paddingen for at det skal se ok ut
    ajourhold_student_frame=LabelFrame(window,text='Studentspesifikk ajourhold')
    ajourhold_student_frame.grid(row=1,column=0,padx=5,pady=5,sticky=NW)

    #knapp i framet
    btn_ajour_student=Button(ajourhold_student_frame,text='Ajourføring for enkeltstudent',width=24,command=ajour_student)
    btn_ajour_student.grid(row=0,column=0,padx=5,pady=(10,5),sticky=W)

    btn_legg_til_student=Button(ajourhold_student_frame,text='Legg til ny student',width=24,command=legg_til_student)
    btn_legg_til_student.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btn_eksamener_dag=Button(visninger,text='Vis alle eksamener på en bestemt dag',width=30,command=eksamener_dag)
    btn_eksamener_dag.grid(row=5,column=0,padx=5,pady=5,sticky=W)

    #Terminer program
    btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
    btn_avslutt.grid(row=3,column=1,padx=5,pady=5,sticky=E)

    window.mainloop()
main()