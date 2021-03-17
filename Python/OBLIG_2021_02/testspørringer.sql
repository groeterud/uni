USE oblig2021;
SELECT * FROM eksamen WHERE Dato<=CURRENT_DATE() ORDER BY Dato DESC;

SELECT COUNT(eksamensresultat.Karakter) AS Antall
FROM eksamensresultat;

SELECT Emnekode, Dato, Romnr, COUNT(*) AS Antall
FROM eksamen JOIN 
    eksamensresultat USING (Emnekode,Dato)
WHERE eksamen.Dato<=CURRENT_DATE()
GROUP BY eksamen.Emnekode,eksamen.Dato
HAVING Antall>0
ORDER BY eksamen.Dato DESC;
WHERE eksamen.Dato<=CURRENT_DATE() 
ORDER BY eksamen.Dato DESC;



SELECT *
FROM eksamensresultat
WHERE Emnekode='DFIATMC1' AND Dato='20200525';

SELECT Emnenavn
FROM emne
WHERE Emnekode='DFIATMC1';


-- Selekter alle eksamensnummer
SELECT Emnekode FROM emne;

-- qry for å selektere alle eksamensresultater fra 1 spesifikt emne 
SELECT Studentnr,Karakter,Dato AS Eksamensdato
FROM eksamensresultat
WHERE Emnekode=%s
ORDER BY Studentnr;


-- Karakterutskrift:
SELECT eksamensresultat.Dato,eksamensresultat.Emnekode,Emnenavn,Karakter,Studiepoeng
FROM eksamensresultat,Emne
WHERE eksamensresultat.Emnekode=emne.Emnekode 
AND Studentnr=%s 
ORDER BY eksamensresultat.Dato;


-- Vitnemål
SELECT eksamensresultat.Emnekode,Emnenavn,MIN(Karakter) AS StandpunktKarakter,Studiepoeng
FROM eksamensresultat,Emne
WHERE eksamensresultat.Emnekode=emne.Emnekode 
AND Studentnr='000001'
GROUP BY eksamensresultat.Emnekode
ORDER BY eksamensresultat.Emnekode;


-- eksamener i en bestemt period

-- eksamener på en bestemt dag 
SELECT *
FROM eksamen
WHERE Dato>=%s AND Dato<=%s;

--1
SELECT *
FROM eksamen
WHERE Dato=%s