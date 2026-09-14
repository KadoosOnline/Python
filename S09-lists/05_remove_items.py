numbers = [5, 20, -7, 8, 14]

# pop() removes an item BY POSITION and returns it.
last = numbers.pop()        # no argument -> the last item
print('Removed:', last, '->', numbers)

first = numbers.pop(0)      # by index
print('Removed:', first, '->', numbers)

# remove() removes the first item equal to the given VALUE.
numbers.remove(8)
print(numbers)

# del removes by index (or by slice) without returning anything.
del numbers[0]
print(numbers)

# clear() empties the list.
numbers.clear()
print(numbers)              # []
