'''The smallest web site in the world.

    pip install flask

A web program is a program that ANSWERS. The browser sends a request
("give me /about"), your program returns an answer (some HTML), and that is
the whole story.

Flask connects the two with a decorator:

    @app.route('/about')      <- the address (the "route")
    def about():              <- the "view function"
        return 'some HTML'    <- the answer

Run it in one of two ways:

    python app.py                      # what we do in this course
    flask --app app run --debug        # the official way

Then open  http://127.0.0.1:5000  in the browser.

`debug=True` gives you two things you will not want to live without:
* the server RESTARTS by itself when you save a file;
* an error shows a full page with the traceback instead of "Internal Server
  Error".

*** and it must NEVER be true on a real server ***: that page also gives a
visitor a Python console inside your program.
'''

from flask import Flask


# `__name__` tells Flask where this file is, so it can find `templates/`
# and `static/` next to it.
app = Flask(__name__)


@app.route('/')
def home() -> str:
    '''The home page. The name of the function is up to you.'''
    return '<h1>Hello!</h1><p>This is my first Flask program.</p>'


@app.route('/about')
def about() -> str:
    return ('<h1>Kadoos Institute</h1>'
            '<p>Python course, Rasht.</p>'
            '<p><a href="/">back home</a></p>')


# One function can answer several addresses.
@app.route('/contact')
@app.route('/contact-us')
def contact() -> str:
    return '<h1>Contact</h1><p>Come and see us in Rasht.</p>'


if __name__ == '__main__':
    # host='127.0.0.1' = only this computer can open it.
    # host='0.0.0.0' would let the whole classroom network in.
    app.run(debug=True)
