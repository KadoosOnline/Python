'''Creating the whole schema in one go.

executescript() runs SEVERAL statements separated by ';'.
It is the right tool for a schema; for a normal query use execute().
'''

import sqlite3

SCHEMA = '''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name  TEXT NOT NULL,
        email      TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name  TEXT NOT NULL,
        department TEXT
    );

    CREATE TABLE IF NOT EXISTS courses (
        course_id  INTEGER PRIMARY KEY AUTOINCREMENT,
        title      TEXT NOT NULL,
        teacher_id INTEGER,
        credit     INTEGER DEFAULT 3,
        FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
            ON DELETE SET NULL ON UPDATE CASCADE
    );

    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id      INTEGER NOT NULL,
        course_id       INTEGER NOT NULL,
        grade           REAL,
        enrollment_date TEXT DEFAULT (date('now')),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
            ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
            ON DELETE CASCADE ON UPDATE CASCADE,
        UNIQUE (student_id, course_id)
    );
'''


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    cursor.executescript(SCHEMA)

    # Nothing is really written until commit() is called.
    conn.commit()
    conn.close()

    print('The tables were created.')


if __name__ == '__main__':
    main()
