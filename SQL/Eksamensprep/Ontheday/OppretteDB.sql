DROP SCHEMA IF EXISTS Bildedeling;

CREATE SCHEMA IF NOT EXISTS Bildedeling;

USE Bildedeling;

CREATE TABLE Bruker (
    BrukerID CHAR(6),
    Fornavn CHAR(20) NOT NULL,
    Etternavn CHAR(20) NOT NULL,
    Epost CHAR(40) NOT NULL,
    CONSTRAINT BrukerPK PRIMARY KEY (BrukerID)
);
INSERT INTO bruker VALUES
('CRO100','Jonas','Blundenes','Demarco.Ryan4@yahoo.com'),
('Der100','Alex','Rosen','Hermina49@hotmail.com');

CREATE TABLE Bilde (
    BildeID CHAR(6),
    Beskrivelse VARCHAR(100),
    OpplastetDato DATE NOT NULL,
    Fotograf CHAR (6) NOT NULL,
    CONSTRAINT BildePK PRIMARY KEY (BildeID),
    CONSTRAINT BildeBrukerFK FOREIGN KEY (Fotograf) REFERENCES Bruker(BrukerID)
);
INSERT INTO Bilde VALUES
('pic100','Fint bilde av vannet','20210502','CRO100'),
('pic099','Litt mye vær','20210430','CRO100'),
('pic101','Idkman','20210503','CRO100');

CREATE TABLE Likes (
    BildeID CHAR(6),
    BrukerID CHAR(6),
    CONSTRAINT LikesPK PRIMARY KEY (BildeID,BrukerID),
    CONSTRAINT LikesBildeFK FOREIGN KEY (BildeID) REFERENCES Bilde(BildeID),
    CONSTRAINT LikesBrukerFK FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
);

INSERT INTO likes VALUES
('pic099','CRO100'),('pic099','Der100'),('pic100','Der100');

CREATE TABLE Kommentar (
    BildeID CHAR(6),
    BrukerID CHAR(6),
    Kommentaren VARCHAR(100) NOT NULL,
    CONSTRAINT KommentarPK PRIMARY KEY (BildeID,BrukerID),
    CONSTRAINT KommentarBildeFK FOREIGN KEY (BildeID) REFERENCES Bilde(BildeID),
    CONSTRAINT KommentarBrukerFK FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
);
INSERT INTO Kommentar VALUES
('pic100','Der100','Kult bilde!'),
('pic100','CRO100','Takk mann :D'),
('pic099','CRO100','Dette ble ikke helt vellykket');

CREATE TABLE Emneknagg (
    EmneknaggID INT AUTO_INCREMENT,
    Emneknaggen CHAR(20) NOT NULL,
    CONSTRAINT EmneknaggPK PRIMARY KEY (EmneknaggID)
);
INSERT INTO Emneknagg (Emneknaggen) VALUES
('VakreMolde'),('BareMolde'),('AldriMolde'),('BergenBy');

CREATE TABLE TagForBilde (
    BildeID CHAR(6),
    EmneknaggID INT,
    CONSTRAINT TagForBildePK PRIMARY KEY (BildeID,EmneknaggID),
    CONSTRAINT TagForBildeBildeFK FOREIGN KEY (BildeID) REFERENCES Bilde(BildeID),
    CONSTRAINT TagForBildeEmneknaggFK FOREIGN KEY (EmneknaggID) REFERENCES Emneknagg(EmneknaggID)
);

INSERT INTO tagforbilde (BildeID,EmneknaggID) VALUES
('pic100',1),
('pic100',2),
('pic099',1),
('pic101',3),
('pic101',4);