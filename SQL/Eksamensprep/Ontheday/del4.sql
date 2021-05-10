USE Bildedeling;

--s
SELECT BildeID,COUNT(*) AS Mest
FROM kommentar
GROUP BY BildeID
HAVING COUNT(*)=(
	SELECT MAX(Teller) 
	FROM (
		SELECT BildeID,COUNT(*) AS Teller 
		FROM kommentar 
		GROUP BY BildeID
	) AS FlestKommentarer
);

--t
DELETE FROM kommentar
WHERE BrukerID='ant100' AND BildeID IN (
    SELECT BildeID
    FROM bilde
    WHERE bilde.Fotograf='kar100'

);



SELECT * from kommentar;