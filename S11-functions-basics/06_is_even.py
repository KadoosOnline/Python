# Three ways of writing the same function, from the longest to the shortest.

def is_even_v1(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_even_v2(number):
    if number % 2 == 0:
        return True
    return False            # the else is not needed: return already exits

def is_even_v3(number):
    return number % 2 == 0  # the comparison IS already True or False

number = 4

# A function that returns a bool can be used directly inside an if.
if is_even_v3(number):
    print('Even')
else:
    print('Odd')

print(is_even_v1(7), is_even_v2(7), is_even_v3(7))
