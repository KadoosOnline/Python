# A variable created inside a function only exists inside that function.
def calculate():
    result = 42          # local variable
    print('inside: ', result)

calculate()

# This line would raise NameError: name 'result' is not defined
# print('outside:', result)

# Two functions may use the same name without disturbing each other.
def first():
    value = 1
    print('first:', value)

def second():
    value = 2
    print('second:', value)

first()
second()
