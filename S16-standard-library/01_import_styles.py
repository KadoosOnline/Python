# Way 1: import the whole module, then use 'module.name'
import random
print(random.randint(1, 6))

# Way 2: import it under a shorter name
import random as rnd
print(rnd.randint(1, 6))

# Way 3: import only what we need, then use the name directly
from random import randint, choice
print(randint(1, 6))
print(choice(['red', 'green', 'blue']))

# 'from module import *' imports everything. Avoid it: you no longer know
# where a name comes from, and it can silently overwrite your own names.
