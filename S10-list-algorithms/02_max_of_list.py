# Finding the biggest item.
# The trick: start with the FIRST item as the current champion,
# then compare it with every other item.
numbers = [30, 20, 45, 18, -7, 22]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print('Max:', largest)

# Starting from 0 instead of numbers[0] would be a bug:
# with a list of only negative numbers the answer would wrongly be 0.
