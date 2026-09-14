# Comparing two numbers entered by the user.
num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))

if num1 > num2:
    print(num1, 'is bigger!')
elif num2 > num1:
    print(num2, 'is bigger!')
else:
    print('The two numbers are equal.')
