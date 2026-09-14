'''SQL injection: the mistake, the attack, and the fix.

Run it and type   ' OR '1'='1   at the prompt.
'''

import sqlite3


def unsafe_search(cursor: sqlite3.Cursor, name: str) -> list:
    'NEVER DO THIS: the value is glued into the SQL text.'
    query = f"SELECT * FROM students WHERE first_name = '{name}'"
    print('  SQL sent:', query)
    cursor.execute(query)
    return cursor.fetchall()


def safe_search(cursor: sqlite3.Cursor, name: str) -> list:
    'The right way: the value travels apart from the query.'
    cursor.execute('SELECT * FROM students WHERE first_name = ?', (name,))
    return cursor.fetchall()


def main() -> None:
    conn = sqlite3.connect('database.db')
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    name = input("First name to search (try:  ' OR '1'='1 ): ")

    print('\n--- unsafe version ---')
    rows = unsafe_search(cursor, name)
    print(f'  {len(rows)} row(s) returned')

    print('\n--- safe version ---')
    rows = safe_search(cursor, name)
    print(f'  {len(rows)} row(s) returned')

    print('''
The unsafe version returned every student, because the text typed by the user
became part of the query. With '?', the same text stays a plain value and
matches nothing.

Remember: '?' is NOT a string substitution. Never write
    cursor.execute('... WHERE name = ?' % name)          # wrong
    cursor.execute(f'... WHERE name = {name}')           # wrong
    cursor.execute('... WHERE name = ?', (name,))        # right
''')

    conn.close()


if __name__ == '__main__':
    main()
