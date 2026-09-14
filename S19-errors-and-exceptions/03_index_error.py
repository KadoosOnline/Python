items = [10, 20, 30]

try:
    print(items[5])
except IndexError:
    print('This index does not exist!')

# The same protection without an exception:
index = 5
if 0 <= index < len(items):
    print(items[index])
else:
    print('index out of range (checked with an if)')
