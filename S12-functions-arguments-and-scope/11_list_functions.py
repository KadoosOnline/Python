# Functions that take a list as a parameter and return a value.

def total_of(numbers):
    'Return the sum of a list of numbers.'
    total = 0
    for number in numbers:
        total += number
    return total

def average_of(numbers):
    'Return the average, or 0 for an empty list.'
    if len(numbers) == 0:
        return 0
    return total_of(numbers) / len(numbers)

def bigger_list(list1, list2):
    'Return the list whose items add up to more.'
    if total_of(list1) > total_of(list2):
        return list1
    return list2

def squares_of(numbers):
    'Return a NEW list with the square of every item.'
    result = []
    for number in numbers:
        result.append(number * number)
    return result

def main():
    l1 = [3, 2, 5, 6]
    l2 = [10, 2]

    print('total  :', total_of(l1))
    print('average:', average_of(l1))
    print('bigger :', bigger_list(l1, l2))
    print('squares:', squares_of(l1))
    print('empty  :', average_of([]))

if __name__ == '__main__':
    main()
