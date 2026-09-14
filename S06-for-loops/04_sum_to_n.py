# The accumulator pattern:
#   1) start with a variable set to 0
#   2) add something to it on every turn of the loop
#   3) use it after the loop
total = 0

for i in range(10001):      # 0, 1, 2, ..., 10000
    total = total + i
    # the short form is:  total += i

print(total)
