-- Add a course without a teacher, so that the difference becomes visible.
INSERT INTO courses (title, unit, teacher_id) VALUES ('زبان تخصصی', 2, NULL);

-- INNER JOIN: the course without a teacher DISAPPEARS from the result.
SELECT c.title, t.teacher_name
FROM courses c
INNER JOIN teachers t ON c.teacher_id = t.teacher_id;

-- LEFT JOIN: every row of the LEFT table is kept; the missing right side
-- becomes NULL.
SELECT c.title, COALESCE(t.teacher_name, 'no teacher yet') AS teacher
FROM courses c
LEFT JOIN teachers t ON c.teacher_id = t.teacher_id;
