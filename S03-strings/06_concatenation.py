# '+' glues two strings together.
first_name = 'Ali'
last_name = 'Rezaei'

full_name = first_name + ' ' + last_name
print(full_name)

# '*' repeats a string.
print('-' * 30)
print('ab' * 3)

# '+' only works between two strings. This line would raise a TypeError:
# print('Score: ' + 20)
# The fix is to convert the number to text first:
print('Score: ' + str(20))
