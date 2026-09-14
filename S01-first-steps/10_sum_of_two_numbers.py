# First complete mini program: read two numbers and print their sum.
# float() is used instead of int() so the user may also enter 3.5

user_input = input('Enter the first number: ')
num1 = float(user_input)

user_input = input('Enter the second number: ')
num2 = float(user_input)

total = num1 + num2

print('The sum is:', total)
