# In a DEFINITION, * and ** collect the arguments.
def print_all(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


def main() -> None:
    print_all(1, 2, 3, name='Ali', age=20)

    # In a CALL, * and ** do the opposite: they spread a container.
    data = [1, 2, 3]
    info = {'name': 'Ali', 'age': 20}
    print_all(*data, **info)          # exactly the same call as above

    # A very frequent use: passing the items of a list to print().
    words = ['Kadoos', 'Institute', 'Rasht']
    print(*words)                     # Kadoos Institute Rasht
    print(*words, sep=' - ')

    # And to hand a configuration dictionary to a function.
    def connect(host: str, port: int, timeout: float = 5.0):
        print(f'connecting to {host}:{port} (timeout {timeout})')

    settings = {'host': 'localhost', 'port': 5432}
    connect(**settings)


if __name__ == '__main__':
    main()
