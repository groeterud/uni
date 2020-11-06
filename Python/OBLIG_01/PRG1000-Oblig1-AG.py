#while variabel
igjen='Ja'

#while loop
while igjen=="ja" or igjen=="Ja" or igjen=="JA":

    #input
    pris_bil=int(input("Vennligst skriv totalprisen på bilen du ønsker å kjøpe: "))
    egenkapital=int(input("Hvor mye egenkapital har du? "))
    nedbetalingstid=int(input("Over hvor mange år ønsker du å nedbetale lånet? "))

    #beregning av variabler som er nødvendige for if test
    egenkapital_pct=egenkapital/pris_bil*100

    #tilordning av sikkerhetsvariabl
    laanekalulasjon=False

    #sjekke om inputs er ok
    if nedbetalingstid<0:
        print("ERROR. Nedbetalingstid må være positivt tall over 0")
    else:
        if pris_bil<=0:
            print("ERROR. Om du får betalt for å kjøpe bilen, eller om den er gratis så har du ikke behov for lån.")
        else:
            if egenkapital<0:
                print("ERROR: Egenkapital kan ikke være negativ")
            else:
                if egenkapital>pris_bil:
                    print("Du har nok egenkapital til at du ikke behøver noe lån, dermed kan vi ikke tilby deg et.")
                else:
                    if egenkapital_pct<35:
                        print("Beklager, det foreligger krav om 35.00 prosent egenkapital og du har bare",format(egenkapital_pct,".2f"),"prosent egenkapital. Lånet kan dermed ikke innvilges")
                    else:
                        laanekalulasjon=True #bare kjøre lånekalkulasjon om input er ok
            
    #lånekalkulasjon dersom input er ok
    if laanekalulasjon==True:
        #definere rente gitt prosent egenkapital
        if egenkapital_pct<50:
            aarlig_rente=0.045
        else:
            if egenkapital_pct<60:
                aarlig_rente=0.03
            else:
                aarlig_rente=0.025

        #Beregne variabler som er avhengige av if løkkens utfall
        terminrente=aarlig_rente/12
        antall_terminer=nedbetalingstid*12
        laanebelop=pris_bil-egenkapital

        #Beregne terminbeløp
        terminbelop = laanebelop*((((1+terminrente)**antall_terminer)*terminrente)/(((1+terminrente)**antall_terminer)-1))

        print()
        print("Gratulerer, siden du har",format(egenkapital_pct,".2f"),"prosent egenkapital kan lånet innvilges")
        print("Dersom du takker ja til lånet vil terminbeløpet være:",format(terminbelop,".2f"),"kr")
        
    igjen=input('Ønsker du å kjøre Billånskalkulatoren igjen? Skriv "Ja" etterfulgt av enter: ')

#fin
print("Program avsluttet")