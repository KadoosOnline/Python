import random

# random() -> a decimal number between 0.0 and 1.0 (1.0 excluded)
print(random.random())

# uniform(a, b) -> a decimal number between a and b
print(random.uniform(5, 10))

# A percentage with two decimals:
print(round(random.random() * 100, 2))
