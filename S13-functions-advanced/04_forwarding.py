# A very common use of *args / **kwargs: accept anything and hand it over
# unchanged to another function. Here we build our own print().
def show(*args, **kwargs):
    print(*args, **kwargs)

def main():
    show('Hello World!', end=' *** ')
    show('Hello Kadoos!', end=' *** ')
    show()
    show('a', 'b', 'c', sep='-')

if __name__ == '__main__':
    main()
