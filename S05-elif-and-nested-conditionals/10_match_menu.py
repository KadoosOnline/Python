# A menu is the classic use of match/case.
print('1) New file')
print('2) Open file')
print('3) Save file')
print('0) Exit')

choice = input('Enter the number: ')

match choice:
    case '1':
        print('Creating a new file...')
    case '2':
        print('Opening a file...')
    case '3':
        print('Saving the file...')
    case '0':
        print('Goodbye!')
    case _:
        print('Unknown option.')
