import os

def main():
    igjen=True

    while igjen:
        print('Velg 1 for å registrere ny kunde')
        print('Velg 2 for å registrere ny hund')
        print('Velg 3 for å slette kunde')
        print('velg 5 for å avslutte')

        valg=input('Skriv inn ditt valg: ')

        if valg=='1':
            registrer_ny_kunde()
        else:
            if valg=='2':
                registrer_ny_hund()
            else: 
                if valg=='3':
                    slett_kunde()
                else:
                    if valg=='5':
                        igjen=False
#ferdig main()

def registrer_ny_kunde():
    search=input('Skriv inn kundens mobilnr: ')

    kundefil=open('kunde.txt','r')
    mobilnr=kundefil.readline()

    funnet=False

    while mobilnr!='':
        fornavn=kundefil.readline()
        etternavn=kundefil.readline()
        betalingskortnr=kundefil.readline()

        mobilnr=mobilnr.rstrip('\n')
        fornavn=fornavn.rstrip('\n')
        etternavn=etternavn.rstrip('\n')
        betalingskortnr=betalingskortnr.rstrip('\n')

        if mobilnr==search:
            funnet=True
    
    kundefil.close()
    if funnet==True:
        print('Beklager, kan ikke overskrive kundedata')
    else:
        kundefil=open('kunde.txt','a')
        kundefil.write(search+('\n'))#mobilnr
        fornavn=input('Skriv inn fornavn: ')
        etternavn=input('Skriv inn etternavn: ')
        betalingskortnr=('Registrer betalingskort: ')
        kundefil.write(fornavn+('\n'))
        kundefil.write(etternavn+('\n'))
        kundefil.write(betalingskortnr+('\n'))

        print('Kundedata er registrert')

        kundefil.close()
#end registrer ny kunde


def registrer_ny_hund():
    search=input('Skriv inn kundens mobilnr: ')

    kundefil=open('kunde.txt','r')
    mobilnr=kundefil.readline()

    funnet=False

    while mobilnr!='':
        fornavn=kundefil.readline()
        etternavn=kundefil.readline()
        betalingskortnr=kundefil.readline()

        mobilnr=mobilnr.rstrip('\n')
        fornavn=fornavn.rstrip('\n')
        etternavn=etternavn.rstrip('\n')
        betalingskortnr=betalingskortnr.rstrip('\n')

        if mobilnr==search:
            funnet=True
    
    kundefil.close()
    if funnet==True:
        hundefil=open('hunder.txt','r')
        hundeID=hundefil.readline()
        funnet_hund=False
        while hundeID!='':
            hundenavn=hundefil.readline()
            rase=hundefil.readline()
            eiersMobilnr=hundefil.readline()
            startdato =hundefil.readline()
            eiersMobilnr=eiersMobilnr.rstrip('\n')
            if eiersMobilnr==search:
                funnet_hund=True
        
        hundefil.close()

        if funnet_hund==False:
            hundefil=open('hunder.txt','a')
            hundeID=input('Skriv inn hundeID: ')
            hundenavn=input('Skriv inn navnet på hunden: ')
            rase=input('Hvilken rase er hunden?: ')
            eiersMobilnr=search
            startdato=('Skriv inn dagens dato: ')

            hundefil.write(hundeID+('\n'))
            hundefil.write(hundenavn+('\n'))
            hundefil.write(rase+('\n'))
            hundefil.write(eiersMobilnr+('\n'))
            hundefil.write(startdato+('\n'))

            print('Hundens data er registrert')

            hundefil.close()
        else:
            print('Både eier og hund allerede funnet')
        
    else:
        print('Eier ikke funnet, vennligst registrer eier først.')
#slutt registrer_ny_hund()

def slett_kunde(): 
    search=input('Skriv inn mobilnr på kunden som skal slettes')
    hundefil=open('hunder.txt','r')
    hundeID=hundefil.readline()
    funnet_hund=False
    while hundeID!='':
        hundenavn=hundefil.readline()
        rase=hundefil.readline()
        eiersMobilnr=hundefil.readline()
        startdato =hundefil.readline()
        eiersMobilnr=eiersMobilnr.rstrip('\n')
        if eiersMobilnr==search:
            funnet_hund=True
    
    hundefil.close()
    if funnet_hund==True:
        print('Beklager, kan ikke slette da det er registrert en hund på denne kunden')
    else:
        kundefil=open('kunde.txt','r')
        tempfil=open('temp.txt','w')

        mobilnr=kundefil.readline()

        while mobilnr!='':
            fornavn=kundefil.readline()
            etternavn=kundefil.readline()
            betalingskortnr=kundefil.readline()
            mobilnr=mobilnr.rstrip('\n')

            if mobilnr!=search:
                mobilnr=mobilnr+('\n')
                tempfil.write(mobilnr)
                tempfil.write(fornavn)
                tempfil.write(etternavn)
                tempfil.write(betalingskortnr)
        
        kundefil.close()
        tempfil.close()

        os.remove('kunde.txt')
        os.rename('tempfil.txt','kunde.txt')

        print('Kunde slettet')
#slutt slette 






        