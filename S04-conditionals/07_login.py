# Constants are written in CAPITALS by convention: they are not meant to change.
USERNAME = 'admin'
PASSWORD = 'admin'

user = input('Enter username: ')
password = input('Enter password: ')

# Both conditions must be true, so we use 'and'.
if user == USERNAME and password == PASSWORD:
    print('Welcome,', user)
else:
    print('Access denied!')
