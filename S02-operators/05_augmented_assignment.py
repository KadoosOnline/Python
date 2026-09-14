# 'num1 = num1 + num2' is so common that Python offers a shorter form: '+='.
num1 = 24
num2 = 6

num1 += num2   # same as num1 = num1 + num2
print(num1)    # 30

num1 -= num2   # same as num1 = num1 - num2
print(num1)    # 24

num1 *= num2   # same as num1 = num1 * num2
print(num1)    # 144

num1 /= num2   # same as num1 = num1 / num2  -> the result becomes a float
print(num1)    # 24.0

# The same short form exists for // , % and **
num1 //= 5
print(num1)    # 4.0
