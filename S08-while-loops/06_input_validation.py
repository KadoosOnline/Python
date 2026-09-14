# A very common use of 'while': keep asking until the answer makes sense.
while True:
    user_input = input('Enter your age (1-120): ')

    if not user_input.isdigit():
        print('Please type digits only.')
        continue

    age = int(user_input)

    if age < 1 or age > 120:
        print('The age must be between 1 and 120.')
        continue

    break        # the value is valid, leave the loop

print('Your age is', age)
