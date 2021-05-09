USE dogstore;
-- b
SELECT *
FROM hund;
-- c
SELECT Etternavn, Fornavn, Mobilnr
FROM kunde
ORDER BY Etternavn;
-- d
SELECT *
FROM hund
WHERE Startdato>'20180101';

-- e
SELECT COUNT(*) AS Antall
FROM hund;

-- f
SELECT COUNT(utleie.HundeID) AS AntallUtleie, kunde.*
FROM Kunde
    LEFT JOIN hund ON kunde.Mobilnr=hund.Eier
    LEFT JOIN utleie USING (HundeID)
GROUP BY kunde.Mobilnr;

-- g
SELECT COUNT(utleie.HundeID) AS AntallUtleie, kunde.*
FROM Kunde
    LEFT JOIN hund ON kunde.Mobilnr=hund.Eier
    LEFT JOIN utleie USING (HundeID)
GROUP BY kunde.Mobilnr
HAVING AntallUtleie=0;

-- h 
SELECT COUNT(utleie.BoksID) AS AntallUtleie, boks.BoksID
FROM boks
    LEFT JOIN utleie USING (BoksID)
GROUP BY boks.BoksID
HAVING ANtallUtleie=0;
-- h alt 2
SELECT *
FROM Boks
WHERE BoksID NOT IN (
    SELECT BoksID
    FROM utleie
);

SELECT BoksID,SenterID
FROM Boks
WHERE BoksID NOT IN (SELECT BoksID FROM Utleie)
ORDER BY BoksID;

-- i
INSERT INTO kunde (Fornavn,Etternavn,Mobilnr,Betalingskortnr) VALUES
('Tore','Hundemann','+4711111111','1111222233334444');

-- j
CREATE VIEW LedigeBokser AS(
    SELECT *
    FROM boks
        WHERE BoksID NOT IN (
            SELECT BoksID
            FROM utleie
            WHERE Sluttidspkt IS NULL
        )
);
-- alt 2, noen begrensninger
SELECT *
FROM senter
INNER JOIN boks USING (SenterID)
INNER JOIN utleie USING (BoksID)
WHERE Sluttidspkt IS NOT NULL;

SELECT * FROM ledigebokser;
Select * from utleie;
-- k 
CREATE USER 'Hundesjef' IDENTIFIED BY 'pwd';

-- l
GRANT SELECT ON LedigeBokser TO 'Hundesjef';

-- m
SELECT COUNT(utleie.BoksID) AS AntallUtleie, boks.BoksID, senter.Senternavn
FROM boks
    JOIN utleie USING (BoksID)
    JOIN senter USING (SenterID)
GROUP BY boks.BoksID
HAVING ANtallUtleie>0
ORDER BY AntallUtleie DESC;

-- alt 2 
SELECT Boks.BoksID,Senternavn,COUNT(Starttidspkt) AS AntallUtleier
FROM Boks,Utleie,Senter
WHERE Boks.BoksID=Utleie.BoksID
AND Senter.SenterID=Boks.SenterID
GROUP BY Boks.BoksID
HAVING AntallUtleier>=0
ORDER BY AntallUtleier DESC;

-- alt 3
SELECT Boks.BoksID,Senter.Senternavn, COUNT(Starttidspkt) AS AntallUtleid
FROM Senter JOIN Boks
USING (SenterID)
JOIN Utleie
USING (BoksID)
GROUP BY Utleie.BoksID
HAVING AntallUtleid>0
ORDER BY AntallUtleid DESC;

-- n
SELECT kunde.Mobilnr, Fornavn, Etternavn, SUM(utleie.Belop) AS TotalSum
FROM kunde
    JOIN hund ON kunde.Mobilnr=hund.Eier
    JOIN utleie USING (HundeID)
        WHERE utleie.Belop IS NOT NULL
GROUP BY HundeID
ORDER BY TotalSum DESC;

-- alt 2
SELECT Kunde.Mobilnr,Fornavn,Etternavn, SUM(Utleie.Belop) AS Totalbelop
FROM Utleie JOIN Hund
USING (HundeID)
INNER JOIN Kunde
ON Hund.Eier=Kunde.Mobilnr
GROUP BY Kunde.Mobilnr
ORDER BY Totalbelop DESC;

-- alt 3
SELECT Kunde.Mobilnr,Fornavn,Etternavn,SUM(Belop) AS Totalbeløp
FROM Kunde,Utleie,Hund
WHERE Kunde.Mobilnr=Hund.Eier
AND Hund.HundeID=Utleie.HundeID
GROUP BY Kunde.Mobilnr
ORDER BY Totalbeløp DESC;

-- o
SELECT COUNT(boks.BoksID) AS AntallLedige, senter.SenterID, senter.Senternavn
FROM boks
    JOIN senter USING (SenterID)
WHERE BoksID NOT IN (
    SELECT BoksID
    FROM utleie
    WHERE Sluttidspkt IS NULL
)
GROUP BY SenterID;

-- p 
SELECT kunde.Mobilnr, Etternavn, utleie.BoksID, senter.Senternavn, utleie.Starttidspkt
FROM utleie
    JOIN boks USING (BoksID)
    JOIN senter USING (SenterID)
    JOIN hund USING (HundeID)
    JOIN kunde ON kunde.Mobilnr=hund.Eier
WHERE utleie.Sluttidspkt IS NULL;

-- q
SELECT utleie.HundeID, hund.Hundenavn, Etternavn, kunde.Mobilnr, utleie.BoksID, senter.Senternavn, utleie.Starttidspkt
FROM utleie
    JOIN hund USING (HundeID)
    JOIN boks USING (BoksID)
    JOIN senter USING (SenterID)
    JOIN kunde ON kunde.Mobilnr=hund.Eier
WHERE TIMESTAMPDIFF(HOUR,utleie.Starttidspkt,CURRENT_TIMESTAMP)>=3 AND Sluttidspkt IS NULL;
