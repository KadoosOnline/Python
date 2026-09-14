-- UPDATE changes existing rows.
-- NEVER forget the WHERE: without it, EVERY row is changed.
UPDATE students
SET phone = '09120000000'
WHERE first_name = 'علی' AND last_name = 'علوی';

-- Several columns at once.
UPDATE students
SET phone = '09129999999', birth_date = '2000-02-20'
WHERE student_id = 1;

SELECT * FROM students;
