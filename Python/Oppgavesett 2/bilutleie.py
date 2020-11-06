alt1=750
alt2=300
alt3=150


for n in range(0,501,50):
    alt2=alt2+(2*n)
    alt3=alt3+(4*n)
    if alt1<alt2 and alt1<alt3:
        print("Fastpris på",alt1,"kr er best om du skal kjøre",n,"kilometer.")
    else: 
        if alt2<alt1 and alt2<alt3:
            print("Prismoddel 2, på",alt2,"kr er best om du skal kjøre",n,"kilometer.")
        else:
            print("Prismoddel 3, på",alt3,"kr er best om du skal kjøre",n,"kilometer.")

            