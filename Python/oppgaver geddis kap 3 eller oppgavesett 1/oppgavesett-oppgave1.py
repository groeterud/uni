#deklarerer variabler
baneleie=2500

#input
antall_deltakere=int(input("Hvor mange skal spille paintball?: "))

if antall_deltakere>=20:
    deltakertillegg=350
else:
    if antall_deltakere>=10:
        deltakertillegg=380
    else:
        deltakertillegg=420

#beregn summen
pris=baneleie+(antall_deltakere*antall_deltakere)
print("Pris for spill er kroner:",format(pris,".2f"))

print("deltakertillegg",deltakertillegg)