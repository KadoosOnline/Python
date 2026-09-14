'''A small complete tool: read a CSV file, analyse it, save the result as JSON.

It puts together: csv, json, dictionaries, comprehensions and exceptions.
'''

import csv
import json
import os

CSV_FILE = 'students.csv'
JSON_FILE = 'report.json'

NUMERIC_FIELDS = ['StudentID', 'Age', 'Grade',
                  'Math_Score', 'Science_Score', 'English_Score']


def read_students(path: str) -> list[dict]:
    '''Read the CSV file and convert the numeric columns.'''
    if not os.path.exists(path):
        raise FileNotFoundError(f'{path} was not found')

    students: list[dict] = []

    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            for field in NUMERIC_FIELDS:
                try:
                    row[field] = int(row[field])
                except (KeyError, ValueError):
                    raise ValueError(f'the column {field} is missing or invalid')
            students.append(row)

    return students


def add_computed_fields(students: list[dict]) -> None:
    '''Add the total and the average to every student.'''
    for student in students:
        scores = [student['Math_Score'],
                  student['Science_Score'],
                  student['English_Score']]
        student['Total'] = sum(scores)
        student['Average'] = round(sum(scores) / len(scores), 2)
        student['Passed'] = student['Average'] >= 70


def build_report(students: list[dict]) -> dict:
    '''Build the summary that will be saved as JSON.'''
    by_grade: dict[str, list[str]] = {}
    for student in students:
        by_grade.setdefault(str(student['Grade']), []).append(student['Name'])

    return {
        'source': CSV_FILE,
        'count': len(students),
        'class_average': round(
            sum(s['Average'] for s in students) / len(students), 2),
        'best': max(students, key=lambda s: s['Total'])['Name'],
        'worst': min(students, key=lambda s: s['Total'])['Name'],
        'passed': [s['Name'] for s in students if s['Passed']],
        'failed': [s['Name'] for s in students if not s['Passed']],
        'by_grade': by_grade,
        'students': students,
    }


def main() -> None:
    try:
        students = read_students(CSV_FILE)
    except (FileNotFoundError, ValueError) as e:
        print('Error:', e)
        return

    if not students:
        print('The file contains no student.')
        return

    add_computed_fields(students)
    report = build_report(students)

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f'{report["count"]} students read from {CSV_FILE}')
    print(f'Class average: {report["class_average"]}')
    print(f'Best: {report["best"]}   Worst: {report["worst"]}')
    print(f'Report written to {JSON_FILE}')


if __name__ == '__main__':
    main()
