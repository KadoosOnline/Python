-- A student follows several courses, and a course has several students:
-- this is a MANY-TO-MANY relation, and it always needs a third table.
DROP TABLE IF EXISTS enrollments;

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id    INTEGER,
    course_id     INTEGER,
    grade         REAL,
    enroll_date   DATE DEFAULT CURRENT_DATE,

    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id),

    -- A student cannot enrol twice in the same course.
    UNIQUE (student_id, course_id)
);

-- Look at the real ids first: after the DELETE of file 12 they are not 1,2,3!
SELECT student_id, first_name FROM students;
SELECT course_id, title FROM courses;

-- Instead of typing the ids by hand, let SQL look them up.
INSERT INTO enrollments (student_id, course_id, grade)
SELECT s.student_id, c.course_id, 18.5
FROM students s, courses c
WHERE s.first_name = 'سارا' AND c.title = 'پایگاه داده';

INSERT INTO enrollments (student_id, course_id, grade)
SELECT s.student_id, c.course_id, 15.0
FROM students s, courses c
WHERE s.first_name = 'سارا' AND c.title = 'ریاضی عمومی';

INSERT INTO enrollments (student_id, course_id, grade)
SELECT s.student_id, c.course_id, 20.0
FROM students s, courses c
WHERE s.first_name = 'رضا' AND c.title = 'پایگاه داده';

SELECT * FROM enrollments;
