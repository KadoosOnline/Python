# A dictionary whose values are lists is used to GROUP things.
def main() -> None:
    classes = {
        'python': ['Ali', 'Sara'],
        'linux': ['Reza'],
    }

    # Adding a student to an existing group.
    classes['python'].append('Maryam')

    # Adding a brand new group.
    classes['csharp'] = ['Omid']

    for course, students in classes.items():
        print(f'{course} ({len(students)}): {", ".join(students)}')

    # A dictionary of dictionaries: scores per student per subject.
    scores = {
        'Ali': {'math': 20, 'physics': 18},
        'Sara': {'math': 19, 'physics': 20},
    }
    print(scores['Sara']['physics'])     # 20

    for name, subjects in scores.items():
        average = sum(subjects.values()) / len(subjects)
        print(f'{name}: average {average}')

if __name__ == '__main__':
    main()
