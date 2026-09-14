# '**' collects all the extra KEYWORD arguments into a dictionary.
def show_info(**kwargs):
    print('kwargs is:', kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, ':', value)

show_info(name='Ali', age=22, city='Rasht')
print()
show_info(Riyazi=20, Farsi=19, Dini=12, Varzesh=18)

# '**' at the call site spreads a dictionary into keyword arguments.
data = {'name': 'Sara', 'age': 19}
show_info(**data)
