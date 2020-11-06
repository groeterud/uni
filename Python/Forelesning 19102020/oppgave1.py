tall1=int(input("Tall nr 1: "))
tall2=int(input("Tall nr 2: "))
tall3=int(input("Tall nr 3: "))
tall4=int(input("Tall nr 4: "))
tall5=int(input("Tall nr 5: "))


mylist=[tall1,tall2,tall3,tall4,tall5]

minste_tall=mylist[0]

tallnr=1

for index in range(1,len(mylist),1):
    if mylist[index]<minste_tall:
        #Da er det et nytt tall som er minstetall
        minste_tall=mylist[index]
        #tallnr i rekka er index +1  
        tallnr=index+1

print('Det minste tallet er:',minste_tall)
print('Det er tall nummer',tallnr,'i sekvensen')


