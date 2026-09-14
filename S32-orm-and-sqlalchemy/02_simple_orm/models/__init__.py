'''The models package: one module per table, re-exported here.'''

from .base import Model
from .students import Student
from .teachers import Teacher

__all__ = ['Model', 'Student', 'Teacher']
