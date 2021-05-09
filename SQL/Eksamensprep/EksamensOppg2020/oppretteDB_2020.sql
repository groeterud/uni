DROP SCHEMA IF EXISTS university;

CREATE SCHEMA IF NOT EXISTS university;

USE university;

CREATE TABLE student (
    sid INT AUTO_INCREMENT,
    sname CHAR(40) NOT NULL,
    sex CHAR(1) NOT NULL,
    age INT NOT NULL,
    year INT NOT NULL,
    gpa DECIMAL (2,1),
    CONSTRAINT studentPK PRIMARY KEY (sid)
);
CREATE TABLE dept (
    dname CHAR(20),
    numphds INT,
    CONSTRAINT deptPK PRIMARY KEY (dname)
);
CREATE TABLE prof (
    pname CHAR(40),
    dname CHAR(20),
    CONSTRAINT profPK PRIMARY KEY (pname),
    CONSTRAINT profdeptFK FOREIGN KEY (dname) REFERENCES dept(dname)
);
CREATE TABLE course (
    cno INT AUTO_INCREMENT,
    cname CHAR(20) NOT NULL,
    dname CHAR(20),
    CONSTRAINT coursePK PRIMARY KEY (cno,dname),
    CONSTRAINT coursedeptFK FOREIGN KEY (dname) REFERENCES dept(dname)
);
CREATE TABLE major (
    dname CHAR(20),
    sid INT,
    CONSTRAINT majorPK PRIMARY KEY (dname,sid),
    CONSTRAINT majordeptFK FOREIGN KEY (dname) REFERENCES dept(dname),
    CONSTRAINT majorstudentFK FOREIGN KEY (sid) REFERENCES student(sid)
);
CREATE TABLE section (
    dname CHAR(20),
    cno INT,
    sectno INT UNIQUE NOT NULL,
    pname CHAR(40),
    CONSTRAINT sectionPK PRIMARY KEY (dname,cno,sectno),
    CONSTRAINT sectiondeptFK FOREIGN KEY (dname) REFERENCES dept(dname),
    CONSTRAINT sectioncourseFK FOREIGN KEY (cno) REFERENCES course(cno),
    CONSTRAINT sectionprofFK FOREIGN KEY (pname) REFERENCES prof(pname)
);
CREATE TABLE enroll (
    sid INT,
    grade CHAR(1),
    dname CHAR(20),
    cno INT,
    sectno INT,
    CONSTRAINT enrollPK PRIMARY KEY (sid,dname,cno,sectno),
    CONSTRAINT enrollstudentFK FOREIGN KEY (sid) REFERENCES student(sid),
    CONSTRAINT enrolldeptFK FOREIGN KEY (dname) REFERENCES dept(dname),
    CONSTRAINT enrollcourseFK FOREIGN KEY (cno) REFERENCES course(cno),
    CONSTRAINT enrollsectionFK FOREIGN KEY (sectno) REFERENCES section(sectno)
);
INSERT INTO student (sname,sex,age,year,gpa) VALUES ('Kory Luettgen DVM','M',20,2,3.4),('Ms. Clark Hegmann','F',17,1,2.4),('Cheyanne Hessel','U',19,3,3.9),('Jerrell Glover','M',16,2,4.0),('Deonte Beatty','u',20,4,2.8),('Ms. Arvel Grimes','F',17,5,3.5),('Esperanza West','F',17,1,3.4),('Kaelyn Kling PhD','F',28,5,3.4),('Cedrick Beatty','M',17,2,3.4),('Buddy Schimmel','M',19,3,3.7),('Abe Carter','M',18,5,3.8),('Macy King','F',26,2,3.1),('Riley Crist','U',17,3,2.6),('Eldora White','F',19,3,3.7),('Rowena Torphy Sr.','U',17,2,3.5),('Toy Schuppe','M',25,2,3.4),('Major Champlin','M',17,3,3.4);
INSERT INTO dept VALUES('sexy', 37),('paradigms', 93),('Handmade', 93),('eyeballs', 19),('Books', 18),('dynamic', 84),('seize', 3),('web-enabled', 42),('cutting-edge', 11),('platforms', 75),('Electronics', 90),('Internet', 5),('Generic', 48),('Shoes', 75),('Movies', 91),('Sports', 55),('Outdoors', 83),('streamline', 22),('Industrial', 28);
INSERT INTO prof VALUES('Merle Balistreri','sexy'),('Hollis Ankunding','sexy'),('Ophelia Wisozk','paradigms'),('Brian Orn','paradigms'),('Kamille Glover','paradigms'),('Mrs. Rosalinda Lubowitz','Handmade'),('Carolyne Auer','Handmade'),('Mr. Isabell Tremblay','Handmade'),('Jody Gorczany','eyeballs'),('Rogers Gerhold MD','eyeballs'),('Humberto Crist','eyeballs'),('Freddie Schoen','Books'),('Frieda Green','Books'),('Valentina Smitham III','Books'),('Percy Flatley','Books'),('Dr. Alexandrea Mayert','Books'),('Bertha Reynolds III','Books'),('Evans Kassulke','dynamic'),('Magnus West','dynamic'),('Jayce Koch','dynamic'),('Adalberto Davis','Electronics'),('Maeve Gerhold','Electronics'),('Lorenza Langworth','Electronics'),('Marguerite Jenkins','Generic'),('Fredrick Aufderhar','Generic'),('Lilliana Herzog','Generic'),('Garnett Kovacek','Industrial'),('Allan Wiza MD','Industrial'),('Celestine Von','Internet'),('Jewell Schmitt','Movies'),('Carson Fritsch','Movies'),('Ulises Feil','Movies'),('Name Nader I','Movies'),('Mrs. Letitia Jacobs','Outdoors'),('Margret Bernhard','Outdoors'),('Elton Mitchell','Outdoors'),('Vernon Harber','Outdoors'),('Jessica Schmitt','platforms'),('Darryl Parisian','platforms'),('Neoma Orn','platforms'),('Tianna Spencer','seize'),('Adriana Johns MD','Shoes'),('Grant Jerde','Shoes'),('Muriel Lebsack','Shoes'),('Stewart Metz','Sports'),('Maida Heathcote','Sports'),('Melyna Prohaska','Sports'),('Murl Ward Jr.','Sports'),('Kennedi Marquardt','Sports'),('Davon MacGyver','streamline'),('Miss Theron Schiller','streamline'),('Sincere Moore','streamline'),('Kurtis Senger','streamline'),('Gerard Feeney','streamline'),('Cristina Mann','web-enabled'),('Terrance Huels','web-enabled'),('Amari Kshlerin','web-enabled'),('Annette Cassin','web-enabled'),('Caterina Rosenbaum','sexy');

INSERT INTO course (cname,dname) VALUES 
('Computer Science','Electronics'),
('Programming ezmode','Electronics');

INSERT INTO major VALUES
('Generic',1),
('Generic',2),
('Generic',3),
('Electronics',4),
('Generic',5),
('Electronics',6),
('Handmade',7),
('Electronics',8),
('Electronics',9),
('Handmade',10),
('Electronics',11),
('Handmade',12),
('Electronics',13),
('Handmade',14),
('Electronics',15),
('Handmade',16),
('Handmade',17);


INSERT INTO section VALUES
('Electronics',1,1,'Adalberto Davis'),
('Electronics',2,2,'Adalberto Davis');

INSERT INTO enroll VALUES (1,NULL,'Electronics',2,2),(1,NULL,'Electronics',1,1),(2,NULL,'Electronics',1,1),(4,NULL,'Electronics',1,1),(5,NULL,'Electronics',1,1),(6,NULL,'Electronics',1,1),(7,NULL,'Electronics',1,1),(9,NULL,'Electronics',1,1),(10,'C','Electronics',1,1),(11,NULL,'Electronics',1,1),(13,NULL,'Electronics',1,1),(15,'B','Electronics',1,1),(16,'A','Electronics',1,1);

