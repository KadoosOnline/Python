'''SQLAlchemy ORM, step by step.

    pip install -r requirements.txt

Every example is a function. main() runs them in order; comment out the ones
you have already seen, or delete database.db to start again from zero.
'''

from sqlalchemy import create_engine, event
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from models import Base, Course, Enrollment, Student, Teacher

DATABASE_URL = 'sqlite:///database.db'

# The engine is the connection pool: ONE per application.
# echo=True prints every SQL statement - switch it on to see what the ORM does.
engine = create_engine(DATABASE_URL, echo=False, future=True)


@event.listens_for(engine, 'connect')
def set_sqlite_pragma(dbapi_connection, connection_record) -> None:
    '''Turn the foreign keys on for every new connection.

    Exactly the "PRAGMA foreign_keys = ON" of session 31, but done once here
    instead of in every function.
    '''
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()


# A factory that produces sessions. A Session is one "conversation" with the
# database: it collects the changes and writes them at commit().
SessionLocal = sessionmaker(bind=engine, future=True)


def example_1_create_tables() -> None:
    'Example 1: create every table described by the models.'
    print('\n=== Example 1: creating the tables ===')
    Base.metadata.create_all(engine)
    print('Tables created successfully.')


def example_2_insert_data() -> None:
    'Example 2: insert teachers, courses and students.'
    print('\n=== Example 2: inserting data ===')
    with SessionLocal() as session:
        t1 = Teacher(name='Dr. Smith', email='smith@edu.com')
        t2 = Teacher(name='Prof. Johnson', email='johnson@edu.com')
        session.add_all([t1, t2])

        # flush() sends the INSERTs so that the ids exist, but does NOT commit.
        session.flush()

        session.add_all([
            Course(title='Mathematics 101', teacher_id=t1.id),
            Course(title='Physics 101', teacher_id=t1.id),
            Course(title='History 101', teacher_id=t2.id),
        ])

        session.add_all([
            Student(name='Alice', email='alice@student.edu'),
            Student(name='Bob', email='bob@student.edu'),
            Student(name='Charlie', email='charlie@student.edu'),
        ])

        session.commit()
        print('Data inserted and committed.')


def example_3_read_data() -> None:
    'Example 3: read every teacher and every student.'
    print('\n=== Example 3: reading data ===')
    with SessionLocal() as session:
        print('Teachers:')
        for teacher in session.query(Teacher).all():
            print(f'  {teacher.name} ({teacher.email})')

        print('Students:')
        for student in session.query(Student).all():
            print(f'  {student.name} ({student.email})')


def example_4_update_record() -> None:
    'Example 4: change the email of a student.'
    print('\n=== Example 4: updating a record ===')
    with SessionLocal() as session:
        student = session.query(Student).filter_by(name='Alice').first()

        if student is None:
            print('Alice not found.')
            return

        old_email = student.email
        # Simply assigning to the attribute is enough: the session notices it.
        student.email = 'alice.new@student.edu'
        session.commit()
        print(f'Alice email updated from {old_email} to {student.email}')


def example_5_delete_course() -> None:
    'Example 5: delete a course.'
    print('\n=== Example 5: deleting a course ===')
    with SessionLocal() as session:
        course = session.query(Course).filter_by(title='History 101').first()

        if course is None:
            print('Course not found.')
            return

        title = course.title
        session.delete(course)
        session.commit()
        print(f"Course '{title}' deleted.")


def example_6_enroll_students() -> None:
    'Example 6: create enrolments (many-to-many with an extra grade).'
    print('\n=== Example 6: enrolling students ===')
    with SessionLocal() as session:
        alice = session.query(Student).filter_by(name='Alice').first()
        bob = session.query(Student).filter_by(name='Bob').first()
        math = session.query(Course).filter_by(title='Mathematics 101').first()
        physics = session.query(Course).filter_by(title='Physics 101').first()

        if not all([alice, bob, math, physics]):
            print('Required records missing. Run example 2 first.')
            return

        # The objects are given directly: SQLAlchemy fills the ids in for us.
        session.add_all([
            Enrollment(student=alice, course=math, grade=85.5),
            Enrollment(student=bob, course=math, grade=79.0),
            Enrollment(student=alice, course=physics, grade=92.0),
        ])
        session.commit()
        print('Enrollments created: Alice->Math, Bob->Math, Alice->Physics')


def example_7_query_enrollments() -> None:
    'Example 7: read the enrolments through the relations.'
    print('\n=== Example 7: querying enrollments ===')
    with SessionLocal() as session:
        for e in session.query(Enrollment).all():
            # e.student and e.course are real objects: no JOIN to write.
            print(f'{e.student.name} enrolled in {e.course.title} '
                  f'- Grade: {e.grade}')

        # Navigating the other way round is just as easy.
        alice = session.query(Student).filter_by(name='Alice').first()
        if alice:
            print(f'Alice follows {len(alice.enrollments)} course(s):',
                  [e.course.title for e in alice.enrollments])


def example_8_cascade_delete_student() -> None:
    'Example 8: deleting a student also deletes their enrolments.'
    print('\n=== Example 8: cascade delete - student ===')
    with SessionLocal() as session:
        bob = session.query(Student).filter_by(name='Bob').first()

        if bob is None:
            print('Bob not found.')
            return

        bob_id = bob.id
        before = session.query(Enrollment).filter_by(student_id=bob_id).count()
        print(f'Bob has {before} enrollment(s).')

        session.delete(bob)
        session.commit()

        after = session.query(Enrollment).filter_by(student_id=bob_id).count()
        print(f"After deletion, Bob's enrollments: {after}")


def example_9_cascade_delete_course() -> None:
    'Example 9: deleting a course also deletes its enrolments.'
    print('\n=== Example 9: cascade delete - course ===')
    with SessionLocal() as session:
        physics = session.query(Course).filter_by(title='Physics 101').first()

        if physics is None:
            print('Physics 101 not found.')
            return

        course_id = physics.id
        before = session.query(Enrollment).filter_by(course_id=course_id).count()
        print(f'Physics has {before} enrollment(s).')

        session.delete(physics)
        session.commit()

        after = session.query(Enrollment).filter_by(course_id=course_id).count()
        print(f'After deletion, Physics enrollments: {after}')


def example_10_transaction_rollback() -> None:
    'Example 10: a failed transaction is rolled back.'
    print('\n=== Example 10: transaction rollback ===')
    with SessionLocal() as session:
        try:
            # The email already belongs to Alice, and the column is UNIQUE.
            session.add(Student(name='Duplicate',
                                email='alice.new@student.edu'))
            session.commit()
        except IntegrityError:
            session.rollback()
            print('IntegrityError caught! Transaction rolled back.')

            duplicate = session.query(Student).filter_by(name='Duplicate').first()
            print(f"Duplicate student in DB? {'Yes' if duplicate else 'No'}")
        except Exception as e:
            session.rollback()
            print(f'Other error: {e}')


def main() -> None:
    'Run every example in order.'
    example_1_create_tables()
    example_2_insert_data()
    example_3_read_data()
    example_4_update_record()
    example_5_delete_course()
    example_6_enroll_students()
    example_7_query_enrollments()
    example_8_cascade_delete_student()
    example_9_cascade_delete_course()
    example_10_transaction_rollback()

    print("\nAll examples completed. Open 'database.db' with DB Browser "
          "for SQLite to see the result.")


if __name__ == '__main__':
    main()
