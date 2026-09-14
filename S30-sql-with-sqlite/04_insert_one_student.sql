-- INSERT adds one row.
-- Always name the columns: the query then keeps working when the table changes.
-- student_id is not given, because AUTOINCREMENT fills it in.
INSERT INTO students (first_name, last_name, birth_date, phone)
VALUES ('علی', 'علوی', '2000-01-15', '09121111111');
