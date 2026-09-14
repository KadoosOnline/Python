# The complete shape:
#   try     -> the risky code
#   except  -> what to do when it fails
#   else    -> runs only when NOTHING failed
#   finally -> runs ALWAYS (success or failure), used to clean up
user_input = input('Enter a number: ')

try:
    number = int(user_input)
    x = 10 / number
    print(x)
except ZeroDivisionError:
    print('Division by zero error')
except ValueError:
    print('That was not a number')
else:
    print('The division is done!')
finally:
    print('Error or no error, this always runs.')
