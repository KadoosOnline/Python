-- Another answer to the same question.
-- A course whose teacher leaves is still a course: we only want to empty
-- the reference, not to delete the course.
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT NOT NULL,
    unit       INTEGER CHECK (unit > 0 AND unit < 5),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET NULL
);

INSERT INTO courses (title, unit, teacher_id) VALUES
('پایگاه داده', 3, 1),
('ریاضی عمومی', 3, 2),
('برنامه نویسی پیشرفته', 4, 1);

SELECT * FROM courses;

-- Delete the teacher number 1: their courses stay, with teacher_id = NULL.
DELETE FROM teachers WHERE teacher_id = 1;

SELECT * FROM courses;

-- The three possible answers are therefore:
--   ON DELETE CASCADE    delete the children too
--   ON DELETE SET NULL   keep them, empty the reference
--   (nothing)            refuse the deletion (RESTRICT), the default
