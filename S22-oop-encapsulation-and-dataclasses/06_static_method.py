# A @staticmethod is a plain function that we choose to store inside a class,
# because it belongs to the same subject. It receives neither self nor cls.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


# It is called on the CLASS, no object is needed.
print(MathUtils.add(2, 3))
print(MathUtils.is_even(10))

# It also works through an object, but that is unusual.
utils = MathUtils()
print(utils.add(4, 5))


class Validator:
    'A realistic use: a group of related checks.'

    @staticmethod
    def is_valid_email(text: str) -> bool:
        return '@' in text and '.' in text.split('@')[-1]

    @staticmethod
    def is_valid_phone(text: str) -> bool:
        return text.isdigit() and len(text) == 11


print(Validator.is_valid_email('ali@kadoosedu.ir'))
print(Validator.is_valid_phone('09121234567'))
