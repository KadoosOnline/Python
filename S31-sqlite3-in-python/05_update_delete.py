'''UPDATE and DELETE from Python.

cursor.rowcount tells us how many rows were really affected - use it to know
whether the WHERE matched anything.
'''

import sqlite3


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE students SET email = ? WHERE email = ?',
        ('new_alireza@kadoosedu.ir', 'alireza@kadoosedu.ir'),
    )
    print('rows updated:', cursor.rowcount)
    conn.commit()

    cursor.execute(
        'DELETE FROM enrollments WHERE grade < ?',
        (16,),
    )
    print('rows deleted:', cursor.rowcount)
    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()
