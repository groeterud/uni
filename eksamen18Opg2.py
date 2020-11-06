l1=[1,14,26,37,100,86,77]
l2=[2,13,27,38,9,85,78]
nyliste=[]

print(l1)
print(l2)
print(nyliste)
print()

for x in range (0,len(l1),1):
    if l1[x]<=l2[x]:
        nyliste+=[l1[x]]
        nyliste+=[l2[x]]
    else:
        nyliste+=[l2[x]]
        nyliste+=[l1[x]]

print(nyliste)