# Three possible outcomes -> if / elif / else.
user_input = input('Enter a number: ')
number = float(user_input)

if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')
