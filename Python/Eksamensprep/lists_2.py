myList=[8746,12744,5478,21144,221,57788,12835,4587,2668,223,3547,45884,11147,5475]
print('myList used to be:',myList)
sorted_list_asc=[]

storste_tall=1

for x in range(0,len(myList),1):
    if myList[x]>storste_tall:
        storste_tall=myList[x]

#while there is data in unsorted list
while myList:
    minste_tall=storste_tall

    for x in range(0,len(myList),1):
        #if current value in X is smaller than minste_tall
        if myList[x]<minste_tall:
            #overwrite the value of minste_tall with the current value of unsorted list in X index. 
            minste_tall=myList[x]

    #adding the smallest number to the sorted list
    sorted_list_asc+=[minste_tall]
    
    #deleting the smallest number from the unsorted list. 
    myList.remove(minste_tall)



myList=sorted_list_asc

print('myList is now sorted:',myList)

