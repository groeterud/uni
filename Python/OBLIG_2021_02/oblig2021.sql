DROP SCHEMA IF EXISTS oblig2021;
CREATE SCHEMA oblig2021;
USE oblig2021;

CREATE TABLE Student
(
    Studentnr CHAR (6) NOT NULL,
    Fornavn CHAR (30) NOT NULL,
    Etternavn CHAR (20) NOT NULL,
    Epost CHAR (40),
    Telefon CHAR (8),
    CONSTRAINT StudentPK PRIMARY KEY (Studentnr)
);

CREATE TABLE Emne
(
    Emnekode CHAR (8) NOT NULL,
    Emnenavn CHAR (40) NOT NULL,
    Studiepoeng DECIMAL (3,1) NOT NULL,
    CONSTRAINT EmnePK PRIMARY KEY (Emnekode)
);

CREATE TABLE Rom
(
    Romnr CHAR (4) NOT NULL,
    Antallplasser INTEGER (3),
    CONSTRAINT RomPK PRIMARY KEY (Romnr)
);
CREATE TABLE Eksamen
(
    Emnekode CHAR (8) NOT NULL,
    Dato DATE NOT NULL,
    Romnr CHAR (4) NOT NULL,
    CONSTRAINT EksamenPK PRIMARY KEY (Emnekode,Dato),
    CONSTRAINT EksamenEmneFK FOREIGN KEY (Emnekode) REFERENCES Emne (Emnekode),
    CONSTRAINT EksamenRomFK FOREIGN KEY (Romnr) REFERENCES Rom (Romnr)
);
CREATE TABLE Eksamensresultat
(
    Studentnr CHAR (6) NOT NULL,
    Emnekode CHAR (8) NOT NULL,
    Dato DATE NOT NULL, 
    Karakter CHAR (1),
    CONSTRAINT EksamensresultatPK PRIMARY KEY (Studentnr,Emnekode,Dato),
    CONSTRAINT EksamensresultatStudentFK FOREIGN KEY (Studentnr) REFERENCES Student (Studentnr),
    CONSTRAINT EksamensresultatEksamenFK FOREIGN KEY (Emnekode,Dato) REFERENCES Eksamen (Emnekode,Dato)
);

