# From now on we put the "story" of the program inside a function called main().
# It keeps every variable local and makes the program easy to read.
def show(text):
    print(text)

def main():
    show('Kadoos')
    show('Rasht')

if __name__ == '__main__':
    main()
