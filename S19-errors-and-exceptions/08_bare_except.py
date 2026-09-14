# A bare 'except:' catches EVERYTHING, even the mistakes in your own code
# and Ctrl-C. The bug then becomes invisible - never do this.
try:
    x = 10 / 0
except:
    print('Something is wrong!')      # but WHAT exactly? we have no idea

# Catch the exception you expect ...
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print('Clear message:', e)

# ... or, if you really must catch everything, at least keep the object.
try:
    x = 10 / 0
except Exception as e:
    print(f'{type(e).__name__}: {e}')
