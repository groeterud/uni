pseudokode oppgave 1

definere igjen = ja

definere navneliste=[]

# while løkke
input fornavn 
nytt navn? 

end while
# 

print liste

# reversere lista
definere liste_reverse=[]

for index in range(len(navneliste),0,-1):
    liste_reverse.append(navneliste[index])

print liste_reverse

# verifikasjon reversjon
navneliste.reverse()

print navneliste
