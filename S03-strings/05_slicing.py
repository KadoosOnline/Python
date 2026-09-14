# A slice takes a PIECE of the string: text[start:stop:step]
# 'start' is included, 'stop' is NOT included.
name = 'Kadoos'

print(name[1:4])    # 'ado'   -> characters 1, 2, 3
print(name[:3])     # 'Kad'   -> from the beginning to index 2
print(name[2:])     # 'doos'  -> from index 2 to the end
print(name[:])      # 'Kadoos'-> a full copy
print(name[::2])    # 'Kdo'   -> every second character
print(name[::-1])   # 'soodaK'-> the string reversed
print(name[-3:])    # 'oos'   -> the last three characters
