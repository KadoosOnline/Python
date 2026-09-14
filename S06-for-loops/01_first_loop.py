# Without a loop we would have to write print() five times.
# 'for' repeats the indented block once for every value produced by range().
for i in range(5):
    print(i, 'Hello Kadoos!')

print('---')

# range(1, 5) starts at 1 and STOPS BEFORE 5 -> 1, 2, 3, 4
for i in range(1, 5):
    print(i, 'Hello Kadoos!')
