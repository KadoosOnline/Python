DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title     TEXT NOT NULL,

    -- CHECK: a rule the value must respect, tested at every INSERT/UPDATE.
    unit      INTEGER CHECK (unit > 0 AND unit < 5),

    -- A FOREIGN KEY says: this column must contain a teacher_id that really
    -- exists in the teachers table. This is what makes the data "relational".
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- IMPORTANT: SQLite ignores foreign keys unless you switch them on,
-- once per connection:
PRAGMA foreign_keys = ON;
