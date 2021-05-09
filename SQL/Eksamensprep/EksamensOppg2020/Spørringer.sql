USE university;
--b
SELECT *
FROM student;
--c
SELECT sname AS name, year, gpa
FROM student 
ORDER BY name;
--d
SELECT *
FROM student
WHERE year=1;

--e
SELECT COUNT(*) AS Antall
FROM student;

--f
SELECT pname 
FROM prof
    JOIN dept USING (dname)
WHERE numphds < 50;

--g
SELECT MIN((gpa)) AS lavesteGPA, sname
FROM student;

-- h jeg bruker Electronics som eksempel fordi lazy 
SELECT cno, sectno, gpa
FROM enroll
    JOIN student USING (sid)
WHERE dname='Electronics';

-- i bruker annet tall for illustrativitet.
SELECT cname, cno, section.sectno, COUNT(sid) AS Antall
FROM course
    JOIN section using (cno)
    JOIN enroll USING (cno)
GROUP BY cname
HAVING Antall<15;

-- j 
SELECT sname, student.sid, MAX (teller) AS Mest
FROM (
    SELECT sid, COUNT(sid) AS teller
    FROM enroll
    GROUP BY sid
)AS TellerSporring
    JOIN student USING (sid);


-- k
SELECT DISTINCT dname
FROM major
    JOIN student USING (sid)
WHERE student.age<18;

-- l
SELECT DISTINCT sname, major.dname
FROM enroll
    JOIN student USING (sid)
    JOIN major USING (dname)
    JOIN course USING (cno)
WHERE cname='Computer Science';


-- m
SELECT dname, numphds
FROM dept
WHERE dname NOT IN (
    SELECT enroll.dname
    FROM enroll
        JOIN course USING (cno)
    WHERE cname='Computer Science'
);

-- n 
SELECT sname
FROM student
WHERE sid IN (
    SELECT sid
    FROM enroll
        JOIN course USING (cno)
    WHERE cname='Computer Science'
)
    AND
    sid IN (
        SELECT sid
        FROM enroll
            JOIN course USING (cno)
        WHERE cname='Programming ezmode'
    )
;
--o
SELECT (MAX(student.age)-MIN(student.age)) AS Aldersforskjell
FROM student
WHERE sid IN (
    SELECT sid
    FROM enroll
        JOIN course USING (cno)
    WHERE cname='Computer Science'
);

SELECT major.dname, AVG(student.gpa) AS AvgGPA
FROM major
    JOIN student USING (sid)
GROUP BY major.dname
HAVING AvgGPA>3.3;


--q
SELECT sid, sname,gpa
FROM student
WHERE sid IN (
    SELECT sid
    FROM enroll
        JOIN course USING (cno)
    WHERE cname='Computer Science'
);