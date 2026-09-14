# Same program, but the password is only READ when the username is correct.
# This is the real advantage of nesting: we skip work we do not need.
USERNAME = 'admin'
PASSWORD = '123456'

username_input = input('Enter username: ')

if username_input == USERNAME:
    password_input = input('Enter password: ')

    if password_input == PASSWORD:
        print('Welcome!')
    else:
        print('Password error!')
else:
    print('Username error!')
