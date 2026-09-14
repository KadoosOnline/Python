# A class may have several parents. super() then follows the MRO,
# not simply "the first parent".
class Logger:
    def __init__(self):
        print('Logger init')
        super().__init__()          # keep the chain going!

    def log(self, message='...'):
        print('Logging:', message)


class Database:
    def __init__(self):
        print('Database init')
        super().__init__()


class App(Logger, Database):
    def __init__(self):
        print('App init')
        super().__init__()          # starts the chain: Logger, then Database


if __name__ == '__main__':
    app = App()
    app.log('the application started')

    # The order of the parents decides the MRO.
    print(App.__mro__)

    # Multiple inheritance is powerful but easy to get wrong.
    # In practice, prefer composition (session 22) or a "mixin" that only
    # adds behaviour and no state, like Logger here.
