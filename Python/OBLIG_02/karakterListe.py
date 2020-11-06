def karakterListe():
    igjen=True

    while igjen==True:
        search=input('Skriv inn student du ønsker karakterutskrift på: ')

        funnet=False

        eksamensFil=open('eksamensresultat.txt','r')
        resultat=eksamensFil.readline()

        #tabell til å holde data
        eksamensdata=[]

        #kjører gjennom fila og dytter den inn i tabell så vi kan jobbe med den
        while resultat!='':
            resultat=resultat.rstrip('\n')
            if resultat==search:
                funnet=True
            eksamensdata+=[resultat]
            resultat=eksamensFil.readline()
        
        eksamensFil.close()


        if funnet==True:
            
            #hener ut persondata fra studen.txt 
            studentfil=open('student.txt','r')
            studentnr=studentfil.readline()

            #jobber gjennom fila og henter ut persondata tilknyttet studenten
            while studentnr!='':
                studentnr=studentnr.strip('\n')
               
                if studentnr==search:
                    fornavn=studentfil.readline()
                    fornavn=fornavn.rstrip('\n')
                    etternavn=studentfil.readline()
                    etternavn=etternavn.rstrip('\n')
                    studium=studentfil.readline()
                    studium=studium.rstrip('\n')
               
                studentnr=studentfil.readline()
            print()
            print('Her følger Eksamensdata for student',search,fornavn,etternavn,'som går studiet',studium)
            print()
            #egen liste for eksamensdata tilknyttet studentet
            student_eksamensdata=[]

            #vi teller antall eksamenstreff for bruk senere
            antall_treff=0

            #for loop for å finne treff på student nummer i eksamensdata.
            #range starter på index 1 som er studentnr, hop på 3 og siden vi karakter er siste så er lengde riktig max limit
            for i in range(1,len(eksamensdata),3):
                if eksamensdata[i]==search:
                    antall_treff+=1
                    #legger inn alle eksamenstreff inn i personifisert liste, vi beholder strukturen
                    student_eksamensdata+=[eksamensdata[i-1]] #emnekode
                    student_eksamensdata+=[eksamensdata[i]] #studentnr
                    student_eksamensdata+=[eksamensdata[i+1]] #karakter
            
            

            #vi knytter sammen emnekoder og emner i en liste så vi enkelt kan jobbe oss gjennom og sammenligne
            emner=[]

            emneFil=open('emne.txt','r')
            emnekode=emneFil.readline()

            #jobber oss gjennom fila og dytter den inn i tabell
            while emnekode!='':
                emnekode=emnekode.rstrip('\n')
                emnenavn=emneFil.readline()
                emnenavn=emnenavn.strip('\n')
                
                #legger data inn i tabell
                emner+=[emnekode]
                emner+=[emnenavn]

                emnekode=emneFil.readline()
            
            #knytte sammen emnekoder fra student_eksamensdata og får ut sluttprinten 
            #Vi ønsker først å mot treff på emnekode, like mange ganger som vi har funnet eksamensresultat på studenten
            for index in range(0,antall_treff*3,3):
                emnekode=student_eksamensdata[index]
                #vi går gjennom tabellen med emner og emnekoder og ser om vi har treff på den emnekoden hvor man har eksamensresultat
                for x in range(0,len(emner),2):
                    if emner[x]==emnekode:
                        #printer ut eksamenskarakterer og emneinfor for alle karakterer
                        print('Eksmamenskarakter for emnet',emner[x+1],'- (',emner[x],')')
                        print('Karakter:',student_eksamensdata[index+2])
            
            #styling            
            print()
        else:
            print('Studenten har ikke registrert eksamensdata.')
            print()
        
        mer=input('Ønsker du å se karakterutskrift fra flere studenter?: ')
        if mer=='nei':
            igjen=False 









karakterListe()

print('Program Slutt')