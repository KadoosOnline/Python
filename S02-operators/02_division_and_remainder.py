# '/' always gives a float, even when the division is exact.
print(10 / 2)     # 5.0
print(10 / 3)     # 3.3333333333333335

# '//' throws away the decimal part and gives the whole number of times
# the second value fits into the first.
print(10 // 3)    # 3

# '%' gives what is left over. It is the tool we use to test even/odd numbers
# and to know whether one number divides another.
print(10 % 3)     # 1
print(10 % 2)     # 0  -> 10 is even
print(7 % 2)      # 1  -> 7 is odd
