# A condition can be written on a single character of a string.
name = input('Enter your name: ')

# name[0] is the first character. An empty answer would crash the program,
# so we check the length first.
if len(name) > 0 and name[0].lower() == 's':
    print('Salam')
else:
    print('Hello')
