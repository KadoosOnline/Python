-- Four tables in one query: enrollments -> students, courses -> teachers.
-- Every JOIN adds one table and says how it is attached.
SELECT
    s.first_name || ' ' || s.last_name AS 'نام دانشجو',
    c.title                            AS 'نام درس',
    t.teacher_name                     AS 'استاد',
    e.grade                            AS 'نمره'
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses  c ON e.course_id  = c.course_id
LEFT JOIN teachers t ON c.teacher_id = t.teacher_id
ORDER BY s.last_name;

-- The average grade of every course: a JOIN together with a GROUP BY.
SELECT c.title, ROUND(AVG(e.grade), 2) AS average, COUNT(*) AS students
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
GROUP BY c.title
ORDER BY average DESC;
