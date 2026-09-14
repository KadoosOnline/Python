import math

value = 3.567

print(round(value))         # 4     -> nearest whole number
print(round(value, 2))      # 3.57  -> two decimals
print(math.floor(value))    # 3     -> always down
print(math.ceil(value))     # 4     -> always up
print(int(value))           # 3     -> simply cuts the decimals

# Careful with negative numbers: int() and floor() are NOT the same.
print(int(-3.7), math.floor(-3.7))    # -3  and  -4

# Python uses "banker's rounding": .5 goes to the nearest EVEN number.
print(round(2.5), round(3.5))         # 2  and  4
