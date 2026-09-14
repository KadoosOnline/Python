# From Python 3.10 on, 'match ... case' is a clean alternative to a long
# chain of elif branches that all compare the SAME value.
user_input = input('Enter a number (1-7): ')

match user_input:
    case '1':
        print('Shanbe')
    case '2':
        print('Yekshanbe')
    case '3':
        print('Doshanbe')
    case '4':
        print('Seshanbe')
    case '5':
        print('Chaharshanbe')
    case '6' | '7':          # '|' means "or": one branch for two values
        print('Weekend')
    case _:                  # '_' is the default branch, like 'else'
        print('Error: the number must be between 1 and 7')
