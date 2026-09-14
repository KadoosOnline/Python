# Try it: run 'python animals/animal.py' -> the test code of the module runs.
# Then run 'python app.py' -> only the two animals below are printed,
# because the guard stops the test code of the module.
from animals import Animal

if __name__ == '__main__':
    the_cat = Animal('Tom', 7)
    print(the_cat)

    the_wolf = Animal('Fang', 20)
    print(the_wolf)
