import os

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
                print('Tut å kjør, her skal det slettes!')
                print()
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
studentSlett()

print('Program avsluttet')