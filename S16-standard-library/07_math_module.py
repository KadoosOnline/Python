import math

print(math.pi)              # 3.141592653589793
print(math.e)

print(math.sqrt(16))        # 4.0  -> square root
print(math.pow(2, 10))      # 1024.0 (a float; the operator ** gives an int)
print(2 ** 10)              # 1024

print(math.factorial(5))    # 120
print(math.gcd(12, 18))     # 6  -> greatest common divisor

print(math.floor(3.7))      # 3  -> down
print(math.ceil(3.2))       # 4  -> up
print(math.fabs(-5))        # 5.0

# Area of a circle.
radius = float(input('Radius of the circle: '))
print('Area:', math.pi * radius ** 2)
