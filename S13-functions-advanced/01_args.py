# A '*' in front of a parameter collects ALL the extra positional arguments
# into a tuple. The name 'args' is only a convention.
def sum_numbers(*args):
    print('args is:', args, type(args))
    total = 0
    for number in args:
        total += number
    return total

print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40))
print(sum_numbers())              # an empty tuple -> 0

# A '*' at the CALL site does the opposite: it spreads a list into arguments.
numbers = [5, 10, 15]
print(sum_numbers(*numbers))
