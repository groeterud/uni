poengsum=int(input("Les inn poengsum: "))
'''
if poengsum >= 92:
    karakter="A"
else:
    if poengsum >= 77:
        karakter="B"
    else:
        if poengsum >= 58:
            karakter="C"
        else:
            if poengsum >= 46:
                karakter="D"
            else:
                if poengsum >= 40:
                    karakter="E"
                else: 
                    karakter="F"
'''

if poengsum >= 92:
    karakter="A"
elif poengsum >= 77:
    karakter="B"
elif poengsum >= 58:
    karakter="C"
elif poengsum >= 46:
    karakter="D"
elif poengsum >= 40:
    karakter="E"
else:
    karakter="F"

print("Karakteren til inidividet er:",karakter)