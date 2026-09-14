# A 'for' loop can walk directly through the characters of a string.
name = 'Kadoos'

for char in name:
    print(char, end=' ')
print()

# Counting the vowels of a sentence.
sentence = input('Enter a sentence: ')
vowels = 0

for char in sentence.lower():
    if char in 'aeiou':
        vowels += 1

print('Number of vowels:', vowels)
