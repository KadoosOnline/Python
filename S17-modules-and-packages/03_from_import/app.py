# 'from ... import ...' brings the name directly into our file,
# so we call it without the module prefix.
from math_module import add

if __name__ == '__main__':
    result = add(num1=5, num2=6)
    print(result)
