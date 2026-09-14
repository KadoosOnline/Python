'''Module docstring: what this program or module is for.

It is the very first string of the file. `help(module)` shows it, and so does
the editor when you hover over the module name.
'''


class Test:
    'Docstring of a class: what this class represents.'

    def method(self) -> None:
        'Docstring of a method: what it does.'


def main() -> None:
    'The entry point of the program.'
    t = Test()
    print(t)

    # A triple-quoted string can span several lines. Used as a VALUE it is a
    # normal string; used as the first statement of a module, a class or a
    # function it becomes the docstring.
    text = '''Hello,
    This is a test!
    Goodbye!
    '''
    print(text)


if __name__ == '__main__':
    main()

'''
A triple-quoted string that nobody assigns and that is not in the first
position is simply ignored: people often use it as a multi-line comment.

Notice that it changes nothing in the behaviour of the program.
'''
