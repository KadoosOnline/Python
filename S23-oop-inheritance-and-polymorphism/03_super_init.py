# super() gives access to the parent class.
# It is used above all to run the parent __init__.
class Human:
    def __init__(self, name: str = 'Adam'):
        self.name = name

    def greet(self):
        print(f'Hello {self.name}!')


class Student(Human):
    def __init__(self, name: str = 'Adam'):
        super().__init__(name)      # let Human set self.name
        # extra work of the child would go here

    def learn(self):
        print('I try to learn!')


if __name__ == '__main__':
    h = Human(name='Alireza')
    h.greet()

    s = Student(name='Hassan')
    s.greet()          # inherited
    s.learn()          # its own
