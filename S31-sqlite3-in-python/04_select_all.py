'''Reading data.

    fetchone()   -> one row, or None
    fetchall()   -> every remaining row, in a list
    fetchmany(n) -> n rows
    looping over the cursor -> one row at a time, without loading everything
'''

import sqlite3


def show_table(table_name: str) -> None:
    '''Print the content of one table.

    The table NAME cannot be a '?' parameter (parameters are only for values),
    so this function must only ever be called with a name WE choose, never with
    something typed by a user.
    '''
    print(f'\n--- {table_name} ---')

    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM {table_name}')

    # cursor.description holds the column names.
    columns = [column[0] for column in cursor.description]
    print(' | '.join(columns))

    for row in cursor:               # looping is the memory-friendly way
        print(row)

    print('-' * 40)
    conn.close()


def main() -> None:
    for table in ('students', 'teachers', 'courses', 'enrollments'):
        show_table(table)


if __name__ == '__main__':
    main()
