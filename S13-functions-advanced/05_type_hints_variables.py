# A type hint says WHAT KIND of value a name is supposed to hold.
# It changes nothing at run time, but the editor can then warn us.
number: int = 23
PI: float = 3.14
name: str = 'Kadoos'
is_active: bool = True

user_input: str = input('Enter a number: ')
my_number: float = float(user_input)

print(number, PI, name, is_active, my_number)
