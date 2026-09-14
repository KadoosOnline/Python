'''A JOIN written from Python.

The SQL is exactly the SQL of session 30; only the way we run it changes.
A triple-quoted string keeps a long query readable.
'''

import sqlite3

QUERY = '''
    SELECT s.first_name || ' ' || s.last_name AS student,
           c.title                            AS course,
           e.grade                            AS grade
    FROM enrollments e
    JOIN students s ON e.student_id = s.student_id
    JOIN courses  c ON e.course_id  = c.course_id
    ORDER BY student, course
'''


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    cursor.execute(QUERY)

    print('\nRecords (student - course - grade):')
    for student, course, grade in cursor.fetchall():
        print(f'{student:<20}{course:<25}{grade}')

    conn.close()


if __name__ == '__main__':
    main()
