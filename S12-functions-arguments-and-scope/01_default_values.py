# A parameter can have a default value, used when the caller omits it.
def welcome(name='Omid', lastname='Shabani'):
    print('Welcome', name, lastname)

welcome()                       # both defaults
welcome('Alireza')              # only 'lastname' keeps its default
welcome('Alireza', 'Ghasemi')   # no default used

# Parameters WITH a default must come after the ones without.
def calculate_price(price, tax=0.0):
    return price * (1 + tax)

print(calculate_price(100000))         # 100000.0
print(calculate_price(100000, 0.2))    # 120000.0
