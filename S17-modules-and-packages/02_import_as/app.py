# A module can be renamed while importing it. This is useful when the real
# name is long (you will see 'import pandas as pd' in real projects).
import math_module as m

if __name__ == '__main__':
    result = m.add(num1=5, num2=6)
    print(result)
