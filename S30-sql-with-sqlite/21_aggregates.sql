-- An aggregate function turns many rows into ONE value.
SELECT COUNT(*) AS number_of_students FROM students;

-- COUNT(column) ignores the NULLs - compare the two numbers:
SELECT COUNT(*) AS all_rows, COUNT(phone) AS rows_with_a_phone FROM students;

SELECT MIN(birth_date) AS oldest, MAX(birth_date) AS youngest FROM students;

SELECT SUM(unit) AS total_units, AVG(unit) AS average_units FROM courses;

-- ROUND makes the result readable.
SELECT ROUND(AVG(unit), 2) AS average_units FROM courses;
