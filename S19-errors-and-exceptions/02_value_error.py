# int() raises ValueError when the text is not a number.
text = 'Kadoos'

try:
    age = int(text)
    print(age)
except ValueError as e:
    # 'as e' gives us the exception object, which contains the message.
    print("Can't convert this string to an integer!")
    print('The message of Python was:', e)
