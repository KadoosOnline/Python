'''A LEFT JOIN: the courses without a teacher stay in the result.'''

import sqlite3

QUERY = '''
    SELECT c.title                             AS course,
           t.first_name || ' ' || t.last_name  AS teacher,
           c.credit                            AS credit
    FROM courses c
    LEFT JOIN teachers t ON c.teacher_id = t.teacher_id
    ORDER BY c.title
'''


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    cursor.execute(QUERY)

    print('\nCourses and teachers:')
    for course, teacher, credit in cursor.fetchall():
        # A LEFT JOIN gives None (SQL NULL) when there is no teacher.
        print(f'{course:<25}{teacher or "(no teacher)":<25}{credit}')

    conn.close()


if __name__ == '__main__':
    main()
