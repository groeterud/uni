
i=int(input("Skriv inn heltal: "))


#finn ut om tallet er positivt, negativt eller null.
if i<0:
    print("tallet er negativt")
else:
    if i==0:
        print("tallet er null")
    else:
        print("tallet er positivt")

#sjekk om tallet er delelig på 2 uten noen rest
if i%2==0:
    print(i,"er ett partall")
else:
    print(i,"er ett oddetall")

