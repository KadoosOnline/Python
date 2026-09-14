# Counting backwards with a negative step.
user_input = input('Start the countdown from: ')
start = int(user_input)

for i in range(start, 0, -1):
    print(i)

print('Lift off!')
