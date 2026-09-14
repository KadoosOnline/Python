# In a condition, Python treats these values as False:
#   False, None, 0, 0.0, '', [], (), {}, set(), range(0)
# Everything else is True.

for value in [0, 1, '', 'a', [], [0], {}, {'a': 1}, None, set()]:
    print(repr(value), '->', bool(value))

print('---')

names: list[str] = []

# Not Pythonic:
if len(names) == 0:
    print('empty (long version)')

# Pythonic:
if not names:
    print('empty (short version)')

names.append('Ali')
if names:
    print('there is at least one name')

# Careful: 'if x:' and 'if x is not None:' are NOT the same.
count = 0
if not count:
    print('0 is falsy, so this runs')
if count is not None:
    print('...but the value is not None')

# So when 0 or '' are legal values, always test against None explicitly.
def greet(name: str | None = None) -> None:
    if name is None:          # NOT "if not name"
        name = 'guest'
    print('Hello', name)

greet()
greet('')
