# input() always returns a string, even when the user types digits.
# To calculate with it we must convert (cast) it to a number first.
user_input = input('Enter a number: ')

print('Before conversion:', type(user_input))   # <class 'str'>

number = int(user_input)                        # str -> int
print('After conversion: ', type(number))       # <class 'int'>

number = number + 2
print('Your number plus 2 is:', number)

# Other useful conversions:
print(float('3.5'))   # str   -> float
print(int(3.9))       # float -> int (the decimal part is cut off, NOT rounded)
print(str(25))        # int   -> str
