'''A transaction: several statements that must all succeed, or none of them.

Here we create a student AND their enrolment. If the second insert fails,
we do not want the student to stay in the database alone.
'''

import sqlite3


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO students (first_name, last_name, email) '
            'VALUES (?, ?, ?)',
            ('Sara', 'Hosseini', 'sara2@kadoosedu.ir'),
        )
        new_student_id = cursor.lastrowid

        cursor.execute('SELECT course_id FROM courses WHERE title = ?',
                       ('Python Programming',))
        row = cursor.fetchone()
        if row is None:
            raise sqlite3.Error('the course does not exist')

        cursor.execute(
            'INSERT INTO enrollments (student_id, course_id, grade) '
            'VALUES (?, ?, ?)',
            (new_student_id, row[0], 20),
        )

        # commit() makes everything permanent, in one single step.
        conn.commit()
        print('Transaction done.')

    except sqlite3.Error as e:
        # rollback() undoes everything since the last commit.
        conn.rollback()
        print('Rollback happened:', e)

    finally:
        conn.close()

    # Note: "with sqlite3.connect(...) as conn:" commits on success and rolls
    # back on an exception, but it does NOT close the connection.
    with sqlite3.connect('database.db') as conn2:
        conn2.execute('PRAGMA foreign_keys = ON')
        conn2.execute('UPDATE students SET last_name = ? WHERE email = ?',
                      ('Hosseini', 'sara2@kadoosedu.ir'))
    conn2.close()


if __name__ == '__main__':
    main()
