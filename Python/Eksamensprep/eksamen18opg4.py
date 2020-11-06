import os

def main():
    igjen=True

    while igjen==True:
        print('Velkommen til utlånsprogrammet')
        print()
        print('Du får nå 4 valg ')
        print()
        print('Skriv 1 for registrering av ny utlåner')
        print()
        print('Skriv 2 for nytt utlån')
        print()
        print('Skriv 3 for sletting av lånetager')
        print()
        print('Skriv 4 for å avslutte programmet')
        print()

        valg=input('Skriv inn ønsket valg: ')

        if valg=='1':
            ny_laanetager()
        else:
            if valg=='2':
                utlaan()
            else:
                if valg=='3':
                    slett()
                else:
                    if valg=='4':
                        igjen=False
                    else:
                        print('Ugyldig input, prøv igjen')

def ny_laanetager():
    #definerer persondata-fila sin struktur som: mobilnr, lånetagernr, fornavn, etternavn
    igjen=True

    while igjen==True:
        search=input('Skriv inn mobilnr på ny registrant: ')
        funnet=False

        brukerFil=open('brukere.txt','r')
        mobilnr=brukerFil.readline()

        while mobilnr!='':
            mobilnr=mobilnr.rstrip('\n')
            lnr=brukerFil.readline()
            lnr=lnr.rstrip('\n')
            fornavn=brukerFil.readline()
            fornavn=fornavn.rstrip('\n')
            etternavn=brukerFil.readline()
            etternavn=etternavn.rstrip('\n')

            if search==mobilnr:
                funnet=True
                print('Kan ikke registerer, fant bruker med mobilnummer:',mobilnr,'. Lånetagenummer:',lnr)        
            
            mobilnr=brukerFil.readline()

        brukerFil.close()

        if funnet==False:
            brukerFil=open('brukere.txt','a')
            lnr=input('Skriv inn lånetagernr: ')
            fornavn=input('Skriv inn fornavn: ')
            etternavn=input('Skriv inn etternavn: ')
            
            brukerFil.write(search+'\n')
            brukerFil.write(lnr+'\n')
            brukerFil.write(fornavn+'\n')
            brukerFil.write(etternavn+'\n')

        igjen=input('Ønsker du å registrere en ny student (y/n)? ')
        if igjen=='n':
            igjen=False
        else:
            igjen=True

#end ny_laanetager? 

def utlaan():
    igjen=True

    while igjen==True:
        

        search=input('Skriv inn lånetagernr på lånetager: ')
        funnet=False

        brukerFil=open('brukere.txt','r')
        mobilnr=brukerFil.readline()

        while mobilnr!='':
            mobilnr=mobilnr.rstrip('\n')
            lnr=brukerFil.readline()
            lnr=lnr.rstrip('\n')
            fornavn=brukerFil.readline()
            fornavn=fornavn.rstrip('\n')
            etternavn=brukerFil.readline()
            etternavn=etternavn.rstrip('\n')

            if search==lnr:
                funnet=True

            mobilnr=brukerFil.readline()

        brukerFil.close()

        if funnet==False:
            print('Beklager, du må registrere lånetageren først')
        else:
            utlaansregister=[]
            utlaansFil=open('Utlaan.txt','r')
            #struktur på utlånsfil <utlaansnr, lnr, ISBN, utlaansdato,innleveringsdato>
            utlaansnr=utlaansFil.readline()

            while utlaansnr!='':
                utlaansnr=utlaansnr.rstrip('\n')
                utlaansregister+=[utlaansnr]

                lnr=utlaansFil.readline()
                isbn=utlaansFil.readline()
                utlaansdato=utlaansFil.readline()
                innleveringsdato=utlaansFil.readline()

                utlaansnr=utlaansFil.readline()
            

            #beregner og tilordner neste sekvensielle utlånsnr
            utlaansFil.close()
            utlaansregister.sort(reverse=True)
            utlaansnr_ny=utlaansregister[0]
            utlaansnr_ny=int(utlaansnr_ny)+1
            utlaansnr=str(utlaansnr_ny)

            #skriv til fil
            utlaansFil=open('Utlaan.txt','a')
            lnr=search #bare overskriver verdien for å gjøre writen mer semantisk
            innleveringsdato='x' #vi må ha data i feltet for retroaktivitet. 
            isbn=input('Skriv in ISBN nummeret: ')
            utlaansdato=input('Skriv inn Utlånsdato (format år-måned-dag, eks 20201230: ')

            utlaansFil.write(utlaansnr+'\n')
            utlaansFil.write(lnr+'\n')
            utlaansFil.write(isbn+'\n')
            utlaansFil.write(utlaansdato+'\n')
            utlaansFil.write(innleveringsdato+'\n')

            utlaansFil.close()

        igjen=input('Ønsker du å registrere et til utlån (y/n)? ')
        if igjen=='n':
            igjen=False
        else:
            igjen=True

#slutt utlån

def slett():
    igjen=True
    
    while igjen==True:
        search=input('Skriv inn mobilnr på bruker som skal slettes: ')
        funnet=False
        funnet_utl=False
        brukerFil=open('brukere.txt','r')
        mobilnr=brukerFil.readline()

        while mobilnr!='':
            mobilnr=mobilnr.rstrip('\n')
            lnr=brukerFil.readline()
            lnr=lnr.rstrip('\n')
            fornavn=brukerFil.readline()
            fornavn=fornavn.rstrip('\n')
            etternavn=brukerFil.readline()
            etternavn=etternavn.rstrip('\n')

            if search==mobilnr:
                funnet=True
                utlaansFil=open('Utlaan.txt','r')
                #struktur på utlånsfil <utlaansnr, lnr, ISBN, utlaansdato,innleveringsdato>
                utlaansnr=utlaansFil.readline()

                while utlaansnr!='':
                    utlaansnr=utlaansnr.rstrip('\n')
                    lnr_utl=utlaansFil.readline()
                    lnr_utl=lnr_utl.rstrip('\n')
                    isbn=utlaansFil.readline()
                    utlaansdato=utlaansFil.readline()
                    innleveringsdato=utlaansFil.readline()
                    
                    if lnr==lnr_utl:
                        funnet_utl=True
                        print('Kan ikke slette, det er registrert utlån på lånetageren ')

                    utlaansnr=utlaansFil.readline()
                
                #beregner og tilordner neste sekvensielle utlånsnr
                utlaansFil.close()  
            mobilnr=brukerFil.readline()           
        brukerFil.close()

        if funnet==True and funnet_utl==False:
            brukerFil=open('brukere.txt','r')
            tempfil=open('tempfil.txt','w')
            mobilnr=brukerFil.readline()

            while mobilnr!='':
                mobilnr=mobilnr.rstrip('\n')
                lnr=brukerFil.readline()
                fornavn=brukerFil.readline()
                etternavn=brukerFil.readline()
              

                if search!=mobilnr:
                    tempfil.write(mobilnr+'\n')
                    tempfil.write(lnr)
                    tempfil.write(fornavn)
                    tempfil.write(etternavn)
                
                mobilnr=brukerFil.readline()

            brukerFil.close()
            tempfil.close()
            
            os.remove('brukere.txt')
            os.rename('tempfil.txt','brukere.txt')
           
            print('Bruker slettet')
        else:
            print('Bruker ikke funnet, kan ikke slette')


        igjen=input('Ønsker du å slette en til registrant (y/n)? ')
        if igjen=='n':
            igjen=False
        else:
            igjen=True

#slutt på slett
main()