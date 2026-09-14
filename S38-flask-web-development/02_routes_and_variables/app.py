'''Addresses that carry a value, and the right way to fail.

    @app.route('/hello/<name>')          -> /hello/sara     name = 'sara'
    @app.route('/post/<int:post_id>')    -> /post/12        post_id = 12 (an int!)

The converters: `string` (the default, no slash), `int`, `float`, `path`
(slashes allowed), `uuid`.

`<int:...>` is worth a lot: `/post/abc` gives a clean 404 instead of reaching
your code with a string you would then have to convert.

`url_for('function_name', **arguments)` builds an address FROM the name of the
view function. Always use it instead of writing '/post/12' by hand: change the
route once and every link follows.

THE BUG OF THE ORIGINAL VERSION
`return render_template(..., name=usernames[username])` -- an unknown user
raised `KeyError`, and the visitor got a 500 "Internal Server Error", which
means "the programmer made a mistake". A user who does not exist is not a
mistake, it is a **404 Not Found**. That is what `abort(404)` is for.
'''

from flask import Flask, abort, redirect, url_for


app = Flask(__name__)

USERS = {
    'arad': 'Arad Lotfi',
    'raha': 'Raha Mousavi',
    'mohanna': 'Mohanna Mohammadi',
    'mehrnoosh': 'Mehrnoosh Ajdadi',
}

POSTS = {1: 'Why Python?', 2: 'Loops in ten minutes', 3: 'What is a class?'}


@app.route('/')
def home() -> str:
    # url_for builds the links; the routes below can change freely.
    links = ''.join(
        f'<li><a href="{url_for("profile", username=name)}">{name}</a></li>'
        for name in USERS)
    posts = ''.join(
        f'<li><a href="{url_for("post", post_id=key)}">{title}</a></li>'
        for key, title in POSTS.items())
    return (f'<h1>Users</h1><ul>{links}</ul>'
            f'<h1>Posts</h1><ul>{posts}</ul>'
            f'<p><a href="{url_for("profile", username="nobody")}">'
            'a user who does not exist</a> -> a clean 404</p>')


@app.route('/user/<username>')
def profile(username: str) -> str:
    '''A missing user is a 404, not a crash.'''
    if username not in USERS:
        abort(404)
    return f'<h1>{USERS[username]}</h1><p>username: {username}</p>'


@app.route('/post/<int:post_id>')
def post(post_id: int) -> str:
    '''`<int:...>`: post_id really is an int here.'''
    title = POSTS.get(post_id)
    if title is None:
        abort(404)
    # post_id is a real int, so arithmetic works without any conversion.
    return (f'<h1>{title}</h1>'
            f'<p>post {post_id}; the next one would be {post_id + 1}</p>')


@app.route('/old-home')
def old_home():
    '''A page that moved: send the browser to the new address.'''
    return redirect(url_for('home'))


@app.errorhandler(404)
def not_found(error):
    '''Our own 404 page. The second value is the HTTP STATUS CODE.'''
    return ('<h1>404 - not found</h1>'
            f'<p><a href="{url_for("home")}">back home</a></p>'), 404


if __name__ == '__main__':
    app.run(debug=True)
