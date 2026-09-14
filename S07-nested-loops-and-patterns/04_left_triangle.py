# Row 0 gets 0 stars, row 1 gets 1 star, row 2 gets 2 stars ...
# Version 1: the inner loop simply runs 'i' times. This is the clean way.
for i in range(5):
    for j in range(i):
        print('*', end=' ')
    print()

print('---')

# Version 2: the inner loop always runs 5 times but only prints when i > j.
# It gives the same drawing; it just does more useless turns.
for i in range(5):
    for j in range(5):
        if i > j:
            print('*', end=' ')
    print()
