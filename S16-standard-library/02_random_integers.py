import random

# randint(a, b) -> a whole number between a and b, BOTH included.
x = random.randint(1, 6)
y = random.randint(1, 6)
print(f'{x}, {y}')

# randrange() works like range(): the last value is NOT included.
print(random.randrange(1, 10))        # 1..9
print(random.randrange(0, 100, 5))    # 0, 5, 10, ... 95
