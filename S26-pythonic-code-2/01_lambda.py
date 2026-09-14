# 'lambda arguments: expression' creates a function without a name.
# It can only contain ONE expression, and it returns it automatically.
double = lambda x: x * 2
print(double(5))

# Exactly the same thing, written normally - and this version is better,
# because the function then has a real name in the tracebacks.
def double_v2(x):
    return x * 2

print(double_v2(5))

# A lambda earns its place when a function is needed for one single moment,
# usually as an argument of another function.
students = [('Ali', 18), ('Sara', 20), ('Reza', 12)]
print(sorted(students, key=lambda student: student[1]))

# Several parameters are allowed.
add = lambda a, b: a + b
print(add(2, 3))

# Default values too.
greet = lambda name='guest': f'Hello {name}'
print(greet(), greet('Ali'))

# Rule: if you feel like giving your lambda a name with '=',
# write a normal 'def' instead.
