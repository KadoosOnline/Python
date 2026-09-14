import random

# The "random" numbers of a computer are computed from a starting value
# called the seed. With the same seed we always get the same sequence -
# which is exactly what we want while testing a program.
random.seed(42)
print([random.randint(1, 100) for _ in range(5)])

random.seed(42)
print([random.randint(1, 100) for _ in range(5)])   # the same five numbers

# Without a seed, Python uses the current time, so the numbers change.
random.seed()
print([random.randint(1, 100) for _ in range(5)])
