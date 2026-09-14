# The exception lives in errors.py and is imported like any other name.
from errors import LoginError


def login(username: str, password: str) -> str:
    if username != 'admin':
        raise LoginError('Username is incorrect')
    if password != '1234':
        raise LoginError('Password is incorrect')
    return 'Logged in!'


if __name__ == '__main__':
    try:
        print(login('admin', '1234'))
    except LoginError as e:
        print('Error:', e)

    try:
        print(login('user', '1234'))
    except LoginError as e:
        print('Error:', e)
