# Keys and values can come from variables.
def main() -> None:
    key1 = 'name'
    key2 = 'age'
    key3 = 'city'

    value1 = 'Ali'
    value2 = 25
    value3 = 'Rasht'

    person = {
        key1: value1,
        key2: value2,
        key3: value3,
    }

    print(person)

    # dict() with keyword arguments is another way of building one.
    other = dict(name='Sara', age=19, city='Rasht')
    print(other)

if __name__ == '__main__':
    main()
