# Counting is the killer application of dictionaries:
# the key is the thing we count, the value is how many times we saw it.
def main() -> None:
    sentence = input('Enter a sentence: ')

    counts: dict[str, int] = {}

    for char in sentence:
        if char == ' ':
            continue
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for char, count in counts.items():
        print(f'{char}: {count}')

    # The same loop written with get(), which removes the if/else:
    counts2: dict[str, int] = {}
    for char in sentence.replace(' ', ''):
        counts2[char] = counts2.get(char, 0) + 1

    print(counts2)

if __name__ == '__main__':
    main()
