'''Every page of the notes project, gathered in a BLUEPRINT.

A blueprint is a group of routes that is registered on an application later:

    notes = Blueprint('notes', __name__)

    @notes.route('/')            instead of @app.route('/')
    ...
    app.register_blueprint(notes)

Why bother? Because a real site has fifty routes, and putting them all in one
`app.py` next to the configuration is how a project becomes unreadable. With
blueprints you can split them by subject (`notes.py`, `admin.py`, `api.py`),
and each group can have its own url prefix and its own templates.

One thing changes: inside a blueprint, `url_for` needs the blueprint name.

    url_for('notes.index')       not  url_for('index')
'''

from flask import (Blueprint, abort, flash, jsonify, redirect,
                   render_template, request, url_for)

from models import Category, Note, db


notes_bp = Blueprint('notes', __name__)


# -- helpers ---------------------------------------------------------------
def all_categories():
    return db.session.scalars(db.select(Category).order_by(Category.name)).all()


def validate_note(form) -> tuple[dict, list[str]]:
    '''Clean the fields and collect every problem.'''
    data = {'title': form.get('title', '').strip(),
            'body': form.get('body', '').strip(),
            'category_id': form.get('category_id', '')}
    errors = []

    if not 3 <= len(data['title']) <= 120:
        errors.append('The title must be between 3 and 120 characters.')

    # '' means "no category". Anything else must be a real id: the value
    # comes from a <select>, and a <select> is not a guarantee of anything.
    if data['category_id']:
        if not data['category_id'].isdigit():
            errors.append('That category does not exist.')
        elif db.session.get(Category, int(data['category_id'])) is None:
            errors.append('That category does not exist.')

    return data, errors


# -- pages -----------------------------------------------------------------
@notes_bp.route('/')
def index():
    '''The list, with a search box and a category filter.'''
    query = db.select(Note).order_by(Note.created_at.desc())

    search = request.args.get('q', '').strip()
    if search:
        # ilike = LIKE without caring about upper/lower case.
        # The % is inside a PARAMETER, so there is no SQL injection here.
        pattern = f'%{search}%'
        query = query.where(db.or_(Note.title.ilike(pattern),
                                   Note.body.ilike(pattern)))

    category_id = request.args.get('category', '')
    if category_id.isdigit():
        query = query.where(Note.category_id == int(category_id))

    return render_template('index.html',
                           notes=db.session.scalars(query).all(),
                           categories=all_categories(),
                           search=search, category_id=category_id,
                           total=db.session.scalar(
                               db.select(db.func.count(Note.id))))


@notes_bp.route('/note/<int:note_id>')
def detail(note_id: int):
    note = db.get_or_404(Note, note_id)
    return render_template('detail.html', note=note)


@notes_bp.route('/note/new', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data, errors = validate_note(request.form)
        if errors:
            for message in errors:
                flash(message, 'error')
            return render_template('form.html', data=data,
                                   categories=all_categories(), note=None)

        note = Note(title=data['title'], body=data['body'],
                    category_id=int(data['category_id'])
                    if data['category_id'] else None)
        db.session.add(note)
        db.session.commit()
        flash('The note was created.', 'success')
        # POST / Redirect / GET.
        return redirect(url_for('notes.detail', note_id=note.id))

    return render_template('form.html', data={}, note=None,
                           categories=all_categories())


@notes_bp.route('/note/<int:note_id>/edit', methods=['GET', 'POST'])
def edit(note_id: int):
    note = db.get_or_404(Note, note_id)

    if request.method == 'POST':
        data, errors = validate_note(request.form)
        if errors:
            for message in errors:
                flash(message, 'error')
            return render_template('form.html', data=data, note=note,
                                   categories=all_categories())

        note.title = data['title']
        note.body = data['body']
        note.category_id = (int(data['category_id'])
                            if data['category_id'] else None)
        # No `add()`: the object already belongs to the session, and the
        # commit writes the change. `updated_at` moves by itself (onupdate).
        db.session.commit()
        flash('The note was saved.', 'success')
        return redirect(url_for('notes.detail', note_id=note.id))

    # GET: fill the form with what is in the database.
    return render_template('form.html', note=note, categories=all_categories(),
                           data={'title': note.title, 'body': note.body,
                                 'category_id': str(note.category_id or '')})


@notes_bp.route('/note/<int:note_id>/delete', methods=['POST'])
def delete(note_id: int):
    '''POST only. A link that deletes something is a bug waiting to happen:
    a browser (or a crawler) may follow it on its own.'''
    note = db.get_or_404(Note, note_id)
    db.session.delete(note)
    db.session.commit()
    flash(f'"{note.title}" was deleted.', 'success')
    return redirect(url_for('notes.index'))


@notes_bp.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        if len(name) < 2:
            flash('The name is too short.', 'error')
        elif db.session.scalar(db.select(Category)
                               .where(Category.name == name)):
            # Check first for a friendly message; the UNIQUE column is still
            # what really guarantees it.
            flash('That category already exists.', 'error')
        else:
            db.session.add(Category(name=name))
            db.session.commit()
            flash('Category added.', 'success')
        return redirect(url_for('notes.categories'))

    return render_template('categories.html', categories=all_categories())


# -- the JSON API of the same data -----------------------------------------
@notes_bp.route('/api/notes')
def api_notes():
    notes = db.session.scalars(
        db.select(Note).order_by(Note.created_at.desc())).all()
    return jsonify(count=len(notes), notes=[note.to_dict() for note in notes])


@notes_bp.route('/api/notes/<int:note_id>')
def api_note(note_id: int):
    note = db.session.get(Note, note_id)
    if note is None:
        return jsonify(error='no such note'), 404
    return jsonify(note.to_dict())
