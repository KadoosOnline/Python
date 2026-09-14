-- GROUP BY splits the rows into groups and applies the aggregate to each group.
-- "How many teachers per department?"
SELECT department, COUNT(*) AS number_of_teachers
FROM teachers
GROUP BY department;

-- "How many courses does each teacher give?"
SELECT teacher_id, COUNT(*) AS number_of_courses, SUM(unit) AS total_units
FROM courses
GROUP BY teacher_id;

-- Rule: every column of the SELECT must either be in the GROUP BY
-- or be inside an aggregate function.
