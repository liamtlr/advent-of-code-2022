with open('input_data.txt', 'r') as infile:
    input_data: list = infile.read().splitlines()[0]

    value = None

    for i in range(4, len(input_data)):
        checker = set(input_data[i-4:i])
        if len(checker) == 4:
            value = i
            break

    print(value)
