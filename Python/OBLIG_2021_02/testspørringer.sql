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
SELECT Studentnr,eksamensresultat.Emnekode,Dato,Karakter,Emnenavn,Studiepoeng
FROM eksamensresultat,Emne
WHERE eksamensresultat.Emnekode=emne.Emnekode 
AND Studentnr=%s 
ORDER BY eksamensresultat.Emnekode;


-- Vitnemål
SELECT Studentnr,eksamensresultat.Emnekode,Dato,MIN(Karakter) AS StandpunktKarakter,Emnenavn,Studiepoeng
FROM eksamensresultat,Emne
WHERE eksamensresultat.Emnekode=emne.Emnekode 
AND Studentnr=%s
GROUP BY eksamensresultat.Emnekode
ORDER BY eksamensresultat.Emnekode;