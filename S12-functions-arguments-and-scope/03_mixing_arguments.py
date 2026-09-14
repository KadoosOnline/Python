def welcome(name='Omid', lastname='Shabani'):
    print('Welcome', name, lastname)

welcome(lastname='Ahmadi')                    # skip the first parameter
welcome(lastname='Raeisi', name='Ebrahim')    # both by name

# Positional arguments must always come BEFORE keyword arguments.
# This line would be a SyntaxError:
#   welcome(name='Ali', 'Ahmadi')

def add(num1=0.0, num2=0.0):
    return num1 + num2

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))

print(add(num2=num2, num1=num1))
