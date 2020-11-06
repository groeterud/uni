fortsette=True

while fortsette==True:
    manedslonn=int(input('Oppgi månedslønn i kr: '))

    if manedslonn<=20000:
        skatt=0.00
    else:
        if manedslonn<=35000:
            skatt=0.28
        else:
            if manedslonn<=50000:
                skatt=0.35
            else:
                if manedslonn<=70000:
                    skatt=0.42
                else:
                    skatt=0.48

    utbetalt=manedslonn*(1-skatt)
    print('Du får utbetalt',format(utbetalt,'.2f'),'kr per måned og skatteprosenten er',int(skatt*100),'%')

    svar=input('Skal du utføre flere lønnsberegninger (Ja/ja)? ')

    if svar=='Ja' or svar=='ja':
        fortsette=True
    else:
        fortsette=False