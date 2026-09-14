# 'elif' means "else if". Python tests the branches from top to bottom and
# runs ONLY the first one whose condition is True.
user_input = input('Enter a number (1-7): ')

if user_input == '1':
    print('Shanbe')
elif user_input == '2':
    print('Yekshanbe')
elif user_input == '3':
    print('Doshanbe')
elif user_input == '4':
    print('Seshanbe')
elif user_input == '5':
    print('Chaharshanbe')
elif user_input == '6':
    print('Panjshanbe')
elif user_input == '7':
    print('Jome')
else:
    print('Error: the number must be between 1 and 7')
