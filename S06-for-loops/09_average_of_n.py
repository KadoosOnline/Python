# Two accumulators at the same time: a total and a counter.
user_input = input('How many numbers do you want to enter? ')
count = int(user_input)

total = 0

for i in range(count):
    number = float(input(f'Number {i + 1}: '))
    total += number

# Dividing by zero must be avoided when the user answers 0.
if count > 0:
    print('Average:', total / count)
else:
    print('No number was entered.')
