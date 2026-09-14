# We define a variable called user_input   (this is a comment)

user_input = input('Enter the first number: ')
num1 = float(user_input)

user_input = input('Enter the second number: ')
num2 = float(user_input)

# NOTE: do not call a variable 'sum' - that is the name of a built-in function.
total = num1 + num2

print('The sum is:', total)
