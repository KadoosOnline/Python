# The items of a list can themselves be lists.
def main() -> None:
    matrix = [
        [4, 17, 81],
        [11, 41, 17],
        [20, 12, 13],
    ]

    # A new row is appended like any other item.
    matrix.append([4, 5, 6])

    print(matrix[1][1])     # 41  -> row 1, column 1

    # Two loops to visit every value.
    for row in matrix:
        for value in row:
            print(value, end='\t')
        print()

if __name__ == '__main__':
    main()
