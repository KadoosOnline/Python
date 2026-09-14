student = {'name': 'Ali', 'age': 20}

try:
    print(student['city'])
except KeyError as e:
    print('This key does not exist:', e)

# get() is the usual way to avoid the exception completely.
print(student.get('city', 'unknown'))
