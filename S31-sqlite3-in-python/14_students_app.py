'''A complete little application on top of sqlite3.

Everything of the session in one place: a connection helper, a schema, safe
queries, sqlite3.Row, error handling and a menu.
'''

import os
import sqlite3

DB_NAME = 'students.db'

SCHEMA = '''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name  TEXT NOT NULL,
        email      TEXT UNIQUE NOT NULL
    );
'''


def get_connection() -> sqlite3.Connection:
    '''Return a ready-to-use connection.

    Every function of the program goes through here, so the PRAGMA and the
    row_factory are never forgotten.
    '''
    conn = sqlite3.connect(DB_NAME)
    conn.execute('PRAGMA foreign_keys = ON')
    conn.row_factory = sqlite3.Row
    return conn


def create_db() -> None:
    'Create the table when it does not exist yet.'
    with get_connection() as conn:
        conn.executescript(SCHEMA)
    print('The database is ready.')


def add_student(first_name: str, last_name: str, email: str) -> bool:
    'Insert one student. Return False when the email already exists.'
    try:
        with get_connection() as conn:
            conn.execute(
                'INSERT INTO students (first_name, last_name, email) '
                'VALUES (?, ?, ?)',
                (first_name, last_name, email),
            )
        return True
    except sqlite3.IntegrityError:
        # Raised by the UNIQUE constraint on the email.
        return False


def list_students() -> list[sqlite3.Row]:
    'Return every student, sorted by last name.'
    conn = get_connection()
    try:
        return conn.execute(
            'SELECT * FROM students ORDER BY last_name'
        ).fetchall()
    finally:
        conn.close()


def find_students(text: str) -> list[sqlite3.Row]:
    'Search in the first name, the last name and the email.'
    conn = get_connection()
    try:
        pattern = f'%{text}%'          # the % go into the VALUE, not the SQL
        return conn.execute(
            'SELECT * FROM students '
            'WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ? '
            'ORDER BY last_name',
            (pattern, pattern, pattern),
        ).fetchall()
    finally:
        conn.close()


def delete_student(student_id: int) -> int:
    'Delete one student. Return how many rows were removed.'
    with get_connection() as conn:
        cursor = conn.execute('DELETE FROM students WHERE student_id = ?',
                              (student_id,))
        return cursor.rowcount


def show(rows: list[sqlite3.Row]) -> None:
    'Print a list of students as a table.'
    if not rows:
        print('  (nothing to show)')
        return

    print(f"  {'id':<5}{'First name':<15}{'Last name':<15}{'Email'}")
    for row in rows:
        print(f"  {row['student_id']:<5}{row['first_name']:<15}"
              f"{row['last_name']:<15}{row['email']}")


def main() -> None:
    create_db()

    while True:
        print('\n1) List the students')
        print('2) Add a student')
        print('3) Search')
        print('4) Delete a student')
        print('0) Exit')

        choice = input('Your choice: ').strip()

        if choice == '1':
            show(list_students())

        elif choice == '2':
            first_name = input('First name: ').strip()
            last_name = input('Last name: ').strip()
            email = input('Email: ').strip()

            if not first_name or not last_name or not email:
                print('Every field is required.')
                continue

            if add_student(first_name, last_name, email):
                print('Student added.')
            else:
                print('That email is already used.')

        elif choice == '3':
            show(find_students(input('Search for: ').strip()))

        elif choice == '4':
            answer = input('Id of the student to delete: ').strip()
            if not answer.isdigit():
                print('The id must be a number.')
                continue
            if delete_student(int(answer)):
                print('Student deleted.')
            else:
                print('No student with that id.')

        elif choice == '0':
            print('Goodbye!')
            break

        else:
            print('Unknown option.')


if __name__ == '__main__':
    main()
