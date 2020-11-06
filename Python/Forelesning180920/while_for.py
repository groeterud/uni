#while er unødvendig her.
''' forsøk 1: while løkke
i=-5

i=int(input("Tast inn tall: "))

while i in range(1,37,2):
    if i>=1 and i<11:
        print("Tallet er rødt")
    else:
        if i>=11 and i<19:
            print("Tallet er sort")
        else:
            if i>=19 and i<29:
                print("Tallet er rødt")
            else:
                print("Tallet er sort") 

    i=-5

while i in range(2,37,2):
    if i>=1 and i<11:
        print("Tallet er sort")
    else:
        if i>=11 and i<19:
            print("Tallet er rødt")
        else:
            if i>=19 and i<29:
                print("Tallet er sort")
            else:
                print("Tallet er rødt")
    i=-5

if i==0:
    print("Tallet er grønt!")
    i=-5

'''

#forsøk 2: definere partall og odetall som range list i variabel
'''
tall=int(input("Skriv in tall: "))

sort_en=range(2,11,2)
sort_to=range(11,18,2)
sort_tre=range(20,29,2)
sort_fire=range(29,37,2)


if tall>=0 and tall<=36:
    if tall==0:
        print("Tallet er grønt")
    else:
        if (tall in sort_en) or (tall in sort_to) or (tall in sort_tre) or (tall in sort_fire):
            print("Tallet er sort")
        else:
            print("Tallet er rødt")

'''


#forsøk 3: While løkke
