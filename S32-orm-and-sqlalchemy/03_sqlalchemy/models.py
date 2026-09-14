'''SQLAlchemy ORM models for a small school.

One class per table. SQLAlchemy reads the type hints (`Mapped[...]`) and the
`mapped_column(...)` calls to know how to build the table.

The relations:
    Teacher 1 --- * Course        (a teacher gives several courses)
    Student 1 --- * Enrollment * --- 1 Course
                  (Enrollment is the many-to-many table, plus a grade)
'''

from typing import List, Optional

from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    'Every model inherits from this; it collects the metadata of the tables.'


class Teacher(Base):
    __tablename__ = 'teacher'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # One teacher -> many courses.
    # back_populates links the two sides so that both stay in agreement.
    courses: Mapped[List['Course']] = relationship(
        back_populates='teacher',
        cascade='all, delete-orphan',   # deleting a teacher deletes the courses
        passive_deletes=True,           # let the DATABASE do the cascade
    )

    def __repr__(self) -> str:
        return f'<Teacher(id={self.id}, name={self.name!r})>'


class Course(Base):
    __tablename__ = 'course'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)

    # The foreign key column itself ...
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey('teacher.id', ondelete='CASCADE'), nullable=False
    )
    # ... and the Python side of the relation.
    teacher: Mapped['Teacher'] = relationship(back_populates='courses')

    enrollments: Mapped[List['Enrollment']] = relationship(
        back_populates='course',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f'<Course(id={self.id}, title={self.title!r})>'


class Student(Base):
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    enrollments: Mapped[List['Enrollment']] = relationship(
        back_populates='student',
        cascade='all, delete-orphan',
        passive_deletes=True,
    )

    def __repr__(self) -> str:
        return f'<Student(id={self.id}, name={self.name!r})>'


class Enrollment(Base):
    '''The link between a student and a course.

    It is a table of its own because it carries extra data: the grade.
    '''

    __tablename__ = 'enrollment'

    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    student_id: Mapped[int] = mapped_column(
        ForeignKey('student.id', ondelete='CASCADE'), nullable=False
    )
    course_id: Mapped[int] = mapped_column(
        ForeignKey('course.id', ondelete='CASCADE'), nullable=False
    )

    student: Mapped['Student'] = relationship(back_populates='enrollments')
    course: Mapped['Course'] = relationship(back_populates='enrollments')

    def __repr__(self) -> str:
        return (f'<Enrollment(student_id={self.student_id}, '
                f'course_id={self.course_id}, grade={self.grade})>')
