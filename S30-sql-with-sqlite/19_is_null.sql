-- NULL is not a value, so it can never be compared with '='.
-- This query returns NOTHING, even when a phone number is missing:
SELECT * FROM students WHERE phone = NULL;

-- The correct way:
SELECT * FROM students WHERE phone IS NULL;
SELECT * FROM students WHERE phone IS NOT NULL;

-- COALESCE replaces NULL with a value of our choice.
SELECT first_name, COALESCE(phone, 'no phone') AS phone FROM students;
