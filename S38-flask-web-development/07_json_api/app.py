'''A JSON API: a web program whose visitors are other programs.

In session 28 we CALLED a REST API with `requests`. Now we write one.

The difference with the pages above: instead of HTML we return JSON, and the
HTTP STATUS CODE carries the meaning.

    200 OK          here it is
    201 Created     I created what you sent
    204 No content  done, and there is nothing to send back
    400 Bad request YOUR message was wrong (a missing field, bad JSON)
    401 / 403       you are not logged in / you are not allowed
    404 Not found   there is no such thing
    405             wrong method for this address
    500             *I* made a mistake

Returning 200 with `{"error": "..."}` inside -- which is what a beginner
usually does -- makes every client have to read the body to know whether it
worked. Use the codes.

    return jsonify(data), 201
    return jsonify(error='...'), 400

The REST convention for the addresses:

    GET    /api/books          the list
    POST   /api/books          create one
    GET    /api/books/3        one of them
    PUT    /api/books/3        replace it
    PATCH  /api/books/3        change a part of it
    DELETE /api/books/3        remove it

THE BUG OF THE ORIGINAL VERSION
`payload = request.get_json()` then `payload['title']`. If the client forgets
the field -- or sends no JSON at all -- that is a `KeyError` or a
`TypeError`, and the client gets a 500 page. A missing field is the CLIENT's
mistake: 400. Every function below checks before it touches the data.
'''

from flask import Flask, jsonify, request


app = Flask(__name__)

BOOKS = {
    1: {'title': 'Clean Code', 'author': 'Robert Martin', 'year': 2008},
    2: {'title': 'Fluent Python', 'author': 'Luciano Ramalho', 'year': 2022},
}
next_id = 3


def with_id(book_id: int) -> dict:
    '''The stored book plus its id -- the shape we send to the client.'''
    return {'id': book_id, **BOOKS[book_id]}


def read_payload() -> tuple[dict | None, tuple | None]:
    '''Return (data, error_response). Exactly one of the two is None.'''
    # silent=True -> None instead of an exception when the body is not JSON.
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None, (jsonify(error='the body must be a JSON object'), 400)
    return payload, None


@app.route('/api/books', methods=['GET'])
def list_books():
    '''?author=... filters the list.'''
    author = request.args.get('author', '').lower()
    books = [with_id(key) for key in BOOKS
             if not author or author in BOOKS[key]['author'].lower()]
    # A top-level LIST is legal JSON, but wrapping it in an object leaves room
    # to add "count" or "next page" later without breaking every client.
    return jsonify(count=len(books), books=books)


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id: int):
    if book_id not in BOOKS:
        return jsonify(error=f'no book with id {book_id}'), 404
    return jsonify(with_id(book_id))


@app.route('/api/books', methods=['POST'])
def create_book():
    global next_id

    payload, error = read_payload()
    if error:
        return error

    title = str(payload.get('title', '')).strip()
    if not title:
        return jsonify(error='"title" is required'), 400

    year = payload.get('year')
    if year is not None and not isinstance(year, int):
        return jsonify(error='"year" must be a whole number'), 400

    book_id = next_id
    next_id += 1
    BOOKS[book_id] = {'title': title,
                      'author': str(payload.get('author', '')).strip(),
                      'year': year}
    # 201 Created, and the address of the new thing in the Location header.
    return jsonify(with_id(book_id)), 201, {
        'Location': f'/api/books/{book_id}'}


@app.route('/api/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id: int):
    if book_id not in BOOKS:
        return jsonify(error=f'no book with id {book_id}'), 404

    payload, error = read_payload()
    if error:
        return error

    # PATCH: change only the keys that were sent, ignore the rest.
    for field in ('title', 'author', 'year'):
        if field in payload:
            BOOKS[book_id][field] = payload[field]
    return jsonify(with_id(book_id))


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id: int):
    if book_id not in BOOKS:
        return jsonify(error=f'no book with id {book_id}'), 404
    del BOOKS[book_id]
    # 204: it worked and there is nothing to say.
    return '', 204


@app.errorhandler(404)
def api_not_found(error):
    '''An API must answer JSON even when it fails -- never an HTML page.'''
    return jsonify(error='not found'), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(error='wrong method for this address'), 405


if __name__ == '__main__':
    app.run(debug=True)
