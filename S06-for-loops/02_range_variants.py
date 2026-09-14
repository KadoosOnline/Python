# range(stop)              -> 0, 1, ..., stop-1
for i in range(5):
    print(i, end=' ')
print()

# range(start, stop)       -> start, ..., stop-1
for i in range(2, 6):
    print(i, end=' ')
print()

# range(start, stop, step) -> jumps of 'step'
for i in range(0, 21, 5):
    print(i, end=' ')
print()

# A negative step counts backwards.
for i in range(10, 0, -2):
    print(i, end=' ')
print()

# The 'stop' value is NEVER included - this is the most common beginner mistake.
# To print 1..10 we need range(1, 11):
for i in range(1, 11):
    print(i, end=' ')
print()
