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




#snurr film
studentRegistrering()

print('Program avsluttet')