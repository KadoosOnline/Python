# One 'try' can have several 'except' blocks: Python runs the first one
# that matches the exception that happened.
text = 'AA'          # try also with '10' and with '1'
numbers = [1, 2, 3]

try:
    index = int(text)          # may raise ValueError
    print(numbers[index])      # may raise IndexError
except ValueError:
    print('Conversion error!')
except IndexError:
    print('Index error!')

# Several exceptions can share the same block.
try:
    index = int(text)
    print(numbers[index])
except (ValueError, IndexError) as e:
    print('Something went wrong:', type(e).__name__, '-', e)
