# A function that only prints does NOT give a value back:
# its result is the special value None.
def show_sum(a, b):
    print(a + b)

result = show_sum(2, 3)
print(result)            # None

# A function that returns can be reused in other calculations.
def get_sum(a, b):
    return a + b

result = get_sum(2, 3)
print(result * 10)       # 50

# Rule of thumb: compute with 'return', display with 'print' - not both.
