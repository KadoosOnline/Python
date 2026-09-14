# Thanks to the re-exports in __init__.py, we no longer have to know
# in which module of the package each function lives.
from math_package import add, mul, sub, div

if __name__ == '__main__':
    print(add(num1=5, num2=6))
    print(mul(num1=5, num2=6))
    print(sub(num1=5, num2=6))
    print(div(num1=5, num2=6))
