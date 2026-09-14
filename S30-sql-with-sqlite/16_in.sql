-- IN tests a list of values.
SELECT * FROM students
WHERE first_name IN ('علی', 'رضا');

-- The long version with OR - IN is shorter and easier to read.
SELECT * FROM students
WHERE first_name = 'علی' OR first_name = 'رضا';

-- NOT IN is the opposite.
SELECT * FROM students
WHERE first_name NOT IN ('علی', 'رضا');
