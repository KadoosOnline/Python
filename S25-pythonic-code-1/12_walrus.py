# The walrus operator ':=' assigns AND returns the value at the same time.
# It removes the duplicated call or the duplicated line.

# Without it:
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
if total > 10:
    print(f'the total {total} is big')

# With it:
if (total := sum(numbers)) > 10:
    print(f'the total {total} is big')

# Its best use: a read-until loop written without 'while True'.
while (answer := input('Say something (or "exit"): ')) != 'exit':
    print('You said:', answer)

# And inside a comprehension, to avoid computing the same thing twice.
words = ['python', 'is', 'wonderful']
print([length for word in words if (length := len(word)) > 3])

# Do not overuse it: when it makes the line hard to read,
# a normal assignment on its own line is better.
