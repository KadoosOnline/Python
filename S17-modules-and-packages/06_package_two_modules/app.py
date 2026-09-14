# Two modules of the same package, each imported with its own path.
from math_package.my_math import add, mul
from math_package.your_math import sub, div

if __name__ == '__main__':
    print(add(num1=5, num2=6))
    print(mul(num1=5, num2=6))
    print(sub(num1=5, num2=6))
    print(div(num1=5, num2=6))
