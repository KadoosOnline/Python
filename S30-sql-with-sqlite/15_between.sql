-- BETWEEN a AND b: both limits are INCLUDED.
SELECT * FROM students
WHERE birth_date BETWEEN '2000-01-01' AND '2002-12-31';

-- Exactly the same thing, written by hand:
SELECT * FROM students
WHERE birth_date >= '2000-01-01' AND birth_date <= '2002-12-31';
