# Classic operations on a square matrix.
matrix = [
    [4, 17, 81],
    [11, 41, 17],
    [20, 12, 13],
]

SIZE = len(matrix)

# Total of every row.
for i in range(SIZE):
    print(f'sum of row {i}:', sum(matrix[i]))

# Total of every column: the column index stays fixed while the row moves.
for column in range(SIZE):
    column_total = 0
    for row in range(SIZE):
        column_total += matrix[row][column]
    print(f'sum of column {column}:', column_total)

# The main diagonal is made of the items where row == column.
diagonal_total = 0
for i in range(SIZE):
    diagonal_total += matrix[i][i]
print('sum of the diagonal:', diagonal_total)

# The biggest value of the whole matrix.
largest = matrix[0][0]
for row in matrix:
    for value in row:
        if value > largest:
            largest = value
print('largest value:', largest)
