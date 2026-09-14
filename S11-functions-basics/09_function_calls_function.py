# A function may call another function. Here pow() is built on top of mul().
def mul(num1, num2):
    'Multiply two whole numbers using repeated addition.'
    result = 0
    for i in range(num2):
        result += num1
    return result

def power(num1, num2):
    'Raise num1 to the power num2 using repeated multiplication.'
    result = 1
    for i in range(num2):
        result = mul(result, num1)
    return result

a = int(input('Enter the base: '))
b = int(input('Enter the exponent: '))

print(power(a, b))
