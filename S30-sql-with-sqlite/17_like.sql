-- LIKE searches a pattern. '%' means "any number of characters".
SELECT * FROM students WHERE first_name LIKE 'س%';    -- starts with س
SELECT * FROM students WHERE last_name  LIKE '%ی';    -- ends with ی
SELECT * FROM students WHERE last_name  LIKE '%می%';  -- contains می
