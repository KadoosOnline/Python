-- DELETE removes rows. Here again, the WHERE is what protects the data.
-- Tip: run the same condition as a SELECT first, to see what will disappear.
SELECT * FROM students WHERE phone IS NULL;

DELETE FROM students WHERE phone IS NULL;

-- "DELETE FROM students;" without a WHERE empties the whole table.
