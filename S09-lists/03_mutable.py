# A list is MUTABLE: an item can be replaced without creating a new list.
cars = ['BMW', 'Benz', 'Pride']

cars[2] = 'Peugeot'
print(cars)             # ['BMW', 'Benz', 'Peugeot']

# A whole slice can be replaced as well.
cars[0:2] = ['Mazda', 'Kia']
print(cars)

# Remember: a string cannot be changed like this,
#   name = 'kadoos'
#   name[0] = 'K'      ->  TypeError
