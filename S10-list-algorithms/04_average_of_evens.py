# Average of the even numbers only: we need a total AND a counter,
# because we do not know in advance how many even numbers there are.
numbers = [30, 20, 45, 18, -7, 22]

total = 0
counter = 0

for number in numbers:
    if number % 2 == 0:
        total += number
        counter += 1

# Guard against a list without any even number.
if counter == 0:
    print('There is no even number in the list.')
else:
    print('Average of the even numbers:', total / counter)
