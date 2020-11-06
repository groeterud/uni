"""
6+3*5=15+6=21 ok
12/4-4=3-4=-1 ok 
9+14*2-6=9+28-6=28+3=31 ok
(6+2)*3=8*3=24      ok
14/(11-4)=14/7=2  ok
9+12*(8-3)=9+12*5=60+9=69
"""

a=6+3*5
b=12/4-4
c=9+14*2-6
d=14/(11-4)
e=9+12*(8-3)

print("Svaret på a) er:",a)
print("Svaret på b) er:",b)
print("Svaret på c) er:",c)
print("Svaret på d) er:",d)
print("svaret på e) er:",e)


#formatering av desimaltall
pris_pr_kilo=10.37
antall_kilo=9.6
pris_total=antall_kilo*pris_pr_kilo

print("Prisen er:",format(pris_total,".2f"))
print("Prisen er:",round(pris_total,2))
print("er den avrunda??",pris_total)


dobbel_total=2*pris_total
print("Dobbel av totalpris er:",dobbel_total)



