# Adding every item of a list, the manual way.
numbers = [200, 350, 40, 1000, 270]

total = 0
for number in numbers:
    total = total + number
    # short form: total += number

print('Total:', total)
print('Average:', total / len(numbers))
