# Numbers and strings are IMMUTABLE: the function works on a copy.
def try_to_change(number):
    number += 1
    print('inside: ', number)

value = 10
try_to_change(value)
print('outside:', value)     # 10 -> unchanged

# Lists are MUTABLE: the function receives the SAME list, not a copy.
def add_item(items):
    items.append('new')

my_list = ['a', 'b']
add_item(my_list)
print(my_list)               # ['a', 'b', 'new'] -> changed!

# When you do not want that, pass a copy.
def add_item_safely(items):
    items = items.copy()
    items.append('new')
    return items

original = ['a', 'b']
changed = add_item_safely(original)
print(original, changed)
