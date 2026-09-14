# An 'if' inside a loop lets us accumulate only some of the values.
total = 0

for i in range(10001):
    if i % 2 == 0:
        total += i

print('Sum of the even numbers from 0 to 10000:', total)

# The same result without an 'if', by making range() jump two by two:
total = 0
for i in range(0, 10001, 2):
    total += i
print('Same result with a step of 2:', total)
