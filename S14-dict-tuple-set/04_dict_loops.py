def main() -> None:
    student = {
        'name': 'alireza',
        'age': 20,
        'email': 'alireza@kadoosedu.ir',
    }

    # Looping over a dictionary gives the KEYS.
    for key in student:
        print(key, ':', student[key])

    print('---')

    # The three views:
    print(list(student.keys()))     # ['name', 'age', 'email']
    print(list(student.values()))   # ['alireza', 20, 'alireza@kadoosedu.ir']
    print(list(student.items()))    # [('name', 'alireza'), ...]

    print('---')

    # items() gives the key and the value together - the usual way.
    for key, value in student.items():
        print(f'{key} -> {value}')

if __name__ == '__main__':
    main()
