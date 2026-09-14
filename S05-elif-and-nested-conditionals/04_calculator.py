# A simple calculator: two numbers and one operator.
num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))

operator = input('Enter the sign (+ - * / **): ')

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    # Dividing by zero would crash the program, so we check it first.
    if num2 == 0:
        print('Error: division by zero!')
    else:
        result = num1 / num2
        print(result)
elif operator == '**':
    result = num1 ** num2
    print(result)
else:
    print('Error: unknown operator!')
