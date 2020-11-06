i=int(input("Enter pocket number: "))

#er det partall?
if i%2==0:
    partall=True
else:
    partall=False

''' 
#main body
if i>=1 and i<=10:
    if partall:
        print("It's black")
    else:
        print("It's red")
else:
    if i>10 and i<=18:
        if partall:
            print("it's red")
        else:
            print("it's black")
    else:
        if i>18 and i<=28:
            if partall:
                print("it's black")
            else:
                print("it's red")
        else:
            if i>28 and i<=36:
                if partall:
                    print("it's red")
                else:
                    print("it's black")
            else:
                if i==0:
                    print("It's green!")
                else:
                    print("ERROR: INPUT OUTSIDE OF RANGE")
#end loop

'''
#med elif
if i>=1 and i<=10:
    if partall:
        print("It's black")
    else:
        print("It's red")
elif i>10 and i<=18:
    if partall:
        print("It's red")
    else:
        print("It's black")
elif i>18 and i<=28:
    if partall:
        print("it's black")
    else:
        print("it's red")
elif i>28 and i<=36:
    if partall:
        print("It's red")
    else:
        print("It's black")
elif i==0:
    print("It's green!")
else:
    print("ERROR: INPUT OUTSIDE OF RANGE")


