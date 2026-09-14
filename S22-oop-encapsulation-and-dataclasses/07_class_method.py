# A @classmethod receives the CLASS itself as its first parameter ('cls').
# Its main use is to offer other ways of building an object.
class Student:
    school = 'Kadoos'            # class attribute
    count = 0                    # how many students were created

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Student.count += 1       # shared counter

    @classmethod
    def from_string(cls, text: str) -> 'Student':
        'Build a Student out of "name,age".'
        name, age = text.split(',')
        return cls(name.strip(), int(age))

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        'Build a Student out of a dictionary.'
        return cls(data['name'], data['age'])

    @classmethod
    def change_school(cls, new_name: str) -> None:
        'Change the class attribute for every student at once.'
        cls.school = new_name

    def describe(self) -> str:
        return f'{self.name}, {self.age}, {self.school}'


s1 = Student('Ali', 20)
s2 = Student.from_string('Sara, 19')
s3 = Student.from_dict({'name': 'Reza', 'age': 22})

print(s1.describe())
print(s2.describe())
print(s3.describe())
print('Students created:', Student.count)

Student.change_school('Kadoos Rasht')
print(s1.describe())
