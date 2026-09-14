# Several names can be imported in one line.
from math_module import add, mul

# 'from math_module import *' would import everything, but then the reader of
# the file no longer knows where 'add' comes from. Avoid it.

if __name__ == '__main__':
    print(add(num1=5, num2=6))
    print(mul(num1=5, num2=6))
