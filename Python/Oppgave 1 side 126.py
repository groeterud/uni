numSeq = [12, 15, 5, 2 ,1 ,3, 8]

# Metode 1: Bruk sorted og tabellindexer for å gi svaret

numSeqSortedAsc = sorted(numSeq)
numSeqSortedDec = sorted(numSeq, reverse=True)
numSeqSum = sum(numSeq)

print("Number sequence is:", numSeq)
print("Number sequence sorted is:", numSeqSortedDec)
print("The biggest number in the sequence is:", numSeqSortedDec[0])
print("The smallest number is", numSeqSortedAsc[0])
print("The sum of the numbers is:",numSeqSum)

# Metode 2: Bruk min og max for å returnere tallene. 

numSeq_min = min(numSeq)
numSeq_max = max(numSeq)
print("Keep it simple, smallest value is:", numSeq_min)
print("Keep it simple, big number value is:", numSeq_max)

# Metode 3: While løkke for å overskrive numseq med en sortrert liste. 

numSeq_sorted_list = []

while numSeq:
    minimum = numSeq[0]
    for x in numSeq:
        if x < minimum:
            minimum = x
    numSeq_sorted_list.append(minimum)
    numSeq.remove(minimum)

del numSeq    
print("numSeq sorted:", numSeq_sorted_list)


#manuell algoritme for summering
listsum=0
for x in numSeq_sorted_list:
    listsum=listsum+x
    print(listsum)

print("sum is:",listsum)