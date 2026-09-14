'''Why an ORM? The same job written twice.

Run this file to see both versions produce the same result.
'''

import sqlite3

DB = 'demo.db'


# ---------------------------------------------------------------- raw SQL ---
def with_raw_sql() -> None:
    '''The way of session 31.

    Problems:
      * the SQL is spread all over the program;
      * a row is a tuple, so we read it with row[2] and nobody knows what
        column 2 is;
      * every table needs its own copy-pasted insert/select/update/delete;
      * changing a column name means hunting through the whole project.
    '''
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name  TEXT NOT NULL,
                        email      TEXT UNIQUE NOT NULL)''')

    cursor.execute(
        'INSERT OR IGNORE INTO students (first_name, last_name, email) '
        'VALUES (?, ?, ?)',
        ('Ali', 'Rezaei', 'ali@kadoosedu.ir'),
    )
    conn.commit()

    cursor.execute('SELECT * FROM students WHERE email = ?',
                   ('ali@kadoosedu.ir',))
    row = cursor.fetchone()
    print('raw SQL  ->', row, '| the name is', row[1])   # row[1]... which one?

    conn.close()


# -------------------------------------------------------------- with an ORM --
def with_an_orm() -> None:
    '''The same thing, with the tiny ORM of folder 02.

    The SQL lives in ONE place (the model), and the rest of the program only
    ever talks about objects and attributes.
    '''
    import sys
    sys.path.insert(0, '../02_simple_orm')

    from models import Student           # noqa: E402  (import after sys.path)

    Student.create_table()

    student = Student.get_or_create(
        email='ali@kadoosedu.ir',
        first_name='Ali',
        last_name='Rezaei',
    )
    print('ORM      ->', student, '| the name is', student.first_name)


def main() -> None:
    with_raw_sql()
    try:
        with_an_orm()
    except ImportError:
        print('(run 02_simple_orm first, or start this file from its folder)')


if __name__ == '__main__':
    main()
