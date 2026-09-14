# An f-string is a string with the letter f in front of it.
# Anything inside { } is evaluated and inserted into the text.
name = 'Noshad'
age = 20

print(f'{name} is {age} years old.')

# Any expression is allowed inside the braces.
print(f'Next year {name} will be {age + 1}.')

# It works with items of a list ...
numbers = [3, 5, 7, 18, -9]
print(f'My number: {numbers[2]}')

# ... and with items of a dictionary.
person = {
    'name': 'Mehrsa',
    'age': 15,
    'city': 'Rasht',
}
print(f"My name is {person['name']} and I live in {person['city']}.")
