# An attribute written in the body of the class belongs to the CLASS:
# it is shared by every object that does not define its own.
class Counter:
    total = 0            # class attribute - ONE copy for everybody


def main():
    a = Counter()
    b = Counter()

    print(a.total, b.total)        # 0 0

    # Assigning through an object creates an INSTANCE attribute that hides
    # the class one - only for that object.
    a.total = 10
    print(a.total, b.total)        # 10 0

    # Changing it on the class itself changes it for everyone who has no
    # instance attribute of that name.
    Counter.total = 99
    print(a.total, b.total)        # 10 99

    # This is why mutable class attributes are dangerous:
    class Basket:
        items = []                 # shared by ALL the baskets!

    b1 = Basket()
    b2 = Basket()
    b1.items.append('apple')
    print(b2.items)                # ['apple'] - surprise!

    # The fix is to create the list inside __init__ (see 04_init.py).


if __name__ == '__main__':
    main()
