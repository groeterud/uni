tall1=int(input("Skriv inn tall nummer en:"))
tall2=int(input("Skriv inn tall nummer to:"))
tall3=int(input("Skriv inn tall nummer tre:"))
tall4=int(input("Skriv inn tall nummer fire:"))
tall5=int(input("Skriv inn tall nummer fem:"))


#5head
"""
tall_liste=(tall1,tall2,tall3,tall4,tall5)

tall_liste_sorted=sorted(tall_liste)

minste_tall=tall_liste_sorted[0]

index=tall_liste.index(minste_tall)

sekvens=index+1

print("Det minste tallet ditt er:",minste_tall)
print("Det minste tallet du skrev ble tastet inn som tall nummer:",sekvens)
"""
#sikrer at minste_tall er predefinert som en variabel som garantert er større enn det minste tallet uansett størelsesorden
minste_tall=tall1*tall2*tall3*tall4*tall5

#kjedelig
if tall1<tall2:
    minste_tall=tall1
    tall_sekvens=1

if tall3<minste_tall:
    minste_tall=tall3
    tall_sekvens=3

if tall4<minste_tall:
    minste_tall=tall4
    tall_sekvens=4

if tall5<minste_tall:
    minste_tall=tall5
    tall_sekvens=5

if tall2<minste_tall:
    minste_tall=tall2
    tall_sekvens=2

print("Det minste tallet er:",minste_tall)
print("Og det er tall nummer:",tall_sekvens,"i rekken")