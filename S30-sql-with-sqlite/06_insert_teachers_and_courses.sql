-- The teachers must exist BEFORE the courses that point at them.
INSERT INTO teachers (teacher_name, department) VALUES
('دکتر محمدی', 'کامپیوتر'),
('دکتر رضایی', 'ریاضی');

-- AUTOINCREMENT gave teacher_id = 1 to the first one and 2 to the second.
INSERT INTO courses (title, unit, teacher_id) VALUES
('پایگاه داده', 3, 1),
('ریاضی عمومی', 3, 2),
('برنامه نویسی پیشرفته', 4, 1);

-- Check what was inserted:
SELECT * FROM teachers;
SELECT * FROM courses;
