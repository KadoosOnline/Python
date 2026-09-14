# 'sum', 'max', 'min', 'list', 'str', 'input' ... are names of built-in things.
# If you use them as variable names, the built-in version disappears.
numbers = [1, 2, 3]

sum = 0                 # BAD: the built-in function sum() is now hidden
for n in numbers:
    sum += n
print(sum)              # works ...

# ... but now this line would raise:
#   TypeError: 'int' object is not callable
# print(sum(numbers))

# Always prefer a descriptive name instead:
total = 0
for n in numbers:
    total += n
print(total)
print(sum)              # still the integer, the damage is done in this file
