# Without a try, this line stops the whole program:
#     x = 10 / 0
#     ZeroDivisionError: division by zero

# 'try' contains the risky code, 'except' says what to do when it fails.
try:
    x = 10 / 0
    print(x)
except ZeroDivisionError:
    print('Division by zero error')

print('The program continues normally.')
