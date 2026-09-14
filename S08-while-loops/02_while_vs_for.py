# Use 'for' when you know in advance how many turns you need.
for i in range(1, 6):
    print(i, end=' ')
print()

# Use 'while' when the number of turns depends on something that happens
# during the loop.
i = 1
while i <= 5:
    print(i, end=' ')
    i += 1
print()
