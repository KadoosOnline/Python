'''The engine, the session, and the transaction helper.

One engine for the whole program, created once when this module is imported.
`SessionLocal()` then gives out sessions -- a session is one "conversation"
with the database: you add and change objects, and `commit()` writes them all
at once.

`session_scope()` is the context manager that makes that safe:

    with session_scope() as session:
        session.add(book)
        ...
    # commit() here if nothing went wrong, rollback() if it did, always close()

Without it, an exception in the middle leaves a half-written transaction and a
session that nobody closed.

`PRAGMA foreign_keys = ON` has to run on EVERY connection -- SQLite ignores
foreign keys otherwise, so `ondelete='CASCADE'` would quietly do nothing. The
`event.listens_for(..., 'connect')` hook is how you make sure of it.
'''

from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker

from .models import Base
from .paths import database_path


ENGINE = create_engine(f'sqlite:///{database_path()}', echo=False,
                       future=True)

# expire_on_commit=False is important here. By default, `commit()` marks every
# loaded attribute as "must be read again", and reading one after the session
# is closed raises DetachedInstanceError. The GUI keeps the objects it showed
# (to know which row is selected), so we need their values to stay usable
# after the transaction ends.
SessionLocal = sessionmaker(bind=ENGINE, autoflush=False, autocommit=False,
                            expire_on_commit=False, future=True)


@event.listens_for(ENGINE, 'connect')
def _enable_foreign_keys(dbapi_connection, connection_record) -> None:
    '''SQLite needs this on every connection, or ON DELETE does nothing.'''
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()


def init_database() -> None:
    '''Create the file and the tables if they are not there yet.'''
    Base.metadata.create_all(bind=ENGINE)


@contextmanager
def session_scope() -> Iterator[Session]:
    '''One transaction: commit on success, roll back on any exception.'''
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise               # the caller still has to know
    finally:
        session.close()
