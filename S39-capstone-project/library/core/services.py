'''The rules of the library.

Every operation the program can perform is a function here. The windows call
these functions and show what they return; they never write a query and they
never decide a rule.

Why that matters:

* the rule "a member may not have more than five books" is written ONCE, so
  the button and the future web page cannot disagree;
* this file can be read, reviewed and tested without starting a window;
* an operation that must not be interrupted (lending: two rows to change) is a
  single function with a single transaction.

Errors: the services raise `LibraryError` for a rule the user broke ("that
book is already out"). The GUI catches it and shows the message. A bug in the
program is a different thing and is not caught here.
'''

from datetime import datetime, timedelta

from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from .models import Book, Borrow, Member


LOAN_DAYS = 14              # how long a book may be kept
MAX_OPEN_LOANS = 5          # how many books one member may hold at once


class LibraryError(Exception):
    '''A rule of the library was broken. The message is shown to the user.'''


# -- books -----------------------------------------------------------------
def list_books(session: Session, search: str = '') -> list[Book]:
    '''Every book, newest search first. `selectinload` fetches the loans in
    one extra query instead of one per book (the "N+1 queries" problem).'''
    query = select(Book).options(selectinload(Book.borrows)).order_by(Book.title)

    if search:
        pattern = f'%{search}%'
        # The % is inside a PARAMETER: no SQL injection (session 30).
        query = query.where(or_(Book.title.ilike(pattern),
                                Book.author.ilike(pattern),
                                Book.publisher.ilike(pattern),
                                Book.isbn.ilike(pattern)))

    return list(session.scalars(query))


def available_books(session: Session) -> list[Book]:
    '''The books that are not out: no borrow row without a return date.'''
    open_book_ids = select(Borrow.book_id).where(Borrow.return_date.is_(None))
    query = (select(Book)
             .where(Book.id.not_in(open_book_ids))
             .order_by(Book.title))
    return list(session.scalars(query))


def create_book(session: Session, **fields) -> Book:
    book = Book(**fields)
    session.add(book)
    session.flush()         # gives the object its id without committing
    return book


def update_book(session: Session, book: Book, **fields) -> Book:
    for name, value in fields.items():
        setattr(book, name, value)
    return book


def delete_book(session: Session, book: Book) -> None:
    if book.is_out:
        raise LibraryError('This book is lent out. Take it back first.')
    session.delete(book)


# -- members ---------------------------------------------------------------
def list_members(session: Session, search: str = '') -> list[Member]:
    query = (select(Member)
             .options(selectinload(Member.borrows))
             .order_by(Member.last_name, Member.first_name))

    if search:
        pattern = f'%{search}%'
        query = query.where(or_(Member.first_name.ilike(pattern),
                                Member.last_name.ilike(pattern),
                                Member.card_number.ilike(pattern),
                                Member.phone.ilike(pattern)))

    return list(session.scalars(query))


def create_member(session: Session, **fields) -> Member:
    card_number = fields.get('card_number', '')
    # Check for a friendly message; the UNIQUE column is the real guarantee.
    if session.scalar(select(Member).where(Member.card_number == card_number)):
        raise LibraryError(f'Card number {card_number} is already used.')
    member = Member(**fields)
    session.add(member)
    session.flush()
    return member


def update_member(session: Session, member: Member, **fields) -> Member:
    card_number = fields.get('card_number')
    if card_number and card_number != member.card_number:
        clash = session.scalar(
            select(Member).where(Member.card_number == card_number))
        if clash is not None:
            raise LibraryError(f'Card number {card_number} is already used.')
    for name, value in fields.items():
        setattr(member, name, value)
    return member


def delete_member(session: Session, member: Member) -> None:
    if member.open_borrows:
        raise LibraryError('This member still has books. Take them back first.')
    session.delete(member)


# -- lending ---------------------------------------------------------------
def open_borrows(session: Session) -> list[Borrow]:
    '''Every book that is currently out, oldest loan first.'''
    query = (select(Borrow)
             .options(selectinload(Borrow.book), selectinload(Borrow.member))
             .where(Borrow.return_date.is_(None))
             .order_by(Borrow.due_date))
    return list(session.scalars(query))


