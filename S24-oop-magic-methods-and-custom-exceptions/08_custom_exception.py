# An exception is just a class that inherits from Exception.
# Creating your own makes the error messages of your program meaningful.
class LoginError(Exception):
    'Raised when a login attempt fails.'


def login(username: str, password: str) -> str:
    if username != 'admin':
        raise LoginError('Username is incorrect')
    if password != '1234':
        raise LoginError('Password is incorrect')
    return 'Logged in!'


if __name__ == '__main__':
    try:
        print(login('admin', '1234'))
        print(login('admin', 'wrong'))
    except LoginError as e:
        print('Error:', e)

    # Because LoginError inherits from Exception, a general handler still
    # catches it - but a specific one gives a much better message.
    try:
        login('someone', 'x')
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
