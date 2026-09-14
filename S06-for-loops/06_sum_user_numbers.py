# The loop can also contain an input(): here we read exactly five numbers.
total = 0

for i in range(5):
    user_input = input(f'Enter number {i + 1} of 5: ')
    number = float(user_input)
    total += number

print('Sum:', total)
