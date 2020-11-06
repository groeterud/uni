numlist=[]

while len(numlist)<5:
    inndata=int(input("Skriv inn tall:"))
    numlist.append(inndata)

numlist=sorted(numlist)
print("Det minste tallet er:",numlist[0])
