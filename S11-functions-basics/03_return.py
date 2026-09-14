# 'return' sends a value back to the place where the function was called.
def add(number1, number2):
    total = number1 + number2
    return total

# The returned value can be stored ...
c = add(3, 2)
print(c)

d = add(7, 4)
print(d)

# ... or used directly.
print(add(3, 2))
print(add(1, 2) + add(3, 4))

# 'return' also ENDS the function immediately.
def first_positive(a, b):
    if a > 0:
        return a
    return b            # only reached when a is not positive

print(first_positive(-5, 8))
