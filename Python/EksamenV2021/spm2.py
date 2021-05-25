from tkinter import *
import mysql.connector

db=mysql.connector.connect(host='localhost',port=3306,user='Dekksjef',passwd='eksamen2021',db='Dekkhotell')

def vis_info(evt):
    valgt=lbox.get(lbox.curselection())
    #valgt[0] fordi 2 dimensjonal liste
    regnr=valgt[0]

    #finner hylleplassering
    hylle_markor=db.cursor()
    hylle_markor.execute('''
    SELECT Mobilnr, Hylle
    FROM Oppbevaring
    WHERE Regnr=%s AND Utlevert IS NULL
    ''',(regnr,))
    for row in hylle_markor:
        mobilnr=row[0]
        hylle=row[1]
    hylle_markor.close()

    #finn eier info:
    eier_markor=db.cursor()
    eier_markor.execute('''
    SELECT Fornavn,Etternavn,epost
    FROM Kunde
    WHERE Mobilnr=%s
    ''',(mobilnr,))
    for row in eier_markor:
        fornavn=row[0]
        etternavn=row[1]
        epost=row[2]
    eier_markor.close()


    #visninger
    fornavn_lbl['text']=fornavn
    etternavn_lbl['text']=etternavn
    epost_lbl['text']=epost
    hylle_lbl['text']=hylle
 

aapne_oppbevaringer=[]

aapen_markor=db.cursor()

aapen_markor.execute('''
SELECT Regnr, Innlevert
FROM Oppbevaring
WHERE Utlevert IS NULL
ORDER BY Innlevert 
''')
for row in aapen_markor:
    aapne_oppbevaringer+=[row]


## UI 
window=Tk()
window.title('Oversikt over åpne oppbevaringer')

lb_lf=LabelFrame(window)
lb_lf.grid(row=0,column=0,padx=5,pady=5)

visning_lf=LabelFrame(window,text='Informasjon')
visning_lf.grid(row=0,column=1,padx=5,pady=5,sticky=N)

btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
btn_avslutt.grid(row=1,column=1,padx=5,pady=(20,5),sticky=SE)

## lb_lf innhold
y_scroll=Scrollbar(lb_lf,orient=VERTICAL)
y_scroll.grid(row=0,column=1,rowspan=5,padx=(0,20),pady=5,sticky=NS)

innhold_lbox=StringVar()
lbox=Listbox(lb_lf,width=50, height=5, listvariable=innhold_lbox,yscrollcommand=y_scroll.set)
lbox.grid(column=0,row=0,padx=5,pady=5)
innhold_lbox.set(aapne_oppbevaringer)
lbox.bind("<<ListboxSelect>>",vis_info)
y_scroll["command"]=lbox.yview

## visning_lf innhold
fornavn_lbl=Label(visning_lf,text='Fornavn')
fornavn_lbl.grid(row=0,column=0,padx=5,pady=5,sticky=W)

etternavn_lbl=Label(visning_lf,text='Etternavn')
etternavn_lbl.grid(row=0,column=1,padx=5,pady=5,sticky=W)

epost_lbl=Label(visning_lf,text='Epost')
epost_lbl.grid(row=1,column=0,padx=5,pady=5,sticky=W)

hylle_lbl=Label(visning_lf,text='Hylle')
hylle_lbl.grid(row=1,column=1,padx=5,pady=5,sticky=W)

window.mainloop()