# Reaching deep into a structure is easy, but every level can be missing.
def main() -> None:
    data = {
        'school': 'Kadoos',
        'classes': [
            {'title': 'Python', 'students': ['Ali', 'Sara']},
            {'title': 'Linux', 'students': []},
        ],
    }

    print(data['classes'][0]['students'][1])     # 'Sara'

    # A missing key raises KeyError, a missing index raises IndexError.
    # get() with a default protects us level by level.
    teacher = data.get('teacher', 'unknown')
    print(teacher)

    for course in data['classes']:
        students = course.get('students', [])
        if len(students) == 0:
            print(f"{course['title']}: no student yet")
        else:
            print(f"{course['title']}: {len(students)} student(s)")

if __name__ == '__main__':
    main()
