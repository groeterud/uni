#hvis bruttolønn er under 20k så er skattesatsen 28%
#hvis bruttolønn er 20k eller mer så er den 35%


#hent bruttolønn
brutto_lonn=int(input("Hva er din brutto lønn? "))

#tilordn konstante verdier til variabler.
trinn=[20000,30000]
skattesatser=[0.28,0.35,0.4]

#finn riktig skattesats
if brutto_lonn<trinn[0]:
    skattesats=skattesatser[0]
elif brutto_lonn<trinn[1]:
    skattesats=skattesatser[1]
else:
    skattesats=skattesatser[2]


#beregn skatt og nettolønn
skatteprosent=skattesats*100
skatt=brutto_lonn*skattesats
netto_lonn=brutto_lonn-skatt

#skriv ut lønnsberegningen
print("Din skatteprosent er:",round(skatteprosent,1),"%")
print("Du betaler kr:",format(skatt,".2f"),"i skatt")
print("Din netto lønn etter skatt er:",format(netto_lonn,".2f"),"kr")

