'''ON DELETE CASCADE seen from Python.

Deleting a student also deletes their enrolments - but ONLY because
PRAGMA foreign_keys = ON was executed on this connection.
Comment that line out and run the program again to see the difference.
'''

import sqlite3


def count_enrollments(cursor: sqlite3.Cursor, student_id: int) -> int:
    'Return how many enrolments a student has.'
    cursor.execute('SELECT COUNT(*) FROM enrollments WHERE student_id = ?',
                   (student_id,))
    return cursor.fetchone()[0]


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')       # <- try removing this line
    cursor = conn.cursor()

    cursor.execute('SELECT student_id FROM students WHERE email = ?',
                   ('maryam@kadoosedu.ir',))
    row = cursor.fetchone()

    if row is None:
        print('That student does not exist (any more).')
        conn.close()
        return

    student_id = row[0]
    print('enrolments before:', count_enrollments(cursor, student_id))

    cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
    conn.commit()

    print('enrolments after: ', count_enrollments(cursor, student_id))

    conn.close()


if __name__ == '__main__':
    main()
