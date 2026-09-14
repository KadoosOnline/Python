-- WHERE filters the ROWS (before grouping).
-- HAVING filters the GROUPS (after grouping).
SELECT teacher_id, COUNT(*) AS number_of_courses
FROM courses
GROUP BY teacher_id
HAVING COUNT(*) > 1;

-- The two can be used together.
SELECT teacher_id, COUNT(*) AS number_of_courses
FROM courses
WHERE unit >= 3                 -- keep only the courses of 3 units or more
GROUP BY teacher_id
HAVING COUNT(*) >= 1            -- then keep only the teachers who have some
ORDER BY number_of_courses DESC;
