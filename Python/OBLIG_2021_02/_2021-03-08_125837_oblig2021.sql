DROP TABLE IF EXISTS eksamen;
CREATE TABLE `eksamen` (
  `Emnekode` char(8) NOT NULL,
  `Dato` date NOT NULL,
  `Romnr` char(4) NOT NULL,
  PRIMARY KEY (`Emnekode`,`Dato`),
  KEY `EksamenRomFK` (`Romnr`),
  CONSTRAINT `EksamenEmneFK` FOREIGN KEY (`Emnekode`) REFERENCES `emne` (`Emnekode`),
  CONSTRAINT `EksamenRomFK` FOREIGN KEY (`Romnr`) REFERENCES `rom` (`Romnr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS eksamensresultat;
CREATE TABLE `eksamensresultat` (
  `Studentnr` char(6) NOT NULL,
  `Emnekode` char(8) NOT NULL,
  `Dato` date NOT NULL,
  `Karakter` char(1) DEFAULT NULL,
  PRIMARY KEY (`Studentnr`,`Emnekode`,`Dato`),
  KEY `EksamensresultatEksamenFK` (`Emnekode`,`Dato`),
  CONSTRAINT `EksamensresultatEksamenFK` FOREIGN KEY (`Emnekode`, `Dato`) REFERENCES `eksamen` (`Emnekode`, `Dato`),
  CONSTRAINT `EksamensresultatStudentFK` FOREIGN KEY (`Studentnr`) REFERENCES `student` (`Studentnr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS emne;
CREATE TABLE `emne` (
  `Emnekode` char(8) NOT NULL,
  `Emnenavn` char(40) NOT NULL,
  `Studiepoeng` decimal(3,1) NOT NULL,
  PRIMARY KEY (`Emnekode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS rom;
CREATE TABLE `rom` (
  `Romnr` char(4) NOT NULL,
  `Antallplasser` int DEFAULT NULL,
  PRIMARY KEY (`Romnr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS student;
CREATE TABLE `student` (
  `Studentnr` char(6) NOT NULL,
  `Fornavn` char(30) NOT NULL,
  `Etternavn` char(20) NOT NULL,
  `Epost` char(40) DEFAULT NULL,
  `Telefon` char(8) DEFAULT NULL,
  PRIMARY KEY (`Studentnr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




INSERT INTO eksamen(Emnekode,Dato,Romnr) VALUES('DFIATMC1','2020-05-25','0012'),('FVWUSYZ1','2020-05-21','0012'),('FVWUSYZ1','2020-05-22','0012'),('FVWUSYZ1','2020-05-24','0012'),('DFIATMC1','2020-05-21','0032'),('DFIATMC1','2020-05-22','0032'),('FVWUSYZ1','2020-05-25','0032'),('10001000','2020-05-10','1234'),('20002000','2020-06-18','1234'),('FVWUSYZ1','2020-05-23','1234'),('30003000','2020-05-03','2234'),('40004000','2020-05-12','2234'),('YFRIKRB1','2020-05-23','3211'),('YFRIKRB1','2020-05-24','3211'),('50005000','2020-03-07','3234'),('60006000','2020-04-19','3234'),('70007000','2020-04-09','4234'),('80008000','2020-03-29','4234'),('90009000','2020-05-24','5234');

INSERT INTO eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES('000001','DFIATMC1','2020-05-21','D'),('000001','DFIATMC1','2020-05-22','C'),('000001','DFIATMC1','2020-05-25','B'),('000001','FVWUSYZ1','2020-05-21','B'),('000001','FVWUSYZ1','2020-05-24','A'),('000001','YFRIKRB1','2020-05-23','D'),('000001','YFRIKRB1','2020-05-24','B'),('000002','FVWUSYZ1','2020-05-21','A'),('000003','FVWUSYZ1','2020-05-21','D'),('000004','DFIATMC1','2020-05-25','E'),('000005','DFIATMC1','2020-05-25','A'),('000005','YFRIKRB1','2020-05-24','B'),('111111','10001000','2020-05-10','B'),('111111','20002000','2020-06-18',''),('211204','YFRIKRB1','2020-05-24','A'),('222222','30003000','2020-05-03','C'),('222222','40004000','2020-05-12','D'),('333333','60006000','2020-04-19','B'),('333333','80008000','2020-03-29','A'),('444444','40004000','2020-05-12','D'),('444444','90009000','2020-05-24','E'),('555555','50005000','2020-03-07','C'),('555555','70007000','2020-04-09','B'),('666666','70007000','2020-04-09','E'),('777777','50005000','2020-03-07','A'),('777777','90009000','2020-05-24','E'),('888888','20002000','2020-06-18',''),('999999','10001000','2020-05-10','A'),('999999','80008000','2020-03-29','B');

INSERT INTO emne(Emnekode,Emnenavn,Studiepoeng) VALUES('10001000','FørsteEmne',7.5),('20002000','AndreEmne',15.0),('30003000','TredjeEmne',7.5),('40004000','FjerdeEmne',30.0),('50005000','FemteEmne',15.0),('60006000','sjetteEmne',7.5),('70007000','syvendeEmne',15.0),('80008000','åttendeEmne',30.0),('90009000','niendeEmne',7.5),('DFIATMC1','Expanded zero defect pricing structure',15.0),('FVWUSYZ1','Self-enabling background matrices',7.5),('YFRIKRB1','Seamless modular leverage',7.5);

INSERT INTO rom(Romnr,Antallplasser) VALUES('0012',150),('0032',300),('1234',123),('2234',50),('3211',500),('3234',78),('4234',39),('5234',99);
INSERT INTO student(Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES('000001','Syble','Funk','Carlie.Osinski@gmail.com','75174885'),('000002','Annamae','Kuhlman','Cydney40@hotmail.com','55311542'),('000003','Mellie','Cremin','Lauriane.Powlowski47@gmail.com','89104304'),('000004','Willy','Bode','Margaret70@gmail.com','90040471'),('000005','Chris','Erdman','Brando71@example.org','36003677'),('111111','Ada','Martin','a.martin@randatmail.com','11111111'),('211204','Howell','Johns','Kristofer55@gmail.com','51066733'),('222222','Eilan','Carroll','e.carroll@randatmail.com','22222222'),('333333','Jordan','Cameron','j.cameron@randatmail.com','33333333'),('444444','Andrew','Payne','a.payne@randatmail.com','44444444'),('555555','Sabrina','Spencer','s.spencer@randatmail.com','55555555'),('666666','Alexia','Williams','\ta.williams@randatmail.com','66666666'),('777777','Dale','Miller','d.miller@randatmail.com','77777777'),('888888','Ried','Ferguson','r.ferguson@randatmail.com','88888888'),('999999','Madelein','Bailie','m.bailey@randatmail.com','99999999');







