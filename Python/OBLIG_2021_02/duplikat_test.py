import mysql.connector

eksamensdatabase=mysql.connector.connect(host='localhost',port=3306,user='Eksamenssjef',passwd='oblig2021',db='oblig2021')
romnr='0012'
dato='20210618'


duplikat=False
#henter på nytt i tilfelle databasen har blitt oppdatert siden tidligere. 
duplikat_markor=eksamensdatabase.cursor()
duplikat_markor.execute("SELECT * FROM eksamen WHERE Dato>CURRENT_DATE() ORDER BY Dato ASC")

#hiver det inn i en tom liste
dup_post_list=[]
for row in duplikat_markor:
    dup_post_list+=[row]


#gjør duplikatsjekken vår
for x in range(len(dup_post_list)):
    datofix=str(dup_post_list[x][1])
    datofix=datofix.replace('-','')
    if romnr==dup_post_list[x][2] and dato==datofix:
        duplikat=True

duplikat_markor.close()

print(duplikat)