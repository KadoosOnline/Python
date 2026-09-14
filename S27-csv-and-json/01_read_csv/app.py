'''Reading a CSV file with Python's built-in csv module.

Every example reads 'students.csv', which sits in the same folder.

IMPORTANT: always open a CSV file with newline='' - otherwise the csv module
and the operating system both add a line ending and you get blank lines.
'''

import csv


def read_as_lists() -> None:
    '''csv.reader gives every row as a LIST of strings.'''
    print('=== Basic reading with csv.reader (lists) ===')
    with open('students.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        header = next(reader)          # the first line is the header
        print('Header:', header)

        rows = []
        for row in reader:             # the reader continues after the header
            rows.append(row)

        print(f'Total students: {len(rows)}')
        print('First 3 rows:')
        for row in rows[:3]:
            print(row)
    print()


def read_as_dicts() -> None:
    '''csv.DictReader gives every row as a DICTIONARY: much more readable.'''
    print('=== Reading with csv.DictReader (dictionaries) ===')
    with open('students.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)     # the header becomes the keys

        students = []
        for row in reader:
            # Everything read from a CSV file is TEXT: convert what is numeric.
            row['StudentID'] = int(row['StudentID'])
            row['Age'] = int(row['Age'])
            row['Grade'] = int(row['Grade'])
            row['Math_Score'] = int(row['Math_Score'])
            row['Science_Score'] = int(row['Science_Score'])
            row['English_Score'] = int(row['English_Score'])
            students.append(row)

        print('First 3 students:')
        for s in students[:3]:
            # Use DOUBLE quotes outside when the keys use single quotes.
            print(f"  {s['Name']} (Grade {s['Grade']}): "
                  f"Math={s['Math_Score']}, Science={s['Science_Score']}, "
                  f"English={s['English_Score']}")
    print()


def show_averages() -> None:
    '''Compute the average of every subject.'''
    print('=== Class averages ===')
    total_math = 0
    total_science = 0
    total_english = 0
    count = 0

    with open('students.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_math += int(row['Math_Score'])
            total_science += int(row['Science_Score'])
            total_english += int(row['English_Score'])
            count += 1

    if count == 0:
        print('  (the file is empty)')
        return

    print(f'  Math:    {total_math / count:.1f}')
    print(f'  Science: {total_science / count:.1f}')
    print(f'  English: {total_english / count:.1f}')
    print()


def filter_by_grade(grade: int) -> None:
    '''Show the names of the students of one grade.'''
    print(f'=== Students in Grade {grade} ===')
    found = False

    with open('students.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['Grade']) == grade:
                print(f"  {row['Name']}")
                found = True

    if not found:
        print('  (none)')
    print()


def best_student() -> None:
    '''Find the student with the best total, keeping the file open only once.'''
    print('=== Best student ===')
    with open('students.csv', newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    def total(row: dict) -> int:
        return (int(row['Math_Score'])
                + int(row['Science_Score'])
                + int(row['English_Score']))

    best = max(rows, key=total)
    print(f"  {best['Name']} with {total(best)} points")
    print()


def main() -> None:
    print('Exploring student data with the csv module (reading only).\n')
    read_as_lists()
    read_as_dicts()
    show_averages()
    filter_by_grade(9)
    best_student()


if __name__ == '__main__':
    main()
