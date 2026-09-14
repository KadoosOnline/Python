# Strings are compared character by character, and the comparison is
# case sensitive: 'Kadoos' and 'kadoos' are NOT equal.
name = input('Enter your name: ')

if name == 'kadoos':
    print('Welcome', name)
else:
    print('Access denied!')

# To ignore the capitals, lower the text before comparing.
if name.lower() == 'kadoos':
    print('(case-insensitive check) Welcome', name)
