-- ASC = ascending (the default), DESC = descending.
SELECT * FROM students ORDER BY last_name ASC;
SELECT * FROM students ORDER BY last_name DESC;

-- Sorting on several columns: first by last name, then by first name.
SELECT * FROM students ORDER BY last_name ASC, first_name ASC;
