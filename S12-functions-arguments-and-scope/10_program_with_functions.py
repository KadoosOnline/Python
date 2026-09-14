# A complete program cut into small functions:
# one function reads, one computes, one displays, and main() puts them together.

def read_number(message):
    'Ask the user for a number until the answer is really a number.'
    while True:
        user_input = input(message)
        try:
            return float(user_input)
        except ValueError:
            print('That is not a number, try again.')

def add(number1, number2):
    return number1 + number2

def show_result(value):
    print('Sum:', value)

def main():
    num1 = read_number('Enter a number: ')
    num2 = read_number('Enter a number: ')
    show_result(add(num1, num2))

if __name__ == '__main__':
    main()
