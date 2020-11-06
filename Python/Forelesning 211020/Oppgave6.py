

def drommebolig():
    print('Velkommen til kalkulatoren: Drømmebolig')


def lanebevis():
    print('Velkommen til kalkulatoren: Lånebevis')

def main():
    fortsette=True

    while fortsette==True:
        selector=int(input('Hvilken kalkulator ønsker du å bruke? Skriv "1" for Drømmebolig og "2" for Lånebevis: '))

        if selector==1:
            drommebolig()
        else:
            lanebevis()

        fortsette=input('Ønsker du å bruke en av kalkulatorene på nytt?: ')
        if fortsette=='ja' or fortsette=='Ja' or fortsette=='JA':
            fortsette=True
        else:
            fortsette=False

main()
print('Program slutt')
