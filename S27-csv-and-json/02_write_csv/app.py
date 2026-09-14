'''Writing CSV files.

Reminder: mode 'w' ERASES the file, mode 'a' adds to its end.
'''

import csv

FIELDNAMES = [
    'StudentID', 'Name', 'Age', 'Grade',
    'Math_Score', 'Science_Score', 'English_Score',
]


def write_list_data() -> None:
    '''csv.writer writes rows given as LISTS.'''
    rows = [
        [11, 'Liam', 14, 9, 77, 81, 79],
        [12, 'Mia', 15, 10, 88, 92, 90],
        [13, 'Noah', 13, 8, 64, 68, 70],
    ]

    filename = 'students_from_lists.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(FIELDNAMES)    # one row
        writer.writerows(rows)         # many rows at once

    print(f'List-based CSV file created: {filename}')


def write_dict_data() -> None:
    '''csv.DictWriter writes rows given as DICTIONARIES.'''
    students = [
        {'StudentID': 14, 'Name': 'Olivia', 'Age': 14, 'Grade': 9,
         'Math_Score': 95, 'Science_Score': 97, 'English_Score': 93},
        {'StudentID': 15, 'Name': 'Peter', 'Age': 15, 'Grade': 10,
         'Math_Score': 72, 'Science_Score': 76, 'English_Score': 74},
        {'StudentID': 16, 'Name': 'Quinn', 'Age': 13, 'Grade': 8,
         'Math_Score': 81, 'Science_Score': 85, 'English_Score': 88},
    ]

    filename = 'students_from_dicts.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()           # the header comes from fieldnames
        writer.writerows(students)

    print(f'Dict-based CSV file created: {filename}')


def append_to_file() -> None:
    '''Mode "a" adds a row without touching what is already there.'''
    filename = 'students_from_lists.csv'
    new_student = [17, 'Ruby', 14, 9, 89, 91, 86]

    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_student)

    print(f'Appended one student to {filename}')


def write_with_semicolon() -> None:
    '''Some spreadsheets expect ';' instead of ','.'''
    filename = 'students_semicolon.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Name', 'City'])
        writer.writerow(['Ali', 'Rasht'])
        writer.writerow(['Sara, the second', 'Lahijan'])   # the comma is quoted

    with open(filename, encoding='utf-8') as f:
        print(f.read())


def main() -> None:
    print('Creating CSV files using the csv module.\n')
    write_list_data()
    append_to_file()
    write_dict_data()
    write_with_semicolon()


if __name__ == '__main__':
    main()
