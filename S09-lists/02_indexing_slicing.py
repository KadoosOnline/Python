# Indexes and slices work exactly like they do on strings.
cars = ['BMW', 'Benz', 'Pride', 'Paykan', 'Ford']

print(cars[0])      # 'BMW'
print(cars[-1])     # 'Ford'   -> the last one
print(cars[1:3])    # ['Benz', 'Pride']
print(cars[:2])     # ['BMW', 'Benz']
print(cars[2:])     # ['Pride', 'Paykan', 'Ford']
print(cars[::-1])   # the list reversed
