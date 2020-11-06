month=int(input("Please the the month as represented by it's number on a calendar: "))

first=False
second=False
third=False
fourth=False

if month==1:
    first=True
else:
    if month==2:
        first=True
    else:
        if month==3:
            first=True
        else:
            if month==4:
                second=True
            else:
                if month==5:
                    second=True
                else:
                    if month==6:
                        second=True
                    else:
                        if month==7:
                            third=True
                        else:
                            if month==8:
                                third=True
                            else:
                                if month==9:
                                    third=True
                                else:
                                    if month==10:
                                        fourth=True
                                    else:
                                        if month==11:
                                            fourth=True
                                        else:
                                            if month==12:
                                                fourth=True
                                            else:
                                                print("ERROR: INVALID INPUT")

if first:
    print("the month with the number:",month,"is in the first quarter of the year")
else:
    if second:
        print("the month with the number:",month,"is in the second quarter of the year")
    else:
        if third:
            print("the month with the number:",month,"is in the third quarter of the year")
        else:
            if fourth:
                print("the month with the number:",month,"is in the fourth quarter of the year")
