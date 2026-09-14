'''Inserting data.

NEVER build the SQL with an f-string or with '+': always use '?' parameters.
The values are then sent apart from the query and can never become SQL code.
'''

import sqlite3


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    # executemany() runs the same query once per tuple of the list.
    students_data = [
        ('Ali', 'Rezaei', 'alireza@kadoosedu.ir'),
        ('Maryam', 'Ahmadi', 'maryam@kadoosedu.ir'),
        ('Sara', 'Karimi', 'sara@kadoosedu.ir'),
        ('Zahra', 'Mousavi', 'zahra@kadoosedu.ir'),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO students (first_name, last_name, email) '
        'VALUES (?, ?, ?)',
        students_data,
    )

    teachers_data = [
        ('Mohammad', 'Mohammadi', 'Computer'),
        ('Norouz', 'Norouzi', 'Language'),
        ('Ghasem', 'Ghasemi', 'Computer'),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO teachers (first_name, last_name, department) '
        'VALUES (?, ?, ?)',
        teachers_data,
    )
    conn.commit()

    # We must not guess the ids: we ask the database for them.
    # NOTE: the comma in ('Mohammadi',) is what makes it a TUPLE.
    cursor.execute('SELECT teacher_id FROM teachers WHERE last_name = ?',
                   ('Mohammadi',))
    teacher1 = cursor.fetchone()[0]

    cursor.execute('SELECT teacher_id FROM teachers WHERE last_name = ?',
                   ('Norouzi',))
    teacher2 = cursor.fetchone()[0]

    cursor.execute('SELECT teacher_id FROM teachers WHERE last_name = ?',
                   ('Ghasemi',))
    teacher3 = cursor.fetchone()[0]

    courses_data = [
        ('Python Programming', teacher1, 3),
        ('Linux', teacher2, 3),
        ('C# Programming', teacher3, 2),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO courses (title, teacher_id, credit) '
        'VALUES (?, ?, ?)',
        courses_data,
    )
    conn.commit()

    # A single insert, and the id it produced.
    cursor.execute(
        'INSERT OR IGNORE INTO students (first_name, last_name, email) '
        'VALUES (?, ?, ?)',
        ('Omid', 'Shabani', 'omid@kadoosedu.ir'),
    )
    print('The new student got the id', cursor.lastrowid)
    conn.commit()

    # Enrolments: again we look the ids up instead of writing them by hand.
    def student_id(email: str) -> int:
        cursor.execute('SELECT student_id FROM students WHERE email = ?',
                       (email,))
        return cursor.fetchone()[0]

    def course_id(title: str) -> int:
        cursor.execute('SELECT course_id FROM courses WHERE title = ?',
                       (title,))
        return cursor.fetchone()[0]

    s1 = student_id('alireza@kadoosedu.ir')
    s2 = student_id('maryam@kadoosedu.ir')
    c1 = course_id('Python Programming')
    c2 = course_id('C# Programming')

    enrollments_data = [
        (s1, c1, 18.5),
        (s1, c2, 15.0),
        (s2, c1, 19.0),
        (s2, c2, 17.5),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO enrollments (student_id, course_id, grade) '
        'VALUES (?, ?, ?)',
        enrollments_data,
    )
    conn.commit()
    conn.close()

    print('The data was inserted.')


if __name__ == '__main__':
    main()
