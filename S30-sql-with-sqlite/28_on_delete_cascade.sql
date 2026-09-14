-- What must happen to the enrolments when a student is deleted?
-- ON DELETE CASCADE: they are deleted too. That is what we want here,
-- because an enrolment has no meaning without its student.
PRAGMA foreign_keys = ON;      -- WITHOUT THIS LINE SQLITE IGNORES THE RULE!

DROP TABLE IF EXISTS enrollments;

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER,
    course_id     INTEGER,
    grade         REAL,
    enroll_date   DATE DEFAULT CURRENT_DATE,

    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)  ON DELETE CASCADE
);

INSERT INTO enrollments (student_id, course_id, grade)
SELECT s.student_id, c.course_id, 18.5
FROM students s, courses c
WHERE s.first_name = 'سارا' AND c.title = 'پایگاه داده';

INSERT INTO enrollments (student_id, course_id, grade)
SELECT s.student_id, c.course_id, 15.0
FROM students s, courses c
WHERE s.first_name = 'سارا' AND c.title = 'ریاضی عمومی';

SELECT * FROM enrollments;

-- Now delete the course 'ریاضی عمومی' and look at the enrolments again:
-- the matching row disappeared by itself.
DELETE FROM courses WHERE title = 'ریاضی عمومی';

SELECT * FROM enrollments;
