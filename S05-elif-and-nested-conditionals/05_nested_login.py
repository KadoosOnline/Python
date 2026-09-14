# A nested 'if' is an 'if' placed inside the block of another 'if'.
# Here the password is only asked about when the username is correct.
username = input('Enter the username: ')
password = input('Enter the password: ')

if username == 'admin':
    if password == '123456':
        print('Welcome', username)
    else:
        print('The password is incorrect!')
else:
    print('The username is incorrect!')
