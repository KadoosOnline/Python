# A dictionary stores pairs of "key: value".
# The key is how we find the value again - there are no positions here.
def main() -> None:
    student = {
        'name': 'alireza',
        'age': 20,
        'email': 'alireza@kadoosedu.ir',
    }

    # It can also be written on a single line:
    # student = {'name': 'alireza', 'age': 20, 'email': 'alireza@kadoosedu.ir'}

    print(student)
    print(student['age'])       # reading by key
    print(student['email'])
    print(student['name'])

    print(len(student))         # number of pairs -> 3
    print('age' in student)     # 'in' looks at the KEYS -> True

if __name__ == '__main__':
    main()
