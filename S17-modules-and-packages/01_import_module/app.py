# 'import math_module' loads the file math_module.py that sits next to this one.
# The functions are then reached through the module name.
import math_module

if __name__ == '__main__':
    result = math_module.add(num1=5, num2=6)
    print(result)

# The first time a module is imported, Python stores a compiled copy in a
# folder called __pycache__ so the next import is faster. It can be deleted
# at any time; it is never part of the source code.
