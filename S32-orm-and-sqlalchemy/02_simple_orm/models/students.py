'''The Student model: CRUD operations on the students table.'''

from .base import Model


class Student(Model):
    'One row of the students table.'

    table = 'students'
    pk = 'student_id'
    columns = ['first_name', 'last_name', 'email']

    SCHEMA = '''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name  TEXT NOT NULL,
            email      TEXT UNIQUE NOT NULL
        );
    '''

    def __init__(self,
                 email: str,
                 first_name: str = 'New',
                 last_name: str = 'Student') -> None:
        # Creating the OBJECT does not touch the database; save() does.
        # That separation is what the original version was missing.
        self.student_id: int | None = None
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} <{self.email}>'

    def __repr__(self) -> str:
        return f'Student({self.email!r})'

    @property
    def full_name(self) -> str:
        'The two names together.'
        return f'{self.first_name} {self.last_name}'
