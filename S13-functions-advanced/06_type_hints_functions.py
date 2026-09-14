# Parameters are annotated with ': type', the result with '-> type'.
def add(number1: float, number2: float) -> float:
    return number1 + number2

def greet(name: str) -> str:
    return f'Hello {name}'

# A function that returns nothing is annotated with '-> None'.
def main() -> None:
    print(add(3.2, 2.0))
    print(greet('Kadoos'))

if __name__ == '__main__':
    main()
