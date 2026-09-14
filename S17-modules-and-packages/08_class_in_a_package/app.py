# A package usually exports classes, not only functions.
from animals import Animal

if __name__ == '__main__':
    the_cat = Animal('Tom', 7, is_pet=True)
    print(the_cat)

    the_wolf = Animal('Fang', 20)
    print(the_wolf)
