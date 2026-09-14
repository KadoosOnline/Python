'''Opening a connection to a SQLite database.

sqlite3 is part of the standard library - there is nothing to install.
connect() CREATES the file when it does not exist yet.
'''

import sqlite3


def main() -> None:
    # The file is created next to the program, in the current folder.
    conn = sqlite3.connect('database.db')

    # SQLite ignores the foreign keys unless we switch them on,
    # and it forgets the setting at every new connection.
    conn.execute('PRAGMA foreign_keys = ON')

    # The cursor is the object that runs the queries and holds the results.
    cursor = conn.cursor()

    # A first query to prove that everything works.
    cursor.execute('SELECT sqlite_version()')
    print('SQLite version:', cursor.fetchone()[0])

    # Always close what you opened.
    conn.close()

    # ':memory:' creates a database that only lives in the RAM - perfect
    # for trying things out.
    temp = sqlite3.connect(':memory:')
    temp.close()


if __name__ == '__main__':
    main()
