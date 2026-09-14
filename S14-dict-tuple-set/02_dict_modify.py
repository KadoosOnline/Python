# A dictionary is mutable: keys can be added, changed and removed.
def main() -> None:
    student = {'name': 'Ali', 'age': 20}

    student['age'] = 21              # change an existing key
    student['city'] = 'Rasht'        # a key that does not exist is CREATED
    print(student)

    student.update({'age': 22, 'email': 'ali@kadoosedu.ir'})
    print(student)

    removed = student.pop('email')   # remove and return the value
    print('removed:', removed)

    del student['city']              # remove without returning
    print(student)

    student.clear()
    print(student)                   # {}

if __name__ == '__main__':
    main()
