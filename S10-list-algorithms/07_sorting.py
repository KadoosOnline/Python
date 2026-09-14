numbers = [30, 20, 45, 18, -7, 22]

# sorted() returns a NEW sorted list and leaves the original alone.
ordered = sorted(numbers)
print('sorted():', ordered)
print('original:', numbers)

# sort() sorts the list IN PLACE and returns None.
numbers.sort()
print('after sort():', numbers)

# Descending order.
numbers.sort(reverse=True)
print('descending:', numbers)

# reverse() just turns the list around, it does not sort.
numbers.reverse()
print('reversed:', numbers)

# Sorting text.
names = ['Reza', 'ali', 'Maryam']
print(sorted(names))                    # capitals come first
print(sorted(names, key=str.lower))     # case-insensitive order
