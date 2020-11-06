#program for å summere 5 tall
antall_tall=int(input("Hvor mange tall skal du summere? "))
summen_er=0


for n in range(1,antall_tall+1,1):
    print("tall nr:",n)
    tall=int(input("Oppgi tall: "))
    summen_er += tall

print("Summen av de",antall_tall,"tallene er:",summen_er)

