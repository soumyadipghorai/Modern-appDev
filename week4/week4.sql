-- hostel mapping 
SELECT Students.name, Hostles.name FROM Students 
INNER JOIN Hostles
ON Students.hostelID = Hostels.ID;

-- find all students in calculas 
SELECT s.name FROM Students s
JOIN StudentsCourses sc ON s.IDNumber = sc.studentID 
WHERE c.name = 'Calculus';