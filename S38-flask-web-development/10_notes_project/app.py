'''The notes project -- the application itself.

This file uses the APPLICATION FACTORY pattern: instead of one global `app`
built when the module is imported, a function BUILDS an application and
returns it.

    def create_app(config=None) -> Flask:
        app = Flask(__name__)
        ...
        return app

Why it is worth the extra function:

* the configuration is an argument, so the same code can run with a different
  database (a real one, a temporary one, one per developer);
* nothing happens merely because somebody imported the module;
* the circular-import knot disappears: `models` and `routes` never import
  `app`.

Run it:

    python app.py                       (creates the tables on the first run)
    flask --app app init-db             (tables + a little sample data)
    flask --app app run --debug

The database file lands in `instance/notes.db`, a folder Flask creates itself.
'''

import os

from flask import Flask, render_template

from models import Category, Note, db
from routes import notes_bp


def create_app(database_uri: str | None = None) -> Flask:
    '''Build and return a ready application.'''
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',
                                              'dev-key-not-for-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = (database_uri
                                             or 'sqlite:///notes.db')

    db.init_app(app)
    app.register_blueprint(notes_bp)

    register_error_handlers(app)
    register_commands(app)

    return app


def register_error_handlers(app: Flask) -> None:
    '''Our own pages instead of the bare Werkzeug ones.'''

    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.html', code=404,
                               message='There is nothing at this address.'), 404

    @app.errorhandler(500)
    def server_error(error):
        # A 500 means WE made a mistake: roll the session back, or the next
        # request inherits a broken transaction.
        db.session.rollback()
        return render_template('error.html', code=500,
                               message='Something went wrong on our side.'), 500


def register_commands(app: Flask) -> None:
    '''Commands you type, not addresses anybody can open.'''

    @app.cli.command('init-db')
    def init_db() -> None:
        '''Create the tables and add a few notes to look at.'''
        db.create_all()

        if db.session.scalar(db.select(db.func.count(Category.id))) == 0:
            lessons = Category(name='Lessons')
            ideas = Category(name='Ideas')
            db.session.add_all([lessons, ideas])
            db.session.add_all([
                Note(title='Session 38 - Flask',
                     body='Routes, templates, forms, sessions, an API.',
                     category=lessons),
                Note(title='Read about blueprints',
                     body='Split a big application into groups of routes.',
                     category=ideas),
                Note(title='A note with no category',
                     body='category_id may be NULL, and that is on purpose.'),
            ])
            db.session.commit()
            print('Database created and filled.')
        else:
            print('Database ready (it already had data).')

    @app.cli.command('drop-db')
    def drop_db() -> None:
        '''Throw everything away and start again.'''
        db.drop_all()
        print('All the tables were dropped.')


# The module-level `app` is what `flask --app app ...` looks for.
app = create_app()


if __name__ == '__main__':
    # So that `python app.py` works on a fresh clone with no command to type.
    with app.app_context():
        db.create_all()
    app.run(debug=True)
