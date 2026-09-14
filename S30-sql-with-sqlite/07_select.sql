-- '*' means "every column".
SELECT * FROM students;

-- In real code, ask only for the columns you need: it is faster and it does
-- not break when a column is added later.
SELECT first_name, last_name FROM students;

-- AS renames a column in the result (only in the result).
SELECT first_name AS name, last_name AS family FROM students;

-- '||' glues two texts together in SQLite.
SELECT first_name || ' ' || last_name AS full_name FROM students;
