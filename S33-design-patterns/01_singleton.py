'''SINGLETON - creational pattern.

Problem:  some objects must exist only once in the whole program:
          a logger, a configuration, a connection pool.
Solution: the class itself makes sure that every call returns the SAME object.
'''


class SingletonLogger:
    # A class attribute holds the single instance.
    _instance = None

    def __new__(cls):
        '''__new__ runs BEFORE __init__ and is what really creates the object.

        By overriding it we can return an object that already exists instead of
        building a new one.
        '''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []      # initialised only the first time
        return cls._instance

    def log(self, message: str) -> None:
        self.logs.append(message)
        print(f'LOG: {message}')


if __name__ == '__main__':
    logger1 = SingletonLogger()
    logger2 = SingletonLogger()

    logger1.log('First message')
    logger2.log('Second message')

    print(logger1 is logger2)    # True - it is the very same object
    print(logger1.logs)          # ['First message', 'Second message']

    # In Python there is a simpler way: a MODULE is already a singleton.
    # Putting `logger = Logger()` at the top of a module and importing it
    # gives the same guarantee, with no magic at all.
