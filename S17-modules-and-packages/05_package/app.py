# A package is a FOLDER that contains an __init__.py file.
# The path to a module inside it uses dots: package.module
from math_package.my_math import add, mul

if __name__ == '__main__':
    print(add(num1=5, num2=6))
    print(mul(num1=5, num2=6))
