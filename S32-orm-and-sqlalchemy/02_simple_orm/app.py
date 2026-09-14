'''A menu-driven program using our own tiny ORM.

Not one line of SQL in this file: everything goes through the models.
'''

import os

from models import Student, Teacher


def clear() -> None:
    'Clear the terminal on Windows as well as on Linux/macOS.'
    os.system('cls' if os.name == 'nt' else 'clear')


def pause() -> None:
    input('\nPress Enter to continue...')


def main_menu() -> None:
    print('1) Students')
    print('2) Teachers')
    print('0) Exit')


def student_menu() -> None:
    print('1) Show all')
    print('2) Find a student')
    print('3) Add a student')
    print('4) Rename a student')
    print('5) Delete a student')
    print('9) Back to the main menu')


def students_section() -> None:
    'Everything about the students.'
    while True:
        clear()
        student_menu()
        choice = input('Enter the number: ').strip()

        if choice == '1':
            clear()
            students = Student.all()
            if not students:
                print('(no student yet)')
            for student in students:
                print(f'{student.student_id:<5}{student}')
            pause()

        elif choice == '2':
            clear()
            email = input('Enter the email: ').strip()
            student = Student.get(email=email)
            if student is None:
                print('No student with that email.')
            else:
                print(f'Name:  {student.full_name}')
                print(f'Email: {student.email}')
            pause()

        elif choice == '3':
            clear()
            email = input('Enter the email: ').strip()
            if Student.get(email=email) is not None:
                print('That email is already used.')
                pause()
                continue

            first_name = input('Enter the first name: ').strip()
            last_name = input('Enter the last name: ').strip()

            student = Student(email=email,
                              first_name=first_name or 'New',
                              last_name=last_name or 'Student')
            student.save()
            print(f'Student added with the id {student.student_id}.')
            pause()

        elif choice == '4':
            clear()
            student = Student.get(email=input('Enter the email: ').strip())
            if student is None:
                print('No student with that email.')
            else:
                student.update(first_name=input('New first name: ').strip())
                print('Updated:', student)
            pause()

        elif choice == '5':
            clear()
            student = Student.get(email=input('Enter the email: ').strip())
            if student is None:
                print('No student with that email.')
            else:
                student.delete()
                print('Deleted.')
            pause()

        elif choice == '9':
            return

        else:
            print('Unknown option.')
            pause()


def teachers_section() -> None:
    'A very small section, to show how little a second model costs.'
    clear()
    teachers = Teacher.all()
    if not teachers:
        print('(no teacher yet - two are being created)')
        Teacher('Mohammad', 'Mohammadi', 'Computer').save()
        Teacher('Norouz', 'Norouzi', 'Language').save()
        teachers = Teacher.all()

    for teacher in teachers:
        print(f'{teacher.teacher_id:<5}{teacher}')
    pause()


def main() -> None:
    # Create the tables once, at start-up.
    Student.create_table()
    Teacher.create_table()

    while True:
        clear()
        main_menu()
        choice = input('Enter the number: ').strip()

        if choice == '1':
            students_section()
        elif choice == '2':
            teachers_section()
        elif choice == '0':
            print('Goodbye!')
            break
        else:
            print('Unknown option.')
            pause()


if __name__ == '__main__':
    main()
