-- WHY THIS FILE EXISTS
--
-- Imagine a Python program that builds its SQL by gluing strings together:
--
--     name = input('name: ')
--     cursor.execute("SELECT * FROM students WHERE first_name = '" + name + "'")
--
-- If the user types:      ' OR '1'='1
-- the database receives:  SELECT * FROM students WHERE first_name = '' OR '1'='1'
-- ... and returns EVERY student.
--
-- If the user types:      '; DROP TABLE students; --
-- the database receives two statements, and the second one destroys the table:

INSERT INTO students (first_name, last_name, birth_date, phone)
VALUES ('علی', 'علوی', '2000-01-15', '09121111111'); DROP TABLE IF EXISTS students; --');

-- THE FIX (session 31): never glue values into the SQL text.
-- Use a parameterised query and let the driver do the escaping:
--
--     cursor.execute('SELECT * FROM students WHERE first_name = ?', (name,))
--
-- The '?' is not a text substitution: the value can never become SQL code.
