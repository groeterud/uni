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

-- n
SELECT kunde.Mobilnr, Fornavn, Etternavn, SUM(utleie.Belop) AS TotalSum
FROM kunde
    JOIN hund ON kunde.Mobilnr=hund.Eier
    JOIN utleie USING (HundeID)
        WHERE utleie.Belop IS NOT NULL
GROUP BY HundeID
ORDER BY TotalSum DESC;



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
