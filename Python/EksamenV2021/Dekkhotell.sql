DROP SCHEMA IF EXISTS Dekkhotell;

CREATE SCHEMA IF NOT EXISTS Dekkhotell;

USE Dekkhotell;

CREATE TABLE Kunde (
    Mobilnr CHAR(11),
    Fornavn CHAR(30) NOT NULL,
    Etternavn CHAR(30) NOT NULL,
    epost CHAR(30) NOT NULL,
    CONSTRAINT KundePK PRIMARY KEY (Mobilnr)
);

INSERT INTO Kunde VALUES
('+4711111111','Caterina','Block','Audra.Marvin@hotmail.com'),
('+4722222222','Madison','Kirlin','Angel_Sawayn@gmail.com');

CREATE TABLE Dekksett (
    Mobilnr CHAR(11),
    Regnr CHAR(7),
    CONSTRAINT DekksettPK PRIMARY KEY (Mobilnr,Regnr),
    CONSTRAINT DekksettKundeFK FOREIGN KEY (Mobilnr) REFERENCES Kunde(Mobilnr)
);

INSERT INTO Dekksett VALUES 
('+4711111111','SV12345'),
('+4711111111','SV54321'),
('+4722222222','EL12345');

CREATE TABLE Oppbevaring (
    Mobilnr CHAR(11),
    Regnr CHAR(7),
    Innlevert DATE,
    Utlevert DATE,
    Hylle CHAR(5) NOT NULL,
    Pris INT,
    CONSTRAINT OppbevaringPK PRIMARY KEY (Mobilnr,Regnr,Innlevert),
    CONSTRAINT OppbevaringDekksetFK FOREIGN KEY (Mobilnr,Regnr) REFERENCES Dekksett(Mobilnr,Regnr)
);

INSERT INTO oppbevaring VALUES
('+4711111111','SV54321',CURRENT_DATE,NULL,'C25',NULL),
('+4722222222','EL12345','20210120',NULL,'E13',NULL);


CREATE USER 'Dekksjef' IDENTIFIED BY 'eksamen2021';
GRANT ALL ON *.* TO 'Dekksjef';