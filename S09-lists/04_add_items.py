numbers = [10, 20, 30]

# append() adds ONE item at the end.
numbers.append(40)
print(numbers)          # [10, 20, 30, 40]

# insert() adds an item at a chosen position.
numbers.insert(0, 5)
print(numbers)          # [5, 10, 20, 30, 40]

# extend() adds all the items of another list.
numbers.extend([50, 60])
print(numbers)          # [5, 10, 20, 30, 40, 50, 60]

# Careful: append() with a list adds the LIST itself as one single item.
numbers.append([70, 80])
print(numbers)          # [..., 60, [70, 80]]

# '+' builds a new list without touching the originals.
print([1, 2] + [3, 4])