INSERT INTO student(Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES('000001','Syble','Funk','Carlie.Osinski@gmail.com','75174885'),('000002','Annamae','Kuhlman','Cydney40@hotmail.com','55311542'),('000003','Mellie','Cremin','Lauriane.Powlowski47@gmail.com','89104304'),('000004','Willy','Bode','Margaret70@gmail.com','90040471'),('000005','Chris','Erdman','Brando71@example.org','36003677'),('111111','Ada','Martin','a.martin@randatmail.com','11111111'),('211204','Howell','Johns','Kristofer55@gmail.com','51066733'),('222222','Eilan','Carroll','e.carroll@randatmail.com','22222222'),('333333','Jordan','Cameron','j.cameron@randatmail.com','33333333'),('444444','Andrew','Payne','a.payne@randatmail.com','44444444'),('555555','Sabrina','Spencer','s.spencer@randatmail.com','55555555'),('666666','Alexia','Williams','\ta.williams@randatmail.com','66666666'),('777777','Dale','Miller','d.miller@randatmail.com','77777777'),('888888','Ried','Ferguson','r.ferguson@randatmail.com','88888888'),('900009','Madelein','Bailie','m.bailey@randatmail.com','900009');
INSERT INTO emne(Emnekode,Emnenavn,Studiepoeng) VALUES('SYS1000','FørsteEmne',7.5),('AID3000','AI & Deep Learning',15.0),('SAM1000','SAMunnsansvar og Etikk',7.5),('ORGL1000','Organisasjon og Ledelse',30.0),('ITIS1000','IT og Informasjonssystemer',15.0),('WEB1100','Webutvikling',7.5),('PRG2000','Avansert PRGrammering',15.0),('PRG1100','Videregående PRGrammering',30.0),('DAT2000','Videregående Database',7.5),('DAT1000','Grunnleggende database',15.0),('PRG1000','Grunnleggende PRGrammering',7.5),('PRO1000','Praktisk Prosjekt',7.5);
INSERT INTO rom(Romnr,Antallplasser) VALUES('0012',150),('0032',300),('1234',123),('2234',50),('3211',500),('3234',78),('4234',39),('5234',99);
INSERT INTO eksamen(Emnekode,Dato,Romnr) VALUES('DAT1000','2020-05-25','0012'),('PRG1000','2020-05-21','0012'),('PRG1000','2020-05-22','0012'),('PRG1100','2020-05-24','0012'),('DAT1000','2020-05-21','0032'),('DAT2000','2020-05-22','0032'),('PRG1000','2020-05-25','0032'),('SYS1000','2020-05-10','1234'),('AID3000','2020-06-18','1234'),('PRG1000','2020-05-23','1234'),('SAM1000','2020-05-03','2234'),('ORGL1000','2020-05-12','2234'),('PRO1000','2020-05-23','3211'),('PRO1000','2020-05-24','3211'),('ITIS1000','2020-03-07','3234'),('WEB1100','2020-04-19','3234'),('PRG2000','2020-04-09','4234'),('PRG1100','2020-03-29','4234'),('DAT2000','2020-05-24','5234'),('ITIS1000','2021-07-07','3234'),('WEB1100','2021-04-19','3234'),('PRG2000','2021-04-09','4234'),('PRG1100','2021-03-29','4234'),('DAT2000','2021-05-24','5234');
INSERT INTO eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES('000001','DAT2000','2020-05-22','C'),('000001','DAT1000','2020-05-25','B'),('000001','PRG1000','2020-05-21','B'),('000001','PRG1100','2020-05-24','A'),('000001','PRO1000','2020-05-23','D'),('000001','PRO1000','2020-05-24','B'),('000002','PRG1000','2020-05-21','A'),('000003','PRG1000','2020-05-21','D'),('000004','DAT1000','2020-05-25','E'),('000005','DAT1000','2020-05-25','A'),('000005','PRO1000','2020-05-24','B'),('111111','SYS1000','2020-05-10','B'),('111111','AID3000','2020-06-18',NULL),('211204','PRO1000','2020-05-24','A'),('222222','SAM1000','2020-05-03','C'),('222222','ORGL1000','2020-05-12','D'),('333333','WEB1100','2020-04-19','B'),('333333','PRG1100','2020-03-29','A'),('444444','ORGL1000','2020-05-12','D'),('444444','DAT2000','2020-05-24','E'),('555555','ITIS1000','2020-03-07','C'),('555555','PRG2000','2020-04-09','B'),('666666','PRG2000','2020-04-09','E'),('777777','ITIS1000','2020-03-07','A'),('777777','DAT2000','2020-05-24','E'),('888888','AID3000','2020-06-18','C'),('900009','SYS1000','2020-05-10','A'),('900009','PRG1100','2020-03-29','B');

-- Nullverdi på karakter på eksamensresultat, klar til inserts, skal legge typ 20

INSERT INTO eksamensresultat VALUES 
('000001','DAT1000','2020-05-21',NULL),
('000002','DAT1000','2020-05-21',NULL),
('000003','DAT1000','2020-05-21',NULL),
('000004','DAT1000','2020-05-21',NULL),
('000005','DAT1000','2020-05-21',NULL),
('111111','DAT1000','2020-05-21',NULL),
('211204','DAT1000','2020-05-21',NULL),
('222222','DAT1000','2020-05-21',NULL),
('333333','DAT1000','2020-05-21',NULL),
('444444','DAT1000','2020-05-21',NULL),
('555555','DAT1000','2020-05-21',NULL),
('666666','DAT1000','2020-05-21',NULL),
('777777','DAT1000','2020-05-21',NULL),
('888888','DAT1000','2020-05-21',NULL),
('900009','DAT1000','2020-05-21',NULL);
