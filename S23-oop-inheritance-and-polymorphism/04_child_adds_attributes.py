# The usual pattern: the child calls super().__init__() and then adds its own
# attributes.
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def describe(self) -> str:
        return f'{self.name}, {self.age} years old'


class Employee(Person):
    def __init__(self, name: str, age: int, salary: float) -> None:
        super().__init__(name, age)     # name and age handled by Person
        self.salary = salary            # only Employee has this

    def describe(self) -> str:
        # Reusing the parent version instead of repeating it.
        return f'{super().describe()}, salary {self.salary:,.0f}'


class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float, team: list[str]) -> None:
        super().__init__(name, age, salary)
        self.team = team

    def describe(self) -> str:
        return f'{super().describe()}, manages {len(self.team)} people'


if __name__ == '__main__':
    print(Person('Ali', 30).describe())
    print(Employee('Sara', 28, 30_000_000).describe())
    print(Manager('Reza', 45, 60_000_000, ['Ali', 'Sara']).describe())
