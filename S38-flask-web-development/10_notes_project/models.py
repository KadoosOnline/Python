'''The database of the notes project.

Kept in its own module so that `routes.py` can import the models without a
circular import: `models` imports nothing from the application, and the
application imports `models`.

`db` is created here but tied to no application yet -- `db.init_app(app)` does
that in `app.py`. That is what lets the same models serve a real application
and, one day, a test application with a different database.
'''

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    '''The base class of every model.'''


db = SQLAlchemy(model_class=Base)


class Category(db.Model):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(primary_key=True)
    # unique=True: the database itself refuses two categories with one name.
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    notes: Mapped[list['Note']] = relationship(back_populates='category')

    def __repr__(self) -> str:
        return f'<Category {self.name}>'


class Note(db.Model):
    __tablename__ = 'note'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False, default='')

    # A note without a category is allowed, so the column may be NULL.
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey('category.id'), nullable=True)
    category: Mapped[Category | None] = relationship(back_populates='notes')

    # server_default=func.now(): the DATABASE fills it in, so the value is
    # right even for a row inserted by hand in another program.
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f'<Note {self.id} {self.title!r}>'

    def to_dict(self) -> dict:
        '''The shape the JSON API sends out.'''
        return {'id': self.id,
                'title': self.title,
                'body': self.body,
                'category': self.category.name if self.category else None,
                'created_at': self.created_at.isoformat()}
