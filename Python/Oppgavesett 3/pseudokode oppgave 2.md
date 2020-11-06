igjen=ja

studentliste=[]

# while loop
while loop
input studentnr
studentliste+=[studentnr]
input fornavn
studentliste+=[fornavn]
input studium
studentliste+=[studium]
igjen input "skal det leses inn en ny student? 'skriv ja': "
# slutt while 


input: oppgi studentnr

if input in studentliste:
    for index in range studentliste[0,len(studentliste),3]
        print: studentliste[index]
        print: studentliste[index+1]
        print: studentliste[index+2]
else:
    print('Ingen student med det studentnummeret')

input: oppgi studie

if studie in studentliste:
    for index in range studentliste[2,len(studentliste)+1,3]:
        print: studentliste[index-2]
        print: studentliste[index-1]
        print: studentliste[index]


        
