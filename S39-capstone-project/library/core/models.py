'''The tables of the library, as SQLAlchemy 2.0 models.

    Member  1 --- n  Borrow  n --- 1  Book

A `Borrow` row is one loan. `return_date IS NULL` means the book is still out,
which is why we do not need a duplicated "available" flag on `Book`: the
answer is always one query away, and one fact stored in one place cannot
disagree with itself.

(Session 35 did keep such a flag, and its bug was exactly that: two places to
update, one transaction to get wrong.)
'''

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column,
                            relationship)


class Base(DeclarativeBase):
    '''The base class of every model.'''


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(160), nullable=False)
    author: Mapped[str] = mapped_column(String(120), default='')
    publisher: Mapped[str] = mapped_column(String(120), default='')
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    isbn: Mapped[str] = mapped_column(String(20), default='')
    description: Mapped[str] = mapped_column(Text, default='')
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now())

    # cascade: deleting a book deletes its loan history with it.
    borrows: Mapped[list['Borrow']] = relationship(
        back_populates='book', cascade='all, delete-orphan')

    @property
    def is_out(self) -> bool:
        '''True while one of the loans has no return date.'''
        return any(borrow.return_date is None for borrow in self.borrows)

    def __repr__(self) -> str:
        return f'<Book {self.id} {self.title!r}>'

    def __str__(self) -> str:
        # __str__ must return a STRING. The original returned `self.member`,
        # an object, which raised TypeError the first time it was printed.
        return f'{self.title} ({self.author})' if self.author else self.title


class Member(Base):
    __tablename__ = 'members'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), default='')
    email: Mapped[str] = mapped_column(String(120), default='')
    # unique=True: the DATABASE refuses a duplicate, whoever inserts it.
    card_number: Mapped[str] = mapped_column(String(30), unique=True,
                                             nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now())

    borrows: Mapped[list['Borrow']] = relationship(
        back_populates='member', cascade='all, delete-orphan')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def open_borrows(self) -> list['Borrow']:
        return [borrow for borrow in self.borrows if borrow.return_date is None]

    def __repr__(self) -> str:
        return f'<Member {self.id} {self.card_number}>'

    def __str__(self) -> str:
        return f'{self.full_name} (#{self.card_number})'


class Borrow(Base):
    __tablename__ = 'borrows'

    id: Mapped[int] = mapped_column(primary_key=True)
    # ondelete=CASCADE is the rule inside the DATABASE; the `cascade=` above
    # is the rule inside SQLAlchemy. You want both, and SQLite only obeys the
    # first one when `PRAGMA foreign_keys = ON` is set (see database.py).
    book_id: Mapped[int] = mapped_column(
        ForeignKey('books.id', ondelete='CASCADE'), nullable=False)
    member_id: Mapped[int] = mapped_column(
        ForeignKey('members.id', ondelete='CASCADE'), nullable=False)

    # datetime.now, not datetime.utcnow: utcnow is deprecated since 3.12.
    borrow_date: Mapped[datetime] = mapped_column(DateTime,
                                                  default=datetime.now)
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    return_date: Mapped[datetime | None] = mapped_column(DateTime,
                                                         nullable=True)
    note: Mapped[str] = mapped_column(Text, default='')

    book: Mapped['Book'] = relationship(back_populates='borrows')
    member: Mapped['Member'] = relationship(back_populates='borrows')

    @property
    def is_open(self) -> bool:
        return self.return_date is None

    @property
    def is_late(self) -> bool:
        '''Out, and past the due date.'''
        return self.is_open and datetime.now() > self.due_date

    @property
    def days_late(self) -> int:
        if not self.is_late:
            return 0
        return (datetime.now() - self.due_date).days

    def __repr__(self) -> str:
        return f'<Borrow {self.id} book={self.book_id} member={self.member_id}>'

    def __str__(self) -> str:
        state = 'out' if self.is_open else 'returned'
        return f'{self.book.title} -> {self.member.full_name} ({state})'
