# A comparison is an expression whose value is either True or False.
print(5 > 3)      # True
print(5 < 3)      # False
print(5 == 5)     # True   -> '==' asks "are they equal?"
print(5 != 5)     # False  -> '!=' asks "are they different?"
print(5 >= 5)     # True
print(5 <= 4)     # False

# Careful: '=' stores a value, '==' compares two values.
age = 18          # assignment
print(age == 18)  # comparison -> True

# The result of a comparison is a real value of type bool.
result = 10 > 2
print(result, type(result))
