# When an if/else only chooses between two VALUES, Python offers a one-line form:
#     value_if_true if condition else value_if_false
age = int(input('Enter your age: '))

status = 'adult' if age >= 18 else 'minor'
print(status)

# The long version does exactly the same thing:
if age >= 18:
    status = 'adult'
else:
    status = 'minor'
print(status)

# It is often used directly inside a print():
number = 7
print(f'{number} is', 'even' if number % 2 == 0 else 'odd')
