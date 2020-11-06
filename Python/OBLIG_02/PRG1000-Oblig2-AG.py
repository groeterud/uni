import os

def studentRegistrering():
    igjen=True

    while igjen==True:
        #input fra bruker
        search=input('Skriv inn studentnr på studenten: ')
        print()
        print('Gjennomgår filen for å se om studentnummere allerede eksisterer') 
        print()
        #åpner studentfilen i append mode så vi kan søke gjennom den og skrive inn studentdata 
        studentfil=open('student.txt','r')
        #a+ starter alltid på slutten av fila
        studentnr=studentfil.readline()
        #flag for å se om vi har en match på stud nr
        funnet=False
        
        #while loop for å jobbe gjennom fila
        while studentnr != '':
            #hopper over fornavn, etternavn og studie, vi ønsker bare å sjekke alle studentnr
            studentfil.readline()
            studentfil.readline()
            studentfil.readline()

            #fjerner linjeskift fra studentnr
            studentnr=studentnr.strip('\n')
            
            if studentnr==search:
                funnet=True
        
            studentnr=studentfil.readline()

        studentfil.close()
        
        if funnet==True:
            print('Studentnummer eksisterer allerede, kan ikke overskrive eksisterende studentdata')
        else:
            print('Studentummer ikke funnet, registrering kan fortsette.')
            print()
            #åpner fila i append mode så vi kan legge til studentinformasjonen på slutten av fila
            studentfil=open('student.txt','a')
            #skriver studentnr til fil
            studentfil.write(search+'\n')
            #henter og skriver fornavn
            fornavn=input('Skriv inn fornavn: ')
            studentfil.write(fornavn+'\n')
            #henter og skriver etternavn
            etternavn=input('Skriv inn etternavn: ')
            studentfil.write(etternavn+'\n')
            #henter og skriver studium
            studium=input('Hvilket studie går studenten?: ')
            studentfil.write(studium+'\n')

            studentfil.close()

            print()
            print('Studentdata lagret')
            print()
    
        mer=input('Ønsker du å legge til flere studenter?: ')
        if mer=='nei':
            igjen=False  

def studentSlett():
    igjen=True
    
    while igjen==True:
        search=input('Skriv inn studentnummeret på studenten du ønsker å slette: ')
        print()
        print('Utfører kontroll for å se om studenten finnes i studentregisteret')
        print()

        #åpner og starter lesing av linje inn i variabel
        studentfil=open('student.txt','r')
        studentnr=studentfil.readline()

        funnet=False

        while studentnr!='':
            #hopper over fornavn, etternavn og studie, vi ønsker bare å sjekke alle studentnr
            studentfil.readline()
            studentfil.readline()
            studentfil.readline()

            #fjerner linjeskift fra studentnr
            studentnr=studentnr.strip('\n')
            
            if studentnr==search:
                funnet=True
                print('Studentnummer har blitt funnet i student.txt')
                print()
        
            studentnr=studentfil.readline()

        studentfil.close()
        
        if funnet==True:
             #åpner eksamensresultater for å se om studenten har registrert eksamensresultat
            studentfil=open('eksamensresultat.txt','r')
            studentnr=studentfil.readline()

            funnet=False

            while studentnr!='':

                #fjerner linjeskift fra studentnr
                studentnr=studentnr.strip('\n')
                
                if studentnr==search:
                    funnet=True
                    print('Studentnummer har blitt funnet i eksamensresultat.txt')
                    print()
                studentnr=studentfil.readline()

            studentfil.close()

            if funnet==True:
                print('Beklager, kan ikke slette student med eksamensresultater.')
                print()
            else:
                #åpner temp fil for å mellomlagre data og studentfilen for gjennomgang
                tempfil=open('tempfil.txt','w')
                studentfil=open('student.txt','r')
                studentnr=studentfil.readline()

                while studentnr!='':
                    studentnr=studentnr.rstrip('\n')
                    #definerer relative variabler
                    fornavn=studentfil.readline()
                    etternavn=studentfil.readline()
                    studium=studentfil.readline()

                    #skriver alle datapunktene vi skal beholde til temp fila
                    if studentnr!=search:
                        tempfil.write(studentnr+'\n')
                        tempfil.write(fornavn)
                        tempfil.write(etternavn)
                        tempfil.write(studium)

                    studentnr=studentfil.readline()
                
                #lukker filene
                tempfil.close()
                studentfil.close()

                #fjerner gammel student.txt og endrer navn på tempfila til student.txt
                os.remove('student.txt')
                os.rename('tempfil.txt','student.txt')

                print('Studentens data har blitt slettet!')
                print()

        else:
            print('Ingen student med det studentnummeret.')
            print()
       
        mer=input('Ønsker du å slette flere studenter?: ')
        if mer=='nei':
            igjen=False

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

def main():
    igjen=True
    #while løkke for å påse at programmet bare avsluttes av brukerens eget ønske 
    while igjen==True:
        print()
        print('Velkommen til Studentdata')
        print()
        print('I denne menyen har du følgende valg:')
        print('Valg 1 - Legg til ny student')
        print('Valg 2 - Slett student')
        print('Valg 3 - Skriv ut karakterliste på student')
        print()
        print('Valg 9 - Avslutt program')
        print()

        valg=int(input('Vennligst velg et av alternativene i menyen for å gå videre: '))

        if valg==1:
            studentRegistrering()
        else:
            if valg==2:
                studentSlett()
            else:
                if valg==3:
                    karakterListe()
                else:
                    if valg==9:
                        igjen=False
                    else:
                        print('Ugyldig input, vennligst tast inn ett av valgene')

main()
print()
print('Program Avsluttet')