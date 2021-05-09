DROP SCHEMA IF EXISTS DogStore;
CREATE SCHEMA IF NOT EXISTS DogStore;
USE DogStore; 

CREATE TABLE Senter (
    SenterID INT AUTO_INCREMENT,
    Senternavn CHAR(20) NOT NULL,
    CONSTRAINT SenterPK PRIMARY KEY (SenterID)
);

CREATE TABLE Kunde (
    Mobilnr CHAR(11),
    Fornavn CHAR(20) NOT NULL,
    Etternavn CHAR(20) NOT NULL,
    Betalingskortnr CHAR(16) NOT NULL,
    CONSTRAINT KundePK PRIMARY KEY (Mobilnr)
);

CREATE TABLE Boks (
    BoksID INT AUTO_INCREMENT,
    SenterID INT,
    CONSTRAINT BoksPK PRIMARY KEY (BoksID),
    CONSTRAINT BoksSenterFK FOREIGN KEY (SenterID) REFERENCES Senter(SenterID)
);

CREATE TABLE Hund (
    HundeID INT AUTO_INCREMENT,
    Hundenavn CHAR(30) NOT NULL,
    Rase CHAR(20) NOT NULL,
    Eier CHAR(11) NOT NULL,
    Startdato DATE,
    CONSTRAINT HundPK PRIMARY KEY (HundeID),
    CONSTRAINT HundKundeFK FOREIGN KEY (Eier) REFERENCES Kunde(Mobilnr)
);

CREATE TABLE Utleie (
    BoksID INT,
    Starttidspkt TIMESTAMP NOT NULL,
    HundeID INT,
    Sluttidspkt TIMESTAMP,
    Belop DECIMAL(8,2),
    CONSTRAINT UtleiePK PRIMARY KEY (BoksID,Starttidspkt),
    CONSTRAINT UtleieBoksFK FOREIGN KEY (BoksID) REFERENCES Boks(BoksID),
    CONSTRAINT UtleieHundFK FOREIGN KEY (HundeID) REFERENCES Hund(HundeID)
);


INSERT INTO senter (Senternavn) VALUES
('Schulistside'),('Eunicehaven'),('Isabellaton'),('Nitzschemouth'),('West Jamalside'),('New Darionfurt'),('Shieldsland');

INSERT INTO boks (SenterID) VALUES 
(2),(1),(5),(4),(3),(7),(6),(2);

INSERT INTO kunde VALUES
('+4766444373','Ahmed','Cartwright','7380111800014462'),
('+4702437918','Joshuah','Nitzsche','8292901160227195'),
('+4712152682','Greta','Mueller','4661906296362913'),
('+4782606894','Arvilla','Larson','1064969763514438'),
('+4719552435','Michaela','Doyle','9351023299625311'),
('+4774853971','Brady','Langosh','8244411760319113');

INSERT INTO hund (Hundenavn, Rase, Eier, Startdato) VALUES
('Fido','Dachs','+4766444373','20210301'),
('Arne','Huskatt','+4702437918','20210105'),
('Lloyd','Dalmatian','+4712152682','20210508'),
('Emery','Schaefer','+4782606894','20201108'),
('Rodolfo','Bulldog','+4774853971','20200517'),
('Shana','Beagle','+4774853971','20210102'),
('Destin','Golden Retriever','+4766444373','20210214');

INSERT INTO utleie VALUES
(1,'2021-01-01 09:00:15', 3, '2021-01-03 15:30:01', 857.87),
(2,'2021-02-01 09:00:15', 2, '2021-02-02 15:30:01', 457.87),
(1,'2021-01-04 09:00:15', 4, '2021-01-03 15:30:01', 257.87),
(1,'2021-03-01 09:00:15', 3, '2021-03-03 15:30:01', 857.87),
(3,'2021-01-01 09:00:15', 5, '2021-01-03 15:30:01', 857.87),
(4,'2021-04-01 09:00:15', 2, '2021-04-04 15:30:01', 1857.87),
(6,'2021-06-01 09:00:15', 5, '2021-06-06 15:30:01', 1357.87),
(5,'2021-01-01 09:00:15', 3, '2021-01-03 15:30:01', 857.87),
(7,'2021-05-09 09:00:15', 7, NULL, NULL),
(3,'2021-05-01 09:00:15', 3, NULL, NULL);
