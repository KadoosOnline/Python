# A condition at the END filters: it decides WHICH items are kept.
squares_of_even = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares_of_even)

names = ['Ali', 'Sara', 'Reza', 'Arad']
print([name for name in names if name.startswith('A')])

# A ternary at the BEGINNING transforms: it decides WHAT is stored.
print(['even' if x % 2 == 0 else 'odd' for x in range(6)])

# Both at the same time.
print([x * 2 if x > 0 else 0 for x in [-3, 1, -5, 7] if x != 1])

# Remember the two positions:
#   [ <expression, may use a ternary>  for x in seq  if <filter> ]

# A realistic example: the passing students of a list of dictionaries.
students = [
    {'name': 'Ali', 'score': 18},
    {'name': 'Sara', 'score': 8},
    {'name': 'Reza', 'score': 12},
]
print([s['name'] for s in students if s['score'] >= 10])
