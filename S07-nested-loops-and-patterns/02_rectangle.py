# A rectangle of stars: the outer loop counts the rows,
# the inner loop prints the characters of one row.
ROWS = 4
COLUMNS = 8

for row in range(ROWS):
    for column in range(COLUMNS):
        # end='' keeps the cursor on the same line
        print('*', end=' ')
    # this print() ends the current line and starts a new one
    print()
