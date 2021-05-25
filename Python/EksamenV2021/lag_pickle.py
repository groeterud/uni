import mysql.connector
import pickle

db=mysql.connector.connect(host='localhost',port=3306,user='Dekksjef',passwd='eksamen2021',db='Dekkhotell')
class Kunde:
    def __init__(self,mobilnr,fornavn,etternavn,epost):
        self.__mobilnr=mobilnr
        self.__fornavn=fornavn
        self.__etteravn=etternavn
        self.__epost=epost
    
    def set_mobilnr(self,mobilnr):
        self.__mobilnr=mobilnr
    
    def set_fornavn(self,fornavn):
        self.__fornavn=fornavn

    def set_etternavn(self,etternavn):
        self.__etteravn=etternavn
    
    def set_epost(self,epost):
        self.__epost=epost
    
    def get_mobilnr(self):
        return self.__mobilnr
    
    def get_fornavn(self):
        return self.__fornavn
    
    def get_etternavn(self):
        return self.__etteravn

    def get_epost(self):
        return self.__epost



FILENAME_PICK='Kunde.dat'


def main():
    #hent alle kunder
    kunde_markor=db.cursor()
    kunde_markor.execute('''
    SELECT *
    FROM Kunde
    ''')
    kunder=[]

    for row in kunde_markor:
        kunde=Kunde(mobilnr=row[0],fornavn=row[1],etternavn=row[2],epost=row[3])
        print (kunde.get_etternavn())
        kunder+=[kunde]

    kunde_markor.close()

    output_file=open(FILENAME_PICK,'wb')
    
    for x in range(len(kunder)):
        pickle.dump(kunder[x],output_file)
        print('DUMPED:\t',kunder[x])
    
    output_file.close()
    print('Alle hunder lagret i ',FILENAME_PICK)

main()