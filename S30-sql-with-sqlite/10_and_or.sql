-- AND: both conditions must be true.
SELECT first_name, last_name, birth_date FROM students
WHERE first_name = 'علی' AND last_name = 'علوی';

-- OR: at least one of them.
SELECT * FROM students
WHERE first_name = 'علی' OR first_name = 'رضا';

-- NOT reverses a condition.
SELECT * FROM students WHERE NOT first_name = 'علی';

-- Use parentheses whenever AND and OR are mixed: AND binds tighter than OR.
SELECT * FROM students
WHERE (first_name = 'علی' OR first_name = 'رضا')
  AND birth_date > '1999-01-01';
