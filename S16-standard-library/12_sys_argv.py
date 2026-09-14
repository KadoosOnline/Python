'''Reading the arguments typed on the command line.

Run it like this:
    python 12_sys_argv.py 12 30
'''

import sys


def main() -> None:
    # sys.argv[0] is the name of the file itself.
    print('All the arguments:', sys.argv)

    if len(sys.argv) < 3:
        print('Usage: python 12_sys_argv.py <number1> <number2>')
        sys.exit(1)          # stop the program with an error code

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    print('Sum:', num1 + num2)


if __name__ == '__main__':
    main()