def borrow_history(session: Session, limit: int = 200) -> list[Borrow]:
    query = (select(Borrow)
             .options(selectinload(Borrow.book), selectinload(Borrow.member))
             .order_by(Borrow.borrow_date.desc())
             .limit(limit))
    return list(session.scalars(query))


def lend_book(session: Session, book: Book, member: Member,
              days: int = LOAN_DAYS) -> Borrow:
    '''Lend one book to one member. Every rule of a loan is checked here.'''
    # Ask the database, not the object: another window may have lent it
    # a second ago.
    already_out = session.scalar(
        select(Borrow).where(Borrow.book_id == book.id,
                             Borrow.return_date.is_(None)))
    if already_out is not None:
        raise LibraryError(f'"{book.title}" is already lent out.')

    open_count = session.scalar(
        select(func.count(Borrow.id))
        .where(Borrow.member_id == member.id, Borrow.return_date.is_(None)))
    if open_count and open_count >= MAX_OPEN_LOANS:
        raise LibraryError(f'{member.full_name} already has '
                           f'{MAX_OPEN_LOANS} books.')

    now = datetime.now()
    borrow = Borrow(book_id=book.id, member_id=member.id,
                    borrow_date=now, due_date=now + timedelta(days=days))
    session.add(borrow)
    session.flush()
    return borrow


def return_book(session: Session, borrow: Borrow) -> Borrow:
    '''Close a loan.'''
    if borrow.return_date is not None:
        raise LibraryError('This loan is already closed.')
    borrow.return_date = datetime.now()
    return borrow


def extend_loan(session: Session, borrow: Borrow,
                days: int = LOAN_DAYS) -> Borrow:
    if borrow.return_date is not None:
        raise LibraryError('This loan is already closed.')
    borrow.due_date = borrow.due_date + timedelta(days=days)
    return borrow


# -- numbers for the dashboard ---------------------------------------------
def statistics(session: Session) -> dict:
    '''One dictionary with everything the statistics tab shows.'''
    total_books = session.scalar(select(func.count(Book.id))) or 0
    total_members = session.scalar(select(func.count(Member.id))) or 0
    out = session.scalar(
        select(func.count(Borrow.id)).where(Borrow.return_date.is_(None))) or 0
    late = session.scalar(
        select(func.count(Borrow.id))
        .where(Borrow.return_date.is_(None),
               Borrow.due_date < datetime.now())) or 0

    # The five most borrowed titles: GROUP BY + ORDER BY (session 30).
    popular = session.execute(
        select(Book.title, func.count(Borrow.id).label('times'))
        .join(Borrow, Borrow.book_id == Book.id)
        .group_by(Book.id)
        .order_by(func.count(Borrow.id).desc())
        .limit(5)).all()

    return {'books': total_books,
            'members': total_members,
            'on_loan': out,
            'available': total_books - out,
            'late': late,
            'popular': [(title, times) for title, times in popular]}


def add_sample_data(session: Session) -> None:
    '''A few rows so the program has something to show on the first run.'''
    if session.scalar(select(func.count(Book.id))):
        return              # never overwrite real data

    books = [
        Book(title='Clean Code', author='Robert C. Martin',
             publisher='Prentice Hall', year=2008, isbn='9780132350884'),
        Book(title='Fluent Python', author='Luciano Ramalho',
             publisher="O'Reilly", year=2022, isbn='9781492056355'),
        Book(title='Automate the Boring Stuff', author='Al Sweigart',
             publisher='No Starch', year=2019, isbn='9781593279929'),
        Book(title='The Pragmatic Programmer', author='Hunt & Thomas',
             publisher='Addison-Wesley', year=2019),
    ]
    members = [
        Member(first_name='Sara', last_name='Ahmadi', card_number='1001',
               phone='09110000001', email='sara@example.com'),
        Member(first_name='Ali', last_name='Rezaei', card_number='1002',
               phone='09110000002'),
        Member(first_name='Mina', last_name='Karimi', card_number='1003'),
    ]
    session.add_all(books + members)
    session.flush()

    lend_book(session, books[0], members[0])
    # A loan that is already late, so the red rows can be seen at once.
    late = lend_book(session, books[1], members[1])
    late.due_date = datetime.now() - timedelta(days=3)
