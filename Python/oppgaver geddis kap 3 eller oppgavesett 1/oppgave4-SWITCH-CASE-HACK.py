i=int(input("Skriv inn heltal for å få returnert romertall: "))

def romertall(i):
    romertall_dict={
        1:'I',
        2:'II',
        3:'III',
        4:'IV',
        5:'V',
        6:'VI',
        7:'VII',
        8:'VIII',
        9:'IX',
        10:'X'
    }
    return romertall_dict.get(i,"tall utenfor biblioteksgrense")

print("Ditt tall i romertall er:",romertall(i))

