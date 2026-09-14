-- DROP TABLE removes the table completely (data included).
-- "IF EXISTS" avoids an error the first time the script is run.
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    -- PRIMARY KEY: the column that identifies a row uniquely.
    -- AUTOINCREMENT: SQLite fills it in for us, 1, 2, 3, ...
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- NOT NULL: this column can never be empty.
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,

    -- SQLite has no real DATE type; dates are stored as TEXT 'YYYY-MM-DD'.
    birth_date DATE,

    -- UNIQUE: two students can never have the same phone number.
    phone TEXT UNIQUE
);
