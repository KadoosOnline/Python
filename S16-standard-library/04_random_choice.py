import random

colors = ['red', 'green', 'blue']

# choice() -> ONE item
print(random.choice(colors))

# sample() -> k DIFFERENT items (no repetition)
print(random.sample(colors, 2))

# choices() -> k items WITH repetition allowed
print(random.choices(colors, k=5))

# choices() can also be given weights.
print(random.choices(colors, weights=[10, 1, 1], k=5))

# shuffle() mixes a list IN PLACE and returns None.
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
