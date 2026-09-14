-- Several rows in a single INSERT: much faster than several statements.
-- The last student has NULL as a phone number: "we do not know it".
-- NULL is not 0 and not an empty string - it means "no value".
INSERT INTO students (first_name, last_name, birth_date, phone) VALUES
('سارا', 'احمدی', '2001-05-22', '09122222222'),
('رضا',  'کریمی', '1999-11-02', '09123333333'),
('مریم', 'حسینی', '2002-09-10', NULL);
