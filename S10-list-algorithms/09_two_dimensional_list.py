# A list whose items are themselves lists is a 2-D list (a matrix).
matrix = [
    [4, 17, 81],
    [11, 41, 17],
    [20, 12, 13],
]

# Two indexes: first the row, then the column.
print(matrix[1][1])      # 41
print(matrix[0])         # the whole first row

# A new row can be appended like any other item.
matrix.append([4, 5, 6])

# Printing a matrix needs two loops.
for row in matrix:
    for value in row:
        print(value, end='\t')
    print()
