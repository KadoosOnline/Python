-- LIMIT returns at most N rows.
SELECT * FROM students LIMIT 2;

-- OFFSET skips the first rows: this is how pagination is done.
SELECT * FROM students LIMIT 2 OFFSET 2;   -- rows 3 and 4

-- LIMIT together with ORDER BY answers "the top N".
SELECT * FROM students ORDER BY birth_date DESC LIMIT 1;   -- the youngest
