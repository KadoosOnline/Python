# Read a number from the user and increase it by 2.
user_input = input('Enter a number: ')

number = int(user_input)   # input() gives text, so we must convert it
number += 2

print('Your number plus 2 is:', number)
