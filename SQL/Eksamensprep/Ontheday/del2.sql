USE Bildedeling;

SELECT *
FROM bilde;

SELECT Etternavn,Fornavn,Epost
FROM bruker
ORDER BY Etternavn;

SELECT *
FROM bilde
WHERE OpplastetDato>'20210501';

SELECT COUNT(*) AS Antall
FROM bruker;