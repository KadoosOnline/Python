VALUE = 1
LENGTH = 4

# A 2-D list: the inner comprehension builds one row,
# the outer one repeats it.
two_d = [[VALUE for _ in range(LENGTH)] for _ in range(LENGTH)]
print(two_d)

# NEVER write [[0] * 4] * 4 : every row would be the SAME list.
wrong = [[0] * 4] * 4
wrong[0][0] = 9
print(wrong)          # every row changed!

right = [[0] * 4 for _ in range(4)]
right[0][0] = 9
print(right)          # only the first row changed

# A multiplication table.
table = [[i * j for j in range(1, 5)] for i in range(1, 5)]
for row in table:
    print(row)

# Flattening a 2-D list: the two 'for' are read from left to right,
# exactly like nested loops.
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [value for row in matrix for value in row]
print(flat)
