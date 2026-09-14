# Every line read from a file ends with '\n'. strip() removes it
# (together with the spaces at both ends).
with open('numbers.txt', encoding='utf-8') as file:
    for line in file:
        clean = line.strip()
        if clean == '':          # skip the empty lines
            continue
        number = int(clean)
        print(number, number * 2)
