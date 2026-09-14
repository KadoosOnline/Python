'''A small menu-driven program built around a class.'''


class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.scores: list[float] = []

    def add_score(self, score: float) -> None:
        'Store one score.'
        self.scores.append(score)

    def average(self) -> float:
        'Return the average score (0 when there is none).'
        if len(self.scores) == 0:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def describe(self) -> str:
        'Return a one-line description.'
        return f'{self.name} ({self.age}) - average {self.average():.2f}'


def find(students: list[Student], name: str) -> Student | None:
    'Return the student with that name, or None.'
    for student in students:
        if student.name.lower() == name.lower():
            return student
    return None


def main() -> None:
    students: list[Student] = []

    while True:
        print('\n1) Add a student')
        print('2) Add a score')
        print('3) Show all the students')
        print('0) Exit')

        choice = input('Your choice: ')

        if choice == '1':
            name = input('Name: ')
            try:
                age = int(input('Age: '))
            except ValueError:
                print('The age must be a whole number.')
                continue
            students.append(Student(name, age))
            print('Added.')

        elif choice == '2':
            student = find(students, input('Name: '))
            if student is None:
                print('No such student.')
                continue
            try:
                student.add_score(float(input('Score: ')))
            except ValueError:
                print('The score must be a number.')

        elif choice == '3':
            if len(students) == 0:
                print('(no student yet)')
            for student in students:
                print(' -', student.describe())

        elif choice == '0':
            break

        else:
            print('Unknown option.')


if __name__ == '__main__':
    main()
