'''Flask + SQLAlchemy: the database of session 32, inside a web site.

    pip install Flask-SQLAlchemy

Flask-SQLAlchemy is a thin layer over the SQLAlchemy of session 32. It gives
you `db.session` and `db.Model` already tied to the application, so you do not
have to create an engine and a session yourself.

    db = SQLAlchemy(model_class=Base)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
    db.init_app(app)

`sqlite:///library.db` is a RELATIVE path: the file goes into the `instance/`
folder that Flask creates next to your program.

Two habits worth taking straight away:

* Create the tables with a COMMAND (`flask --app app init-db`), not with a
  route. The original version of this course had `GET /api/init-db`, which
  means anybody who finds that address can touch your database -- and a GET
  is supposed to change nothing at all.
* `db.get_or_404(Model, id)` raises a clean 404 instead of returning `None`
  that explodes three lines later.

The modern query style (SQLAlchemy 2.x):

    db.session.scalars(db.select(Book)).all()             every row
    db.session.scalars(db.select(Book).where(...)).all()  filtered
    db.session.get(Book, 3)                               by primary key
    db.session.add(book); db.session.commit()             save
    db.session.delete(book); db.session.commit()          remove
'''

from flask import Flask, abort, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    '''The base class every model inherits from (SQLAlchemy 2 style).'''


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


class Author(db.Model):
    __tablename__ = 'author'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    # One author has many books. `back_populates` connects the two sides;
    # `cascade` deletes the books of an author we delete.
    books: Mapped[list['Book']] = relationship(
        back_populates='author', cascade='all, delete-orphan')

    def to_dict(self) -> dict:
        return {'id': self.id, 'name': self.name,
                'book_count': len(self.books)}


class Book(db.Model):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    summary: Mapped[str | None] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))

    author: Mapped[Author] = relationship(back_populates='books')

    def to_dict(self) -> dict:
        return {'id': self.id, 'title': self.title,
                'summary': self.summary,
                'author': self.author.name if self.author else None}


# -- commands, not routes --------------------------------------------------
@app.cli.command('init-db')
def init_db_command() -> None:
    '''Create the tables and a little sample data.

    Run it with:  flask --app app init-db
    '''
    db.create_all()

    if db.session.scalar(db.select(db.func.count(Author.id))) == 0:
        martin = Author(name='Robert Martin')
        ramalho = Author(name='Luciano Ramalho')
        martin.books = [Book(title='Clean Code', summary='How to write it.'),
                        Book(title='Clean Architecture')]
        ramalho.books = [Book(title='Fluent Python',
                              summary='Python, deeply.')]
        db.session.add_all([martin, ramalho])
        db.session.commit()
        print('Tables created and filled.')
    else:
        print('Tables created (they already had data).')


# -- HTML pages ------------------------------------------------------------
@app.route('/')
def home():
    authors = db.session.scalars(db.select(Author).order_by(Author.name)).all()
    return render_template('index.html', authors=authors)


@app.route('/author/<int:author_id>')
def author_page(author_id: int):
    # get_or_404: no `if is None` to forget.
    author = db.get_or_404(Author, author_id)
    return render_template('author.html', author=author)


# -- the JSON API ----------------------------------------------------------
@app.route('/api/books')
def api_books():
    query = db.select(Book).join(Author).order_by(Book.title)

    search = request.args.get('q', '').strip()
    if search:
        # `like` with a parameter -- never an f-string (session 30).
        query = query.where(Book.title.ilike(f'%{search}%'))

    books = db.session.scalars(query).all()
    return jsonify(count=len(books), books=[book.to_dict() for book in books])


@app.route('/api/books', methods=['POST'])
def api_create_book():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(error='the body must be a JSON object'), 400

    title = str(payload.get('title', '')).strip()
    if not title:
        return jsonify(error='"title" is required'), 400

    author_id = payload.get('author_id')
    author = db.session.get(Author, author_id) if author_id else None
    if author is None:
        return jsonify(error='"author_id" must be an existing author'), 400

    book = Book(title=title, summary=payload.get('summary'), author=author)
    db.session.add(book)
    db.session.commit()             # the id is filled in by the commit
    return jsonify(book.to_dict()), 201


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def api_delete_book(book_id: int):
    book = db.session.get(Book, book_id)
    if book is None:
        return jsonify(error='no such book'), 404
    db.session.delete(book)
    db.session.commit()
    return '', 204


@app.errorhandler(404)
def not_found(error):
    # An API address answers JSON; a page answers HTML.
    if request.path.startswith('/api/'):
        return jsonify(error='not found'), 404
    return render_template('404.html'), 404


if __name__ == '__main__':
    # For the first run, create the tables so `python app.py` alone works.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
