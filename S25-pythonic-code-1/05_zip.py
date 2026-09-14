subjects = ['math', 'physics', 'english']
scores = [20, 18, 19]
teachers = ['Ahmadi', 'Rezaei', 'Karimi']

# zip() walks several sequences at the same time.
for subject, score in zip(subjects, scores):
    print(f'{subject}: {score}')

print('---')

# It accepts more than two.
for subject, score, teacher in zip(subjects, scores, teachers):
    print(f'{subject:<10}{score:>3}  ({teacher})')

print('---')

# zip() stops at the SHORTEST sequence.
print(list(zip([1, 2, 3], 'ab')))

# strict=True (Python 3.10+) raises an error when the lengths differ,
# which catches a bug instead of hiding it.
try:
    print(list(zip([1, 2, 3], 'ab', strict=True)))
except ValueError as e:
    print('strict zip:', e)

# Building a dictionary out of two lists.
print(dict(zip(subjects, scores)))

# zip(*matrix) transposes a matrix - a classic trick.
matrix = [[1, 2, 3], [4, 5, 6]]
print([list(row) for row in zip(*matrix)])
