# A parameter is a variable that receives a value when the function is called.
def hello(name):
    print('Hello', name)

# 'Matin', 'Maryam' and 'Raha' are the arguments.
hello('Matin')
hello('Maryam')
hello('Raha')

# A function may have several parameters; their ORDER matters.
def introduce(name, city):
    print(f'{name} lives in {city}.')

introduce('Ali', 'Rasht')
