# A "method" is a function that belongs to a value and is called with a dot.
text = '  Kadoos Institute, Rasht  '

print(text.upper())            # everything in capitals
print(text.lower())            # everything in small letters
print(text.title())            # First Letter Of Each Word In Capitals
print(text.strip())            # remove the spaces at both ends
print(text.strip().center(40, '.'))

print(text.replace('Rasht', 'Tehran'))

# split() cuts a string into a list of pieces.
words = text.strip().split(' ')
print(words)                   # ['Kadoos', 'Institute,', 'Rasht']

# join() does the opposite: it glues a list of strings together.
print('-'.join(['2026', '09', '08']))

# Useful checks that return True or False:
print('12345'.isdigit())       # True  -> only digits
print('Kadoos'.isalpha())      # True  -> only letters
print('kadoos'.islower())      # True
