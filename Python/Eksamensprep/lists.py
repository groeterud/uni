myList=[]

listefil=open('list.txt','r')
nummer=listefil.readline()
while nummer!='':
    nummer=nummer.rstrip('\n')
    nummer=float(nummer)
    
    myList+=[nummer]
    
    nummer=listefil.readline()
listefil.close()

print(myList)

stOrste_tall=1

for x in range(0,len(myList),1):
    if myList[x]>stOrste_tall:
        stOrste_tall=myList[x]

print(stOrste_tall)

nyListe=[]

while myList:
    minste_tall=stOrste_tall
    for x in range(0,len(myList),1):
        if myList[x]<minste_tall:
            minste_tall=myList[x]
    nyListe+=[minste_tall]
    myList.remove(minste_tall)

print(nyListe)


