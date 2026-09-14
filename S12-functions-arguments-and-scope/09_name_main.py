# Python gives every file a variable called __name__.
#  * when the file is RUN directly       -> __name__ == '__main__'
#  * when the file is IMPORTED elsewhere -> __name__ is the module name
#
# So the guard below means: "run this only when I am the program being started".
# It is what allows a file to be both a program and a reusable module
# (see session 17).
print('The value of __name__ here is:', __name__)

def main():
    print('main() was called')

if __name__ == '__main__':
    main()
