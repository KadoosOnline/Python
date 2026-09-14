# The complete order of the parameters:
#   normal, with a default, *args, **kwargs
def demo(a, b=10, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print('args:', args)
    print('kwargs:', kwargs)

demo(1, 20, 30, 40, name='Ali', city='Rasht')
print()
demo(1)
