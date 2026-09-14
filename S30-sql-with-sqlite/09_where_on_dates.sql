-- Dates are stored as 'YYYY-MM-DD', which is exactly why that format is used:
-- comparing the TEXT gives the right chronological order.
SELECT first_name, last_name, birth_date
FROM students
WHERE birth_date > '2000-01-01';
