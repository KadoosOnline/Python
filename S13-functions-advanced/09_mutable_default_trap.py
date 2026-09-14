# A default value is created ONCE, when the function is defined.
# With a list as a default, all the calls end up sharing the SAME list.
def add_student_wrong(name, students=[]):
    students.append(name)
    return students

print(add_student_wrong('Ali'))     # ['Ali']
print(add_student_wrong('Sara'))    # ['Ali', 'Sara']  <- surprise!

# The correct pattern uses None as the default.
def add_student(name: str, students: list[str] | None = None) -> list[str]:
    if students is None:
        students = []
    students.append(name)
    return students

print(add_student('Ali'))           # ['Ali']
print(add_student('Sara'))          # ['Sara']

existing = ['Taghi', 'Naghi']
print(add_student('Rahman', existing))
