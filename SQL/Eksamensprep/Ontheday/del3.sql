USE Bildedeling;

-- f
SELECT COUNT(Fotograf) AS AntallBilder, BrukerID
FROM bilde
   RIGHT JOIN bruker ON bilde.Fotograf=bruker.BrukerID
GROUP BY Fotograf;

-- g
SELECT *
FROM bruker
WHERE BrukerID NOT IN (
    SELECT fotograf
    FROM bilde
);

--h
SELECT *
FROM bilde
WHERE BildeID NOT IN (
    SELECT BildeID
    FROM kommentar
);

--i
SELECT *
FROM bruker
WHERE BrukerID IN (
    SELECT BrukerID
    FROM likes
    WHERE BildeID='pic100'
);

--j
SELECT COUNT(likes.BildeID) AS AntallLikes, bilde.BildeID
FROM likes
    RIGHT JOIN bilde USING (BildeID)
GROUP BY bilde.BildeID;

--k
SELECT *
FROM kommentar
WHERE BildeID='pic100';

--l
SELECT *
FROM emneknagg
WHERE Emneknaggen LIKE '%Molde%';

--m
SELECT *
FROM bilde
WHERE BildeID IN(
    SELECT BildeID
    FROM tagforbilde
    WHERE EmneknaggID IN (
        SELECT EmneknaggID
        FROM emneknagg
        WHERE Emneknaggen LIKE '%VakreMolde'
    )
);

-- n
SELECT BrukerID, Fornavn, Etternavn, Kommentaren
FROM bruker
    JOIN kommentar USING (BrukerID)
WHERE kommentar.BildeID IN(
    SELECT BildeID
    FROM tagforbilde
    WHERE EmneknaggID IN (
        SELECT EmneknaggID
        FROM emneknagg
        WHERE Emneknaggen LIKE '%VakreMolde'
    )
);

--o
INSERT INTO bruker VALUES 
('kar100','Kari','Karisen','kari@kari.no');

--p
CREATE VIEW MangeLikes AS (
    SELECT COUNT(Likes.BildeID) AS AntallLikes, BildeID,Beskrivelse, OpplastetDato 
    FROM Likes
    JOIN bilde USING (BildeID)
    GROUP BY BildeID
    HAVING AntallLikes>100
);

--q
CREATE USER 'Moderator' IDENTIFIED BY 'ghva948';

--r
GRANT DELETE ON Kommentar TO 'Moderator';