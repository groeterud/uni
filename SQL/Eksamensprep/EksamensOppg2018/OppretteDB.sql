DROP SCHEMA IF EXISTS Bildeling;

CREATE SCHEMA IF NOT EXISTS Bildeling;

USE Bildeling;

CREATE TABLE Bil (
    Regnr CHAR(8),
    Merke CHAR(20) NOT NULL,
    Modell CHAR(20) NOT NULL,
    Startdato DATE ,
    Posisjon VARCHAR(60),
    CONSTRAINT BilPK PRIMARY KEY (Regnr)    
);

CREATE TABLE Kunde (
    Mobilnr CHAR (11),
    Fornavn CHAR (20) NOT NULL,
    Etternavn CHAR (20) NOT NULL,
    Betalingskortnr CHAR (12) NOT NULL,
    CONSTRAINT KundePK PRIMARY KEY (Mobilnr)
);

CREATE TABLE Utleie (
    Regnr CHAR(8),
    Utlevert TIMESTAMP NOT NULL,
    KmUt INT NOT NULL,
    Mobilnr CHAR(11),
    Innlevert TIMESTAMP,
    kmInn INT,
    Belop DECIMAL (8,2),
    CONSTRAINT UtleiePK PRIMARY KEY (Regnr,Utlevert),
    CONSTRAINT UtleieBilFK FOREIGN KEY (Regnr) REFERENCES Bil (Regnr),
    CONSTRAINT UtleieKundeFK FOREIGN KEY (Mobilnr) REFERENCES Kunde (Mobilnr)
);

