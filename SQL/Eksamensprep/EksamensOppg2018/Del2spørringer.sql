USE Bildeling;

--b 
SELECT *
FROM bil;


-- c
SELECT Etternavn, Fornavn, Mobilnr
FROM kunde
ORDER BY Etternavn;

-- d
SELECT *
FROM bil
WHERE Startdato > '20180501';

-- e
SELECT COUNT(*) AS AntallKunder
From kunde;

-- f
CREATE USER 'Bilsjef' IDENTIFIED BY 'pwd';

-- g -- posisjon kan være null dummy
CREATE VIEW LedigeBiler AS (
    SELECT bil.Regnr,Merke, Modell, Posisjon
    FROM bil 
    LEFT JOIN utleie on bil.Regnr=utleie.Regnr
    WHERE utleie.Regnr IS NULL
);

SELECT *
FROM LedigeBiler;

-- h
GRANT SELECT ON LedigeBiler TO 'Bilsjef';

-- i
INSERT INTO kunde (Fornavn,Etternavn,Mobilnr,Betalingskortnr) VALUES 
('Tore','Bilese','11111111','1111222233334444');
-- j 
INSERT INTO utleie VALUES ('AA11111','2021-05-08 16:57:00', 14500, '+4711111111', NULL, NULL, NULL);
-- k
SELECT kunde.*, COUNT(utleie.Mobilnr) AS AntallLeie
FROM kunde LEFT JOIN 
    utleie USING (Mobilnr)
GROUP BY kunde.Mobilnr;

--l
SELECT *
FROM kunde
    LEFT JOIN utleie USING (Mobilnr)
    WHERE utleie.Mobilnr IS NULL;

-- m
SELECT bil.Regnr, bil.Merke, bil.Modell, COUNT(utleie.Regnr) AS AntallLeie
FROM bil LEFT JOIN 
    utleie USING (Regnr)
GROUP BY bil.Regnr
HAVING AntallLeie>0
ORDER BY AntallLeie DESC;

SELECT COUNT(Regnr) AS AntallLeie, Regnr
FROM utleie
GROUP BY Regnr
HAVING AntallLeie>0
ORDER BY AntallLeie DESC;


-- n
SELECT kunde.Mobilnr, kunde.Fornavn, kunde.Etternavn, SUM(utleie.Belop) AS Beløp
FROM kunde INNER JOIN
    utleie USING (Mobilnr)
GROUP BY Mobilnr
ORDER BY Beløp DESC;

-- o
SELECT kunde.Etternavn, kunde.Mobilnr, bil.Regnr, bil.Startdato, utleie.Utlevert
FROM utleie
    JOIN kunde USING (Mobilnr)
    JOIN bil USING (Regnr)
WHERE Innlevert IS NULL;
-- Option 2
SELECT Etternavn,Kunde.Mobilnr,Bil.Regnr,Startdato,Utlevert
FROM Bil,Kunde,Utleie
WHERE Kunde.Mobilnr=Utleie.Mobilnr
AND Bil.Regnr=Utleie.Regnr
AND Innlevert IS NULL
GROUP BY Etternavn,Kunde.Mobilnr,Bil.Regnr,Startdato,Utlevert;
    

-- p
SELECT kunde.*, utleie.Regnr, utleie.Utlevert
FROM utleie
    JOIN kunde USING (Mobilnr)
WHERE 
    (TIMESTAMPDIFF(DAY,utleie.Utlevert,CURRENT_TIMESTAMP)>=3) AND Innlevert IS NULL;

-- Niklas
SELECT *
FROM kunde 
    JOIN utleie USING (Mobilnr)
WHERE TIMESTAMPDIFF(HOUR,Utlevert,Innlevert)>72;

    
-- q
SELECT MOD(KmInn,15000) AS KmTilService, utleie.Regnr
FROM utleie INNER JOIN (
    SELECT Regnr, MAX(Innlevert) AS MaxDate
    FROM utleie
    GROUP BY Regnr
) AS DatoMax
ON utleie.Regnr=DatoMax.Regnr AND utleie.Innlevert=DatoMax.MaxDate;


SELECT Regnr, KmInn,
CASE
    WHEN (MOD(KmInn,15000)<1001) THEN 'Snart Service'
    ELSE 'Ikke servicebehov enda'
END AS ServiceBehovStatus
FROM Utleie
GROUP BY Regnr, KmInn,'ServiceBehovStatus';


SELECT Regnr, KmInn,
CASE
WHEN (MAX(KmInn)>=14000 AND MAX(KmInn)<15000) THEN 'Snart 15.000km service'
WHEN (MAX(KmInn)>=29000 AND MAX(KmInn)<30000) THEN 'Snart 30.000km service'
WHEN (MAX(KmInn)>=44000 AND MAX(KmInn)<45000) THEN 'Snart 45.000km service'
WHEN (MAX(KmInn)>=59000 AND MAX(KmInn)<60000) THEN 'Snart 60.000km service'
WHEN (MAX(KmInn)>=74000 AND MAX(KmInn)<75000) THEN 'Snart 75.000km service'
WHEN (MAX(KmInn)>=89000 AND MAX(KmInn)<90000) THEN 'Snart 90.000km service'
ELSE 'Ikke servicebehov enda'
END AS ServiceBehovStatus
FROM Utleie
GROUP BY Regnr, KmInn,'ServiceBehovStatus';