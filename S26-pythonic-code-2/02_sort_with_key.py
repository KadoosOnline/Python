students = [
    {'name': 'Ali', 'score': 18, 'age': 20},
    {'name': 'Sara', 'score': 20, 'age': 19},
    {'name': 'Reza', 'score': 12, 'age': 22},
]

# 'key' is a function that says WHAT to compare for each item.
print(sorted(students, key=lambda s: s['score']))
print(sorted(students, key=lambda s: s['score'], reverse=True))
print([s['name'] for s in sorted(students, key=lambda s: s['name'])])

# Sorting by two criteria: return a tuple.
print([s['name'] for s in sorted(students, key=lambda s: (-s['score'], s['name']))])

# operator.itemgetter / attrgetter are the faster, ready-made version.
from operator import itemgetter
print([s['name'] for s in sorted(students, key=itemgetter('age'))])

# min / max accept the same key.
print(max(students, key=lambda s: s['score'])['name'])
print(min(students, key=lambda s: s['age'])['name'])

# Sorting words by length, then alphabetically.
words = ['banana', 'kiwi', 'apple', 'fig']
print(sorted(words, key=lambda w: (len(w), w)))
