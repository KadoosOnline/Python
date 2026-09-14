numbers = [1, 2, 3, 4, 5, 6]

# map() applies a function to every item.
print(list(map(lambda x: x ** 2, numbers)))
# The comprehension says the same thing more clearly:
print([x ** 2 for x in numbers])

# filter() keeps the items for which the function returns True.
print(list(filter(lambda x: x % 2 == 0, numbers)))
print([x for x in numbers if x % 2 == 0])

# map() shines when the function already exists and has a name.
words = ['10', '20', '30']
print(list(map(int, words)))
print(list(map(str.upper, ['ali', 'sara'])))

# map() with several sequences works like zip().
prices = [1000, 2000]
quantities = [3, 5]
print(list(map(lambda p, q: p * q, prices, quantities)))

# Both return an ITERATOR, not a list: they compute nothing until you loop.
result = map(lambda x: x * 2, numbers)
print(result)              # <map object ...>
print(list(result))        # now it is computed
print(list(result))        # [] - an iterator can only be read once!
