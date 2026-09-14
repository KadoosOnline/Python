'''The other side: a program that USES the API of example 07.

Start the server first, in another terminal:

    cd ../07_json_api
    python app.py

then run this file. This is exactly what session 28 did with a public API --
except that this time you wrote the server too.

Three things this client does that the original one did not:

* it sets a `timeout` on every call (without one, a request can hang for ever);
* it does not call `raise_for_status()` blindly -- it looks at the code, so it
  can tell "the book does not exist" (404) from "the server is broken" (500);
* it tells the user clearly when the server is simply not running.
'''

import requests


BASE_URL = 'http://127.0.0.1:5000'
TIMEOUT = 5


def show(label: str, response: requests.Response) -> None:
    print(f'{label}: {response.status_code}')
    if response.status_code != 204 and response.content:
        print('   ', response.json())


def main() -> None:
    session = requests.Session()        # reuses the connection

    try:
        show('GET the list', session.get(f'{BASE_URL}/api/books',
                                         timeout=TIMEOUT))

        # -- create one ----------------------------------------------------
        response = session.post(f'{BASE_URL}/api/books',
                                json={'title': 'Automate the Boring Stuff',
                                      'author': 'Al Sweigart',
                                      'year': 2019},
                                timeout=TIMEOUT)
        show('POST a new book', response)
        book_id = response.json()['id']
        print('    Location header:', response.headers.get('Location'))

        # -- change a part of it -------------------------------------------
        show('PATCH the year',
             session.patch(f'{BASE_URL}/api/books/{book_id}',
                           json={'year': 2020}, timeout=TIMEOUT))

        show('GET the new book',
             session.get(f'{BASE_URL}/api/books/{book_id}', timeout=TIMEOUT))

        # -- the errors the server is supposed to give ----------------------
        show('GET a book that does not exist',
             session.get(f'{BASE_URL}/api/books/999', timeout=TIMEOUT))

        show('POST with no title',
             session.post(f'{BASE_URL}/api/books', json={'author': 'nobody'},
                          timeout=TIMEOUT))

        show('POST with a body that is not JSON',
             session.post(f'{BASE_URL}/api/books', data='hello',
                          timeout=TIMEOUT))

        show('DELETE it',
             session.delete(f'{BASE_URL}/api/books/{book_id}',
                            timeout=TIMEOUT))

        show('GET the list again',
             session.get(f'{BASE_URL}/api/books', timeout=TIMEOUT))

    except requests.ConnectionError:
        print('The server does not answer.\n'
              'Start it first:  cd ../07_json_api && python app.py')
    except requests.Timeout:
        print(f'The server took more than {TIMEOUT} seconds to answer.')


if __name__ == '__main__':
    main()
