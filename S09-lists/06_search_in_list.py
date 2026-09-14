cars = ['BMW', 'Benz', 'Pride', 'Paykan', 'Ford', 'Benz']

car = input('Enter the car name: ')

# 'in' tells us whether a value exists in the list.
if car in cars:
    print(car, 'found.')
else:
    print(car, 'not found!')

# index() gives the position of the FIRST occurrence.
print(cars.index('Pride'))

# count() says how many times a value appears.
print(cars.count('Benz'))    # 2
