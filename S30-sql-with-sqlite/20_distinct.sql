-- DISTINCT removes the duplicated rows from the RESULT.
SELECT DISTINCT department FROM teachers;

-- Without it, one line per teacher would be returned.
SELECT department FROM teachers;
