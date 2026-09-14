# When a function has several optional parameters, keyword arguments let us
# set only the one we care about.
def register(name, role='student', active=True):
    print(name, role, active)

register('Ali', active=False)     # 'role' keeps its default
register('Saeed')                 # everything default
register('Sara', 'teacher')       # 'role' given positionally

# Division with a safe default divisor.
def div(num1, num2=1.0):
    if num2 == 0:
        print('Cannot divide by zero!')
        return None
    return num1 / num2

number = float(input('Enter a number: '))
print(div(num1=number))           # divided by the default 1.0
print(div(number, 0))             # the guard protects us
