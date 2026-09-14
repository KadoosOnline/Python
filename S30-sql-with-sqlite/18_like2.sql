-- '_' means "exactly one character".
-- '__ر%' = two characters, then ر, then anything.
SELECT * FROM students WHERE first_name LIKE '__ر%';

-- '____' matches every name of exactly four characters.
SELECT * FROM students WHERE first_name LIKE '____';
