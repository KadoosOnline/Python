# A comprehension builds a list in one expression.
#   [ WHAT      for ITEM in SEQUENCE ]

# The long way:
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

# The Pythonic way:
squares = [x ** 2 for x in range(10)]
print(squares)

# It works on anything we can loop over.
names = ['ali', 'sara', 'reza']
print([name.capitalize() for name in names])
print([len(name) for name in names])

# Turning the lines of a file into numbers (see session 18).
lines = ['22\n', '-7\n', '13\n']
print([int(line.strip()) for line in lines])

# Careful: a comprehension is for BUILDING a list.
# When you only want a side effect (printing), use a normal for loop.
