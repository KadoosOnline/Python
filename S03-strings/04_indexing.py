# Every character has a position (an index). Counting starts at 0.
#
#   K  a  d  o  o  s
#   0  1  2  3  4  5      <- positive indexes
#  -6 -5 -4 -3 -2 -1      <- negative indexes (from the end)

name = 'Kadoos'

print(name[0])    # 'K'  -> the first character
print(name[2])    # 'd'
print(name[-1])   # 's'  -> the last character
print(name[-2])   # 'o'

# An index that does not exist raises an IndexError:
# print(name[10])  ->  IndexError: string index out of range
