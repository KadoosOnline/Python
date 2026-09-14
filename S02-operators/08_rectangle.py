# Area and perimeter of a rectangle.
length_input = input('Length of the rectangle: ')
width_input = input('Width of the rectangle: ')

length = float(length_input)
width = float(width_input)

area = length * width
perimeter = (length + width) * 2

print('Area:     ', area)
print('Perimeter:', perimeter)
