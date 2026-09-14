'''fetchone() returns ONE row, or None when nothing matched.

Forgetting to test for None is the most common bug of this session:
"TypeError: 'NoneType' object is not subscriptable".
'''

import sqlite3


def find_student(email: str) -> tuple | None:
    'Return the row of a student, or None.'
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
    student = cursor.fetchone()

    conn.close()
    return student


def main() -> None:
    for email in ('zahra@kadoosedu.ir', 'nobody@kadoosedu.ir'):
        student = find_student(email)

        if student:
            print('Student found:', student)
        else:
            print(f'No student with the email {email}.')


if __name__ == '__main__':
    main()
