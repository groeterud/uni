def les_print_read():
    print('les_print_read()')
    tekstFil=open('Tall.txt')
    output=tekstFil.read()
    tekstFil.close()
    print(output)


def les_linje_print():
    print('les_linje_print()')
    tekstFil=open('Tall.txt')
    output=tekstFil.readline()
    while output!='':
        output=output.rstrip('\n')
        print(output)
        output=tekstFil.readline()
    tekstFil.close()
  

def les_post_print():
    print('les_post_print()')
    tekstFil=open('Tall.txt')
    output=tekstFil.readline()
    while output!='':
        output=output.rstrip('\n')
        verdi=tekstFil.readline()
        verdi=verdi.rstrip('\n')
        print(output)
        print(verdi)
        output=tekstFil.readline()
    tekstFil.close()


def les_post_summer():
    print('les_post_summer()')
    tekstFil=open('Tall.txt')
    output=tekstFil.readline()
    sum=0
    while output!='':
        output=output.rstrip('\n')
        verdi=tekstFil.readline()
        verdi=int(verdi.rstrip('\n'))
        sum=sum+verdi    
        print(output)
        print(verdi)
        output=tekstFil.readline()
    tekstFil.close()
    print('summen er',sum)

def les_post_avg():
    print('les_post_avg()')
    tekstFil=open('Tall.txt')
    output=tekstFil.readline()
    sum=0
    i=0
    while output!='':
        output=output.rstrip('\n')
        verdi=tekstFil.readline()
        verdi=int(verdi.rstrip('\n'))
        sum=sum+verdi    
        i+=1
        print(output)
        print(verdi)
        output=tekstFil.readline()
    tekstFil.close()
    avg=sum//i
    print('gjennomsnittet er',avg)

def les_post_storst():
    print('les_post_storst()')
    tekstFil=open('Tall.txt')
    output=tekstFil.readline()
    storst=0
    while output!='':
        output=output.rstrip('\n')
        verdi=tekstFil.readline()
        verdi=int(verdi.rstrip('\n'))
        print(output)
        print(verdi)
        output=tekstFil.readline()
        if verdi > storst:
            storst=verdi
    tekstFil.close()
    print('det største tallet er:',storst)

def main():
    again=True
    while again==True:
        print('----------------------------------------------------------------------------------')
        print('Meny')
        print('Valg 1 - lese hele fila med read-metoden og skrive ut innholdet')
        print('Valg 2 - lese hele fila linje for linje med for-løkke og skrive ut innholdet')
        print('Valg 3 - lese hele fila "post for post" og skrive ut innholdet og skrive ut innholdet')
        print('Valg 4 - lese hele fila "post for post" og skrive ut innholdet og summere tallene')
        print('Valg 5 - lese hele fila "post for post" og skrive ut innholdet og beregne gjennomsnittet av tallene')
        print('Valg 6 - lese hele fila "post for post" og skrive ut innholdet og finne største tall')
        print('Valg 9 - Avslutt program')
        print('----------------------------------------------------------------------------------')
        question=int(input('Vennligst velg program: '))
        if question==1:
            les_print_read()
        else:
            if question==2:
                les_linje_print()
            else:
                if question==3:
                    les_post_print()
                else:
                    if question==4:
                        les_post_summer()
                    else:
                        if question==5:
                            les_post_avg()
                        else:
                            if question==6:
                                les_post_storst()
                            else:
                                if question==9:
                                    again==False
                                    print('skal være false nå da din balle')
                                else:
                                    print('ugyldig input')
  

main()
print('Program Avsluttet')