# A function that compares two numbers and returns the bigger one.
# (Python already has max(); we write it here to practise.)
def bigger(num1, num2):
    if num1 > num2:
        return num1
    return num2

user_input = input('Enter the first number: ')
a = float(user_input)

user_input = input('Enter the second number: ')
b = float(user_input)

print('Max:', bigger(a, b))
