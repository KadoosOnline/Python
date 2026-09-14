# Same algorithm, with the comparison turned around.
numbers = [30, 20, 45, 18, -7, 22]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print('Min:', smallest)
