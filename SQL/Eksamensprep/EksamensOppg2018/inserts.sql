USE Bildeling;

INSERT INTO Bil VALUES (
    'AX88775', 'Kovacek','Avensis', '20210508', '39.0346, -45.3685'
),
(   'SV32875', 'Hagenes Inc','Derplord', '20201001', '-76.6890, 3.2198'
);



INSERT INTO Kunde VALUES (
    '81893542', 'Cassandra', 'Bradtke', '68963701'
),
(   '57065559', 'Hilbert', 'Yost', '12505510'
),
(   '88157833', 'Efren', 'Heaney', '78874224'
);


INSERT INTO bil VALUES ('SV11324', 'Mercedez','E250','20180401', '111.5460, -44.9528');


INSERT INTO utleie (Regnr, Utlevert, KmUt, Mobilnr, Innlevert,kmInn,Belop) 
VALUES 
(
    'AX88775', '2021-05-08 15:24:05', 145000, '81893542', NULL, NULL, NULL 
),
(
    'AX88775', '2021-05-07 08:00:15', 135000, '81893542', '2021-05-07 15:15:15', 142000, 1250.90
);

INSERT INTO utleie  VALUES ('SV11324','2020-04-20 13:37:13', 10000,'57065559','2020-06-01 16:06:11',18000,3575.50);

INSERT INTO utleie  VALUES ('SV11324','2020-06-15 16:06:01', 18000,'81893542','2020-06-18 16:06:01',22000,1250.50);

INSERT INTO utleie  VALUES ('SV32875','2020-06-15 16:06:01', 180000,'57065559','2020-06-18 16:06:01',195000,1750.50);

INSERT INTO utleie  VALUES ('AX88775','2020-06-15 16:06:01', 125000,'88157833','2020-06-18 16:06:01',12750,1750.50);

INSERT INTO utleie VALUES ('SV11324','2021-05-01 01:05:30', 22000, '81893542', NULL, NULL, NULL);

CREATE USER 'Bilsjef' IDENTIFIED BY 'eksamen2020';

GRANT ALL PRIVILEGES ON Bildeling.* TO 'Bilsjef';