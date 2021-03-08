USE oblig2021;

INSERT INTO Student (Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES
('111111','Ada','Martin','a.martin@randatmail.com','11111111'),
('222222','Eilan','Carroll','e.carroll@randatmail.com','22222222'),
('333333','Jordan','Cameron','j.cameron@randatmail.com','33333333'),
('444444','Andrew','Payne','a.payne@randatmail.com','44444444'),
('555555','Sabrina','Spencer','s.spencer@randatmail.com','55555555'),
('666666','Alexia','Williams','	a.williams@randatmail.com','66666666'),
('777777','Dale','Miller','d.miller@randatmail.com','77777777'),
('888888','Ried','Ferguson','r.ferguson@randatmail.com','88888888'),
('999999','Madelein','Bailie','m.bailey@randatmail.com','99999999');


INSERT INTO Emne (Emnekode,Emnenavn,Studiepoeng) VALUES
('10001000','FørsteEmne',7.5),
('20002000','AndreEmne',15.0),
('30003000','TredjeEmne',7.5),
('40004000','FjerdeEmne',30.0),
('50005000','FemteEmne',15.0),
('60006000','sjetteEmne',7.5),
('70007000','syvendeEmne',15.0),
('80008000','åttendeEmne',30.0),
('90009000','niendeEmne',7.5);


INSERT INTO Rom (Romnr,Antallplasser) VALUES
('1234',100),
('2234',50),
('3234',78),
('4234',39),
('5234',99);


INSERT INTO Eksamen (Emnekode,Dato,Romnr) VALUES
('10001000','20200510','1234'),
('20002000','20200618','1234'),
('30003000','20200503','2234'),
('40004000','20200512','2234'),
('50005000','20200307','3234'),
('60006000','20200419','3234'),
('70007000','20200409','4234'),
('80008000','20200329','4234'),
('90009000','20200524','5234');


INSERT INTO Eksamensresultat (Studentnr,Emnekode,Dato,Karakter) VALUES
('111111','10001000','20200510','B'),
('111111','20002000','20200618',''),
('222222','30003000','20200503','C'),
('222222','40004000','20200512','D'),
('333333','80008000','20200329','A'),
('333333','60006000','20200419','B'),
('444444','90009000','20200524','E'),
('444444','40004000','20200512','D'),
('555555','70007000','20200409','B'),
('555555','50005000','20200307','C'),
('666666','70007000','20200409','E'),
('777777','50005000','20200307','A'),
('777777','90009000','20200524','E'),
('888888','20002000','20200618',''),
('999999','10001000','20200510','A'),
('999999','80008000','20200329','B');

SELECT*
FROM Eksamensresultat;

CREATE USER 'Eksamenssjef' IDENTIFIED BY 'oblig2021';






