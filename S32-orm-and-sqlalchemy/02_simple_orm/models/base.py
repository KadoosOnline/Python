'''The shared part of every model.

This is the heart of the tiny ORM: the connection handling and the generic
CRUD helpers live here ONCE, and every model inherits them.
'''

import sqlite3

DATABASE_PATH = 'database.db'


class Model:
    '''Base class of every model.

    A subclass only has to define:
        table       the name of the table
        pk          the name of its primary key column
        columns     the other columns, in order
        SCHEMA      the CREATE TABLE statement
    '''

    table: str = ''
    pk: str = 'id'
    columns: list[str] = []
    SCHEMA: str = ''

    # ------------------------------------------------------------ database --
    @classmethod
    def connect(cls) -> sqlite3.Connection:
        'Return a configured connection. Everything goes through here.'
        conn = sqlite3.connect(DATABASE_PATH)
        conn.execute('PRAGMA foreign_keys = ON')
        conn.row_factory = sqlite3.Row      # rows readable by column name
        return conn

    @classmethod
    def create_table(cls) -> None:
        'Create the table of this model.'
        with cls.connect() as conn:
            conn.executescript(cls.SCHEMA)

    # --------------------------------------------------------------- read ---
    @classmethod
    def all(cls) -> list['Model']:
        'Return every row as a list of objects.'
        conn = cls.connect()
        try:
            rows = conn.execute(
                f'SELECT * FROM {cls.table} ORDER BY {cls.pk}'
            ).fetchall()
        finally:
            conn.close()
        return [cls.from_row(row) for row in rows]

    @classmethod
    def get(cls, **where) -> 'Model | None':
        '''Return the first row matching the given columns, or None.

        Example:  Student.get(email='ali@kadoosedu.ir')
        '''
        # The column NAMES come from our own code, the VALUES from the caller,
        # so only the values become '?' parameters.
        conditions = ' AND '.join(f'{column} = ?' for column in where)
        values = tuple(where.values())

        conn = cls.connect()
        try:
            row = conn.execute(
                f'SELECT * FROM {cls.table} WHERE {conditions}', values
            ).fetchone()
        finally:
            conn.close()

        return cls.from_row(row) if row else None

    # -------------------------------------------------------------- write ---
    def save(self) -> None:
        'Insert this object, and store the id it received.'
        columns = ', '.join(self.columns)
        placeholders = ', '.join('?' for _ in self.columns)
        values = tuple(getattr(self, column) for column in self.columns)

        with self.connect() as conn:
            cursor = conn.execute(
                f'INSERT INTO {self.table} ({columns}) VALUES ({placeholders})',
                values,
            )
            setattr(self, self.pk, cursor.lastrowid)

    def update(self, **changes) -> None:
        '''Change some columns of this object AND of its row.

        Example:  student.update(first_name='Alireza')
        '''
        for column in changes:
            if column not in self.columns:
                raise ValueError(f'unknown column: {column}')

        assignments = ', '.join(f'{column} = ?' for column in changes)
        values = tuple(changes.values()) + (getattr(self, self.pk),)

        with self.connect() as conn:
            conn.execute(
                f'UPDATE {self.table} SET {assignments} WHERE {self.pk} = ?',
                values,
            )

        # Keep the object and the row in agreement.
        for column, value in changes.items():
            setattr(self, column, value)

    def delete(self) -> None:
        'Delete the row of this object.'
        with self.connect() as conn:
            conn.execute(
                f'DELETE FROM {self.table} WHERE {self.pk} = ?',
                (getattr(self, self.pk),),
            )

    @classmethod
    def get_or_create(cls, **fields) -> 'Model':
        '''Return the existing object, or create it.

        The lookup uses the first column of 'fields'.
        '''
        key = next(iter(fields))
        existing = cls.get(**{key: fields[key]})
        if existing is not None:
            return existing

        obj = cls(**fields)
        obj.save()
        return obj

    # -------------------------------------------------------------- helper --
    @classmethod
    def from_row(cls, row: sqlite3.Row) -> 'Model':
        'Build an object out of a database row.'
        obj = cls.__new__(cls)                 # create it without __init__
        for key in row.keys():
            setattr(obj, key, row[key])
        return obj
