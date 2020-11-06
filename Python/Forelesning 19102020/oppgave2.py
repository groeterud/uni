#første og siste element i en liste skal bytte plass
talliste=[5,3,2,1,4]
print('lista før bytte er:', talliste)
print('første og siste element i lista skal bytte plas')
print()


#bytte er byttevariabelen vi bruker for å ta vare på første verdi
bytte=talliste[0]

#talliste av 0 får verdien til talliste av 4
talliste[0]=talliste[4]

#talliste av 4 får verdien av byttevariabelen
talliste[4]=bytte

print('listen er nå:',talliste)

talliste_sorted=[]

while talliste:
    storst=talliste[0]
    for x in talliste:
        if x > storst:
            storst=x
    talliste_sorted.append(storst)
    talliste.remove(storst)

print('sortert talliste:',talliste_sorted)