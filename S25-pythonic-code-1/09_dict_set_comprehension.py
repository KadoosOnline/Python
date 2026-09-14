names = ['Ali', 'Sara', 'Reza']
scores = [18, 20, 12]

# Dictionary comprehension: { KEY: VALUE for ... }
print({name: len(name) for name in names})
print({name: score for name, score in zip(names, scores)})
print({name: score for name, score in zip(names, scores) if score >= 15})

# Reversing a dictionary.
original = {'a': 1, 'b': 2}
print({value: key for key, value in original.items()})

# Set comprehension: { VALUE for ... } - duplicates disappear.
sentence = 'kadoos institute rasht'
print({letter for letter in sentence if letter != ' '})

# A generator expression uses ( ) and computes the values one by one,
# without building the whole list in memory (see session 26).
total = sum(x ** 2 for x in range(1_000_000))
print(total)
