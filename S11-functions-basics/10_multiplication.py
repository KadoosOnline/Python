# Multiplication written as repeated addition - a classic exercise
# to show that a loop can replace an operator.
def mul(num1, num2):
    result = 0
    for i in range(num2):
        result += num1      # result = result + num1
    return result

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

print(mul(a, b))
print('Check:', a * b)
