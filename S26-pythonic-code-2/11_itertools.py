import itertools

# count() - an infinite counter
for i in itertools.count(10, 5):
    if i > 30:
        break
    print(i, end=' ')
print()

# cycle() - repeats a sequence for ever
colors = itertools.cycle(['red', 'green', 'blue'])
print([next(colors) for _ in range(7)])

# repeat() - the same value n times
print(list(itertools.repeat('ok', 3)))

# chain() - glues several sequences into one
print(list(itertools.chain([1, 2], [3, 4], 'ab')))

# islice() - a slice of any iterator (even an infinite one)
print(list(itertools.islice(itertools.count(), 5)))

# combinations() / permutations() / product()
print(list(itertools.combinations('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))
print(list(itertools.product([1, 2], 'ab')))

# groupby() - groups CONSECUTIVE items, so sort first!
students = [
    {'name': 'Ali', 'city': 'Rasht'},
    {'name': 'Sara', 'city': 'Rasht'},
    {'name': 'Reza', 'city': 'Lahijan'},
]
students.sort(key=lambda s: s['city'])
for city, group in itertools.groupby(students, key=lambda s: s['city']):
    print(city, [s['name'] for s in group])

# accumulate() - the running total
print(list(itertools.accumulate([1, 2, 3, 4])))
