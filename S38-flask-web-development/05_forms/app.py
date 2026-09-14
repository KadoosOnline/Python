'''Forms: reading what the visitor typed, and the redirect that follows.

A form sends its fields to your program:

    <form method="post" action="{{ url_for('register') }}">
        <input name="full_name">
    </form>

    request.form['full_name']          KeyError -> 400 if the field is missing
    request.form.get('full_name', '')  safer: a default instead of an error
    request.args.get('q')              the ?q=... part of the address (GET)
    request.files['photo']             an uploaded file

GET or POST?
    GET  -- "give me something". The values are in the address, so they are
            bookmarked, logged and sent again on every reload. For a search.
    POST -- "here is something, keep it". For anything that CHANGES data.

THE POST / REDIRECT / GET RULE
After a successful POST, never render a page: **redirect**. Otherwise the
browser still has the POST in hand, and pressing F5 sends the form again --
the second registration, the second payment. Redirecting turns the last action
into a harmless GET.

FLASH MESSAGES
`flash('...')` stores a message in the session and the NEXT page shows it.
That is how you say "saved" after a redirect. It needs `app.secret_key`,
because the session is a signed cookie.

*** the secret key must not be written in the source of a real site ***:
read it from the environment, exactly like the bot token of session 37.
'''

import os
import re

from flask import (Flask, flash, redirect, render_template, request, url_for)


app = Flask(__name__)
# Fine for the classroom; on a real server this comes from the environment.
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-not-for-production')

# Our "database" for today.
REGISTRATIONS: list[dict] = []

COURSES = ['Introduction to Python', 'Advanced Python', 'Web with Flask']

EMAIL_PATTERN = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')


def validate(form) -> tuple[dict, list[str]]:
    '''Clean the fields and collect every problem, not just the first one.'''
    data = {
        'name': form.get('name', '').strip(),
        'email': form.get('email', '').strip(),
        'course': form.get('course', ''),
        'sessions': form.get('sessions', '').strip(),
        'newsletter': 'newsletter' in form,      # a checkbox is present or not
    }
    errors = []

    if len(data['name']) < 3:
        errors.append('The name must be at least 3 characters long.')
    if not EMAIL_PATTERN.match(data['email']):
        errors.append('That does not look like an e-mail address.')
    # Never trust a <select>: the browser is not the only thing that can POST.
    if data['course'] not in COURSES:
        errors.append('Please choose a course from the list.')
    if not data['sessions'].isdigit() or not 1 <= int(data['sessions']) <= 20:
        errors.append('The number of sessions must be between 1 and 20.')

    return data, errors


@app.route('/', methods=['GET', 'POST'])
def register():
    '''One address, two methods: show the form, then receive it.'''
    if request.method == 'POST':
        data, errors = validate(request.form)

        if errors:
            for message in errors:
                flash(message, 'error')
            # Give the form back WITH what the visitor already typed.
            return render_template('register.html', courses=COURSES,
                                   data=data)

        data['sessions'] = int(data['sessions'])
        REGISTRATIONS.append(data)
        flash(f'Thank you {data["name"]}, you are registered.', 'success')
        # POST / Redirect / GET: F5 now reloads a harmless page.
        return redirect(url_for('registrations'))

    # GET: an empty form.
    return render_template('register.html', courses=COURSES, data={})


@app.route('/registrations')
def registrations():
    '''A GET page, with an optional ?q=... search.'''
    query = request.args.get('q', '').strip().lower()
    rows = [row for row in REGISTRATIONS
            if not query or query in row['name'].lower()]
    return render_template('registrations.html', rows=rows, query=query,
                           total=len(REGISTRATIONS))


if __name__ == '__main__':
    app.run(debug=True)
