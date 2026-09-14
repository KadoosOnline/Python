'''Sessions and a login -- who is on the other side of the connection?

HTTP has NO memory. Every request arrives alone, and the server has no idea
that the person asking for /profile is the same one who filled in /login a
second ago. The answer is a COOKIE.

Flask's `session` is a dict that is stored in a cookie:

    session['username'] = 'sara'      # write
    session.get('username')           # read
    session.pop('username', None)     # forget
    session.clear()                   # forget everything

What you must know about it:

* The cookie is SIGNED with `app.secret_key`, so nobody can change it without
  being caught -- but it is only base64, so anybody can READ it. Never put a
  password, a card number or anything private in the session.
* If the secret key changes, every session is invalidated at once.
* The whole thing lives in the visitor's browser: keep it small.

PASSWORDS
Never, ever store a password. Store a HASH:

    generate_password_hash('1234')   -> 'scrypt:32768:8:1$xYz...'
    check_password_hash(hash, typed) -> True / False

A hash cannot be turned back into the password, so a stolen database does not
hand the attacker everybody's password. `werkzeug` comes with Flask, so you
already have it.

PROTECTING A PAGE
`@login_required` is a decorator (session 26) that runs before the view and
redirects to the login page when nobody is logged in.
'''

import functools
import os

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-not-for-production')

# In a real application this is a table (session 31), not a dict -- but the
# passwords are stored exactly like this: hashed, never in clear text.
USERS = {
    'sara': {'name': 'Sara Ahmadi',
             'password_hash': generate_password_hash('python123')},
    'ali': {'name': 'Ali Rezaei',
            'password_hash': generate_password_hash('kadoos456')},
}

SECRET_NOTES = {'sara': ['Finish the Flask exercise', 'Buy a notebook'],
                'ali': ['Read about decorators']}


def login_required(view):
    '''A decorator that sends anonymous visitors to the login page.'''
    @functools.wraps(view)          # keep the name of the wrapped function
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            flash('Please log in first.', 'error')
            # `next=` remembers where the visitor wanted to go.
            return redirect(url_for('login', next=request.path))
        return view(*args, **kwargs)
    return wrapper


@app.route('/')
def home():
    return render_template('home.html', user=current_user())


def current_user() -> dict | None:
    '''The logged-in user, or None.'''
    username = session.get('username')
    return USERS.get(username) if username else None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip().lower()
        password = request.form.get('password', '')

        user = USERS.get(username)
        # ONE message for both cases: saying "no such user" would tell an
        # attacker which names exist.
        if user is None or not check_password_hash(user['password_hash'],
                                                   password):
            flash('Wrong user name or password.', 'error')
            return render_template('login.html', username=username)

        # A new session id at login: it closes the "session fixation" hole.
        session.clear()
        session['username'] = username
        flash(f'Welcome {user["name"]}!', 'success')

        # Never redirect to any address the visitor sends us: an absolute URL
        # here would be an "open redirect" straight to a phishing page.
        target = request.args.get('next', '')
        if not target.startswith('/') or target.startswith('//'):
            target = url_for('profile')
        return redirect(target)

    return render_template('login.html', username='')


@app.route('/logout')
def logout():
    session.clear()
    flash('You are logged out.', 'success')
    return redirect(url_for('home'))


@app.route('/profile')
@login_required
def profile():
    username = session['username']
    return render_template('profile.html', user=USERS[username],
                           username=username,
                           notes=SECRET_NOTES.get(username, []))


@app.route('/counter')
def counter():
    '''The session is an ordinary dict: here it counts the visits.'''
    session['visits'] = session.get('visits', 0) + 1
    return render_template('counter.html', visits=session['visits'])


if __name__ == '__main__':
    app.run(debug=True)
