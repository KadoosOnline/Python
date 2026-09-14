# A number is even when the remainder of its division by 2 is zero.
user_input = input('Please enter a number: ')
number = int(user_input)

if number % 2 == 0:
    print('Even')
else:
    print('Odd')
