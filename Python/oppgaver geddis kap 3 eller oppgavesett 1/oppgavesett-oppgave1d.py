#deklarerer variabler
baneleie=2500

#input
antall_deltakere=int(input("Hvor mange skal spille paintball?: "))

#Beregn prisstrategi_gammel
if antall_deltakere>=20:
    deltakertillegg=350
else:
    if antall_deltakere>=10:
        deltakertillegg=380
    else:
        deltakertillegg=420

#beregn summen
prisstrategi_gammel=baneleie+(antall_deltakere*deltakertillegg)


#verifisering
#print("prisstrategi_gammel",prisstrategi_gammel)
#print("deltakertillegg gammel",deltakertillegg)
#print("baneleie gammel",baneleie)

#beregn prisstrategi ny
if antall_deltakere>30:
    print("error, for mange deltakere")
else:
    if antall_deltakere>=20:
        baneleie=1000
        deltakertillegg=450
    else:
        if antall_deltakere>=10: 
            baneleie=2000
            deltakertillegg=400
        else:
            if antall_deltakere>=1:
                baneleie=3500
                deltakertillegg=350
            else:
                print("Error, ikke nok deltakere")

prisstrategi_ny=baneleie+(antall_deltakere*deltakertillegg) 

#verifikasjon
#print("prisstrategi_ny",prisstrategi_ny)
#print("deltakertillegg ny",deltakertillegg)
#print("baneleie ny",baneleie)

#finn delta
prisstrategi_delta=prisstrategi_ny-prisstrategi_gammel
prisstrategi_delta_motsatt=prisstrategi_gammel-prisstrategi_ny

print("Pris etter gammel strategi:",prisstrategi_gammel)
print("Pris etter ny strategi",prisstrategi_ny)

#finn vinner
if prisstrategi_delta>0:
    print("Den nye strategien var best, og du tjente ville tjent:",prisstrategi_delta,"på valg av strategi")
else:
    if prisstrategi_delta<0:
        print("Den gamle strategien var bedre, og du ville tjent kr:",prisstrategi_delta_motsatt,"på valg av strategi")
    else:
        print("begge strategiene var like gode")


