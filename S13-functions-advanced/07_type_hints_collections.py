# Hints for collections say what is INSIDE them.
def get_total(numbers: list[int]) -> int:
    return sum(numbers)

def show_student(data: dict[str, int]) -> None:
    print(data)

# '|' means "one type OR the other".
def add(number1: int | float = 1, number2: int | float = 1) -> int | float:
    return number1 + number2

# 'X | None' is used for a value that may be missing.
def find_name(names: list[str], target: str) -> str | None:
    for name in names:
        if name == target:
            return name
    return None

# A long signature is easier to read spread over several lines.
def register(
    number1: float = 1.0,
    number2: float = 1.0,
    name: str = 'Kadoos',
    active: bool = True,
) -> float:
    return number1 + number2

def main() -> None:
    print(get_total([2, 4, 5, 17]))
    show_student({'riyazi': 20, 'varzesh': 20, 'zaban': 19})
    print(add(number1=3.2, number2=2.0))
    print(find_name(['Ali', 'Sara'], 'Reza'))
    print(register(number1=3.2, number2=2.0))

if __name__ == '__main__':
    main()
