'''A tiny contact book: one file per friend, four lines inside it.

Try it with the file friends.txt that is already in this folder:
    Enter your friend's name: friends
'''

import os


def main() -> None:
    friend_name = input("Enter your friend's name: ")
    filename = f'{friend_name}.txt'

    # Never open a file without checking that it exists.
    if not os.path.exists(filename):
        print(f'No contact file called {filename}.')
        return

    with open(filename, encoding='utf-8') as f:
        firstname = f.readline().strip()
        lastname = f.readline().strip()
        cellphone = f.readline().strip()
        email = f.readline().strip()

    print(f'Firstname: {firstname}')
    print(f'Lastname:  {lastname}')
    print(f'Cellphone: {cellphone}')
    print(f'Email:     {email}')


if __name__ == '__main__':
    main()
