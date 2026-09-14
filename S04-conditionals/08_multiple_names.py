# Accepting several valid names with 'or'.
name = input('Enter your name: ')

if name == 'alireza' or name == 'omid' or name == 'arad':
    print('Welcome', name)
else:
    print('Access denied!')

# A shorter and much more readable way (we will study lists in session 09):
if name in ('alireza', 'omid', 'arad'):
    print('(short version) Welcome', name)
