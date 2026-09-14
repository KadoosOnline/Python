# Three levels of inheritance. Every 'do' calls the one above it with super().
class A:
    def do(self):
        print('A')


class B(A):
    def do(self):
        print('B')
        super().do()


class C(B):
    def do(self):
        print('C')
        super().do()


if __name__ == '__main__':
    c = C()
    c.do()          # prints C, then B, then A

    # The MRO (Method Resolution Order) is the exact list of classes Python
    # searches, in order.
    print(C.__mro__)
