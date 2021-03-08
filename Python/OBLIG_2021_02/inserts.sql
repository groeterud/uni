USE oblig2021;

INSERT INTO student(Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES
('000001','Syble','Funk','Carlie.Osinski@gmail.com','75174885'),
('000002','Annamae','Kuhlman','Cydney40@hotmail.com','55311542'),
('000003','Mellie','Cremin','Lauriane.Powlowski47@gmail.com','89104304'),
('000004','Willy','Bode','Margaret70@gmail.com','90040471'),
('000005','Chris','Erdman','Brando71@example.org','36003677'),
('211204','Howell','Johns','Kristofer55@gmail.com','51066733');

INSERT INTO emne(Emnekode,Emnenavn,Studiepoeng) VALUES 
('FVWUSYZ1','Self-enabling background matrices',7.5),
('DFIATMC1','Expanded zero defect pricing structure',15.0),
('YFRIKRB1','Seamless modular leverage',7.5);


INSERT INTO rom(Romnr,Antallplasser) VALUES 
('0012',150),
('0032',300),
('1234',123),
('3211',500);


INSERT INTO eksamen(Emnekode,Dato,Romnr) VALUES 
('FVWUSYZ1','20200521','0012'),
('DFIATMC1','20200522','0032'),
('YFRIKRB1','20200523','3211'),
('FVWUSYZ1','20200524','0012'),
('FVWUSYZ1','20200525','0032'),
('DFIATMC1','20200521','0032'),
('FVWUSYZ1','20200522','0012'),
('FVWUSYZ1','20200523','1234'),
('YFRIKRB1','20200524','3211'),
('DFIATMC1','20200525','0012');

INSERT INTO eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES 
('000001','FVWUSYZ1','20200521','B'),
('000001','DFIATMC1','20200522','C'),
('000001','YFRIKRB1','20200523','D'),
('000001','FVWUSYZ1','20200524','A'),
('000001','DFIATMC1','20200525','B'),
('000001','YFRIKRB1','20200524','B'),
('000002','FVWUSYZ1','20200521','A'),
('000003','FVWUSYZ1','20200521','D'),
('000001','DFIATMC1','20200521','D'),
('211204','YFRIKRB1','20200524','A'),
('000004','DFIATMC1','20200525','E'),
('000005','DFIATMC1','20200525','A');

