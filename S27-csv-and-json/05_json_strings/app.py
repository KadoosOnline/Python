'''json.dumps / json.loads: JSON as a STRING instead of a file.

This is what you use with a web API (session 28).
'''

import json
from datetime import date


def main() -> None:
    student = {
        'name': 'Ali',
        'age': 20,
        'scores': [18, 20, 15],
        'active': True,
        'address': None,
        'city': 'رشت',
    }

    # dumps() -> a Python object becomes a JSON string
    text = json.dumps(student)
    print(text)
    print(type(text))

    # The options make it readable.
    print(json.dumps(student, indent=2, ensure_ascii=False, sort_keys=True))

    # loads() -> a JSON string becomes a Python object
    back = json.loads(text)
    print(back['name'], back['scores'][0])
    print(type(back))

    # The correspondence between the two worlds:
    #   JSON      Python
    #   object    dict
    #   array     list
    #   string    str
    #   number    int / float
    #   true      True
    #   false     False
    #   null      None
    print(json.loads('{"a": true, "b": null, "c": [1, 2.5]}'))

    # A broken text raises JSONDecodeError (a subclass of ValueError).
    try:
        json.loads('{not json}')
    except json.JSONDecodeError as e:
        print('Invalid JSON:', e)

    # JSON cannot store a date, a set or an object.
    data = {'day': date.today(), 'tags': {'a', 'b'}}
    try:
        json.dumps(data)
    except TypeError as e:
        print('Cannot serialise:', e)

    # Solution 1: convert by hand.
    print(json.dumps({'day': str(date.today()), 'tags': list({'a', 'b'})}))

    # Solution 2: give dumps() a 'default' function for the unknown types.
    def convert(value):
        if isinstance(value, date):
            return value.isoformat()
        if isinstance(value, set):
            return sorted(value)
        raise TypeError(f'{type(value)} is not serialisable')

    print(json.dumps(data, default=convert))


if __name__ == '__main__':
    main()
