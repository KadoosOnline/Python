'''By default a row is a TUPLE, so we read it with row[0], row[1]...
That is short but unreadable, and it breaks when a column is added.

sqlite3.Row lets us read a row by COLUMN NAME.
'''

import sqlite3


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')

    # Default: tuples.
    cursor = conn.cursor()
    cursor.execute('SELECT student_id, first_name, email FROM students')
    for row in cursor.fetchall()[:3]:
        print(row, '->', row[1])

    print('---')

    # With sqlite3.Row: access by name (and still by index).
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT student_id, first_name, email FROM students')
    for row in cursor.fetchall()[:3]:
        print(row['first_name'], row['email'], '| id =', row['student_id'])

    print('---')

    # A row can be turned into a real dictionary, ready for JSON.
    cursor.execute('SELECT * FROM students LIMIT 2')
    students = [dict(row) for row in cursor.fetchall()]
    print(students)

    conn.close()


if __name__ == '__main__':
    main()
