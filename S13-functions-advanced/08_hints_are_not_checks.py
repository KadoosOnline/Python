# Python does NOT check the type hints while the program runs.
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))          # 5, as expected

# The hints say "int", but this call still works, because '+' also works
# on two strings. The editor will warn us; Python will not.
print(add('Hi', 'Hello'))  # 'HiHello'

# If we really want to refuse wrong types, we must check by hand.
def strict_add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('strict_add() only accepts integers')
    return a + b

print(strict_add(2, 3))
# strict_add('Hi', 'Hello')  ->  TypeError
