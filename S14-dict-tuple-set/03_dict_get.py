# Reading a key that does not exist with [] raises a KeyError.
def main() -> None:
    student = {'name': 'Ali', 'age': 20}

    # print(student['city'])   ->  KeyError: 'city'

    # get() returns None instead of crashing ...
    print(student.get('city'))              # None

    # ... or a default value that we choose.
    print(student.get('city', 'unknown'))   # 'unknown'

    # The safe pattern with 'in':
    if 'city' in student:
        print(student['city'])
    else:
        print('the key "city" does not exist')

    # setdefault() reads the key, and creates it when it is missing.
    print(student.setdefault('city', 'Rasht'))
    print(student)

if __name__ == '__main__':
    main()
