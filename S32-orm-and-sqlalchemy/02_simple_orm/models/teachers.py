'''The Teacher model.

Notice how little code a new model needs: everything else is inherited.
'''

from .base import Model


class Teacher(Model):
    'One row of the teachers table.'

    table = 'teachers'
    pk = 'teacher_id'
    columns = ['first_name', 'last_name', 'department']

    SCHEMA = '''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name  TEXT NOT NULL,
            department TEXT DEFAULT 'General'
        );
    '''

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 department: str = 'General') -> None:
        self.teacher_id: int | None = None
        self.first_name = first_name
        self.last_name = last_name
        self.department = department

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.department})'
