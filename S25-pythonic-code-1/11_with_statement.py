# Before 'with', closing a file safely needed a try/finally.
def the_old_way() -> str:
    f1 = open('data.txt', 'r', encoding='utf-8')
    try:
        return f1.read()
    finally:
        f1.close()          # runs even when read() raises


# 'with' does exactly the same thing, in one line.
def the_pythonic_way() -> str:
    with open('data.txt', 'r', encoding='utf-8') as f2:
        return f2.read()
    # the file is already closed here


def main() -> None:
    # Create the file so that the example can run.
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write('Kadoos\n')

    print(the_old_way(), end='')
    print(the_pythonic_way(), end='')

    # Several context managers in one 'with'.
    with open('data.txt', encoding='utf-8') as source, \
         open('copy.txt', 'w', encoding='utf-8') as target:
        target.write(source.read())

    print('copied')

    # 'with' is not only for files: locks, database connections, timers...
    # Any object with __enter__ and __exit__ works (session 24).


if __name__ == '__main__':
    main()
