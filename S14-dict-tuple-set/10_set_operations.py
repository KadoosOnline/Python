# Sets support the operations of mathematical set theory.
def main() -> None:
    python_students = {'Ali', 'Sara', 'Reza', 'Maryam'}
    linux_students = {'Reza', 'Maryam', 'Omid'}

    print('union       :', python_students | linux_students)
    print('intersection:', python_students & linux_students)
    print('difference  :', python_students - linux_students)
    print('symmetric   :', python_students ^ linux_students)

    # The same operations have method names too.
    print(python_students.union(linux_students))
    print(python_students.intersection(linux_students))
    print(python_students.difference(linux_students))

    print(linux_students.issubset(python_students))   # False

if __name__ == '__main__':
    main()
