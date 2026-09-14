'''A small report built on a list of dictionaries.'''

STUDENTS = [
    {'name': 'Ali', 'city': 'Rasht', 'scores': [20, 18, 15]},
    {'name': 'Sara', 'city': 'Rasht', 'scores': [19, 20, 20]},
    {'name': 'Reza', 'city': 'Lahijan', 'scores': [12, 14, 9]},
    {'name': 'Maryam', 'city': 'Anzali', 'scores': [17, 16, 18]},
]


def average(numbers: list[float]) -> float:
    'Return the average of a list of numbers (0 for an empty list).'
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def print_table() -> None:
    'Print one line per student with their average.'
    print(f"{'Name':<10}{'City':<10}{'Average':>8}")
    print('-' * 28)
    for student in STUDENTS:
        avg = average(student['scores'])
        print(f"{student['name']:<10}{student['city']:<10}{avg:>8.2f}")


def best_student() -> dict:
    'Return the student with the best average.'
    best = STUDENTS[0]
    for student in STUDENTS:
        if average(student['scores']) > average(best['scores']):
            best = student
    return best


def group_by_city() -> dict[str, list[str]]:
    'Return {city: [names]}.'
    groups: dict[str, list[str]] = {}
    for student in STUDENTS:
        city = student['city']
        if city not in groups:
            groups[city] = []
        groups[city].append(student['name'])
    return groups


def main() -> None:
    print_table()
    print()
    print('Best student:', best_student()['name'])
    print('By city:', group_by_city())
    print('Cities:', sorted({student['city'] for student in STUDENTS}))


if __name__ == '__main__':
    main()
