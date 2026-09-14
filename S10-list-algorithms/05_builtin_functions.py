# Python already knows how to do all of that. Use the built-in functions:
# they are shorter, faster and impossible to get wrong.
numbers = [30, 20, 45, 18, -7, 22]

print('len:', len(numbers))
print('sum:', sum(numbers))
print('max:', max(numbers))
print('min:', min(numbers))
print('avg:', sum(numbers) / len(numbers))

# They work on strings too.
words = ['pear', 'apple', 'banana']
print(max(words))            # the last one in alphabetical order
print(min(words, key=len))   # the shortest word
