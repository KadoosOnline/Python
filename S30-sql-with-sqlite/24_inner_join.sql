-- A JOIN reads two tables at once, matching them on a common column.
-- INNER JOIN keeps only the rows that HAVE a match on both sides.
SELECT
    courses.title        AS 'نام درس',
    teachers.teacher_name AS 'نام استاد',
    courses.unit         AS 'تعداد واحد'
FROM courses
INNER JOIN teachers ON courses.teacher_id = teachers.teacher_id;

-- Table aliases make a long query much shorter.
SELECT c.title, t.teacher_name, c.unit
FROM courses c
INNER JOIN teachers t ON c.teacher_id = t.teacher_id
ORDER BY t.teacher_name;
