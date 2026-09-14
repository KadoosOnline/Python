'''Template inheritance and static files -- how a real site is organised.

Copying the same <head>, menu and footer into every page is the fastest way to
end up with five pages that no longer look alike. Jinja solves it with
INHERITANCE:

    base.html      defines the skeleton and leaves holes: {% block content %}
    index.html     {% extends 'base.html' %} and fills the holes

You can also cut a repeated piece into its own file and pull it in with
`{% include 'card.html' %}`, and turn a repeated piece of MARKUP with
arguments into a `{% macro %}`.

STATIC FILES (css, js, images) live in a folder called `static/`, and you link
to them with:

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

Never write href="/static/style.css" by hand: `url_for` keeps working when the
application is served from a sub-folder, and it is what lets Flask add a
cache-busting parameter.
'''

from flask import Flask, render_template


app = Flask(__name__)

COURSES = [
    {'slug': 'python1', 'title': 'Introduction to Python',
     'sessions': 20, 'price': 4_500_000},
    {'slug': 'python2', 'title': 'Advanced Python',
     'sessions': 20, 'price': 5_200_000},
    {'slug': 'flask', 'title': 'Web development with Flask',
     'sessions': 12, 'price': 3_800_000},
]


@app.context_processor
def inject_globals():
    '''Whatever this returns is available in EVERY template.

    Perfect for the things the menu and the footer need, so you do not have to
    pass them from all thirty view functions.
    '''
    return {'site_name': 'Kadoos Institute', 'year': 1404}


@app.route('/')
def home():
    return render_template('index.html', courses=COURSES)


@app.route('/courses')
def courses():
    return render_template('courses.html', courses=COURSES)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
