l1=[1,14,26,37,100,86,77]
l2=[2,13,27,38,99,85,78]
nyliste=[]

print(l1)
print(l2)
print(nyliste)
print()


#your job: combine the 2 lists
#The values are to be added with the smalles value first according to the index of x in both lists.
#assume both lists are of the same length.

for x in range (0,len(l1),1):
    if l1[x]<=l2[x]:
        nyliste+=[l1[x]]
        nyliste+=[l2[x]]
    else:
        nyliste+=[l2[x]]
        nyliste+=[l1[x]]

#nyliste.sort()
print(nyliste)
