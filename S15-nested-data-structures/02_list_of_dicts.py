# A list of dictionaries is how a table of data is normally represented:
# one dictionary per row, the keys are the column names.
def main() -> None:
    students = [
        {'name': 'Ali', 'age': 18, 'email': 'ali@kadoosedu.ir'},
        {'name': 'Reza', 'age': 20, 'email': 'reza@kadoosedu.ir'},
        {'name': 'Ahmad', 'age': 23, 'email': 'ahmad@kadoosedu.ir'},
    ]

    print(students[1]['name'])     # Reza

    # NOTE: use double quotes OUTSIDE the f-string when the keys are written
    # with single quotes - it works on every version of Python.
    print('Name\tAge\tEmail')
    for student in students:
        print(f"{student['name']}\t{student['age']}\t{student['email']}")

    # Filtering the table.
    adults = []
    for student in students:
        if student['age'] >= 20:
            adults.append(student['name'])
    print('20 or older:', adults)

if __name__ == '__main__':
    main()
