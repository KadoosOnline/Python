'''The data layer of the library application.

Everything that talks to SQLite lives HERE, and nothing in this file imports
tkinter. That separation is the point of the example:

* `database.py` knows about tables and rows, not about windows;
* `app.py` knows about windows, not about SQL.

You could plug the very same `Database` class into a Flask site (session 38)
or into a PyQt window (session 36) without changing one line.

Notes on the SQLite details:

* `check_same_thread=False` is NOT used: we stay on the single GUI thread.
* `PRAGMA foreign_keys = ON` must be executed on EVERY connection -- SQLite
  ignores foreign keys otherwise, and `ON DELETE` clauses do nothing.
* `row_factory = sqlite3.Row` lets us write `row['title']` instead of `row[1]`.
* Every value that comes from the user goes in as a `?` parameter, never with
  an f-string (session 30: SQL injection).
'''

import sqlite3
from datetime import datetime
from pathlib import Path


# The database file sits next to this module, whatever the current folder is.
DB_PATH = Path(__file__).parent / 'library.db'

SCHEMA = '''
CREATE TABLE IF NOT EXISTS books (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    title     TEXT NOT NULL,
    author    TEXT,
    isbn      TEXT,
    year      INTEGER,
    available INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS members (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT NOT NULL,
    phone     TEXT,
    email     TEXT,
    join_date TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS borrowings (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id     INTEGER NOT NULL REFERENCES books(id)   ON DELETE CASCADE,
    member_id   INTEGER NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    borrow_date TEXT NOT NULL,
    return_date TEXT
);
'''


class Database:
    '''A thin wrapper around one SQLite connection.'''

    def __init__(self, path: Path = DB_PATH) -> None:
        self.connection = sqlite3.connect(path)
        self.connection.row_factory = sqlite3.Row
        # Without this line ON DELETE CASCADE is silently ignored.
        self.connection.execute('PRAGMA foreign_keys = ON')
        # executescript runs several statements at once.
        self.connection.executescript(SCHEMA)
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    # -- small helpers -----------------------------------------------------
    def query(self, sql: str, params: tuple = ()) -> list[sqlite3.Row]:
        '''Run a SELECT and return all the rows.'''
        return self.connection.execute(sql, params).fetchall()

    def query_one(self, sql: str, params: tuple = ()) -> sqlite3.Row | None:
        '''Run a SELECT and return the first row, or None.'''
        return self.connection.execute(sql, params).fetchone()

    def execute(self, sql: str, params: tuple = ()) -> int:
        '''Run an INSERT / UPDATE / DELETE and return the new row id.'''
        cursor = self.connection.execute(sql, params)
        self.connection.commit()
        return cursor.lastrowid

    # -- books -------------------------------------------------------------
    def list_books(self, search: str = '') -> list[sqlite3.Row]:
        if search:
            pattern = f'%{search}%'
            return self.query(
                '''SELECT * FROM books
                   WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?
                   ORDER BY title''',
                (pattern, pattern, pattern))
        return self.query('SELECT * FROM books ORDER BY title')

    def available_books(self) -> list[sqlite3.Row]:
        return self.query(
            'SELECT * FROM books WHERE available = 1 ORDER BY title')

    def add_book(self, title: str, author: str,
                 isbn: str, year: int | None) -> int:
        return self.execute(
            'INSERT INTO books (title, author, isbn, year) VALUES (?, ?, ?, ?)',
            (title, author, isbn, year))

    def update_book(self, book_id: int, title: str, author: str,
                    isbn: str, year: int | None) -> None:
        self.execute(
            'UPDATE books SET title = ?, author = ?, isbn = ?, year = ? '
            'WHERE id = ?',
            (title, author, isbn, year, book_id))

    def delete_book(self, book_id: int) -> None:
        # The cascade removes the borrowing history of that book too.
        self.execute('DELETE FROM books WHERE id = ?', (book_id,))

    # -- members -----------------------------------------------------------
    def list_members(self, search: str = '') -> list[sqlite3.Row]:
        if search:
            pattern = f'%{search}%'
            return self.query(
                '''SELECT * FROM members
                   WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?
                   ORDER BY name''',
                (pattern, pattern, pattern))
        return self.query('SELECT * FROM members ORDER BY name')

    def add_member(self, name: str, phone: str, email: str) -> int:
        return self.execute(
            'INSERT INTO members (name, phone, email, join_date) '
            'VALUES (?, ?, ?, ?)',
            (name, phone, email, datetime.now().strftime('%Y-%m-%d %H:%M')))

    def update_member(self, member_id: int, name: str,
                      phone: str, email: str) -> None:
        self.execute(
            'UPDATE members SET name = ?, phone = ?, email = ? WHERE id = ?',
            (name, phone, email, member_id))

    def delete_member(self, member_id: int) -> None:
        self.execute('DELETE FROM members WHERE id = ?', (member_id,))

    # -- borrowings --------------------------------------------------------
    def open_borrowings(self) -> list[sqlite3.Row]:
        '''The books that are out right now (no return date yet).'''
        return self.query(
            '''SELECT b.id, bo.title AS book_title, m.name AS member_name,
                      b.borrow_date
               FROM borrowings AS b
               JOIN books   AS bo ON b.book_id   = bo.id
               JOIN members AS m  ON b.member_id = m.id
               WHERE b.return_date IS NULL
               ORDER BY b.borrow_date DESC''')

    def borrow(self, book_id: int, member_id: int) -> None:
        '''Lend a book. Two statements, ONE transaction.

        If the UPDATE failed after the INSERT succeeded, the book would be
        borrowed and still marked as available. `with self.connection:`
        commits when the block ends normally and rolls back on any exception.
        '''
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        with self.connection:
            # The WHERE ... AND available = 1 makes the check atomic.
            cursor = self.connection.execute(
                'UPDATE books SET available = 0 WHERE id = ? AND available = 1',
                (book_id,))
            if cursor.rowcount == 0:
                raise ValueError('That book is not available any more.')
            self.connection.execute(
                'INSERT INTO borrowings (book_id, member_id, borrow_date) '
                'VALUES (?, ?, ?)',
                (book_id, member_id, now))

    def give_back(self, borrowing_id: int) -> None:
        '''Return a book: close the borrowing and free the book again.'''
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        with self.connection:
            row = self.connection.execute(
                'SELECT book_id FROM borrowings '
                'WHERE id = ? AND return_date IS NULL',
                (borrowing_id,)).fetchone()
            if row is None:
                raise ValueError('This borrowing is already closed.')
            self.connection.execute(
                'UPDATE borrowings SET return_date = ? WHERE id = ?',
                (now, borrowing_id))
            self.connection.execute(
                'UPDATE books SET available = 1 WHERE id = ?', (row['book_id'],))
